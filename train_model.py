import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Generate synthetic dataset
np.random.seed(42)
data_size = 500

data = pd.DataFrame({
    "patients_before": np.random.randint(0, 20, data_size),
    "doctor_experience": np.random.randint(1, 30, data_size),
    "patient_type": np.random.randint(0, 2, data_size),  # 0 follow-up, 1 new
    "day": np.random.randint(0, 7, data_size),
    "hour": np.random.randint(8, 17, data_size),
})

# Target variable (appointment duration)
data["duration"] = (
    15
    + data["patients_before"] * 0.8
    - data["doctor_experience"] * 0.3
    + data["patient_type"] * 10
    + np.random.normal(0, 3, data_size)
)

X = data.drop("duration", axis=1)
y = data["duration"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Save model
joblib.dump(model, "scheduler_model.pkl")
print("Model saved as scheduler_model.pkl")
