"""
Telit Supply Chain - Risk Intelligence Dashboard
Global supply chain risk monitoring and scenario analysis
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from components.styles import (
    get_telit_css, render_header, render_section_header, render_alert_card,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import get_risk_data, get_risk_by_region

# Page config
st.set_page_config(page_title="Risk - Telit Supply Chain", page_icon="⚠️", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>⚠️ Risk Intelligence</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Global Risk Monitoring</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    risk_category = st.multiselect("Risk Category", ["Geopolitical", "Natural Disaster", "Supplier", "Logistics", "Regulatory", "Cyber"])
    impact_level = st.selectbox("Impact Level", ["All", "High", "Medium", "Low"])

# Header
st.markdown(render_header("Risk Intelligence", "Real-time supply chain risk monitoring and scenario analysis"), unsafe_allow_html=True)

# Get data
risk_df = get_risk_data()
region_risk = get_risk_by_region()

# Apply filters
if risk_category:
    risk_df = risk_df[risk_df['category'].isin(risk_category)]
if impact_level != "All":
    risk_df = risk_df[risk_df['impact'] == impact_level]

# =============================================================================
# KPI CARDS
# =============================================================================
total_risks = len(risk_df)
high_risks = len(risk_df[risk_df['impact'] == 'High'])
avg_score = risk_df['score'].mean()
critical_alerts = len(risk_df[risk_df['score'] > 7])

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Risks Monitored</div>
            <div class="kpi-value">{total_risks}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card" style="border-top: 3px solid {TELIT_RED};">
            <div class="kpi-label">High Impact Risks</div>
            <div class="kpi-value" style="color: {TELIT_RED};">{high_risks}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Risk Score</div>
            <div class="kpi-value">{avg_score:.1f}</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">out of 10</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card" style="border-top: 3px solid {TELIT_ORANGE};">
            <div class="kpi-label">Critical Alerts</div>
            <div class="kpi-value" style="color: {TELIT_ORANGE};">{critical_alerts}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# CRITICAL ALERTS
# =============================================================================
high_score_risks = risk_df[risk_df['score'] > 7]
for _, risk in high_score_risks.iterrows():
    st.markdown(render_alert_card(
        f"<strong>[{risk['category']}]</strong> {risk['description']}<br>"
        f"<small>Region: {risk['region']} | Impact: {risk['impact']} | Probability: {risk['probability']*100:.0f}%</small>",
        "critical" if risk['score'] > 8 else "warning",
        "🚨" if risk['score'] > 8 else "⚠️"
    ), unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["🗺️ Risk Heatmap", "📊 Risk Analysis", "🎯 Scenario Planning"])

with tab1:
    st.markdown(render_section_header("Global Risk Heatmap"), unsafe_allow_html=True)
    
    # Regional risk data for map
    regions_data = pd.DataFrame([
        {"region": "North America", "lat": 40, "lon": -100, "risk_score": 4.2, "size": 25},
        {"region": "South America", "lat": -15, "lon": -60, "risk_score": 5.5, "size": 20},
        {"region": "Western Europe", "lat": 50, "lon": 10, "risk_score": 5.8, "size": 25},
        {"region": "Eastern Europe", "lat": 50, "lon": 30, "risk_score": 6.5, "size": 18},
        {"region": "Middle East", "lat": 25, "lon": 45, "risk_score": 7.2, "size": 20},
        {"region": "Africa", "lat": 0, "lon": 20, "risk_score": 6.0, "size": 15},
        {"region": "South Asia", "lat": 20, "lon": 78, "risk_score": 5.5, "size": 22},
        {"region": "East Asia", "lat": 35, "lon": 115, "risk_score": 7.1, "size": 30},
        {"region": "Southeast Asia", "lat": 5, "lon": 110, "risk_score": 5.8, "size": 20},
        {"region": "Oceania", "lat": -25, "lon": 135, "risk_score": 3.5, "size": 15},
    ])
    
    fig = px.scatter_mapbox(
        regions_data,
        lat='lat',
        lon='lon',
        size='size',
        color='risk_score',
        color_continuous_scale=[[0, TELIT_GREEN], [0.5, TELIT_YELLOW], [1, TELIT_RED]],
        hover_name='region',
        hover_data={'risk_score': True, 'lat': False, 'lon': False, 'size': False},
        zoom=1,
        mapbox_style="carto-positron"
    )
    
    fig.update_layout(
        height=450,
        margin={"r":0,"t":0,"l":0,"b":0},
        coloraxis_colorbar_title="Risk Score"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Region risk cards
    col1, col2, col3 = st.columns(3)
    
    for col, (_, region) in zip([col1, col2, col3], region_risk.iterrows()):
        risk_color = TELIT_RED if region['risk_score'] > 6 else TELIT_YELLOW if region['risk_score'] > 4 else TELIT_GREEN
        trend_icon = "↑" if region['trend'] == 'increasing' else "↓" if region['trend'] == 'decreasing' else "→"
        trend_color = TELIT_RED if region['trend'] == 'increasing' else TELIT_GREEN if region['trend'] == 'decreasing' else TELIT_GRAY
        
        with col:
            st.markdown(f"""
                <div style="background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <h3 style="margin: 0; color: {TELIT_DARK};">{region['region']}</h3>
                        <span style="font-size: 24px; font-weight: 700; color: {risk_color};">{region['risk_score']}</span>
                    </div>
                    <div style="margin-top: 8px; font-size: 13px;">
                        <span style="color: {trend_color};">{trend_icon} {region['trend'].capitalize()}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(render_section_header("Risk by Category"), unsafe_allow_html=True)
        
        category_risks = risk_df.groupby('category')['score'].mean().reset_index()
        category_risks = category_risks.sort_values('score', ascending=True)
        
        colors = [TELIT_RED if s > 7 else TELIT_YELLOW if s > 5 else TELIT_GREEN for s in category_risks['score']]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=category_risks['category'],
            x=category_risks['score'],
            orientation='h',
            marker_color=colors,
            text=category_risks['score'].round(1),
            textposition='outside'
        ))
        
        fig.update_layout(
            height=350,
            xaxis_title="Avg Risk Score",
            xaxis_range=[0, 10],
            margin=dict(l=0, r=40, t=20, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Risk Matrix"), unsafe_allow_html=True)
        
        fig = go.Figure()
        
        for _, risk in risk_df.iterrows():
            impact_val = {"High": 3, "Medium": 2, "Low": 1}[risk['impact']]
            fig.add_trace(go.Scatter(
                x=[risk['probability']],
                y=[impact_val],
                mode='markers+text',
                marker=dict(size=risk['score']*5, color=TELIT_RED if risk['score'] > 7 else TELIT_YELLOW if risk['score'] > 5 else TELIT_GREEN),
                text=[risk['category'][:10]],
                textposition='top center',
                name=risk['description'][:30],
                hovertemplate=f"<b>{risk['category']}</b><br>{risk['description']}<br>Score: {risk['score']}<extra></extra>"
            ))
        
        fig.update_layout(
            height=350,
            xaxis_title="Probability",
            yaxis=dict(
                ticktext=["Low", "Medium", "High"],
                tickvals=[1, 2, 3],
                title="Impact"
            ),
            showlegend=False,
            xaxis_range=[0, 1]
        )
        
        # Add quadrant backgrounds
        fig.add_shape(type="rect", x0=0.5, y0=2, x1=1, y1=3.5, fillcolor=TELIT_RED, opacity=0.1, line_width=0)
        fig.add_shape(type="rect", x0=0, y0=0.5, x1=0.5, y1=2, fillcolor=TELIT_GREEN, opacity=0.1, line_width=0)
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Risk register table
    st.markdown(render_section_header("Risk Register"), unsafe_allow_html=True)
    
    display_df = risk_df[['id', 'category', 'description', 'impact', 'probability', 'score', 'region']]
    
    st.dataframe(
        display_df,
        column_config={
            "id": "Risk ID",
            "category": "Category",
            "description": st.column_config.TextColumn("Description", width="large"),
            "impact": "Impact",
            "probability": st.column_config.NumberColumn("Probability", format="%.0f%%"),
            "score": st.column_config.ProgressColumn("Risk Score", min_value=0, max_value=10),
            "region": "Region"
        },
        hide_index=True,
        use_container_width=True
    )

with tab3:
    st.markdown(render_section_header("What-If Scenario Analysis"), unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Select Scenario:**")
        scenario = st.selectbox(
            "Scenario Type",
            ["Taiwan Strait Disruption", "Major Port Closure", "Key Supplier Bankruptcy", "Pandemic Resurgence", "Cyber Attack on Logistics"],
            label_visibility="collapsed"
        )
        
        duration = st.slider("Duration (weeks)", 1, 12, 4)
        severity = st.select_slider("Severity", ["Low", "Medium", "High", "Critical"], value="High")
        
        if st.button("🔮 Run Scenario Analysis", type="primary"):
            st.session_state['scenario_run'] = True
    
    with col2:
        if st.session_state.get('scenario_run', False):
            st.markdown(f"""
                <div style="background: {TELIT_RED}10; border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_RED};">
                    <h4 style="margin: 0 0 12px 0;">Scenario: {scenario}</h4>
                    <p style="margin: 0; color: {TELIT_GRAY};">Duration: {duration} weeks | Severity: {severity}</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Impact metrics
            impact_col1, impact_col2, impact_col3, impact_col4 = st.columns(4)
            
            impacts = [
                ("Revenue Impact", f"-${np.random.randint(5, 25)}M", TELIT_RED),
                ("Supply Delay", f"+{np.random.randint(2, 8)} weeks", TELIT_ORANGE),
                ("Affected Products", f"{np.random.randint(3, 8)}", TELIT_YELLOW),
                ("Alt Suppliers Needed", f"{np.random.randint(2, 5)}", TELIT_BLUE),
            ]
            
            for col, (label, value, color) in zip([impact_col1, impact_col2, impact_col3, impact_col4], impacts):
                with col:
                    st.markdown(f"""
                        <div style="background: white; border-radius: 10px; padding: 16px; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.05);">
                            <div style="font-size: 24px; font-weight: 700; color: {color};">{value}</div>
                            <div style="font-size: 12px; color: {TELIT_GRAY};">{label}</div>
                        </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(render_section_header("Recommended Mitigations"), unsafe_allow_html=True)
            
            mitigations = [
                {"action": "Activate secondary supplier agreements", "timeline": "Immediate", "cost": "$500K"},
                {"action": "Increase safety stock for critical components", "timeline": "1-2 weeks", "cost": "$1.2M"},
                {"action": "Expedite shipments via air freight", "timeline": "Ongoing", "cost": "$800K"},
                {"action": "Customer communication and order prioritization", "timeline": "Immediate", "cost": "N/A"},
            ]
            
            for mit in mitigations:
                st.markdown(f"""
                    <div style="display: flex; align-items: center; padding: 12px; background: white; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
                        <div style="flex: 1;">
                            <strong style="color: {TELIT_DARK};">{mit['action']}</strong>
                        </div>
                        <div style="text-align: right;">
                            <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 2px 8px; border-radius: 4px; font-size: 11px; margin-right: 8px;">{mit['timeline']}</span>
                            <span style="color: {TELIT_GRAY}; font-size: 12px;">{mit['cost']}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background: #f8fafc; border-radius: 12px; padding: 40px; text-align: center;">
                    <div style="font-size: 48px; margin-bottom: 16px;">🎯</div>
                    <h3 style="color: {TELIT_DARK}; margin: 0 0 8px 0;">Run a Scenario Analysis</h3>
                    <p style="color: {TELIT_GRAY};">Select a scenario type, duration, and severity to see the potential impact on your supply chain.</p>
                </div>
            """, unsafe_allow_html=True)

