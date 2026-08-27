import { useState } from "react";
import {
  Upload,
  FileText,
  Search,
  CheckCircle,
  AlertTriangle,
  Lightbulb,
  Brain,
  Loader2,
} from "lucide-react";

function App() {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) return;

    if (file.type !== "application/pdf") {
      setError("Please upload a PDF resume.");
      setResume(null);
      return;
    }

    setResume(file);
    setError("");
    setResult(null);
  };

  const handleScreenResume = async () => {
    if (!resume) {
      setError("Please upload a resume PDF.");
      return;
    }

    if (!jobDescription.trim()) {
      setError("Please enter the job description.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const formData = new FormData();

      formData.append("resume", resume);
      formData.append("job_description", jobDescription);

      const response = await fetch(
        "http://127.0.0.1:8000/api/screen",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong.");
      }

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div className="logo">
          <Brain size={32} />
          <div>
            <h1>AI Resume Screener</h1>
            <p>AI-powered resume analysis</p>
          </div>
        </div>
      </header>

      {/* Main */}
      <main className="container">

        {/* Introduction */}
        <section className="hero">
          <h2>Find the Right Candidate Faster</h2>

          <p>
            Upload a resume and enter a job description to analyze
            candidate suitability using AI.
          </p>
        </section>

        {/* Input Section */}
        <section className="input-grid">

          {/* Resume Upload */}
          <div className="card">

            <div className="card-title">
              <FileText size={22} />
              <h3>Upload Resume</h3>
            </div>

            <label className="upload-box">

              <input
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
              />

              <Upload size={40} />

              {resume ? (
                <>
                  <strong>{resume.name}</strong>
                  <span>Resume selected successfully</span>
                </>
              ) : (
                <>
                  <strong>Upload your resume</strong>
                  <span>PDF files only</span>
                </>
              )}

            </label>

          </div>

          {/* Job Description */}
          <div className="card">

            <div className="card-title">
              <FileText size={22} />
              <h3>Job Description</h3>
            </div>

            <textarea
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="Enter the job description here..."
            />

          </div>

        </section>

        {/* Error */}
        {error && (
          <div className="error">
            <AlertTriangle size={20} />
            {error}
          </div>
        )}

        {/* Screen Button */}
        <button
          className="screen-button"
          onClick={handleScreenResume}
          disabled={loading}
        >

          {loading ? (
            <>
              <Loader2 className="spin" size={22} />
              Analyzing Resume...
            </>
          ) : (
            <>
              <Search size={22} />
              Screen Resume
            </>
          )}

        </button>

        {/* Results */}
        {result && (

          <section className="results">

            <h2>Screening Results</h2>

            {/* Score */}
            <div className="score-card">

              <div>
                <p>Resume Match Score</p>

                <strong>
                  {result.match_score}%
                </strong>
              </div>

              <div className="score-circle">
                {result.match_score}%
              </div>

            </div>

            {/* Strengths */}
            <div className="result-card">

              <div className="result-title">
                <CheckCircle size={24} />
                <h3>Strengths</h3>
              </div>

              <ul>
                {result.strengths?.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>

            </div>

            {/* Skill Gaps */}
            <div className="result-card">

              <div className="result-title">
                <AlertTriangle size={24} />
                <h3>Skill Gaps</h3>
              </div>

              <ul>
                {result.skill_gaps?.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>

            </div>

            {/* Reasoning */}
            <div className="result-card">

              <div className="result-title">
                <Brain size={24} />
                <h3>AI Reasoning</h3>
              </div>

              <p className="reasoning">
                {result.reasoning}
              </p>

            </div>

            {/* Recommendations */}
            <div className="result-card">

              <div className="result-title">
                <Lightbulb size={24} />
                <h3>Recommendations</h3>
              </div>

              <ul>
                {result.recommendations?.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>

            </div>

          </section>

        )}

      </main>

    </div>
  );
}

export default App;