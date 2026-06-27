# 🚀 IRVision AI

### AI-Powered Infrared Image Enhancement & Colorization for Improved Object Interpretation

> **Bharatiya Antariksh Hackathon (BAH) 2026 Submission**

---

# 📌 Problem Statement

**Problem Statement 10 – Infrared Image Colorization and Enhancement for Improved Object Interpretation**

The objective is to develop an end-to-end AI pipeline capable of:

- Enhancing low-resolution Thermal Infrared (TIR) satellite imagery
- Performing Super-Resolution from **200m → 100m**
- Colorizing Thermal Infrared imagery into realistic RGB images
- Improving object interpretation for downstream geospatial analysis

---

# ✨ Features

- Super-Resolution (200m → 100m)
- Thermal Infrared → RGB Colorization
- End-to-End AI Pipeline
- Automatic Model Checkpointing
- PSNR & SSIM Evaluation
- FastAPI Backend
- REST API
- Swagger Documentation
- Modular Training Framework
- Ready for React Frontend

---

# 🏗️ System Pipeline

```text
Landsat-9 Dataset
        │
        ▼
Dataset Validation
        │
        ▼
Preprocessing & Patch Generation
        │
        ▼
Super Resolution Model
(200m → 100m)
        │
        ▼
Colorization Model
(100m TIR → RGB)
        │
        ▼
Evaluation
(PSNR • SSIM)
        │
        ▼
FastAPI Backend
        │
        ▼
REST API
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
│   ├── exported/
│   └── weights/
├── backend/
├── baseline/
├── datasets/
├── docs/
├── evaluation/
├── frontend/
├── inference/
├── notebooks/
├── reports/
├── results/
├── tests/
├── training/
│   ├── colorization/
│   ├── super_resolution/
│   ├── configs/
│   ├── datasets/
│   ├── losses/
│   ├── models/
│   ├── trainers/
│   └── utils/
├── README.md
└── .gitignore
```

---

# 🛠 Tech Stack

## Machine Learning

- Python
- PyTorch
- segmentation-models-pytorch
- NumPy
- OpenCV
- Pillow

## Geospatial Data

- Rasterio
- tifffile
- Landsat-9 Collection-2

## Backend

- FastAPI
- Uvicorn

## Frontend (In Progress)

- React
- TypeScript
- Tailwind CSS

## Development

- Git
- GitHub

---

# 📊 Evaluation

Current evaluation metrics:

- PSNR
- SSIM

Average Results:

| Metric | Score |
|---------|------:|
| PSNR | **20.43 dB** |
| SSIM | **0.598** |

---

# 📈 Development Roadmap

| Milestone | Status |
|-----------|--------|
| ✅ Repository Setup | Complete |
| ✅ Official Baseline Integration | Complete |
| ✅ Dataset Preprocessing | Complete |
| ✅ Patch Generation | Complete |
| ✅ Dataset Loader | Complete |
| ✅ Super-Resolution Model | Complete |
| ✅ Super-Resolution Training | Complete |
| ✅ Colorization Model | Complete |
| ✅ Colorization Training | Complete |
| ✅ Automatic Checkpoint Saving | Complete |
| ✅ End-to-End Inference | Complete |
| ✅ Evaluation Pipeline | Complete |
| ✅ FastAPI Backend | Complete |
| ✅ REST API | Complete |
| ⏳ React Frontend | In Progress |
| ⏳ Docker Deployment | Pending |
| ⏳ Final Submission | Pending |

---

# 🎉 Latest Progress

Completed:

- ✅ Official BAH preprocessing integration
- ✅ Dataset loader
- ✅ Super-Resolution model
- ✅ Colorization model
- ✅ Training pipeline
- ✅ Automatic checkpoint saving
- ✅ End-to-End inference pipeline
- ✅ PSNR & SSIM evaluation
- ✅ FastAPI backend
- ✅ REST API
- ✅ Swagger API documentation

---

# 🚀 Running the Project

## Train Models

```bash
python training/train.py
```

## Run Evaluation

```bash
python evaluation/evaluate.py
```

## Run Inference

```bash
python inference/infer.py
```

## Start Backend

```bash
uvicorn backend.app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 📊 Current Status

| Module | Status |
|---------|--------|
| Dataset Pipeline | ✅ |
| Super Resolution | ✅ |
| Colorization | ✅ |
| Training | ✅ |
| Inference | ✅ |
| Evaluation | ✅ |
| FastAPI Backend | ✅ |
| REST API | ✅ |
| Swagger UI | ✅ |
| Frontend | ⏳ |
| Deployment | ⏳ |

---

# 🚀 Upcoming Work

- React Dashboard
- Docker Support
- Cloud Deployment
- Documentation
- Final Model Optimization
- Hackathon Submission

---

# 📜 License

This repository includes the official preprocessing baseline provided for the Bharatiya Antariksh Hackathon.

All AI models, training pipelines, inference modules, evaluation scripts, backend services, frontend components, and documentation are independently developed as part of our hackathon solution.

---

# ⭐ Project Progress

**Overall Completion:** **~95%**

**Status:** 🚀 Backend Complete | Frontend Under Development