"""
Predictive Maintenance - Snowflake Version
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Predictive Maintenance", page_icon="🔧", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🔧 Predictive Maintenance</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">AI-powered equipment health monitoring</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Equipment", "8")
col2.metric("Healthy", "5", delta_color="normal")
col3.metric("Warning", "2", delta_color="off")
col4.metric("Critical", "1", delta_color="inverse")
col5.metric("Avg Health", "86.4%")

# Critical alert
st.markdown(f"""
    <div style="background: {TELIT_RED}15; border-left: 4px solid {TELIT_RED}; padding: 16px; border-radius: 0 8px 8px 0; margin: 16px 0;">
        🚨 <strong>CRITICAL:</strong> AOI Station 2 requires immediate attention - Health Score: 65.2% | Failure Probability: 34.8%
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Equipment health
st.subheader("📊 Equipment Health Matrix")

equipment = pd.DataFrame({
    'Equipment': ['SMT Line 1', 'SMT Line 2', 'Reflow Oven', 'AOI Station 1', 'AOI Station 2', 'Tester 1', 'Tester 2', 'Packaging'],
    'Health': [92.5, 78.3, 95.1, 88.7, 65.2, 91.8, 89.4, 94.2],
    'Status': ['Good', 'Warning', 'Good', 'Good', 'Critical', 'Good', 'Good', 'Good'],
    'Temp': [45.2, 52.8, 68.5, 38.2, 42.1, 35.5, 36.8, 28.5],
    'Vibration': [0.3, 0.8, 0.2, 0.4, 1.2, 0.25, 0.35, 0.15],
    'Risk': [7.5, 21.7, 4.9, 11.3, 34.8, 8.2, 10.6, 5.8],
    'NextMaint': ['30 days', '7 days', '45 days', '21 days', '3 days', '35 days', '28 days', '60 days']
})

equipment_sorted = equipment.sort_values('Health')
colors = [TELIT_RED if s == 'Critical' else TELIT_ORANGE if s == 'Warning' else TELIT_GREEN for s in equipment_sorted['Status']]

fig = go.Figure(go.Bar(
    y=equipment_sorted['Equipment'],
    x=equipment_sorted['Health'],
    orientation='h',
    marker_color=colors,
    text=equipment_sorted['Health'].astype(str) + '%',
    textposition='outside'
))

fig.add_vline(x=70, line_dash="dash", line_color=TELIT_RED, opacity=0.5)
fig.add_vline(x=85, line_dash="dash", line_color=TELIT_ORANGE, opacity=0.5)
fig.update_layout(height=350, xaxis_range=[0, 105], xaxis_title="Health Score (%)")
st.plotly_chart(fig, use_container_width=True)

# Sensor data
st.subheader("📈 Sensor Analytics - AOI Station 2")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Temperature Trend (°C)**")
    hours = 24
    timestamps = [datetime.now() - timedelta(hours=x) for x in range(hours, 0, -1)]
    temps = [42 + np.sin(i/4) * 3 + np.random.normal(0, 1) for i in range(hours)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=temps, mode='lines', fill='tozeroy',
                             line=dict(color=TELIT_ORANGE), fillcolor=f'rgba(255,107,53,0.2)'))
    fig.add_hline(y=50, line_dash="dash", line_color=TELIT_RED, annotation_text="Threshold")
    fig.update_layout(height=250)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("**Vibration Level (mm/s)**")
    vibrations = [1.2 + np.random.exponential(0.2) for _ in range(hours)]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=timestamps, y=vibrations, mode='lines', fill='tozeroy',
                             line=dict(color=TELIT_RED), fillcolor=f'rgba(255,71,87,0.2)'))
    fig.add_hline(y=1.5, line_dash="dash", line_color=TELIT_RED, annotation_text="Threshold")
    fig.update_layout(height=250)
    st.plotly_chart(fig, use_container_width=True)

# Failure prediction
st.subheader("🔮 Failure Probability Forecast")

dates = [datetime.now() + timedelta(days=x) for x in range(30)]
probs = {}

for eq in ['AOI Station 2', 'SMT Line 2', 'AOI Station 1']:
    base = equipment[equipment['Equipment'] == eq]['Risk'].values[0]
    probs[eq] = [min(100, base + (i * base * 0.02) + np.random.normal(0, 1)) for i in range(30)]

fig = go.Figure()
for eq, prob in probs.items():
    fig.add_trace(go.Scatter(x=dates, y=prob, mode='lines', name=eq))

fig.add_hline(y=30, line_dash="dash", line_color=TELIT_RED, annotation_text="Action Threshold (30%)")
fig.update_layout(height=350, yaxis_range=[0, 50], yaxis_title="Failure Probability (%)",
                  legend=dict(orientation="h", yanchor="bottom", y=1.02))
st.plotly_chart(fig, use_container_width=True)

# ROI
st.subheader("💰 Predictive Maintenance ROI")

roi_cols = st.columns(4)
roi_data = [
    ("Downtime Reduction", "-42%", "vs. reactive"),
    ("Maintenance Costs", "-28%", "annual savings"),
    ("Equipment Life", "+15%", "extended"),
    ("Cost Avoidance", "$1.8M", "prevented failures")
]

for col, (label, value, sub) in zip(roi_cols, roi_data):
    with col:
        st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <div style="font-size: 28px; font-weight: 700; color: {TELIT_GREEN};">{value}</div>
                <div style="font-size: 14px; font-weight: 600; color: {TELIT_DARK};">{label}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

