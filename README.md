# 🚀 IRVision AI

### AI-Powered Thermal Infrared Image Enhancement & Colorization

**Bharatiya Antariksh Hackathon (BAH) 2026**

---

## 📖 Overview

**IRVision AI** is an end-to-end deep learning solution developed for the **Bharatiya Antariksh Hackathon (BAH) 2026**. The system enhances low-resolution Thermal Infrared (TIR) satellite imagery using Super-Resolution and converts grayscale thermal infrared images into realistic RGB images using deep learning.

The project provides a complete AI pipeline with:

* Deep Learning Models
* FastAPI Backend
* React Frontend
* End-to-End AI Inference
* Interactive Web Interface

Users can upload a thermal infrared satellite image (`.npy`), perform AI inference, and download the enhanced RGB image.

---

# 🎯 Problem Statement

### Problem Statement 10

**Infrared Image Colorization and Enhancement for Improved Object Interpretation**

The objective is to develop an AI system capable of:

* Enhancing low-resolution Thermal Infrared imagery
* Performing Super Resolution (200 m → 100 m)
* Colorizing thermal infrared images into realistic RGB images
* Improving object interpretation for remote sensing applications

---

# ✨ Features

## AI

* Thermal Infrared Image Enhancement
* Deep Learning Super Resolution
* AI-Based Image Colorization
* End-to-End Inference Pipeline
* Modular Model Architecture

## Backend

* FastAPI REST API
* Interactive Swagger Documentation
* Model Loading & Inference
* Image Validation
* Logging & Error Handling

## Frontend

* Modern React + Vite Interface
* Image Upload
* AI Processing
* Result Visualization
* Download Generated Images
* Responsive Design

---

# 🏗️ System Architecture

```text
               Thermal Image (.npy)
                        │
                        ▼
              Image Preprocessing
                        │
                        ▼
        Super Resolution Neural Network
                 (200 m → 100 m)
                        │
                        ▼
          AI Colorization Network
                        │
                        ▼
             Image Post Processing
                        │
                        ▼
                 RGB Output Image
                        │
                        ▼
                FastAPI Backend
                        │
                        ▼
               React Frontend
```

---

# 📂 Repository Structure

```text
BAH2026-IR-Colorization/

├── api/
├── artifacts/
│   ├── checkpoints/
│   └── exported/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── inference.py
│   ├── logger.py
│   ├── model_loader.py
│   ├── validators.py
│   ├── cleanup.py
│   └── requirements.txt
│
├── baseline/
├── datasets/
├── docs/
├── evaluation/
├── frontend/
├── notebooks/
├── reports/
├── results/
├── tests/
│
├── training/
│   ├── colorization/
│   ├── configs/
│   ├── datasets/
│   ├── losses/
│   ├── models/
│   ├── super_resolution/
│   ├── trainers/
│   └── utils/
│
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

## Artificial Intelligence

* Python
* PyTorch
* NumPy
* OpenCV
* Pillow

## Backend

* FastAPI
* Uvicorn

## Frontend

* React
* Vite
* Axios
* CSS

## Development

* Git
* GitHub

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/Jatindra2/BAH2026-IR-Colorization.git

cd BAH2026-IR-Colorization
```

---

## 2. Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn app:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger API:

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```
http://localhost:5173
```

---

# 📤 API Endpoint

## POST `/predict`

Upload a thermal infrared `.npy` file.

### Request

```
multipart/form-data

file: thermal_image.npy
```

### Response

```
PNG Image
```

---

# 📊 Evaluation

Current evaluation metrics include:

* PSNR (Peak Signal-to-Noise Ratio)
* SSIM (Structural Similarity Index)

Evaluation:

```bash
python evaluation/evaluate.py
```

---

# 🧠 AI Pipeline

```
Thermal Image
      │
      ▼
Normalization
      │
      ▼
Super Resolution Network
      │
      ▼
Colorization Network
      │
      ▼
RGB Image
```

---

# 📈 Current Project Status

| Module                    | Status         |
| ------------------------- | -------------- |
| Dataset Pipeline          | ✅ Complete     |
| Super Resolution Model    | ✅ Complete     |
| Colorization Model        | ✅ Complete     |
| Training Pipeline         | ✅ Complete     |
| Evaluation Pipeline       | ✅ Complete     |
| FastAPI Backend           | ✅ Complete     |
| REST API                  | ✅ Complete     |
| React Frontend            | ✅ Complete     |
| End-to-End Integration    | ✅ Complete     |
| Model Output Optimization | 🚧 In Progress |
| UI/UX Enhancement         | 🚧 In Progress |
| Docker Deployment         | ⏳ Planned      |
| Cloud Deployment          | ⏳ Planned      |

---

# 🎯 Future Improvements

* Improve AI colorization quality
* Train on larger thermal datasets
* Add side-by-side image comparison
* Drag-and-drop upload support
* Batch image inference
* Docker support
* Cloud deployment
* Model quantization for faster inference

---

# 🤝 Team

Developed as part of the **Bharatiya Antariksh Hackathon (BAH) 2026**.

---

# 📄 License

This repository includes the official preprocessing baseline provided for the Bharatiya Antariksh Hackathon.

The AI models, training pipeline, backend, frontend, inference system, and documentation have been developed as part of our hackathon solution.

Please follow the hackathon guidelines regarding the usage and redistribution of the provided baseline resources.

---

# ⭐ Acknowledgements

* Bharatiya Antariksh Hackathon (BAH) 2026
* PyTorch
* FastAPI
* React
* Vite
* OpenCV
* NumPy

---

## 🌟 If you found this project interesting, consider giving it a star on GitHub!
