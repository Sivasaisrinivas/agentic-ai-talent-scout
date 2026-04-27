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

# Tech Stack

## Frontend
- React
- Vite
- Axios
- React Router

## Backend
- Python
- FastAPI
- Uvicorn

---

# Repository Structure

```bash
ai-talent-scout/
├── frontend/
├── backend/
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

# Prerequisites

Install first:

- Node.js 18+
- npm
- Python 3.10+

Check:

```bash
node -v
npm -v
python --version
```

---

# Step 1 Install Root Dependency (Concurrently)

Install root dependencies:

```bash
npm install
```

If needed manually install concurrently:

```bash
npm install concurrently --save-dev
```

Verify:

```bash
npx concurrently --version
```

---

# Step 2 Install Frontend Dependencies (Vite + React Packages)

```bash
cd frontend
npm install
```

Verify Vite:

```bash
npx vite --version
```

Back to root:

```bash
cd ..
```

---

# Step 3 Install Python Backend Dependencies

```bash
cd backend
python -m pip install -r requirements.txt
```

Windows:

```bash
py -m pip install -r requirements.txt
```

Verify:

```bash
python -m uvicorn --version
```

Back to root:

```bash
cd ..
```

---

# One Command Run

Start frontend + backend together:

```bash
npm run dev
```

Runs:

- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- Swagger: http://localhost:8000/docs

---

# Root package.json

```json
{
  "name": "ai-talent-scout",
  "private": true,
  "scripts": {
    "frontend": "cd frontend && npm run dev",
    "backend": "cd backend && python -m uvicorn app:app --reload",

    "dev": "npx concurrently \"npm run backend\" \"npm run frontend\"",

    "install:frontend": "cd frontend && npm install",
    "install:backend": "cd backend && python -m pip install -r requirements.txt",

    "postinstall": "npm run install:frontend && npm run install:backend"
  },
  "devDependencies": {
    "concurrently": "^9.0.0"
  }
}
```

---

# First Time Setup (Recommended)

Run in order:

```bash
npm install

cd frontend
npm install
cd ..

cd backend
python -m pip install -r requirements.txt
cd ..

npm run dev
```

---

# requirements.txt

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

Example:

```env
OPENAI_API_KEY=replace_me
```

Never commit real secrets.

---

# API Endpoints

## Candidate Ranking

```http
POST /rank
```

## Autonomous Agents

```http
POST /autonomous-agents
```

## LLM Agents

```http
POST /llm-agents
```

Example payload:

```json
{
 "job_description":"Python FastAPI AWS engineer"
}
```

---

# Frontend Environment

Create:

```bash
frontend/.env
```

```env
VITE_API_URL=http://localhost:8000
```

---

# Demo Workflow

1. Recruiter pastes Job Description

2. Planner Agent builds execution graph

3. Agents:
- Analyze JD
- Rank candidates
- Generate outreach
- Produce shortlist

4. Recruiter gets explainable recommendations

---

# Future Improvements

- Real LangGraph implementation
- Resume embeddings + FAISS
- RAG talent search
- LinkedIn enrichment
- CrewAI agents

---

# Deployment

## Backend (Render)

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 10000
```

## Frontend (Vercel)

```bash
vercel
```

---

# Git Push

```bash
git init
git add .
git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/yourusername/agentic-ai-talent-scout.git

git push -u origin main
```

---

# GitHub Topics

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

# Troubleshooting

## concurrently not recognized

```bash
npm install concurrently --save-dev
```

---

## vite not recognized

```bash
cd frontend
npm install
```

---

## uvicorn not recognized

```bash
cd backend
python -m pip install -r requirements.txt
```

Use:

```bash
python -m uvicorn app:app --reload
```

instead of plain:

```bash
uvicorn app:app --reload
```
