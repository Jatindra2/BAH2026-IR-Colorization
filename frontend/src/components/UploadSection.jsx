import { useState } from "react";
import { uploadImage } from "../services/api";

import "../styles/upload.css";

export default function UploadSection({
  setPrediction,
  setStatus,
  setError,
  error,
  status,
}) {
  const [file, setFile] = useState(null);
  const [dragActive, setDragActive] = useState(false);

  function validate(selectedFile) {
    if (!selectedFile) return false;

    if (!selectedFile.name.endsWith(".npy")) {
      setError("Only .npy files are supported.");
      return false;
    }

    setError("");
    return true;
  }

  function handleFile(selectedFile) {
    if (!validate(selectedFile)) return;

    setFile(selectedFile);
  }

  async function handlePredict() {
    if (!file) {
      setError("Please choose a .npy file.");
      return;
    }

    try {
      setStatus("uploading");

      const blob = await uploadImage(file);

      setStatus("processing");

      const imageURL = URL.createObjectURL(blob);

      setPrediction((previous) => {
        if (previous) URL.revokeObjectURL(previous);
        return imageURL;
      });

      setStatus("completed");

    } catch (err) {
      console.error(err);

      setStatus("error");

      setError(
        err?.response?.data?.detail ||
        "Prediction failed."
      );
    }
  }

  return (
    <section
      id="upload"
      className="section"
    >
      <div
        className={`upload-card ${
          dragActive ? "drag-active" : ""
        }`}
        onDragOver={(e) => {
          e.preventDefault();
          setDragActive(true);
        }}
        onDragLeave={() => setDragActive(false)}
        onDrop={(e) => {
          e.preventDefault();
          setDragActive(false);

          if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
          }
        }}
      >
        <h2>Upload Thermal Image</h2>

        <p>
          Upload a thermal infrared (.npy)
          satellite image.
        </p>

        {error && (
          <div className="error-box">
            {error}
          </div>
        )}

        <input
          type="file"
          accept=".npy"
          onChange={(e) =>
            handleFile(e.target.files[0])
          }
        />

        {file && (
          <div className="file-info">
            <strong>{file.name}</strong>

            <small>
              {(file.size / 1024).toFixed(2)} KB
            </small>
          </div>
        )}

        <button
            className="primary-btn"
            onClick={handlePredict}
            disabled={
                status === "uploading" ||
                status === "processing"
            }
        >
          Generate RGB Image
        </button>
      </div>
    </section>
  );
}