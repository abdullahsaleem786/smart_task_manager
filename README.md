# Smart Task Manager with Analytics & ML

Smart Task Manager is a CLI-based task management system that goes beyond basic CRUD operations by collecting task behavior data and preparing it for analytics and future machine learning workflows.

The project is built incrementally using a **day-by-day engineering approach**, focusing on clean architecture, testability, and data readiness.

---

## 🚀 Features

### Core Task Management
- Create, list, complete, and delete tasks
- Persistent storage using JSON
- Unique task IDs
- Priority-based task handling

### Analytics
- Task completion statistics
- Completed vs pending task counts
- Average task completion time

### Machine Learning (Data-Ready)
- Feature extraction from completed tasks
- Clean dataset export for ML experimentation
- Baseline logic before introducing models
- ML modules structured for future expansion

---

## 🧠 ML Pipeline (Conceptual & Partial Implementation)

### 1. Data Collection
- Task creation and completion timestamps are stored automatically

### 2. Feature Engineering
- Priority
- Task duration
- Creation hour
- Day of week
- Description length

### 3. Dataset Export
- Completed tasks can be exported as a clean CSV
- Dataset is ready for external analysis or model training

> ⚠️ Note: ML models are experimental and intentionally minimal to avoid fake or premature ML claims.

---

## 🏗 Project Architecture

app/
├── cli/ # CLI menu and input handling
├── models/ # Task data models
├── services/ # Business logic
├── storage/ # JSON persistence layer
├── analytics/ # Statistical analysis
├── ml/ # Feature engineering & ML groundwork
└── main.py # Application entry point


---

## 🛠 Tech Stack
- Python 3
- JSON (local persistence)
- CLI-based interface
- pytest for testing
- ML groundwork (no heavy frameworks yet)

---

## ▶️ How to Run

```bash
python -m app.main

🧪 Testing

This project uses pytest for automated testing.

Run tests:

python -m pytest

🧩 Design Principles

CLI-first to validate logic before UI

Service-layer architecture for testability

Storage abstraction for future scalability

Analytics and ML isolated from core logic

No fake ML — baseline logic before models