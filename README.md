
# 🧠  From Noise to Clarity: A Study of Filtering Techniques in Biomedical Imaging

**Engineering Mathematics – Sharif University of Technology**  
- 📅 Winter 1403  (Fall 2024 & Winter 2025)
- 👨‍🏫 Instructor: Prof. Hamid Aghajan

---

## 📁 Repository Structure

```
📦 root/
├── 📓 EngMath.ipynb     # Main code file including all analyses and visualizations
├── 📁 Codes Per Part/         # Separated code snippets for documentation (not executable)
├── 📁 pics/                    # All figures used in the report + original images
├── 📄 EngMath_Project.pdf     # Final project report
└── 📄 README.md               # Project overview and guide
```

---

## 🧪 Project Overview

This project explores the modeling and mitigation of noise in biomedical images. It includes both theoretical analysis and practical implementation of various filtering methods to denoise MRI images and analyze frequency and statistical properties of noise.

---

## 🎯 Objectives

- Explore image properties in frequency domain
- Model different types of noise (uniform, normal)
- Apply LPF/HPF in the frequency domain
- Implement classical and adaptive image filters
- Evaluate filtering performance using **SNR** and **PSNR**

---

## 🛠️ Technologies Used

- **Python**  
- **OpenCV**  
- **NumPy**, **Matplotlib**, **Pandas**  
- **Jupyter Notebook**

---

## 🖼️ Image Content

All images (original, noisy, and filtered) are located in the `pics/` directory.

Includes:
- Brain and spine MRI (original + noisy)
- Frequency domain visualizations
- Noise plots, histograms, and filter results

---

## 📊 Filter Comparison Table

| Filter           | Brain MRI (PSNR / SNR) | Spine MRI (PSNR / SNR) | Notes                            |
|------------------|-------------------------|--------------------------|----------------------------------|
| **Mean Filter**  | 🔻 Lowest               | 🔻 Lowest                | Blurs edges, weak denoising      |
| **Gaussian**     | ✅ Good                 | ⚠️ Moderate              | Smooth but may remove details    |
| **Bilateral**    | ✅ Good                 | ✅ Very Good             | Preserves edges, effective       |
| **Adaptive**     | 🏆 Best                 | 🏆 Best                 | Learns local variance, optimal   |

---

## 📜 Final Report

All theoretical explanations, figures, and outputs are provided in [`EngMath_Project.pdf`](EngMath_Project.pdf).

---

## ✅ How to Run

To run the full project:

```bash
jupyter notebook EngMath.ipynb
```

Make sure to install dependencies:

```bash
pip install numpy matplotlib opencv-python pandas
```

---

## 👥 Contributors
  ### Authors
- **Mohammadparsa Ghaderahmadi** – [mhparsaghdi@gmail.com](mailto:mhparsaghdi@gmail.com)  
- **Matin M. Babaei** – [matinmb82@gmail.com](mailto:matinmb82@gmail.com)
  ### By
- **Moein Yousefinia** – [moein.yoo84@sharif.edu](mailto:moein.yoo84@sharif.edu) or [moein_yoo@outlook.com](mailto:moein_yoo@outlook.com)

---

> This project was developed as part of the Engineering Mathematics course and showcases the practical applications of noise modeling and filtering in biomedical imaging.
