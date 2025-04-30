// src/components/Heatmap.js
import React from 'react';

function Heatmap() {
  return (
    <div className="page">
      <header>
        <h1>Heatmap: Confirmed Fires Across Boston</h1>
        <p className="subheader">Mapbox GL JS with KMeans Clustering</p>
      </header>

      <section className="card">
        <h2>What This Map Shows</h2>
        <p>
          This heatmap visualizes all confirmed fire incidents reported in Boston over the past 12 years.
          Each point represents a fire event, and clustering is applied to reveal high-density fire zones.
        </p>
        <p>
          Using KMeans clustering, we grouped incidents into key hot spots, revealing spatial concentrations of risk. 
          Heat intensity reflects the relative frequency of fire calls within that zone.
        </p>
      </section>

      <section className="card">
        <h2>Interactive Heatmap</h2>
        <div style={{ height: '600px', width: '100%', borderRadius: '12px', overflow: 'hidden' }}>
          <iframe
            src="https://your-mapbox-heatmap-url.com"
            title="Confirmed Fires Heatmap"
            width="100%"
            height="600px"
            style={{ border: "2px solid #ff6b3d", borderRadius: "10px", boxShadow: "0px 4px 10px rgba(255, 107, 61, 0.3)" }}
            allowFullScreen
          ></iframe>
        </div>
        <p style={{ marginTop: '10px' }}>
          Having issues? Open it here: <a href="https://your-mapbox-heatmap-url.com" target="_blank" rel="noopener noreferrer">Open Fullscreen</a>
        </p>
      </section>

      <footer>
        <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default Heatmap;
