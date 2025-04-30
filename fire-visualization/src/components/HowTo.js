// src/components/HowTo.js
import React from 'react';

function HowTo() {
  return (
    <div className="page">
      <header>
        <h1>How to Use This Project</h1>
        <p className="subheader">Installation, Setup, and Project Structure</p>
      </header>

      <section className="card">
        <h2>Overview</h2>
        <p>
          This project combines Python scripts for machine learning and data processing with a React-based website for visualization.
          It predicts fire incident categories and fire likelihood using historical Boston fire incident data, enhanced with EDA, SMOTE, and geospatial overlays.
        </p>
      </section>

      <section className="card">
        <h2>Project Structure Overview</h2>
        <p>The project is organized into the following sections:</p>
        <ul>
          <li><code>Fire_Data/</code>: Contains all scripts and datasets for merging, training, and evaluation</li>
          <li><code>models/</code>: Stores saved model <code>.pkl</code> files</li>
          <li><code>plots/</code>: Stores generated visualizations used on the website</li>
          <li><code>fireData.csv</code>: Cleaned and merged dataset used for training</li>
        </ul>
      </section>

      <section className="card">
        <h2>How to Run the Python Code</h2>
        <p>
          You'll need Python 3.9+ and these dependencies:
        </p>
        <code>
          pip install pandas matplotlib seaborn scikit-learn imbalanced-learn joblib
        </code>
        <ul>
          <li><strong>Step 1:</strong> Generate or update <code>fireData.csv</code> using <code>1.merging.py</code></li>
          <li><strong>Step 2:</strong> Run EDA: <code>python3 2.fireEDA.py</code></li>
          <li><strong>Step 3:</strong> Train fire model: <code>python3 5.trainFire_SMOTE.py</code></li>
          <li><strong>Step 4:</strong> Train category model: <code>python3 7.trainCategory_SMOTE.py</code></li>
          <li><strong>Step 5:</strong> Save plots:
            <ul>
              <li><code>python3 6.fireModelPlots_SMOTE.py</code></li>
              <li><code>python3 8.categoryModelPlots_SMOTE.py</code></li>
            </ul>
          </li>
        </ul>
      </section>

      <section className="card">
        <h2>Run the Website Locally</h2>
        <p>
          The React website is inside <code>/fire-visualization</code>. Use the following steps:
        </p>
        <code>
          cd fire-visualization
          <br />
          npm install
          <br />
          npm start
        </code>
        <p>This starts a local server at <code>http://localhost:3000</code></p>
      </section>

      <section className="card">
        <h2>Dependencies</h2>
        <p>
          <strong>Python:</strong> pandas, seaborn, matplotlib, scikit-learn, joblib, imbalanced-learn
          <br />
          <strong>JavaScript:</strong> React, React Router, React Scroll, Mapbox GL (optional for maps)
        </p>
      </section>

      <section className="card">
        <h2>Notes</h2>
        <ul>
          <li>Models are pre-trained and saved in the <code>/models</code> directory.</li>
          <li>Plots are located in the <code>/plots</code> folder and used in the website UI.</li>
          <li>The site is static and does not auto-update plots; Python scripts must be run manually.</li>
        </ul>
      </section>

      <footer>
        <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default HowTo;