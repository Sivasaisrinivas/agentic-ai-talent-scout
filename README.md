# AI Talent Scouting Agent 🚀

![Python](https://img.shields.io/badge/Python-FastAPI-blue)
![React](https://img.shields.io/badge/React-Vite-61dafb)
![Hackathon](https://img.shields.io/badge/Built%20For-Hackathon-purple)

An autonomous **AI recruiting copilot** where specialized agents collaborate through shared graph state to source, evaluate, engage and prioritize candidates.

---

# Elevator Pitch

Traditional ATS systems do keyword matching.

This platform uses:

- Autonomous multi-agent orchestration
- LLM-powered reasoning
- Candidate ranking
- AI-generated outreach
- Explainable hiring recommendations

Think **LangGraph + Recruiter Copilot + Talent Intelligence**.

---

# Features

| Feature | Status |
|--------|--------|
| Candidate Matching | ✅ |
| Multi-Agent Workflow | ✅ |
| AI Outreach Messages | ✅ |
| Explainable Decisions | ✅ |
| Autonomous Agent Trace | ✅ |
| FastAPI Swagger APIs | ✅ |

---

# Multi-Agent Workflow

```text
START
 ↓
Planner Agent
 ↓
JD Intelligence Agent
 ↓
Candidate Match Agent
 ↓
Outreach Agent
 ↓
Decision Agent
 ↓
END
```

Autonomous workflow traces are visible in the UI.

---

# Architecture

```text
React Frontend
   ↓
FastAPI Backend
   ↓
Planner Agent
├── JD Agent
├── Candidate Match Agent
├── Outreach Agent
└── Decision Agent
   ↓
OpenAI / LLM
```

---

# Screenshots

Add screenshots inside:

```bash
screenshots/
```

Example:

```md
## Dashboard
![Dashboard](screenshots/dashboard.png)

## Agent Workflow
![Workflow](screenshots/agent-workflow.png)

## Candidate Ranking
![Ranking](screenshots/candidate-ranking.png)
```

---

# Demo Video

Add Loom/Youtube demo link:

```text
https://loom.com/your-demo-link
```

---

# Tech Stack

## Frontend
- React
- Vite
- Axios
- React Router
- TailwindCSS (optional)

## Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

---

# Repository Structure

```bash
ai-talent-scout/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── .env.example
│
├── backend/
│   ├── agents/
│   │   ├── jd_agent.py
│   │   ├── match_agent.py
│   │   ├── outreach_agent.py
│   │   ├── decision_agent.py
│   │   └── langgraph_workflow.py
│   │
│   ├── app.py
│   ├── ai_agent.py
│   ├── candidates.py
│   ├── requirements.txt
│   └── .env.example
│
├── screenshots/
├── .gitignore
├── package.json
└── README.md
```

---

# Quick Start

Clone repository:

```bash
git clone https://github.com/yourusername/agentic-ai-talent-scout.git

cd agentic-ai-talent-scout
```

---

# One Command Startup (Frontend + Backend)

Install root dependency:

```bash
npm install
```

Run entire stack:

```bash
npm run dev
```

Starts:

- React frontend
- FastAPI backend

Single command launches full stack.

---

# Root package.json

```json
{
 "scripts": {
   "frontend":"npm --prefix frontend run dev",
   "backend":"python -m uvicorn backend.app:app --reload",
   "dev":"concurrently \"npm run backend\" \"npm run frontend\""
 }
}
```

---

# Backend Setup

```bash
cd backend

python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

---

## requirements.txt

```txt
fastapi
uvicorn
python-dotenv
openai
python-multipart
```

---

# OpenAI API Setup

Create:

```bash
backend/.env
```

Add:

```env
OPENAI_API_KEY=your_api_key_here
```

Example file committed:

```bash
backend/.env.example
```

```env
OPENAI_API_KEY=replace_me
```

Never commit real `.env`.

---

# Run Backend Only

```bash
uvicorn app:app --reload
```

Swagger:

```text
http://localhost:8000/docs
```

---

# API Endpoints

## Candidate Ranking

```http
POST /rank
```

---

## Autonomous Agents

```http
POST /autonomous-agents
```

---

## LLM Agents

```http
POST /llm-agents
```

Payload:

```json
{
 "job_description":"Python FastAPI AWS engineer"
}
```

---

# Frontend Setup (Optional Separate)

```bash
cd frontend
npm install
npm run dev
```

Runs:

```text
http://localhost:5173
```

---

## Frontend Environment

Create:

```bash
frontend/.env
```

```env
VITE_API_URL=http://localhost:8000
```

---

# Demo Workflow

1 Recruiter pastes Job Description

2 Planner agent builds execution plan

3 AI agents:
- Analyze JD
- Rank candidates
- Simulate outreach
- Generate shortlist

4 Recruiter receives explainable recommendations

---

# Future Improvements

- Real LangGraph implementation
- Resume embeddings + FAISS
- LinkedIn enrichment
- Email outreach automation
- Supervisor routing agents
- RAG talent search
- CrewAI agents

---

# Why This Is Different

Traditional ATS:
- Boolean keyword search
- Manual screening

This System:
- Autonomous agents
- LLM reasoning
- Explainability
- AI outreach
- Talent intelligence

---

# Deployment

## Backend (Render)

Build:

```bash
pip install -r requirements.txt
```

Start:

```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

---

## Frontend (Vercel)

```bash
vercel
```

---

# GitHub Topics

Suggested tags:

```text
ai
agents
fastapi
react
openai
langgraph
hackathon
genai
recruiting
```

---

# Git Push

```bash
git init
git add .
git commit -m "Initial commit"

git remote add origin https://github.com/yourusername/agentic-ai-talent-scout.git

git push -u origin main
```

---

# Demo GIF (Optional)

Add:

```md
![Demo](demo.gif)
```
