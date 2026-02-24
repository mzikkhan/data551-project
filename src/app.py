import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import altair as alt
import os

# Base path
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'WorldSustainabilityDataset.csv')
df = pd.read_csv(DATA_PATH)

# Clean/prepare columns
col_mapping = {
    'Country Name': 'Country',
    'Access to electricity (% of population) - EG.ELC.ACCS.ZS': 'Elec_Access',
    'GDP (current US$) - NY.GDP.MKTP.CD': 'GDP',
    'Annual production-based emissions of carbon dioxide (CO2), measured in million tonnes': 'CO2_Emissions',
    'Life expectancy at birth, total (years) - SP.DYN.LE00.IN': 'Life_Exp',
    'Proportion of seats held by women in national parliaments (%) - SG.GEN.PARL.ZS': 'Women_Parliament',
    'Adjusted savings: carbon dioxide damage (% of GNI) - NY.ADJ.DCO2.GN.ZS': 'CO2_Damage_GNI',
    'Adjusted savings: natural resources depletion (% of GNI) - NY.ADJ.DRES.GN.ZS': 'Nat_Res_Depletion',
    'Inflation, consumer prices (annual %) - FP.CPI.TOTL.ZG': 'Inflation',
    'Regime Type (RoW Measure Definition)': 'Regime_Type',
    'Income Classification (World Bank Definition)': 'Income_Group',
    'World Regions (UN SDG Definition)': 'SDG_Region'
}
df.rename(columns=col_mapping, inplace=True)

