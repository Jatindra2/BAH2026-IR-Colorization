import { useEffect, useState } from "react";

import "../styles/results.css";

export default function Results({
    prediction,
    status,
    error,
}) {

  const [visible, setVisible] = useState(false);

  useEffect(() => {
    if (prediction) {
      setVisible(true);
    }
  }, [prediction]);

  if (status === "error") {

    return (

        <section className="section">

            <div className="container">

                <div className="error-box">

                    <h3>Prediction Failed</h3>

                    <p>{error}</p>

                </div>

            </div>

        </section>

    );

}

if (!prediction) return null;

  return (
    <section className="section">

      <div className="container">

        <div className={`fade ${visible ? "show" : ""}`}>

          <h2 className="title">
            AI Prediction Results
          </h2>

          <p className="subtitle">
            Thermal infrared imagery has been enhanced
            using Super Resolution and AI Colorization.
          </p>

          <div className="success-box">
            ✅ RGB image generated successfully.
          </div>

          <div className="results-grid">

            <div className="result-card">

              <h3>Generated RGB Image</h3>

              <img
                src={prediction}
                alt="Prediction"
                className="result-image"
              />

            </div>

          </div>

          <div className="result-info">

            <div className="info-card">
              <h4>Output Format</h4>
              <p>PNG</p>
            </div>

            <div className="info-card">
              <h4>AI Pipeline</h4>
              <p>Super Resolution → Colorization</p>
            </div>

            <div className="info-card">
              <h4>Status</h4>
              <p>Completed</p>
            </div>

          </div>

          <div className="download-box">

            <a
              href={prediction}
              download="prediction.png"
            >
              <button className="primary-btn">
                ⬇ Download RGB Image
              </button>
            </a>

          </div>

        </div>

      </div>

    </section>
  );
}