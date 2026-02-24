# Dashboard Application Architecture (`src/app.py`)

This document provides a breakdown of how the `app.py` script functions to create the interactive Dash dashboard.

## 1. Imports and Setup
The script begins by importing necessary libraries:
- `dash` and related modules (`dcc`, `html`, `Input`, `Output`) for building the web application framework and reactive components.
- `dash_bootstrap_components` (`dbc`) for applying a Bootstrap styling system (grid layout, pre-styled components).
- `pandas` for handling the loaded dataset as a DataFrame.
- `altair` for creating the interactive charts and visualizations.

## 2. Data Loading and Preprocessing
- **`DATA_PATH`**: The script constructs an absolute path to the dataset located at `data/raw/WorldSustainabilityDataset.csv` using Python's `os` module.
- It then uses `pd.read_csv()` to load the data.
- **`col_mapping`**: To make the code cleaner and the dashboard labels easier to read, long, complex column names (like `"Annual production-based emissions of carbon dioxide (CO2)..."`) are renamed to simpler variables (like `"CO2_Emissions"`).
- Rows missing a `Continent` assignment are dropped, and the `Year` column is cast to DateTime objects to ensure proper time-series rendering in charts later.

## 3. Application Initialization and Styling
- The script initializes the Dash app: `app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])`.
- Custom CSS logic is injected via `app.index_string`. This CSS block defines how the "Cards" (the white boxes holding charts and KPIs) look. It includes premium aesthetics such as:
  - Importing the **Inter Google Font**.
  - A subtle **glassmorphism/floating effect** with `#f0f4f8` background, drop shadows, and rounded borders.
  - Hover micro-animations so cards float upwards.
  - Distinct **purple borders** (`2px solid #8b5cf6` and `6px` top accent) framing all KPI values.

## 4. Layout Structure (`app.layout`)
Dash uses a declarative component tree to build the UI, mapping directly to HTML. The layout is wrapped in a Bootstrap `dbc.Container`:

### The Grid System
- **Rows and Columns**: The dashboard is divided into distinct sections using `dbc.Row` and `dbc.Col`. Boostrap uses a 12-column grid system. For instance, `md=4` means a column takes up 4/12 (one-third) of the screen width on medium and larger devices.

### Section Breakdown
1. **Top Row**: Contains the `Group`, `Selection` dropdown menus (using `dcc.Dropdown`), and a `Year Range` slider (using `dcc.RangeSlider`) on the left half (`md=6`), and the three large, top KPI cards (CO2 Emissions, GDP, Natural Resource Depletion) on the right half.
2. **Bottom Row**:
   - **Left**: The large "Environment Factors" chart taking up half the width (`md=6`). It includes its own inner dropdown to toggle the metric being viewed.
   - **Middle**: Two vertically stacked smaller charts ("Economic Trackers" and "SDG Tracker") taking up one-third of the width (`md=4`), each with their own metric toggles.
   - **Right**: Four vertically stacked "Side KPIs" (Inflation, Regime Type, Women Representation, Health) taking up the remaining width (`md=2`).

## 5. Reactivity (The `@app.callback` Decorators)
Callbacks are the heart of Dash. They map inputs (like a user changing a dropdown) to outputs (like a chart rendering new data or a text value updating). 

### First Callback: `update_entity_options`
- **Inputs**: The user selects a specific `Group` from the first dropdown (e.g., "Country" or "Continent").
- **Logic**: It looks at the selected column in the dataset, extracts all unique, valid values, and alphabetically sorts them.
- **Outputs**: It updates the label above the second dropdown and populates its internal selectable options. For instance, if you pick "Continent", the options become a list of continents. If you pick "Country", the options become a list of all countries. It then defaults the selection to the first item in that list.

### Second Callback: `update_dashboard`
- **Inputs**: Listens to the selection from the second dropdown (the specific `entity`), the `year_range` from the slider, as well as the metric selections for the three different line charts.
- **Logic**:
  - Filters the entire pandas DataFrame down to only rows matching the selected entity and the selected year range (`filtered = df_filtered[(df_filtered[group] == entity) & (df_filtered['Year'].dt.year >= year_range[0]) & ...]`).
  - Passes this filtered data to the `get_line_chart()` helper function to generate the HTML for the three Altair charts.
  - Extracts the data for the most recent year (`curr`) and the year prior (`prev`) in the filtered dataset for that specific entity.
  - Passes these values through helper functions (`calc_kpi_large` and `calc_kpi`) to calculate the percentage change contextually and format the text properly (e.g., adding "B" for billions).
- **Outputs**: It returns 16 different values simultaneously! These values update the `srcDoc` (HTML content) of the three chart iframes, and update the `<H3>` and subtext components of the 6 different KPI cards on the dashboard.

## 6. Chart Generation (`get_line_chart`)
This helper function takes filtered data and the specific `y_col` metric requested. It uses the `altair` library to create a line chart showing the progression over `Year`. It sets styling rules (removing gridlines, hiding axes labels, coloring) and then uses `.to_html()` to convert the interactive Javascript/HTML chart into a string that Dash can insert directly into the webpage's iframe container.
