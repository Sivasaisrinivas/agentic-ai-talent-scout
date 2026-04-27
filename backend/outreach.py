def simulate_outreach(candidate):

    score=candidate["interest"]

    if score>90:
        return "Highly Interested"

    if score>75:
        return "Warm Candidate"

    return "Passive Candidate"