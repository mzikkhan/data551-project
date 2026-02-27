# 🌍 Global Sustainability Tracker

🔗 **Live Dashboard:** *(https://sustainability-dashboard-1fd6.onrender.com/)*  
📊 Interactive visualization of global sustainability trends (2000–2018)

![Dashboard Sketch - Comparative Map View](screen_2.png)

---

## 📌 Table of Contents

- [Overview](#overview)
- [Motivation](#motivation)
- [What You Can Do With This Dashboard](#what-you-can-do-with-this-dashboard)
- [Key Features](#key-features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [For Contributors](#for-contributors)
- [Future Improvements](#future-improvements)
- [Why This Project Matters](#what-you-can-do-with-this-dashboard)

---

## Overview

The **Global Sustainability Tracker** is an interactive dashboard designed to explore trade-offs between economic growth, environmental impact, and social development across countries from **2000–2018**.

It integrates:

- 🌱 Environmental indicators (CO₂ emissions, forest depletion)
- 💰 Economic metrics (GDP, inflation)
- 🎯 UN Sustainable Development Goals (health, gender equality, energy access)

This tool helps users examine whether economic growth is aligned with long-term sustainability.

---

## Motivation

Economic expansion often comes at environmental and social costs. Policymakers, researchers, and NGOs need accessible tools to understand:

- Are countries growing sustainably?
- Is GDP growth correlated with higher emissions?
- How do development indicators vary across income groups?

This dashboard makes those trade-offs visible and interactive, enabling deeper insight into global development patterns.

---

## What You Can Do With This Dashboard

This app is designed for:

- 📊 Researchers exploring sustainability trends  
- 🌍 Policy analysts comparing regional development  
- 📈 Students learning about global economic-environment trade-offs  

With the dashboard, you can:

- Filter by **continent, country, region, or income group**
- Track **time-series trends (2000–2018)**
- Compare environmental vs economic indicators
- View global patterns via an interactive choropleth map
- Toggle between multiple sustainability metrics dynamically

No technical knowledge required — simply use the dropdown menus and filters.

---

## Key Features

### 1️⃣ Deep-Dive Country View

- KPI summary cards (GDP, CO₂, resource depletion)
- Year-over-year percentage changes
- Three synchronized time-series charts:
  - Environment
  - Economy
  - SDG indicators
- Internal dropdowns to switch variables

---

### 2️⃣ Comparative Analysis via Interactive Map

- Global choropleth map
- Income-level filtering
- Year-range selection
- Cross-country comparison
- Distribution plots (GDP vs CO₂)
- Trend comparison panels

This dual-view design allows both:

- Micro-level country analysis
- Macro-level global benchmarking

---

## Installation

To install the app locally:
      ```
      pip install -r requirements.txt
      ```

To run the app locally:
      ```
      python src/app.py
      ```

The dashboard will be available at `http://127.0.0.1:8050`.

---

## Project Structure

```bash
├── data/                # Cleaned dataset files
├── src/
│   ├── app.py           # Main Dash application
│   ├── components/      # Reusable dashboard components
│   ├── utils/           # Data processing functions
├── requirements.txt
├── README.md
```
---

## For Contributors

We welcome contributions!

If you're interested in improving the project, here’s how you can help:

### 🛠 Areas for Improvement

- Improve UI/UX design consistency
- Add more SDG indicators
- Improve map interactivity (hover insights, dynamic scaling)
- Optimize callback performance
- Add unit tests
- Deploy via Docker or cloud hosting

---

### 🚀 How to Run Locally

1. Clone the repository

2. Create a virtual environment

3. Install dependencies

4. Run `python src/app.py`

---

### 📌 Suggested Workflow

- Create a new branch
- Make changes
- Submit a pull request
- Include clear commit messages

---

## Future Improvements

- Add predictive sustainability scoring
- Include carbon intensity metrics
- Enable country-to-country side-by-side comparison panel
- Add export functionality (CSV/PDF)
- Add animation across time

---

## Why This Project Matters

Sustainability is one of the defining challenges of our generation.

This dashboard helps make complex development trade-offs transparent, measurable, and actionable.

By combining economic, environmental, and social metrics into a single interactive interface, we aim to promote data-driven global awareness.
