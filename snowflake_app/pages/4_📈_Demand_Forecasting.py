"""
Demand Forecasting - Snowflake Version
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
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Demand Forecasting", page_icon="📈", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">📈 Demand Forecasting</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">AI/ML-powered demand predictions</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Forecasted Demand", "847K units", "Next 12 months")
col2.metric("Avg Growth Rate", "+12.5%", "YoY")
col3.metric("Forecast Accuracy", "94.2%", "↑ 1.5%")
col4.metric("MAPE", "5.8%", "↓ 0.4%")

st.markdown("---")

# Generate forecast data
np.random.seed(42)
dates = pd.date_range(start='2024-06-01', periods=18, freq='M')
historical = [8000 + np.sin(i/3) * 1500 + np.random.normal(0, 300) for i in range(6)]
forecast = [historical[-1] + (i+1) * 200 + np.sin(i/3) * 1000 for i in range(12)]
lower = [f * 0.9 for f in forecast]
upper = [f * 1.1 for f in forecast]

# Forecast chart
st.subheader("📊 Demand Forecast - ME310G1")

fig = go.Figure()

# Historical
fig.add_trace(go.Scatter(x=dates[:6], y=historical, mode='lines+markers',
                         name='Historical', line=dict(color=TELIT_BLUE, width=2)))

# Forecast
fig.add_trace(go.Scatter(x=dates[5:], y=[historical[-1]] + forecast, mode='lines+markers',
                         name='Forecast', line=dict(color=TELIT_ORANGE, width=2, dash='dot')))

# Confidence band
fig.add_trace(go.Scatter(x=list(dates[6:]) + list(dates[6:])[::-1],
                         y=upper + lower[::-1], fill='toself',
                         fillcolor='rgba(255,107,53,0.15)', line=dict(color='rgba(0,0,0,0)'),
                         name='95% Confidence'))

fig.add_vline(x=dates[5], line_dash="dash", line_color=TELIT_GRAY, opacity=0.5)
fig.update_layout(height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02))
st.plotly_chart(fig, use_container_width=True)

# Seasonality
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Seasonality Index")
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    seasonality = [0.85, 0.88, 0.95, 1.02, 1.08, 1.12, 1.05, 0.98, 1.15, 1.20, 1.10, 0.92]
    colors = [TELIT_GREEN if s >= 1 else TELIT_ORANGE for s in seasonality]
    
    fig = go.Figure(go.Bar(x=months, y=seasonality, marker_color=colors))
    fig.add_hline(y=1, line_dash="dash", line_color=TELIT_GRAY)
    fig.update_layout(height=300, yaxis_title="Seasonal Index")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🎯 Forecast Accuracy Trend")
    acc_months = pd.date_range(end=datetime.now(), periods=12, freq='M')
    accuracy = [92, 93, 91, 94, 93, 95, 94, 93, 95, 94, 95, 94]
    
    fig = go.Figure(go.Scatter(x=acc_months, y=accuracy, mode='lines+markers',
                               line=dict(color=TELIT_GREEN, width=2), fill='tozeroy',
                               fillcolor='rgba(0,196,140,0.2)'))
    fig.update_layout(height=300, yaxis_range=[85, 100], yaxis_title="Accuracy %")
    st.plotly_chart(fig, use_container_width=True)

# Recommendations
st.subheader("💡 Planning Recommendations")

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
        <div style="background: {TELIT_GREEN}15; border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_GREEN};">
            <h4 style="margin: 0 0 12px 0;">📈 Growth Products</h4>
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>FN980 5G</strong> - +28% growth expected</li>
                <li><strong>ME310G1</strong> - +22% growth expected</li>
                <li><strong>WE310F6 Wi-Fi 6</strong> - +18% growth</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="background: {TELIT_ORANGE}15; border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_ORANGE};">
            <h4 style="margin: 0 0 12px 0;">⚠️ Demand Spikes</h4>
            <ul style="margin: 0; padding-left: 20px;">
                <li><strong>Q4 2024</strong> - Holiday surge (+35%)</li>
                <li><strong>Q2 2025</strong> - Automotive launch (+25%)</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

