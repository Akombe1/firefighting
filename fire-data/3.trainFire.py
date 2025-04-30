# 3.trainFire.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np


def train_fire_model(fireData_path):
    # Load dataset
    fireData = pd.read_csv(fireData_path, low_memory=False)

    # Feature engineering
    fireData['alarm_date'] = pd.to_datetime(fireData['alarm_date'], errors='coerce')
    fireData['month'] = fireData['alarm_date'].dt.month
    fireData['day_of_week'] = fireData['alarm_date'].dt.dayofweek
    fireData['hour'] = pd.to_datetime(fireData['alarm_time'], format='%H:%M:%S', errors='coerce').dt.hour

    # Clean incident types
    fireData['incident_type_clean'] = fireData['incident_type'].astype(str).str.extract(r'(^\d{3})')
    fireData['incident_type_clean'] = pd.to_numeric(fireData['incident_type_clean'], errors='coerce')

    # Define binary target (fire = 1 if type 100-199)
    fireData['is_fire'] = fireData['incident_type_clean'].between(100, 199).astype(int)

    # Select features
    features = ['zip', 'district', 'property_use', 'month', 'day_of_week', 'hour', 'is_fire']
    fire_model_data = fireData[features].dropna()

    # Encode categorical variables
    X = pd.get_dummies(fire_model_data.drop(columns=['is_fire']))
    y = fire_model_data['is_fire']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train random forest with class_weight='balanced'
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)

    print("\n🔥 Fire Prediction Model Evaluation")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Feature Importance
    importances = model.feature_importances_
    feature_names = np.array(X.columns)
    top_indices = importances.argsort()[::-1][:10]
    print("\nTop 10 Important Features:")
    for i in top_indices:
        print(f"{feature_names[i]}: {importances[i]:.4f}")

    return model


if __name__ == "__main__":
    train_fire_model('fireData.csv')


# Example Usage:
# fire_model = train_fire_model('fireData.csv')