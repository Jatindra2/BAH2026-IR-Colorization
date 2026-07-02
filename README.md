# 🚀 IRVision AI

## Thermal Infrared Image Enhancement and Colorization using Deep Learning

**Bharatiya Antariksh Hackathon (BAH) 2026**

---

## 📖 Overview

IRVision AI is an AI-powered solution that reconstructs high-quality RGB satellite imagery from low-resolution Thermal Infrared (TIR) satellite images. The system combines Super Resolution and Deep Learning-based Colorization to improve image quality and generate visually meaningful RGB outputs for remote sensing applications.

The solution consists of:
- Super Resolution Network for spatial enhancement
- Deep Learning Colorization Network
- FastAPI backend for inference
- React-based frontend for user interaction

---

# 🎯 Problem Statement

### Problem Statement 10

**Infrared Image Colorization and Enhancement for Improved Object Interpretation**

Develop an AI-based solution capable of:

- Enhancing low-resolution Thermal Infrared imagery
- Performing Super Resolution (200 m → 100 m)
- Generating realistic RGB images from thermal data
- Improving object interpretation for remote sensing applications

---

# ✨ Features

- Thermal Infrared Image Enhancement
- Deep Learning-based Super Resolution
- AI-powered Image Colorization
- End-to-End Inference Pipeline
- FastAPI REST API
- Modern React Web Interface
- Real-time Prediction
- Download Generated Images

---

# 🏗️ System Architecture

```text
Input Thermal Image (.npy)
           │
           ▼
Image Preprocessing
           │
           ▼
Super Resolution Network
      (200 m → 100 m)
           │
           ▼
Colorization Network
           │
           ▼
LAB to RGB Conversion
           │
           ▼
Final RGB Image
```

---

# 🧠 Model Pipeline

1. Load Thermal Infrared (.npy) image
2. Normalize input data
3. Perform Super Resolution
4. Predict color channels using the Colorization Network
5. Convert LAB image to RGB
6. Return:
   - Super-Resolved Image
   - Final RGB Image

---

# 📂 Repository Structure

```text
BAH2026-IR-Colorization/
│
├── artifacts/
│   └── checkpoints/
│
├── backend/
│
├── frontend/
│
├── training/
│
├── evaluation/
│
├── baseline/
│
├── docs/
│
├── README.md
└── .gitignore
```

---

# 🛠️ Technology Stack

### Artificial Intelligence
- Python
- PyTorch
- NumPy
- OpenCV
- Pillow
- segmentation-models-pytorch

### Backend
- FastAPI
- Uvicorn

### Frontend
- React
- Vite
- Axios
- CSS

### Version Control
- Git
- GitHub

---

# 📊 Evaluation

The generated outputs can be evaluated using:

- PSNR (Peak Signal-to-Noise Ratio)
- SSIM (Structural Similarity Index)

Run evaluation using:

```bash
python evaluation/evaluate.py
```

---

# 🌍 Applications

- Remote Sensing
- Environmental Monitoring
- Disaster Management
- Agriculture
- Urban Planning
- Land Cover Analysis
- Satellite Image Interpretation

---

# 🤝 Team

Developed as part of the **Bharatiya Antariksh Hackathon (BAH) 2026**.

---

# 📄 License

This project was developed for the **Bharatiya Antariksh Hackathon (BAH) 2026**.

Please follow the hackathon guidelines regarding the use of the provided baseline resources and datasets.

---

# Acknowledgements

- Bharatiya Antariksh Hackathon (BAH) 2026
- PyTorch
- FastAPI
- React
- Vite
- OpenCV
- NumPy
