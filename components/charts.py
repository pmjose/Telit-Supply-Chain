"""
Telit Supply Chain - Chart Components
Reusable Plotly charts with Telit theming
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from components.styles import (
    TELIT_BLUE, TELIT_DARK, TELIT_NAVY, TELIT_ORANGE, 
    TELIT_GREEN, TELIT_RED, TELIT_YELLOW, TELIT_GRAY
)

# Common layout settings
COMMON_LAYOUT = {
    'font': {'family': 'Inter, sans-serif', 'color': TELIT_DARK},
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'margin': {'l': 40, 'r': 40, 't': 40, 'b': 40},
}

TELIT_COLORS = [TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN, TELIT_NAVY, TELIT_YELLOW, TELIT_RED]


def create_gauge_chart(value: float, title: str, max_value: float = 100, 
                       suffix: str = "%", threshold_good: float = 80, 
                       threshold_warning: float = 60):
    """Create a gauge chart"""
    color = TELIT_GREEN if value >= threshold_good else TELIT_YELLOW if value >= threshold_warning else TELIT_RED
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'size': 16, 'color': TELIT_DARK}},
        number={'suffix': suffix, 'font': {'size': 28, 'color': TELIT_DARK}},
        gauge={
            'axis': {'range': [0, max_value], 'tickcolor': TELIT_GRAY},
            'bar': {'color': color},
            'bgcolor': 'white',
            'borderwidth': 2,
            'bordercolor': '#e9ecef',
            'steps': [
                {'range': [0, threshold_warning], 'color': 'rgba(255,71,87,0.1)'},
                {'range': [threshold_warning, threshold_good], 'color': 'rgba(255,184,0,0.1)'},
                {'range': [threshold_good, max_value], 'color': 'rgba(0,196,140,0.1)'},
            ],
            'threshold': {
                'line': {'color': TELIT_DARK, 'width': 2},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        height=200,
        margin={'l': 20, 'r': 20, 't': 60, 'b': 20},
    )
    
    return fig


def create_donut_chart(df: pd.DataFrame, values_col: str, names_col: str, title: str = ""):
    """Create a donut chart"""
    fig = go.Figure(data=[go.Pie(
        labels=df[names_col],
        values=df[values_col],
        hole=0.6,
        marker={'colors': TELIT_COLORS},
        textinfo='percent+label',
        textposition='outside',
        textfont={'size': 12},
        hovertemplate="<b>%{label}</b><br>%{value:,.0f}<br>%{percent}<extra></extra>"
    )])
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        showlegend=False,
        height=350,
    )
    
    return fig


def create_bar_chart(df: pd.DataFrame, x_col: str, y_col: str, title: str = "", 
                     horizontal: bool = False, color: str = None):
    """Create a bar chart"""
    if horizontal:
        fig = go.Figure(go.Bar(
            y=df[x_col],
            x=df[y_col],
            orientation='h',
            marker_color=color or TELIT_BLUE,
            hovertemplate="<b>%{y}</b><br>%{x:,.0f}<extra></extra>"
        ))
    else:
        fig = go.Figure(go.Bar(
            x=df[x_col],
            y=df[y_col],
            marker_color=color or TELIT_BLUE,
            hovertemplate="<b>%{x}</b><br>%{y:,.0f}<extra></extra>"
        ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        xaxis={'showgrid': False, 'title': ''},
        yaxis={'showgrid': True, 'gridcolor': '#e9ecef', 'title': ''},
        height=350,
    )
    
    return fig


def create_line_chart(df: pd.DataFrame, x_col: str, y_cols: list, title: str = "",
                      show_area: bool = False):
    """Create a line chart with multiple series"""
    fig = go.Figure()
    
    colors = TELIT_COLORS[:len(y_cols)]
    
    for i, col in enumerate(y_cols):
        if show_area:
            fig.add_trace(go.Scatter(
                x=df[x_col],
                y=df[col],
                name=col,
                fill='tozeroy',
                fillcolor=f'rgba{tuple(list(int(colors[i].lstrip("#")[j:j+2], 16) for j in (0, 2, 4)) + [0.2])}',
                line={'color': colors[i], 'width': 2},
                hovertemplate="<b>%{x}</b><br>%{y:,.2f}<extra></extra>"
            ))
        else:
            fig.add_trace(go.Scatter(
                x=df[x_col],
                y=df[col],
                name=col,
                mode='lines',
                line={'color': colors[i], 'width': 2},
                hovertemplate="<b>%{x}</b><br>%{y:,.2f}<extra></extra>"
            ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        xaxis={'showgrid': False, 'title': ''},
        yaxis={'showgrid': True, 'gridcolor': '#e9ecef', 'title': ''},
        legend={'orientation': 'h', 'yanchor': 'bottom', 'y': 1.02, 'xanchor': 'right', 'x': 1},
        height=350,
    )
    
    return fig


def create_map_chart(df: pd.DataFrame, lat_col: str, lon_col: str, 
                     size_col: str = None, color_col: str = None,
                     hover_data: list = None, title: str = ""):
    """Create a scatter map"""
    fig = px.scatter_mapbox(
        df,
        lat=lat_col,
        lon=lon_col,
        size=size_col if size_col else None,
        color=color_col if color_col else None,
        hover_data=hover_data,
        color_discrete_sequence=TELIT_COLORS,
        zoom=1,
        mapbox_style="carto-positron"
    )
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        height=400,
        margin={'l': 0, 'r': 0, 't': 40, 'b': 0},
    )
    
    return fig


def create_scatter_mapbox(locations: list, title: str = ""):
    """Create a scatter mapbox with custom markers"""
    fig = go.Figure()
    
    for loc in locations:
        fig.add_trace(go.Scattermapbox(
            lat=[loc['lat']],
            lon=[loc['lon']],
            mode='markers+text',
            marker=dict(
                size=15,
                color=TELIT_BLUE if loc.get('status', 'ok') == 'ok' else TELIT_ORANGE,
            ),
            text=loc.get('name', ''),
            textposition='top center',
            name=loc.get('name', ''),
            hovertemplate=f"<b>{loc.get('name', '')}</b><br>" +
                         f"Region: {loc.get('region', '')}<br>" +
                         f"Capacity: {loc.get('capacity', 0):,}<extra></extra>"
        ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        mapbox=dict(
            style="carto-positron",
            center=dict(lat=30, lon=0),
            zoom=1
        ),
        showlegend=False,
        height=400,
        margin={'l': 0, 'r': 0, 't': 40, 'b': 0},
    )
    
    return fig


def create_radar_chart(categories: list, values: list, title: str = ""):
    """Create a radar/spider chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Close the polygon
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor=f'rgba(0,167,225,0.2)',
        line=dict(color=TELIT_BLUE, width=2),
        name='Score'
    ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showline=False,
                gridcolor='#e9ecef',
            ),
            angularaxis=dict(
                gridcolor='#e9ecef',
            ),
            bgcolor='rgba(0,0,0,0)',
        ),
        showlegend=False,
        title={'text': title, 'font': {'size': 16}},
        height=350,
    )
    
    return fig


