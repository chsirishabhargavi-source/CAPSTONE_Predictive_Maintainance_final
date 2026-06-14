import joblib
import pandas as pd
from flask import Flask, request, jsonify
<<<<<<< HEAD
from model import load_model
from plots import plot_sensors
=======
>>>>>>> 6807225c8a0f257067e4248bb153f1922667deb7

app = Flask(__name__)

# Load the trained model
model = joblib.load('best_random_forest_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the request
        data = request.get_json(force=True)

        # Convert input data to DataFrame
        # Ensure the order of columns matches the training data
        # Expected features: Engine rpm, Lub oil pressure, Fuel pressure, Coolant pressure, Coolant temp
        input_df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        # Return prediction as JSON
        return jsonify({
            'engine_condition_prediction': int(prediction[0]),
            'probability_normal': prediction_proba[0][0],
            'probability_faulty': prediction_proba[0][1]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
