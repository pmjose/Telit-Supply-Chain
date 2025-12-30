"""
Telit Supply Chain - Predictive Maintenance Dashboard
Equipment health monitoring and failure prediction
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

from components.styles import (
    get_telit_css, render_header, render_section_header, render_alert_card,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import get_equipment_health, get_sensor_readings
from components.charts import create_gauge_chart, create_line_chart

# Page config
st.set_page_config(page_title="Maintenance - Telit Supply Chain", page_icon="🔧", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>🔧 Predictive Maintenance</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Equipment Health</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    equipment_type = st.multiselect("Equipment Type", ["SMT", "Oven", "Inspection", "Testing", "Packaging"])
    alert_level = st.selectbox("Alert Level", ["All", "Critical Only", "Warning & Critical"])

# Header
st.markdown(render_header("Predictive Maintenance", "AI-powered equipment health monitoring and failure prediction"), unsafe_allow_html=True)

# Get data
equipment_df = get_equipment_health()

# Apply filters
if equipment_type:
    equipment_df = equipment_df[equipment_df['type'].isin(equipment_type)]

# =============================================================================
# KPI CARDS
# =============================================================================
total_equipment = len(equipment_df)
healthy = len(equipment_df[equipment_df['status'] == 'Good'])
warning = len(equipment_df[equipment_df['status'] == 'Warning'])
critical = len(equipment_df[equipment_df['status'] == 'Critical'])
avg_health = equipment_df['health_score'].mean()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">Total Equipment</div>
            <div class="kpi-value">{total_equipment}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center; border-top: 3px solid {TELIT_GREEN};">
            <div class="kpi-label">Healthy</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">{healthy}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center; border-top: 3px solid {TELIT_YELLOW};">
            <div class="kpi-label">Warning</div>
            <div class="kpi-value" style="color: {TELIT_YELLOW};">{warning}</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center; border-top: 3px solid {TELIT_RED};">
            <div class="kpi-label">Critical</div>
            <div class="kpi-value" style="color: {TELIT_RED};">{critical}</div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">Avg Health Score</div>
            <div class="kpi-value">{avg_health:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# ALERTS
# =============================================================================
critical_equipment = equipment_df[equipment_df['status'] == 'Critical']
if len(critical_equipment) > 0:
    for _, eq in critical_equipment.iterrows():
        st.markdown(render_alert_card(
            f"<strong>{eq['name']}</strong> requires immediate attention - Health Score: {eq['health_score']}% | "
            f"Failure Probability: {eq['failure_probability']}%",
            "critical", "🚨"
        ), unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["📊 Equipment Overview", "📈 Sensor Analytics", "🔮 Failure Prediction"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(render_section_header("Equipment Health Matrix"), unsafe_allow_html=True)
        
        # Health score bar chart
        equipment_sorted = equipment_df.sort_values('health_score')
        colors = [TELIT_RED if s < 70 else TELIT_YELLOW if s < 85 else TELIT_GREEN 
                  for s in equipment_sorted['health_score']]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=equipment_sorted['name'],
            x=equipment_sorted['health_score'],
            orientation='h',
            marker_color=colors,
            text=equipment_sorted['health_score'].round(1).astype(str) + '%',
            textposition='outside'
        ))
        
        fig.add_vline(x=70, line_dash="dash", line_color=TELIT_RED, opacity=0.5,
                      annotation_text="Critical", annotation_position="top")
        fig.add_vline(x=85, line_dash="dash", line_color=TELIT_YELLOW, opacity=0.5,
                      annotation_text="Warning", annotation_position="top")
        
        fig.update_layout(
            height=400,
            xaxis_title="Health Score (%)",
            xaxis_range=[0, 105],
            margin=dict(l=0, r=50, t=20, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Health Distribution"), unsafe_allow_html=True)
        
        fig = go.Figure(data=[go.Pie(
            values=[healthy, warning, critical],
            labels=['Healthy', 'Warning', 'Critical'],
            marker_colors=[TELIT_GREEN, TELIT_YELLOW, TELIT_RED],
            hole=0.6,
            textinfo='value+percent'
        )])
        
        fig.update_layout(
            height=300,
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Maintenance schedule
        st.markdown(render_section_header("Upcoming Maintenance"), unsafe_allow_html=True)
        
        upcoming = equipment_df.nsmallest(4, 'next_maintenance')[['name', 'next_maintenance']]
        for _, eq in upcoming.iterrows():
            days_until = (datetime.strptime(eq['next_maintenance'], '%Y-%m-%d') - datetime.now()).days
            urgency = TELIT_RED if days_until < 7 else TELIT_YELLOW if days_until < 14 else TELIT_GREEN
            st.markdown(f"""
                <div style="display: flex; justify-content: space-between; padding: 8px 0; border-bottom: 1px solid #e9ecef; font-size: 13px;">
                    <span>{eq['name'][:20]}...</span>
                    <span style="color: {urgency}; font-weight: 600;">{days_until}d</span>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown(render_section_header("Real-Time Sensor Data"), unsafe_allow_html=True)
    
    selected_equipment = st.selectbox("Select Equipment", equipment_df['name'].tolist())
    
    # Get sensor readings
    sensor_df = get_sensor_readings(selected_equipment)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Temperature Trend**")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=sensor_df['timestamp'], y=sensor_df['temperature'],
            mode='lines', fill='tozeroy',
            line=dict(color=TELIT_ORANGE), fillcolor='rgba(255,107,53,0.2)'
        ))
        fig.add_hline(y=60, line_dash="dash", line_color=TELIT_RED, annotation_text="Threshold")
        fig.update_layout(height=250, yaxis_title="°C")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**Vibration Analysis**")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=sensor_df['timestamp'], y=sensor_df['vibration'],
            mode='lines', fill='tozeroy',
            line=dict(color=TELIT_BLUE), fillcolor='rgba(0,167,225,0.2)'
        ))
        fig.add_hline(y=1.5, line_dash="dash", line_color=TELIT_RED, annotation_text="Threshold")
        fig.update_layout(height=250, yaxis_title="mm/s")
        st.plotly_chart(fig, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("**Power Consumption**")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=sensor_df['timestamp'], y=sensor_df['power_consumption'],
            mode='lines', fill='tozeroy',
            line=dict(color=TELIT_GREEN), fillcolor='rgba(0,196,140,0.2)'
        ))
        fig.update_layout(height=250, yaxis_title="kW")
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.markdown("**Cycle Time**")
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=sensor_df['timestamp'], y=sensor_df['cycle_time'],
            mode='lines', fill='tozeroy',
            line=dict(color='#9c27b0'), fillcolor='rgba(156,39,176,0.2)'
        ))
        fig.add_hline(y=15, line_dash="dash", line_color=TELIT_RED, annotation_text="Max")
        fig.update_layout(height=250, yaxis_title="seconds")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown(render_section_header("AI Failure Prediction"), unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Failure probability over time
        dates = [datetime.now() + timedelta(days=x) for x in range(30)]
        
        fig = go.Figure()
        
        for _, eq in equipment_df.iterrows():
            base_prob = eq['failure_probability']
            probabilities = [min(100, base_prob + (i * base_prob * 0.02) + np.random.normal(0, 1)) for i in range(30)]
            
            fig.add_trace(go.Scatter(
                x=dates, y=probabilities,
                mode='lines',
                name=eq['name'][:15],
                opacity=0.7
            ))
        
        fig.add_hline(y=30, line_dash="dash", line_color=TELIT_RED, 
                      annotation_text="Action Threshold (30%)")
        
        fig.update_layout(
            height=400,
            yaxis_title="Failure Probability (%)",
            yaxis_range=[0, 50],
            legend=dict(orientation="h", yanchor="bottom", y=1.02),
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Risk Factors"), unsafe_allow_html=True)
        
        risk_factors = [
            {"factor": "Age/Runtime Hours", "contribution": 35},
            {"factor": "Vibration Anomaly", "contribution": 25},
            {"factor": "Temperature Trend", "contribution": 20},
            {"factor": "Power Fluctuation", "contribution": 12},
            {"factor": "Maintenance Gap", "contribution": 8},
        ]
        
        for rf in risk_factors:
            st.markdown(f"""
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px;">
                        <span>{rf['factor']}</span>
                        <strong>{rf['contribution']}%</strong>
                    </div>
                    <div style="background: #e9ecef; height: 8px; border-radius: 4px;">
                        <div style="background: {TELIT_BLUE}; width: {rf['contribution']}%; height: 100%; border-radius: 4px;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style="background: {TELIT_BLUE}10; border-radius: 12px; padding: 16px;">
                <h4 style="margin: 0 0 8px 0; color: {TELIT_DARK};">💡 Recommendations</h4>
                <ul style="margin: 0; padding-left: 20px; font-size: 13px; color: {TELIT_GRAY};">
                    <li>Schedule SMT Line 2 maintenance within 7 days</li>
                    <li>Replace AOI Station 1 camera module</li>
                    <li>Calibrate reflow oven temperature sensors</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Maintenance ROI
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Predictive Maintenance ROI"), unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    metrics = [
        ("Unplanned Downtime", "-42%", "vs. reactive maintenance"),
        ("Maintenance Costs", "-28%", "annual savings"),
        ("Equipment Lifespan", "+15%", "extended life"),
        ("Cost Avoidance", "$1.8M", "prevented failures"),
    ]
    
    for col, (label, value, sub) in zip([col1, col2, col3, col4], metrics):
        with col:
            st.markdown(f"""
                <div style="background: white; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                    <div style="font-size: 28px; font-weight: 700; color: {TELIT_GREEN};">{value}</div>
                    <div style="font-size: 14px; font-weight: 600; color: {TELIT_DARK};">{label}</div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">{sub}</div>
                </div>
            """, unsafe_allow_html=True)

