import dash
from dash import dcc, html, Input, Output
import pandas as pd
import altair as alt
import os

# Set working directory to project root or adjacent to src so it can find data
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'WorldSustainabilityDataset.csv')

# Load dataset
df = pd.read_csv(DATA_PATH)

# Clean/prepare columns (some names are long)
# Simplify names for ease of use in plotting
col_mapping = {
    'Access to electricity (% of population) - EG.ELC.ACCS.ZS': 'Elec_Access',
    'GDP (current US$) - NY.GDP.MKTP.CD': 'GDP',
    'Annual production-based emissions of carbon dioxide (CO2), measured in million tonnes': 'CO2_Emissions',
    'Life expectancy at birth, total (years) - SP.DYN.LE00.IN': 'Life_Exp',
    'Proportion of seats held by women in national parliaments (%) - SG.GEN.PARL.ZS': 'Women_Parliament',
    'Adjusted savings: carbon dioxide damage (% of GNI) - NY.ADJ.DCO2.GN.ZS': 'CO2_Damage_GNI'
}
df.rename(columns=col_mapping, inplace=True)

import dash_bootstrap_components as dbc

# Drop rows where critical variables are completely missing to speed up drawing (or fill)
focus_cols = ['Country Name', 'Year', 'Continent', 'GDP', 'CO2_Emissions', 'Women_Parliament', 'CO2_Damage_GNI']
df_filtered = df[focus_cols].dropna(subset=['GDP', 'CO2_Emissions', 'Continent'])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(className='container mt-4', children=[
    html.Div(className='row mb-4', children=[
        html.Div(className='col-12', children=[
            html.H1("Global Sustainability Tracker", className='text-center fw-bold'),
            html.P("Explore relationships between economic growth, environmental degradation, and social development.", className='text-center text-muted')
        ])
    ]),
    
    html.Div(className='row mb-4', children=[
        html.Div(className='col-md-4', children=[
            html.Label("Select Year Range:"),
            dcc.RangeSlider(
                id='year-slider',
                min=df_filtered['Year'].min(),
                max=df_filtered['Year'].max(),
                value=[2005, 2015],
                marks={str(year): str(year) for year in range(int(df_filtered['Year'].min()), int(df_filtered['Year'].max())+1, 2)},
                step=1
            )
        ]),
        html.Div(className='col-md-4', children=[
            html.Label("Select Continent(s):"),
            dcc.Dropdown(
                id='continent-dropdown',
                options=[{'label': c, 'value': c} for c in df_filtered['Continent'].dropna().unique()],
                value=list(df_filtered['Continent'].dropna().unique())[:2],
                multi=True
            )
        ])
    ]),
    
    html.Div(className='row', children=[
        html.Div(className='col-md-6', children=[
            html.H4("GDP vs CO2 Emissions"),
            html.Iframe(
                id='scatter-plot',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}
            )
        ]),
        html.Div(className='col-md-6', children=[
            html.H4("CO2 Damage over Time by Continent"),
            html.Iframe(
                id='bar-plot',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}
            )
        ])
    ]),
    
    html.Div(className='row mt-4', children=[
        html.Div(className='col-md-12', children=[
            html.H4("Women in Parliament over Time"),
            html.Iframe(
                id='line-plot',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}
            )
        ])
    ])
])

@app.callback(
    Output('scatter-plot', 'srcDoc'),
    [Input('year-slider', 'value'),
     Input('continent-dropdown', 'value')]
)
def update_scatter_plot(year_range, continents):
    if not continents:
        return ""
    filtered = df_filtered[
        (df_filtered['Year'] >= year_range[0]) & 
        (df_filtered['Year'] <= year_range[1]) &
        (df_filtered['Continent'].isin(continents))
    ]
    if filtered.empty:
        return ""
    
    chart = alt.Chart(filtered).mark_circle(size=60, opacity=0.7).encode(
        x=alt.X('GDP:Q', scale=alt.Scale(type='log'), title='GDP (Log Scale US$)'),
        y=alt.Y('CO2_Emissions:Q', scale=alt.Scale(type='log'), title='CO2 Emissions (Log Scale)'),
        color='Continent:N',
        tooltip=['Country Name', 'Year', 'GDP', 'CO2_Emissions']
    ).properties(
        width='container',
        height=300
    ).interactive()
    return chart.to_html()

@app.callback(
    Output('bar-plot', 'srcDoc'),
    [Input('year-slider', 'value'),
     Input('continent-dropdown', 'value')]
)
def update_bar_plot(year_range, continents):
    if not continents:
        return ""
    filtered = df_filtered[
        (df_filtered['Year'] >= year_range[0]) & 
        (df_filtered['Year'] <= year_range[1]) &
        (df_filtered['Continent'].isin(continents))
    ]
    if filtered.empty:
        return ""
        
    chart = alt.Chart(filtered).mark_bar().encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('mean(CO2_Damage_GNI):Q', title='Mean CO2 Damage (% GNI)'),
        color='Continent:N',
        tooltip=['Continent', 'Year']
    ).properties(
        width='container',
        height=300
    ).interactive()
    return chart.to_html()

@app.callback(
    Output('line-plot', 'srcDoc'),
    [Input('year-slider', 'value'),
     Input('continent-dropdown', 'value')]
)
def update_line_plot(year_range, continents):
    if not continents:
        return ""
    filtered = df_filtered[
        (df_filtered['Year'] >= year_range[0]) & 
        (df_filtered['Year'] <= year_range[1]) &
        (df_filtered['Continent'].isin(continents))
    ]
    if filtered.empty:
        return ""
        
    chart = alt.Chart(filtered).mark_line(point=True).encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('mean(Women_Parliament):Q', title='Mean Women in Parliament (%)'),
        color='Continent:N',
        tooltip=['Continent', 'Year']
    ).properties(
        width='container',
        height=300
    ).interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run(debug=True, port=8050)
