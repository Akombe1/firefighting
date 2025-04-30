# trainCategory_SMOTE.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
import numpy as np


def train_category_model_with_smote(fireData_path):
    fireData = pd.read_csv(fireData_path, low_memory=False)

    # Feature engineering
    fireData['alarm_date'] = pd.to_datetime(fireData['alarm_date'], errors='coerce')
    fireData['month'] = fireData['alarm_date'].dt.month
    fireData['day_of_week'] = fireData['alarm_date'].dt.dayofweek
    fireData['hour'] = pd.to_datetime(fireData['alarm_time'], errors='coerce').dt.hour

    fireData['incident_type_clean'] = fireData['incident_type'].astype(str).str.extract(r'(^\d{3})')
    fireData['incident_type_clean'] = pd.to_numeric(fireData['incident_type_clean'], errors='coerce')

    # Define category
    fireData['category'] = fireData['incident_type_clean'].dropna().astype(int).astype(str).str[0]

    features = ['zip', 'district', 'property_use', 'month', 'day_of_week', 'hour', 'category']
    cat_model_data = fireData[features].dropna()

    X = pd.get_dummies(cat_model_data.drop(columns=['category']))
    y = cat_model_data['category']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Apply SMOTE
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    model.fit(X_resampled, y_resampled)

    # Predict
    y_pred = model.predict(X_test)

    print("\n🔥 SMOTE Category Prediction Model Evaluation")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    return model


if __name__ == "__main__":
    train_category_model_with_smote('fireData.csv')