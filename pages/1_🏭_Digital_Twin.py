"""
Telit Supply Chain - Digital Twin / Smart Factory Dashboard
Interactive factory floor visualization with real-time KPIs
"""

import streamlit as st
import pandas as pd
import graphviz
from datetime import datetime

from components.styles import (
    get_telit_css, render_header, render_section_header,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import (
    get_factory_zones, get_factory_kpis, get_production_flow, get_equipment_health
)
from components.factory_map import (
    render_factory_floor, render_factory_kpi_panel, render_equipment_list
)
from components.charts import create_gauge_chart, create_line_chart

# Page config
st.set_page_config(
    page_title="Digital Twin - Telit Supply Chain",
    page_icon="🏭",
    layout="wide"
)

st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f"""
        <div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">
            {TELIT_LOGO_SVG}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px; margin-bottom: 20px;">
            <div style="color: white; font-size: 13px;">
                <strong>🏭 Digital Twin</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Smart Factory Dashboard</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Factory selector
    st.selectbox("Select Factory", ["Telit Manufacturing - Germany", "Telit Assembly - China", "Telit Production - USA"])
    
    # Auto-refresh toggle
    auto_refresh = st.toggle("Auto Refresh", value=True)
    if auto_refresh:
        st.markdown("""
            <div style="color: rgba(255,255,255,0.6); font-size: 11px;">
                ⟳ Refreshing every 30 seconds
            </div>
        """, unsafe_allow_html=True)

# Header
st.markdown(render_header(
    "Digital Twin - Smart Factory",
    "Real-time visualization of factory operations and equipment status"
), unsafe_allow_html=True)

# Get data
zones = get_factory_zones()
kpis = get_factory_kpis()
production = get_production_flow()
equipment = get_equipment_health()

# =============================================================================
# TOP KPI BAR
# =============================================================================
kpi_cols = st.columns(8)

kpi_items = [
    ("OEE", f"{kpis['oee']['value']}%", kpis['oee']['status']),
    ("Throughput", f"{kpis['throughput']['value']:,}", kpis['throughput']['status']),
    ("Quality", f"{kpis['quality_rate']['value']}%", kpis['quality_rate']['status']),
    ("Availability", f"{kpis['availability']['value']}%", kpis['availability']['status']),
    ("Performance", f"{kpis['performance']['value']}%", kpis['performance']['status']),
    ("Workers", f"{kpis['active_workers']['value']}", kpis['active_workers']['status']),
    ("Machines", f"{kpis['active_machines']['value']}/20", kpis['active_machines']['status']),
    ("Energy", f"{kpis['energy_kwh']['value']} kWh", kpis['energy_kwh']['status']),
]

for col, (label, value, status) in zip(kpi_cols, kpi_items):
    status_color = TELIT_GREEN if status == 'good' else TELIT_YELLOW if status == 'warning' else TELIT_RED
    with col:
        st.markdown(f"""
            <div style="
                background: white;
                border-radius: 10px;
                padding: 12px;
                text-align: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.06);
                border-top: 3px solid {status_color};
            ">
                <div style="font-size: 11px; color: {TELIT_GRAY}; text-transform: uppercase;">{label}</div>
                <div style="font-size: 20px; font-weight: 700; color: {TELIT_DARK};">{value}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# MAIN CONTENT - TABS
# =============================================================================
tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Factory Floor", "⚙️ Equipment Status", "📊 Production Flow", "📈 Analytics"])

