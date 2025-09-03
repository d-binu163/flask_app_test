from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load("diabetes_model.pkl")

@app.route("/")
def home():
    return "Diabetes Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()  # Get JSON input
    # Validate input
    expected_features = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
    for feature in expected_features:
        if feature not in data:
            return jsonify({"error": f"Missing feature: {feature}"}), 400

    # Convert input to DataFrame
    input_df = pd.DataFrame([data])
    
    # Predict
    prediction = model.predict(input_df)[0]
    
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')