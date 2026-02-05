# Smart Task Manager with Analytics & ML

Smart Task Manager is a CLI-based task management system that goes beyond CRUD operations by collecting task behavior data and preparing it for analytics and machine learning.

This project is built incrementally using a day-by-day engineering approach.

---

## 🚀 Features

### Core Task Management
- Create, list, complete, and delete tasks
- Persistent storage using JSON
- Unique task IDs
- Priority-based task handling

### Analytics
- Task completion statistics
- Daily task creation and completion trends
- Average completion time analysis

### Machine Learning (Data-Ready)
- Feature extraction from completed tasks
- ML-ready dataset generation
- Baseline vs ML model evaluation
- Task duration prediction (experimental)

---

## 🧠 ML Pipeline Explained

1. **Data Collection**
   - Task creation and completion timestamps are stored automatically

2. **Feature Engineering**
   - Priority
   - Task duration
   - Creation hour
   - Day of week
   - Description length

3. **Dataset Export**
   - Completed tasks are converted into a clean CSV dataset
   - Ready for model training or external analysis

---

## 🏗 Project Architecture

app/
├── cli/ # CLI menu and input handling
├── models/ # Task data model
├── services/ # Business logic
├── storage/ # JSON persistence layer
├── analytics/ # Statistical analysis
├── ml/ # Feature engineering & ML
└── main.py # Application entry point


---

## 🛠 Tech Stack
- Python 3
- JSON (local persistence)
- CLI-based interface
- Basic machine learning (from scratch)

---

## ▶️ How to Run

```bash
python -m app.main
