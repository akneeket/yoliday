
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

## 🌐 Deployment and Technology Integration

In this project, we've combined **FastAPI**, **Render**, and **Streamlit Community Cloud** to build and deploy our application in a seamless, cloud-based setup:

✅ **FastAPI**

* Used as the core web application framework to build our backend API endpoints.
* It powers the main logic for user login, query generation (casual and formal text), and history tracking.
* Locally runs at `http://127.0.0.1:8000/docs` for testing and Swagger documentation.

✅ **Render**

* Deployed our FastAPI backend to Render, a fully managed cloud platform.
* Render automatically builds and deploys the app from our GitHub repository, ensuring it’s **always live and accessible**.
* No need to keep your local machine or GitHub open—Render hosts the FastAPI app 24/7.

✅ **Streamlit Community Cloud**

* We used Streamlit to build a **user-friendly frontend** that interacts with the FastAPI backend.
* The Streamlit app provides an intuitive UI for users to log in, enter queries, and view generated responses.
* Deployed to Streamlit Community Cloud, making it easily shareable and accessible via a unique URL.

🪄 **How It All Works Together:**

1. **Users access the Streamlit app** (hosted on Streamlit Community Cloud).
2. The Streamlit frontend **sends API requests** to the FastAPI backend hosted on Render.
3. FastAPI processes these requests, interacts with the database, and generates responses.
4. The responses are **displayed in real-time on the Streamlit app**.

✅ This architecture ensures the app is fully functional and accessible **without needing to keep your local environment running**!

---

## 🤝 Contribution

Feel free to fork the repo, add features, and submit pull requests. Please raise issues for any bugs or feature requests.

---

## ⚠️ Disclaimer

This project is a demo/prototype and should not be used as-is in production. It lacks robust security and error handling for real-world usage.

```

Let me know if you want to:  
- Add links to the actual Streamlit and Render deployments,  
- Polish further (like adding badges or CI info),  
- Or make any final tweaks! 🚀✨
```
