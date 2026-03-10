# Deloitte Graduate Hiring Assessment - 2025

## Candidate Information
* **Full Name:** Rugved Shrikrushna Dhable
* **Email ID:** dhabalerugved7@gmail.com
* **College Name:** PES's Modern Colleg of Engineering
* **Selected Skill Track:** AI & Machine Learning

---

## Project Overview: Student Success Predictor API
For this assessment, I have developed and deployed a Machine Learning-based REST API that predicts a student's final academic result (PASS/FAIL) based on key performance metrics. 

Instead of a simple local script, I engineered this as a production-ready backend service. The application takes in continuous variables, calculates a weighted success probability, and returns a JSON response. 

### Tech Stack Used
* **Language:** Python 3
* **Web Framework:** Flask
* **Deployment & Hosting:** Render (Live Web Service)
* **API Security:** Flask-CORS (Cross-Origin Resource Sharing enabled for frontend integration)

---

## Live Deployment (Bonus)
The API is currently live and hosted on Render. It can be accessed and tested globally.
* **Live API Endpoint:** `https://student-prediction-api-6pqy.onrender.com/predict`
* **Method:** `POST`

---

## How to Run & Test in Replit
To evaluate this project locally within the Replit environment, follow these steps:

### 1. Start the Server
1. Open the Replit shell/console.
2. Ensure dependencies are installed by running: `pip install -r requirements.txt`
3. Start the Flask server by running: `python app.py`
4. The server will start running on `http://0.0.0.0:5000`

### 2. Test the API
I have included a dedicated testing script (`test_api.py`) to simulate a client request to the backend.
1. Open a second terminal tab in Replit.
2. Run the test script: `python test_api.py`
3. The script will send a JSON payload to the server and print the predicted outcome.

---

## API Schema Definition

**Request Format (`application/json`)**
```json
{
    "hours": 75,
    "attendance": 85,
    "previous_score": 82,
    "assignments": 8
}
