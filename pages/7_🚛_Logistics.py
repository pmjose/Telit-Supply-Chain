"""
Telit Supply Chain - Logistics & Fleet Dashboard
Real-time fleet tracking and delivery analytics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.styles import (
    get_telit_css, render_header, render_section_header,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import get_fleet_data, get_delivery_kpis
from components.charts import create_gauge_chart

# Page config
st.set_page_config(page_title="Logistics - Telit Supply Chain", page_icon="🚛", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>🚛 Logistics & Fleet</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Real-time Tracking</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    region = st.selectbox("Region", ["All Regions", "North America", "Europe", "Asia Pacific"])
    vehicle_status = st.multiselect("Vehicle Status", ["En Route", "Delivering", "Returning", "Idle"])

# Header
st.markdown(render_header("Logistics & Fleet Management", "Real-time vehicle tracking and delivery performance"), unsafe_allow_html=True)

# Get data
fleet_df = get_fleet_data()
delivery_kpis = get_delivery_kpis()

# Apply filters
if vehicle_status:
    fleet_df = fleet_df[fleet_df['status'].isin(vehicle_status)]

# =============================================================================
# KPI CARDS
# =============================================================================
col1, col2, col3, col4, col5, col6 = st.columns(6)

kpi_data = [
    ("On-Time Rate", f"{delivery_kpis['on_time_rate']}%", TELIT_GREEN),
    ("Avg Delivery", f"{delivery_kpis['avg_delivery_time']}h", TELIT_BLUE),
    ("Today's Deliveries", f"{delivery_kpis['deliveries_today']}", TELIT_BLUE),
    ("Active Vehicles", f"{delivery_kpis['active_vehicles']}", TELIT_GREEN),
    ("Fuel Efficiency", f"{delivery_kpis['fuel_efficiency']} mpg", TELIT_ORANGE),
    ("Customer Rating", f"{delivery_kpis['customer_satisfaction']}/5", TELIT_GREEN),
]

for col, (label, value, color) in zip([col1, col2, col3, col4, col5, col6], kpi_data):
    with col:
        st.markdown(f"""
            <div class="kpi-card" style="text-align: center; padding: 16px;">
                <div class="kpi-label" style="font-size: 10px;">{label}</div>
                <div class="kpi-value" style="font-size: 1.5rem; color: {color};">{value}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["🗺️ Live Fleet Map", "📊 Performance Analytics", "🚚 Vehicle Details"])

