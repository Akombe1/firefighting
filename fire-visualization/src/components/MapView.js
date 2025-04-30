// src/components/MapView.js
import React from 'react';

function MapView() {
  return (
    <div className="page">
      <header>
        <h1>3D Map: Fire Risk Visualization</h1>
        <p className="subheader">Built with Mapbox GL JS</p>
      </header>

      <section className="card">
        <h2>About the Visualization</h2>
        <p>
          This interactive 3D map overlays fire incident predictions onto a geospatial model of Boston using Mapbox.
          It allows viewers to explore spatial patterns in emergency response and incident severity across time and neighborhoods.
        </p>
        <p>
          We use geo-referenced fire data, paired with property use and time-of-day signals, to visualize hot zones for likely fire events.
        </p>
      </section>

      <section className="card">
        <h2>Explore the 3D Map</h2>
        <div style={{ height: '600px', width: '100%', borderRadius: '12px', overflow: 'hidden' }}>
          <iframe
            src="https://your-mapbox-url.com"
            title="Mapbox 3D Fire Risk Map"
            width="100%"
            height="600px"
            style={{ border: "2px solid #ff6b3d", borderRadius: "10px", boxShadow: "0px 4px 10px rgba(255, 107, 61, 0.3)" }}
            allowFullScreen
          ></iframe>
        </div>
        <p style={{ marginTop: '10px' }}>
          Trouble loading? Try this link: <a href="https://your-mapbox-url.com" target="_blank" rel="noopener noreferrer">Open Fullscreen</a>
        </p>
      </section>

      <footer>
        <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default MapView;

