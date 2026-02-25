TAs idea:
-	One type of visualization right now
o	Bubble chart -> three variables
o	Main chart is the bubble chart with the three variables
	Line charts will be on the side panel
-	Add the flag of the country to the little county toggle
-	Alignment of the card be the same
o	UI thing
-	Need to scroll down, maybe make it locked
o	UI
-	What do the captions mean?
-	Fix alignment of titles
-	See all the parameter text in the drop downs
-	Feature engineering -> billion



# Milestone 2 Reflection for the Global Sustainability Tracker


## What we have in our prototype


We have implemented the core interactive dashboard of the Global Sustainability Tracker Dashboard using Dash, Dash Bootstrap components and Altair.
The core functionalities are:

-	Dynamic filtering 
  o	Group selector (Continent, Country, Income Group, SDG Region)
  o	Entity selector that updates based on group
  o	Year range slider
-	Visualizations
  o	Three charts are displayed (environment, economic, social), currently implemented as line charts rendered via Altair and embedded into Dash with iframes.
-	KPI Cards
  o	CO₂ Emissions, GDP, Natural Resource Depletion, Inflation, Women in Parliament, Life Expectancy, and Regime Type.
  o	KPIs compute the mean for the most recent year in the selected range and compare it to the previous year, showing percent change with positive/negative styling.
  o	Large-number formatting (K/M/B) is implemented for GDP and CO₂.
-	Design / styling
  o	Custom CSS for a card-based layout, hover effects, and consistent color/theme choices.


