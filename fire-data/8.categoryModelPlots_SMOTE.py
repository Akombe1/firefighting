# categoryModelPlots_SMOTE.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
from saveModels import save_model
import importlib.util
import sys

spec = importlib.util.spec_from_file_location("trainCategory_SMOTE", "./7.trainCategory_SMOTE.py")
trainCategory_SMOTE = importlib.util.module_from_spec(spec)
sys.modules["trainCategory_SMOTE"] = trainCategory_SMOTE
spec.loader.exec_module(trainCategory_SMOTE)

model = trainCategory_SMOTE.train_category_model_with_smote("fireData.csv")
save_model(model, "category_model_smote.pkl")

# Load and prepare data
fireData = pd.read_csv("fireData.csv", low_memory=False)
fireData['alarm_date'] = pd.to_datetime(fireData['alarm_date'], errors='coerce')
fireData['month'] = fireData['alarm_date'].dt.month
fireData['day_of_week'] = fireData['alarm_date'].dt.dayofweek
fireData['hour'] = pd.to_datetime(fireData['alarm_time'], errors='coerce').dt.hour

fireData['incident_type_clean'] = fireData['incident_type'].astype(str).str.extract(r'(^\d{3})')
fireData['incident_type_clean'] = pd.to_numeric(fireData['incident_type_clean'], errors='coerce')
fireData['category'] = fireData['incident_type_clean'].dropna().astype(int).astype(str).str[0]

features = ['zip', 'district', 'property_use', 'month', 'day_of_week', 'hour', 'category']
data = fireData[features].dropna()
X = pd.get_dummies(data.drop(columns=['category']))
y = data['category']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict
y_pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix: Category Prediction (SMOTE)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("plots/category_confusion_matrix_smote.png", dpi=300)
plt.close()

# Feature Importance
importances = model.feature_importances_
feature_names = np.array(X.columns)
top_idx = np.argsort(importances)[-10:][::-1]

plt.figure(figsize=(10,6))
sns.barplot(x=importances[top_idx] * 100, y=feature_names[top_idx], palette="magma")
plt.title("Top 10 Feature Importances: Category Prediction (SMOTE)")
plt.xlabel("Importance (%)")
plt.ylabel("Feature")
plt.tight_layout()
plt.savefig("plots/category_feature_importance_smote.png", dpi=300)
plt.close()

# Print test accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n🔥 SMOTE Category Model Test Accuracy: {accuracy:.4f}")
print("🔥 SMOTE category plots saved to /plots directory!")
