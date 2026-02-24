# Milestone 2 Reflection

## Implementation Status

We have implemented a prototype of the **Global Sustainability Tracker** dashboard as proposed. The dashboard successfully loads sustainability data and allows users to explore macroeconomic and environmental indicators interactively.

### What is currently implemented:
- **Interactive Scatter Plot**: Allows exploring the relationship between GDP and CO2 emissions using logarithmic scales.
- **Bar Chart**: Visualizes the average CO2 damage as a percentage of GNI across different continents over time.
- **Line Chart**: Tracks the mean percentage of women in parliament by region over time.
- **Filtering Mechanisms**: We have integrated a year range slider and a continent multi-select dropdown that dynamically update all visualizations simultaneously.

### What is not yet implemented (Limitations and Future Work):
- **Predictive/Composite Metrics**: The proposal mentioned creating composite sustainability metrics or deriving trends, which are not completely fleshed out yet.
- **Handling Missing Data**: Missing values for certain indicators cause issues when creating plots. The current state utilizes strict dropping, meaning we may be missing countries and regions that lack consistent reporting on factors like GDP and CO2 emissions. We plan to implement imputation strategies or show clear indicators when data is unavailable.
- **Layout and Refinement**: The visual alignment using Bootstrap could be further improved. Tooltips show standard numerical values without pretty formatting (e.g. adding the dollar sign or commas). 

Overall, the core structure is functional, and the interactivity works, allowing us to build out the remaining functionality effectively in the upcoming milestones.
