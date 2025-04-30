// src/components/Home.js
import React from 'react';

function Home() {
  return (
    <div className="page">
  <h1>The Future of Fire: Boston Fire Incident Prediction</h1>
  <p>
    Each year, fire departments across the United States respond to hundreds of thousands of emergencies, many of which are preventable or influenced by spatial and temporal risk factors. In 2024 alone, over 3,500 lives were lost to fire-related events, with more than 57,000 fires caused by human activity, burning over 4.6 million acres. This project seeks to help prevent such outcomes by using machine learning to better understand and ultimately predict emergency fire response patterns in urban environments.
  </p>

  <p>
    Our work focuses on Boston, MA, where we used open-source datasets from the City of Boston and NFIRS (National Fire Incident Reporting System), spanning 2012 through March 2025. We merged fire response records, property datasets (including proposed structures), and geospatial coordinates to build a predictive model and accompanying visualization platform.
  </p>

  <section className="card">
    <h2>Methodology</h2>
    <p>
      Our process began by merging over 600,000 incident records from multiple city sources and cleaning the data. We standardized timestamps, extracted incident types, and engineered features such as month, hour, day of week, zip code, district, and property use category. We also translated addresses to latitude/longitude coordinates using geocoding, enabling geospatial analysis and map-based visualization.
    </p>

    <p>
      We trained two machine learning models using Random Forest classifiers:
    </p>
    <ul>
      <li><strong>Binary Fire Prediction:</strong> Predicts whether a given incident will be a fire</li>
      <li><strong>Multiclass Incident Category Prediction:</strong> Classifies incidents into NFIRS categories (e.g., alarms, service calls, structural fires)</li>
    </ul>
    <p>
      Due to severe class imbalance where fires are rare compared to false alarms, we applied <strong>SMOTE (Synthetic Minority Oversampling Technique)</strong> to generate synthetic examples of the minority class and ensure more balanced learning.
    </p>
  </section>

  <section className="card">
    <h2>Results</h2>
    <ul>
      <li><strong>Fire Prediction Model:</strong> 83.5% accuracy after SMOTE, with hour, month, and day of week as the top predictive features</li>
      <li><strong>Category Prediction Model:</strong> 39.7% accuracy across 8 major emergency categories — strongest on service calls and false alarms</li>
    </ul>
    <p>
      We evaluated model performance using confusion matrices and feature importance plots, all visualized within this site.
    </p>
  </section>

  <section className="card">
    <h2>Interactive Map</h2>
    <p>
      We also geocoded and visualized the full dataset on a Mapbox-powered interactive map. Users can explore fire incidents across Boston’s built environment, including both current and proposed structures, to better understand neighborhood-level risk patterns.
    </p>
  </section>

  <div className="cta-buttons">
    <a href="/eda" className="nav-link">View EDA</a>
    <a href="/fire-model" className="nav-link">Fire Model</a>
    <a href="/category-model" className="nav-link">Category Model</a>
    <a href="/map" className="nav-link">Fire Map</a>
  </div>

  <footer>
    <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
  </footer>
</div>

  );
}

export default Home;

