# 🚀 IRVision AI

### AI-Powered Infrared Image Enhancement & Colorization for Improved Object Interpretation

> **Bharatiya Antariksh Hackathon (BAH) 2026 Submission**

---

## 📌 Problem Statement

**Problem Statement 10 – Infrared Image Colorization and Enhancement for Improved Object Interpretation**

Develop an end-to-end AI pipeline capable of:

* Enhancing low-resolution Thermal Infrared (TIR) satellite imagery
* Performing super-resolution from **200m → 100m**
* Colorizing thermal images into realistic RGB representations
* Improving object interpretation for downstream geospatial analysis

---

# 🎯 Project Objectives

* Develop a Super-Resolution model for Thermal Infrared imagery
* Develop a Thermal-to-RGB Colorization model
* Build a scalable AI training pipeline
* Create a production-ready inference API
* Develop an interactive web dashboard
* Evaluate models using quantitative image quality metrics

---

# 🏗️ System Architecture

```text
Landsat-9 Level-2 Dataset
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
Inference API (FastAPI)
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
├── baseline/          # Official preprocessing pipeline
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

### AI & Machine Learning

* Python
* PyTorch *(planned)*
* NumPy
* OpenCV
* Pillow
* tifffile

### Backend

* FastAPI *(planned)*

### Frontend

* React *(planned)*
* TypeScript *(planned)*
* Tailwind CSS *(planned)*

### Development Tools

* Git
* GitHub
* Docker *(planned)*

---

# 📈 Development Roadmap

| Milestone                                  | Status      |
| ------------------------------------------ | ----------- |
| ✅ Repository Setup                         | Complete    |
| ✅ Official Baseline Integration            | Complete    |
| ✅ Project Architecture                     | Complete    |
| ✅ Landsat Dataset Acquisition              | Complete    |
| ✅ Dataset Preprocessing & Patch Generation | Complete    |
| 🔄 PyTorch Dataset Loader                  | In Progress |
| ⏳ Super-Resolution Model                   | Planned     |
| ⏳ Colorization Model                       | Planned     |
| ⏳ Model Training & Evaluation              | Planned     |
| ⏳ Backend API                              | Planned     |
| ⏳ Frontend Dashboard                       | Planned     |
| ⏳ Deployment & Final Submission            | Planned     |

---

# 🎉 Latest Progress

Successfully completed the official preprocessing workflow using a **Landsat-9 Level-2** scene.

Current achievements include:

* ✅ Downloaded and validated Landsat-9 imagery
* ✅ Generated RGB images from spectral bands
* ✅ Created 100m and 200m thermal imagery
* ✅ Successfully generated **16 aligned training patches**
* ✅ Organized a modular project structure for future development

---

# 📊 Current Project Status

| Module                 | Status         |
| ---------------------- | -------------- |
| Repository Setup       | ✅ Complete     |
| Baseline Integration   | ✅ Complete     |
| Landsat Dataset        | ✅ Complete     |
| Dataset Preprocessing  | ✅ Complete     |
| Patch Generation       | ✅ Complete     |
| PyTorch Dataset Loader | 🔄 In Progress |
| AI Models              | ⏳ Planned      |
| Backend API            | ⏳ Planned      |
| Frontend Dashboard     | ⏳ Planned      |

---

# 🚀 Next Milestone

The next development phase focuses on implementing the AI pipeline:

* Build the PyTorch Dataset Loader
* Develop the Super-Resolution Network
* Develop the Thermal-to-RGB Colorization Network
* Implement the training pipeline
* Integrate inference into the web application

---

# 📜 License

This repository includes the official preprocessing baseline in the `baseline/` directory for reference.

All custom AI models, training code, backend services, and frontend components are developed separately to maintain a clean separation between the reference implementation and our solution.

---

⭐ **Project Status:** Active Development
