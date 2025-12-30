"""
Quality Control - Snowflake Version
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

st.set_page_config(page_title="Quality Control", page_icon="✅", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">✅ Quality Control</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">SPC analytics and defect tracking</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("First Pass Yield", "98.7%", "↑ 0.3%")
col2.metric("Defect Rate", "0.8%", "↓ 0.2%")
col3.metric("Scrap Rate", "0.3%", "↓ 0.1%")
col4.metric("Rework Rate", "0.5%", "↓ 0.1%")
col5.metric("Returns", "0.12%", "↓ 0.02%")

st.markdown("---")

# Defect Pareto
st.subheader("📊 Defect Pareto Analysis")

defects = pd.DataFrame({
    'Defect': ['Solder Bridge', 'Missing Part', 'Misalignment', 'Cold Solder', 'Tombstone', 'Damage', 'Wrong Part', 'PCB Issue'],
    'Count': [245, 180, 142, 98, 72, 45, 28, 15]
})
defects['Cumulative'] = defects['Count'].cumsum() / defects['Count'].sum() * 100

fig = go.Figure()
fig.add_trace(go.Bar(x=defects['Defect'], y=defects['Count'], name='Count', marker_color=TELIT_BLUE))
fig.add_trace(go.Scatter(x=defects['Defect'], y=defects['Cumulative'], name='Cumulative %',
                         yaxis='y2', line=dict(color=TELIT_ORANGE, width=2), marker=dict(size=8)))
fig.update_layout(
    yaxis2=dict(title='Cumulative %', overlaying='y', side='right', range=[0, 105]),
    legend=dict(orientation="h", yanchor="bottom", y=1.02),
    height=350
)
st.plotly_chart(fig, use_container_width=True)

# Control Chart
st.subheader("📈 SPC Control Chart - Solder Paste Thickness")

np.random.seed(42)
dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
values = [2.5 + np.random.normal(0, 0.3) for _ in range(30)]
values[10], values[22] = 3.8, 1.2  # Out of control points

ucl, lcl, mean = 3.5, 1.5, 2.5
colors = [TELIT_RED if v > ucl or v < lcl else TELIT_BLUE for v in values]

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=[ucl]*30, mode='lines', name='UCL', line=dict(color=TELIT_RED, dash='dash')))
fig.add_trace(go.Scatter(x=dates, y=[lcl]*30, mode='lines', name='LCL', line=dict(color=TELIT_RED, dash='dash')))
fig.add_trace(go.Scatter(x=dates, y=[mean]*30, mode='lines', name='Mean', line=dict(color=TELIT_GREEN, dash='dot')))
fig.add_trace(go.Scatter(x=dates, y=values, mode='lines+markers', name='Value',
                         line=dict(color=TELIT_BLUE, width=2), marker=dict(color=colors, size=8)))
fig.update_layout(height=350, legend=dict(orientation="h", yanchor="bottom", y=1.02))
st.plotly_chart(fig, use_container_width=True)

# Alerts
st.markdown(f"""
    <div style="background: {TELIT_ORANGE}15; border-left: 4px solid {TELIT_ORANGE}; padding: 12px; border-radius: 0 8px 8px 0;">
        ⚠️ <strong>2 out-of-control points detected!</strong> - Investigate solder paste application process
    </div>
""", unsafe_allow_html=True)

# Quality by line
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏭 FPY by Production Line")
    lines = pd.DataFrame({
        'Line': ['SMT Line 1', 'SMT Line 2', 'Assembly', 'Testing'],
        'FPY': [99.2, 97.8, 98.9, 99.5]
    })
    fig = go.Figure(go.Bar(x=lines['Line'], y=lines['FPY'], marker_color=[TELIT_GREEN, TELIT_ORANGE, TELIT_GREEN, TELIT_GREEN]))
    fig.update_layout(height=300, yaxis_range=[95, 100])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📅 Daily Defect Trend")
    trend_dates = pd.date_range(end=datetime.now(), periods=14, freq='D')
    defect_trend = [45, 52, 48, 55, 42, 38, 35, 40, 38, 42, 35, 32, 30, 28]
    
    fig = go.Figure(go.Scatter(x=trend_dates, y=defect_trend, mode='lines+markers',
                               fill='tozeroy', line=dict(color=TELIT_BLUE), fillcolor=f'rgba(0,167,225,0.2)'))
    fig.add_hline(y=40, line_dash="dash", line_color=TELIT_GREEN, annotation_text="Target")
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

