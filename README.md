# 🚗 Car Price Prediction - ML Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green)
![ML](https://img.shields.io/badge/ML-Linear%20Regression-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

> **An end-to-end Machine Learning project that predicts car prices using Linear Regression with Flask backend and interactive HTML/CSS/JS frontend.**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Model Performance](#model-performance)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project implements a **Car Price Prediction System** using Machine Learning. Users can input car details (year, mileage, fuel type, etc.) and get instant price predictions powered by a trained Linear Regression model.

### Key Highlights
- ✅ **Machine Learning Model**: Linear Regression with 85%+ accuracy
- ✅ **RESTful API**: Flask backend with CORS support
- ✅ **Modern UI**: Responsive and attractive frontend
- ✅ **Easy Deployment**: Ready for Heroku, Render, or local hosting
- ✅ **Real-time Predictions**: Instant results via AJAX calls

---

## ✨ Features

- 🔮 **Accurate Price Predictions** using trained ML model
- 📊 **Feature Engineering** (Car age calculation, categorical encoding)
- 🎨 **Beautiful UI** with gradient design and smooth animations
- 🚀 **Fast API** with JSON responses
- 📱 **Responsive Design** works on all devices
- 🔒 **Input Validation** with error handling
- 💾 **Model Persistence** using pickle files

---

## 🛠️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask** - Web framework
- **scikit-learn** - Machine Learning
- **pandas** - Data manipulation
- **NumPy** - Numerical computing
- **pickle** - Model serialization

### Frontend
- **HTML5**
- **CSS3** (Inline styling with gradients & animations)
- **JavaScript (ES6+)**
- **Fetch API** for AJAX calls

### ML Algorithm
- **Linear Regression** (scikit-learn)
- **Label Encoding** for categorical features

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8 or higher** installed
- **pip** (Python package manager)
- **Git** (optional, for cloning)
- **A dataset** (CSV file with car data)

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
```

### Step 2: Create Project Structure

```bash
mkdir -p backend/templates frontend notebooks
```

### Step 3: Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

**Or install individually:**

```bash
pip install flask==3.0.0 flask-cors==4.0.0 pandas==2.1.4 numpy==1.26.2 scikit-learn==1.3.2
```

### Step 4: Prepare Dataset

Place your `car_data.csv` in the `backend/` folder with these columns:

| Column | Type | Example |
|--------|------|---------|
| Year | Integer | 2018 |
| Present_Price | Float | 6.50 |
| Kms_Driven | Integer | 45000 |
| Fuel_Type | String | Petrol/Diesel/CNG |
| Seller_Type | String | Individual/Dealer |
| Transmission | String | Manual/Automatic |
| Selling_Price | Float | 5.25 (target) |

**Sample CSV:**
```csv
Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Selling_Price
2018,6.50,45000,Petrol,Dealer,Manual,5.25
2015,8.25,72000,Diesel,Individual,Manual,6.50
2020,10.00,15000,Petrol,Dealer,Automatic,9.25
```

### Step 5: Train the Model

```bash
cd backend
python train_model.py
```

**Output:**
```
Training R² Score: 0.8743
Testing R² Score: 0.8521
Model and encoders saved successfully!
```

This generates:
- `car_price_model.pkl` - Trained model
- `label_encoders.pkl` - Categorical encoders

### Step 6: Run the Application

**Terminal 1 - Backend:**
```bash
cd backend
python app.py
```
> Backend runs at: `http://localhost:5000`

**Terminal 2 - Frontend:**
```bash
cd frontend
python -m http.server 8000
```
> Frontend runs at: `http://localhost:8000`

---

## 📂 Project Structure

```
car-price-prediction/
│
├── backend/
│   ├── app.py                      # Flask API
│   ├── train_model.py              # Model training script
│   ├── templates/                  # Flask templates (if serving frontend)
│   │   └── index.html             
│   ├── car_data.csv                # Training dataset
│   ├── car_price_model.pkl         # Trained model (generated)
│   ├── label_encoders.pkl          # Encoders (generated)
│   └── requirements.txt            # Python dependencies
│
├── frontend/
│   └── index.html                  # Frontend UI
│
├── notebooks/
│   └── car_price_analysis.ipynb    # EDA & experiments
│
├── README.md                       # Documentation
└── .gitignore                      # Git ignore file
```

---

## 🔌 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "API is running"
}
```

#### 2. Predict Car Price
```http
POST /predict
```

**Request Body:**
```json
{
  "year": 2018,
  "present_price": 6.5,
  "kms_driven": 45000,
  "fuel_type": "Petrol",
  "seller_type": "Dealer",
  "transmission": "Manual"
}
```

**Response (Success):**
```json
{
  "success": true,
  "predicted_price": 5.25,
  "message": "Prediction successful"
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Invalid input data",
  "message": "Prediction failed"
}
```

### cURL Example

```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "year": 2018,
    "present_price": 6.5,
    "kms_driven": 45000,
    "fuel_type": "Petrol",
    "seller_type": "Dealer",
    "transmission": "Manual"
  }'
