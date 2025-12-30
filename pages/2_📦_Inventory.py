"""
Telit Supply Chain - IoT Module Inventory Dashboard
Real-time inventory visibility across global warehouses
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.styles import (
    get_telit_css, render_header, render_section_header, render_alert_card,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import (
    get_inventory_levels, get_warehouse_summary, TELIT_PRODUCTS, WAREHOUSES
)
from components.charts import create_bar_chart, create_heatmap, create_gauge_chart

# Page config
st.set_page_config(page_title="Inventory - Telit Supply Chain", page_icon="📦", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>📦 Inventory Management</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">IoT Module Stock Levels</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Filters
    st.markdown("<br>", unsafe_allow_html=True)
    region_filter = st.multiselect("Filter by Region", ["Americas", "EMEA", "APAC"], default=["Americas", "EMEA", "APAC"])
    category_filter = st.multiselect("Filter by Category", list(set([p['category'] for p in TELIT_PRODUCTS])))

# Header
st.markdown(render_header("IoT Module Inventory", "Real-time stock levels and warehouse distribution"), unsafe_allow_html=True)

# Get data
inventory_df = get_inventory_levels()
warehouse_df = get_warehouse_summary()

# Apply filters
if region_filter:
    inventory_df = inventory_df[inventory_df['region'].isin(region_filter)]
    warehouse_df = warehouse_df[warehouse_df['region'].isin(region_filter)]

# =============================================================================
# KPI CARDS
# =============================================================================
total_units = inventory_df['current_stock'].sum()
low_stock_items = len(inventory_df[inventory_df['status'] == 'Low Stock'])
avg_dos = inventory_df['days_of_supply'].mean()
warehouse_util = warehouse_df['utilization'].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Units in Stock</div>
            <div class="kpi-value">{total_units:,}</div>
            <div class="kpi-change positive">↑ 5.2% vs last month</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Low Stock Alerts</div>
            <div class="kpi-value" style="color: {TELIT_RED if low_stock_items > 10 else TELIT_YELLOW};">{low_stock_items}</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">Items below reorder point</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Days of Supply</div>
            <div class="kpi-value">{avg_dos:.1f}</div>
            <div class="kpi-change positive">↑ 2.1 days vs target</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Warehouse Utilization</div>
            <div class="kpi-value">{warehouse_util:.1f}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">Across all locations</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["🏭 Warehouse Overview", "📊 Stock Analysis", "⚠️ Alerts & Reorders"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(render_section_header("Global Warehouse Network"), unsafe_allow_html=True)
        
        # Map with warehouses
        fig = px.scatter_mapbox(
            warehouse_df,
            lat='lat',
            lon='lon',
            size='current_units',
            color='utilization',
            color_continuous_scale=[[0, TELIT_GREEN], [0.7, TELIT_YELLOW], [1, TELIT_RED]],
            hover_name='name',
            hover_data=['region', 'current_units', 'capacity', 'utilization'],
            zoom=1,
            mapbox_style="carto-positron"
        )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Warehouse Utilization"), unsafe_allow_html=True)
        
        for _, wh in warehouse_df.iterrows():
            util = wh['utilization']
            color = TELIT_GREEN if util < 70 else TELIT_YELLOW if util < 90 else TELIT_RED
            st.markdown(f"""
                <div style="background: white; padding: 12px; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                        <span style="font-weight: 600; font-size: 13px;">{wh['name']}</span>
                        <span style="color: {color}; font-weight: 600;">{util:.1f}%</span>
                    </div>
                    <div style="background: #e9ecef; height: 6px; border-radius: 3px;">
                        <div style="background: {color}; width: {util}%; height: 100%; border-radius: 3px;"></div>
                    </div>
                    <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 4px;">{int(wh['current_units']):,} / {int(wh['capacity']):,} units</div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(render_section_header("Stock by Product Category"), unsafe_allow_html=True)
        category_stock = inventory_df.groupby('category')['current_stock'].sum().reset_index()
        fig = create_bar_chart(category_stock, 'category', 'current_stock', horizontal=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(render_section_header("Stock by Region"), unsafe_allow_html=True)
        region_stock = inventory_df.groupby('region')['current_stock'].sum().reset_index()
        fig = px.pie(region_stock, values='current_stock', names='region', hole=0.5,
                     color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN])
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(render_section_header("Inventory Heatmap (Warehouse x Product)"), unsafe_allow_html=True)
    
    # Pivot table for heatmap
    pivot_df = inventory_df.pivot_table(
        values='current_stock', 
        index='product_name', 
        columns='warehouse_name', 
        aggfunc='sum'
    ).fillna(0)
    
    fig = px.imshow(
        pivot_df.head(8),
        color_continuous_scale=[[0, '#f0f9ff'], [0.5, TELIT_BLUE], [1, TELIT_DARK]],
        aspect='auto'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown(render_section_header("Low Stock Alerts"), unsafe_allow_html=True)
    
    low_stock_df = inventory_df[inventory_df['status'] == 'Low Stock'].sort_values('days_of_supply')
    
    if len(low_stock_df) > 0:
        for _, item in low_stock_df.head(10).iterrows():
            severity = "critical" if item['days_of_supply'] < 5 else "warning"
            st.markdown(render_alert_card(
                f"<strong>{item['product_name']}</strong> at {item['warehouse_name']}<br>"
                f"Current: {item['current_stock']:,} | Reorder Point: {item['reorder_point']:,} | "
                f"<strong>{item['days_of_supply']} days of supply</strong>",
                severity,
                "🔴" if severity == "critical" else "🟡"
            ), unsafe_allow_html=True)
    else:
        st.success("✅ All inventory levels are healthy!")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Reorder Recommendations"), unsafe_allow_html=True)
    
    # Show reorder table
    reorder_df = low_stock_df[['product_name', 'warehouse_name', 'current_stock', 'reorder_point', 'days_of_supply']].copy()
    reorder_df['suggested_order'] = (reorder_df['reorder_point'] * 2 - reorder_df['current_stock']).clip(lower=0)
    
    st.dataframe(
        reorder_df.head(10),
        column_config={
            "product_name": "Product",
            "warehouse_name": "Warehouse",
            "current_stock": st.column_config.NumberColumn("Current Stock", format="%d"),
            "reorder_point": st.column_config.NumberColumn("Reorder Point", format="%d"),
            "days_of_supply": st.column_config.NumberColumn("Days of Supply", format="%.1f"),
            "suggested_order": st.column_config.NumberColumn("Suggested Order", format="%d"),
        },
        hide_index=True,
        use_container_width=True
    )

