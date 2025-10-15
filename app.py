from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Load the trained model and encoders
with open('car_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    encoders = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        
        # Extract features
        year = int(data['year'])
        present_price = float(data['present_price'])
        kms_driven = int(data['kms_driven'])
        fuel_type = data['fuel_type']
        seller_type = data['seller_type']
        transmission = data['transmission']
        
        # Calculate car age
        car_age = 2025 - year
        
        # Encode categorical variables
        fuel_encoded = encoders['fuel'].transform([fuel_type])[0]
        seller_encoded = encoders['seller'].transform([seller_type])[0]
        transmission_encoded = encoders['transmission'].transform([transmission])[0]
        
        # Prepare features for prediction
        features = np.array([[present_price, kms_driven, fuel_encoded, 
                            seller_encoded, transmission_encoded, car_age]])
        
        # Make prediction
        predicted_price = model.predict(features)[0]
        predicted_price = round(predicted_price, 2)
        
        return jsonify({
            'success': True,
            'predicted_price': predicted_price,
            'message': 'Prediction successful'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Prediction failed'
        }), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'API is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)