# 🚀 IRVision AI

### AI-Powered Infrared Image Enhancement & Colorization for Improved Object Interpretation

> Bharatiya Antariksh Hackathon (BAH) 2026 Submission

---

## 📌 Problem Statement

**Problem Statement 10 – Infrared Image Colorization and Enhancement for Improved Object Interpretation**

Develop an end-to-end AI pipeline capable of:

* Enhancing low-resolution thermal infrared (TIR) satellite imagery.
* Performing super-resolution from **200m → 100m**.
* Colorizing thermal images into realistic RGB representations.
* Improving interpretation for downstream analysis and decision-making.

---

# 🎯 Objectives

* Develop a Super-Resolution model for thermal infrared imagery.
* Develop a Thermal-to-RGB Colorization model.
* Build a scalable AI training pipeline.
* Create a production-ready inference API.
* Develop an interactive web dashboard for image processing and visualization.
* Generate evaluation reports using quantitative image quality metrics.

---

# 🏗️ Project Architecture

```text
Landsat Dataset
        │
        ▼
Dataset Validation
        │
        ▼
Patch Generation
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
(FastAPI)
        │
        ▼
React Dashboard
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
│   ├── configs/
│   ├── datasets/
│   ├── losses/
│   ├── models/
│   ├── super_resolution/
│   ├── trainers/
│   └── utils/
└── README.md
```

---

# 🛠️ Tech Stack

### AI & Machine Learning

* Python
* PyTorch
* NumPy
* OpenCV
* Pillow
* tifffile

### Backend

* FastAPI

### Frontend

* React
* TypeScript
* Tailwind CSS

### Development

* Git
* GitHub
* Docker (planned)

---

# 📈 Development Roadmap

* ✅ Milestone 1 – Repository Setup & Baseline Integration
* ✅ Milestone 2 – Project Architecture
* ⏳ Milestone 3 – Dataset Acquisition & Validation
* ⏳ Milestone 4 – Super-Resolution Model
* ⏳ Milestone 5 – Colorization Model
* ⏳ Milestone 6 – Model Evaluation
* ⏳ Milestone 7 – Backend API
* ⏳ Milestone 8 – Frontend Dashboard
* ⏳ Milestone 9 – Deployment & Final Submission

---

# 📊 Current Progress

| Module                 | Status        |
| ---------------------- | ------------- |
| Repository Setup       | ✅ Complete    |
| Baseline Integration   | ✅ Complete    |
| Project Architecture   | ✅ Complete    |
| Dataset Preparation    | ⏳ In Progress |
| Super-Resolution Model | ⏳ Planned     |
| Colorization Model     | ⏳ Planned     |
| Backend API            | ⏳ Planned     |
| Frontend Dashboard     | ⏳ Planned     |

---

# 📜 License

This repository includes the official baseline code in the `baseline/` directory for reference. All custom development is implemented outside the baseline to maintain a clean separation between the reference implementation and our enhancements.
