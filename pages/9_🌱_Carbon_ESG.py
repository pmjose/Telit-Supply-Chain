"""
Telit Supply Chain - Carbon Footprint & ESG Dashboard
Sustainability metrics and environmental impact tracking
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

from components.styles import (
    get_telit_css, render_header, render_section_header,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_GRAY
)
from components.fake_data import get_carbon_metrics, get_emissions_trend
from components.charts import create_gauge_chart

# Page config
st.set_page_config(page_title="ESG - Telit Supply Chain", page_icon="🌱", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>🌱 Carbon & ESG</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Sustainability Metrics</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    year = st.selectbox("Reporting Year", [2024, 2023, 2022])
    scope = st.multiselect("Emission Scope", ["Scope 1", "Scope 2", "Scope 3"], default=["Scope 1", "Scope 2", "Scope 3"])

# Header
st.markdown(render_header("Carbon Footprint & ESG", "Environmental sustainability and emissions tracking"), unsafe_allow_html=True)

# Get data
carbon = get_carbon_metrics()
emissions_df = get_emissions_trend(12)

# =============================================================================
# KPI CARDS
# =============================================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card" style="background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);">
            <div class="kpi-label">Total Emissions</div>
            <div class="kpi-value">{carbon['total_emissions']:,}</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">tons CO₂e</div>
            <div class="kpi-change positive">↓ {carbon['yoy_reduction']}% YoY</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Renewable Energy</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">{carbon['renewable_energy_pct']}%</div>
            <div class="kpi-change positive">↑ 8% vs target</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Waste Diverted</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">{carbon['waste_diverted_pct']}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">from landfill</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Water Recycled</div>
            <div class="kpi-value">{carbon['water_recycled_pct']}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">of total usage</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["📊 Emissions Overview", "🎯 Targets & Progress", "📋 ESG Scorecard"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(render_section_header("Emissions by Scope"), unsafe_allow_html=True)
        
        scope_data = pd.DataFrame({
            'scope': ['Scope 1\n(Direct)', 'Scope 2\n(Indirect)', 'Scope 3\n(Value Chain)'],
            'emissions': [carbon['scope1_emissions'], carbon['scope2_emissions'], carbon['scope3_emissions']],
            'description': ['Direct emissions from owned sources', 'Indirect emissions from purchased energy', 'All other indirect emissions']
        })
        
        fig = go.Figure()
        
        colors = [TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN]
        for i, row in scope_data.iterrows():
            fig.add_trace(go.Bar(
                x=[row['scope']],
                y=[row['emissions']],
                name=row['scope'].split('\n')[0],
                marker_color=colors[i],
                text=f"{row['emissions']:,}",
                textposition='outside'
            ))
        
        fig.update_layout(
            height=350,
            showlegend=False,
            yaxis_title="Tons CO₂e",
            bargap=0.4
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Emissions Breakdown"), unsafe_allow_html=True)
        
        # Donut chart
        fig = go.Figure(data=[go.Pie(
            values=[carbon['scope1_emissions'], carbon['scope2_emissions'], carbon['scope3_emissions']],
            labels=['Scope 1', 'Scope 2', 'Scope 3'],
            hole=0.6,
            marker_colors=[TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN],
            textinfo='percent+label'
        )])
        
        fig.update_layout(
            height=350,
            showlegend=False,
            annotations=[dict(text=f'{carbon["total_emissions"]:,}', x=0.5, y=0.5, font_size=20, showarrow=False),
                        dict(text='tons CO₂e', x=0.5, y=0.4, font_size=12, showarrow=False)]
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Emissions trend
    st.markdown(render_section_header("Monthly Emissions Trend"), unsafe_allow_html=True)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=emissions_df['date'], y=emissions_df['emissions'],
        mode='lines+markers',
        fill='tozeroy',
        line=dict(color=TELIT_GREEN, width=2),
        fillcolor='rgba(0,196,140,0.2)'
    ))
    
    # Add target line
    fig.add_hline(y=carbon['carbon_target']/12, line_dash="dash", line_color=TELIT_ORANGE,
                  annotation_text="Monthly Target")
    
    fig.update_layout(height=300, xaxis_title="", yaxis_title="Tons CO₂e")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown(render_section_header("2030 Net Zero Progress"), unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fig = create_gauge_chart(carbon['carbon_progress'], "Carbon Reduction", suffix="%", threshold_good=70, threshold_warning=50)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"<div style='text-align:center;color:{TELIT_GRAY};font-size:12px;'>Target: 50% reduction by 2030</div>", unsafe_allow_html=True)
    
    with col2:
        fig = create_gauge_chart(carbon['renewable_energy_pct'], "Renewable Energy", suffix="%", threshold_good=80, threshold_warning=50)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"<div style='text-align:center;color:{TELIT_GRAY};font-size:12px;'>Target: 100% by 2030</div>", unsafe_allow_html=True)
    
    with col3:
        fig = create_gauge_chart(carbon['waste_diverted_pct'], "Zero Waste", suffix="%", threshold_good=90, threshold_warning=70)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(f"<div style='text-align:center;color:{TELIT_GRAY};font-size:12px;'>Target: 95% diversion by 2030</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Sustainability Initiatives"), unsafe_allow_html=True)
    
    initiatives = [
        {"name": "Solar Panel Installation", "status": "In Progress", "impact": "-850 tons CO₂/year", "completion": 75, "color": TELIT_YELLOW},
        {"name": "Fleet Electrification", "status": "Planned", "impact": "-420 tons CO₂/year", "completion": 25, "color": TELIT_BLUE},
        {"name": "Packaging Optimization", "status": "Completed", "impact": "-180 tons CO₂/year", "completion": 100, "color": TELIT_GREEN},
        {"name": "Supplier Green Program", "status": "In Progress", "impact": "-1,200 tons CO₂/year", "completion": 60, "color": TELIT_YELLOW},
    ]
    
    for init in initiatives:
        st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div>
                        <strong style="color: {TELIT_DARK};">{init['name']}</strong>
                        <span style="background: {init['color']}20; color: {init['color']}; padding: 2px 8px; border-radius: 10px; font-size: 11px; margin-left: 8px;">{init['status']}</span>
                    </div>
                    <span style="color: {TELIT_GREEN}; font-weight: 600;">{init['impact']}</span>
                </div>
                <div style="background: #e9ecef; height: 8px; border-radius: 4px;">
                    <div style="background: {init['color']}; width: {init['completion']}%; height: 100%; border-radius: 4px;"></div>
                </div>
                <div style="text-align: right; font-size: 11px; color: {TELIT_GRAY}; margin-top: 4px;">{init['completion']}% complete</div>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown(render_section_header("ESG Performance Scorecard"), unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # Environmental
    with col1:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e8f5e9 0%, white 100%); border-radius: 16px; padding: 24px; height: 100%;">
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 48px;">🌍</div>
                    <h3 style="margin: 8px 0; color: {TELIT_DARK};">Environmental</h3>
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_GREEN};">A</div>
                </div>
                <div style="font-size: 13px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Carbon Intensity</span><strong style="color: {TELIT_GREEN};">-15% YoY</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Renewable Energy</span><strong>{carbon['renewable_energy_pct']}%</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Water Efficiency</span><strong>+12% YoY</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Waste Reduction</span><strong style="color: {TELIT_GREEN};">-22% YoY</strong>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Social
    with col2:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #e3f2fd 0%, white 100%); border-radius: 16px; padding: 24px; height: 100%;">
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 48px;">👥</div>
                    <h3 style="margin: 8px 0; color: {TELIT_DARK};">Social</h3>
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_BLUE};">A-</div>
                </div>
                <div style="font-size: 13px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Employee Safety</span><strong style="color: {TELIT_GREEN};">0.8 TRIR</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Diversity Index</span><strong>42%</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Training Hours</span><strong>40 hrs/emp</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Community Investment</span><strong>$1.2M</strong>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Governance
    with col3:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f3e5f5 0%, white 100%); border-radius: 16px; padding: 24px; height: 100%;">
                <div style="text-align: center; margin-bottom: 20px;">
                    <div style="font-size: 48px;">⚖️</div>
                    <h3 style="margin: 8px 0; color: {TELIT_DARK};">Governance</h3>
                    <div style="font-size: 36px; font-weight: 700; color: #9c27b0;">A</div>
                </div>
                <div style="font-size: 13px;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Board Independence</span><strong>78%</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Ethics Compliance</span><strong style="color: {TELIT_GREEN};">100%</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
                        <span>Supplier Audits</span><strong>95%</strong>
                    </div>
                    <div style="display: flex; justify-content: space-between;">
                        <span>Data Privacy</span><strong style="color: {TELIT_GREEN};">ISO 27001</strong>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

