// src/components/EDA.js
import React from 'react';
import { Element } from 'react-scroll';

function EDA() {
  return (
    <div>
      <header>
        <h1>Exploratory Data Analysis</h1>
        <p className="subheader">
          A visual overview of Boston fire incident patterns, distributions, and risk indicators.
        </p>
      </header>

      <Element name="yearly" className="card">
        <h2>Annual Fire Incident Trends (2012–2025)</h2>
        <img src="/images/incidents_by_year.png" alt="Incidents per Year" className="eda-image"/>
        <p>
          The number of reported fire-related incidents in Boston has steadily increased over the last decade, reaching a peak in 2024. This growth emphasizes the need for better resource planning, risk prevention, and data-informed dispatching.
        </p>
      </Element>

      <Element name="month" className="card">
        <h2>Monthly Incident Patterns</h2>
        <img src="/images/incidents_per_month.png" alt="Incidents per Month" className="eda-image"/>
        <p>
          Incidents show seasonal variability, with peaks in July and January. These months align with extreme temperature patterns that can increase fire risk through heating systems and summer activity.
        </p>
      </Element>

      <Element name="incident-types" className="card">
        <h2>Top 10 Fire Incident Types</h2>
        <img src="/images/top_incident_types.png" alt="Top Incident Types" className="eda-image"/>
        <p>
          The most common incidents are service-related or triggered by alarms (e.g., public service calls, unintentional activations, good intent calls). True fires represent a smaller share of overall dispatches.
        </p>
      </Element>

      <Element name="loss" className="card">
        <h2>Top Incident Types by Property Loss</h2>
        <img src="/images/property_loss_by_type.png" alt="Property Loss by Incident Type" className="eda-image"/>
        <p>
          While alarm and minor fire incidents dominate in volume, actual <strong>building fires</strong> lead in financial impact—causing over $400M in estimated damages. Other costly incidents include vehicle fires and explosions.
        </p>
      </Element>

      <Element name="neighborhoods" className="card">
        <h2>Top Neighborhoods by Incident Count</h2>
        <img src="/images/top_neighborhoods.png" alt="Top Neighborhoods" className="eda-image"/>
        <p>
          Central and historically dense neighborhoods like Boston proper, Dorchester, and Roxbury report the highest number of incidents—likely due to population density, older housing stock, and public infrastructure load.
        </p>
      </Element>

      <Element name="heatmap" className="card">
        <h2>Heatmap: Incidents by Day of Week and Hour</h2>
        <img src="/images/heatmap_day_hour.png" alt="Heatmap of Incidents" className="eda-image"/>
        <p>
          Most incidents cluster during weekday daylight hours (8AM–6PM), with midweek peaks. Early mornings and late nights show the fewest dispatches, matching sleep hours and low activity periods.
        </p>
      </Element>

      <Element name="zipcodes" className="card">
        <h2>Top Zip Codes by Incident Frequency</h2>
        <img src="/images/toptenzipcodes.png" alt="Top Zip Codes" className="eda-image"/>
        <p>
          While neighborhood analysis is insightful, breaking it down further by ZIP code highlights more granular hotspots. These findings can guide localized interventions and safety campaigns.
        </p>
      </Element>

      <footer>
         <p>Project by Adrian Kombe and Abigail Kinaro | MIT 1.001 | Spring 2025</p>
      </footer>
    </div>
  );
}

export default EDA;

