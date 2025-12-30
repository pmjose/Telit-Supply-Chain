"""
Supply Chain Visibility - Snowflake Version
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

st.set_page_config(page_title="Supply Chain Visibility", page_icon="🚚", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🚚 Supply Chain Visibility</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">End-to-end shipment tracking</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Active Shipments", "1,247")
col2.metric("In Transit", "847")
col3.metric("Delivered Today", "156")
col4.metric("Value in Transit", "$12.4M")

st.markdown("---")

# Shipment Map
st.subheader("🗺️ Live Shipment Tracking")

shipments = pd.DataFrame({
    'Shipment': ['SHP-10001', 'SHP-10002', 'SHP-10003', 'SHP-10004', 'SHP-10005'],
    'lat': [35.5, 48.2, 22.3, 40.7, -23.5],
    'lon': [-100.5, 5.5, 114.2, -74.0, -46.6],
    'Status': ['In Transit', 'In Transit', 'At Hub', 'Delivered', 'In Transit'],
    'Progress': [65, 82, 45, 100, 30]
})

colors = {'In Transit': TELIT_BLUE, 'At Hub': TELIT_ORANGE, 'Delivered': TELIT_GREEN}
shipments['color'] = shipments['Status'].map(colors)

fig = px.scatter_mapbox(shipments, lat='lat', lon='lon', color='Status',
                        hover_name='Shipment', size_max=15,
                        color_discrete_map=colors, zoom=1, mapbox_style="carto-positron")
fig.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Status breakdown
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Shipments by Status")
    status_data = pd.DataFrame({
        'Status': ['In Transit', 'At Hub', 'Customs', 'Delivered', 'Delayed'],
        'Count': [520, 180, 85, 412, 50]
    })
    fig = px.pie(status_data, values='Count', names='Status', hole=0.5,
                 color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, '#9c27b0', TELIT_GREEN, '#ef5350'])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📦 Shipments by Carrier")
    carrier_data = pd.DataFrame({
        'Carrier': ['DHL', 'FedEx', 'UPS', 'Maersk', 'K+N'],
        'Count': [380, 320, 280, 167, 100]
    })
    fig = px.bar(carrier_data, x='Count', y='Carrier', orientation='h',
                 color_discrete_sequence=[TELIT_BLUE])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# Recent shipments
st.subheader("📋 Recent Shipments")

recent = pd.DataFrame({
    'Shipment ID': ['SHP-10001', 'SHP-10002', 'SHP-10003', 'SHP-10004', 'SHP-10005'],
    'Origin': ['Shanghai', 'Frankfurt', 'Singapore', 'Los Angeles', 'São Paulo'],
    'Destination': ['Los Angeles', 'London', 'Tokyo', 'Dallas', 'Frankfurt'],
    'Status': ['In Transit', 'In Transit', 'At Hub', 'Delivered', 'In Transit'],
    'ETA': ['Dec 28', 'Dec 26', 'Dec 27', 'Delivered', 'Jan 2'],
    'Progress': [65, 82, 45, 100, 30]
})

st.dataframe(recent, column_config={
    "Progress": st.column_config.ProgressColumn("Progress", min_value=0, max_value=100)
}, hide_index=True, use_container_width=True)

