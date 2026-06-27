# 🚀 IRVision AI

### AI-Powered Infrared Image Enhancement & Colorization for Improved Object Interpretation

> **Bharatiya Antariksh Hackathon (BAH) 2026 Submission**

---

# 📌 Problem Statement

**Problem Statement 10 – Infrared Image Colorization and Enhancement for Improved Object Interpretation**

The objective is to develop an end-to-end AI pipeline capable of:

* Enhancing low-resolution Thermal Infrared (TIR) satellite imagery
* Performing Super-Resolution from **200m → 100m**
* Colorizing Thermal Infrared imagery into realistic RGB images
* Improving object interpretation for downstream geospatial analysis

---

# 🎯 Project Objectives

* Super-Resolution of Thermal Infrared imagery
* Thermal-to-RGB Colorization
* End-to-End AI Pipeline
* Quantitative Image Quality Evaluation
* FastAPI Backend
* Interactive Web Dashboard

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
(200m TIR → 100m TIR)
        │
        ▼
Colorization Model
(100m TIR → RGB)
        │
        ▼
Evaluation
(PSNR • SSIM • LPIPS • FID)
        │
        ▼
Inference API
        │
        ▼
Web Dashboard
```

---

# 📂 Repository Structure

```text
BAH2026-IR-Colorization/

├── api/
├── artifacts/
├── backend/
├── baseline/
├── docs/
├── evaluation/
├── frontend/
├── inference/
├── notebooks/
├── reports/
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
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

### Machine Learning

* Python
* PyTorch
* segmentation-models-pytorch
* NumPy
* OpenCV
* Pillow

### Data Processing

* tifffile
* Rasterio
* Landsat-9 Level-2 Dataset

### Backend (Planned)

* FastAPI

### Frontend (Planned)

* React
* TypeScript
* Tailwind CSS

### Development

* Git
* GitHub

---

# 📈 Development Roadmap

| Milestone                       | Status      |
| ------------------------------- | ----------- |
| ✅ Repository Setup              | Complete    |
| ✅ Official Baseline Integration | Complete    |
| ✅ Landsat Dataset Acquisition   | Complete    |
| ✅ Dataset Preprocessing         | Complete    |
| ✅ Patch Generation              | Complete    |
| ✅ PyTorch Dataset Loader        | Complete    |
| ✅ Super-Resolution Model        | Complete    |
| ✅ Super-Resolution Training     | Complete    |
| ✅ Colorization Model            | Complete    |
| ✅ Colorization Training         | Complete    |
| ✅ Automatic Checkpoint Saving   | Complete    |
| ⏳ End-to-End Inference Pipeline | In Progress |
| ⏳ Evaluation Metrics            | Planned     |
| ⏳ Backend API                   | Planned     |
| ⏳ Frontend Dashboard            | Planned     |
| ⏳ Final Deployment              | Planned     |

---

# 🎉 Latest Progress

### Completed

* Successfully integrated the official BAH baseline preprocessing pipeline.
* Generated aligned training patches from Landsat-9 imagery.
* Implemented a PyTorch Dataset Loader.
* Built a Super-Resolution network for **200m → 100m Thermal Infrared** enhancement.
* Trained the Super-Resolution model successfully.
* Implemented a Thermal-to-RGB Colorization network.
* Trained the Colorization model successfully.
* Implemented automatic checkpoint saving for both models.
* Created a modular training pipeline for future experimentation.

---

# 📊 Current Project Status

| Component            | Status        |
| -------------------- | ------------- |
| Dataset Pipeline     | ✅ Complete    |
| Super-Resolution     | ✅ Complete    |
| Colorization         | ✅ Complete    |
| Model Training       | ✅ Complete    |
| Checkpoint Saving    | ✅ Complete    |
| End-to-End Inference | ⏳ In Progress |
| Evaluation           | ⏳ Planned     |
| Backend              | ⏳ Planned     |
| Frontend             | ⏳ Planned     |

---

# 🚀 Upcoming Work

* End-to-End Inference Pipeline
* PSNR / SSIM / LPIPS / FID Evaluation
* FastAPI Backend
* React Dashboard
* Final Model Optimization
* Hackathon Submission

---

# 📜 License

This repository includes the official preprocessing baseline provided for the Bharatiya Antariksh Hackathon.

All AI models, training pipelines, inference modules, backend services, frontend components, and documentation are independently developed as part of our hackathon solution.

---

## ⭐ Current Progress

**Project Completion:** **~80%**

**Status:** 🚀 Active Development
