# Proposal and Data Structure

## 1. Motivation and Purpose

Often times policymakers, sustainability analysts, and economists are tasked with developing policies related to sustainability. In addition to sustainability, they must also consider economic growth, environmental degradation, and social development. Ideally, they would aim to support policies that positively impact all three areas.

However, identifying trends and potential correlations between these domains is difficult when they are analyzed in isolation. This makes it challenging to understand trade-offs and broader systemic patterns.

We propose building the **Global Sustainability Tracker**, an interactive dashboard that allows policymakers to explore sustainability metrics at the country level while comparing them alongside economic and social indicators over time.

The dashboard will enable users to investigate relationships between variables such as:

- Carbon emissions  
- GDP  
- Social representation  

This will help users form hypotheses about development trajectories and trade-offs. The application is designed to support exploratory analysis and informed decision-making.

---

## 2. Description of the Data

We will use the **World Sustainability Dataset** (sourced from Kaggle/TrueCue), which tracks 173 countries over a 19-year period. The dataset contains 54 variables grouped into three high-level categories:

### Environmental Indicators

- CO₂ emissions (total and per capita)
- CO₂ damage as % of Gross National Income
- Energy use
- Other climate-related metrics

### Economic Indicators

- GDP
- Gross National Income
- Income group
- Macroeconomic indicators

### Societal Indicators

- Women's representation in parliament and business
- Education-related variables
- Social development metrics

Because the dataset is wide and contains missing values, we will focus on a selected subset of variables.

We will also derive:

- Normalized metrics (e.g., emissions per capita)
- Rolling trends

---

## 3. Research Questions and Usage Scenarios

**Target Audience:**  
International Development Analysts, Environmental Policy Researchers, and NGO Program Managers.

### Core Research Questions

- Do increases in GDP coincide with increases or decreases in CO₂ emissions?
- Are there countries where economic growth has decoupled from emissions?
- Does CO₂ damage (% of GNI) appear economically significant?
- Are social development metrics improving even when environmental indicators worsen?
- Did major global shocks (e.g., the 2008 financial crisis) produce synchronized changes across domains?
- **Trade-off Analysis:** Does rapid economic growth (rising GDP) historically correlate with increased environmental degradation (CO₂ damage and resource depletion) in developing nations?
- **Resource Dependence:** How do countries with high natural resource rents perform in social metrics? Do they experience the "resource curse," lagging in life expectancy or gender equality despite economic gains?
- **SDG Progress:** Are specific regions on track to meet UN Sustainable Development Goals (e.g., SDG 7: Energy Access and SDG 13: Climate Action), or are improvements in one area masking declines in another?

---

## Usage Scenario

### Persona

**Amira**, a policy analyst working at an international development agency, has been tasked with proposing a new composite sustainability metric to help prioritize countries for climate-transition funding.

Before designing this metric, she needs to understand:

- Where environmental degradation is economically damaging
- Whether economic growth appears tied to rising emissions
- Whether social development indicators move independently of environmental performance
- Which countries exhibit unusual patterns
