from flask import Flask, request, jsonify
from flask_cors import CORS
import csv


app = Flask(__name__)
CORS(app)

# 1. Your original prediction logic (unchanged)
def predict(hours, attendance, previous_score, assignments):
    score = (
        0.35 * (hours / 10) +
        0.25 * (attendance / 100) +
        0.25 * (previous_score / 100) +
        0.15 * (assignments / 10)
    )

    if score >= 0.5:
        return "PASS"
    else:
        return "FAIL"

# 2. Updated data loader (changed path from /content/ to relative path)
def load_dataset():
    data = []
    try:
        with open("./dataset.csv") as file:  # Looks for file in the same folder
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        return []

# Load dataset once when the server starts up
dataset = load_dataset()
print(f"Dataset loaded: {len(dataset)} records")

# 3. The new Web Endpoint
@app.route('/predict', methods=['POST'])
def get_prediction():
    # Receive JSON data from the web request instead of using input()
    data = request.get_json()

    try:
        # Extract variables from the incoming JSON
        hours = float(data['hours'])
        attendance = float(data['attendance'])
        previous = float(data['previous_score'])
        assignments = float(data['assignments'])

        # Run your prediction function
        result = predict(hours, attendance, previous, assignments)

        # Return a JSON response back to the client/frontend
        return jsonify({
            "status": "success",
            "prediction": result,
            "inputs_received": {
                "hours": hours,
                "attendance": attendance,
                "previous_score": previous,
                "assignments": assignments
            }
        }), 200

    except KeyError as e:
        # Handle cases where the frontend forgets to send a required field
        return jsonify({"status": "error", "message": f"Missing field: {str(e)}"}), 400
    except ValueError:
        return jsonify({"status": "error", "message": "All inputs must be numbers."}), 400

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)