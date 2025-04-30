# The Future of Fire

## Team Members

Adrian Kombe and Abbie Kinaro

## Project Overview

This project explores the prediction and visualization of fire incidents across Boston.
We combined historical fire incident data, geospatial mapping, and machine learning to:

- Predict where and what types of fires are most likely to occur
- Visualize historical and projected fire incidents on a 3D map of Boston
- Analyze seasonal and temporal patterns of fire activity

We aimed to answer two questions:

1. Can we predict fire incidents by location and type?
2. How can spatial-temporal trends help improve fire preparedness?

## Dataset

We merged three fire incident datasets containing over 500,000 incidents:

- Fire incident reports (2012–2025)
- Location addresses and property data
- Fire codes categorized by type of incident
We performed preprocessing, geocoding, and cleaning to build the final fireData dataset.
  
## Objectives

- Improve public safety insights using machine learning
- Predict the likely category of an emergency incident before dispatch
- Handle severe class imbalance using reclassification and resampling
- Integrate model output into a geospatial viewer for interpretation

## Machine Learning Approach

We built a fire prediction model using:

Random Forest Classifier

- Target: Fire incident category (based on NFIRS fire codes)
- Features: Location, time (seasonality), and property type

Model Highlights:

- Overall Accuracy: ~43–45%
- Strongest performance predicting structural fires (building, vehicle, dumpster fires)
- Challenges in distinguishing rare fire categories

## Geospatial Visualization

We visualized past and projected fire incidents with a 3D Boston city model built with:

- CesiumJS (for 3D interactive maps)
- Boston OSM Buildings
- Boston City Boundary overlay

Features:

- Color-coded map showing fire incidents (past and predicted)
- Timeline animation showing changes over time from 2012–2025
- Hover effects for interactive exploration
- Fire stations and fire events are highlighted dynamically
- City boundaries are drawn for context