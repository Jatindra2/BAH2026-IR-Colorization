import { useState } from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import About from "./components/About";
import Workflow from "./components/Workflow";
import UploadSection from "./components/UploadSection";
import Processing from "./components/Processing";
import Results from "./components/Results";
import Applications from "./components/Applications";
import Footer from "./components/Footer";

import "./index.css";

function App() {
  const [prediction, setPrediction] = useState(null);
  const [status, setStatus] = useState("idle");
  const [error, setError] = useState("");

  return (
    <>
      <Navbar />
      <Hero />
      <About />
      <Workflow />

      <UploadSection
        setPrediction={setPrediction}
        setStatus={setStatus}
        setError={setError}
        error={error}
        status={status}
      />

      <Processing status={status} />

      <Results
        prediction={prediction}
        status={status}
        error={error}
      />

      <Applications />
      <Footer />
    </>
  );
}

export default App;