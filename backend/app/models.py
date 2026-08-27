from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func

from .database import Base


class ResumeScreening(Base):
    __tablename__ = "resume_screenings"

    id = Column(Integer, primary_key=True, index=True)

    resume_filename = Column(String(255), nullable=False)

    job_description = Column(Text, nullable=False)

    resume_text = Column(Text, nullable=False)

    match_score = Column(Float, nullable=False)

    strengths = Column(Text, nullable=True)

    skill_gaps = Column(Text, nullable=True)

    reasoning = Column(Text, nullable=True)

    recommendations = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )