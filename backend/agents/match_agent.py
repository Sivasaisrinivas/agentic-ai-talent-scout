def run_match_agent(
candidate,
jd_analysis
):

    skills=jd_analysis["skills"]

    matches=[
      s for s in candidate["skills"]
      if s.lower() in skills
    ]

    score=(
      len(matches)/len(skills)
    )*100 if skills else 0

    return {
      "match_score":round(score,2),
      "matched_skills":matches,
      "reason":
      f"{len(matches)} skills aligned"
    }