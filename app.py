import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_URL = os.getenv("API_URL", "http://localhost:8000")

# Session state keys for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_id" not in st.session_state:
    st.session_state.user_id = ""
if "token" not in st.session_state:
    st.session_state.token = ""

def login():
    login_user = st.session_state.login_user.strip()
    login_pass = st.session_state.login_pass.strip()

    if not login_user or not login_pass:
        st.error("⚠️ Please enter both username and password.")
        return

    try:
        resp = requests.post(f"{API_URL}/login", json={"username": login_user, "password": login_pass}, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            st.session_state.logged_in = True
            st.session_state.user_id = login_user
            st.session_state.token = data["access_token"]
            st.success(f"✅ Logged in as {login_user}")
        else:
            st.error("🚫 Login failed: " + resp.json().get("detail", "Unknown error"))
    except Exception as e:
        st.error(f"❌ Login request error: {e}")

def logout():
    st.session_state.logged_in = False
    st.session_state.user_id = ""
    st.session_state.token = ""
    st.success("👋 Logged out")

# Page Title
st.title("✨ AI Prompt Generator 🧠")

if not st.session_state.logged_in:
    st.markdown("### 🔐 Please Log In")
    st.text_input("Username", key="login_user")
    st.text_input("Password", type="password", key="login_pass")
    st.button("🔓 Log In", on_click=login)
    st.stop()

# If logged in
st.markdown(f"👋 Welcome, **{st.session_state.user_id}**")
st.button("🚪 Log Out", on_click=logout)

st.markdown("Generate both **Casual 😎** and **Formal 🧑‍💼** responses to your queries.")

# 📥 Input Form
with st.form(key='query_form'):
    st.markdown("### 📌 Enter Your Query")
    query = st.text_area("📝 Your Query")
    submit_button = st.form_submit_button("🚀 Generate Response")

# 🧪 Input Validation & Response Generation
if submit_button:
    if not query.strip():
        st.error("⚠️ Query cannot be empty.")
    else:
        with st.spinner("🔄 Generating responses..."):
            headers = {"Authorization": f"Bearer {st.session_state.token}"}
            try:
                response = requests.post(
                    f"{API_URL}/generate",
                    json={"user_id": st.session_state.user_id, "query": query.strip()},
                    headers=headers,
                    timeout=30,
                )
                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Response generated!")

                    st.markdown("### 😎 Casual Response")
                    st.write(data["casual_response"])

                    st.markdown("### 🧑‍💼 Formal Response")
                    st.write(data["formal_response"])
                else:
                    st.error(f"🚫 Error from server: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Request failed: {e}")

# 📜 Sidebar History
st.sidebar.header("📚 Query History")

if st.session_state.logged_in:
    headers = {"Authorization": f"Bearer {st.session_state.token}"}
    try:
        response = requests.get(f"{API_URL}/history", params={"user_id": st.session_state.user_id}, headers=headers)
        if response.status_code == 200:
            history = response.json()
            if history:
                st.sidebar.success("🕘 History loaded!")
                for idx, item in enumerate(history):
                    st.sidebar.markdown(f"**🔍 Query:** {item['query']}")
                    st.sidebar.markdown(f"🧠 *Casual:* {item['casual_response'][:50]}...")
                    st.sidebar.markdown(f"🏢 *Formal:* {item['formal_response'][:50]}...")

                    full_text = (
                        f"🔍 Query:\n{item['query']}\n\n"
                        f"🧠 Casual Response:\n{item['casual_response']}\n\n"
                        f"🏢 Formal Response:\n{item['formal_response']}"
                    )

                    st.sidebar.download_button(
                        label="📥 Download this response",
                        data=full_text,
                        file_name=f"response_{idx+1}.txt",
                        mime="text/plain",
                        key=f"download_{idx}"
                    )

                    st.sidebar.markdown("---")
            else:
                st.sidebar.warning("📭 No history found.")
        else:
            st.sidebar.error("🚫 Failed to load history.")
    except requests.exceptions.RequestException as e:
        st.sidebar.error(f"❌ Request failed: {e}")
else:
    st.sidebar.info("ℹ️ Log in to load your query history.")