with tab1:
    # Factory Floor Map
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(render_section_header("Interactive Factory Floor Map"), unsafe_allow_html=True)
        
        # Render the SVG factory map
        factory_svg = render_factory_floor(zones, width=680, height=450)
        st.markdown(f"""
            <div style="
                background: white;
                border-radius: 16px;
                padding: 20px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            ">
                {factory_svg}
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(render_section_header("Zone Details"), unsafe_allow_html=True)
        
        # Zone selector
        selected_zone = st.selectbox(
            "Select Zone",
            options=[z['name'] for z in zones],
            index=0
        )
        
        # Get selected zone data
        zone_data = next((z for z in zones if z['name'] == selected_zone), zones[0])
        
        status_color = TELIT_GREEN if zone_data['status'] == 'active' else TELIT_YELLOW if zone_data['status'] == 'warning' else TELIT_GRAY
        
        st.markdown(f"""
            <div style="
                background: white;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 2px 12px rgba(0,0,0,0.06);
            ">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 16px;">
                    <span style="
                        width: 12px;
                        height: 12px;
                        border-radius: 50%;
                        background: {status_color};
                        display: inline-block;
                    "></span>
                    <span style="font-size: 18px; font-weight: 600; color: {TELIT_DARK};">{zone_data['name']}</span>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                        <div style="font-size: 11px; color: {TELIT_GRAY};">UTILIZATION</div>
                        <div style="font-size: 24px; font-weight: 700; color: {TELIT_DARK};">{zone_data['utilization']}%</div>
                    </div>
                    <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                        <div style="font-size: 11px; color: {TELIT_GRAY};">UNITS TODAY</div>
                        <div style="font-size: 24px; font-weight: 700; color: {TELIT_DARK};">{zone_data['units_today']:,}</div>
                    </div>
                    <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                        <div style="font-size: 11px; color: {TELIT_GRAY};">TEMPERATURE</div>
                        <div style="font-size: 24px; font-weight: 700; color: {TELIT_DARK};">{zone_data['temperature']}°C</div>
                    </div>
                    <div style="background: #f8fafc; padding: 12px; border-radius: 8px;">
                        <div style="font-size: 11px; color: {TELIT_GRAY};">HUMIDITY</div>
                        <div style="font-size: 24px; font-weight: 700; color: {TELIT_DARK};">{zone_data['humidity']}%</div>
                    </div>
                </div>
                
                <div style="margin-top: 16px; padding-top: 16px; border-top: 1px solid #e9ecef;">
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Workers on shift: <strong>{zone_data['workers']}</strong></div>
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Status: <strong style="color: {status_color};">{zone_data['status'].upper()}</strong></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Live sensors card
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_DARK}dd 100%);
                border-radius: 12px;
                padding: 16px;
                color: white;
            ">
                <div style="font-size: 12px; opacity: 0.8; margin-bottom: 8px;">🔴 LIVE SENSOR DATA</div>
                <div style="display: flex; justify-content: space-between; font-size: 13px;">
                    <span>Connected Sensors</span>
                    <strong>847</strong>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 13px;">
                    <span>Data Points/sec</span>
                    <strong>12,450</strong>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 13px;">
                    <span>Last Update</span>
                    <strong>{datetime.now().strftime('%H:%M:%S')}</strong>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown(render_section_header("Equipment Health Monitoring"), unsafe_allow_html=True)
    
    # Equipment health summary
    eq_df = pd.DataFrame(equipment.to_dict('records'))
    
    col1, col2, col3 = st.columns(3)
    
    good_count = len(eq_df[eq_df['status'] == 'Good'])
    warning_count = len(eq_df[eq_df['status'] == 'Warning'])
    critical_count = len(eq_df[eq_df['status'] == 'Critical'])
    
    with col1:
        st.markdown(f"""
            <div style="background: rgba(0,196,140,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_GREEN};">
                <div style="font-size: 36px; font-weight: 700; color: {TELIT_GREEN};">{good_count}</div>
                <div style="font-size: 14px; color: {TELIT_DARK};">Equipment in Good Condition</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style="background: rgba(255,184,0,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_YELLOW};">
                <div style="font-size: 36px; font-weight: 700; color: {TELIT_YELLOW};">{warning_count}</div>
                <div style="font-size: 14px; color: {TELIT_DARK};">Require Attention</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div style="background: rgba(255,71,87,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_RED};">
                <div style="font-size: 36px; font-weight: 700; color: {TELIT_RED};">{critical_count}</div>
                <div style="font-size: 14px; color: {TELIT_DARK};">Critical Status</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Equipment table
    st.markdown(render_equipment_list(equipment.to_dict('records')), unsafe_allow_html=True)

with tab3:
    st.markdown(render_section_header("Production Flow Diagram"), unsafe_allow_html=True)
    
    # Production flow stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Input", f"{production['total_input']:,} units")
    with col2:
        st.metric("In Progress", f"{production['in_progress']:,} units")
    with col3:
        st.metric("Completed", f"{production['completed']:,} units")
    with col4:
        st.metric("Scrapped", f"{production['scrapped']:,} units")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Graphviz flow diagram
    flow = graphviz.Digraph()
    flow.attr(rankdir='LR', bgcolor='transparent')
    flow.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='11')
    flow.attr('edge', fontname='Arial', fontsize='9')
    
    # Define nodes with colors
    flow.node('receiving', 'Receiving\n▣ 3 Docks', fillcolor='#E3F2FD', color='#00A7E1')
    flow.node('warehouse', 'Warehouse\n▣ 45,000 units', fillcolor='#E3F2FD', color='#00A7E1')
    flow.node('smt1', 'SMT Line 1\n⚡ 847 units/hr', fillcolor='#E8F5E9', color='#00C48C')
    flow.node('smt2', 'SMT Line 2\n⚡ 792 units/hr', fillcolor='#E8F5E9', color='#00C48C')
    flow.node('testing', 'Testing\n✓ 98.7% pass', fillcolor='#E8F5E9', color='#00C48C')
    flow.node('quality', 'Quality Lab\n◉ 24 samples', fillcolor='#FFF3E0', color='#FF6B35')
    flow.node('packaging', 'Packaging\n📦 2,340/hr', fillcolor='#E8F5E9', color='#00C48C')
    flow.node('shipping', 'Shipping\n🚛 Ready', fillcolor='#E3F2FD', color='#00A7E1')
    
    # Define edges
    flow.edge('receiving', 'warehouse', 'Inbound')
    flow.edge('receiving', 'smt1', 'Direct')
    flow.edge('warehouse', 'smt1')
    flow.edge('warehouse', 'smt2')
    flow.edge('smt1', 'testing')
    flow.edge('smt2', 'testing')
    flow.edge('testing', 'quality', 'Samples', style='dashed')
    flow.edge('testing', 'packaging')
    flow.edge('packaging', 'shipping')
    
    st.graphviz_chart(flow, use_container_width=True)
    
    # Production metrics
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Production Metrics"), unsafe_allow_html=True)
    
    met_col1, met_col2, met_col3 = st.columns(3)
    
    with met_col1:
        fig = create_gauge_chart(production['oee'], "OEE", suffix="%", threshold_good=85)
        st.plotly_chart(fig, use_container_width=True)
    
    with met_col2:
        fig = create_gauge_chart(production['throughput_rate'], "Throughput Rate", max_value=1000, suffix=" u/hr", threshold_good=800, threshold_warning=600)
        st.plotly_chart(fig, use_container_width=True)
    
    with met_col3:
        fig = create_gauge_chart(production['cycle_time'], "Cycle Time", max_value=60, suffix=" sec", threshold_good=45, threshold_warning=50)
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.markdown(render_section_header("Production Analytics"), unsafe_allow_html=True)
    
    # Generate sample analytics data
    import numpy as np
    from datetime import timedelta
    
    hours = 24
    timestamps = [datetime.now() - timedelta(hours=x) for x in range(hours, 0, -1)]
    
    analytics_df = pd.DataFrame({
        'timestamp': timestamps,
        'throughput': [800 + np.sin(i/3) * 100 + np.random.normal(0, 20) for i in range(hours)],
        'oee': [85 + np.sin(i/4) * 5 + np.random.normal(0, 2) for i in range(hours)],
        'quality': [98 + np.random.normal(0, 0.5) for _ in range(hours)],
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = create_line_chart(analytics_df, 'timestamp', ['throughput'], "Throughput Over Time", show_area=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = create_line_chart(analytics_df, 'timestamp', ['oee', 'quality'], "OEE & Quality Trends")
        st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown(f"""
    <div style="text-align: center; padding: 20px; margin-top: 40px; border-top: 1px solid #e9ecef; color: {TELIT_GRAY}; font-size: 12px;">
        Digital Twin Dashboard | Powered by Snowflake ❄️ | Real-time IoT Data Processing
    </div>
""", unsafe_allow_html=True)

