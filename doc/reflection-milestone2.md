# Milestone 2 Reflection for the Global Sustainability Tracker


## What we have in our prototype


We have implemented the core interactive dashboard of the Global Sustainability Tracker Dashboard using Dash, Dash Bootstrap components and Altair.
The core functionalities are:


<ul>
  <li><b>Dynamic filtering</b></li>
  <ul>
      <li>Group selector (Continent, Country, Income Group, SDG Region)</li>
      <li>Entity selector that updates based on group</li>
      <li>Year range slider</li>
    </ul>
  <li><b>Visualizations</b></li>
    <ul>
      <li>Three charts are displayed (environment, economic, social), currently implemented as line charts rendered via Altair and embedded into Dash with iframes.</li>
    </ul>
  <li><b>KPI Cards</b></li>
    <ul>
      <li>CO₂ Emissions, GDP, Natural Resource Depletion, Inflation, Women in Parliament, Life Expectancy, and Regime Type.</li>
      <li>KPIs compute the mean for the most recent year in the selected range and compare it to the previous year, showing percent change with positive/negative styling.</li>
      <li>Large-number formatting (K/M/B) is implemented for GDP and CO₂.</li>
    </ul>
  <li><b>Design / styling</b></li>
    <ul>
      <li>Custom CSS for a card-based layout, hover effects, and consistent color/theme choices.</li>
    </ul>
</ul>




## What is not implemented yet

There are several more features and design improvements that are still in development.

**Visualization Components**
-	The main visualization was intended to be a bubble chart (three variables), but is currently implemented as a line chart.
-	Line charts are working, but we have not implemented multi-variable chart interactions (e.g., choosing x/y/size for bubble plots).
-	Multi-entity comparison (e.g., comparing two countries or two continents side-by-side) is not yet supported.


**UI Components (Layout & Usability)**

-	Card alignment is not fully consistent (some KPI/chart card heights and spacing differ).
-	Titles and chart headers still need alignment/formatting cleanup
-	Dropdown text can be truncated; users cannot always see full parameter names easily.
-	The page requires scrolling; we plan to improve layout so the experience feels more “locked” and dashboard-like.
-	Captions/labels are not yet explained clearly (users may not know what each metric means or why it matters).


  
**Data components (Cleaning, Features & Enrichment)**
-	Country flags beside the country selector would be a nice improvement
-	Feature engineering is partially implemented (K/M/B formatting exists), but needs to be standardized across metrics (e.g., consistent “GDP in billions” display).
-	Missing data handling is minimal; some entities/years may produce gaps or “-” outputs rather than a clear message explaining why.



