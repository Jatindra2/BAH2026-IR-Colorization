import { useState, useEffect } from "react";
import logo from "../assets/logo.png";

export default function Navbar() {
  const [isLightMode, setIsLightMode] = useState(false);

  useEffect(() => {
    // Check initial state
    const hasLightClass = document.documentElement.classList.contains("light-mode");
    setIsLightMode(hasLightClass);
  }, []);

  const toggleTheme = () => {
    const nextMode = !isLightMode;
    setIsLightMode(nextMode);
    if (nextMode) {
      document.documentElement.classList.add("light-mode");
    } else {
      document.documentElement.classList.remove("light-mode");
    }
  };

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

        <div style={{ display: "flex", alignItems: "center", gap: "15px" }}>
          <button 
            onClick={toggleTheme} 
            className="theme-toggle-btn"
            title={isLightMode ? "Switch to Dark Mode" : "Switch to Light Mode"}
          >
            {isLightMode ? "🌙" : "☀️"}
          </button>

          <a
            className="github-btn"
            href="https://github.com/Jatindra2/BAH2026-IR-Colorization"
            target="_blank"
            rel="noreferrer"
          >
            GitHub
          </a>
        </div>

      </div>
    </header>
  );
}