"""
Telit Supply Chain Intelligence Platform
Powered by Snowflake - Executive Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Import custom components
from components.styles import (
    get_telit_css, render_kpi_card, render_header, render_section_header,
    render_alert_card, render_snowflake_badge, TELIT_LOGO_SVG,
    TELIT_BLUE, TELIT_DARK, TELIT_NAVY, TELIT_ORANGE, TELIT_GREEN, TELIT_RED, TELIT_YELLOW, TELIT_GRAY
)
from components.fake_data import (
    get_executive_kpis, get_revenue_by_region, get_revenue_trend,
    get_top_products, get_active_alerts, get_warehouse_summary, WAREHOUSES
)
from components.charts import (
    create_gauge_chart, create_donut_chart, create_line_chart,
    create_bar_chart, create_scatter_mapbox
)

# Page configuration
st.set_page_config(
    page_title="Executive Dashboard - Telit Supply Chain",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_telit_css(), unsafe_allow_html=True)

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
    # Telit Logo
    st.markdown(f"""
        <div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">
            {TELIT_LOGO_SVG}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="color: rgba(255,255,255,0.7); font-size: 12px; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px;">
            Supply Chain Intelligence
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation info
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px; margin-bottom: 20px;">
            <div style="color: white; font-size: 13px;">
                <strong>📊 Executive Dashboard</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Overview of all KPIs</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Snowflake badge
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    st.markdown(render_snowflake_badge(), unsafe_allow_html=True)
    
    # Last updated
    st.markdown(f"""
        <div style="color: rgba(255,255,255,0.5); font-size: 11px; margin-top: 20px;">
            Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        </div>
    """, unsafe_allow_html=True)

# =============================================================================
# MAIN CONTENT - EXECUTIVE DASHBOARD
# =============================================================================

# Header
st.markdown(render_header(
    "Executive Dashboard",
    "Real-time overview of global supply chain operations"
), unsafe_allow_html=True)

# Get data
kpis = get_executive_kpis()
revenue_by_region = get_revenue_by_region()
revenue_trend = get_revenue_trend(30)
top_products = get_top_products()
alerts = get_active_alerts()
warehouses = get_warehouse_summary()

# =============================================================================
# KPI CARDS ROW
# =============================================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(render_kpi_card(
        "Total Revenue (YTD)",
        f"${kpis['revenue']['value']}M",
        kpis['revenue']['change']
    ), unsafe_allow_html=True)

with col2:
    st.markdown(render_kpi_card(
        "Orders in Transit",
        f"{kpis['orders_in_transit']['value']:,}",
        kpis['orders_in_transit']['change']
    ), unsafe_allow_html=True)

with col3:
    st.markdown(render_kpi_card(
        "Inventory Value",
        f"${kpis['inventory_value']['value']}M",
        kpis['inventory_value']['change']
    ), unsafe_allow_html=True)