```

---

## 💻 Usage

### Using the Web Interface

1. **Open Frontend**: Navigate to `http://localhost:8000`
2. **Fill Form**: Enter car details
   - Year (e.g., 2018)
   - Present Price in Lakhs (e.g., 6.50)
   - Kilometers Driven (e.g., 45000)
   - Fuel Type (Petrol/Diesel/CNG)
   - Seller Type (Individual/Dealer)
   - Transmission (Manual/Automatic)
3. **Click "Get Price Prediction"**
4. **View Result**: Predicted price appears below

### Using Python Requests

```python
import requests

url = "http://localhost:5000/predict"
data = {
    "year": 2018,
    "present_price": 6.5,
    "kms_driven": 45000,
    "fuel_type": "Petrol",
    "seller_type": "Dealer",
    "transmission": "Manual"
}

response = requests.post(url, json=data)
result = response.json()
print(f"Predicted Price: ₹{result['predicted_price']} Lakhs")
```

---

## 🚀 Deployment

### Option 1: Deploy to Heroku

1. **Create `Procfile`:**
```
web: gunicorn app:app
```

2. **Update `requirements.txt`:**
```bash
echo "gunicorn==21.2.0" >> requirements.txt
```

3. **Deploy:**
```bash
heroku login
heroku create car-price-api
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

4. **Update Frontend API URL:**
```javascript
const API_URL = 'https://car-price-api.herokuapp.com/predict';
```

---

### Option 2: Deploy to Render

1. **Push to GitHub**
2. **Connect to Render**
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `python app.py`
5. **Add Environment Variables** (if needed)

---

### Option 3: Deploy Frontend to Netlify

1. **Drag & drop** `frontend/index.html` to Netlify
2. **Update API URL** in HTML
3. **Publish**

---

### Option 4: Docker Deployment

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

EXPOSE 5000

CMD ["python", "app.py"]
```

**Build & Run:**
```bash
docker build -t car-price-predictor .
docker run -p 5000:5000 car-price-predictor
```

---

## 📊 Model Performance

### Training Metrics
- **R² Score (Training):** 0.8743
- **R² Score (Testing):** 0.8521
- **Algorithm:** Multiple Linear Regression

### Feature Importance
1. **Car Age** - Most significant
2. **Present Price** - High impact
3. **Kms Driven** - Moderate impact
4. **Fuel Type** - Moderate impact
5. **Transmission** - Low impact
6. **Seller Type** - Low impact

### Improving Accuracy

**Add More Features:**
- Owner count
- Brand/Model
- Color
- Number of previous owners

**Try Advanced Algorithms:**
```python
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

# Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)

# XGBoost
model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
```

**Feature Engineering:**
```python
# Add depreciation rate
df['depreciation'] = (df['Present_Price'] - df['Selling_Price']) / df['Present_Price']

# Add price per km
df['price_per_km'] = df['Selling_Price'] / (df['Kms_Driven'] + 1)
```

---

## 🐛 Troubleshooting

### Issue 1: `TemplateNotFound: index.html`

**Solution:**
- Create `templates/` folder in backend
- Move `index.html` to `backend/templates/`
- OR use API-only mode (remove render_template)

### Issue 2: CORS Error

**Solution:**
```python
from flask_cors import CORS
CORS(app)  # Add this line
```

### Issue 3: Model Not Found

**Solution:**
```bash
cd backend
python train_model.py  # Train model first
```

### Issue 4: API Connection Failed

**Checklist:**
- ✅ Backend running on port 5000?
- ✅ Frontend API URL correct?
- ✅ Firewall blocking connections?
- ✅ Check browser console for errors

### Issue 5: Prediction Errors

**Solution:**
- Ensure categorical values match training data exactly
- Check data types (int, float, string)
- Validate input ranges

---

## 🔒 Security Best Practices

### For Production:

1. **Add Rate Limiting:**
```python
from flask_limiter import Limiter
limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/predict', methods=['POST'])
@limiter.limit("10/minute")
def predict():
    # ...
```

2. **Input Validation:**
```python
from marshmallow import Schema, fields, validate

class PredictionSchema(Schema):
    year = fields.Int(required=True, validate=validate.Range(min=1990, max=2025))
    present_price = fields.Float(required=True, validate=validate.Range(min=0))
    # ...
```

3. **Environment Variables:**
```python
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key')
```

---

## 📈 Future Enhancements

- [ ] Add authentication & user accounts
- [ ] Store predictions in database
- [ ] Create admin dashboard
- [ ] Add car image recognition
- [ ] Implement A/B testing for models
- [ ] Add data visualization charts
- [ ] Create mobile app (React Native)
- [ ] Add more ML algorithms comparison
- [ ] Implement model retraining pipeline
- [ ] Add unit tests & CI/CD

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: https://github.com/devendrareddy2344/
- LinkedIn: https://www.linkedin.com/in/devendra-reddy-vennapusa-b3665628a/
- Email: devendrareddy2344@gmail.com

---

## 🙏 Acknowledgments

- Dataset from [Kaggle Car Price Dataset](https://www.kaggle.com/)
- Inspired by various ML tutorials
- Flask documentation
- scikit-learn community

---

## 📞 Support

For support, devendrareddy2344@email.com or open an issue in the repository.

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

<div align="center">
  
**Made with ❤️ Devendra Reddy**

[⬆ Back to Top](#-car-price-prediction---ml-project)

</div>
