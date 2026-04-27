export default function CandidateCard({ candidate }) {

    return (
        <div className="candidate-card">

            <h2>{candidate.name}</h2>

            <p>
                Experience:
                {candidate.experience} years
            </p>

            <p>
                Match Score:
                {candidate.match_score}%
            </p>

            <p>
                Interest:
                {candidate.interest_score}%
            </p>

            <p>
                Final Score:
                {candidate.final_score}
            </p>

            <p>
                Outreach:
                {candidate.outreach}
            </p>

            <p>
                Recommendation:
                {candidate.recommendation}
            </p>

            <p>
                Reason:
                {candidate.reason}
            </p>

            <p>
                AI Outreach:
                {candidate.simulated_reply}
            </p>

            <h4>Matched Skills</h4>

            <ul>
                {
                    candidate.matched_skills.map(
                        (skill, index) => (
                            <li key={index}>
                                {skill}
                            </li>
                        ))
                }
            </ul>

        </div>
    )

}