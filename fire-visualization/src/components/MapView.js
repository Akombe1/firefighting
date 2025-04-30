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
          This interactive 3D map visualizes fire activity across Boston, animating year-by-year fire incidents from 2012 to 2024. 
          It uses building height, camera tilt, and fire emoji markers to dynamically highlight spatial fire patterns over time.
        </p>
        <p>
          The map is built with Mapbox GL JS and leverages CSV-based location data processed through PapaParse. 
          Each fire is represented with a marker, and the animation progresses chronologically.
        </p>
      </section>

      <section className="card">
        <h2>Explore the 3D Map</h2>
        <iframe
          src="/maps/index.html"
          title="Boston Fire 3D Map"
          width="100%"
          height="600px"
          loading="lazy"
          style={{
            border: "2px solid #ff6b3d",
            borderRadius: "10px",
            boxShadow: "0px 4px 10px rgba(255, 107, 61, 0.3)",
          }}
          allowFullScreen
        ></iframe>
      </section>

      <footer>
        <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default MapView;