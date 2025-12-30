"""
Executive Dashboard - Snowflake Version
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Colors
TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Executive Dashboard", page_icon="📊", layout="wide")

# Header
st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">📊 Executive Dashboard</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Real-time overview of global supply chain operations</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", "$247.8M", "↑ 12.3%")
col2.metric("Orders in Transit", "1,247", "↑ 8.2%")
col3.metric("Inventory Value", "$89.4M", "↓ 2.1%")
col4.metric("On-Time Delivery", "94.7%", "↑ 1.8%")

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Revenue by Region")
    region_data = pd.DataFrame({
        'Region': ['Americas', 'EMEA', 'APAC'],
        'Revenue': [98.5, 82.3, 67.0]
    })
    fig = px.pie(region_data, values='Revenue', names='Region', hole=0.5,
                 color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📈 Top Products")
    products = pd.DataFrame({
        'Product': ['ME310G1', 'FN980', 'LE910C4', 'SE868K3', 'WE310F6'],
        'Units': [45000, 38000, 32000, 28000, 25000]
    })
    fig = px.bar(products, x='Units', y='Product', orientation='h',
                 color_discrete_sequence=[TELIT_BLUE])
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

# Health Gauges
st.subheader("🎯 Supply Chain Health")
g1, g2, g3, g4 = st.columns(4)

for col, (label, value) in zip([g1, g2, g3, g4], 
    [("Inventory", 87), ("Quality", 94), ("Delivery", 91), ("Supplier", 88)]):
    with col:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': label},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': TELIT_GREEN if value >= 85 else TELIT_ORANGE},
                   'steps': [{'range': [0, 60], 'color': "#ffebee"},
                            {'range': [60, 80], 'color': "#fff3e0"},
                            {'range': [80, 100], 'color': "#e8f5e9"}]}
        ))
        fig.update_layout(height=200, margin=dict(t=50, b=0, l=20, r=20))
        st.plotly_chart(fig, use_container_width=True)

# Alerts
st.subheader("⚠️ Active Alerts")
alerts = [
    ("🔴", "Critical", "Low stock: FN980-NA below reorder point at Shanghai DC"),
    ("🟡", "Warning", "Supplier delay: Taiwan Semiconductor shipment delayed 3 days"),
    ("🟡", "Warning", "Quality alert: Increased defect rate on SMT Line 2"),
    ("🔵", "Info", "New order: 10,000 units ME310G1 from Automotive OEM Alpha"),
]

for icon, level, msg in alerts:
    color = TELIT_RED if level == "Critical" else TELIT_ORANGE if level == "Warning" else TELIT_BLUE
    st.markdown(f"""
        <div style="background: {color}15; border-left: 4px solid {color}; padding: 12px; border-radius: 0 8px 8px 0; margin-bottom: 8px;">
            {icon} <strong>{level}:</strong> {msg}
        </div>
    """, unsafe_allow_html=True)

