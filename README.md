# 🎬 Movie Recommendation Chatbot

This is a web-based intelligent movie recommendation chatbot that suggests movies to users based on their preferred genre or type using content-based filtering techniques. The project is built using **HTML**, **CSS**, **JavaScript** for the frontend and **Python (Flask)** with a machine learning model for the backend.

> Developed as a Mini Project by Darsh Rajput and Harsh Patel under the guidance of Dr. Priyang Bhatt at G H Patel College of Engineering & Technology.

---

## 📌 Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack Used](#tech-stack-used)
- [Project Architecture](#project-architecture)
- [Installation](#installation)
- [How it Works](#how-it-works)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)
- [License](#license)

---

## 📖 About the Project

The Movie Recommendation Chatbot helps users find movie suggestions tailored to their preferences. The system takes genre-based input from the user through a chatbot interface and uses a machine learning model (TF-IDF + Cosine Similarity) to return a list of recommended movies. This recommendation engine is trained on a dataset of movies containing titles and genres.

---

## 🌟 Features

- Interactive chatbot interface for a smooth user experience
- Real-time communication using AJAX (no page reloads)
- Uses Natural Language Processing to analyze user preferences
- Machine Learning model trained on movie genres using TF-IDF vectorization
- Content-based filtering to provide personalized recommendations
- Lightweight, responsive, and fast

---

## 🔧 Tech Stack Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Chatbot UI using DOM Manipulation
- AJAX for backend communication

### Backend
- Python 3
- Flask (Micro web framework)
- Pickle (for saving trained model)

### Machine Learning
- Scikit-learn
  - TF-IDF Vectorizer
  - Cosine Similarity

### Tools
- Visual Studio Code
- Git & GitHub
- Browser (for running the web app)

---

## 🧠 Project Architecture

```text
User → Chatbot UI → AJAX Request → Flask Backend → Recommendation Engine → JSON Response → Chatbot Display
