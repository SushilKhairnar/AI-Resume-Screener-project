from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends

from ..database import get_db
from ..models import ResumeScreening
from ..services.pdf_service import extract_text_from_pdf
from ..services.llm_service import analyze_resume


router = APIRouter(
    prefix="/api",
    tags=["Resume Screening"]
)


@router.post("/screen")
async def screen_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    db: Session = Depends(get_db)
):

    # Check file type
    if resume.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    # Read uploaded PDF
    file_bytes = await resume.read()

    # Extract text from PDF
    resume_text = extract_text_from_pdf(file_bytes)

    if not resume_text:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from the PDF."
        )

    # Send resume + job description to Gemini
    try:
        analysis = analyze_resume(
            resume_text,
            job_description
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI analysis failed: {str(e)}"
        )

    # Save result in PostgreSQL
    screening = ResumeScreening(
        resume_filename=resume.filename,
        job_description=job_description,
        resume_text=resume_text,
        match_score=analysis["match_score"],
        strengths="\n".join(analysis["strengths"]),
        skill_gaps="\n".join(analysis["skill_gaps"]),
        reasoning=analysis["reasoning"],
        recommendations="\n".join(analysis["recommendations"])
    )

    db.add(screening)
    db.commit()
    db.refresh(screening)

    return {
        "id": screening.id,
        "resume_filename": screening.resume_filename,
        "match_score": screening.match_score,
        "strengths": analysis["strengths"],
        "skill_gaps": analysis["skill_gaps"],
        "reasoning": analysis["reasoning"],
        "recommendations": analysis["recommendations"]
    }