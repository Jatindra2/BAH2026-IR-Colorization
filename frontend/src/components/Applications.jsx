export default function Applications() {
  const applications = [
    {
      title: "Disaster Management",
      desc: "Analyze thermal satellite imagery for wildfire monitoring, flood assessment, volcanic activity and emergency response."
    },
    {
      title: "Urban Heat Mapping",
      desc: "Visualize heat distribution across cities to support climate studies, smart city planning and infrastructure management."
    },
    {
      title: "Agriculture",
      desc: "Improve crop monitoring, irrigation planning and vegetation health analysis using enhanced thermal imagery."
    },
    {
      title: "Environmental Monitoring",
      desc: "Track forests, wetlands, water bodies and ecological changes using AI-enhanced satellite observations."
    }
  ];

  return (
    <section className="section" id="applications">
      <div className="container">

        <div className="section-title">
          <h2>Applications</h2>

          <p>
            IRVision AI enables enhanced thermal satellite imagery for multiple
            Earth observation applications.
          </p>
        </div>

        <div className="applications-grid">

          {applications.map((app, index) => (
            <div className="application-card" key={index}>
              <h3>{app.title}</h3>
              <p>{app.desc}</p>
            </div>
          ))}

        </div>

      </div>
    </section>
  );
}