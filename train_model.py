import pandas as pd
import joblib
from sklearn.metrics import r2_score

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("india_housing_prices.csv")

# Remove missing values
df = df.dropna()

# Features
X = df[["BHK", "Size_in_SqFt"]]

# Target
y = df["Price_in_Lakhs"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy Score
score = r2_score(y_test, y_pred)

print("Model Accuracy:", round(score * 100, 2), "%")

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model Trained and Saved Successfully")