import { useState } from "react";

const API = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export default function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyze = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const res = await fetch(`${API}/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      if (!res.ok) throw new Error();
      setResult(await res.json());
    } catch {
      setError("Could not reach the API");
    }
    setLoading(false);
  };

  return (
    <div className="card">
      <h1>AI Sentiment Analyzer</h1>
      <p className="sub">Type a sentence and the model predicts its sentiment.</p>
      <textarea
        rows={4}
        placeholder="Type a sentence..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={analyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
      {error && <p className="error">{error}</p>}
      {result && (
        <div className={`result ${result.label.toLowerCase()}`}>
          {result.label} ({result.confidence}%)
          <div className="bar">
            <div style={{ width: `${result.confidence}%` }} />
          </div>
        </div>
      )}
    </div>
  );
}