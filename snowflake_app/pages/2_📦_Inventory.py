"""
Inventory Management - Snowflake Version
"""
import streamlit as st
import pandas as pd
import plotly.express as px

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Inventory", page_icon="📦", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">📦 Inventory Management</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Real-time stock levels across global warehouses</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Units", "285,000", "↑ 5.2%")
col2.metric("Low Stock Alerts", "12", "↓ 3")
col3.metric("Avg Days Supply", "18.5", "↑ 2.1")
col4.metric("Warehouse Util.", "72.4%", "↓ 1.8%")

st.markdown("---")

# Warehouse Map
st.subheader("🌍 Global Warehouse Network")

warehouses = pd.DataFrame({
    'Warehouse': ['Los Angeles DC', 'Dallas DC', 'Frankfurt Hub', 'London DC', 'Shanghai DC', 'Singapore Hub', 'Tokyo DC', 'São Paulo DC'],
    'lat': [34.05, 32.78, 50.11, 51.51, 31.23, 1.35, 35.68, -23.55],
    'lon': [-118.24, -96.80, 8.68, -0.13, 121.47, 103.82, 139.65, -46.63],
    'Units': [45000, 32000, 42000, 28000, 55000, 38000, 22000, 18000],
    'Utilization': [78, 65, 82, 70, 92, 75, 68, 55]
})

fig = px.scatter_mapbox(warehouses, lat='lat', lon='lon', size='Units', color='Utilization',
                        hover_name='Warehouse', hover_data=['Units', 'Utilization'],
                        color_continuous_scale=[[0, TELIT_GREEN], [0.7, TELIT_ORANGE], [1, TELIT_RED]],
                        zoom=1, mapbox_style="carto-positron")
fig.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Stock by Category
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Stock by Category")
    categories = pd.DataFrame({
        'Category': ['Cellular 5G', 'Cellular LTE', 'Cellular LPWA', 'Wi-Fi & BT', 'Positioning'],
        'Stock': [65000, 85000, 72000, 38000, 25000]
    })
    fig = px.bar(categories, x='Stock', y='Category', orientation='h', color_discrete_sequence=[TELIT_BLUE])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🏭 Stock by Region")
    regions = pd.DataFrame({'Region': ['Americas', 'EMEA', 'APAC'], 'Stock': [95000, 98000, 92000]})
    fig = px.pie(regions, values='Stock', names='Region', hole=0.5,
                 color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# Low Stock Alerts
st.subheader("⚠️ Low Stock Alerts")

low_stock = pd.DataFrame({
    'Product': ['FN980-NA', 'ME310G1-W1', 'LE910C4-NF', 'SE868K3-A'],
    'Warehouse': ['Shanghai DC', 'Los Angeles DC', 'Frankfurt Hub', 'Singapore Hub'],
    'Current': [180, 250, 320, 95],
    'Reorder Point': [500, 400, 500, 200],
    'Days Supply': [3.2, 5.1, 6.8, 2.4]
})

st.dataframe(low_stock, column_config={
    "Product": "Product",
    "Warehouse": "Warehouse", 
    "Current": st.column_config.NumberColumn("Current Stock"),
    "Reorder Point": st.column_config.NumberColumn("Reorder Point"),
    "Days Supply": st.column_config.NumberColumn("Days of Supply", format="%.1f")
}, hide_index=True, use_container_width=True)

