from agents.jd_agent import analyze_job_description
from agents.match_agent import run_match_agent
from agents.outreach_agent import outreach_agent
from agents.decision_agent import decision_agent

from candidates import candidates


def planner_agent(state):

    state["trace"].append(
      "Planner created workflow"
    )

    state["plan"]=[
      "Parse JD",
      "Match Candidates",
      "Simulate Outreach",
      "Make Decisions"
    ]

    return state


def jd_agent(state):

    analysis=analyze_job_description(
      state["job_description"]
    )

    state["jd_analysis"]=analysis

    state["trace"].append(
      "JD Agent completed"
    )

    return state


def candidate_agent(state):

    results=[]

    for c in candidates:

        match=run_match_agent(c,state["jd_analysis"])

        results.append({
          **c,
          **match
        })

    state["candidates"]=results

    state["trace"].append(
      "Candidate Agent ranked talent"
    )

    return state


def outreach_node(state):

    enriched=[]

    for c in state["candidates"]:

        outreach=outreach_agent(c)

        enriched.append({
           **c,
           **outreach
        })

    state["candidates"]=enriched

    state["trace"].append(
      "Outreach Agent simulated conversations"
    )

    return state


def decision_node(state):

    final=[]

    for c in state["candidates"]:

        decision=decision_agent(
           c["match_score"],
           c["interest"]
        )

        final.append({
           **c,
           **decision
        })

    final=sorted(
      final,
      key=lambda x:
      x["final_score"],
      reverse=True
    )

    state["results"]=final

    state["trace"].append(
      "Decision Agent finalized shortlist"
    )

    return state


def run_graph(job_description):

    state={
      "job_description":job_description,
      "trace":[]
    }

    state=planner_agent(state)
    state=jd_agent(state)
    state=candidate_agent(state)
    state=outreach_node(state)
    state=decision_node(state)

    return state