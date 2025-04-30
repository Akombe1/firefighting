// src/components/FireModel.js
import React from 'react';

function FireModel() {
  return (
    <div className="page">
      <header>
        <h1>Fire Incident Prediction Model</h1>
        <p className="subheader">Binary Classification: Is the Emergency Call a Fire?</p>
      </header>

      <section className="card">
        <h2>Modeling Approach</h2>
        <p>
          To better understand and predict fire-related emergencies, we framed a binary classification problem where each historical incident 
          was labeled as either a fire (1) or not a fire (0) using official NFIRS incident codes. Our final dataset included over 600,000 records from 2012 to 2024, 
          covering a wide range of emergency scenarios in Boston.
        </p>
        <p>
          We engineered features from the time and location of the alarm such as <strong>hour of day</strong>, <strong>month</strong>, and <strong>day of the week</strong>
          as well as <strong>property use</strong> and <strong>district</strong>. After one-hot encoding the categorical variables and dropping missing values, 
          we trained a <strong>Random Forest Classifier</strong> to learn patterns associated with fire events.
        </p>
        <p>
          Since fire incidents made up only about 10% of the total data, we used <strong>SMOTE (Synthetic Minority Oversampling Technique)</strong> to balance the classes and ensure the model learned meaningful patterns for the minority class.
        </p>
      </section>

      <section className="card">
        <h2>Model Performance</h2>
        <p><strong>Test Accuracy:</strong> 83.5%</p>
        <p>
          While accuracy is relatively high, this metric is somewhat misleading in imbalanced datasets. 
          Our model correctly identified the vast majority of non-fire incidents (true negatives), but 
          struggled more with fire incidents (true positives). SMOTE helped improve this by increasing recall for fires.
        </p>
        <p>
          We evaluated our model using a <strong>confusion matrix</strong>, shown below.
        </p>
      </section>

      <section className="card">
        <h2>Confusion Matrix</h2>
        <img src="/images/fire_confusion_matrix_smote.png" alt="Fire Model Confusion Matrix" className="eda-image" />
        <p>
          From the matrix, we can see that out of over 123,000 test samples, the model correctly predicted 103,628 non-fires 
          and 1,830 true fires. However, 11,179 fire incidents were misclassified as non-fires, 
          highlighting the continued difficulty of predicting minority class events.
        </p>
        <p>
          This result underscores the importance of exploring other methods (e.g., weighted loss functions or ensemble strategies) for even better performance.
        </p>
      </section>

      <section className="card">
        <h2>Top Predictive Features</h2>
        <img src="/images/fire_feature_importance_smote.png" alt="Fire Model Feature Importances" className="eda-image" />
        <p>
          The model heavily relied on <strong>hour of the day</strong> and <strong>month</strong>, which aligns with real-world expectations as many fires follow daily and seasonal behavioral patterns (e.g., cooking fires at meal times, heating fires in winter). 
          <strong>Property use codes</strong> (e.g., apartments, commercial buildings) and <strong>districts</strong> also played an important role in shaping predictions.
        </p>
        <p>
          These insights help fire departments and emergency planners understand when and where risks are higher and could inform smarter resource allocation and prevention strategies.
        </p>
      </section>

      <footer>
        <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default FireModel;