# Drop rows missing Continent
df_filtered = df.dropna(subset=['Continent', 'Year'])
df_filtered['Year'] = pd.to_datetime(df_filtered['Year'], format='%Y')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Custom CSS for styling cards
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body { background-color: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            .kpi-card { background-color: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #e9ecef; }
            .chart-card { background-color: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 20px; border: 1px solid #e9ecef; min-height: 400px; }
            .kpi-title { font-size: 0.9rem; font-weight: 600; color: #1a237e; margin-bottom: 10px; }
            .kpi-value { font-size: 1.8rem; font-weight: bold; margin-bottom: 0; }
            .kpi-sub { font-size: 0.8rem; color: #6c757d; }
            .kpi-change { font-size: 0.8rem; font-weight: bold; }
            .kpi-positive { color: #28a745; }
            .kpi-negative { color: #dc3545; }
            .chart-title { font-size: 1.1rem; font-weight: 600; color: #1a237e; }
            .dropdown-label { font-size: 0.85rem; font-weight: 600; color: #1a237e; margin-bottom: 5px; }
            .top-filter-card { background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); height: 100%; border: 1px solid #e9ecef;}
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

def create_kpi(id_prefix, title):
    return html.Div(className='kpi-card', children=[
        html.Div(title, className='kpi-title'),
        html.H3(id=f'{id_prefix}-value', className='kpi-value', children='-'),
        html.Div(id=f'{id_prefix}-sub', className='kpi-sub', children='vs prev -')
    ])

app.layout = dbc.Container(fluid=True, className='p-4', children=[
    
    # TOP ROW: Filters and Top KPIs
    dbc.Row(className='mb-4 align-items-stretch', children=[
        # Filters
        dbc.Col(md=4, children=[
            dbc.Row(className='h-100', children=[
                dbc.Col(width=6, children=[
                    html.Div(className='top-filter-card', children=[
                        html.Div("Group", className='dropdown-label'),
                        dcc.Dropdown(
                            id='group-dropdown',
                            options=[
                                {'label': 'Continent', 'value': 'Continent'},
                                {'label': 'Country', 'value': 'Country'},
                                {'label': 'Income Group', 'value': 'Income_Group'},
                                {'label': 'SDG Region', 'value': 'SDG_Region'}
                            ],
                            value='Continent',
                            clearable=False
                        )
                    ])
                ]),
                dbc.Col(width=6, children=[
                    html.Div(className='top-filter-card', children=[
                        html.Div("Selection", id='entity-dropdown-label', className='dropdown-label'),
                        dcc.Dropdown(
                            id='entity-dropdown',
                            options=[{'label': c, 'value': c} for c in df_filtered['Continent'].dropna().unique()],
                            value='Asia',
                            clearable=False
                        )
                    ])
                ])
            ])
        ]),
        
        # Top KPIs
        dbc.Col(md=8, children=[
            dbc.Row(children=[
                dbc.Col(width=4, children=create_kpi('kpi-co2', 'CO2 Emissions (% GNI)')),
                dbc.Col(width=4, children=create_kpi('kpi-gdp', 'GDP')),
                dbc.Col(width=4, children=create_kpi('kpi-natres', 'Natural Resources Depletion (%)'))
            ])
        ])
    ]),
    
    # BOTTOM ROW: Charts & Side KPIs
    dbc.Row(children=[
        
        # LEFT: Large Chart (Environment Factors)
        dbc.Col(md=6, children=[
            html.Div(className='chart-card', children=[
                dbc.Row(children=[
                    dbc.Col(html.Div("Environment Factors", className='chart-title'), width=8),
                    dbc.Col(dcc.Dropdown(
                        id='env-metric-dropdown',
                        options=[
                            {'label': 'CO2 Emissions', 'value': 'CO2_Emissions'},
                            {'label': 'CO2 Damage (% GNI)', 'value': 'CO2_Damage_GNI'},
                            {'label': 'Elect. Access', 'value': 'Elec_Access'}
                        ],
                        value='CO2_Emissions',
                        clearable=False
                    ), width=4)
                ]),
                html.Iframe(id='env-chart', style={'border': 'none', 'width': '100%', 'height': '450px', 'marginTop': '20px'})
            ])
        ]),
        
        # MIDDLE: 2 Stacked Charts
        dbc.Col(md=4, children=[
            # Economic Trackers
            html.Div(className='chart-card', style={'minHeight': '260px'}, children=[
                dbc.Row(children=[
                    dbc.Col(html.Div("Economic Trackers", className='chart-title'), width=8),
                    dbc.Col(dcc.Dropdown(
                        id='econ-metric-dropdown',
                        options=[
                            {'label': 'GDP', 'value': 'GDP'},
                            {'label': 'Inflation', 'value': 'Inflation'}
                        ],
                        value='GDP',
                        clearable=False
                    ), width=4)
                ]),
                html.Iframe(id='econ-chart', style={'border': 'none', 'width': '100%', 'height': '200px', 'marginTop': '10px'})
            ]),
            
            # SDG Tracker
            html.Div(className='chart-card', style={'minHeight': '260px'}, children=[
                dbc.Row(children=[
                    dbc.Col(html.Div("SDG Tracker", className='chart-title'), width=8),
                    dbc.Col(dcc.Dropdown(
                        id='sdg-metric-dropdown',
                        options=[
                            {'label': 'Life Expectancy', 'value': 'Life_Exp'},
                            {'label': 'Women in Parliament', 'value': 'Women_Parliament'}
                        ],
                        value='Women_Parliament',
                        clearable=False
                    ), width=4)
                ]),
                html.Iframe(id='sdg-chart', style={'border': 'none', 'width': '100%', 'height': '200px', 'marginTop': '10px'})
            ])
        ]),
        
        # RIGHT: Stacked Side KPIs
        dbc.Col(md=2, children=[
            create_kpi('kpi-inflation', 'Inflation (%)'),
            html.Div(className='kpi-card', children=[
                html.Div('Regime Type', className='kpi-title'),
                html.Div(id='kpi-regime-value', style={'fontSize': '1.1rem', 'marginTop': '10px'})
            ]),
            create_kpi('kpi-women', 'Women Representation'),
            create_kpi('kpi-health', 'Health (Life Expectancy)')
        ])
        
    ])
])

# Utility to render charts
def get_line_chart(df, y_col, color='#1c32c8', height=200):
    if df.empty or y_col not in df.columns:
        return ""
    # Aggregate mean per year
    agg_df = df.groupby('Year', as_index=False)[y_col].mean()
    
    chart = alt.Chart(agg_df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
        x=alt.X('Year:T', title=''),
        y=alt.Y(f'{y_col}:Q', title=''),
        color=alt.value(color),
        tooltip=['Year:T', alt.Tooltip(f'{y_col}:Q', format='.2f')]
    ).properties(
        width='container',
        height=height
    ).configure_axis(
        grid=False,
        domain=False
    ).configure_view(
        strokeWidth=0
    )
    return chart.to_html()

@app.callback(
    [Output('entity-dropdown-label', 'children'),
     Output('entity-dropdown', 'options'),
     Output('entity-dropdown', 'value')],
    Input('group-dropdown', 'value')
)
def update_entity_options(selected_group):
    if not selected_group or selected_group not in df_filtered.columns:
        return "Selection", [], None
    
    options = df_filtered[selected_group].dropna().unique().tolist()
    options.sort()
    
    label_map = {
        'Continent': 'Continent',
        'Country': 'Country',
        'Income_Group': 'Income Group',
        'SDG_Region': 'SDG Region'
    }
    label = label_map.get(selected_group, "Selection")
    
    val = options[0] if options else None
    return label, [{'label': str(opt), 'value': opt} for opt in options], val

@app.callback(
    [
     Output('env-chart', 'srcDoc'),
     Output('econ-chart', 'srcDoc'),
     Output('sdg-chart', 'srcDoc'),
     Output('kpi-co2-value', 'children'), Output('kpi-co2-sub', 'children'),
     Output('kpi-gdp-value', 'children'), Output('kpi-gdp-sub', 'children'),
     Output('kpi-natres-value', 'children'), Output('kpi-natres-sub', 'children'),
     Output('kpi-inflation-value', 'children'), Output('kpi-inflation-sub', 'children'),
     Output('kpi-women-value', 'children'), Output('kpi-women-sub', 'children'),
     Output('kpi-health-value', 'children'), Output('kpi-health-sub', 'children'),
     Output('kpi-regime-value', 'children')
    ],
    [Input('group-dropdown', 'value'),
     Input('entity-dropdown', 'value'),
     Input('env-metric-dropdown', 'value'),
     Input('econ-metric-dropdown', 'value'),
     Input('sdg-metric-dropdown', 'value')]
)
def update_dashboard(group, entity, env_metric, econ_metric, sdg_metric):
    if not group or not entity or group not in df_filtered.columns:
        return "", "", "", "-", "", "-", "", "-", "", "-", "", "-", "", "-", "", "-"
        
    filtered = df_filtered[df_filtered[group] == entity]
    
    env_html = get_line_chart(filtered, env_metric, '#1c32c8', 400)
    econ_html = get_line_chart(filtered, econ_metric, '#1c32c8', 180)
    sdg_html = get_line_chart(filtered, sdg_metric, '#1c32c8', 180)
    
    # KPI Logic: Compare max year vs previous year in dataset
    if filtered.empty:
        return env_html, econ_html, sdg_html, "-", "", "-", "", "-", "", "-", "", "-", "", "-", "", "-"
        
    years = sorted(filtered['Year'].unique())
    if len(years) < 2:
        return env_html, econ_html, sdg_html, "-", "", "-", "", "-", "", "-", "", "-", "", "-", "", "-"
        
    y_curr = years[-1]
    y_prev = years[-2]
    
    c_df = filtered[filtered['Year'] == y_curr]
    p_df = filtered[filtered['Year'] == y_prev]
    
    def calc_kpi(col, fmt='{:.1f}'):
        if col not in filtered.columns: return "-", "-"
        curr = c_df[col].mean()
        prev = p_df[col].mean()
        if pd.isna(curr) or pd.isna(prev) or prev == 0: return "-", "-"
        pct = ((curr - prev) / prev) * 100
        sign = "+" if pct >= 0 else ""
        color_class = "kpi-positive" if pct >= 0 else "kpi-negative"
        sub = html.Span([f"vs prev {fmt.format(prev)} (", html.Span(f"{sign}{pct:.1f}%", className=color_class), ")"])
        return fmt.format(curr), sub

    def format_large(val):
        if pd.isna(val): return "-"
        if val >= 1e9: return f"{val/1e9:.1f}B"
        if val >= 1e6: return f"{val/1e6:.1f}M"
        if val >= 1e3: return f"{val/1e3:.1f}K"
        return f"{val:.1f}"
        
    def calc_kpi_large(col):
        if col not in filtered.columns: return "-", "-"
        curr = c_df[col].mean()
        prev = p_df[col].mean()
        if pd.isna(curr) or pd.isna(prev) or prev == 0: return "-", "-"
        pct = ((curr - prev) / prev) * 100
        sign = "+" if pct >= 0 else ""
        color_class = "kpi-positive" if pct >= 0 else "kpi-negative"
        sub = html.Span([f"vs prev {format_large(prev)} (", html.Span(f"{sign}{pct:.1f}%", className=color_class), ")"])
        return format_large(curr), sub

    co2_v, co2_s = calc_kpi_large('CO2_Emissions')
    gdp_v, gdp_s = calc_kpi_large('GDP')
    natres_v, natres_s = calc_kpi('Nat_Res_Depletion')
    inf_v, inf_s = calc_kpi('Inflation')
    wom_v, wom_s = calc_kpi('Women_Parliament')
    hlt_v, hlth_s = calc_kpi('Life_Exp')
    
    regime = c_df['Regime_Type'].mode()[0] if 'Regime_Type' in c_df.columns and not c_df['Regime_Type'].empty else "-"
    
    return env_html, econ_html, sdg_html, co2_v, co2_s, gdp_v, gdp_s, natres_v, natres_s, inf_v, inf_s, wom_v, wom_s, hlt_v, hlth_s, regime

if __name__ == '__main__':
    app.run(debug=True, port=8050)
