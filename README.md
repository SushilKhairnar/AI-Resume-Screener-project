# AI Resume Screener

An AI-powered full-stack application that analyzes a candidate's resume against a job description and generates a resume match score along with detailed feedback.

## Live Demo

**Frontend:** https://ai-resume-screener-project-plum.vercel.app/

**Backend API / Swagger Documentation:** https://ai-resume-screener-project.onrender.com/docs

## Project Overview

The AI Resume Screener helps recruiters and candidates evaluate how well a resume matches a specific job description.

The user uploads a resume in PDF format and provides a job description. The application sends the information to the FastAPI backend, where the Gemini API analyzes the resume and job requirements. The system then generates a match score and feedback highlighting the candidate's strengths and areas for improvement.

##  Features

* Upload resume in PDF format
* Enter job description
* AI-powered resume analysis
* Generate resume-to-job match score
* Generate detailed feedback
* FastAPI REST API
* PostgreSQL database integration
* React-based frontend
* Responsive web interface
* Production deployment
* Separate frontend and backend deployment

##  Project Architecture

```text
User
  │
  ▼
React Frontend
(Vercel)
  │
  │ REST API
  ▼
FastAPI Backend
(Render)
  │
  ├──────────────► Gemini API
  │
  ▼
PostgreSQL Database
(Render)
```

##  Technologies Used

### Frontend

* React
* Vite
* JavaScript
* HTML
* CSS

### Backend

* Python
* FastAPI
* Uvicorn
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### AI

* Google Gemini API

### Deployment

* Vercel — Frontend
* Render — Backend and PostgreSQL

### Version Control

* Git
* GitHub

##  Project Structure

```text
AI-Resume-Screener-project/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── routes/
│   │       └── screening.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   └── ...
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
```

##  Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SushilKhairnar/AI-Resume-Screener-project.git
```

Navigate into the project:

```bash
cd AI-Resume-Screener-project
```

---

##  Backend Setup

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file inside the backend directory and add your own credentials:

```env
DATABASE_URL=your_postgresql_database_url
GEMINI_API_KEY=your_gemini_api_key
```

**Do not commit the `.env` file to GitHub.**

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

---

##  Frontend Setup

Open another terminal and navigate to the frontend:

```bash
cd frontend
```

Install Node.js dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

##  Frontend-Backend Connection

During local development, the React frontend communicates with:

```text
http://127.0.0.1:8000/api/screen
```

For production, the frontend communicates with the deployed Render backend:

```text
https://ai-resume-screener-project.onrender.com/api/screen
```

The production frontend is deployed on Vercel and the backend is deployed on Render.

##  Security

Sensitive credentials are stored using environment variables.

The following should never be pushed to GitHub:

* API keys
* Database passwords
* `.env` files
* Secret credentials

The `.gitignore` file is used to prevent sensitive and unnecessary files from being committed.

##  Deployment

### Frontend

The React frontend is deployed using **Vercel**.

Live application:

https://ai-resume-screener-project-plum.vercel.app/

### Backend

The FastAPI backend is deployed using **Render**.

Backend:

https://ai-resume-screener-project.onrender.com/

Swagger documentation:

https://ai-resume-screener-project.onrender.com/docs

### Database

PostgreSQL is hosted on Render and connected to the FastAPI backend using SQLAlchemy.

## Application Workflow

1. User opens the web application.
2. User uploads a resume PDF.
3. User enters the job description.
4. React sends the resume and job description to the FastAPI backend.
5. FastAPI processes the request.
6. The Gemini API analyzes the resume against the job description.
7. The application generates a match score and feedback.
8. The result is displayed on the React frontend.
9. Relevant screening information can be stored in PostgreSQL.

##  API Endpoint

### Screen Resume

```text
POST /api/screen
```

This endpoint receives the resume and job description and returns the AI-generated screening result.

### Health Check

```text
GET /health
```

Returns the health status of the backend.

##  Future Improvements

* User authentication and authorization
* Resume history dashboard
* Multiple resume comparison
* Recruiter dashboard
* Advanced candidate ranking
* Job description recommendations
* Improved resume parsing
* Analytics and reporting

##  Author

**Sushil Khairnar**

GitHub:

https://github.com/SushilKhairnar/AI-Resume-Screener-project
