<div align="center">

<img src="./assets/banner.png" width="100%" alt="AI Skin Disease Detection Banner"/>

# 🩺 AI Skin Disease Detection System

### Deep Learning Powered Medical Diagnostic Assistant

<p>
An end-to-end AI-powered web application that detects skin diseases from medical images using <b>EfficientNetB0</b>. The system provides intelligent disease prediction, confidence analysis, downloadable medical reports, prediction history, and an interactive analytics dashboard.
</p>

<p>

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python"/>
<img src="https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow"/>
<img src="https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask"/>
<img src="https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv"/>
<img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite"/>
<img src="https://img.shields.io/badge/Hosted_on-Render-46E3B7?style=for-the-badge&logo=render"/>

</p>

<a href="https://ai-skin-disease-detection-1-fu14.onrender.com">
<img src="https://img.shields.io/badge/🚀_Live_Demo-Visit_Website-blue?style=for-the-badge"/>
</a>

</div>
# 📖 Overview

Skin diseases affect millions of people worldwide, making early diagnosis essential for timely treatment and better patient outcomes.

The **AI Skin Disease Detection System** leverages Deep Learning and Computer Vision to analyze skin images and identify potential skin diseases with confidence scores. Beyond disease classification, the application provides comprehensive medical information, maintains prediction history, generates downloadable PDF reports, and presents insightful analytics through an interactive dashboard.

The project demonstrates how Artificial Intelligence, Full Stack Web Development, Database Management, and Data Visualization can be integrated into a complete healthcare application.
# 💡 Why This Project?

Access to dermatologists is not always immediate or affordable, especially in remote regions. This project explores how Artificial Intelligence can assist in preliminary skin disease screening by providing rapid image-based analysis.

Unlike conventional image classification projects, this application offers:

- 🧠 AI-powered disease prediction
- 📄 Automated medical report generation
- 📊 Interactive analytics dashboard
- 📜 Prediction history management
- 💾 Database integration
- 🌐 Responsive web application

The goal is to demonstrate an end-to-end healthcare AI solution that combines machine learning with a practical and user-friendly interface.
# ✨ Key Features

### 🤖 AI Disease Detection
- Upload skin images for instant analysis
- EfficientNetB0-based deep learning model
- Real-time disease prediction
- Confidence score visualization

### 📋 Intelligent Medical Report
- Disease name
- Confidence percentage
- Disease description
- Common symptoms
- Recommended precautions
- Downloadable PDF report

### 📜 Prediction History
- Persistent prediction records
- Timestamped results
- Delete individual entries
- SQLite database integration

### 📊 Analytics Dashboard
- Total predictions
- Average confidence score
- Most common disease
- Disease frequency charts
- Prediction trends
- Recent prediction summary

### ⚡ User Experience
- Drag-and-drop image upload
- Loading animation
- Responsive interface
- Modern healthcare-inspired UI
# 🔄 Application Workflow

```text
Upload Skin Image
        │
        ▼
Image Validation
        │
        ▼
Image Preprocessing
        │
        ▼
EfficientNetB0 Model
        │
        ▼
Disease Prediction
        │
        ▼
Generate Prediction Report
        │
        ├────────────► Save to Database
        │
        ├────────────► Generate PDF Report
        │
        └────────────► Update Analytics Dashboard
```
# 🏗 System Architecture

```mermaid
flowchart TD

A[Upload Image]

A --> B[Image Preprocessing]

B --> C[EfficientNetB0 CNN]

C --> D[Disease Prediction]

D --> E[Prediction Report]

E --> F[Symptoms]

E --> G[Precautions]

E --> H[Medical Recommendation]

E --> I[Generate PDF Report]

D --> J[SQLite Database]

J --> K[Prediction History]

J --> L[Analytics Dashboard]
```
# 🧠 Deep Learning Model

| Property | Details |
|-----------|---------|
| Model | EfficientNetB0 |
| Framework | TensorFlow / Keras |
| Input Size | 224 × 224 |
| Task | Multi-Class Skin Disease Classification |
| Output | Disease Class + Confidence Score |
# 📂 Dataset & Training

The model was trained using a labeled skin disease dataset consisting of multiple disease categories.

### Training Configuration

| Parameter | Value |
|-----------|-------|
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Batch Size | 32 |
| Epochs | 25 |
| Image Size | 224 × 224 |

### Data Augmentation

- Rotation
- Horizontal Flip
- Zoom
- Width Shift
- Height Shift
- Brightness Adjustment

> Update the above values if your training configuration differs.
# 📈 Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 95.42% |
| Precision | 94.81% |
| Recall | 94.25% |
| F1-Score | 94.53% |

> Replace these metrics with your actual evaluation results.
# 📸 Application Preview

<table>
<tr>
<td width="50%">
<b>🏠 Home Page</b><br>
<img src="./assets/home.png">
</td>

<td width="50%">
<b>🧠 Prediction Report</b><br>
<img src="./assets/prediction.png">
</td>
</tr>

<tr>
<td>
<b>📜 Prediction History</b><br>
<img src="./assets/history.png">
</td>

<td>
<b>📊 Analytics Dashboard</b><br>
<img src="./assets/dashboard.png">
</td>
</tr>
</table>
# 💻 Technology Stack

| Category | Technology |
|-----------|------------|
| 💻 Language | Python |
| 🧠 Deep Learning | TensorFlow, Keras |
| 👁 Computer Vision | OpenCV |
| 🌐 Backend | Flask |
| 🎨 Frontend | HTML, CSS, JavaScript |
| 📊 Visualization | Chart.js |
| 🗄 Database | SQLite |
| 📄 Reports | ReportLab |
| ☁ Deployment | Render |
# 🚀 Future Enhancements

- Explainable AI using Grad-CAM
- REST API integration
- Docker containerization
- Cloud database support
- User authentication
- Doctor portal
- Patient profile management
- Mobile application
- Disease severity assessment
- AI-powered treatment recommendations
# 📊 Repository Statistics

![Stars](https://img.shields.io/github/stars/BATTURI-VINOD/AI-Skin-Disease-Detection?style=for-the-badge)

![Forks](https://img.shields.io/github/forks/BATTURI-VINOD/AI-Skin-Disease-Detection?style=for-the-badge)

![Last Commit](https://img.shields.io/github/last-commit/BATTURI-VINOD/AI-Skin-Disease-Detection?style=for-the-badge)

![Repo Size](https://img.shields.io/github/repo-size/BATTURI-VINOD/AI-Skin-Disease-Detection?style=for-the-badge)
<div align="center">

# 👨‍💻 Author

## Vinod Batturi

AI Engineer • Full Stack Developer • Machine Learning Enthusiast

<a href="https://github.com/BATTURI-VINOD">GitHub</a> •
<a href="https://ai-skin-disease-detection-1-fu14.onrender.com/">Live Demo</a>

---

⭐ If you found this project useful, consider giving it a star.

Made with ❤️ using Flask, TensorFlow, EfficientNetB0, OpenCV, and SQLite.

</div>
