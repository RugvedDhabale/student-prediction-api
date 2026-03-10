import requests

# The URL of your local server's predict route
url = 'https://student-prediction-api-6pqy.onrender.com/predict'

# The student data we want to send
student_data = {
    "hours": 75,
    "attendance": 85,
    "previous_score": 82,
    "assignments": 8
}

print("Sending data to the server...")

# Send the POST request
response = requests.post(url, json=student_data)

# Print the server's response
print("\nStatus Code:", response.status_code)
print("Response Details:\n", response.json())