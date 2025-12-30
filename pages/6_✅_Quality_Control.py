"""
Telit Supply Chain - Quality Control Dashboard
Defect analytics, control charts, and quality metrics
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
from components.fake_data import get_quality_metrics, get_defect_data, get_control_chart_data
from components.charts import create_pareto_chart, create_control_chart, create_gauge_chart

# Page config
st.set_page_config(page_title="Quality - Telit Supply Chain", page_icon="✅", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>✅ Quality Control</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Defect Analytics</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    date_range = st.date_input("Date Range", value=[])
    production_line = st.selectbox("Production Line", ["All Lines", "SMT Line 1", "SMT Line 2", "Assembly Line"])

# Header
st.markdown(render_header("Quality Control", "SPC analytics, defect tracking, and quality metrics"), unsafe_allow_html=True)

# Get data
quality_metrics = get_quality_metrics()
defect_df = get_defect_data()
control_df = get_control_chart_data()

# =============================================================================
# KPI CARDS
# =============================================================================
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">First Pass Yield</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">{quality_metrics['first_pass_yield']}%</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">Defect Rate</div>
            <div class="kpi-value">{quality_metrics['defect_rate']}%</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">Scrap Rate</div>
            <div class="kpi-value">{quality_metrics['scrap_rate']}%</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">Rework Rate</div>
            <div class="kpi-value">{quality_metrics['rework_rate']}%</div>
        </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
        <div class="kpi-card" style="text-align: center;">
            <div class="kpi-label">Customer Returns</div>
            <div class="kpi-value">{quality_metrics['customer_returns']}%</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["📊 Defect Analysis", "📈 Control Charts", "🔍 Root Cause"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(render_section_header("Defect Pareto Analysis"), unsafe_allow_html=True)
        fig = create_pareto_chart(defect_df, 'defect_type', 'count', "")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Quality Gauges"), unsafe_allow_html=True)
        
        fig1 = create_gauge_chart(quality_metrics['first_pass_yield'], "FPY", suffix="%", threshold_good=98, threshold_warning=95)
        st.plotly_chart(fig1, use_container_width=True)
        
        fig2 = create_gauge_chart(100 - quality_metrics['defect_rate'], "Quality Rate", suffix="%", threshold_good=99, threshold_warning=98)
        st.plotly_chart(fig2, use_container_width=True)
    
    # Defect trend
    st.markdown(render_section_header("Defect Trend (30 Days)"), unsafe_allow_html=True)
    
    from datetime import datetime, timedelta
    dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
    trend_df = pd.DataFrame({
        'date': dates,
        'defects': [int(50 + np.sin(i/5) * 15 + np.random.normal(0, 5)) for i in range(30)],
        'target': [45] * 30
    })
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=trend_df['date'], y=trend_df['defects'], mode='lines+markers',
                             name='Defects', line=dict(color=TELIT_BLUE, width=2)))
    fig.add_trace(go.Scatter(x=trend_df['date'], y=trend_df['target'], mode='lines',
                             name='Target', line=dict(color=TELIT_GREEN, dash='dash')))
    fig.update_layout(height=300, legend=dict(orientation="h", yanchor="bottom", y=1.02))
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown(render_section_header("Statistical Process Control"), unsafe_allow_html=True)
    
    # Control chart
    fig = create_control_chart(control_df, "Solder Paste Thickness (mm)")
    st.plotly_chart(fig, use_container_width=True)
    
    # Alert for out-of-control points
    out_of_control = control_df[(control_df['value'] > control_df['ucl']) | (control_df['value'] < control_df['lcl'])]
    
    if len(out_of_control) > 0:
        st.markdown(render_alert_card(
            f"<strong>{len(out_of_control)} out-of-control points detected!</strong><br>"
            f"Dates: {', '.join(out_of_control['date'].dt.strftime('%Y-%m-%d').tolist())}",
            "warning", "⚠️"
        ), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Multiple control charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**X-bar Chart (Mean)**")
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=control_df['date'], y=control_df['value'], mode='lines+markers',
                                 line=dict(color=TELIT_BLUE)))
        fig.add_hline(y=control_df['mean'].iloc[0], line_dash="dot", line_color=TELIT_GREEN)
        fig.add_hline(y=control_df['ucl'].iloc[0], line_dash="dash", line_color=TELIT_RED)
        fig.add_hline(y=control_df['lcl'].iloc[0], line_dash="dash", line_color=TELIT_RED)
        fig.update_layout(height=250, margin=dict(l=40, r=20, t=20, b=40))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("**R Chart (Range)**")
        range_values = [abs(np.random.normal(0, 0.2)) for _ in range(30)]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=control_df['date'], y=range_values, mode='lines+markers',
                                 line=dict(color=TELIT_ORANGE)))
        fig.add_hline(y=0.4, line_dash="dash", line_color=TELIT_RED)
        fig.update_layout(height=250, margin=dict(l=40, r=20, t=20, b=40))
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown(render_section_header("Root Cause Analysis"), unsafe_allow_html=True)
    
    # Fishbone diagram (using graphviz)
    import graphviz
    
    fish = graphviz.Digraph()
    fish.attr(rankdir='LR', bgcolor='transparent')
    fish.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')
    
    # Main effect
    fish.node('effect', 'Solder\nDefects', fillcolor='#ffebee', color='#ef5350', fontsize='12')
    
    # Categories
    categories = [
        ('machine', 'Machine', ['Temperature drift', 'Nozzle wear', 'Calibration']),
        ('material', 'Material', ['Paste viscosity', 'PCB quality', 'Component lot']),
        ('method', 'Method', ['Profile settings', 'Stencil design', 'Placement speed']),
        ('man', 'Operator', ['Training level', 'Shift handover', 'Fatigue']),
        ('env', 'Environment', ['Humidity', 'ESD control', 'Cleanliness']),
    ]
    
    for cat_id, cat_name, causes in categories:
        fish.node(cat_id, cat_name, fillcolor='#e3f2fd', color='#2196f3')
        fish.edge(cat_id, 'effect')
        for i, cause in enumerate(causes):
            cause_id = f"{cat_id}_{i}"
            fish.node(cause_id, cause, fillcolor='#f5f5f5', color='#9e9e9e', fontsize='9')
            fish.edge(cause_id, cat_id)
    
    st.graphviz_chart(fish, use_container_width=True)
    
    # Top root causes
    st.markdown(render_section_header("Top Contributing Factors"), unsafe_allow_html=True)
    
    root_causes = pd.DataFrame({
        'cause': ['Temperature Drift', 'Paste Viscosity', 'Nozzle Wear', 'Profile Settings', 'Humidity'],
        'contribution': [28, 22, 18, 15, 12],
        'status': ['In Progress', 'Resolved', 'Monitoring', 'In Progress', 'Resolved']
    })
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = px.bar(root_causes, x='contribution', y='cause', orientation='h',
                     color='status',
                     color_discrete_map={'In Progress': TELIT_YELLOW, 'Resolved': TELIT_GREEN, 'Monitoring': TELIT_BLUE})
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 12px rgba(0,0,0,0.06);">
                <h4 style="margin: 0 0 16px 0; color: {TELIT_DARK};">Action Items</h4>
                <div style="margin-bottom: 12px;">
                    <span style="background: {TELIT_YELLOW}20; color: {TELIT_YELLOW}; padding: 2px 8px; border-radius: 4px; font-size: 11px;">IN PROGRESS</span>
                    <div style="margin-top: 4px; font-size: 13px;">Calibrate reflow oven temperature sensors</div>
                </div>
                <div style="margin-bottom: 12px;">
                    <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 2px 8px; border-radius: 4px; font-size: 11px;">RESOLVED</span>
                    <div style="margin-top: 4px; font-size: 13px;">Updated solder paste storage protocol</div>
                </div>
                <div>
                    <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 2px 8px; border-radius: 4px; font-size: 11px;">MONITORING</span>
                    <div style="margin-top: 4px; font-size: 13px;">Implementing predictive nozzle replacement</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