with tab1:
    st.markdown(render_section_header("Live Fleet Tracking"), unsafe_allow_html=True)
    
    # Fleet map
    status_colors = {
        'En Route': TELIT_BLUE,
        'Delivering': TELIT_GREEN,
        'Returning': TELIT_ORANGE,
        'Idle': TELIT_GRAY
    }
    
    fleet_df['color'] = fleet_df['status'].map(status_colors)
    
    fig = px.scatter_mapbox(
        fleet_df,
        lat='lat',
        lon='lon',
        color='status',
        size='deliveries_today',
        hover_name='vehicle_id',
        hover_data=['driver', 'status', 'speed_mph', 'fuel_level', 'eta'],
        color_discrete_map=status_colors,
        zoom=3,
        center={'lat': 39, 'lon': -98},
        mapbox_style="carto-positron"
    )
    
    fig.update_layout(
        height=450,
        margin={"r":0,"t":0,"l":0,"b":0},
        legend=dict(orientation="h", yanchor="bottom", y=1.02)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Legend and summary
    col1, col2, col3, col4 = st.columns(4)
    
    status_counts = fleet_df['status'].value_counts()
    
    for col, status in zip([col1, col2, col3, col4], ['En Route', 'Delivering', 'Returning', 'Idle']):
        count = status_counts.get(status, 0)
        color = status_colors[status]
        with col:
            st.markdown(f"""
                <div style="background: {color}15; border-left: 4px solid {color}; padding: 12px; border-radius: 0 8px 8px 0;">
                    <div style="font-size: 24px; font-weight: 700; color: {color};">{count}</div>
                    <div style="font-size: 12px; color: {TELIT_GRAY};">{status}</div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(render_section_header("On-Time Performance"), unsafe_allow_html=True)
        fig = create_gauge_chart(delivery_kpis['on_time_rate'], "On-Time Delivery", suffix="%", threshold_good=95, threshold_warning=90)
        st.plotly_chart(fig, use_container_width=True)
        
        # Weekly trend
        import numpy as np
        from datetime import datetime, timedelta
        
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        otd_values = [94, 96, 93, 97, 95, 92, 94]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=days, y=otd_values, marker_color=TELIT_BLUE))
        fig.add_hline(y=95, line_dash="dash", line_color=TELIT_GREEN, annotation_text="Target")
        fig.update_layout(height=250, yaxis_range=[85, 100], yaxis_title="On-Time %")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Delivery Efficiency"), unsafe_allow_html=True)
        
        # Deliveries per hour
        hours = list(range(6, 22))
        deliveries = [5, 12, 25, 45, 52, 48, 35, 42, 55, 62, 58, 45, 38, 25, 15, 8]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours, y=deliveries, mode='lines+markers',
                                 fill='tozeroy', line=dict(color=TELIT_BLUE)))
        fig.update_layout(height=250, xaxis_title="Hour", yaxis_title="Deliveries")
        st.plotly_chart(fig, use_container_width=True)
        
        # Delivery distribution
        st.markdown("**Delivery Time Distribution**")
        times = ['<1hr', '1-2hr', '2-3hr', '3-4hr', '>4hr']
        counts = [120, 280, 245, 142, 60]
        
        fig = px.bar(x=times, y=counts, color_discrete_sequence=[TELIT_GREEN, TELIT_GREEN, TELIT_BLUE, TELIT_YELLOW, TELIT_RED])
        fig.update_layout(height=200, xaxis_title="Delivery Time", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown(render_section_header("Vehicle Fleet Status"), unsafe_allow_html=True)
    
    # Vehicle cards
    for _, vehicle in fleet_df.head(8).iterrows():
        status_color = status_colors[vehicle['status']]
        fuel_color = TELIT_GREEN if vehicle['fuel_level'] > 50 else TELIT_YELLOW if vehicle['fuel_level'] > 25 else TELIT_RED
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
                <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); display: flex; align-items: center; gap: 20px;">
                    <div style="background: {status_color}20; width: 60px; height: 60px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 28px;">
                        🚛
                    </div>
                    <div style="flex: 1;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <strong style="font-size: 16px; color: {TELIT_DARK};">{vehicle['vehicle_id']}</strong>
                                <span style="background: {status_color}; color: white; padding: 2px 8px; border-radius: 10px; font-size: 11px; margin-left: 8px;">{vehicle['status']}</span>
                            </div>
                            <span style="color: {TELIT_GRAY}; font-size: 13px;">ETA: {vehicle['eta']}</span>
                        </div>
                        <div style="color: {TELIT_GRAY}; font-size: 13px; margin-top: 4px;">Driver: {vehicle['driver']}</div>
                        <div style="display: flex; gap: 24px; margin-top: 8px;">
                            <span style="font-size: 12px;"><strong>{vehicle['speed_mph']}</strong> mph</span>
                            <span style="font-size: 12px; color: {fuel_color};"><strong>{vehicle['fuel_level']}%</strong> fuel</span>
                            <span style="font-size: 12px;"><strong>{vehicle['deliveries_today']}</strong> deliveries</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    # Fleet summary table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Fleet Summary"), unsafe_allow_html=True)
    
    st.dataframe(
        fleet_df[['vehicle_id', 'driver', 'status', 'speed_mph', 'fuel_level', 'deliveries_today', 'eta']],
        column_config={
            "vehicle_id": "Vehicle",
            "driver": "Driver",
            "status": "Status",
            "speed_mph": st.column_config.NumberColumn("Speed (mph)", format="%d"),
            "fuel_level": st.column_config.ProgressColumn("Fuel", min_value=0, max_value=100),
            "deliveries_today": st.column_config.NumberColumn("Deliveries", format="%d"),
            "eta": "ETA"
        },
        hide_index=True,
        use_container_width=True
    )

