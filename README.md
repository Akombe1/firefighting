# The Future of Fire: Predicting and Visualizing Boston Fire Incidents

By Adrian Kombe and Abigail Kinaro  
MIT 1.001 | Spring 2025

## Overview

The Future of Fire is a machine learning and geospatial analysis project that explores historical fire incident data from Boston (2012–2024) to predict and visualize emergency response patterns.

Using over 600,000 incident records, we built two predictive models. One to determine whether an emergency call is a fire and another to classify the type of incident. Our results are showcased through a custom-built React website with interactive Mapbox maps, charts, and model evaluation summaries.

##  Project Goals

- Use historical fire department data to model and predict:
  - Whether a reported emergency is a fire
  - The most likely emergency category (e.g., EMS, false alarm, fire)
- Address severe class imbalance with SMOTE
- Identify key time/location/property features contributing to fire risk
- Visualize patterns through exploratory data analysis (EDA)
- Present results interactively using Mapbox 3D maps, clustering, and timeline animations

## Methods

### Binary Classifier: Is it a Fire?
- Model: `RandomForestClassifier` with `class_weight='balanced'`
- Features: Time (hour, month), location (zip, district), property type
- Accuracy: ~85%
- Key features: Hour of day, day of week, and property use code

### 🔹 Multiclass Classifier: What Type of Incident?
- Model: Random Forest + SMOTE
- Accuracy: ~40%
- Handles 8 classes including fire, EMS, service calls, and false alarms
- Key challenge: extreme class imbalance


## Visualizations

- EDA Dashboard: Temporal patterns, top incident types, geographic hot zones
- Mapbox Heatmap: Displays all confirmed fires over 12 years using KMeans clustering
- 3D Animated Map: Year-by-year timeline of fire events in Boston, rendered with Mapbox GL JS
- Model Plots: Confusion matrices and top feature importances for both models

## How to Run

### 1. Backend Scripts (Python)

Install dependencies:
```bash
pip install pandas scikit-learn imbalanced-learn matplotlib seaborn

cd Fire_Data
python3 1.merging.py                  # Merge & clean data - download data from google drive link - too large to push on github
python3 3.trainFire.py                # Train binary fire model
python3 4.trainCategories.py          # Train category model
python3 5.fireModelPlots.py           # Save model plots
python3 6.trainFire_SMOTE.py          # Optional: train with SMOTE
python3 7.trainCategory_SMOTE.py
python3 8.categoryModelPlots.py
```

### 2. React Frontend

```
cd fire-visualization
npm install
npm start
```
