def outreach_agent(candidate):

    interest=candidate["interest"]

    if interest>90:
        response="""
Strong positive response.
Open to interview.
Salary flexible.
"""
    elif interest>75:
        response="""
Moderate interest.
Needs persuasion.
"""
    else:
        response="""
Passive candidate.
Low response probability.
"""

    return {
      "engagement_score":interest,
      "simulated_reply":response
    }