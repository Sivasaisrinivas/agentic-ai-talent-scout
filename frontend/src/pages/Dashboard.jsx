import { useState } from "react";
import axios from "axios";
import CandidateCard from "../components/CandidateCard";

export default function Dashboard() {

    const [jd, setJD] = useState("");

    const [results, setResults] = useState([]);

    const [loading, setLoading] = useState(false);

    const [trace, setTrace] = useState([]);

    const analyzeCandidates = async () => {

        try {

            setLoading(true);

            const response = await axios.post(
                "http://127.0.0.1:8000/autonomous-agents",
                {
                    job_description: jd
                }
            );

            setTrace(
                response.data.workflow_trace
            );

            setResults(
                response.data.results
            );

        }
        catch (error) {
            console.error(error);
        }
        finally {
            setLoading(false);
        }

    }

    const clearResults = () => {
        setResults([]);
        setTrace([]);
        setJD("");
    }

    return (

        <div className="container">

            <h1>
                AI Talent Scouting Agent
            </h1>

            <textarea
                rows="8"
                value={jd}
                onChange={(e) =>
                    setJD(e.target.value)
                }
                placeholder="Paste Job Description..."
            />

            <button
                onClick={analyzeCandidates}
            >
                Analyze Candidates
            </button>
            &nbsp;&nbsp;&nbsp;&nbsp;
            <button
                onClick={clearResults}
            >
                Clear
            </button>

            {
                loading &&
                <p>Analyzing...</p>
            }

            <h2>Autonomous Agent Workflow</h2>

            {
                trace.map((step, i) => (
                    <div key={i}>
                        ✓ {step}
                    </div>
                ))
            }

            <div className="grid">
                {
                    results.map(candidate => (
                        <CandidateCard
                            key={candidate.id}
                            candidate={candidate}
                        />
                    ))
                }
            </div>

        </div>

    )

}