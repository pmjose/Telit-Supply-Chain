"""
Logistics & Fleet - Snowflake Version
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Logistics", page_icon="🚛", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🚛 Logistics & Fleet</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Real-time fleet tracking</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("On-Time Rate", "94.7%", "↑ 1.2%")
col2.metric("Avg Delivery", "2.3 hrs", "↓ 0.2")
col3.metric("Today's Deliveries", "847", "↑ 12%")
col4.metric("Active Vehicles", "18/20", "")
col5.metric("Fuel Efficiency", "8.2 mpg", "↑ 0.3")
col6.metric("Customer Rating", "4.7/5", "↑ 0.1")

st.markdown("---")

# Fleet Map
st.subheader("🗺️ Live Fleet Tracking")

vehicles = pd.DataFrame({
    'Vehicle': [f'TRK-{1000+i}' for i in range(12)],
    'lat': [34.1, 33.8, 34.2, 33.9, 34.0, 33.7, 34.3, 33.6, 34.1, 33.5, 34.0, 33.8],
    'lon': [-118.2, -117.9, -118.4, -118.1, -117.8, -118.3, -117.7, -118.0, -118.5, -117.6, -118.2, -117.9],
    'Status': ['En Route', 'Delivering', 'En Route', 'Returning', 'Idle', 'En Route', 
               'Delivering', 'En Route', 'Returning', 'En Route', 'Idle', 'Delivering'],
    'Deliveries': [8, 5, 10, 3, 0, 7, 4, 9, 2, 6, 0, 5]
})

colors = {'En Route': TELIT_BLUE, 'Delivering': TELIT_GREEN, 'Returning': TELIT_ORANGE, 'Idle': TELIT_GRAY}
vehicles['color'] = vehicles['Status'].map(colors)

fig = px.scatter_mapbox(vehicles, lat='lat', lon='lon', color='Status',
                        hover_name='Vehicle', hover_data=['Deliveries'],
                        color_discrete_map=colors, zoom=9, 
                        center={'lat': 33.9, 'lon': -118.1},
                        mapbox_style="carto-positron")
fig.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Status cards
st.subheader("📊 Fleet Status")
status_cols = st.columns(4)
status_counts = vehicles['Status'].value_counts()

for col, status in zip(status_cols, ['En Route', 'Delivering', 'Returning', 'Idle']):
    count = status_counts.get(status, 0)
    color = colors[status]
    with col:
        st.markdown(f"""
            <div style="background: {color}15; border-left: 4px solid {color}; padding: 16px; border-radius: 0 8px 8px 0;">
                <div style="font-size: 28px; font-weight: 700; color: {color};">{count}</div>
                <div style="font-size: 13px; color: {TELIT_GRAY};">{status}</div>
            </div>
        """, unsafe_allow_html=True)

# Performance charts
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Deliveries by Hour")
    hours = list(range(6, 20))
    deliveries = [5, 15, 35, 55, 62, 58, 45, 52, 65, 72, 58, 42, 28, 12]
    
    fig = go.Figure(go.Scatter(x=hours, y=deliveries, mode='lines+markers', fill='tozeroy',
                               line=dict(color=TELIT_BLUE), fillcolor=f'rgba(0,167,225,0.2)'))
    fig.update_layout(height=300, xaxis_title="Hour", yaxis_title="Deliveries")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("⏱️ Delivery Time Distribution")
    times = ['<1hr', '1-2hr', '2-3hr', '3-4hr', '>4hr']
    counts = [120, 280, 245, 142, 60]
    dist_colors = [TELIT_GREEN, TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, TELIT_ORANGE]
    
    fig = go.Figure(go.Bar(x=times, y=counts, marker_color=dist_colors))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# Vehicle list
st.subheader("🚚 Vehicle Fleet")
st.dataframe(vehicles[['Vehicle', 'Status', 'Deliveries']], hide_index=True, use_container_width=True)

