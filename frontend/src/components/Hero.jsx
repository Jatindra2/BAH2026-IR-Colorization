import heroBg from "../assets/hero-bg.png";

export default function Hero() {
  return (
    <section className="hero section" id="hero">
      <div className="container hero-container">

        <div className="hero-left fade">

          <span className="hero-badge">
            Bhartiya Antariksh Hackathon 2026
          </span>

          <h1>
            AI-Powered
            <br />
            Thermal Infrared
            <br />
            Image Enhancement
          </h1>

          <p>
            Transform low-resolution thermal infrared satellite imagery into
            high-resolution realistic RGB images using deep learning for better
            Earth observation and analysis.
          </p>

          <div className="hero-buttons">

            <a href="#upload" className="primary-btn">
              Upload Image
            </a>

            <a href="#about" className="secondary-btn">
              Learn More
            </a>

          </div>

        </div>

        <div className="hero-right fade">

          <img
            src={heroBg}
            alt="Thermal Preview"
          />

        </div>

      </div>
    </section>
  );
}