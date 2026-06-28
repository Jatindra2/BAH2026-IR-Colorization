export default function Workflow() {

  const steps = [
    {
      no: "01",
      title: "Input",
      desc: "Upload a 200 m Thermal Infrared (TIR) satellite image."
    },
    {
      no: "02",
      title: "Super Resolution",
      desc: "Enhance the spatial resolution to 100 m using deep learning."
    },
    {
      no: "03",
      title: "AI Colorization",
      desc: "Generate realistic RGB imagery while preserving thermal information."
    },
    {
      no: "04",
      title: "Output",
      desc: "Download the enhanced high-resolution RGB satellite image."
    }
  ];

  return (

    <section className="section" id="workflow">

      <div className="container">

        <div className="section-title">
          <h2>Workflow</h2>

          <p>
            The complete processing pipeline transforms low-resolution thermal
            satellite imagery into realistic high-resolution RGB imagery using
            AI-powered enhancement and colorization.
          </p>

        </div>

        <div className="workflow-grid">

          {steps.map((step) => (

            <div className="workflow-card" key={step.no}>

              <span>{step.no}</span>

              <h3>{step.title}</h3>

              <p>{step.desc}</p>

            </div>

          ))}

        </div>

      </div>

    </section>

  );

}