def create_heatmap(df: pd.DataFrame, x_col: str, y_col: str, z_col: str, title: str = ""):
    """Create a heatmap"""
    pivot_df = df.pivot(index=y_col, columns=x_col, values=z_col)
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        colorscale=[
            [0, 'rgba(0,167,225,0.1)'],
            [0.5, 'rgba(0,167,225,0.5)'],
            [1, TELIT_BLUE]
        ],
        hovertemplate="<b>%{x}</b> - <b>%{y}</b><br>Value: %{z:,.0f}<extra></extra>"
    ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        height=350,
    )
    
    return fig


def create_control_chart(df: pd.DataFrame, title: str = ""):
    """Create an SPC control chart"""
    fig = go.Figure()
    
    # UCL
    fig.add_trace(go.Scatter(
        x=df['date'], y=df['ucl'],
        mode='lines',
        name='UCL',
        line=dict(color=TELIT_RED, dash='dash', width=1),
    ))
    
    # LCL
    fig.add_trace(go.Scatter(
        x=df['date'], y=df['lcl'],
        mode='lines',
        name='LCL',
        line=dict(color=TELIT_RED, dash='dash', width=1),
    ))
    
    # Mean
    fig.add_trace(go.Scatter(
        x=df['date'], y=df['mean'],
        mode='lines',
        name='Mean',
        line=dict(color=TELIT_GREEN, dash='dot', width=1),
    ))
    
    # Values
    colors = [TELIT_RED if v > df['ucl'].iloc[0] or v < df['lcl'].iloc[0] else TELIT_BLUE 
              for v in df['value']]
    
    fig.add_trace(go.Scatter(
        x=df['date'], y=df['value'],
        mode='lines+markers',
        name='Value',
        line=dict(color=TELIT_BLUE, width=2),
        marker=dict(color=colors, size=8),
    ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        xaxis={'showgrid': False, 'title': ''},
        yaxis={'showgrid': True, 'gridcolor': '#e9ecef', 'title': ''},
        height=350,
        showlegend=True,
        legend={'orientation': 'h', 'yanchor': 'bottom', 'y': 1.02, 'xanchor': 'right', 'x': 1},
    )
    
    return fig


def create_forecast_chart(df: pd.DataFrame, title: str = ""):
    """Create a forecast chart with confidence bands"""
    fig = go.Figure()
    
    # Historical data
    historical = df[~df['is_forecast']]
    forecast = df[df['is_forecast']]
    
    # Historical line
    fig.add_trace(go.Scatter(
        x=historical['date'], y=historical['demand'],
        mode='lines',
        name='Historical',
        line=dict(color=TELIT_BLUE, width=2),
    ))
    
    # Forecast line
    fig.add_trace(go.Scatter(
        x=forecast['date'], y=forecast['demand'],
        mode='lines',
        name='Forecast',
        line=dict(color=TELIT_ORANGE, width=2, dash='dot'),
    ))
    
    # Confidence band
    fig.add_trace(go.Scatter(
        x=list(forecast['date']) + list(forecast['date'])[::-1],
        y=list(forecast['upper_bound']) + list(forecast['lower_bound'])[::-1],
        fill='toself',
        fillcolor='rgba(255,107,53,0.2)',
        line=dict(color='rgba(255,107,53,0)'),
        name='Confidence Band',
        showlegend=True,
    ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        xaxis={'showgrid': False, 'title': ''},
        yaxis={'showgrid': True, 'gridcolor': '#e9ecef', 'title': ''},
        height=400,
        legend={'orientation': 'h', 'yanchor': 'bottom', 'y': 1.02, 'xanchor': 'right', 'x': 1},
    )
    
    return fig


def create_pareto_chart(df: pd.DataFrame, category_col: str, value_col: str, title: str = ""):
    """Create a Pareto chart"""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Bars
    fig.add_trace(
        go.Bar(
            x=df[category_col], 
            y=df[value_col],
            name='Count',
            marker_color=TELIT_BLUE,
        ),
        secondary_y=False,
    )
    
    # Cumulative line
    if 'cumulative_pct' in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df[category_col], 
                y=df['cumulative_pct'],
                name='Cumulative %',
                line=dict(color=TELIT_ORANGE, width=2),
                marker=dict(size=6),
            ),
            secondary_y=True,
        )
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        height=400,
        legend={'orientation': 'h', 'yanchor': 'bottom', 'y': 1.02, 'xanchor': 'right', 'x': 1},
    )
    
    fig.update_yaxes(title_text="Count", secondary_y=False, showgrid=True, gridcolor='#e9ecef')
    fig.update_yaxes(title_text="Cumulative %", secondary_y=True, range=[0, 105])
    
    return fig


