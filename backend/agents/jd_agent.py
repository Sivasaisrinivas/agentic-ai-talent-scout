def analyze_job_description(jd):

    extracted_skills=[]

    skills_bank=[
      "python",
      "fastapi",
      "aws",
      "microservices",
      "ai",
      "llm"
    ]

    for skill in skills_bank:
        if skill in jd.lower():
            extracted_skills.append(skill)

    return {
      "role_fit":"Senior Engineer",
      "skills":extracted_skills,
      "priority_skills":
      extracted_skills[:3],
      "market_difficulty":"Medium"
    }