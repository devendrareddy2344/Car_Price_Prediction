import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('car.csv')

# Data preprocessing
print(df.head())
print(df.info())
print(df.isnull().sum())

# Handle categorical variables
le_fuel = LabelEncoder()
le_seller = LabelEncoder()
le_transmission = LabelEncoder()

df['Fuel_Type'] = le_fuel.fit_transform(df['Fuel_Type'])
df['Seller_Type'] = le_seller.fit_transform(df['Seller_Type'])
df['Transmission'] = le_transmission.fit_transform(df['Transmission'])

# Calculate car age
df['Car_Age'] = 2025 - df['Year']

# Select features
X = df[['Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Car_Age']]
y = df['Selling_Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(f"Training R² Score: {train_score:.4f}")
print(f"Testing R² Score: {test_score:.4f}")

# Save model and encoders
with open('car_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('label_encoders.pkl', 'wb') as f:
    pickle.dump({
        'fuel': le_fuel,
        'seller': le_seller,
        'transmission': le_transmission
    }, f)

print("Model and encoders saved successfully!")