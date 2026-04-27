def decision_agent(
match_score,
interest
):

    final_score=(
      match_score*.7+
      interest*.3
    )

    if final_score>90:
        verdict="Strong Hire"

    elif final_score>75:
        verdict="Interview"

    else:
        verdict="Low Priority"

    return {
      "final_score":
      round(final_score,2),
      "recommendation":
      verdict
    }