def create_treemap(df: pd.DataFrame, path: list, values_col: str, title: str = ""):
    """Create a treemap chart"""
    fig = px.treemap(
        df,
        path=path,
        values=values_col,
        color_discrete_sequence=TELIT_COLORS,
    )
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        height=400,
    )
    
    return fig


def create_sankey_diagram(nodes: list, links: list, title: str = ""):
    """Create a Sankey diagram for supply chain flow"""
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=nodes,
            color=TELIT_COLORS[:len(nodes)]
        ),
        link=dict(
            source=links['source'],
            target=links['target'],
            value=links['value'],
            color='rgba(0,167,225,0.3)'
        )
    )])
    
    fig.update_layout(
        **COMMON_LAYOUT,
        title={'text': title, 'font': {'size': 16}},
        height=400,
    )
    
    return fig


def create_bullet_chart(value: float, target: float, title: str, ranges: list = None):
    """Create a bullet chart for KPI comparison"""
    if ranges is None:
        ranges = [target * 0.5, target * 0.75, target * 1.2]
    
    fig = go.Figure(go.Indicator(
        mode="number+gauge+delta",
        value=value,
        delta={'reference': target},
        domain={'x': [0.1, 1], 'y': [0.2, 0.8]},
        title={'text': title},
        gauge={
            'shape': "bullet",
            'axis': {'range': [0, ranges[-1]]},
            'threshold': {
                'line': {'color': TELIT_DARK, 'width': 2},
                'thickness': 0.75,
                'value': target
            },
            'steps': [
                {'range': [0, ranges[0]], 'color': 'rgba(255,71,87,0.3)'},
                {'range': [ranges[0], ranges[1]], 'color': 'rgba(255,184,0,0.3)'},
                {'range': [ranges[1], ranges[2]], 'color': 'rgba(0,196,140,0.3)'},
            ],
            'bar': {'color': TELIT_BLUE}
        }
    ))
    
    fig.update_layout(
        **COMMON_LAYOUT,
        height=150,
    )
    
    return fig

