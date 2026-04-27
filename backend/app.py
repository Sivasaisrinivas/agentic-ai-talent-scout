from fastapi import FastAPI
from pydantic import BaseModel

from candidates import candidates
from scoring import extract_skills,score_candidate
from outreach import simulate_outreach
from fastapi.middleware.cors import CORSMiddleware

from agents.jd_agent import analyze_job_description
from agents.match_agent import run_match_agent
from agents.outreach_agent import outreach_agent
from agents.decision_agent import decision_agent

from agents.langgraph_workflow import run_graph

app=FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

class JobRequest(BaseModel):
    job_description:str

@app.get("/")
def home():
    return {
      "message":"AI Talent Scout API Running"
    }


@app.post("/rank")
def rank(req:JobRequest):

    jd_skills=extract_skills(
      req.job_description
    )

    results=[]

    for c in candidates:

        score=score_candidate(
          c,
          jd_skills
        )

        results.append({
           **c,
           **score,
           "outreach":
           simulate_outreach(c)
        })

    ranked=sorted(
      results,
      key=lambda x:
      x["final_score"],
      reverse=True
    )

    return ranked
    
@app.post("/agent-workflow")
def run_agents(req:JobRequest):

    jd_analysis=analyze_job_description(req.job_description)

    ranked=[]

    for c in candidates:

        match=run_match_agent(c,jd_analysis)

        outreach=outreach_agent(c)

        decision=decision_agent(match["match_score"],c["interest"])

        ranked.append({
          "candidate":c["name"],
          **match,
          **outreach,
          **decision
        })

    ranked=sorted(
      ranked,
      key=lambda x:
      x["final_score"],
      reverse=True
    )

    return {
      "agent_pipeline":[
        "JD Agent",
        "Match Agent",
        "Outreach Agent",
        "Decision Agent"
      ],
      "results":ranked
    }

@app.post("/autonomous-agents")
def autonomous_agents(req:JobRequest):

    state=run_graph(req.job_description)

    return {
      "workflow_trace":
      state["trace"],
      "results":
      state["results"]
    }
