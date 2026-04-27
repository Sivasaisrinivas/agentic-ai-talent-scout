def extract_skills(jd):

    skills=[
      "python",
      "fastapi",
      "aws",
      "microservices",
      "java",
      "spring",
      "ai"
    ]

    return [
      s for s in skills
      if s in jd.lower()
    ]


def score_candidate(candidate,jd_skills):

    matched=[
      skill for skill in candidate["skills"]
      if skill.lower() in jd_skills
    ]

    if not jd_skills:
        match_score=0
    else:
        match_score=(
            len(matched)/
            len(jd_skills)
        )*100

    interest_score=candidate["interest"]

    final_score=(
       match_score*0.7 +
       interest_score*0.3
    )

    return {
      "match_score":round(match_score,2),
      "interest_score":interest_score,
      "final_score":round(final_score,2),
      "matched_skills":matched
    }