"""
Telit Supply Chain - Supply Chain Visibility Dashboard
End-to-end shipment tracking and supply chain flow visualization
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import graphviz

from components.styles import (
    get_telit_css, render_header, render_section_header, render_status_indicator,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import get_active_shipments, WAREHOUSES
from components.charts import create_donut_chart

# Page config
st.set_page_config(page_title="Visibility - Telit Supply Chain", page_icon="🚚", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>🚚 Supply Chain Visibility</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">End-to-end Tracking</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    status_filter = st.multiselect("Filter by Status", ["In Transit", "Customs Clearance", "At Hub", "Out for Delivery", "Delivered"])
    carrier_filter = st.multiselect("Filter by Carrier", ["DHL Express", "FedEx", "UPS", "Maersk", "Kuehne+Nagel"])

# Header
st.markdown(render_header("Supply Chain Visibility", "Real-time tracking of all shipments and supply chain flow"), unsafe_allow_html=True)

# Get data
shipments_df = get_active_shipments()

# Apply filters
if status_filter:
    shipments_df = shipments_df[shipments_df['status'].isin(status_filter)]
if carrier_filter:
    shipments_df = shipments_df[shipments_df['carrier'].isin(carrier_filter)]

# =============================================================================
# KPI CARDS
# =============================================================================
total_shipments = len(shipments_df)
in_transit = len(shipments_df[shipments_df['status'] == 'In Transit'])
delivered = len(shipments_df[shipments_df['status'] == 'Delivered'])
total_value = shipments_df['value'].sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Active Shipments</div>
            <div class="kpi-value">{total_shipments}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">In Transit</div>
            <div class="kpi-value" style="color: {TELIT_BLUE};">{in_transit}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Delivered Today</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">{delivered}</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Value in Transit</div>
            <div class="kpi-value">${total_value/1000000:.1f}M</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["🗺️ Live Tracking Map", "📊 Shipment Analytics", "🔗 Supply Chain Flow"])

with tab1:
    st.markdown(render_section_header("Global Shipment Tracking"), unsafe_allow_html=True)
    
    # Create map with routes
    fig = go.Figure()
    
    # Add shipment routes
    for _, ship in shipments_df.head(20).iterrows():
        # Draw line from origin to destination
        fig.add_trace(go.Scattermapbox(
            lon=[ship['origin_lon'], ship['dest_lon']],
            lat=[ship['origin_lat'], ship['dest_lat']],
            mode='lines',
            line=dict(width=2, color=TELIT_BLUE),
            opacity=0.5,
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Add current position marker (interpolated based on progress)
        progress = ship['progress'] / 100
        current_lon = ship['origin_lon'] + (ship['dest_lon'] - ship['origin_lon']) * progress
        current_lat = ship['origin_lat'] + (ship['dest_lat'] - ship['origin_lat']) * progress
        
        status_color = {
            'In Transit': TELIT_BLUE,
            'Customs Clearance': TELIT_YELLOW,
            'At Hub': TELIT_ORANGE,
            'Out for Delivery': TELIT_GREEN,
            'Delivered': TELIT_GREEN
        }.get(ship['status'], TELIT_GRAY)
        
        fig.add_trace(go.Scattermapbox(
            lon=[current_lon],
            lat=[current_lat],
            mode='markers',
            marker=dict(size=12, color=status_color),
            name=ship['shipment_id'],
            text=f"{ship['shipment_id']}<br>{ship['status']}<br>ETA: {ship['eta']}",
            hovertemplate="<b>%{text}</b><extra></extra>"
        ))
    
    # Add warehouse markers
    for wh in WAREHOUSES:
        fig.add_trace(go.Scattermapbox(
            lon=[wh['lon']],
            lat=[wh['lat']],
            mode='markers',
            marker=dict(size=18, color=TELIT_DARK, symbol='square'),
            name=wh['name'],
            text=wh['name'],
            hovertemplate="<b>%{text}</b><br>Warehouse<extra></extra>"
        ))
    
    fig.update_layout(
        mapbox=dict(style="carto-positron", center=dict(lat=30, lon=0), zoom=1.5),
        margin={"r":0,"t":0,"l":0,"b":0},
        height=450,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Shipment legend
    st.markdown(f"""
        <div style="display: flex; gap: 20px; justify-content: center; padding: 10px; background: white; border-radius: 8px;">
            <span><span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:{TELIT_BLUE};margin-right:6px;"></span>In Transit</span>
            <span><span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:{TELIT_YELLOW};margin-right:6px;"></span>Customs</span>
            <span><span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:{TELIT_ORANGE};margin-right:6px;"></span>At Hub</span>
            <span><span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:{TELIT_GREEN};margin-right:6px;"></span>Delivered</span>
            <span><span style="display:inline-block;width:12px;height:12px;background:{TELIT_DARK};margin-right:6px;"></span>Warehouse</span>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(render_section_header("Shipments by Status"), unsafe_allow_html=True)
        status_counts = shipments_df['status'].value_counts().reset_index()
        status_counts.columns = ['status', 'count']
        fig = create_donut_chart(status_counts, 'count', 'status')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Shipments by Carrier"), unsafe_allow_html=True)
        carrier_counts = shipments_df['carrier'].value_counts().reset_index()
        carrier_counts.columns = ['carrier', 'count']
        fig = px.bar(carrier_counts, x='count', y='carrier', orientation='h',
                     color_discrete_sequence=[TELIT_BLUE])
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=300,
                          xaxis_title="", yaxis_title="", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(render_section_header("Active Shipments"), unsafe_allow_html=True)
    
    # Shipment table
    display_df = shipments_df[['shipment_id', 'origin', 'destination', 'status', 'carrier', 'eta', 'progress', 'value']].head(15)
    
    st.dataframe(
        display_df,
        column_config={
            "shipment_id": "Shipment ID",
            "origin": "Origin",
            "destination": "Destination",
            "status": st.column_config.TextColumn("Status"),
            "carrier": "Carrier",
            "eta": "ETA",
            "progress": st.column_config.ProgressColumn("Progress", min_value=0, max_value=100),
            "value": st.column_config.NumberColumn("Value", format="$%d"),
        },
        hide_index=True,
        use_container_width=True
    )

