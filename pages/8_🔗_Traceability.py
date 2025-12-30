"""
Telit Supply Chain - Component Traceability Dashboard
Track components through manufacturing lifecycle with genealogy trees
"""

import streamlit as st
import pandas as pd
import graphviz
from datetime import datetime

from components.styles import (
    get_telit_css, render_header, render_section_header, render_alert_card,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import get_component_genealogy, TELIT_PRODUCTS

# Page config
st.set_page_config(page_title="Traceability - Telit Supply Chain", page_icon="🔗", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>🔗 Component Traceability</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Genealogy & Tracking</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    batch_id = st.text_input("Batch/Lot Number", "BATCH-2024-001")
    product_filter = st.selectbox("Product", [p['name'] for p in TELIT_PRODUCTS])

# Header
st.markdown(render_header("Component Traceability", "Track components from raw materials to customer delivery"), unsafe_allow_html=True)

# Get data
genealogy = get_component_genealogy(batch_id)

# =============================================================================
# KPI CARDS
# =============================================================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Batch ID</div>
            <div class="kpi-value" style="font-size: 1.3rem;">{genealogy['batch_id']}</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">{genealogy['product']}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Production Quantity</div>
            <div class="kpi-value">{genealogy['quantity']:,}</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">{genealogy['production_date']}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Test Yield</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">{genealogy['test_results']['yield']}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">{genealogy['test_results']['passed']:,} passed</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Components Tracked</div>
            <div class="kpi-value">{len(genealogy['components'])}</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">Unique part types</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["🌳 Genealogy Tree", "📋 Component Details", "🔄 Recall Simulation"])

with tab1:
    st.markdown(render_section_header("Component Genealogy Tree"), unsafe_allow_html=True)
    
    # Create genealogy graphviz
    tree = graphviz.Digraph()
    tree.attr(rankdir='TB', bgcolor='transparent', splines='ortho')
    tree.attr('node', shape='box', style='rounded,filled', fontname='Arial', fontsize='10')
    
    # Finished product (root)
    tree.node('product', f"Finished Product\\n{genealogy['product']}\\nBatch: {genealogy['batch_id']}\\nQty: {genealogy['quantity']:,}",
              fillcolor='#e8f5e9', color='#4caf50', fontsize='11')
    
    # Components
    for i, comp in enumerate(genealogy['components']):
        comp_id = f"comp_{i}"
        tree.node(comp_id, f"{comp['name']}\\nLot: {comp['lot']}\\nQty: {comp['quantity']:,}\\nSupplier: {comp['supplier']}",
                  fillcolor='#e3f2fd', color='#2196f3')
        tree.edge(comp_id, 'product')
        
        # Raw materials
        raw_id = f"raw_{i}"
        tree.node(raw_id, f"Raw Material\\n{comp['supplier']}",
                  fillcolor='#fff3e0', color='#ff9800', fontsize='9')
        tree.edge(raw_id, comp_id)
    
    # Customers
    for i, cust in enumerate(genealogy['shipped_to']):
        cust_id = f"cust_{i}"
        tree.node(cust_id, f"Customer\\n{cust}",
                  fillcolor='#f3e5f5', color='#9c27b0')
        tree.edge('product', cust_id)
    
    st.graphviz_chart(tree, use_container_width=True)
    
    # Traceability path
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Traceability Timeline"), unsafe_allow_html=True)
    
    timeline_events = [
        ("2024-12-10", "Raw Materials", "Components received from suppliers", TELIT_ORANGE),
        ("2024-12-12", "Incoming QC", "Quality inspection completed - 100% pass", TELIT_GREEN),
        ("2024-12-15", "Production", f"Batch {genealogy['batch_id']} manufactured", TELIT_BLUE),
        ("2024-12-16", "Testing", f"{genealogy['test_results']['yield']}% yield achieved", TELIT_GREEN),
        ("2024-12-17", "Packaging", "Units packaged and labeled", TELIT_BLUE),
        ("2024-12-18", "Shipment", f"Shipped to {len(genealogy['shipped_to'])} customers", TELIT_DARK),
    ]
    
    for date, stage, description, color in timeline_events:
        st.markdown(f"""
            <div style="display: flex; align-items: center; margin-bottom: 12px;">
                <div style="width: 100px; font-size: 12px; color: {TELIT_GRAY};">{date}</div>
                <div style="width: 16px; height: 16px; border-radius: 50%; background: {color}; margin-right: 16px;"></div>
                <div style="flex: 1; background: white; padding: 12px 16px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
                    <strong style="color: {TELIT_DARK};">{stage}</strong>
                    <div style="font-size: 13px; color: {TELIT_GRAY};">{description}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown(render_section_header("Component Bill of Materials"), unsafe_allow_html=True)
    
    # Components table
    comp_df = pd.DataFrame(genealogy['components'])
    
    st.dataframe(
        comp_df,
        column_config={
            "name": "Component",
            "supplier": "Supplier",
            "lot": "Lot Number",
            "quantity": st.column_config.NumberColumn("Quantity", format="%d"),
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Component detail cards
    st.markdown(render_section_header("Component Details"), unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, comp in enumerate(genealogy['components']):
        with cols[i % 2]:
            st.markdown(f"""
                <div style="background: white; border-radius: 12px; padding: 16px; margin-bottom: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div>
                            <strong style="color: {TELIT_DARK}; font-size: 15px;">{comp['name']}</strong>
                            <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 4px;">Lot: {comp['lot']}</div>
                        </div>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 600;">VERIFIED</span>
                    </div>
                    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #e9ecef;">
                        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 12px;">
                            <div><span style="color: {TELIT_GRAY};">Supplier:</span> <strong>{comp['supplier']}</strong></div>
                            <div><span style="color: {TELIT_GRAY};">Quantity:</span> <strong>{comp['quantity']:,}</strong></div>
                            <div><span style="color: {TELIT_GRAY};">Received:</span> <strong>2024-12-10</strong></div>
                            <div><span style="color: {TELIT_GRAY};">IQC Status:</span> <strong style="color: {TELIT_GREEN};">PASS</strong></div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

with tab3:
    st.markdown(render_section_header("Recall Impact Simulation"), unsafe_allow_html=True)
    
    st.markdown(f"""
        <div style="background: rgba(255,71,87,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_RED}; margin-bottom: 20px;">
            <h4 style="margin: 0 0 8px 0; color: {TELIT_RED};">⚠️ Recall Simulation Mode</h4>
            <p style="margin: 0; color: {TELIT_DARK};">This tool simulates the impact of a component recall to help assess exposure and plan containment actions.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Recall parameters
    col1, col2 = st.columns(2)
    
    with col1:
        affected_component = st.selectbox("Affected Component", [c['name'] for c in genealogy['components']])
        affected_lot = st.text_input("Affected Lot Number", genealogy['components'][0]['lot'])
    
    with col2:
        recall_date = st.date_input("Recall Date", datetime.now())
        recall_scope = st.selectbox("Recall Scope", ["Single Lot", "All Lots from Supplier", "Date Range"])
    
    if st.button("🔍 Run Recall Impact Analysis", type="primary"):
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Simulated results
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
                <div style="background: {TELIT_RED}10; border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_RED};">5,000</div>
                    <div style="color: {TELIT_DARK};">Units Affected</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
                <div style="background: {TELIT_ORANGE}10; border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_ORANGE};">2</div>
                    <div style="color: {TELIT_DARK};">Customers Impacted</div>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
                <div style="background: {TELIT_YELLOW}10; border-radius: 12px; padding: 20px; text-align: center;">
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_YELLOW};">$125K</div>
                    <div style="color: {TELIT_DARK};">Estimated Cost</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(render_section_header("Affected Shipments"), unsafe_allow_html=True)
        
        affected_shipments = pd.DataFrame([
            {"Shipment": "SHP-2024-1001", "Customer": "Automotive OEM Alpha", "Quantity": 3000, "Status": "In Field", "Action": "Notify Customer"},
            {"Shipment": "SHP-2024-1002", "Customer": "Fleet Management Inc", "Quantity": 2000, "Status": "In Warehouse", "Action": "Hold & Inspect"},
        ])
        
        st.dataframe(affected_shipments, hide_index=True, use_container_width=True)
        
        st.markdown(render_alert_card(
            "Recommended action: Initiate customer notification for 3,000 units in field and hold 2,000 units in warehouse for inspection.",
            "warning", "📋"
        ), unsafe_allow_html=True)

