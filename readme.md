# Global Sustainability Tracker

**[View Dashboard](https://sustainability-dashboard-1fd6.onrender.com/)**

## Table of Contents

1. [Overview](#overview)
2. [Motivation and Purpose](#motivation-and-purpose)
3. [Installation](#installation)
4. [What You Can Do With This Dashboard](#what-you-can-do-with-this-dashboard)
5. [Folder Structure](#folder-structure)
6. [For Contributors](#for-contributors)

---

## Overview
The **Global Sustainability Tracker** is an interactive dashboard designed to explore trade-offs between economic growth, environmental impact, and social development across countries from **2000–2018**.

It integrates:

- 🌱 Environmental indicators (CO₂ emissions, forest depletion)
- 💰 Economic metrics (GDP, inflation)
- 🎯 UN Sustainable Development Goals (health, gender equality, energy access)

This tool helps users examine whether economic growth is aligned with long-term sustainability.

## Motivation and Purpose
The **Global Sustainability Tracker** is an interactive visualization tool designed to help researchers, policy makers, and NGOs explore the "World Sustainability Dataset" (2000–2018). Its primary objective is to highlight the complex trade-offs between a nation's rapid economic expansion and its corresponding environmental and social footprints. By visualizing these three critical dimensions side-by-side, users can critically assess whether a country’s development is truly sustainable or if it comes at the significant cost of natural resource depletion and ecological damage.

### Interface Design
The dashboard's primary view, as sketched below, provides a deep dive into the sustainability metrics of a single country, region, continent, or income group. The interface is organized into a grid layout featuring three main functional areas:

- **Global Filters & Navigation:** Located at the top-left, a dedicated control panel allows users to filter the entire dashboard by **Continent** and **Country/Entity**. This enables seamless switching between broad regional comparisons and deep-dive analyses of specific nations.
- **Key Performance Indicators (KPIs):** The top row features high-level "snapshot" cards for the selected entity, showcasing metrics like CO₂ Emissions, GDP, and Natural Resource Depletion. These cards dynamically include year-over-year percentage changes, color-coded to provide an immediate visual assessment of developmental trajectories.
- **Multi-Dimensional Trend Analysis:** The core of the dashboard consists of three synchronized time-series charts. These allow users to observe correlations across different domains:
    - **Environment Factors:** Tracks ecological damage metrics such as CO₂ damage and forest depletion.
    - **Economic Trackers:** Monitors financial indicators including GDP growth and inflation rates.
    - **SDG Tracker:** Visualizes progress on United Nations Sustainable Development Goals, specifically focusing on health, gender equality, and energy access.

Each chart panel features internal dropdown menus, allowing users to toggle specific variables within that theme to test hypotheses.

![Dashboard Sketch - Single Entity Analysis](screen_1.png)

### Installation

To install the app locally:
      ```
      pip install -r requirements.txt
      ```


To run the app locally:
      ```
      python src/app.py
      ```


The dashboard will be available at `http://127.0.0.1:8050`.

### Comparative Analysis via Interactive Map
In addition to the deep-dive view, the app provides a comparative mode visualized through an interactive map interface. This feature allows users to select and compare two different countries or regions side-by-side. By leveraging a spatial visualization, users can identify regional clusters of sustainability trends and benchmark the performance of nations. This dual-view approach ensures that both micro-level details and macro-level global patterns are easily accessible to the user.

![Dashboard Sketch - Comparative Map View](screen_2.png)

---

### What You Can Do With This Dashboard

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

## Folder Structure

```
sustainability_dashboard/
├── data/
│   └── raw/               
├── doc/                   
│   ├── proposal.md
│   ├── reflection-milestone2.md
│   └── team-contract.md
├── reports/       
│   ├── Milestone 1.ipynb
│   ├── Milestone 2.ipynb
│   └── explorer.ipynb
├── src/                   
│   └── app.py
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── Procfile
├── README.md
├── environment.yaml
└── requirements.txt
```

---

## For Contributors

We welcome contributions!

If you're interested in improving the project, here’s how you can help:

#### 🛠 Areas for Improvement

- Improve UI/UX design consistency
- Add more SDG indicators
- Improve map interactivity (hover insights, dynamic scaling)
- Optimize callback performance
- Add unit tests

#### 🚀 How to Run Locally

1. Clone the repository

2. Create a virtual environment

3. Install dependencies

4. Run `python src/app.py`

### 📌 Suggested Workflow

- Create a new branch
- Make changes
- Submit a pull request
- Include clear commit messages