with tab3:
    st.markdown(render_section_header("End-to-End Supply Chain Flow"), unsafe_allow_html=True)
    
    # Graphviz supply chain flow
    flow = graphviz.Digraph()
    flow.attr(rankdir='LR', bgcolor='transparent', splines='ortho')
    flow.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')
    
    # Tier 2 Suppliers
    flow.node('tier2_1', 'Raw Materials\n(Tier 2)', fillcolor='#fce4ec', color='#e91e63')
    flow.node('tier2_2', 'Semiconductors\n(Tier 2)', fillcolor='#fce4ec', color='#e91e63')
    
    # Tier 1 Suppliers
    flow.node('tier1_1', 'Taiwan Semi\n(Chipsets)', fillcolor='#fff3e0', color='#ff9800')
    flow.node('tier1_2', 'Qualcomm\n(Modems)', fillcolor='#fff3e0', color='#ff9800')
    flow.node('tier1_3', 'Murata\n(Passives)', fillcolor='#fff3e0', color='#ff9800')
    
    # Manufacturing
    flow.node('mfg', 'Telit\nManufacturing', fillcolor='#e3f2fd', color='#2196f3')
    
    # Distribution Centers
    flow.node('dc_us', 'DC Americas\n(Los Angeles)', fillcolor='#e8f5e9', color='#4caf50')
    flow.node('dc_eu', 'DC EMEA\n(Frankfurt)', fillcolor='#e8f5e9', color='#4caf50')
    flow.node('dc_ap', 'DC APAC\n(Shanghai)', fillcolor='#e8f5e9', color='#4caf50')
    
    # Customers
    flow.node('cust_1', 'Automotive\nOEMs', fillcolor='#ede7f6', color='#673ab7')
    flow.node('cust_2', 'Industrial\nIoT', fillcolor='#ede7f6', color='#673ab7')
    flow.node('cust_3', 'Smart\nMetering', fillcolor='#ede7f6', color='#673ab7')
    
    # Edges
    flow.edge('tier2_1', 'tier1_1')
    flow.edge('tier2_2', 'tier1_1')
    flow.edge('tier2_1', 'tier1_2')
    flow.edge('tier2_2', 'tier1_3')
    
    flow.edge('tier1_1', 'mfg')
    flow.edge('tier1_2', 'mfg')
    flow.edge('tier1_3', 'mfg')
    
    flow.edge('mfg', 'dc_us')
    flow.edge('mfg', 'dc_eu')
    flow.edge('mfg', 'dc_ap')
    
    flow.edge('dc_us', 'cust_1')
    flow.edge('dc_us', 'cust_2')
    flow.edge('dc_eu', 'cust_2')
    flow.edge('dc_eu', 'cust_3')
    flow.edge('dc_ap', 'cust_1')
    flow.edge('dc_ap', 'cust_3')
    
    st.graphviz_chart(flow, use_container_width=True)
    
    # Supply chain metrics
    st.markdown("<br>", unsafe_allow_html=True)
    met_col1, met_col2, met_col3, met_col4 = st.columns(4)
    
    with met_col1:
        st.metric("Avg Lead Time", "18.5 days", "-2.3 days")
    with met_col2:
        st.metric("Perfect Order Rate", "94.7%", "+1.2%")
    with met_col3:
        st.metric("Supply Chain Cost", "$2.4M", "-5.8%")
    with met_col4:
        st.metric("Carbon per Shipment", "12.4 kg", "-8.2%")

