import logo from "../assets/logo.png";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="container nav-container">

        <div className="logo">
          <img src={logo} alt="IRVision AI" />
          <span>
            IRVision <span style={{ color: "var(--primary)" }}>AI</span>
          </span>
        </div>

        <nav>
          <a href="#hero">Home</a>
          <a href="#workflow">Workflow</a>
          <a href="#upload">Upload</a>
          <a href="#applications">Applications</a>
        </nav>

        <a
          className="github-btn"
          href="https://github.com/Jatindra2/BAH2026-IR-Colorization"
          target="_blank"
          rel="noreferrer"
        >
          GitHub
        </a>

      </div>
    </header>
  );
}