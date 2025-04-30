// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './components/Home';
import EDA from './components/EDA';
import FireModel from './components/FireModel';
import CategoryModel from './components/CategoryModel';
import BackToTop from './components/BackToTop';
import MapView from './components/MapView';
import HowTo from './components/HowTo';
import Heatmap from './components/Heatmap';

import './App.css';

function App() {
  return (
    <Router>
      <div className="container">
        {/* Navbar */}
        <nav className="navbar">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/eda" className="nav-link">EDA Plots</Link>
          <Link to="/fire-model" className="nav-link">Fire Model</Link>
          <Link to="/category-model" className="nav-link">Category Model</Link>
          <Link to="/heatmap" className="nav-link">Heatmap</Link>
          <Link to="/map" className="nav-link">3D Map</Link>
          <Link to="/how-to" className="nav-link">How to Run</Link>
        </nav>

        {/* Routes */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/eda" element={<EDA />} />
          <Route path="/fire-model" element={<FireModel />} />
          <Route path="/category-model" element={<CategoryModel />} />
          <Route path="/heatmap" element={<Heatmap />} />
          <Route path="/map" element={<MapView />} />
          <Route path="/how-to" element={<HowTo />} />
        </Routes>

        <BackToTop />
      </div>
    </Router>
  );
}

export default App;
