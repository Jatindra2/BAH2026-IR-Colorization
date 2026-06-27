# 🚀 IRVision AI

> **AI-Powered Thermal Infrared Image Enhancement & Colorization**
> **Bharatiya Antariksh Hackathon (BAH) 2026**

---

## 📖 Overview

**IRVision AI** is an end-to-end deep learning solution developed for the **Bharatiya Antariksh Hackathon (BAH) 2026**. The system enhances low-resolution Thermal Infrared (TIR) satellite imagery using Super-Resolution and converts grayscale thermal images into realistic RGB images using deep learning.

The platform provides an intuitive web interface where users can upload thermal images, perform AI inference, and download the generated colorized results.

---

# 🎯 Problem Statement

**Problem Statement 10 – Infrared Image Colorization and Enhancement for Improved Object Interpretation**

The objective is to develop an AI pipeline capable of:

* Enhancing low-resolution Thermal Infrared (TIR) satellite imagery.
* Performing Super-Resolution from **200 m → 100 m**.
* Colorizing thermal infrared imagery into realistic RGB images.
* Improving object interpretation for downstream geospatial applications.

---

# ✨ Features

* AI-based Thermal Image Colorization
* Super-Resolution (200 m → 100 m)
* End-to-End Deep Learning Pipeline
* Automated Training Pipeline
* PSNR & SSIM Evaluation
* FastAPI REST Backend
* Interactive Swagger API Documentation
* Modern React Frontend
* Image Upload & AI Inference
* Download Generated RGB Images
* Modular Project Structure

---

# 🏗️ System Pipeline

```text
Thermal Infrared Image
          │
          ▼
Image Preprocessing
          │
          ▼
Super Resolution Model
     (200m → 100m)
          │
          ▼
RGB Colorization Model
          │
          ▼
Post Processing
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

├── backend/
├── evaluation/
├── frontend/
├── inference/
├── training/
│   ├── colorization/
│   ├── super_resolution/
│   ├── configs/
│   ├── datasets/
│   ├── losses/
│   ├── models/
│   ├── trainers/
│   └── utils/
├── baseline/
├── artifacts/
├── datasets/
├── docs/
├── README.md
└── .gitignore
```

---

# 🛠 Tech Stack

### Artificial Intelligence

* Python
* PyTorch
* segmentation-models-pytorch
* NumPy
* OpenCV
* Pillow

### Backend

* FastAPI
* Uvicorn

### Frontend

* React
* Vite
* Axios
* CSS

### Development

* Git
* GitHub

---

# 📊 Evaluation

Current evaluation metrics:

* PSNR
* SSIM

Evaluation pipeline:

```bash
python evaluation/evaluate.py
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/Jatindra2/BAH2026-IR-Colorization.git

cd BAH2026-IR-Colorization
```

---

## Backend

```bash
uvicorn backend.app:app --reload
```

Backend:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Frontend

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

## Training

```bash
python training/train.py
```

---

## Inference

```bash
python inference/infer.py
```

---

## Evaluation

```bash
python evaluation/evaluate.py
```

---

# 📊 Project Status

| Module                 | Status         |
| ---------------------- | -------------- |
| Dataset Pipeline       | ✅ Complete     |
| Super-Resolution       | ✅ Complete     |
| Colorization           | ✅ Complete     |
| Training Pipeline      | ✅ Complete     |
| Inference Pipeline     | ✅ Complete     |
| Evaluation             | ✅ Complete     |
| FastAPI Backend        | ✅ Complete     |
| REST API               | ✅ Complete     |
| Swagger Documentation  | ✅ Complete     |
| React Frontend         | ✅ Complete     |
| End-to-End Integration | ✅ Complete     |
| UI Enhancement         | 🚧 In Progress |
| Model Optimization     | 🚧 In Progress |
| Deployment             | ⏳ Pending      |

---

# 🎯 Upcoming Improvements

* Modern UI/UX redesign
* Drag & Drop Upload
* Before/After Image Comparison
* Improved AI Processing Experience
* Training on Larger Thermal Datasets
* Higher PSNR & SSIM Performance
* Docker Support
* Cloud Deployment
* Final Hackathon Submission

---

# 📜 License

This repository includes the official preprocessing baseline provided for the Bharatiya Antariksh Hackathon.

The AI models, training pipeline, inference pipeline, evaluation framework, backend services, frontend application, and documentation have been developed as part of our hackathon solution.

---

# 👥 Team

Developed for **Bharatiya Antariksh Hackathon (BAH) 2026**

---

## ⭐ Project Progress

**Overall Completion:** **96%**

**Current Focus:** UI/UX Redesign • Model Optimization • Dataset Expansion
