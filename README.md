
# Yoliday

Yoliday is a FastAPI-based web application that generates casual and formal text responses based on user queries. It supports user login, history tracking, and demonstrates AI-powered text generation with a simple REST API.

---

## 📁 Project Structure

- `.idea/`  
  PyCharm project configuration files (IDE-specific).

- `__pycache__/`  
  Python bytecode cache folder (auto-generated).

- `deprecated_tests/`  
  Older or deprecated test scripts not currently in use.

- `tests/`  
  Current test files for API endpoints and application logic.

- `.env`  
  Environment variables file (keep this secure, contains sensitive data).

- `ai_engine.py`  
  Contains the core AI logic for generating casual and formal responses.

- `app.py`  
   Frontend application serving the user interface, including login and question/answer pages.

- `database.py`  
  SQLAlchemy setup, database connection, and table creation logic.

- `main.py`  
  Main FastAPI application with routes for login, generate, and history.

- `models.py`  
  SQLAlchemy ORM models defining database tables (e.g., Prompt model).

- `prompts.db`  
  SQLite database file storing user prompts and responses.

- `requirements.txt`  
  Python dependencies for the project.

- `Screenshot 2025-05-24 050540.png`  
  Screenshot of the login page.

- `Screenshot 2025-05-24 050656.png`  
  Screenshot of the question & answer page.

---

## 🚀 Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/akneeket/yoliday.git
   cd yoliday

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI app:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Open your browser to:**

   ```
   http://127.0.0.1:8000/docs
   ```

   This will open the interactive API documentation (Swagger UI).

---

## 🔐 Test User Credentials

For testing and demo purposes, you can use the following user accounts to log in:

| Username | Password    |
| -------- | ----------- |
| alice    | password123 |
| bob      | pass456     |

> **Note:** These credentials are for local testing only. Please secure authentication properly before deploying to production.

---

## 📜 API Endpoints Overview

* **POST /login**
  User login with username and password. Returns an access token.

* **POST /generate**
  Generate casual and formal responses based on a query string. Requires a Bearer token.

* **GET /history**
  Retrieve the history of past queries and responses for the logged-in user.

---

## 📷 Screenshots

* **Login Page**
  ![Login Page](Screenshot%202025-05-24%20050540.png)

* **Question & Answer Page**
  ![Q\&A Page](Screenshot%202025-05-24%20050656.png)

---

## 🛠 Technologies Used

* Python 3.11
* FastAPI
* SQLAlchemy
* SQLite
* Pytest (for testing)

---

## 🤝 Contribution

Feel free to fork the repo, add features, and submit pull requests. Please raise issues for any bugs or feature requests.

---

## ⚠️ Disclaimer

This project is a demo/prototype and should not be used as-is in production. It lacks robust security and error handling for real-world usage.

---


