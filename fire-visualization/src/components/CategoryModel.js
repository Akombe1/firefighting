// src/components/CategoryModel.js
import React from 'react';

function CategoryModel() {
  return (
    <div className="page">
      <header>
        <h1>Fire Incident Category Model</h1>
        <p className="subheader">Multiclass Classification: What Type of Emergency Is It?</p>
      </header>

      <section className="card">
        <h2>Modeling Approach</h2>
        <p>
          Beyond predicting whether an incident was a fire, we sought to classify each emergency into <strong>incident categories </strong> 
           based on the leading digit of its 3-digit NFIRS incident code (e.g., “1xx” for fires, “3xx” for EMS). This formed a <strong>multiclass classification</strong> problem, 
          with 8 distinct categories representing high-level emergency types such as:
        </p>
        <ul>
          <li><strong>1xx</strong> – Fire</li>
          <li><strong>2xx</strong> – Overpressure rupture, explosion</li>
          <li><strong>3xx</strong> – EMS/Rescue</li>
          <li><strong>4xx</strong> – Hazardous Conditions</li>
          <li><strong>5xx</strong> – Service Call</li>
          <li><strong>6xx</strong> – Good Intent Call</li>
          <li><strong>7xx</strong> – False Alarm</li>
          <li><strong>8xx</strong> – Weather/Natural Disaster</li>
        </ul>
        <p>
          We used a <strong>Random Forest classifier</strong> and applied <strong>SMOTE</strong> again due to imbalances across categories. For example, 
          “Good Intent” and “Service Call” categories dominated the data, while others like “Explosion” or “Weather” were rare.
        </p>
      </section>

      <section className="card">
        <h2>Model Performance</h2>
        <p><strong>Test Accuracy:</strong> 39.7%</p>
        <p>
          Multiclass problems are significantly harder, especially when classes are imbalanced and overlapping in feature space.
          Although the overall accuracy is lower than in the binary fire model, we were still able to capture meaningful structure across major categories.
        </p>
        <p>
          Performance varied by class: the model had stronger precision and recall for high-volume categories like “Service Call” (5xx) and “Good Intent” (6xx), 
          while performance dropped on rarer ones like “Explosion” (2xx).
        </p>
      </section>

      <section className="card">
        <h2>Confusion Matrix</h2>
        <img src="/images/category_confusion_matrix_smote.png" alt="Category Model Confusion Matrix" className="eda-image" />
        <p>
          This matrix shows predictions versus true categories. As expected, categories with more samples dominate the diagonals. 
          The model commonly confuses 1xx (Fire), 4xx (Hazards), and 6xx (Good Intent) due to their similar time and location patterns.
        </p>
      </section>

      <section className="card">
        <h2>Top 10 Most Important Features</h2>
        <img src="/images/category_feature_importance_smote.png" alt="Category Model Feature Importances" className="eda-image" />
        <p>
          Similar to the binary model, temporal features like <strong>hour</strong>, <strong>month</strong>, and <strong>day of week</strong> were top predictors. 
          Certain <strong>property types</strong> also correlated strongly with specific categories. For instance, commercial properties with false alarms, or multi-unit housing with EMS and fire.
        </p>
        <p>
          These insights not only improve classification but could help policymakers and emergency responders anticipate the type of response needed for future calls.
        </p>
      </section>

      <footer>
        <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default CategoryModel;

