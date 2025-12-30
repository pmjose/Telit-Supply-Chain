"""
Carbon Footprint & ESG - Snowflake Version
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Carbon & ESG", page_icon="🌱", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_GREEN}90 0%, {TELIT_GREEN}70 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🌱 Carbon Footprint & ESG</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 8px 0 0 0;">Sustainability metrics and environmental impact</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Emissions", "12,450 t CO₂", "↓ 8.5% YoY")
col2.metric("Renewable Energy", "62%", "↑ 8%")
col3.metric("Waste Diverted", "78%", "↑ 5%")
col4.metric("Water Recycled", "45%", "↑ 12%")

st.markdown("---")

# Emissions breakdown
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Emissions by Scope")
    scopes = pd.DataFrame({
        'Scope': ['Scope 1\n(Direct)', 'Scope 2\n(Indirect)', 'Scope 3\n(Value Chain)'],
        'Emissions': [3200, 7800, 1450]
    })
    colors = [TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN]
    
    fig = go.Figure(go.Bar(x=scopes['Scope'], y=scopes['Emissions'], marker_color=colors,
                           text=scopes['Emissions'], textposition='outside'))
    fig.update_layout(height=350, yaxis_title="Tons CO₂e")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🎯 Emissions Breakdown")
    fig = go.Figure(go.Pie(
        values=[3200, 7800, 1450],
        labels=['Scope 1', 'Scope 2', 'Scope 3'],
        hole=0.6,
        marker_colors=[TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN]
    ))
    fig.update_layout(height=350,
        annotations=[dict(text='12,450', x=0.5, y=0.55, font_size=24, showarrow=False),
                    dict(text='tons CO₂e', x=0.5, y=0.42, font_size=12, showarrow=False)])
    st.plotly_chart(fig, use_container_width=True)

# Progress gauges
st.subheader("🎯 2030 Net Zero Progress")
g1, g2, g3 = st.columns(3)

for col, (label, value, target) in zip([g1, g2, g3], 
    [("Carbon Reduction", 75, "50% by 2030"), ("Renewable Energy", 62, "100% by 2030"), ("Zero Waste", 78, "95% by 2030")]):
    with col:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': label},
            number={'suffix': '%'},
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': TELIT_GREEN},
                   'steps': [{'range': [0, 50], 'color': "#ffebee"},
                            {'range': [50, 75], 'color': "#fff3e0"},
                            {'range': [75, 100], 'color': "#e8f5e9"}]}
        ))
        fig.update_layout(height=220, margin=dict(t=80, b=0))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"<div style='text-align:center;color:{TELIT_GRAY};font-size:12px;'>Target: {target}</div>", unsafe_allow_html=True)

# Initiatives
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🚀 Sustainability Initiatives")

initiatives = [
    ("Solar Panel Installation", "In Progress", 75, "-850 t CO₂/year", TELIT_ORANGE),
    ("Fleet Electrification", "Planned", 25, "-420 t CO₂/year", TELIT_BLUE),
    ("Packaging Optimization", "Completed", 100, "-180 t CO₂/year", TELIT_GREEN),
    ("Supplier Green Program", "In Progress", 60, "-1,200 t CO₂/year", TELIT_ORANGE),
]

for name, status, progress, impact, color in initiatives:
    st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <div>
                    <strong>{name}</strong>
                    <span style="background: {color}20; color: {color}; padding: 2px 8px; border-radius: 10px; font-size: 11px; margin-left: 8px;">{status}</span>
                </div>
                <span style="color: {TELIT_GREEN}; font-weight: 600;">{impact}</span>
            </div>
            <div style="background: #e9ecef; height: 8px; border-radius: 4px;">
                <div style="background: {color}; width: {progress}%; height: 100%; border-radius: 4px;"></div>
            </div>
            <div style="text-align: right; font-size: 11px; color: {TELIT_GRAY}; margin-top: 4px;">{progress}% complete</div>
        </div>
    """, unsafe_allow_html=True)

# ESG Scorecard
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📋 ESG Scorecard")

e1, e2, e3 = st.columns(3)

with e1:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e8f5e9 0%, white 100%); border-radius: 16px; padding: 24px; text-align: center;">
            <div style="font-size: 40px;">🌍</div>
            <h3>Environmental</h3>
            <div style="font-size: 36px; font-weight: 700; color: {TELIT_GREEN};">A</div>
            <div style="font-size: 13px; color: {TELIT_GRAY};">Carbon: -15% YoY</div>
        </div>
    """, unsafe_allow_html=True)

with e2:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e3f2fd 0%, white 100%); border-radius: 16px; padding: 24px; text-align: center;">
            <div style="font-size: 40px;">👥</div>
            <h3>Social</h3>
            <div style="font-size: 36px; font-weight: 700; color: {TELIT_BLUE};">A-</div>
            <div style="font-size: 13px; color: {TELIT_GRAY};">Safety: 0.8 TRIR</div>
        </div>
    """, unsafe_allow_html=True)

with e3:
    st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f3e5f5 0%, white 100%); border-radius: 16px; padding: 24px; text-align: center;">
            <div style="font-size: 40px;">⚖️</div>
            <h3>Governance</h3>
            <div style="font-size: 36px; font-weight: 700; color: #9c27b0;">A</div>
            <div style="font-size: 13px; color: {TELIT_GRAY};">Ethics: 100%</div>
        </div>
    """, unsafe_allow_html=True)

