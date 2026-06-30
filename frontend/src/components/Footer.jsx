export default function Footer() {
  return (
    <footer style={{
      background: "var(--bg-light)",
      borderTop: "1px solid var(--border)",
      padding: "40px 0",
      marginTop: "80px",
      transition: "var(--transition)"
    }}>
      <div className="container" style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: "20px",
        textAlign: "center"
      }}>
        <div style={{
          fontSize: "1.2rem",
          fontWeight: "700",
          color: "var(--text)"
        }}>
          🛰️ Team <span style={{ color: "var(--primary)" }}>IRVision</span>
        </div>

        <p style={{
          color: "var(--text-light)",
          fontSize: "0.95rem",
          maxWidth: "500px",
          lineHeight: "1.6",
          margin: "0"
        }}>
          Enhancing thermal satellite imagery details through state-of-the-art Super-Resolution and LAB-space AI Colorization networks.
        </p>

        <div style={{
          display: "flex",
          gap: "30px",
          flexWrap: "wrap",
          justifyContent: "center",
          fontSize: "0.9rem",
          fontWeight: "500",
          color: "var(--text-light)"
        }}>
          <div>
            <strong>GitHub:</strong>{" "}
            <a 
              href="https://github.com/Jatindra2" 
              target="_blank" 
              rel="noreferrer"
              style={{ color: "var(--primary)", transition: "var(--transition)" }}
              onMouseOver={(e) => e.target.style.color = "var(--primary-dark)"}
              onMouseOut={(e) => e.target.style.color = "var(--primary)"}
            >
              Jatindra2
            </a>
          </div>

          <div>
            <strong>Email:</strong>{" "}
            <a 
              href="mailto:jatindra2005@gmail.com"
              style={{ color: "var(--primary)", transition: "var(--transition)" }}
              onMouseOver={(e) => e.target.style.color = "var(--primary-dark)"}
              onMouseOut={(e) => e.target.style.color = "var(--primary)"}
            >
              jatindra2005@gmail.com
            </a>
          </div>
        </div>

        <div style={{
          fontSize: "0.8rem",
          color: "var(--text-light)",
          opacity: 0.6,
          marginTop: "10px"
        }}>
          © {new Date().getFullYear()} Team IRVision. All rights reserved.
        </div>
      </div>
    </footer>
  );
}