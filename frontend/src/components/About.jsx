export default function About() {
  const features = [
    {
      title: "Super Resolution",
      text: "Enhances 200 m thermal infrared imagery into detailed 100 m resolution while preserving important structural information.",
    },
    {
      title: "AI Colorization",
      text: "Generates realistic RGB satellite imagery from single-channel thermal infrared inputs using deep learning.",
    },
    {
      title: "Earth Observation",
      text: "Improves interpretation of thermal satellite data for monitoring cities, agriculture, forests and environmental changes.",
    },
  ];

  return (
    <section className="section" id="about">
      <div className="container">

        <div className="section-title">
          <h2>About the Project</h2>
          <p>
            IRVision AI is an end-to-end framework developed for the
            Bhartiya Antariksh Hackathon 2026 to enhance thermal satellite
            imagery through super-resolution and AI-driven colorization.
          </p>
        </div>

        <div className="about-grid">
          {features.map((item, index) => (
            <div className="feature-card" key={index}>
              <h3>{item.title}</h3>
              <p>{item.text}</p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}