with col4:
    st.markdown(render_kpi_card(
        "On-Time Delivery",
        f"{kpis['on_time_delivery']['value']}%",
        kpis['on_time_delivery']['change']
    ), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# MAIN DASHBOARD GRID
# =============================================================================
left_col, right_col = st.columns([2, 1])

with left_col:
    # Global Operations Map
    st.markdown(render_section_header("Global Operations"), unsafe_allow_html=True)
    
    # Create warehouse map
    warehouse_locations = [
        {**wh, 'status': 'ok'} for wh in WAREHOUSES
    ]
    
    fig_map = create_scatter_mapbox(warehouse_locations, "")
    st.plotly_chart(fig_map, use_container_width=True)
    
    # Revenue Trend
    st.markdown(render_section_header("Revenue Trend (30 Days)"), unsafe_allow_html=True)
    fig_trend = create_line_chart(revenue_trend, 'date', ['revenue'], show_area=True)
    fig_trend.update_layout(height=280)
    st.plotly_chart(fig_trend, use_container_width=True)

with right_col:
    # Supply Chain Health Gauges
    st.markdown(render_section_header("Supply Chain Health"), unsafe_allow_html=True)
    
    gauge_col1, gauge_col2 = st.columns(2)
    
    with gauge_col1:
        fig_inv = create_gauge_chart(87, "Inventory", suffix="%")
        st.plotly_chart(fig_inv, use_container_width=True)
        
        fig_qual = create_gauge_chart(94, "Quality", suffix="%")
        st.plotly_chart(fig_qual, use_container_width=True)
    
    with gauge_col2:
        fig_del = create_gauge_chart(91, "Delivery", suffix="%")
        st.plotly_chart(fig_del, use_container_width=True)
        
        fig_sup = create_gauge_chart(88, "Supplier", suffix="%")
        st.plotly_chart(fig_sup, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# BOTTOM ROW
# =============================================================================
bottom_col1, bottom_col2, bottom_col3 = st.columns(3)

with bottom_col1:
    st.markdown(render_section_header("Revenue by Region"), unsafe_allow_html=True)
    fig_region = create_donut_chart(revenue_by_region, 'revenue', 'region')
    fig_region.update_layout(height=320)
    st.plotly_chart(fig_region, use_container_width=True)

with bottom_col2:
    st.markdown(render_section_header("Top Products by Sales"), unsafe_allow_html=True)
    
    top_products_df = pd.DataFrame(top_products)
    fig_products = create_bar_chart(
        top_products_df.head(6), 
        'name', 
        'units_sold',
        horizontal=True
    )
    fig_products.update_layout(height=320)
    st.plotly_chart(fig_products, use_container_width=True)

with bottom_col3:
    st.markdown(render_section_header("Active Alerts"), unsafe_allow_html=True)
    
    for alert in alerts[:4]:
        icon_map = {
            "critical": "🔴",
            "warning": "🟡", 
            "info": "🔵",
            "success": "🟢"
        }
        st.markdown(render_alert_card(
            f"{alert['message']}<br><small style='opacity:0.6'>{alert['time']}</small>",
            alert['type'],
            icon_map.get(alert['type'], "ℹ️")
        ), unsafe_allow_html=True)

# =============================================================================
# SECONDARY METRICS ROW
# =============================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(render_section_header("Operational Metrics"), unsafe_allow_html=True)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown(f"""
        <div class="kpi-card" style="text-align:center;">
            <div style="font-size: 3rem; margin-bottom: 8px;">🏭</div>
            <div class="kpi-value">{kpis['manufacturing_oee']['value']}%</div>
            <div class="kpi-label">Manufacturing OEE</div>
            <div class="kpi-change positive">↑ {kpis['manufacturing_oee']['change']}%</div>
        </div>
    """, unsafe_allow_html=True)

with metric_col2:
    st.markdown(f"""
        <div class="kpi-card" style="text-align:center;">
            <div style="font-size: 3rem; margin-bottom: 8px;">🤝</div>
            <div class="kpi-value">{kpis['active_suppliers']['value']}</div>
            <div class="kpi-label">Active Suppliers</div>
            <div class="kpi-change positive">↑ {kpis['active_suppliers']['change']}%</div>
        </div>
    """, unsafe_allow_html=True)

with metric_col3:
    st.markdown(f"""
        <div class="kpi-card" style="text-align:center;">
            <div style="font-size: 3rem; margin-bottom: 8px;">✅</div>
            <div class="kpi-value">{kpis['defect_rate']['value']}%</div>
            <div class="kpi-label">Defect Rate</div>
            <div class="kpi-change positive">↓ {abs(kpis['defect_rate']['change'])}%</div>
        </div>
    """, unsafe_allow_html=True)

with metric_col4:
    st.markdown(f"""
        <div class="kpi-card" style="text-align:center;">
            <div style="font-size: 3rem; margin-bottom: 8px;">🌱</div>
            <div class="kpi-value">{kpis['carbon_footprint']['value']:,}</div>
            <div class="kpi-label">Carbon (tons CO₂)</div>
            <div class="kpi-change positive">↓ {abs(kpis['carbon_footprint']['change'])}%</div>
        </div>
    """, unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; padding: 20px; border-top: 1px solid #e9ecef; color: {TELIT_GRAY}; font-size: 12px;">
        <strong>Telit Supply Chain Intelligence Platform</strong> | Powered by Snowflake ❄️<br>
        © 2024 Telit Cinterion. All rights reserved.
    </div>
""", unsafe_allow_html=True)

