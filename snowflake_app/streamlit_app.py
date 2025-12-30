"""
Telit Supply Chain Intelligence Platform
Snowflake-Native Version - All-in-One Dashboard
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# =============================================================================
# CONFIGURATION
# =============================================================================
st.set_page_config(
    page_title="Telit Supply Chain Intelligence",
    page_icon="❄️",
    layout="wide"
)

# Colors
TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_NAVY = "#0D2137"
TELIT_ORANGE = "#FF6B35"
TELIT_GREEN = "#00C48C"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"
TELIT_LIGHT = "#F5F7FA"

# Custom CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    .stApp {{ font-family: 'Inter', sans-serif; }}
    [data-testid="stSidebar"] {{ background: linear-gradient(180deg, #FFFFFF 0%, {TELIT_LIGHT} 100%); }}
    [data-testid="stSidebar"] * {{ color: {TELIT_DARK} !important; }}
    [data-testid="stSidebar"] hr {{ border-color: rgba(0, 167, 225, 0.2) !important; }}
    .hero-section {{
        background: linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_NAVY} 100%);
        padding: 32px; border-radius: 16px; margin-bottom: 24px; color: white;
    }}
    .kpi-card {{
        background: white; border-radius: 12px; padding: 20px;
        text-align: center; box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }}
    .use-case-card {{
        background: white; border-radius: 16px; padding: 24px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08); border: 1px solid #e9ecef; margin-bottom: 16px;
    }}
    .snowflake-benefit {{
        background: linear-gradient(135deg, #29B5E8 0%, #00A3E0 100%);
        border-radius: 12px; padding: 20px; color: white; text-align: center;
    }}
    .data-tag {{
        display: inline-block; background: #e3f2fd; color: #1565c0;
        padding: 4px 10px; border-radius: 12px; font-size: 11px; margin: 2px;
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR NAVIGATION
# =============================================================================
with st.sidebar:
    # Telit Logo - try HTML img tag (may work in some Snowflake configs)
    st.markdown("""
    <div style="text-align: center; padding: 15px 0;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telit_Cinterion_Logo.png/250px-Telit_Cinterion_Logo.png" 
             style="max-width: 180px; height: auto;" 
             onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"
             alt="Telit Cinterion Logo">
        <div style="display: none;">
            <h1 style="margin: 0; font-size: 28px; color: #00A7E1;">telit</h1>
            <p style="margin: 0; font-size: 14px; color: #1E3A5F; opacity: 0.8;">cinterion</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Supply Chain Intelligence")
    
    # Navigation
    page = st.radio(
        "Navigation",
        options=[
            "🏠 Home",
            "📊 Executive Dashboard",
            "🏭 Digital Twin",
            "📦 Inventory & Shipments",
            "📈 Demand Forecast",
            "🤝 Suppliers",
            "✅ Quality",
            "🔗 Traceability",
            "📱 Certifications",
            "🔄 Product Lifecycle",
            "📋 Customer Orders",
            "🔁 Returns & RMA",
            "🏭 CM Portal",
            "💱 Financial & Costing",
            "🌱 Carbon ESG",
            "⚠️ Risk & Maintenance",
            "🏗️ Architecture",
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("""
        <div style="background: linear-gradient(135deg, #29B5E8 0%, #1a8bc4 100%); padding: 12px; border-radius: 8px;">
            <div style="font-size: 20px; text-align: center;">❄️</div>
            <div style="text-align: center; font-size: 12px; color: white; font-weight: 600;">Powered by Snowflake</div>
        </div>
    """, unsafe_allow_html=True)

# =============================================================================
# PAGE: HOME - CIO Executive Overview
# =============================================================================
if page == "🏠 Home":
    # Hero Section
    st.markdown(f"""
        <div class="hero-section">
            <div style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">
                <span style="font-size: 48px;">❄️</span>
                <div>
                    <h1 style="margin: 0; font-size: 2.2rem; font-weight: 700; color: white;">Supply Chain Intelligence Platform</h1>
                    <p style="margin: 8px 0 0 0; opacity: 0.9; font-size: 1.1rem; color: white;">Powered by Snowflake Data Cloud | Built for Telit Cinterion</p>
                </div>
            </div>
            <p style="opacity: 0.95; max-width: 900px; font-size: 1rem; line-height: 1.6; color: white;">
                A comprehensive data platform that unifies <strong>15+ data sources</strong> across the entire supply chain ecosystem. 
                From IoT sensors on the factory floor to global logistics tracking, this platform delivers <strong>real-time visibility</strong>, 
                <strong>AI-powered insights</strong>, and <strong>secure collaboration</strong> with partners.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Executive KPIs - Telit Cinterion specific impact
    st.markdown("### 📊 Executive Summary: Platform Business Impact")
    k1, k2, k3, k4, k5, k6 = st.columns(6)
    k1.metric("Annual Savings", "$4.2M", "projected ROI")
    k2.metric("Data Sources", "12+", "unified")
    k3.metric("IoT Ingestion", "<30 sec", "real-time")
    k4.metric("Inventory Reduction", "10%", "$5M freed")
    k5.metric("Forecast MAPE", "-15%", "ML-powered")
    k6.metric("Module Traceability", "95%", "lot-level")
    
    st.markdown("---")
    
    # =========================================================================
    # CONSOLIDATED USE CASES WITH IMPLEMENTATION PLANS
    # =========================================================================
    st.markdown("### 📋 Supply Chain Use Cases & Implementation Roadmap")
    st.markdown("*Each use case includes business value, data requirements, and implementation timeline*")
    
    # Implementation timeline overview
    st.markdown("#### 🗓️ Implementation Timeline Overview")
    timeline_cols = st.columns(5)
    with timeline_cols[0]:
        st.markdown(f"""
        <div style="background: {TELIT_GREEN}15; border-left: 4px solid {TELIT_GREEN}; padding: 12px; border-radius: 0 8px 8px 0;">
            <strong style="color: {TELIT_GREEN}; font-size: 13px;">Phase 1: Quick Wins</strong><br>
            <span style="font-size: 11px; color: {TELIT_GRAY};">Weeks 1-4</span><br>
            <span style="font-size: 10px;">Executive, Inventory</span>
        </div>
        """, unsafe_allow_html=True)
    with timeline_cols[1]:
        st.markdown(f"""
        <div style="background: {TELIT_BLUE}15; border-left: 4px solid {TELIT_BLUE}; padding: 12px; border-radius: 0 8px 8px 0;">
            <strong style="color: {TELIT_BLUE}; font-size: 13px;">Phase 2: Core</strong><br>
            <span style="font-size: 11px; color: {TELIT_GRAY};">Weeks 5-12</span><br>
            <span style="font-size: 10px;">Twin, Quality, Suppliers</span>
        </div>
        """, unsafe_allow_html=True)
    with timeline_cols[2]:
        st.markdown(f"""
        <div style="background: {TELIT_ORANGE}15; border-left: 4px solid {TELIT_ORANGE}; padding: 12px; border-radius: 0 8px 8px 0;">
            <strong style="color: {TELIT_ORANGE}; font-size: 13px;">Phase 3: Advanced</strong><br>
            <span style="font-size: 11px; color: {TELIT_GRAY};">Weeks 13-20</span><br>
            <span style="font-size: 10px;">Trace, Forecast, Risk</span>
        </div>
        """, unsafe_allow_html=True)
    with timeline_cols[3]:
        st.markdown(f"""
        <div style="background: #9c27b015; border-left: 4px solid #9c27b0; padding: 12px; border-radius: 0 8px 8px 0;">
            <strong style="color: #9c27b0; font-size: 13px;">Phase 4: AI/ML</strong><br>
            <span style="font-size: 11px; color: {TELIT_GRAY};">Weeks 21-28</span><br>
            <span style="font-size: 10px;">Predictive, ESG</span>
        </div>
        """, unsafe_allow_html=True)
    with timeline_cols[4]:
        st.markdown(f"""
        <div style="background: #607d8b15; border-left: 4px solid #607d8b; padding: 12px; border-radius: 0 8px 8px 0;">
            <strong style="color: #607d8b; font-size: 13px;">Phase 5: Extended</strong><br>
            <span style="font-size: 11px; color: {TELIT_GRAY};">Weeks 29-42</span><br>
            <span style="font-size: 10px;">Certs, PLM, CM, Finance</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Visual Use Case Cards
    st.markdown("#### 🎯 Use Cases at a Glance")
    
    # Create 4 rows of 4 cards each for 16 use cases
    row1_cols = st.columns(4)
    row2_cols = st.columns(4)
    row3_cols = st.columns(4)
    row4_cols = st.columns(4)
    
    use_cases_row1 = [
        ("📊", "Executive Dashboard", TELIT_GREEN, "Wk 1-2"),
        ("📦", "Inventory & Shipments", TELIT_GREEN, "Wk 2-4"),
        ("🏭", "Digital Twin", TELIT_BLUE, "Wk 5-8"),
        ("✅", "Quality Control", TELIT_BLUE, "Wk 7-10"),
    ]
    
    use_cases_row2 = [
        ("🤝", "Supplier Performance", TELIT_BLUE, "Wk 10-12"),
        ("📈", "Demand Forecasting", TELIT_ORANGE, "Wk 13-16"),
        ("⚠️", "Risk Intelligence", TELIT_ORANGE, "Wk 14-18"),
        ("🔗", "Traceability", TELIT_ORANGE, "Wk 16-20"),
    ]
    
    use_cases_row3 = [
        ("🔧", "Predictive Maintenance", "#9c27b0", "Wk 21-26"),
        ("🌱", "Carbon & ESG", "#9c27b0", "Wk 24-28"),
        ("📱", "Certifications", "#607d8b", "Wk 29-32"),
        ("🔄", "Product Lifecycle", "#607d8b", "Wk 30-34"),
    ]
    
    use_cases_row4 = [
        ("📋", "Customer Orders", "#607d8b", "Wk 32-35"),
        ("🔁", "Returns & RMA", "#607d8b", "Wk 34-37"),
        ("🏭", "CM Portal", "#607d8b", "Wk 36-40"),
        ("💱", "Financial & Costing", "#607d8b", "Wk 38-42"),
    ]
    
    for idx, (icon, name, color, weeks) in enumerate(use_cases_row1):
        with row1_cols[idx]:
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 15px 10px; text-align: center; 
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-top: 3px solid {color}; min-height: 110px;">
                <div style="font-size: 28px; margin-bottom: 6px;">{icon}</div>
                <div style="font-weight: 600; font-size: 11px; color: {TELIT_DARK}; line-height: 1.3;">{name}</div>
                <div style="margin-top: 6px;">
                    <span style="background: {color}15; color: {color}; font-size: 9px; padding: 2px 6px; border-radius: 8px; font-weight: 500;">{weeks}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    for idx, (icon, name, color, weeks) in enumerate(use_cases_row2):
        with row2_cols[idx]:
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 15px 10px; text-align: center; 
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-top: 3px solid {color}; min-height: 110px;">
                <div style="font-size: 28px; margin-bottom: 6px;">{icon}</div>
                <div style="font-weight: 600; font-size: 11px; color: {TELIT_DARK}; line-height: 1.3;">{name}</div>
                <div style="margin-top: 6px;">
                    <span style="background: {color}15; color: {color}; font-size: 9px; padding: 2px 6px; border-radius: 8px; font-weight: 500;">{weeks}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    for idx, (icon, name, color, weeks) in enumerate(use_cases_row3):
        with row3_cols[idx]:
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 15px 10px; text-align: center; 
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-top: 3px solid {color}; min-height: 110px;">
                <div style="font-size: 28px; margin-bottom: 6px;">{icon}</div>
                <div style="font-weight: 600; font-size: 11px; color: {TELIT_DARK}; line-height: 1.3;">{name}</div>
                <div style="margin-top: 6px;">
                    <span style="background: {color}15; color: {color}; font-size: 9px; padding: 2px 6px; border-radius: 8px; font-weight: 500;">{weeks}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    
    for idx, (icon, name, color, weeks) in enumerate(use_cases_row4):
        with row4_cols[idx]:
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 15px 10px; text-align: center; 
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-top: 3px solid {color}; min-height: 110px;">
                <div style="font-size: 28px; margin-bottom: 6px;">{icon}</div>
                <div style="font-weight: 600; font-size: 11px; color: {TELIT_DARK}; line-height: 1.3;">{name}</div>
                <div style="margin-top: 6px;">
                    <span style="background: {color}15; color: {color}; font-size: 9px; padding: 2px 6px; border-radius: 8px; font-weight: 500;">{weeks}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Tab-based organization by implementation phase
    phase_tab1, phase_tab2, phase_tab3, phase_tab4, phase_tab5 = st.tabs([
        "🟢 Phase 1: Quick Wins", 
        "🔵 Phase 2: Core Ops", 
        "🟠 Phase 3: Advanced", 
        "🟣 Phase 4: AI/ML",
        "⚪ Phase 5: Extended"
    ])
    
    # =================================================================
    # PHASE 1: QUICK WINS
    # =================================================================
    with phase_tab1:
        st.markdown("#### Phase 1: Quick Wins - Foundation & Visibility")
        st.markdown("*Low complexity, high impact dashboards using existing data*")
        
        # Executive Dashboard
        with st.expander("📊 **Executive Dashboard** - C-Suite visibility into supply chain KPIs", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Single source of truth for supply chain performance. Eliminates manual report generation and provides real-time visibility into KPIs that matter: revenue, inventory, on-time delivery, quality.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Real-time KPI tiles (revenue, inventory, OTD, quality, shipments)
                - Trend analysis with drill-down capability
                - Regional performance breakdown
                - Active alerts and exceptions summary
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Report Time", "-75%", "auto vs manual")
                m2.metric("Decision Speed", "+30%", "real-time data")
                m3.metric("Data Accuracy", "98%", "single source")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~2 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 24px; height: 24px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 10px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 8px;"></div>
                            <div style="width: 24px; height: 24px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 10px; font-weight: 700;">2</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 10px; color: #64748b;">
                            <span>SAP extracts + Data models</span>
                            <span>Dashboard + UAT</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 11px; color: #78350f;">✓ SAP access credentials<br>✓ KPI definitions agreed<br>✓ Stakeholder sign-off</div>
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">SAP SD</span>
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">SAP MM</span>
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">SAP PP</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_GREEN};">●</span> Data Cleanup: <strong>Low</strong> - Standard ERP extracts
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Inventory Management
        with st.expander("📦 **Inventory & Shipments** - Global stock visibility and tracking", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Real-time visibility into $78M+ inventory across global warehouses. Identify low stock, excess inventory, and in-transit shipments. Reduce stockouts and optimize working capital.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Multi-warehouse inventory levels by SKU
                - Days of Supply (DOS) calculations
                - Low stock alerts and reorder triggers
                - In-transit shipment tracking
                - Carrier performance analytics
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Stockouts", "-25%", "$800K saved")
                m2.metric("Excess Inventory", "-10%", "$5M freed")
                m3.metric("Visibility", "95%", "key locations")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~3 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">3</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>SAP Integration</span>
                            <span>Carrier APIs</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 11px; color: #78350f;">✓ Warehouse master data<br>✓ SKU-location mapping<br>✓ Carrier API keys (DHL, FedEx)</div>
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">SAP MM/WM</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">Carrier APIs</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">GPS</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_ORANGE};">●</span> Data Cleanup: <strong>Medium</strong> - SKU harmonization needed
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # PHASE 2: CORE
    # =================================================================
    with phase_tab2:
        st.markdown("#### Phase 2: Core Operations - Real-time Manufacturing & Quality")
        st.markdown("*IoT integration and operational dashboards*")
        
        # Digital Twin
        with st.expander("🏭 **Digital Twin / Smart Factory** - Real-time factory floor visualization", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Manufacturing operations lack real-time visibility into equipment performance. Digital Twin provides single pane of glass for factory operations, enabling proactive decision-making and optimized throughput for IoT module production.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Live equipment status (running, idle, fault, maintenance)
                - OEE calculation and trending
                - Production throughput per line, shift, product
                - Energy consumption tracking
                - Real-time anomaly alerts
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("OEE", "+8%", "$320K/year")
                m2.metric("Downtime", "-15%", "$180K/year")
                m3.metric("Energy", "-5%", "$75K/year")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~4 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 8px; font-weight: 700;">1-2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">3</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">4</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>PLC/Snowpipe</span>
                            <span>OEE Calc</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ deviceWISE EDGE installed<br>✓ PLC tag documentation<br>✓ Shop floor network<br>✓ OEE methodology</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">PLC/SCADA</span>
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">MES</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">IoT</span>
                        <span style="background: #6B5B9520; color: #6B5B95; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Energy</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - Tag standardization required
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Quality Control
        with st.expander("✅ **Quality Control & SPC** - Statistical process control", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("IoT modules require IATF 16949 standards for automotive. Real-time SPC enables early detection of process drift BEFORE defects occur, protecting Telit's reputation and reducing Cost of Poor Quality (COPQ).")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Real-time SPC control charts (X-bar, R-chart)
                - Automated control limit violations
                - Defect Pareto by type, line, shift
                - First Pass Yield tracking
                - Customer return correlation
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Defects", "-20%", "$250K/year")
                m2.metric("Scrap", "-15%", "$180K/year")
                m3.metric("Returns", "-25%", "reputation")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~3 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">3</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>AOI Integration</span>
                            <span>SPC Setup</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ AOI system API access<br>✓ Test equipment integration<br>✓ Defect taxonomy defined<br>✓ Control limits documented</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">AOI Systems</span>
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Func Testers</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP QM</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_ORANGE};">●</span> Data Cleanup: <strong>Medium</strong> - Defect code standardization
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Supplier Performance
        with st.expander("🤝 **Supplier Performance** - Scorecards and analytics", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Telit relies on 150+ suppliers including critical semiconductor vendors. Data-driven scorecards enable strategic supplier management, better negotiations, and early warning of at-risk suppliers.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Automated supplier scorecards
                - On-Time Delivery at PO line level
                - Quality metrics (PPM, inspections)
                - Lead time variability analysis
                - Risk scoring
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Procurement", "-3%", "$1.5M/year")
                m2.metric("OTD", "+5%", "fewer delays")
                m3.metric("Risk Events", "-20%", "early warning")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~3 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 22px; height: 22px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">3</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>Ariba + Master</span>
                            <span>Scorecards</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ Supplier master cleaned<br>✓ KPI definitions & weights<br>✓ Historical PO/GR data</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP Ariba</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP MM</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Quality</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - Supplier harmonization required
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # PHASE 3: ADVANCED
    # =================================================================
    with phase_tab3:
        st.markdown("#### Phase 3: Advanced Analytics - Forecasting, Risk & Traceability")
        st.markdown("*ML models and compliance capabilities*")
        
        # Demand Forecasting
        with st.expander("📈 **Demand Forecasting** - AI/ML-powered predictions", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("IoT module demand is volatile due to automotive program timing and technology transitions (4G→5G). ML-powered forecasting improves MAPE by 25-30%, enabling optimal inventory and capacity planning.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - ML predictions (XGBoost, Prophet)
                - External signal integration
                - Design win pipeline integration
                - Forecast accuracy tracking
                - Scenario planning
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("MAPE", "-15%", "accuracy")
                m2.metric("Safety Stock", "-10%", "$1.2M freed")
                m3.metric("Lost Sales", "-20%", "$600K")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~4 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 8px; font-weight: 700;">3-4</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>Data Prep</span>
                            <span>ML Training</span>
                            <span>Deploy</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ 24+ months sales history<br>✓ Product hierarchy clean<br>✓ External sources ID'd<br>✓ Baseline MAPE measured</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP SD</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Salesforce</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">APIs</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - History cleansing required
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Risk Intelligence
        with st.expander("⚠️ **Risk Intelligence** - Global supply chain risk monitoring", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Semiconductor industry faces unprecedented geopolitical risk. Proactive monitoring with alternative sourcing playbooks enables response in days vs months, protecting revenue during crises.")
                
                st.markdown("**Risk Categories:**")
                st.markdown("""
                - **Geopolitical:** Taiwan/China, sanctions
                - **Natural Disasters:** Earthquakes, typhoons
                - **Supplier Financial:** Bankruptcy risk
                - **Cyber Security:** Ransomware threats
                - **Logistics:** Port congestion
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Disruption", "$1M+", "avoided")
                m2.metric("Response", "-40%", "faster")
                m3.metric("Alt Sources", "80%", "qualified")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~4 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 8px; font-weight: 700;">3-4</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>Marketplace</span>
                            <span>Cortex AI</span>
                            <span>Alerts</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ Marketplace access<br>✓ Risk categories defined<br>✓ Supplier-component map<br>✓ Escalation workflows</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">News APIs</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">D&B</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Weather</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_ORANGE};">●</span> Data Cleanup: <strong>Medium</strong> - Supplier hierarchy mapping
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Traceability
        with st.expander("🔗 **Component Traceability** - Full genealogy for compliance", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Automotive customers require full lot traceability within 24 hours. Forward/backward trace in seconds vs days enables rapid recall containment and instant audit readiness.")
                
                st.markdown("**Compliance Standards:**")
                st.markdown("IATF 16949 • FDA 21 CFR • EU MDR • RoHS • Conflict Minerals")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Forward/backward trace in seconds
                - Lot & serial tracking across tiers
                - Recall simulation
                - Audit trail for all movements
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Recall Time", "-60%", "hours vs days")
                m2.metric("Audit Prep", "-40%", "faster")
                m3.metric("Revenue", "$50M", "protected")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~5 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">1-2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">3</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">4-5</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>MES Integration</span>
                            <span>Graph DB</span>
                            <span>UI + Validate</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ MES lot tracking active<br>✓ Barcode/RFID in place<br>✓ Supplier CoC process<br>✓ BOM accuracy >98%</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">MES</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP PP</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">RFID</span>
                        <span style="background: #6B5B9520; color: #6B5B95; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Test</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - BOM & lot genealogy gaps
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # PHASE 4: AI/ML
    # =================================================================
    with phase_tab4:
        st.markdown("#### Phase 4: AI/ML & Sustainability - Advanced Capabilities")
        st.markdown("*Predictive models and ESG compliance*")
        
        # Predictive Maintenance
        with st.expander("🔧 **Predictive Maintenance** - ML-powered equipment health", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Machine learning models predict equipment failures 2-4 weeks ahead using sensor fusion (vibration, temperature, pressure). Automated work orders prevent unplanned downtime.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Sensor data fusion & analysis
                - Remaining Useful Life (RUL) prediction
                - Failure probability scoring
                - Automated work order generation
                - Spare parts optimization
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Unplanned Down", "-30%", "$450K/year")
                m2.metric("Maint. Cost", "-12%", "$150K/year")
                m3.metric("Parts Inventory", "-10%", "$80K freed")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~6 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">1-2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">3-4</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">5-6</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 8px; color: #64748b;">
                            <span>Sensors + Features</span>
                            <span>ML Training</span>
                            <span>CMMS Integration</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ Sensors on critical equip<br>✓ 12+ months sensor data<br>✓ Historical failure log<br>✓ CMMS system access</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Vibration</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Temp</span>
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">CMMS</span>
                        <span style="background: #6B5B9520; color: #6B5B95; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">MES</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - Sensor calibration & labeling
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Carbon ESG
        with st.expander("🌱 **Carbon Footprint & ESG** - Scope 1/2/3 emissions tracking", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("European customers (40% of revenue) require CSRD-compliant ESG data. Automotive OEMs need Scope 3 data from all suppliers. Early ESG leadership becomes competitive differentiator.")
                
                st.markdown("**Compliance Frameworks:**")
                st.markdown("CSRD • SEC Climate Rules • CDP • Science-Based Targets")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Scope 1/2/3 emissions calculation
                - Energy consumption monitoring
                - Supplier ESG scoring
                - Carbon offset tracking
                - CSRD report generation
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Contracts", "$15M", "protected")
                m2.metric("Compliance", "90%", "CSRD progress")
                m3.metric("Energy", "$150K", "savings")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~5 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">2-3</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">4</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">5</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 8px; color: #64748b;">
                            <span>Scope</span>
                            <span>Collection</span>
                            <span>Sharing</span>
                            <span>Reports</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ Energy meter connectivity<br>✓ Emission factors sourced<br>✓ Supplier ESG contacts<br>✓ Baseline year defined</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Energy</span>
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Utilities</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Supplier</span>
                        <span style="background: #6B5B9520; color: #6B5B95; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">LCA</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - Emission factors & scope mapping
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # PHASE 5: EXTENDED CAPABILITIES
    # =================================================================
    with phase_tab5:
        st.markdown("#### Phase 5: Extended Capabilities - Full Supply Chain Coverage")
        st.markdown("*Completing the end-to-end supply chain visibility*")
        
        # Certifications
        with st.expander("📱 **Certifications & Compliance** - Carrier and regulatory approvals", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("IoT modules require carrier certifications (AT&T, Verizon, Vodafone) and regional approvals (FCC, CE, PTCRB). Certification delays = revenue delays. Proactive tracking prevents costly re-certifications and market access issues.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Carrier certification matrix by module/region
                - Expiration tracking and renewal alerts
                - Cost tracking by certification type
                - Compliance audit management
                - Regional regulatory tracking (FCC, CE, TELEC)
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Revenue Protected", "$2M", "prevented delays")
                m2.metric("Renewal Savings", "15%", "early renewal")
                m3.metric("Compliance", "98%", "audit ready")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~4 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 8px; font-weight: 700;">3-4</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>Data Model</span>
                            <span>Integration</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ Certification database access<br>✓ Carrier portal credentials<br>✓ Regulatory calendar</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">PLM</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Carrier APIs</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Docs</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_ORANGE};">●</span> Data Cleanup: <strong>Medium</strong> - Cert data consolidation
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Product Lifecycle
        with st.expander("🔄 **Product Lifecycle Management** - NPI, transitions, and EOL", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Managing 4G→5G transitions, 2G/3G sunsets, and new product introductions. Proactive EOL management prevents customer disruptions and enables strategic planning for technology shifts.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Product portfolio lifecycle status
                - NPI pipeline and milestone tracking
                - Technology transition roadmap
                - EOL announcements and last-time-buy
                - Engineering change order (ECO) management
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Revenue Protected", "$5M", "EOL planning")
                m2.metric("NPI Success", "+15%", "on-time launch")
                m3.metric("LTB Revenue", "$8M", "captured")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~5 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">1-2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">3-4</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">5</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>PLM Integration</span>
                            <span>Roadmap Build</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ PLM system access<br>✓ Product roadmap data<br>✓ EOL policy defined<br>✓ NPI process documented</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">PLM</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Roadmap</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - Product master alignment
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Customer Orders
        with st.expander("📋 **Customer Orders** - Order management and backlog", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Complete visibility into customer orders, backlog, design win pipeline, and VMI/hub inventory. Enables proactive customer management and accurate revenue forecasting.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Open order tracking and status
                - Backlog analysis by customer/product
                - Design win to revenue tracking
                - Customer hub (VMI) inventory
                - Expedite request management
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("OTD", "+3%", "improvement")
                m2.metric("Backlog Visibility", "100%", "real-time")
                m3.metric("Revenue", "$1.5M", "expedite capture")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~4 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 8px; font-weight: 700;">3-4</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>SAP SD</span>
                            <span>CRM Link</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ SAP SD access<br>✓ CRM integration<br>✓ Customer master clean</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP SD</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">CRM</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">VMI</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_ORANGE};">●</span> Data Cleanup: <strong>Medium</strong> - Customer hierarchy
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Returns & RMA
        with st.expander("🔁 **Returns & RMA** - Return tracking and failure analysis", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Track RMA requests, failure analysis, warranty claims, and return trends. Identify quality issues early and reduce warranty costs through proactive management.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - RMA tracking and status
                - Failure analysis results
                - Warranty cost tracking
                - Return rate trending by product
                - Root cause Pareto analysis
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Return Rate", "-0.2%", "reduction")
                m2.metric("Warranty Cost", "-$300K", "savings")
                m3.metric("Resolution", "-3 days", "faster")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~4 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">1</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 4px;"></div>
                            <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 8px; font-weight: 700;">3-4</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>RMA System</span>
                            <span>FA Link</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ RMA system access<br>✓ FA database<br>✓ Warranty policy defined</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP QM</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">RMA</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">FA Lab</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_GREEN};">●</span> Data Cleanup: <strong>Low</strong> - Existing RMA system
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # CM Portal
        with st.expander("🏭 **CM Portal** - Contract manufacturer visibility", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Real-time visibility into contract manufacturer performance, capacity, quality, and inventory. Essential for managing outsourced manufacturing (Foxconn, Flex, Jabil).")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - CM capacity and utilization
                - Quality performance (FPY, DPPM)
                - Production schedule tracking
                - CM inventory visibility (RM, WIP, FG)
                - Quarterly scorecards
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Capacity Util", "+5%", "optimization")
                m2.metric("Quality", "-50 DPPM", "improvement")
                m3.metric("Inventory", "-$800K", "reduction")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~5 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">1-2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">3-4</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">5</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>CM APIs</span>
                            <span>Data Model</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ CM data sharing agreements<br>✓ API access to CM systems<br>✓ Scorecard criteria defined<br>✓ NDA in place</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">CM APIs</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">EDI</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Portal</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_RED};">●</span> Data Cleanup: <strong>High</strong> - CM data standardization
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Financial & Costing
        with st.expander("💱 **Financial & Costing** - Landed cost and currency analysis", expanded=True):
            col1, col2 = st.columns([3, 2])
            with col1:
                st.markdown("**Business Value:**")
                st.success("Deep financial analysis including landed cost breakdown, currency exposure, tariff impact (Section 301), and cost variance. Critical for margin management and strategic sourcing decisions.")
                
                st.markdown("**Functional Scope:**")
                st.markdown("""
                - Landed cost by origin/destination
                - Currency exposure and hedge tracking
                - Tariff analysis and mitigation
                - Standard vs actual cost variance
                - Cost reduction tracking
                """)
                
                st.markdown("**ROI Metrics:**")
                m1, m2, m3 = st.columns(3)
                m1.metric("Cost Savings", "$2M", "identified")
                m2.metric("Tariff Mitigation", "$1.5M", "avoided")
                m3.metric("Margin", "+0.5%", "improvement")
            
            with col2:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                        <span style="font-size: 16px; font-weight: 700; color: #1e293b;">📅 Implementation Plan</span>
                        <span style="background: {TELIT_BLUE}15; color: {TELIT_BLUE}; padding: 6px 14px; border-radius: 8px; font-size: 13px; font-weight: 600;">~5 weeks</span>
                    </div>
                    <div style="background: white; border-radius: 8px; padding: 12px; margin-bottom: 12px;">
                        <div style="font-size: 11px; font-weight: 600; color: #475569; margin-bottom: 8px;">📋 DELIVERY TIMELINE</div>
                        <div style="display: flex; align-items: center; margin-bottom: 6px;">
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">1-2</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 7px; font-weight: 700;">3-4</div>
                            <div style="flex: 1; height: 2px; background: {TELIT_BLUE}; margin: 0 3px;"></div>
                            <div style="width: 18px; height: 18px; background: {TELIT_BLUE}; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-size: 9px; font-weight: 700;">5</div>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-size: 9px; color: #64748b;">
                            <span>SAP FI/CO</span>
                            <span>Analysis</span>
                            <span>Dashboard</span>
                        </div>
                    </div>
                    <div style="background: #fef3c7; border-radius: 8px; padding: 10px; margin-bottom: 12px; border-left: 3px solid #f59e0b;">
                        <div style="font-size: 11px; font-weight: 600; color: #92400e; margin-bottom: 5px;">⚡ PREREQUISITES</div>
                        <div style="font-size: 10px; color: #78350f;">✓ SAP FI/CO access<br>✓ Cost element mapping<br>✓ FX data feeds<br>✓ Tariff schedule</div>
                    </div>
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px;">
                        <span style="background: {TELIT_BLUE}20; color: {TELIT_BLUE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">SAP FI</span>
                        <span style="background: {TELIT_GREEN}20; color: {TELIT_GREEN}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Treasury</span>
                        <span style="background: {TELIT_ORANGE}20; color: {TELIT_ORANGE}; padding: 3px 8px; border-radius: 4px; font-size: 9px; font-weight: 600;">Customs</span>
                    </div>
                    <div style="font-size: 10px; color: #64748b; display: flex; align-items: center; gap: 5px;">
                        <span style="color: {TELIT_ORANGE};">●</span> Data Cleanup: <strong>Medium</strong> - Cost element mapping
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Summary table
    st.markdown("### 📊 Implementation Summary")
    
    # Gantt Chart Data
    gantt_data = [
        {"Use Case": "📊 Executive Dashboard", "Start": 1, "Duration": 2, "Phase": "Phase 1", "Effort": "40 hrs"},
        {"Use Case": "📦 Inventory & Shipments", "Start": 2, "Duration": 3, "Phase": "Phase 1", "Effort": "60 hrs"},
        {"Use Case": "🏭 Digital Twin", "Start": 5, "Duration": 4, "Phase": "Phase 2", "Effort": "120 hrs"},
        {"Use Case": "✅ Quality Control", "Start": 7, "Duration": 3, "Phase": "Phase 2", "Effort": "80 hrs"},
        {"Use Case": "🤝 Supplier Performance", "Start": 10, "Duration": 3, "Phase": "Phase 2", "Effort": "70 hrs"},
        {"Use Case": "📈 Demand Forecasting", "Start": 13, "Duration": 4, "Phase": "Phase 3", "Effort": "100 hrs"},
        {"Use Case": "⚠️ Risk Intelligence", "Start": 14, "Duration": 4, "Phase": "Phase 3", "Effort": "90 hrs"},
        {"Use Case": "🔗 Traceability", "Start": 16, "Duration": 5, "Phase": "Phase 3", "Effort": "120 hrs"},
        {"Use Case": "🔧 Predictive Maintenance", "Start": 21, "Duration": 6, "Phase": "Phase 4", "Effort": "150 hrs"},
        {"Use Case": "🌱 Carbon ESG", "Start": 24, "Duration": 5, "Phase": "Phase 4", "Effort": "110 hrs"},
        {"Use Case": "📱 Certifications", "Start": 29, "Duration": 4, "Phase": "Phase 5", "Effort": "80 hrs"},
        {"Use Case": "🔄 Product Lifecycle", "Start": 30, "Duration": 5, "Phase": "Phase 5", "Effort": "90 hrs"},
        {"Use Case": "📋 Customer Orders", "Start": 32, "Duration": 4, "Phase": "Phase 5", "Effort": "70 hrs"},
        {"Use Case": "🔁 Returns & RMA", "Start": 34, "Duration": 4, "Phase": "Phase 5", "Effort": "60 hrs"},
        {"Use Case": "🏭 CM Portal", "Start": 36, "Duration": 5, "Phase": "Phase 5", "Effort": "100 hrs"},
        {"Use Case": "💱 Financial & Costing", "Start": 38, "Duration": 5, "Phase": "Phase 5", "Effort": "80 hrs"},
    ]
    gantt_df = pd.DataFrame(gantt_data)
    gantt_df["End"] = gantt_df["Start"] + gantt_df["Duration"]
    
    # Phase colors
    phase_colors = {
        "Phase 1": TELIT_GREEN,
        "Phase 2": TELIT_BLUE,
        "Phase 3": TELIT_ORANGE,
        "Phase 4": "#9c27b0",
        "Phase 5": "#607d8b"
    }
    
    # Create Gantt chart using plotly
    fig_gantt = go.Figure()
    
    for idx, row in gantt_df.iterrows():
        fig_gantt.add_trace(go.Bar(
            x=[row["Duration"]],
            y=[row["Use Case"]],
            base=[row["Start"]],
            orientation='h',
            marker=dict(
                color=phase_colors[row["Phase"]],
                line=dict(color='white', width=1)
            ),
            text=f"{row['Duration']} wks • {row['Effort']}",
            textposition='inside',
            textfont=dict(color='white', size=11),
            hovertemplate=f"<b>{row['Use Case']}</b><br>" +
                          f"Start: Week {row['Start']}<br>" +
                          f"Duration: {row['Duration']} weeks<br>" +
                          f"Effort: {row['Effort']}<br>" +
                          f"{row['Phase']}<extra></extra>",
            showlegend=False
        ))
    
    # Add phase markers
    for phase, (start, end, color) in {
        "Phase 1": (1, 4, TELIT_GREEN),
        "Phase 2": (5, 12, TELIT_BLUE),
        "Phase 3": (13, 20, TELIT_ORANGE),
        "Phase 4": (21, 28, "#9c27b0")
    }.items():
        fig_gantt.add_shape(
            type="rect",
            x0=start, x1=end+1,
            y0=-0.5, y1=len(gantt_df)-0.5,
            fillcolor=color,
            opacity=0.08,
            layer="below",
            line_width=0,
        )
    
    fig_gantt.update_layout(
        title=dict(
            text="<b>📅 Implementation Gantt Chart</b>",
            font=dict(size=16, color=TELIT_DARK)
        ),
        xaxis=dict(
            title="Week",
            tickmode='array',
            tickvals=list(range(0, 30, 4)),
            ticktext=[f"Wk {i}" for i in range(0, 30, 4)],
            gridcolor='#e0e0e0',
            range=[0, 30]
        ),
        yaxis=dict(
            title="",
            autorange="reversed",
            categoryorder='array',
            categoryarray=[row["Use Case"] for row in gantt_data]
        ),
        height=450,
        margin=dict(l=20, r=20, t=50, b=40),
        plot_bgcolor='white',
        paper_bgcolor='white',
        bargap=0.3,
        # Add phase legend annotations
        annotations=[
            dict(x=2.5, y=-0.8, text="<b>P1</b>", showarrow=False, font=dict(color=TELIT_GREEN, size=9), xref="x", yref="y"),
            dict(x=8.5, y=-0.8, text="<b>P2</b>", showarrow=False, font=dict(color=TELIT_BLUE, size=9), xref="x", yref="y"),
            dict(x=16.5, y=-0.8, text="<b>P3</b>", showarrow=False, font=dict(color=TELIT_ORANGE, size=9), xref="x", yref="y"),
            dict(x=24.5, y=-0.8, text="<b>P4</b>", showarrow=False, font=dict(color="#9c27b0", size=9), xref="x", yref="y"),
            dict(x=36, y=-0.8, text="<b>P5</b>", showarrow=False, font=dict(color="#607d8b", size=9), xref="x", yref="y"),
        ]
    )
    
    st.plotly_chart(fig_gantt, use_container_width=True)
    
    # Summary table below the Gantt
    st.markdown("#### 📋 Detailed Summary")
    summary_data = pd.DataFrame({
        "Use Case": ["Executive Dashboard", "Inventory & Shipments", "Digital Twin", "Quality Control", "Supplier Performance", "Demand Forecasting", "Risk Intelligence", "Traceability", "Predictive Maintenance", "Carbon ESG", "Certifications", "Product Lifecycle", "Customer Orders", "Returns & RMA", "CM Portal", "Financial & Costing"],
        "Phase": ["1", "1", "2", "2", "2", "3", "3", "3", "4", "4", "5", "5", "5", "5", "5", "5"],
        "Timeline": ["2 weeks", "3 weeks", "4 weeks", "3 weeks", "3 weeks", "4 weeks", "4 weeks", "5 weeks", "6 weeks", "5 weeks", "4 weeks", "5 weeks", "4 weeks", "4 weeks", "5 weeks", "5 weeks"],
        "Effort (hrs)": [40, 60, 120, 80, 70, 100, 90, 120, 150, 110, 80, 90, 70, 60, 100, 80],
        "Data Cleanup": ["Low", "Medium", "High", "Medium", "High", "High", "Medium", "High", "High", "High", "Medium", "High", "Medium", "Low", "High", "Medium"],
        "ROI": ["$500K", "$5.8M", "$575K", "$430K", "$1.5M", "$1.8M", "$1M+", "$50M*", "$680K", "$15M*", "$2M*", "$5M*", "$1.5M", "$300K", "$800K", "$2M"]
    })
    st.dataframe(summary_data, use_container_width=True)
    st.caption("*Revenue/contracts protected, not direct savings")
    
    st.markdown("---")
    
    # =========================================================================
    # INTERACTIVE ROI CALCULATOR
    # =========================================================================
    st.markdown("### 💰 Interactive ROI Calculator")
    st.markdown("*Adjust the sliders to estimate your potential return on investment*")
    
    roi_col1, roi_col2 = st.columns([1, 1])
    
    with roi_col1:
        st.markdown("**📊 Your Business Parameters:**")
        annual_revenue = st.slider("Annual Revenue ($M)", 100, 1000, 500, 50, key="roi_revenue")
        inventory_value = st.slider("Inventory Value ($M)", 20, 200, 78, 5, key="roi_inventory")
        supplier_spend = st.slider("Annual Supplier Spend ($M)", 50, 500, 250, 25, key="roi_spend")
        downtime_cost_hr = st.slider("Downtime Cost ($/hour)", 5000, 50000, 15000, 1000, key="roi_downtime")
        quality_cost_pct = st.slider("Quality Cost (% of Revenue)", 1.0, 5.0, 2.5, 0.5, key="roi_quality")
    
    with roi_col2:
        # Calculate ROI based on inputs
        inventory_savings = inventory_value * 0.15  # 15% reduction
        procurement_savings = supplier_spend * 0.08  # 8% savings
        downtime_savings = (downtime_cost_hr * 8 * 250 * 0.35) / 1000000  # 35% reduction
        quality_savings = (annual_revenue * quality_cost_pct / 100) * 0.40  # 40% reduction
        forecast_savings = inventory_value * 0.05  # Better forecasting
        
        total_savings = inventory_savings + procurement_savings + downtime_savings + quality_savings + forecast_savings
        implementation_cost = 0.5  # $500K
        roi_pct = ((total_savings - implementation_cost) / implementation_cost) * 100
        payback_months = (implementation_cost / total_savings) * 12
        
        st.markdown("**📈 Estimated Annual Savings:**")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_BLUE}15); border-radius: 12px; padding: 20px; margin-bottom: 15px;">
            <div style="text-align: center;">
                <div style="font-size: 42px; font-weight: bold; color: {TELIT_GREEN};">${total_savings:.1f}M</div>
                <div style="font-size: 14px; color: {TELIT_GRAY};">Total Annual Savings</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        roi_m1, roi_m2 = st.columns(2)
        roi_m1.metric("ROI", f"{roi_pct:.0f}%", "Year 1")
        roi_m2.metric("Payback", f"{payback_months:.1f} mo", "Break-even")
        
        # Savings breakdown
        st.markdown("**Savings Breakdown:**")
        savings_df = pd.DataFrame({
            'Category': ['Inventory Optimization', 'Procurement', 'Downtime Reduction', 'Quality Improvement', 'Forecast Accuracy'],
            'Savings ($M)': [inventory_savings, procurement_savings, downtime_savings, quality_savings, forecast_savings]
        })
        fig_savings = px.bar(savings_df, x='Savings ($M)', y='Category', orientation='h',
                            color='Savings ($M)', color_continuous_scale=[[0, TELIT_BLUE], [1, TELIT_GREEN]])
        fig_savings.update_layout(height=200, margin=dict(l=0, r=0, t=0, b=0), showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig_savings, use_container_width=True)
    
    st.markdown("---")
    
    # =========================================================================
    # DATA READINESS ASSESSMENT
    # =========================================================================
    st.markdown("### ✅ Data Readiness Assessment")
    st.markdown("*Check your organization's readiness for each use case*")
    
    readiness_data = {
        "Executive Dashboard": {"SAP Access": True, "KPI Definitions": True, "Stakeholder Buy-in": True},
        "Inventory & Shipments": {"SAP MM/WM": True, "Carrier APIs": False, "SKU Master": True},
        "Digital Twin": {"PLC Connectivity": False, "deviceWISE Edge": False, "OEE Methodology": True},
        "Quality Control": {"AOI Integration": True, "Defect Taxonomy": True, "Control Limits": False},
        "Supplier Performance": {"Ariba Access": True, "Supplier Master": False, "KPI Weights": True},
        "Demand Forecasting": {"24mo History": True, "Product Hierarchy": False, "External Signals": False},
        "Risk Intelligence": {"News APIs": False, "Supplier Mapping": True, "Risk Categories": True},
        "Traceability": {"MES Integration": False, "Lot Tracking": True, "BOM Accuracy": False},
        "Predictive Maintenance": {"Sensor Data": False, "Failure History": False, "CMMS Access": True},
        "Carbon & ESG": {"Energy Meters": False, "Emission Factors": False, "Supplier ESG": False},
        "Certifications": {"Cert Database": True, "Carrier APIs": False, "Reg Calendar": True},
        "Product Lifecycle": {"PLM Access": True, "Roadmap Data": True, "EOL Policy": True},
        "Customer Orders": {"SAP SD": True, "CRM Integration": False, "VMI Data": True},
        "Returns & RMA": {"RMA System": True, "FA Database": True, "Warranty Data": True},
        "CM Portal": {"CM APIs": False, "EDI Links": True, "Scorecard Data": True},
        "Financial & Costing": {"SAP FI/CO": True, "FX Feeds": False, "Tariff Data": True},
    }
    
    ready_col1, ready_col2 = st.columns([2, 1])
    
    with ready_col1:
        # Create readiness matrix
        readiness_rows = []
        for use_case, prereqs in readiness_data.items():
            ready_count = sum(prereqs.values())
            total = len(prereqs)
            pct = (ready_count / total) * 100
            status = "🟢" if pct >= 80 else "🟡" if pct >= 50 else "🔴"
            readiness_rows.append({
                "Use Case": use_case,
                "Ready": f"{ready_count}/{total}",
                "Score": f"{pct:.0f}%",
                "Status": status
            })
        
        readiness_df = pd.DataFrame(readiness_rows)
        st.dataframe(readiness_df, use_container_width=True, height=300)
    
    with ready_col2:
        # Overall readiness score
        total_ready = sum(sum(p.values()) for p in readiness_data.values())
        total_prereqs = sum(len(p) for p in readiness_data.values())
        overall_pct = (total_ready / total_prereqs) * 100
        
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 25px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
            <div style="font-size: 14px; color: {TELIT_GRAY}; margin-bottom: 10px;">Overall Readiness</div>
            <div style="font-size: 48px; font-weight: bold; color: {TELIT_ORANGE};">{overall_pct:.0f}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 5px;">{total_ready} of {total_prereqs} prerequisites met</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        # Legend
        st.markdown("""
        **Status Legend:**
        - 🟢 Ready (≥80%)
        - 🟡 Partial (50-79%)
        - 🔴 Needs Work (<50%)
        """)
        
        st.info("💡 **Tip:** Focus on Phase 1 use cases first - they have the highest readiness and quickest ROI!")
    
    st.markdown("---")
    
    # =========================================================================
    # SNOWFLAKE FEATURE SHOWCASE
    # =========================================================================
    st.markdown("### ⚡ Snowflake Features Powering Each Use Case")
    st.markdown("*The platform capabilities that make these use cases possible*")
    
    sf_features = [
        {"feature": "Snowpipe Streaming", "icon": "🌊", "use_cases": "Digital Twin, Quality", "desc": "Sub-minute IoT data ingestion"},
        {"feature": "Dynamic Tables", "icon": "🔄", "use_cases": "All Dashboards", "desc": "Auto-refreshing data pipelines"},
        {"feature": "Snowpark ML", "icon": "🤖", "use_cases": "Forecasting, Maintenance", "desc": "Python ML in Snowflake"},
        {"feature": "Cortex AI", "icon": "🧠", "use_cases": "Risk, Forecasting", "desc": "Built-in LLMs and ML functions"},
        {"feature": "Data Sharing", "icon": "🔗", "use_cases": "Suppliers, ESG", "desc": "Secure cross-org data access"},
        {"feature": "Time Travel", "icon": "⏰", "use_cases": "Traceability, Audit", "desc": "Query historical data states"},
        {"feature": "Marketplace", "icon": "🛒", "use_cases": "Risk, ESG", "desc": "Third-party data enrichment"},
        {"feature": "Streamlit", "icon": "📊", "use_cases": "All Dashboards", "desc": "Native app development"},
    ]
    
    sf_cols = st.columns(4)
    for idx, feat in enumerate(sf_features):
        with sf_cols[idx % 4]:
            st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 15px; margin-bottom: 10px; 
                        box-shadow: 0 2px 6px rgba(0,0,0,0.06); border-left: 3px solid {TELIT_BLUE}; min-height: 120px;">
                <div style="font-size: 24px; margin-bottom: 5px;">{feat['icon']}</div>
                <div style="font-weight: 600; font-size: 12px; color: {TELIT_DARK};">{feat['feature']}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY}; margin: 5px 0;">{feat['desc']}</div>
                <div style="font-size: 9px; color: {TELIT_BLUE};">→ {feat['use_cases']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # =========================================================================
    # DATA FLOW VISUALIZATION
    # =========================================================================
    st.markdown("### 🔄 Live Data Flow")
    st.markdown("*How data moves from sources to insights*")
    
    # Create a Sankey diagram for data flow
    flow_labels = [
        "SAP ERP", "IoT/PLC", "Carrier APIs", "External Data",  # Sources (0-3)
        "Snowflake", # Hub (4)
        "Executive", "Operations", "Planning", "Compliance"  # Outputs (5-8)
    ]
    
    flow_source = [0, 0, 1, 1, 2, 3, 3, 4, 4, 4, 4]
    flow_target = [4, 4, 4, 4, 4, 4, 4, 5, 6, 7, 8]
    flow_value = [30, 20, 25, 15, 20, 15, 10, 25, 35, 25, 15]
    
    fig_flow = go.Figure(go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="white", width=0.5),
            label=flow_labels,
            color=[TELIT_ORANGE, TELIT_GREEN, TELIT_BLUE, "#9c27b0", 
                   TELIT_DARK,
                   TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, "#9c27b0"]
        ),
        link=dict(
            source=flow_source,
            target=flow_target,
            value=flow_value,
            color="rgba(200,200,200,0.4)"
        )
    ))
    fig_flow.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=10, b=10),
        font=dict(size=11)
    )
    st.plotly_chart(fig_flow, use_container_width=True)
    
    # Flow description
    flow_cols = st.columns(4)
    with flow_cols[0]:
        st.markdown(f"**📥 Data Sources**")
        st.caption("SAP • IoT • APIs • Files")
    with flow_cols[1]:
        st.markdown(f"**⚡ Ingestion**")
        st.caption("Snowpipe • Connectors • Streaming")
    with flow_cols[2]:
        st.markdown(f"**❄️ Processing**")
        st.caption("Transform • Model • Enrich")
    with flow_cols[3]:
        st.markdown(f"**📊 Insights**")
        st.caption("Dashboards • Alerts • Reports")
    
    st.markdown("---")
    
    # =========================================================================
    # EXPECTED BENEFITS SUMMARY
    # =========================================================================
    st.markdown("### 📈 Expected Benefits Summary")
    st.markdown("*Aggregated impact across all use cases*")
    
    benefit_col1, benefit_col2, benefit_col3 = st.columns(3)
    
    with benefit_col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}20, {TELIT_GREEN}05); border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 14px; color: {TELIT_GRAY}; margin-bottom: 8px;">💵 Total Annual Savings</div>
            <div style="font-size: 36px; font-weight: bold; color: {TELIT_GREEN};">$8.5M+</div>
            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 5px;">Across all use cases</div>
        </div>
        """, unsafe_allow_html=True)
    
    with benefit_col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}20, {TELIT_BLUE}05); border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 14px; color: {TELIT_GRAY}; margin-bottom: 8px;">🛡️ Revenue Protected</div>
            <div style="font-size: 36px; font-weight: bold; color: {TELIT_BLUE};">$225M</div>
            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 5px;">Certifications + Contracts</div>
        </div>
        """, unsafe_allow_html=True)
    
    with benefit_col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_ORANGE}20, {TELIT_ORANGE}05); border-radius: 12px; padding: 20px; text-align: center;">
            <div style="font-size: 14px; color: {TELIT_GRAY}; margin-bottom: 8px;">⚡ Efficiency Gains</div>
            <div style="font-size: 36px; font-weight: bold; color: {TELIT_ORANGE};">40%+</div>
            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 5px;">Average improvement</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # Before/After comparison
    st.markdown("**📊 Before vs After Implementation:**")
    
    comparison_data = pd.DataFrame({
        'Metric': ['Report Generation', 'Inventory Visibility', 'Quality Detection', 'Risk Response', 'Forecast Accuracy', 'Traceability Time'],
        'Before': ['4 hours', '24 hours lag', 'End of line', 'Weeks', '65% MAPE', '2-3 days'],
        'After': ['Real-time', 'Real-time', 'In-process', 'Hours', '85% MAPE', 'Seconds'],
        'Improvement': ['99%', '100%', '40%', '95%', '31%', '99%']
    })
    st.dataframe(comparison_data, use_container_width=True)
    
    st.markdown("---")
    
    # High-Level Architecture Diagram using columns
    st.markdown("### 🏗️ Platform Architecture")
    
    # Architecture flow using columns
    a1, arrow1, a2, arrow2, a3, arrow3, a4, arrow4, a5 = st.columns([2, 0.3, 1.5, 0.3, 2.5, 0.3, 1.5, 0.3, 1.5])
    
    with a1:
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
            <h4 style="color: {TELIT_DARK}; margin: 0 0 12px 0; font-size: 13px;">📥 DATA SOURCES</h4>
            <div style="background: {TELIT_ORANGE}15; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {TELIT_ORANGE};">
                <strong style="font-size: 11px;">ERP Systems</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">SAP, Oracle, NetSuite</span>
            </div>
            <div style="background: {TELIT_GREEN}15; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {TELIT_GREEN};">
                <strong style="font-size: 11px;">deviceWISE® EDGE</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">PLC, SCADA, MQTT</span>
            </div>
            <div style="background: {TELIT_BLUE}15; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {TELIT_BLUE};">
                <strong style="font-size: 11px;">Logistics APIs</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">DHL, FedEx, GPS</span>
            </div>
            <div style="background: #f3e5f5; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid #9c27b0;">
                <strong style="font-size: 11px;">External Data</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">Weather, Markets</span>
            </div>
            <div style="background: #f5f5f5; padding: 8px; border-radius: 6px; border-left: 3px solid {TELIT_GRAY};">
                <strong style="font-size: 11px;">Files</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">S3, Azure, SFTP</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with arrow1:
        st.markdown("<div style='text-align: center; padding-top: 100px; font-size: 24px;'>→</div>", unsafe_allow_html=True)
    
    with a2:
        st.markdown(f"""
        <div style="background: #e3f2fd; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border: 2px solid #29B5E8;">
            <h4 style="color: {TELIT_DARK}; margin: 0 0 12px 0; font-size: 13px;">⚡ INGESTION</h4>
            <div style="background: white; padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">Fivetran</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">ERP Connectors</span>
            </div>
            <div style="background: white; padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">Snowpipe</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">Streaming &lt;1 min</span>
            </div>
            <div style="background: white; padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">External Tables</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">API Ingestion</span>
            </div>
            <div style="background: white; padding: 8px; border-radius: 6px;">
                <strong style="font-size: 11px;">Kafka Connect</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">Event Streaming</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with arrow2:
        st.markdown("<div style='text-align: center; padding-top: 100px; font-size: 24px;'>→</div>", unsafe_allow_html=True)
    
    with a3:
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 16px; box-shadow: 0 4px 16px rgba(41,181,232,0.2); border: 3px solid #29B5E8;">
            <h4 style="color: #29B5E8; margin: 0 0 12px 0; font-size: 14px; text-align: center;">❄️ SNOWFLAKE</h4>
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <div style="flex: 1; background: #e3f2fd; padding: 8px; border-radius: 6px; text-align: center;">
                    <strong style="font-size: 10px;">Bronze</strong><br>
                    <span style="font-size: 9px; color: {TELIT_GRAY};">Raw Data</span>
                </div>
                <div style="flex: 1; background: #e8f5e9; padding: 8px; border-radius: 6px; text-align: center;">
                    <strong style="font-size: 10px;">Silver</strong><br>
                    <span style="font-size: 9px; color: {TELIT_GRAY};">Curated</span>
                </div>
                <div style="flex: 1; background: #fff3e0; padding: 8px; border-radius: 6px; text-align: center;">
                    <strong style="font-size: 10px;">Gold</strong><br>
                    <span style="font-size: 9px; color: {TELIT_GRAY};">Analytics</span>
                </div>
            </div>
            <div style="display: flex; gap: 8px; margin-bottom: 8px;">
                <div style="flex: 1; background: #f3e5f5; padding: 8px; border-radius: 6px; text-align: center;">
                    <strong style="font-size: 10px;">🤖 Snowpark ML</strong>
                </div>
                <div style="flex: 1; background: #fce4ec; padding: 8px; border-radius: 6px; text-align: center;">
                    <strong style="font-size: 10px;">🧠 Cortex AI</strong>
                </div>
            </div>
            <div style="background: #e0f7fa; padding: 8px; border-radius: 6px; text-align: center;">
                <strong style="font-size: 10px;">🔒 Governance</strong><br>
                <span style="font-size: 9px; color: {TELIT_GRAY};">RBAC • Masking • Audit</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with arrow3:
        st.markdown("<div style='text-align: center; padding-top: 100px; font-size: 24px;'>→</div>", unsafe_allow_html=True)
    
    with a4:
        st.markdown(f"""
        <div style="background: white; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
            <h4 style="color: {TELIT_DARK}; margin: 0 0 12px 0; font-size: 13px;">📤 CONSUMPTION</h4>
            <div style="background: {TELIT_BLUE}15; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {TELIT_BLUE};">
                <strong style="font-size: 11px;">Streamlit</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">This Platform</span>
            </div>
            <div style="background: {TELIT_GREEN}15; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {TELIT_GREEN};">
                <strong style="font-size: 11px;">BI Tools</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">Power BI, Tableau</span>
            </div>
            <div style="background: {TELIT_ORANGE}15; padding: 8px; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {TELIT_ORANGE};">
                <strong style="font-size: 11px;">Data Sharing</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">Suppliers</span>
            </div>
            <div style="background: #f3e5f5; padding: 8px; border-radius: 6px; border-left: 3px solid #9c27b0;">
                <strong style="font-size: 11px;">APIs</strong><br>
                <span style="font-size: 10px; color: {TELIT_GRAY};">REST, SDK</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with arrow4:
        st.markdown("<div style='text-align: center; padding-top: 100px; font-size: 24px;'>→</div>", unsafe_allow_html=True)
    
    with a5:
        st.markdown(f"""
        <div style="background: {TELIT_DARK}; border-radius: 12px; padding: 16px; color: white;">
            <h4 style="color: white; margin: 0 0 12px 0; font-size: 13px;">👥 USERS</h4>
            <div style="background: rgba(255,255,255,0.15); padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">👔 Executives</strong>
            </div>
            <div style="background: rgba(255,255,255,0.12); padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">📊 Analysts</strong>
            </div>
            <div style="background: rgba(255,255,255,0.09); padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">🏭 Operations</strong>
            </div>
            <div style="background: rgba(255,255,255,0.06); padding: 8px; border-radius: 6px; margin-bottom: 6px;">
                <strong style="font-size: 11px;">🤝 Suppliers</strong>
            </div>
            <div style="background: rgba(255,255,255,0.03); padding: 8px; border-radius: 6px;">
                <strong style="font-size: 11px;">🤖 ML Systems</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("👈 **Select any dashboard** from the sidebar to explore each use case with live data!")

# =============================================================================
# PAGE: EXECUTIVE DASHBOARD
# =============================================================================
elif page == "📊 Executive Dashboard":
    st.markdown(f"""<div class="hero-section">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                <h1 style="margin: 0; font-size: 2rem; color: white;">📊 Executive Dashboard</h1>
                <p style="opacity: 0.9; margin: 8px 0 0 0; color: white;">Telit Cinterion - Global IoT Module Supply Chain Operations</p>
            </div>
            <div style="text-align: right; color: white;">
                <p style="margin: 0; font-size: 12px; opacity: 0.7;">Last Updated</p>
                <p style="margin: 0; font-size: 18px; font-weight: 600;">{datetime.now().strftime("%B %d, %Y %H:%M")}</p>
            </div>
        </div>
    </div>""", unsafe_allow_html=True)
    
    # ==========================================================================
    # EXECUTIVE DASHBOARD TABS
    # ==========================================================================
    exec_tab1, exec_tab2, exec_tab3, exec_tab4, exec_tab5 = st.tabs([
        "📈 Overview", "💰 Financial", "🏭 Operations", "🎯 Customers & Market", "⚠️ Alerts & AI"
    ])
    
    # ==========================================================================
    # TAB 1: OVERVIEW - Executive Summary at a Glance
    # ==========================================================================
    with exec_tab1:
        # Quick Stats Row
        st.markdown("#### 🎯 Key Performance Indicators - Q4 2024")
        kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
        kpi1.metric("Revenue YTD", "$509M", "+6.0%")
        kpi2.metric("Gross Margin", "38.5%", "+1.2 pts")
        kpi3.metric("On-Time Delivery", "95.8%", "+2.1%")
        kpi4.metric("Quality FPY", "98.7%", "+0.3%")
        kpi5.metric("Inventory Days", "45", "-8 days")
        kpi6.metric("Design Wins", "47", "+12 YTD")
        
        st.markdown("---")
        
        # Scorecards
        st.markdown("#### 🏆 Executive Scorecard")
        score_col1, score_col2, score_col3, score_col4 = st.columns(4)
        
        with score_col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}20, {TELIT_GREEN}05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid {TELIT_GREEN}30;">
                <div style="font-size: 12px; color: {TELIT_GRAY}; text-transform: uppercase;">Financial Health</div>
                <div style="font-size: 42px; font-weight: bold; color: {TELIT_GREEN}; margin: 10px 0;">A</div>
                <div style="font-size: 11px; color: {TELIT_GREEN};">↑ Revenue growth on track</div>
            </div>
            """, unsafe_allow_html=True)
        
        with score_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}20, {TELIT_GREEN}05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid {TELIT_GREEN}30;">
                <div style="font-size: 12px; color: {TELIT_GRAY}; text-transform: uppercase;">Supply Chain</div>
                <div style="font-size: 42px; font-weight: bold; color: {TELIT_GREEN}; margin: 10px 0;">A-</div>
                <div style="font-size: 11px; color: {TELIT_GREEN};">↑ OTD improving</div>
            </div>
            """, unsafe_allow_html=True)
        
        with score_col3:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_ORANGE}20, {TELIT_ORANGE}05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid {TELIT_ORANGE}30;">
                <div style="font-size: 12px; color: {TELIT_GRAY}; text-transform: uppercase;">Risk Exposure</div>
                <div style="font-size: 42px; font-weight: bold; color: {TELIT_ORANGE}; margin: 10px 0;">B+</div>
                <div style="font-size: 11px; color: {TELIT_ORANGE};">→ Taiwan exposure monitored</div>
            </div>
            """, unsafe_allow_html=True)
        
        with score_col4:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}20, {TELIT_BLUE}05); border-radius: 12px; padding: 20px; text-align: center; border: 1px solid {TELIT_BLUE}30;">
                <div style="font-size: 12px; color: {TELIT_GRAY}; text-transform: uppercase;">Customer Sat</div>
                <div style="font-size: 42px; font-weight: bold; color: {TELIT_BLUE}; margin: 10px 0;">A</div>
                <div style="font-size: 11px; color: {TELIT_BLUE};">↑ NPS +8 pts YTD</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Quick charts row
        overview_c1, overview_c2 = st.columns(2)
        
        with overview_c1:
            st.markdown("**📊 Revenue vs Target (Quarterly)**")
            quarters = ['Q1', 'Q2', 'Q3', 'Q4']
            fig_rev = go.Figure()
            fig_rev.add_trace(go.Bar(x=quarters, y=[118, 132, 128, 131], name='Actual', marker_color=TELIT_BLUE))
            fig_rev.add_trace(go.Scatter(x=quarters, y=[115, 125, 130, 135], mode='lines+markers', name='Target', line=dict(color=TELIT_ORANGE, dash='dash')))
            fig_rev.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0), legend=dict(orientation="h", y=1.1), yaxis_title="$M")
            st.plotly_chart(fig_rev, use_container_width=True)
        
        with overview_c2:
            st.markdown("**🌍 Revenue by Region**")
            fig_region = px.pie(
                pd.DataFrame({'Region': ['EMEA', 'Americas', 'APAC'], 'Revenue': [204, 178, 127]}),
                values='Revenue', names='Region', hole=0.5,
                color_discrete_sequence=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE]
            )
            fig_region.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0), annotations=[dict(text='$509M', x=0.5, y=0.5, font_size=16, showarrow=False)])
            st.plotly_chart(fig_region, use_container_width=True)
        
        # Top issues
        st.markdown("#### 🚨 Top 3 Executive Issues Requiring Attention")
        issue_col1, issue_col2, issue_col3 = st.columns(3)
        
        with issue_col1:
            st.error("""
            **🔴 5G Chipset Allocation**
            
            Qualcomm SDX62 constrained through Q2. Affects $18M in Q1 orders.
            
            **Action:** Qualify MediaTek T750 (45 days)
            """)
        
        with issue_col2:
            st.warning("""
            **🟡 Taiwan Geopolitical Risk**
            
            TSMC + MediaTek = 28% of component spend. Monitoring required.
            
            **Action:** Build 90-day buffer stock
            """)
        
        with issue_col3:
            st.info("""
            **🔵 ESG Compliance Deadline**
            
            CSRD reporting required by Q2 2025. Scope 3 data gaps remain.
            
            **Action:** Supplier ESG data collection
            """)
    
    # ==========================================================================
    # TAB 2: FINANCIAL - Deep Dive on Financials
    # ==========================================================================
    with exec_tab2:
        st.markdown("#### 💰 Financial Performance - FY 2024")
        
        # Key financial metrics
        f1, f2, f3, f4, f5 = st.columns(5)
        f1.metric("Revenue YTD", "$509M", "+6.0% vs LY")
        f2.metric("Gross Margin", "38.5%", "+1.2 pts")
        f3.metric("Operating Income", "$48.3M", "+9.5%")
        f4.metric("COGS", "$313M", "-2.1%", delta_color="inverse")
        f5.metric("R&D Spend", "$52M", "10.2% of Rev")
        
        st.markdown("---")
        
        fin_col1, fin_col2 = st.columns(2)
        
        with fin_col1:
            st.markdown("**📈 Revenue Trend (12 Months)**")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            rev_monthly = [38, 42, 38, 44, 46, 42, 41, 43, 44, 45, 42, 44]
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(x=months, y=rev_monthly, fill='tozeroy', fillcolor='rgba(41, 181, 232, 0.3)', line=dict(color=TELIT_BLUE)))
            fig_trend.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0), yaxis_title="$M")
            st.plotly_chart(fig_trend, use_container_width=True)
            
            st.markdown("**💵 Cost Structure**")
            cost_data = pd.DataFrame({
                'Category': ['Materials', 'Labor', 'Overhead', 'Logistics', 'R&D', 'SG&A'],
                'Amount': [235, 45, 33, 28, 52, 68]
            })
            fig_cost = px.bar(cost_data, x='Amount', y='Category', orientation='h', color='Amount',
                             color_continuous_scale=[[0, TELIT_GREEN], [1, TELIT_ORANGE]])
            fig_cost.update_layout(height=220, margin=dict(l=0, r=0, t=10, b=0), showlegend=False, coloraxis_showscale=False)
            st.plotly_chart(fig_cost, use_container_width=True)
        
        with fin_col2:
            st.markdown("**📊 Revenue by Segment**")
            fig_seg = px.pie(pd.DataFrame({
                'Segment': ['IoT Modules', 'Connectivity Services', 'Software & Services'],
                'Revenue': [382, 89, 38]
            }), values='Revenue', names='Segment', hole=0.6,
               color_discrete_sequence=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE])
            fig_seg.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0),
                                  annotations=[dict(text='$509M', x=0.5, y=0.5, font_size=16, showarrow=False)])
            st.plotly_chart(fig_seg, use_container_width=True)
            
            st.markdown("**📉 Margin Analysis by Product Line**")
            margin_data = pd.DataFrame({
                'Product': ['5G Modules', 'LTE Cat 4', 'LTE-M/NB-IoT', 'GNSS', 'Legacy 3G'],
                'Margin %': [42, 38, 45, 35, 28]
            })
            fig_margin = px.bar(margin_data, x='Product', y='Margin %', color='Margin %',
                               color_continuous_scale=[[0, TELIT_RED], [0.5, TELIT_ORANGE], [1, TELIT_GREEN]])
            fig_margin.update_layout(height=220, margin=dict(l=0, r=0, t=10, b=0), showlegend=False, coloraxis_showscale=False)
            st.plotly_chart(fig_margin, use_container_width=True)
        
        st.markdown("---")
        
        # Working Capital
        st.markdown("#### 💳 Working Capital & Cash Flow")
        wc1, wc2, wc3, wc4 = st.columns(4)
        wc1.metric("Cash & Equivalents", "$87M", "+$12M QoQ")
        wc2.metric("Accounts Receivable", "$68M", "DSO: 48 days")
        wc3.metric("Inventory Value", "$78.5M", "45 days supply")
        wc4.metric("Accounts Payable", "$52M", "DPO: 38 days")
    
    # ==========================================================================
    # TAB 3: OPERATIONS - Supply Chain & Manufacturing
    # ==========================================================================
    # Create gauge charts (defined outside tabs for reuse)
    def create_gauge(value, title, color):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            title={'text': title, 'font': {'size': 14}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1},
                'bar': {'color': color},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#e9ecef",
                'steps': [
                    {'range': [0, 60], 'color': '#ffebee'},
                    {'range': [60, 80], 'color': '#fff3e0'},
                    {'range': [80, 100], 'color': '#e8f5e9'}
                ],
                'threshold': {'line': {'color': "red", 'width': 2}, 'thickness': 0.75, 'value': 85}
            }
        ))
        fig.update_layout(height=180, margin=dict(l=20, r=20, t=40, b=20))
        return fig
    
    with exec_tab3:
        st.markdown("#### 🏥 Supply Chain Health Score")
        
        g1, g2, g3, g4, trend_col = st.columns([1, 1, 1, 1, 2])
        
        with g1:
            st.plotly_chart(create_gauge(95.8, "On-Time Delivery", TELIT_GREEN), use_container_width=True)
        with g2:
            st.plotly_chart(create_gauge(87.3, "Factory OEE", TELIT_BLUE), use_container_width=True)
        with g3:
            st.plotly_chart(create_gauge(98.7, "Quality (FPY)", TELIT_GREEN), use_container_width=True)
        with g4:
            st.plotly_chart(create_gauge(78.5, "Supplier Score", TELIT_ORANGE), use_container_width=True)
        
        with trend_col:
            st.markdown("**📈 Production Trend (This Week)**")
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
            fig_prod = go.Figure()
            fig_prod.add_trace(go.Bar(x=days, y=[8100, 8450, 8200, 8350, 8247], name='Actual', marker_color=TELIT_BLUE))
            fig_prod.add_trace(go.Scatter(x=days, y=[8000]*5, mode='lines', name='Target', line=dict(color=TELIT_ORANGE, dash='dash')))
            fig_prod.update_layout(height=200, margin=dict(l=0, r=0, t=10, b=0), legend=dict(orientation="h", y=1.1), yaxis_title="Units")
            st.plotly_chart(fig_prod, use_container_width=True)
        
        st.markdown("---")
        
        # Operations snapshot
        ops_col, map_col = st.columns([1, 2])
        
        with ops_col:
            st.markdown("#### 📦 Operations Snapshot")
            st.metric("IoT Modules in Transit", "2.4M units", "+12.3%")
            st.metric("Inventory Value", "$78.5M", "-3.8%", delta_color="inverse")
            st.metric("Open POs", "187", "+8 new")
            st.metric("Order Backlog", "$42.3M", "+$5.2M")
            
            st.markdown("---")
            st.markdown("#### 🏢 Global Sites Status")
            sites = [
                ("🟢", "Trieste, Italy", "Manufacturing", "94%"),
                ("🟢", "Seoul, Korea", "Manufacturing", "89%"),
                ("🟢", "Irvine, CA (HQ)", "R&D/Ops", "Active"),
                ("🟢", "Tel Aviv, Israel", "R&D", "Active"),
                ("🟢", "Bangalore, India", "R&D", "Active"),
            ]
            for status, name, type_, util in sites:
                st.markdown(f"{status} **{name}** - {type_} ({util})")
    
    with map_col:
        st.markdown("#### 🌍 Telit Cinterion Global Footprint & Supply Chain")
        
        # Combined data for Telit locations and key suppliers
        locations_df = pd.DataFrame({
            'name': [
                # Telit Locations
                'Irvine, CA (HQ)', 'Trieste, Italy (Mfg)', 'Seoul, Korea (Mfg)', 
                'Tel Aviv, Israel (R&D)', 'São Paulo, Brazil', 'Bangalore, India (R&D)',
                # Key Suppliers
                'Qualcomm (San Diego)', 'MediaTek (Taiwan)', 'TSMC (Taiwan)',
                'Murata (Japan)', 'TDK (Japan)', 'Amphenol (Connecticut)',
                'TE Connectivity (Switzerland)', 'Infineon (Germany)'
            ],
            'lat': [
                33.68, 45.65, 37.57, 32.07, -23.55, 12.97,  # Telit
                32.72, 24.78, 24.78, 35.68, 35.68, 41.20, 47.05, 48.13  # Suppliers
            ],
            'lon': [
                -117.83, 13.78, 126.98, 34.78, -46.63, 77.59,  # Telit
                -117.16, 120.97, 120.97, 139.69, 139.69, -73.21, 8.30, 11.58  # Suppliers
            ],
            'type': [
                'Telit', 'Telit', 'Telit', 'Telit', 'Telit', 'Telit',
                'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier', 'Supplier'
            ],
            'category': [
                'HQ', 'Manufacturing', 'Manufacturing', 'R&D', 'Distribution', 'R&D',
                'Chipset', 'Chipset', 'Foundry', 'Passives', 'Passives', 'Connectors', 'Connectors', 'Semiconductors'
            ]
        })
        
        # Simple map with st.map (guaranteed to work)
        map_points = locations_df[['lat', 'lon']].copy()
        map_points.columns = ['lat', 'lon']
        st.map(map_points, zoom=1, use_container_width=True)
        
        # Legend with real Telit sites and suppliers
        loc1, loc2 = st.columns(2)
        with loc1:
            st.markdown(f"**<span style='color:{TELIT_BLUE}'>● Telit Cinterion:</span>**", unsafe_allow_html=True)
            st.caption("Irvine (HQ) • Trieste • Seoul • Tel Aviv • Bangalore • São Paulo")
        with loc2:
            st.markdown(f"**<span style='color:{TELIT_ORANGE}'>● Key Suppliers:</span>**", unsafe_allow_html=True)
            st.caption("Qualcomm • MediaTek • TSMC • Murata • TDK • Amphenol • TE • Infineon")
        
        # Revenue by region (realistic split)
        r1, r2, r3 = st.columns(3)
        r1.metric("🌎 Americas", "35%", "$178M")
        r2.metric("🌍 EMEA", "40%", "$204M")
        r3.metric("🌏 APAC", "25%", "$127M")
    
    st.markdown("---")
    
    # ==========================================================================
    # ROW 4: CHARTS - REVENUE BY SEGMENT + TOP MODULES + CUSTOMER MIX
    # ==========================================================================
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("#### 📊 Revenue by Segment")
        # Telit segments: IoT Modules, Connectivity Services, Software
        fig = px.pie(pd.DataFrame({
            'Segment': ['IoT Modules', 'Connectivity Services', 'Software & Services'],
            'Revenue': [382, 89, 38]  # ~$509M total, modules ~75%
        }), values='Revenue', names='Segment', hole=0.6,
           color_discrete_sequence=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE])
        fig.update_layout(height=250, margin=dict(l=0, r=0, t=0, b=0),
                          annotations=[dict(text='$509M', x=0.5, y=0.5, font_size=16, showarrow=False)])
        st.plotly_chart(fig, use_container_width=True)
    
    with c2:
        st.markdown("#### 📦 Top IoT Modules (Units YTD)")
        # Real Telit module families
        products = pd.DataFrame({
            'Module': ['ME310G1 (LTE-M)', 'FN990A (5G)', 'LE910C4 (LTE Cat 4)', 'SE868K3 (GNSS)', 'Cinterion TX62'],
            'Units': [1850000, 620000, 1420000, 890000, 780000]
        })
        fig = px.bar(products, x='Units', y='Module', orientation='h',
                     color='Units', color_continuous_scale=[[0, TELIT_BLUE], [1, TELIT_GREEN]])
        fig.update_layout(height=250, margin=dict(l=0, r=0, t=0, b=0), showlegend=False, coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with c3:
        st.markdown("#### 🏢 Revenue by Vertical")
        # Telit Cinterion key industry verticals (telit.com)
        verticals = ['Telematics', 'Smart Energy', 'Industrial IoT', 'Healthcare', 'Retail/POS', 'Other']
        percentages = [32, 24, 20, 10, 8, 6]
        colors = [TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#9c27b0', '#00BCD4', TELIT_GRAY]
        
        fig = go.Figure(data=[go.Bar(
            x=verticals,
            y=percentages,
            marker_color=colors,
            text=[f"{p}%" for p in percentages],
            textposition='outside'
        )])
        fig.update_layout(height=250, margin=dict(l=0, r=0, t=0, b=0), showlegend=False, yaxis_title="%")
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # ==========================================================================
    # ROW 5: ALERTS & ACTIONS + KEY INSIGHTS
    # ==========================================================================
    alert_col, insight_col = st.columns([1, 1])
    
    with alert_col:
        st.markdown("#### ⚠️ Active Alerts & Required Actions")
        alerts = [
            ("🔴", "CRITICAL", "Low stock: FN990A-WW (5G module) below safety stock", "Expedite Qualcomm chipset PO", 2),
            ("🔴", "CRITICAL", "Quality hold: ME310G1 Lot #TC24-2847 RF calibration drift", "Escalate to Trieste QA", 4),
            ("🟡", "WARNING", "Supplier delay: Murata MLCC +5 days lead time", "Update automotive ETAs", 12),
            ("🟡", "WARNING", "Geopolitical: Taiwan strait monitoring - TSMC exposure", "Review alternate sources", 24),
            ("🔵", "INFO", "New order: 50K LE910C4 units from Continental AG", "Confirm Q1 capacity", 48),
        ]
        for icon, level, msg, action, hrs in alerts:
            color = TELIT_RED if level == "CRITICAL" else TELIT_ORANGE if level == "WARNING" else TELIT_BLUE
            st.markdown(f"""
            <div style="background:{color}10; border-left:4px solid {color}; padding:12px; border-radius:0 8px 8px 0; margin-bottom:8px;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <div>
                        <span style="font-weight:600;">{icon} {level}</span><br>
                        <span style="font-size:13px;">{msg}</span>
                    </div>
                    <div style="text-align:right; font-size:11px;">
                        <span style="background:{color}; color:white; padding:2px 8px; border-radius:4px;">{action}</span><br>
                        <span style="color:{TELIT_GRAY};">Due: {hrs}h</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with insight_col:
        st.markdown("#### 💡 AI-Generated Insights (Cortex AI)")
        st.success("""
        **📈 5G Module Demand Surge**
        
        FN990A orders up 34% QoQ driven by automotive V2X adoption. European OEMs (BMW, VW Group) 
        accelerating telematics upgrades. Recommend +20% Q1 production allocation.
        """)
        st.warning("""
        **⚡ Semiconductor Supply Risk**
        
        Qualcomm SDX62 chipset allocation constrained through Q2. Affects 5G module production. 
        Mitigation: Qualify MediaTek T750 as secondary source within 45 days.
        """)
        st.info("""
        **🌱 ESG Opportunity**
        
        Smart metering segment requests Scope 3 emissions data for SE868 GNSS modules. 
        Early disclosure could secure $8.2M Landis+Gyr contract renewal.
        """)
    
    # ==========================================================================
    # TAB 4: CUSTOMERS & MARKET
    # ==========================================================================
    with exec_tab4:
        st.markdown("#### 🎯 Design Win Pipeline & Customer Health")
        
        # Design wins summary
        dw1, dw2, dw3, dw4 = st.columns(4)
        dw1.metric("Active Design Wins", "47", "+12 YTD")
        dw2.metric("Pipeline Value", "$128M", "+23%")
        dw3.metric("Win Rate", "34%", "+5 pts")
        dw4.metric("Avg Time to Revenue", "18 mo", "-3 mo")
        
        st.markdown("---")
        
        # Design win pipeline
        cust_col1, cust_col2 = st.columns([2, 1])
        
        with cust_col1:
            st.markdown("**🏆 Top Design Wins in Pipeline**")
            design_wins = pd.DataFrame({
                'Customer': ['Continental AG', 'Landis+Gyr', 'John Deere', 'Bosch', 'Siemens'],
                'Application': ['V2X Telematics', 'Smart Metering', 'Fleet Mgmt', 'Industrial IoT', 'Smart Grid'],
                'Module': ['FN990A (5G)', 'ME310G1', 'LE910C4', 'Cinterion TX62', 'ME310G1'],
                'Value ($M)': [18.5, 12.2, 8.7, 15.3, 9.8],
                'Stage': ['Design-In', 'Production', 'Qualification', 'Design-In', 'Production'],
                'Est. Revenue': ['Q2 2025', 'Active', 'Q3 2025', 'Q4 2025', 'Active']
            })
            st.dataframe(design_wins, use_container_width=True)
        
        with cust_col2:
            st.markdown("**📊 Pipeline by Stage**")
            stages = ['Lead', 'Design-In', 'Qualification', 'Production']
            values = [35, 48, 25, 20]
            colors = [TELIT_GRAY, TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN]
            
            fig_stage = go.Figure()
            for i, (stage, val, color) in enumerate(zip(stages, values, colors)):
                fig_stage.add_trace(go.Bar(
                    y=[stage],
                    x=[val],
                    orientation='h',
                    marker_color=color,
                    text=f'${val}M',
                    textposition='inside',
                    name=stage,
                    showlegend=False
                ))
            fig_stage.update_layout(height=220, margin=dict(l=0, r=0, t=10, b=0), barmode='stack', 
                                   xaxis_title="Value ($M)", yaxis=dict(categoryorder='array', categoryarray=stages[::-1]))
            st.plotly_chart(fig_stage, use_container_width=True)
        
        st.markdown("---")
        
        # Top customers
        st.markdown("#### 👥 Top 10 Customers - Health Dashboard")
        
        top_customers = pd.DataFrame({
            'Customer': ['Continental AG', 'Bosch', 'Landis+Gyr', 'Itron', 'John Deere', 
                        'Honeywell', 'Siemens', 'Trimble', 'CalAmp', 'Geotab'],
            'Revenue ($M)': [42.5, 38.2, 28.5, 24.8, 22.1, 19.5, 18.2, 15.8, 14.2, 12.8],
            'YoY Growth': ['+12%', '+8%', '+15%', '-3%', '+22%', '+5%', '+18%', '+7%', '-8%', '+25%'],
            'OTD': ['96%', '94%', '98%', '92%', '95%', '97%', '93%', '96%', '91%', '94%'],
            'Quality PPM': [45, 62, 28, 85, 38, 42, 55, 48, 92, 35],
            'NPS': [72, 68, 85, 58, 78, 65, 70, 62, 45, 80],
            'Health': ['🟢', '🟢', '🟢', '🟡', '🟢', '🟢', '🟢', '🟢', '🔴', '🟢']
        })
        st.dataframe(top_customers, use_container_width=True)
        
        st.markdown("---")
        
        # Technology transition
        st.markdown("#### 📱 Technology Transition Tracker (4G → 5G)")
        
        tech_col1, tech_col2 = st.columns(2)
        
        with tech_col1:
            st.markdown("**Module Portfolio Mix**")
            tech_mix = pd.DataFrame({
                'Technology': ['5G', 'LTE Cat 4+', 'LTE-M/NB-IoT', 'Legacy 3G/2G'],
                'Revenue %': [18, 35, 38, 9]
            })
            fig_tech = px.pie(tech_mix, values='Revenue %', names='Technology', hole=0.5,
                             color_discrete_sequence=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, TELIT_GRAY])
            fig_tech.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0))
            st.plotly_chart(fig_tech, use_container_width=True)
        
        with tech_col2:
            st.markdown("**5G Adoption Forecast**")
            years = ['2023', '2024', '2025', '2026', '2027']
            fig_5g = go.Figure()
            fig_5g.add_trace(go.Bar(x=years, y=[8, 18, 32, 48, 62], name='5G %', marker_color=TELIT_GREEN))
            fig_5g.add_trace(go.Scatter(x=years, y=[8, 18, 32, 48, 62], mode='lines+markers', 
                                        name='Trend', line=dict(color=TELIT_BLUE, width=2)))
            fig_5g.update_layout(height=250, margin=dict(l=0, r=0, t=10, b=0), yaxis_title="% of Revenue", 
                                legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_5g, use_container_width=True)
        
        # Competitive landscape
        st.markdown("---")
        st.markdown("#### 🏁 Competitive Position")
        
        comp_col1, comp_col2, comp_col3 = st.columns(3)
        
        with comp_col1:
            st.markdown(f"""
            <div style="background: {TELIT_GREEN}15; border-radius: 10px; padding: 15px; text-align: center;">
                <div style="font-size: 12px; color: {TELIT_GRAY};">Market Share (IoT Modules)</div>
                <div style="font-size: 32px; font-weight: bold; color: {TELIT_GREEN};">#3</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">Global ranking</div>
            </div>
            """, unsafe_allow_html=True)
        
        with comp_col2:
            st.markdown(f"""
            <div style="background: {TELIT_BLUE}15; border-radius: 10px; padding: 15px; text-align: center;">
                <div style="font-size: 12px; color: {TELIT_GRAY};">Automotive Telematics</div>
                <div style="font-size: 32px; font-weight: bold; color: {TELIT_BLUE};">#2</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">Behind Sierra Wireless</div>
            </div>
            """, unsafe_allow_html=True)
        
        with comp_col3:
            st.markdown(f"""
            <div style="background: {TELIT_ORANGE}15; border-radius: 10px; padding: 15px; text-align: center;">
                <div style="font-size: 12px; color: {TELIT_GRAY};">Smart Metering</div>
                <div style="font-size: 32px; font-weight: bold; color: {TELIT_ORANGE};">#1</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">Market leader</div>
            </div>
            """, unsafe_allow_html=True)
    
    # ==========================================================================
    # TAB 5: ALERTS & AI
    # ==========================================================================
    with exec_tab5:
        st.markdown("#### ⚠️ Active Alerts & Required Actions")
        
        # Alert summary metrics
        alert_m1, alert_m2, alert_m3, alert_m4 = st.columns(4)
        alert_m1.metric("Critical Alerts", "2", "🔴 Action Required")
        alert_m2.metric("Warnings", "3", "🟡 Monitor")
        alert_m3.metric("Info", "5", "🔵 FYI")
        alert_m4.metric("Avg Resolution", "4.2 hrs", "-1.8 hrs")
        
        st.markdown("---")
        
        # Alert list
        alerts_data = [
            ("🔴", "CRITICAL", "Low stock: FN990A-WW (5G module) below safety stock - 2,400 units remaining", "Expedite Qualcomm chipset PO #QC-2024-1847", 2, "Inventory"),
            ("🔴", "CRITICAL", "Quality hold: ME310G1 Lot #TC24-2847 - RF calibration drift detected in 3.2% of samples", "Escalate to Trieste QA Manager", 4, "Quality"),
            ("🟡", "WARNING", "Supplier delay: Murata MLCC delivery +5 days vs PO commitment", "Update Continental AG & BMW ETAs", 12, "Supplier"),
            ("🟡", "WARNING", "Geopolitical: Taiwan strait activity elevated - TSMC/MediaTek exposure monitoring", "Review alternate source qualification status", 24, "Risk"),
            ("🟡", "WARNING", "Capacity: Seoul line 3 OEE dropped to 78% - maintenance window recommended", "Schedule preventive maintenance", 48, "Operations"),
            ("🔵", "INFO", "New order: 50K LE910C4 units from Continental AG for Q1 delivery", "Confirm production capacity allocation", 48, "Sales"),
            ("🔵", "INFO", "Certification: FN990A-WW achieved AT&T FirstNet certification", "Update product marketing materials", 72, "Compliance"),
        ]
        
        for icon, level, msg, action, hrs, category in alerts_data:
            color = TELIT_RED if level == "CRITICAL" else TELIT_ORANGE if level == "WARNING" else TELIT_BLUE
            st.markdown(f"""
            <div style="background:{color}08; border-left:4px solid {color}; padding:15px; border-radius:0 8px 8px 0; margin-bottom:10px;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div style="flex:3;">
                        <span style="font-weight:600; font-size:14px;">{icon} {level}</span>
                        <span style="background:{color}20; color:{color}; padding:2px 8px; border-radius:10px; font-size:10px; margin-left:10px;">{category}</span><br>
                        <span style="font-size:13px; color:{TELIT_DARK}; margin-top:5px; display:block;">{msg}</span>
                    </div>
                    <div style="flex:1; text-align:right;">
                        <div style="background:{color}; color:white; padding:5px 10px; border-radius:6px; font-size:11px; display:inline-block;">{action}</div>
                        <div style="font-size:11px; color:{TELIT_GRAY}; margin-top:5px;">⏱️ Due: {hrs}h</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # AI Insights
        st.markdown("#### 🤖 AI-Generated Insights (Powered by Cortex AI)")
        
        ai_col1, ai_col2 = st.columns(2)
        
        with ai_col1:
            st.success("""
            **📈 Demand Signal: 5G Module Surge**
            
            Analysis of 847 data points shows FN990A orders trending +34% QoQ. Key drivers:
            - European OEM V2X telematics upgrades (BMW, VW Group, Stellantis)
            - US fleet management 4G sunset acceleration
            
            **Recommendation:** Increase Q1 production allocation by 20% (+15K units)
            
            *Confidence: 89% | Data freshness: 2 hours*
            """)
            
            st.warning("""
            **⚡ Supply Risk: Chipset Allocation**
            
            Qualcomm SDX62 allocation constrained through Q2 2025:
            - Industry-wide automotive chip demand +28%
            - Telit allocation: 85% of requested volume
            
            **Recommendation:** Fast-track MediaTek T750 qualification (45-day target)
            
            *Confidence: 94% | Data freshness: 6 hours*
            """)
        
        with ai_col2:
            st.info("""
            **🔮 Predictive: Quality Risk**
            
            ML model detected 2.3σ drift in ME310G1 RF calibration process:
            - Lot #TC24-2847 through #TC24-2852 at risk
            - Root cause probability: 67% humidity control, 23% component variance
            
            **Recommendation:** Increase inspection sampling rate to 100% for 48 hours
            
            *Confidence: 78% | Model: RF_QC_Predict_v3.2*
            """)
            
            st.success("""
            **🌱 Opportunity: ESG Revenue**
            
            Smart metering customers increasingly requesting Scope 3 data:
            - Landis+Gyr contract renewal ($8.2M) contingent on disclosure
            - 3 additional prospects with ESG requirements identified
            
            **Recommendation:** Prioritize supplier carbon data collection
            
            *Confidence: 85% | Data freshness: 24 hours*
            """)
        
        st.markdown("---")
        
        # AI recommendations summary
        st.markdown("#### 📋 AI Recommendation Summary")
        
        rec_data = pd.DataFrame({
            'Priority': ['🔴 High', '🔴 High', '🟡 Medium', '🟡 Medium', '🔵 Low'],
            'Recommendation': [
                'Qualify MediaTek T750 as secondary 5G chipset source',
                'Increase ME310G1 quality inspection sampling',
                'Increase FN990A Q1 production by 20%',
                'Accelerate supplier ESG data collection',
                'Schedule Seoul Line 3 preventive maintenance'
            ],
            'Impact': ['$18M revenue protection', '$2.4M quality cost avoidance', '$4.2M incremental revenue', '$8.2M contract retention', '$180K downtime avoidance'],
            'Effort': ['45 days', '48 hours', '2 weeks', '30 days', '1 weekend'],
            'Status': ['In Progress', 'Pending Approval', 'Approved', 'Planning', 'Scheduled']
        })
        st.dataframe(rec_data, use_container_width=True)

# =============================================================================
# PAGE: DIGITAL TWIN
# =============================================================================
elif page == "🏭 Digital Twin":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">🏭 Digital Twin - Trieste Factory</h1>
        <p style="opacity: 0.8; color: white;">Real-time IoT module production floor visualization</p>
    </div>""", unsafe_allow_html=True)
    
    # =================== LIVE PRODUCTION COUNTER (Always visible) ===================
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_BLUE}, #0D47A1); border-radius: 16px; padding: 25px; margin-bottom: 20px;">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
            <div style="flex: 2;">
                <div style="color: rgba(255,255,255,0.8); font-size: 14px; text-transform: uppercase; letter-spacing: 1px;">Today's Production</div>
                <div style="display: flex; align-items: baseline; gap: 10px; margin: 10px 0;">
                    <span style="font-size: 56px; font-weight: 700; color: white;">8,247</span>
                    <span style="font-size: 24px; color: rgba(255,255,255,0.7);">/ 12,000 units</span>
                </div>
                <div style="background: rgba(255,255,255,0.2); border-radius: 8px; height: 12px; overflow: hidden; margin: 15px 0;">
                    <div style="background: {TELIT_GREEN}; width: 68.7%; height: 100%; border-radius: 8px;"></div>
                </div>
                <div style="color: rgba(255,255,255,0.8); font-size: 13px;">🕐 6h 23m remaining | ⚡ 847 units/hr | 📈 +5.2% vs yesterday</div>
            </div>
            <div style="flex: 1; text-align: right; min-width: 200px;">
                <div style="color: {TELIT_GREEN}; font-size: 42px; font-weight: 600;">68.7%</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 13px;">of daily target</div>
                <div style="color: {TELIT_GREEN}; font-size: 14px; margin-top: 8px;">✓ On track</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Top KPIs (Always visible)
    kpi_cols = st.columns(6)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("OEE", "87.3%", "+2.1%"), 
        ("Throughput", "12,450/day", "+5%"),
        ("Quality FPY", "98.7%", "+0.3%"), 
        ("Availability", "92.1%", "+1.2%"),
        ("Workers", "47/50", "94%"),
        ("Energy", "1,247 kWh", "-8%")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # =================== TABBED INTERFACE ===================
    dt_tab1, dt_tab2, dt_tab3, dt_tab4, dt_tab5, dt_tab6, dt_tab7, dt_tab8, dt_tab9, dt_tab10, dt_tab11 = st.tabs([
        "🏭 Factory Floor", 
        "📈 Production", 
        "🔧 Quality", 
        "📦 Materials",
        "⚡ Energy",
        "🔮 Maintenance",
        "👷 Operators",
        "🔬 Traceability",
        "🎮 Simulator",
        "🚨 Alerts",
        "🤖 AI"
    ])
    
    # =================================================================
    # TAB 1: FACTORY FLOOR
    # =================================================================
    with dt_tab1:
        st.subheader("🗺️ Factory Floor Map - Live Status")
        
        # Create factory floor layout with Plotly
        fig = go.Figure()
        
        # Factory zones with coordinates, status, and KPIs
        zones = [
            {"name": "RECEIVING\nDOCKS", "x": 30, "y": 420, "w": 90, "h": 60, "status": "green", "kpi": "3 Active"},
            {"name": "RAW MATERIAL\nSTORAGE", "x": 30, "y": 300, "w": 90, "h": 100, "status": "green", "kpi": "78% Full"},
            {"name": "SMT LINE 1\n(ME310G1)", "x": 140, "y": 380, "w": 140, "h": 80, "status": "green", "kpi": "847 u/hr | 98%"},
            {"name": "SMT LINE 2\n(FN990A 5G)", "x": 140, "y": 280, "w": 140, "h": 80, "status": "orange", "kpi": "792 u/hr | 94%"},
            {"name": "SMT LINE 3\n(LE910C4)", "x": 140, "y": 180, "w": 140, "h": 80, "status": "green", "kpi": "823 u/hr | 97%"},
            {"name": "SMT LINE 4\n(SE868K3 GNSS)", "x": 140, "y": 80, "w": 140, "h": 80, "status": "green", "kpi": "654 u/hr | 99%"},
            {"name": "REFLOW 1", "x": 300, "y": 380, "w": 60, "h": 80, "status": "green", "kpi": "245°C"},
            {"name": "REFLOW 2", "x": 300, "y": 280, "w": 60, "h": 80, "status": "orange", "kpi": "238°C ⚠️"},
            {"name": "REFLOW 3", "x": 300, "y": 180, "w": 60, "h": 80, "status": "green", "kpi": "243°C"},
            {"name": "REFLOW 4", "x": 300, "y": 80, "w": 60, "h": 80, "status": "green", "kpi": "244°C"},
            {"name": "AOI 1", "x": 380, "y": 380, "w": 50, "h": 80, "status": "green", "kpi": "99.2%"},
            {"name": "AOI 2", "x": 380, "y": 280, "w": 50, "h": 80, "status": "red", "kpi": "65% ⚠️"},
            {"name": "AOI 3", "x": 380, "y": 180, "w": 50, "h": 80, "status": "green", "kpi": "98.8%"},
            {"name": "AOI 4", "x": 380, "y": 80, "w": 50, "h": 80, "status": "green", "kpi": "99.5%"},
            {"name": "FIRMWARE\nPROGRAMMING", "x": 450, "y": 220, "w": 80, "h": 160, "status": "green", "kpi": "1,200/hr"},
            {"name": "RF TEST\nCHAMBER 1", "x": 550, "y": 380, "w": 80, "h": 80, "status": "green", "kpi": "LTE: -105dBm"},
            {"name": "RF TEST\nCHAMBER 2", "x": 550, "y": 280, "w": 80, "h": 80, "status": "green", "kpi": "5G: -98dBm"},
            {"name": "GNSS TEST\nCHAMBER", "x": 550, "y": 180, "w": 80, "h": 80, "status": "green", "kpi": "GPS: 28dB"},
            {"name": "FUNCTIONAL\nTEST", "x": 550, "y": 80, "w": 80, "h": 80, "status": "green", "kpi": "98.7% Pass"},
            {"name": "CERT LAB\nFCC/CE/PTCRB", "x": 650, "y": 280, "w": 90, "h": 80, "status": "green", "kpi": "12 Pending"},
            {"name": "FINAL QC\n& LABELING", "x": 760, "y": 320, "w": 80, "h": 80, "status": "green", "kpi": "2,340/hr"},
            {"name": "FINISHED\nGOODS", "x": 760, "y": 180, "w": 80, "h": 120, "status": "green", "kpi": "85% Full"},
            {"name": "SHIPPING", "x": 860, "y": 220, "w": 70, "h": 140, "status": "green", "kpi": "2 Loading"},
        ]
        
        colors = {"green": "#00C48C", "orange": "#FF9F43", "red": "#FF4757"}
        fill_colors = {
            "green": "rgba(0, 196, 140, 0.2)",
            "orange": "rgba(255, 159, 67, 0.2)",
            "red": "rgba(255, 71, 87, 0.2)"
        }
        
        for zone in zones:
            fig.add_shape(
                type="rect",
                x0=zone["x"], y0=zone["y"],
                x1=zone["x"] + zone["w"], y1=zone["y"] + zone["h"],
                fillcolor=fill_colors[zone["status"]],
                line=dict(color=colors[zone["status"]], width=3),
            )
            fig.add_annotation(
                x=zone["x"] + zone["w"]/2, y=zone["y"] + zone["h"]/2 + 15,
                text=zone["name"], showarrow=False,
                font=dict(size=10, color="#1E3A5F"),
            )
            fig.add_annotation(
                x=zone["x"] + zone["w"]/2, y=zone["y"] + zone["h"]/2 - 15,
                text=zone["kpi"], showarrow=False,
                font=dict(size=9, color=colors[zone["status"]], family="monospace"),
            )
        
        # Add flow arrows (outside the loop)
        arrows = [(170, 380), (380, 380), (490, 380), (600, 310), (730, 310), (860, 310)]
        for x, y in arrows:
            fig.add_annotation(x=x, y=y, text="→", showarrow=False, font=dict(size=20, color="#6B7C93"))
        
        fig.update_layout(
            height=500,
            showlegend=False,
            xaxis=dict(visible=False, range=[0, 1000]),
            yaxis=dict(visible=False, range=[0, 500]),
            margin=dict(l=10, r=10, t=10, b=10),
            plot_bgcolor="#f8fafc",
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Legend
        leg1, leg2, leg3, leg4 = st.columns(4)
        leg1.markdown("🟢 **Normal** - Operating within spec")
        leg2.markdown("🟡 **Warning** - Attention needed")
        leg3.markdown("🔴 **Critical** - Immediate action required")
        leg4.markdown("**Live data** refreshes every 30 sec")
        
        st.markdown("---")
        
        # Equipment Status Table
        st.subheader("⚙️ Equipment Status - IoT Module Production Line")
        
        equipment_data = pd.DataFrame({
            "Equipment": [
                "SMT Line 1 (Juki)", "SMT Line 2 (Juki)", "SMT Line 3 (Fuji)", "SMT Line 4 (Fuji)",
                "Reflow Oven 1 (Heller)", "Reflow Oven 2 (Heller)", 
                "AOI 1 (Koh Young)", "AOI 2 (Koh Young)",
                "Firmware Programmer", "RF Test Chamber 1 (R&S)", "RF Test Chamber 2 (Keysight)", 
                "GNSS Simulator", "Functional Test (NI)"
            ],
            "Status": [
                "🟢 Running", "🟡 Degraded", "🟢 Running", "🟢 Running",
                "🟢 Running", "🟡 Stabilizing",
                "🟢 Running", "🔴 Fault",
                "🟢 Running", "🟢 Running", "🟢 Running",
                "🟢 Running", "🟢 Running"
            ],
            "Product": [
                "ME310G1", "FN990A 5G", "LE910C4", "SE868K3",
                "ME310", "FN990", 
                "All", "FN990",
                "All", "LTE/LTE-M", "5G NR",
                "GNSS", "All"
            ],
            "Metric": [
                "847 u/hr", "792 u/hr", "823 u/hr", "654 u/hr",
                "245°C Peak", "238°C ⚠️",
                "99.2% Yield", "65.2% ⚠️",
                "1,200 u/hr", "-105dBm Sens", "-98dBm Sens",
                "28dB C/N0", "98.7% Pass"
            ],
            "OEE": ["92.5%", "78.3%", "89.1%", "94.2%", "95.1%", "82.0%", "98.5%", "65.2%", "96.8%", "97.2%", "98.1%", "99.5%", "96.3%"],
            "Next Maint.": ["Dec 28", "Dec 24", "Jan 3", "Jan 5", "Dec 30", "Dec 26", "Jan 5", "NOW", "Jan 10", "Jan 8", "Jan 12", "Jan 15", "Jan 8"],
        })
        st.dataframe(equipment_data, use_container_width=True)
        
        st.markdown("---")
        
        # Cleanroom Environment
        st.subheader("🌡️ Cleanroom Environment (ISO Class 7)")
        env_metrics = st.columns(4)
        with env_metrics[0]:
            st.metric("Temperature", "22.1°C", "+0.3°C")
            st.caption("Spec: 21-23°C ✓")
        with env_metrics[1]:
            st.metric("Humidity", "45.2%", "-1.8%")
            st.caption("Spec: 40-60% ✓")
        with env_metrics[2]:
            st.metric("Particles", "2,847/m³", "-12%")
            st.caption("Limit: <352K ✓")
        with env_metrics[3]:
            st.metric("ESD Events", "0", "0")
            st.caption("Last 24h ✓")
        
        st.success("✅ All Environmental Parameters Within Spec - HVAC zones operating normally")
    
    # =================================================================
    # TAB 2: PRODUCTION & PERFORMANCE
    # =================================================================
    with dt_tab2:
        # Shift Performance
        st.subheader("👷 Current Shift Performance")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px; border: 1px solid #cbd5e1;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 15px;">
                <div>
                    <span style="font-size: 18px; font-weight: 600; color: {TELIT_BLUE};">Morning Shift (08:00 - 16:00)</span><br>
                    <span style="color: {TELIT_GRAY}; font-size: 13px;">Supervisor: Maria Bianchi | 47 operators</span>
                </div>
                <div style="text-align: right;">
                    <span style="font-size: 24px; font-weight: 700; color: {TELIT_GREEN};">A+</span><br>
                    <span style="color: {TELIT_GRAY}; font-size: 11px;">Shift Rating</span>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; text-align: center;">
                <div style="background: white; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 22px; font-weight: 600; color: {TELIT_BLUE};">4,892</div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">Units Produced</div>
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 22px; font-weight: 600; color: {TELIT_GREEN};">98.7%</div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">First Pass Yield</div>
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 22px; font-weight: 600; color: {TELIT_GREEN};">0</div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">Safety Incidents</div>
                </div>
                <div style="background: white; padding: 12px; border-radius: 8px;">
                    <div style="font-size: 22px; font-weight: 600; color: {TELIT_ORANGE};">2</div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">Downtime Events</div>
                </div>
            </div>
            <div style="margin-top: 15px; padding-top: 12px; border-top: 1px solid #e2e8f0; font-size: 12px; color: {TELIT_GRAY};">
                📊 vs. Previous Shift: +3.2% units | +0.4% yield | Handover notes: AOI 2 under repair
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Customer Orders in Production
        st.subheader("📋 Customer Orders in Production")
        order_cols = st.columns(4)
        orders = [
            ("BMW Group", "FN990A 5G", "V2X Telematics", 2400, 1872, "78%", TELIT_BLUE, "Dec 27"),
            ("Landis+Gyr", "ME310G1", "Smart Meters", 5000, 3247, "65%", TELIT_GREEN, "Dec 28"),
            ("Continental AG", "LE910C4", "Fleet Mgmt", 1800, 1620, "90%", TELIT_ORANGE, "Dec 24"),
            ("Itron Inc", "SE868K3", "AMI Modules", 3000, 1893, "63%", "#6B5B95", "Dec 30"),
        ]
        for col, (customer, product, application, total, done, pct, color, ship) in zip(order_cols, orders):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}10, {color}05); border-radius: 12px; padding: 15px; border-left: 4px solid {color}; height: 180px;">
                <div style="font-weight: 600; color: {color}; font-size: 14px;">{customer}</div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; margin: 4px 0;">{product} • {application}</div>
                <div style="font-size: 28px; font-weight: 700; margin: 12px 0;">{done:,}<span style="font-size: 14px; color: {TELIT_GRAY};"> / {total:,}</span></div>
                <div style="background: #e0e5ec; border-radius: 4px; height: 8px; overflow: hidden; margin: 8px 0;">
                    <div style="background: {color}; width: {pct}; height: 100%;"></div>
                </div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">🚚 Ship: {ship} | {pct} complete</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Production & OEE Charts
        prod_col, oee_col = st.columns(2)
    
    with prod_col:
        st.subheader("📊 Today's Production by Product Family")
        prod_data = pd.DataFrame({
            "Product": ["ME310G1 (LTE-M)", "FN990A (5G)", "LE910C4 (LTE)", "SE868K3 (GNSS)", "CC864 (2G)"],
            "Produced": [3247, 2891, 2654, 1893, 987],
            "Target": [3500, 3000, 2800, 2000, 1000],
            "Color": [TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, "#6B5B95", TELIT_GRAY]
        })
        prod_data["Variance"] = ((prod_data["Produced"] / prod_data["Target"]) * 100).round(1)
        
        fig_prod = go.Figure()
        fig_prod.add_trace(go.Bar(
            name="Target",
            x=prod_data["Product"],
            y=prod_data["Target"],
            marker_color="rgba(30, 58, 95, 0.3)",
            text=prod_data["Target"],
            textposition="outside"
        ))
        fig_prod.add_trace(go.Bar(
            name="Produced",
            x=prod_data["Product"],
            y=prod_data["Produced"],
            marker_color=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, "#6B5B95", TELIT_GRAY],
            text=[f"{v}%" for v in prod_data["Variance"]],
            textposition="outside"
        ))
        fig_prod.update_layout(
            barmode="overlay",
            height=300,
            margin=dict(l=20, r=20, t=30, b=60),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis_title="Units"
        )
        st.plotly_chart(fig_prod, use_container_width=True)
    
    with oee_col:
        st.subheader("📈 OEE Trend - Last 24 Hours")
        hours = list(range(24))
        oee_values = [84.2, 85.1, 86.3, 87.5, 88.2, 87.9, 86.4, 85.8, 87.3, 88.1, 89.2, 90.1, 
                      89.5, 88.7, 87.9, 86.5, 85.3, 84.8, 85.6, 86.9, 87.8, 88.4, 87.9, 87.3]
        availability = [92.1, 93.2, 94.5, 95.1, 94.8, 93.6, 92.8, 91.5, 92.3, 93.8, 94.2, 95.5,
                        94.8, 93.5, 92.1, 91.8, 90.5, 89.8, 91.2, 92.5, 93.8, 94.5, 93.2, 92.1]
        
        fig_oee = go.Figure()
        fig_oee.add_trace(go.Scatter(x=hours, y=oee_values, name="OEE", line=dict(color=TELIT_BLUE, width=3)))
        fig_oee.add_trace(go.Scatter(x=hours, y=availability, name="Availability", line=dict(color=TELIT_GREEN, width=2, dash="dash")))
        fig_oee.add_hline(y=85, line_dash="dot", line_color=TELIT_RED, annotation_text="Target: 85%")
        fig_oee.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=30, b=40),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis_title="Hour",
            yaxis_title="%",
            yaxis=dict(range=[80, 100])
        )
        st.plotly_chart(fig_oee, use_container_width=True)
        
    st.markdown("---")
    
    # Yield Trend & Cycle Time
    yield_col, cycle_col = st.columns(2)
    
    with yield_col:
        st.subheader("📈 Yield Trend by Lot (Last 10)")
        lots = [f"L{i}" for i in range(2412, 2422)]
        yield_me310 = [98.5, 98.7, 98.2, 98.9, 98.6, 98.4, 98.8, 98.3, 98.7, 98.5]
        yield_fn990 = [97.2, 97.5, 96.8, 97.1, 97.8, 97.3, 96.9, 97.4, 97.6, 97.2]
        yield_le910 = [99.1, 99.0, 98.9, 99.2, 99.0, 98.8, 99.1, 99.0, 98.9, 99.1]
        
        fig_yield = go.Figure()
        fig_yield.add_trace(go.Scatter(x=lots, y=yield_me310, name="ME310G1", line=dict(color=TELIT_BLUE, width=2), mode='lines+markers'))
        fig_yield.add_trace(go.Scatter(x=lots, y=yield_fn990, name="FN990A 5G", line=dict(color=TELIT_ORANGE, width=2), mode='lines+markers'))
        fig_yield.add_trace(go.Scatter(x=lots, y=yield_le910, name="LE910C4", line=dict(color=TELIT_GREEN, width=2), mode='lines+markers'))
        fig_yield.add_hline(y=98, line_dash="dash", line_color=TELIT_RED, annotation_text="Target: 98%")
        fig_yield.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=30, b=40),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            yaxis_title="First Pass Yield %",
            yaxis=dict(range=[96, 100])
        )
        st.plotly_chart(fig_yield, use_container_width=True)
        st.caption("🔍 FN990A 5G below target - SDX62 BGA complexity")
    
    with cycle_col:
        st.subheader("⏱️ Cycle Time & Bottleneck")
        
        stages = ["SMT", "Reflow", "AOI", "FW Prog", "RF Test", "Func", "Pack"]
        cycle_times = [45, 180, 30, 25, 90, 45, 20]
        target_times = [40, 180, 25, 20, 75, 40, 15]
        
        colors_ct = [TELIT_RED if c > t * 1.1 else TELIT_ORANGE if c > t else TELIT_GREEN for c, t in zip(cycle_times, target_times)]
        
        fig_cycle = go.Figure()
        fig_cycle.add_trace(go.Bar(x=stages, y=cycle_times, name="Actual", marker_color=colors_ct, text=[f"{t}s" for t in cycle_times], textposition="outside"))
        fig_cycle.add_trace(go.Scatter(x=stages, y=target_times, name="Target", mode="lines+markers", line=dict(color="#1E3A5F", width=2, dash="dash")))
        fig_cycle.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Seconds")
        st.plotly_chart(fig_cycle, use_container_width=True)
        st.warning("🔴 Bottleneck: RF Test (+20% over target) - Add 2nd R&S CMW500")
    
    st.markdown("---")
    
    # Analytics Summary
    st.subheader("📊 Production Analytics Summary (MTD)")
    analytics_cols = st.columns(5)
    analytics = [
        ("Total Output", "247,832", "+8.3%", TELIT_GREEN),
        ("Avg Cycle Time", "7.2 min", "-0.3 min", TELIT_GREEN),
        ("Scrap Rate", "0.8%", "-0.2%", TELIT_GREEN),
        ("Rework Rate", "1.2%", "+0.1%", TELIT_ORANGE),
        ("OEE (MTD)", "86.7%", "+1.8%", TELIT_GREEN),
    ]
    for col, (label, value, delta, color) in zip(analytics_cols, analytics):
        col.metric(label, value, delta)
    
    # =================================================================
    # TAB 3: QUALITY & PROCESS
    # =================================================================
    with dt_tab3:
        # Reflow & Quality
        reflow_col, quality_col = st.columns(2)
    
        with reflow_col:
            st.subheader("🌡️ Reflow Oven Temperature Profile")
            reflow_zones = ["Preheat 1", "Preheat 2", "Soak", "Ramp", "Reflow", "Peak", "Cooling"]
            oven1 = [150, 180, 200, 220, 238, 245, 180]
            oven2 = [148, 178, 198, 215, 232, 238, 175]
            oven3 = [151, 181, 201, 221, 239, 243, 179]
            target_temps = [150, 180, 200, 220, 235, 245, 180]
            
            fig_reflow = go.Figure()
            fig_reflow.add_trace(go.Scatter(x=reflow_zones, y=target_temps, name="Target Profile", line=dict(color="#1E3A5F", width=3, dash="dash")))
            fig_reflow.add_trace(go.Scatter(x=reflow_zones, y=oven1, name="Oven 1 (ME310)", line=dict(color=TELIT_GREEN, width=2), marker=dict(size=8)))
            fig_reflow.add_trace(go.Scatter(x=reflow_zones, y=oven2, name="Oven 2 (FN990) ⚠️", line=dict(color=TELIT_ORANGE, width=2), marker=dict(size=8)))
            fig_reflow.add_trace(go.Scatter(x=reflow_zones, y=oven3, name="Oven 3 (LE910)", line=dict(color=TELIT_BLUE, width=2), marker=dict(size=8)))
            fig_reflow.update_layout(
                height=300,
                margin=dict(l=20, r=20, t=30, b=60),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                yaxis_title="Temperature (°C)",
                yaxis=dict(range=[100, 270])
            )
            st.plotly_chart(fig_reflow, use_container_width=True)
            st.caption("⚠️ Oven 2 running 7°C below peak target - solder joint quality at risk")
        
        with quality_col:
            st.subheader("✅ First Pass Yield by Shift")
            shifts = ["Night (00-08)", "Morning (08-16)", "Evening (16-24)"]
            fpy_me310 = [98.2, 98.7, 98.5]
            fpy_fn990 = [97.1, 97.8, 96.9]
            fpy_le910 = [98.8, 99.1, 98.9]
            
            fig_fpy = go.Figure()
            fig_fpy.add_trace(go.Bar(x=shifts, y=fpy_me310, name="ME310G1", marker_color=TELIT_BLUE))
            fig_fpy.add_trace(go.Bar(x=shifts, y=fpy_fn990, name="FN990A", marker_color=TELIT_GREEN))
            fig_fpy.add_trace(go.Bar(x=shifts, y=fpy_le910, name="LE910C4", marker_color=TELIT_ORANGE))
            fig_fpy.add_hline(y=98, line_dash="dot", line_color=TELIT_RED, annotation_text="Target: 98%")
            fig_fpy.update_layout(
                barmode="group",
                height=300,
                margin=dict(l=20, r=20, t=30, b=60),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                yaxis_title="FPY %",
                yaxis=dict(range=[95, 100])
            )
            st.plotly_chart(fig_fpy, use_container_width=True)
        
        st.markdown("---")
        
        # RF Testing & Defect Analysis
        rf_col, defect_col = st.columns(2)
        
        with rf_col:
            st.subheader("📡 RF Test Results - Last Hour")
            st.markdown("*Wireless module sensitivity & power calibration*")
            
            rf_tests = ["ME310G1\nLTE-M", "FN990A\n5G NR", "LE910C4\nLTE Cat 4", "SE868K3\nGNSS"]
            sensitivity = [-105.2, -98.5, -103.8, 28.5]
            spec_limit = [-105.0, -98.0, -103.0, 27.0]
            
            fig_rf = go.Figure()
            colors_rf = [TELIT_GREEN if s <= l else TELIT_RED for s, l in zip(sensitivity[:3], spec_limit[:3])]
            colors_rf.append(TELIT_GREEN if sensitivity[3] >= spec_limit[3] else TELIT_RED)
            
            fig_rf.add_trace(go.Bar(
                x=rf_tests, y=[abs(s) for s in sensitivity],
                marker_color=colors_rf,
                text=[f"{s} dBm" if i < 3 else f"{s} dB" for i, s in enumerate(sensitivity)],
                textposition="outside"
            ))
            fig_rf.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=10, b=40),
                yaxis_title="Sensitivity (dBm / dB)",
                showlegend=False
            )
            st.plotly_chart(fig_rf, use_container_width=True)
            
            rf_stats = st.columns(4)
            rf_stats[0].metric("Tested", "1,247", "+12%")
            rf_stats[1].metric("Pass Rate", "99.2%", "+0.1%")
            rf_stats[2].metric("Avg Cal Time", "18.3s", "-2.1s")
            rf_stats[3].metric("RF Failures", "10", "-3")
        
        with defect_col:
            st.subheader("🔍 Defect Pareto - SMT Assembly")
            st.markdown("*Top defects from AOI & X-ray inspection*")
            
            defects = ["Solder Bridge", "Missing\nComponent", "Tombstone", "Cold Joint", "BGA Void", "Misalign"]
            counts = [23, 18, 12, 8, 5, 4]
            cumulative = np.cumsum(counts) / sum(counts) * 100
            
            fig_defect = go.Figure()
            fig_defect.add_trace(go.Bar(
                x=defects, y=counts, name="Defect Count",
                marker_color=[TELIT_RED if c > 15 else TELIT_ORANGE if c > 8 else TELIT_GREEN for c in counts],
                text=counts, textposition="outside"
            ))
            fig_defect.add_trace(go.Scatter(
                x=defects, y=cumulative, name="Cumulative %",
                yaxis="y2", line=dict(color="#1E3A5F", width=2), marker=dict(size=8)
            ))
            fig_defect.add_hline(y=80, line_dash="dot", line_color=TELIT_BLUE, yref="y2", annotation_text="80%")
            fig_defect.update_layout(
                height=280,
                margin=dict(l=20, r=60, t=10, b=40),
                yaxis=dict(title="Count"),
                yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 105]),
                showlegend=False
            )
            st.plotly_chart(fig_defect, use_container_width=True)
    
    # =================================================================
    # TAB 4: RESOURCES & MATERIALS
    # =================================================================
    with dt_tab4:
        # Component Tracking
        st.subheader("📦 Critical Component Inventory at Line Side")
        st.markdown("*Key chipsets and passive components for IoT module production*")
        comp_cols = st.columns(5)
        components = [
            ("Qualcomm MDM9207-1", "ME310G1 LTE-M", 2450, 4000, TELIT_BLUE),
            ("Qualcomm SDX62", "FN990A 5G", 890, 2500, TELIT_ORANGE),
            ("Qualcomm MDM9615M", "LE910C4 LTE", 3120, 3500, TELIT_GREEN),
            ("u-blox UBX-M10050", "SE868K3 GNSS", 1850, 2000, "#6B5B95"),
            ("Skyworks SKY78130", "All (PA/LNA)", 8500, 10000, TELIT_GRAY)
        ]
        for col, (comp, product, current, max_qty, color) in zip(comp_cols, components):
            pct = int((current / max_qty) * 100)
            status = "🟢" if pct > 50 else "🟡" if pct > 25 else "🔴"
            col.markdown(f"""
            <div style="background:linear-gradient(135deg, {color}15, {color}05); border-radius:12px; padding:15px; border:1px solid {color}40;">
                <div style="font-weight:600; color:{color}; font-size:12px;">{comp}</div>
                <div style="font-size:10px; color:{TELIT_GRAY};">for {product}</div>
                <div style="font-size:24px; font-weight:700; margin:10px 0;">{status} {current:,}</div>
                <div style="background:#e0e5ec; border-radius:4px; height:8px; overflow:hidden;">
                    <div style="background:{color}; width:{pct}%; height:100%;"></div>
                </div>
                <div style="font-size:10px; color:{TELIT_GRAY}; margin-top:4px;">{pct}% of {max_qty:,} capacity</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Energy Consumption
        st.subheader("⚡ Energy Consumption by Zone")
        energy_cols = st.columns(4)
        energy_zones = [
            ("SMT Assembly", 285, 320, TELIT_BLUE, "-11%"),
            ("Reflow Ovens", 412, 450, TELIT_RED, "-8%"),
            ("RF Test Labs", 245, 260, TELIT_GREEN, "-6%"),
            ("HVAC/Facility", 305, 350, TELIT_GRAY, "-13%")
        ]
        for col, (zone, current, max_kw, color, delta) in zip(energy_cols, energy_zones):
            col.metric(f"{zone}", f"{current} kWh", delta, delta_color="inverse")
        
        st.markdown("---")
        
        # Supplier Status
        st.subheader("🤝 Key Supplier Status")
        supplier_data = pd.DataFrame({
            "Supplier": ["Qualcomm", "u-blox", "Skyworks", "Murata", "JCET (Assembly)"],
            "Component": ["Modem Chipsets", "GNSS Receivers", "PA/LNA", "Passives", "Packaging"],
            "Lead Time": ["12 weeks", "8 weeks", "6 weeks", "4 weeks", "3 weeks"],
            "Status": ["🟡 Constrained", "🟢 Normal", "🟢 Normal", "🟢 Normal", "🟢 Normal"],
            "Open POs": ["$4.2M", "$1.8M", "$0.9M", "$0.6M", "$2.1M"],
            "Risk Level": ["Medium", "Low", "Low", "Low", "Low"]
        })
        st.dataframe(supplier_data, use_container_width=True)
    
    # =================================================================
    # TAB 5: ENERGY & SUSTAINABILITY
    # =================================================================
    with dt_tab5:
        st.subheader("⚡ Real-Time Energy Monitoring")
        
        # Energy KPIs
        energy_cols = st.columns(4)
        energy_cols[0].metric("Current Power", "847 kW", "-3.2%", help="Total facility power consumption")
        energy_cols[1].metric("Today's Usage", "18.2 MWh", "-5%", help="Cumulative energy today")
        energy_cols[2].metric("Energy/Unit", "0.42 kWh", "-8%", help="Energy per module produced")
        energy_cols[3].metric("Carbon Intensity", "312 g/unit", "-12%", help="CO2 per unit produced")
        
        st.markdown("---")
        
        # Energy consumption by area
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🏭 Consumption by Production Area")
            energy_by_area = pd.DataFrame({
                "Area": ["SMT Lines", "Reflow Ovens", "Testing", "Clean Room", "HVAC", "Lighting", "Other"],
                "Power (kW)": [285, 198, 142, 95, 78, 32, 17],
                "% of Total": [33.6, 23.4, 16.8, 11.2, 9.2, 3.8, 2.0]
            })
            
            fig_energy = px.pie(
                energy_by_area, 
                values="Power (kW)", 
                names="Area",
                color_discrete_sequence=['#00A7E1', '#0D2C54', '#29B5E8', '#5D9CEC', '#8CC4E8', '#B8DCF0', '#E0F0F8']
            )
            fig_energy.update_traces(textposition='inside', textinfo='percent+label')
            fig_energy.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=300)
            st.plotly_chart(fig_energy, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 24-Hour Energy Profile")
            hours = list(range(24))
            power_profile = [520, 485, 478, 475, 490, 580, 720, 845, 895, 910, 905, 890, 
                           875, 895, 905, 890, 865, 820, 765, 680, 610, 575, 550, 530]
            
            fig_profile = go.Figure()
            fig_profile.add_trace(go.Scatter(
                x=hours, y=power_profile, mode='lines+markers',
                fill='tozeroy', fillcolor='rgba(0, 167, 225, 0.3)',
                line=dict(color=TELIT_BLUE, width=2), name='Power (kW)'
            ))
            fig_profile.add_hline(y=847, line_dash="dash", line_color="red", 
                                annotation_text="Current")
            fig_profile.update_layout(
                xaxis_title="Hour", yaxis_title="Power (kW)",
                margin=dict(l=0, r=0, t=20, b=0), height=300
            )
            st.plotly_chart(fig_profile, use_container_width=True)
        
        # Sustainability metrics
        st.subheader("🌱 Sustainability Dashboard")
        sus_cols = st.columns(4)
        sus_cols[0].metric("Renewable Energy", "45%", "+5%", help="% from solar/renewable sources")
        sus_cols[1].metric("Water Usage", "2,450 L/day", "-8%", help="Process water consumption")
        sus_cols[2].metric("Waste Recycled", "89%", "+3%", help="Manufacturing waste recycled")
        sus_cols[3].metric("VOC Emissions", "12 ppm", "-15%", help="Volatile organic compounds")
        
        # Energy efficiency trends
        st.markdown("##### 📊 Energy Efficiency Trends (Last 12 Months)")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        efficiency_data = pd.DataFrame({
            "Month": months,
            "Energy/Unit (kWh)": [0.52, 0.50, 0.49, 0.48, 0.46, 0.45, 0.44, 0.43, 0.42, 0.42, 0.42, 0.42],
            "Target": [0.48, 0.47, 0.46, 0.45, 0.44, 0.43, 0.42, 0.41, 0.40, 0.40, 0.40, 0.40]
        })
        
        fig_eff = go.Figure()
        fig_eff.add_trace(go.Scatter(x=months, y=efficiency_data["Energy/Unit (kWh)"],
                                     mode='lines+markers', name='Actual', line=dict(color=TELIT_BLUE, width=3)))
        fig_eff.add_trace(go.Scatter(x=months, y=efficiency_data["Target"],
                                     mode='lines', name='Target', line=dict(color='green', width=2, dash='dash')))
        fig_eff.update_layout(xaxis_title="Month", yaxis_title="kWh/Unit",
                             margin=dict(l=0, r=0, t=20, b=0), height=250)
        st.plotly_chart(fig_eff, use_container_width=True)
    
    # =================================================================
    # TAB 6: PREDICTIVE MAINTENANCE
    # =================================================================
    with dt_tab6:
        st.subheader("🔮 Equipment Health & Predictions")
        
        # Equipment health overview
        equipment_health = [
            {"Machine": "SMT Line 1 - Pick & Place", "Health": 94, "Status": "🟢 Good", "Next Maint": "12 days", "RUL": "2,850 hrs", "Risk": "Low"},
            {"Machine": "SMT Line 2 - Pick & Place", "Health": 78, "Status": "🟡 Watch", "Next Maint": "5 days", "RUL": "1,200 hrs", "Risk": "Medium"},
            {"Machine": "Reflow Oven 1", "Health": 96, "Status": "🟢 Good", "Next Maint": "28 days", "RUL": "4,200 hrs", "Risk": "Low"},
            {"Machine": "Reflow Oven 2", "Health": 89, "Status": "🟢 Good", "Next Maint": "15 days", "RUL": "2,100 hrs", "Risk": "Low"},
            {"Machine": "AOI Station 1", "Health": 62, "Status": "🔴 Alert", "Next Maint": "Now", "RUL": "450 hrs", "Risk": "High"},
            {"Machine": "Solder Paste Printer", "Health": 91, "Status": "🟢 Good", "Next Maint": "18 days", "RUL": "3,100 hrs", "Risk": "Low"},
            {"Machine": "Flying Probe Tester", "Health": 85, "Status": "🟢 Good", "Next Maint": "10 days", "RUL": "1,850 hrs", "Risk": "Low"},
            {"Machine": "Wire Bonder", "Health": 72, "Status": "🟡 Watch", "Next Maint": "3 days", "RUL": "820 hrs", "Risk": "Medium"},
        ]
        
        health_cols = st.columns(4)
        healthy = sum(1 for e in equipment_health if e["Health"] >= 85)
        watch = sum(1 for e in equipment_health if 70 <= e["Health"] < 85)
        critical = sum(1 for e in equipment_health if e["Health"] < 70)
        health_cols[0].metric("🟢 Healthy", f"{healthy}", help="Health > 85%")
        health_cols[1].metric("🟡 Watch", f"{watch}", help="Health 70-85%")
        health_cols[2].metric("🔴 Critical", f"{critical}", help="Health < 70%")
        health_cols[3].metric("Avg Health", f"{sum(e['Health'] for e in equipment_health)//len(equipment_health)}%", "+2%")
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("##### 🏭 Equipment Health Status")
            health_df = pd.DataFrame(equipment_health)
            
            # Create health bar chart
            fig_health = px.bar(
                health_df.sort_values("Health"), 
                x="Health", y="Machine", orientation='h',
                color="Health",
                color_continuous_scale=[(0, "red"), (0.5, "yellow"), (1, "green")]
            )
            fig_health.add_vline(x=85, line_dash="dash", line_color="green", annotation_text="Healthy")
            fig_health.add_vline(x=70, line_dash="dash", line_color="orange", annotation_text="Watch")
            fig_health.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=350, showlegend=False)
            st.plotly_chart(fig_health, use_container_width=True)
        
        with col2:
            st.markdown("##### ⚠️ Maintenance Alerts")
            for eq in sorted(equipment_health, key=lambda x: x["Health"])[:3]:
                if eq["Health"] < 85:
                    color = "#FF4B4B" if eq["Health"] < 70 else "#FFA500"
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, {color}20, {color}10); 
                                border-left: 4px solid {color}; padding: 10px; margin: 5px 0; border-radius: 5px;">
                        <strong>{eq['Machine']}</strong><br/>
                        <small>Health: {eq['Health']}% | RUL: {eq['RUL']}</small><br/>
                        <small>Action: Maintenance in {eq['Next Maint']}</small>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Failure prediction
        st.subheader("📊 Failure Probability Forecast (Next 30 Days)")
        days = list(range(1, 31))
        fail_prob = pd.DataFrame({
            "Day": days,
            "AOI Station 1": [0.02 + i*0.025 for i in range(30)],
            "Wire Bonder": [0.01 + i*0.012 for i in range(30)],
            "SMT Line 2": [0.005 + i*0.008 for i in range(30)]
        })
        
        fig_fail = go.Figure()
        fig_fail.add_trace(go.Scatter(x=days, y=fail_prob["AOI Station 1"], name="AOI Station 1", 
                                      line=dict(color="red", width=2)))
        fig_fail.add_trace(go.Scatter(x=days, y=fail_prob["Wire Bonder"], name="Wire Bonder", 
                                      line=dict(color="orange", width=2)))
        fig_fail.add_trace(go.Scatter(x=days, y=fail_prob["SMT Line 2"], name="SMT Line 2", 
                                      line=dict(color=TELIT_BLUE, width=2)))
        fig_fail.add_hline(y=0.5, line_dash="dash", line_color="red", annotation_text="High Risk Threshold")
        fig_fail.update_layout(xaxis_title="Days from Now", yaxis_title="Failure Probability",
                              margin=dict(l=0, r=0, t=20, b=0), height=280)
        st.plotly_chart(fig_fail, use_container_width=True)
    
    # =================================================================
    # TAB 7: OPERATOR PERFORMANCE
    # =================================================================
    with dt_tab7:
        st.subheader("👷 Operator Performance Dashboard")
        
        # Shift summary
        shift_cols = st.columns(4)
        shift_cols[0].metric("Current Shift", "Day (A)", help="Active shift")
        shift_cols[1].metric("Operators On Floor", "24", help="Active operators")
        shift_cols[2].metric("Avg Efficiency", "94.2%", "+1.8%", help="Shift average")
        shift_cols[3].metric("Training Due", "3", help="Certifications expiring soon")
        
        st.markdown("---")
        
        # Operator performance table
        operator_data = [
            {"ID": "OP-101", "Name": "Chen Wei", "Station": "SMT Line 1", "Efficiency": 98.2, "Quality": 99.5, "Units": 342, "Cert Status": "🟢 Current"},
            {"ID": "OP-102", "Name": "Maria Santos", "Station": "SMT Line 2", "Efficiency": 96.5, "Quality": 99.2, "Units": 328, "Cert Status": "🟢 Current"},
            {"ID": "OP-103", "Name": "James Wilson", "Station": "Testing Bay 1", "Efficiency": 94.8, "Quality": 99.8, "Units": 412, "Cert Status": "🟢 Current"},
            {"ID": "OP-104", "Name": "Yuki Tanaka", "Station": "Reflow Oven", "Efficiency": 97.1, "Quality": 99.4, "Units": 355, "Cert Status": "🟡 Expiring"},
            {"ID": "OP-105", "Name": "Ahmed Hassan", "Station": "AOI Station", "Efficiency": 93.4, "Quality": 99.1, "Units": 398, "Cert Status": "🟢 Current"},
            {"ID": "OP-106", "Name": "Lisa Chen", "Station": "Wire Bonding", "Efficiency": 95.9, "Quality": 99.6, "Units": 287, "Cert Status": "🟢 Current"},
            {"ID": "OP-107", "Name": "Klaus Mueller", "Station": "Final Assembly", "Efficiency": 91.2, "Quality": 98.8, "Units": 265, "Cert Status": "🟡 Expiring"},
            {"ID": "OP-108", "Name": "Priya Patel", "Station": "Quality Lab", "Efficiency": 99.1, "Quality": 99.9, "Units": 520, "Cert Status": "🟢 Current"},
        ]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("##### 📊 Operator Performance Metrics")
            op_df = pd.DataFrame(operator_data)
            st.dataframe(op_df, use_container_width=True)
        
        with col2:
            st.markdown("##### 🏆 Top Performers (This Month)")
            top_3 = sorted(operator_data, key=lambda x: x["Efficiency"], reverse=True)[:3]
            for i, op in enumerate(top_3):
                medal = ["🥇", "🥈", "🥉"][i]
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {TELIT_BLUE}20, {TELIT_BLUE}10);
                            padding: 10px; margin: 5px 0; border-radius: 8px;">
                    <span style="font-size: 24px;">{medal}</span>
                    <strong>{op['Name']}</strong><br/>
                    <small>Efficiency: {op['Efficiency']}% | Quality: {op['Quality']}%</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Skill matrix
        st.subheader("📚 Skill & Certification Matrix")
        skills = ["SMT Operation", "Reflow Setup", "AOI Programming", "Testing", "Wire Bonding", "Quality Control"]
        skill_matrix = pd.DataFrame({
            "Operator": [op["Name"] for op in operator_data],
            "SMT Operation": ["✅", "✅", "⬜", "✅", "⬜", "✅", "⬜", "⬜"],
            "Reflow Setup": ["✅", "⬜", "⬜", "✅", "⬜", "⬜", "✅", "⬜"],
            "AOI Programming": ["⬜", "✅", "⬜", "⬜", "✅", "⬜", "⬜", "✅"],
            "Testing": ["✅", "✅", "✅", "⬜", "✅", "⬜", "✅", "✅"],
            "Wire Bonding": ["⬜", "⬜", "⬜", "⬜", "⬜", "✅", "⬜", "⬜"],
            "Quality Control": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"]
        })
        st.dataframe(skill_matrix, use_container_width=True)
    
    # =================================================================
    # TAB 8: TRACEABILITY LOOKUP
    # =================================================================
    with dt_tab8:
        st.subheader("🔬 Unit Traceability & Genealogy")
        
        # Search interface
        search_col1, search_col2, search_col3 = st.columns([2, 1, 1])
        with search_col1:
            serial_input = st.text_input("🔍 Enter Serial Number or Lot ID", value="ME310G1-W1-12847")
        with search_col2:
            search_type = st.selectbox("Search Type", ["Serial Number", "Lot ID", "Work Order"])
        with search_col3:
            st.write("")
            st.write("")
            search_btn = st.button("🔍 Search", use_container_width=True)
        
        if serial_input:
            st.markdown("---")
            
            # Unit info card
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10);
                        border-radius: 10px; padding: 20px; margin: 10px 0;">
                <h3 style="margin: 0;">📦 Unit: {serial_input}</h3>
                <div style="display: flex; gap: 40px; margin-top: 15px;">
                    <div><strong>Product:</strong> ME310G1-W1</div>
                    <div><strong>Work Order:</strong> WO-2024-12847</div>
                    <div><strong>Build Date:</strong> 2024-12-28</div>
                    <div><strong>Status:</strong> <span style="color: green;">✅ Shipped</span></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("##### 🧩 Component Genealogy")
                components = pd.DataFrame({
                    "Component": ["Qualcomm SDX55 Modem", "u-blox M10 GNSS", "Skyworks PA", "Murata Antenna", "Samsung Flash", "PCB Assembly"],
                    "Supplier Lot": ["QC-2024-A4521", "UB-2024-M8832", "SK-2024-P2341", "MU-2024-A9912", "SS-2024-F5521", "PCB-2024-12847"],
                    "Date Code": ["2448", "2447", "2446", "2448", "2445", "2449"],
                    "Verified": ["✅", "✅", "✅", "✅", "✅", "✅"]
                })
                st.dataframe(components, use_container_width=True)
            
            with col2:
                st.markdown("##### 🔄 Process History")
                process_history = pd.DataFrame({
                    "Step": ["1. SMT Assembly", "2. Reflow Solder", "3. AOI Inspection", "4. Programming", "5. RF Testing", "6. Final Test", "7. Packaging"],
                    "Station": ["SMT-L1", "RO-1", "AOI-1", "PRG-2", "RF-3", "FT-1", "PKG-2"],
                    "Operator": ["Chen Wei", "Auto", "Auto", "Maria Santos", "James Wilson", "Priya Patel", "Lisa Chen"],
                    "Time": ["08:15", "08:45", "08:52", "09:10", "09:35", "10:02", "10:15"],
                    "Result": ["✅", "✅", "✅", "✅", "✅", "✅", "✅"]
                })
                st.dataframe(process_history, use_container_width=True)
            
            # Test results
            st.markdown("##### 📊 Test Results Summary")
            test_cols = st.columns(5)
            test_cols[0].metric("RF Sensitivity", "-108 dBm", "Spec: -107", help="Better than spec")
            test_cols[1].metric("TX Power", "23.1 dBm", "Spec: 23±1", help="Within spec")
            test_cols[2].metric("Current Draw", "142 mA", "Spec: <150", help="Within spec")
            test_cols[3].metric("GNSS Fix Time", "28 sec", "Spec: <35", help="Within spec")
            test_cols[4].metric("Overall", "PASS", "All 47 tests passed")
            
            # Shipping info
            st.markdown("##### 🚚 Shipping & Customer Info")
            ship_cols = st.columns(4)
            ship_cols[0].metric("Customer", "Trimble Inc.")
            ship_cols[1].metric("Ship Date", "2024-12-28")
            ship_cols[2].metric("Carrier", "DHL Express")
            ship_cols[3].metric("Tracking", "1234567890")
    
    # =================================================================
    # TAB 9: PRODUCTION SIMULATOR
    # =================================================================
    with dt_tab9:
        st.subheader("🎮 Production What-If Simulator")
        
        st.markdown("""
        <div style="background: linear-gradient(135deg, #00A7E120, #0D2C5410); 
                    padding: 15px; border-radius: 10px; margin-bottom: 20px;">
            <strong>💡 Simulate different production scenarios</strong> to optimize throughput, 
            identify bottlenecks, and plan capacity. Adjust the parameters below to see projected outcomes.
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### ⚙️ Production Parameters")
            sim_lines = st.slider("Active SMT Lines", 1, 4, 2)
            sim_shifts = st.slider("Shifts per Day", 1, 3, 2)
            sim_efficiency = st.slider("Target Efficiency (%)", 70, 100, 92)
            sim_changeover = st.slider("Changeover Time (min)", 15, 60, 30)
            sim_product_mix = st.selectbox("Product Mix", ["Standard (ME310)", "High-Mix (Multiple)", "New Product (NPI)"])
        
        with col2:
            st.markdown("##### 📊 Scenario Constraints")
            sim_demand = st.number_input("Daily Demand (units)", 500, 5000, 2000)
            sim_operators = st.slider("Operators per Shift", 4, 12, 8)
            sim_maintenance = st.slider("Planned Maintenance (hrs/week)", 0, 24, 8)
            sim_defect_target = st.slider("Target Defect Rate (ppm)", 50, 500, 150)
        
        st.markdown("---")
        
        # Calculate simulation results
        base_capacity = sim_lines * 400 * (sim_efficiency / 100)
        shift_capacity = base_capacity * sim_shifts
        weekly_capacity = shift_capacity * 5 * (1 - sim_maintenance / (24 * 7))
        changeover_loss = sim_changeover * 2 / 480 if sim_product_mix == "High-Mix (Multiple)" else 0
        actual_capacity = shift_capacity * (1 - changeover_loss)
        
        utilization = min(100, (sim_demand / actual_capacity) * 100)
        bottleneck = "SMT Lines" if sim_lines < 2 else ("Operators" if sim_operators < 6 else "Testing")
        
        # Results display
        st.subheader("📈 Simulation Results")
        
        result_cols = st.columns(4)
        result_cols[0].metric("Daily Capacity", f"{int(actual_capacity)}", 
                             f"{'+' if actual_capacity > sim_demand else ''}{int(actual_capacity - sim_demand)} vs demand")
        result_cols[1].metric("Utilization", f"{utilization:.1f}%", 
                             "⚠️ Over capacity" if utilization > 95 else "✅ Healthy")
        result_cols[2].metric("Weekly Output", f"{int(weekly_capacity)}", 
                             f"×5 days")
        result_cols[3].metric("Bottleneck", bottleneck, 
                             "Limiting factor")
        
        # Capacity visualization
        cap_col1, cap_col2 = st.columns(2)
        
        with cap_col1:
            st.markdown("##### 📊 Capacity vs Demand")
            fig_cap = go.Figure()
            fig_cap.add_trace(go.Bar(x=["Capacity", "Demand"], y=[actual_capacity, sim_demand],
                                    marker_color=[TELIT_BLUE, '#FF6B6B' if sim_demand > actual_capacity else '#4ECDC4']))
            fig_cap.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=250)
            st.plotly_chart(fig_cap, use_container_width=True)
        
        with cap_col2:
            st.markdown("##### 🔄 Capacity Breakdown")
            breakdown = pd.DataFrame({
                "Factor": ["Base Capacity", "Efficiency Loss", "Changeover Loss", "Maintenance Loss"],
                "Impact": [sim_lines * 400 * sim_shifts, 
                          -sim_lines * 400 * sim_shifts * (1 - sim_efficiency/100),
                          -base_capacity * sim_shifts * changeover_loss,
                          -weekly_capacity * sim_maintenance / (24 * 7) / 5]
            })
            fig_breakdown = px.bar(breakdown, x="Factor", y="Impact", 
                                  color="Impact",
                                  color_continuous_scale=[(0, "red"), (0.5, "gray"), (1, "green")])
            fig_breakdown.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=250, showlegend=False)
            st.plotly_chart(fig_breakdown, use_container_width=True)
        
        # Recommendations
        st.markdown("##### 💡 AI Recommendations")
        recommendations = []
        if utilization > 95:
            recommendations.append(("🔴", "Capacity shortage! Consider adding a shift or SMT line."))
        if sim_efficiency < 85:
            recommendations.append(("🟡", f"Efficiency at {sim_efficiency}% - investigate root causes for improvement."))
        if sim_product_mix == "High-Mix (Multiple)" and sim_changeover > 30:
            recommendations.append(("🟡", f"High changeover time ({sim_changeover}min) - implement SMED techniques."))
        if sim_operators < sim_lines * 3:
            recommendations.append(("🟡", "Operator shortage may limit throughput - consider cross-training."))
        if not recommendations:
            recommendations.append(("🟢", "Configuration looks optimal! Current settings meet demand efficiently."))
        
        for icon, rec in recommendations:
            st.markdown(f"{icon} {rec}")
    
    # =================================================================
    # TAB 10: ALERTS & ACTIONS
    # =================================================================
    with dt_tab10:
        # Alert Summary
        alert_summary = st.columns(4)
        alert_summary[0].metric("🔴 Critical", "1", "AOI fault")
        alert_summary[1].metric("🟡 Warnings", "3", "Inventory, Temp")
        alert_summary[2].metric("🔵 Info", "2", "Updates")
        alert_summary[3].metric("✅ Resolved (24h)", "5", "+2")
        
        st.markdown("---")
        
        # Active Alerts
        st.subheader("🚨 Active Alerts & Recommended Actions")
        alert_col1, alert_col2 = st.columns(2)
        
        with alert_col1:
            st.error("""
            **🔴 CRITICAL: AOI Station 2 - Vision System Fault**
            
            Camera calibration lost on 01005 component detection. 312 FN990A 5G modules in hold.
            
            **Root Cause:** Lens contamination from flux residue
            **Product Impact:** FN990A 5G modules (SDX62 fine-pitch BGA inspection blocked)
            **Action:** Technician M. Rossi dispatched. ETA: 15 min. Hold queue routed to AOI 3.
            """)
            
            st.warning("""
            **🟡 WARNING: Qualcomm SDX62 Inventory Low**
            
            890 units remaining (36% of line-side capacity). Consumption: 792/day
            
            **Supplier:** Qualcomm (Singapore fab)
            **Reorder Status:** PO #47823 in transit, ETA: Dec 26 (2,500 units)
            **Risk:** FN990A 5G production may halt in 27 hours without emergency order
            **Action:** Expedite shipment, contact Qualcomm account manager
            """)
        
        with alert_col2:
            st.warning("""
            **🟡 WARNING: Reflow Oven 2 - Temperature Deviation**
            
            Peak zone at 238°C (target: 245°C). Affects FN990A 5G module solder joints.
            
            **Risk:** Cold solder joints on SDX62 BGA (0.4mm pitch). RF performance impact.
            **Quality Hold:** Next 50 units require X-ray inspection for BGA voids
            **ETA to Spec:** 12 minutes (heater element stabilizing)
            """)
            
            st.info("""
            **🔵 INFO: RF Calibration Update Available**
            
            New R&S CMW500 firmware improves 5G NR FR1/FR2 test accuracy by 0.3dB
            
            **Applies to:** RF Test Chamber 1 & 2
            **Recommended:** Install during next maintenance window (Dec 26)
            **Impact:** Reduces FN990A test time by 8%, improves yield correlation
            """)
        
        st.markdown("---")
        
        # Recent Actions Log
        st.subheader("📋 Recent Actions Log")
        actions_log = pd.DataFrame({
            "Time": ["14:23", "13:45", "12:30", "11:15", "10:05"],
            "Type": ["🔴 Critical", "🟡 Warning", "✅ Resolved", "✅ Resolved", "🔵 Info"],
            "Issue": ["AOI 2 Vision Fault", "SMT Line 2 Pick Rate", "Reflow Oven 1 PM Complete", "RF Cal Drift Corrected", "Firmware v2.3.1 Released"],
            "Action Taken": ["Technician dispatched", "Feeder F-23 scheduled", "Back online", "Auto-recalibration", "Staged for ME310G1"],
            "Owner": ["M. Rossi", "L. Ferrari", "P. Bianchi", "System", "R&D Team"],
            "Status": ["In Progress", "Scheduled", "Complete", "Complete", "Ready"]
        })
        st.dataframe(actions_log, use_container_width=True)
    
    # =================================================================
    # TAB 6: AI RECOMMENDATIONS
    # =================================================================
    with dt_tab11:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🧠</span>
                <div>
                    <div style="font-size: 24px; font-weight: 700; color: white;">Snowflake Cortex AI Engine</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Real-time ML predictions powered by Snowpark ML | Models trained on 2.4M production records</div>
                </div>
                <div style="margin-left: auto; text-align: right;">
                    <div style="font-size: 28px; font-weight: 700; color: #00C48C;">97.3%</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px;">Avg Model Accuracy</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Model Performance KPIs
        model_cols = st.columns(5)
        models = [
            ("Predictive Maintenance", "98.2%", "XGBoost", "12min ago"),
            ("Yield Prediction", "96.8%", "LightGBM", "5min ago"),
            ("Demand Forecast", "94.5%", "Prophet", "1hr ago"),
            ("Anomaly Detection", "99.1%", "Isolation Forest", "Real-time"),
            ("Quality Prediction", "97.4%", "Neural Net", "8min ago"),
        ]
        for col, (name, acc, model, updated) in zip(model_cols, models):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 10px; padding: 12px; text-align: center; border: 1px solid #cbd5e1;">
                <div style="font-size: 11px; color: {TELIT_GRAY}; text-transform: uppercase;">{name}</div>
                <div style="font-size: 26px; font-weight: 700; color: {TELIT_GREEN}; margin: 8px 0;">{acc}</div>
                <div style="font-size: 10px; color: {TELIT_BLUE};">{model}</div>
                <div style="font-size: 9px; color: {TELIT_GRAY};">Updated: {updated}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # AI Recommendations with Priority
        st.subheader("🎯 AI-Generated Recommendations")
        
        rec_col1, rec_col2 = st.columns(2)
        
        with rec_col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_RED}15, {TELIT_RED}05); border-radius: 12px; padding: 18px; border-left: 5px solid {TELIT_RED}; margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <span style="background: {TELIT_RED}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: 600;">HIGH PRIORITY</span>
                        <div style="font-size: 16px; font-weight: 600; margin: 10px 0; color: #1E3A5F;">Replace AOI Station 2 Camera Module</div>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; line-height: 1.5;">
                            ML model predicts 78% probability of complete failure within 48 hours based on degradation pattern analysis. 
                            Current false rejection rate trending upward (was 2.1%, now 4.8%).
                        </div>
                    </div>
                </div>
                <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid {TELIT_RED}30; display: flex; gap: 20px; font-size: 12px;">
                    <div><span style="color: {TELIT_GRAY};">Confidence:</span> <strong>94.2%</strong></div>
                    <div><span style="color: {TELIT_GRAY};">Impact:</span> <strong style="color: {TELIT_RED};">$45K/day</strong></div>
                    <div><span style="color: {TELIT_GRAY};">Action Window:</span> <strong>48 hrs</strong></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05); border-radius: 12px; padding: 18px; border-left: 5px solid {TELIT_ORANGE}; margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <span style="background: {TELIT_ORANGE}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: 600;">MEDIUM PRIORITY</span>
                        <div style="font-size: 16px; font-weight: 600; margin: 10px 0; color: #1E3A5F;">Optimize FN990A 5G Reflow Profile</div>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; line-height: 1.5;">
                            Neural network analysis suggests increasing Zone 4 temperature by 3°C will improve BGA solder joint quality by 12%. 
                            Current FPY: 97.2% → Predicted: 98.5%.
                        </div>
                    </div>
                </div>
                <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid {TELIT_ORANGE}30; display: flex; gap: 20px; font-size: 12px;">
                    <div><span style="color: {TELIT_GRAY};">Confidence:</span> <strong>89.7%</strong></div>
                    <div><span style="color: {TELIT_GRAY};">Yield Gain:</span> <strong style="color: {TELIT_GREEN};">+1.3%</strong></div>
                    <div><span style="color: {TELIT_GRAY};">Est. Savings:</span> <strong>$28K/month</strong></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_BLUE}05); border-radius: 12px; padding: 18px; border-left: 5px solid {TELIT_BLUE}; margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <span style="background: {TELIT_BLUE}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px; font-weight: 600;">OPTIMIZATION</span>
                        <div style="font-size: 16px; font-weight: 600; margin: 10px 0; color: #1E3A5F;">Shift ME310G1 Production to Line 3</div>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; line-height: 1.5;">
                            Capacity optimization model recommends shifting 30% of ME310G1 volume from Line 1 to Line 3. 
                            Reduces bottleneck at RF Test by 18% through better load balancing.
                        </div>
                    </div>
                </div>
                <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid {TELIT_BLUE}30; display: flex; gap: 20px; font-size: 12px;">
                    <div><span style="color: {TELIT_GRAY};">Confidence:</span> <strong>91.3%</strong></div>
                    <div><span style="color: {TELIT_GRAY};">Throughput:</span> <strong style="color: {TELIT_GREEN};">+8%</strong></div>
                    <div><span style="color: {TELIT_GRAY};">Implementation:</span> <strong>2 hrs</strong></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with rec_col2:
            # Predictive Maintenance Chart
            st.subheader("🔧 Predictive Maintenance - Equipment Health")
            
            equipment = ["SMT Line 1", "SMT Line 2", "Reflow Oven 1", "Reflow Oven 2", "AOI Station 2", "RF Chamber 1"]
            health_score = [92, 78, 88, 71, 45, 95]
            days_to_failure = [45, 18, 32, 12, 2, 60]
            
            fig_health = go.Figure()
            fig_health.add_trace(go.Bar(
                x=equipment, y=health_score, name="Health Score",
                marker_color=[TELIT_GREEN if h > 80 else TELIT_ORANGE if h > 60 else TELIT_RED for h in health_score],
                text=[f"{h}%" for h in health_score], textposition="outside"
            ))
            fig_health.add_hline(y=70, line_dash="dash", line_color=TELIT_RED, annotation_text="Alert Threshold")
            fig_health.update_layout(
                height=250,
                margin=dict(l=20, r=20, t=10, b=40),
                yaxis_title="Health Score %",
                yaxis=dict(range=[0, 105])
            )
            st.plotly_chart(fig_health, use_container_width=True)
            
            # Days to predicted failure
            failure_cols = st.columns(6)
            for col, eq, days in zip(failure_cols, equipment, days_to_failure):
                color = TELIT_RED if days < 7 else TELIT_ORANGE if days < 21 else TELIT_GREEN
                col.markdown(f"""
                <div style="text-align: center; padding: 8px; background: {color}15; border-radius: 6px;">
                    <div style="font-size: 18px; font-weight: 700; color: {color};">{days}d</div>
                    <div style="font-size: 9px; color: {TELIT_GRAY};">to failure</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Demand Forecast & Anomaly Detection
        forecast_col, anomaly_col = st.columns(2)
        
        with forecast_col:
            st.subheader("📈 AI Demand Forecast - Next 12 Weeks")
            
            weeks = [f"W{i}" for i in range(1, 13)]
            actual = [12500, 13200, 12800, None, None, None, None, None, None, None, None, None]
            predicted = [12500, 13200, 12800, 14100, 15200, 14800, 13900, 14500, 15800, 16200, 15500, 14900]
            upper = [12500, 13200, 12800, 15200, 16500, 16100, 15200, 15900, 17400, 18000, 17200, 16500]
            lower = [12500, 13200, 12800, 13000, 13900, 13500, 12600, 13100, 14200, 14400, 13800, 13300]
            
            fig_forecast = go.Figure()
            fig_forecast.add_trace(go.Scatter(x=weeks, y=upper, fill=None, mode='lines', line=dict(color='rgba(0,167,225,0.1)'), name='Upper 95%'))
            fig_forecast.add_trace(go.Scatter(x=weeks, y=lower, fill='tonexty', mode='lines', line=dict(color='rgba(0,167,225,0.1)'), fillcolor='rgba(0,167,225,0.2)', name='Confidence'))
            fig_forecast.add_trace(go.Scatter(x=weeks, y=predicted, mode='lines+markers', name='Predicted', line=dict(color=TELIT_BLUE, width=2, dash='dash')))
            fig_forecast.add_trace(go.Scatter(x=weeks[:3], y=[12500, 13200, 12800], mode='lines+markers', name='Actual', line=dict(color=TELIT_GREEN, width=3)))
            fig_forecast.update_layout(
                height=280,
                margin=dict(l=20, r=20, t=10, b=40),
                legend=dict(orientation="h", yanchor="bottom", y=1.02),
                yaxis_title="Units/Week"
            )
            st.plotly_chart(fig_forecast, use_container_width=True)
            st.info("📊 **Forecast Insight:** 5G module demand (FN990A) expected to surge +28% in W5-W6 driven by automotive OEM orders. Recommend increasing SDX62 chipset buffer stock.")
        
        with anomaly_col:
            st.subheader("🔍 Anomaly Detection - Last 24 Hours")
            
            # Anomaly timeline
            anomaly_data = pd.DataFrame({
                "Time": ["06:23", "09:47", "11:15", "14:32", "16:58", "19:21"],
                "Equipment": ["SMT Line 2", "Reflow Oven 2", "AOI Station 2", "RF Chamber 1", "SMT Line 2", "Reflow Oven 2"],
                "Anomaly Type": ["Pick rate drop", "Temp variance", "Vision drift", "Cal shift", "Feeder jam", "Zone 3 spike"],
                "Severity": ["Medium", "Low", "High", "Low", "Medium", "Medium"],
                "Auto-Resolved": ["Yes", "Yes", "No", "Yes", "Yes", "No"]
            })
            
            severity_colors = {"High": TELIT_RED, "Medium": TELIT_ORANGE, "Low": TELIT_GREEN}
            
            for _, row in anomaly_data.iterrows():
                color = severity_colors[row["Severity"]]
                resolved = "✅" if row["Auto-Resolved"] == "Yes" else "⚠️"
                st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; background: {color}10; border-radius: 6px; margin-bottom: 6px; border-left: 3px solid {color};">
                    <span style="font-size: 11px; color: {TELIT_GRAY}; min-width: 45px;">{row["Time"]}</span>
                    <span style="font-size: 12px; font-weight: 600; min-width: 100px;">{row["Equipment"]}</span>
                    <span style="font-size: 12px; flex: 1;">{row["Anomaly Type"]}</span>
                    <span style="font-size: 11px; background: {color}; color: white; padding: 2px 8px; border-radius: 4px;">{row["Severity"]}</span>
                    <span>{resolved}</span>
                </div>
                """, unsafe_allow_html=True)
            
            st.caption("🤖 Isolation Forest model monitoring 847 sensor signals in real-time")
        
        st.markdown("---")
        
        # Feature Importance & Model Insights
        st.subheader("🧪 ML Model Insights - Yield Prediction Feature Importance")
        
        insight_col1, insight_col2, insight_col3 = st.columns([2, 1, 1])
        
        with insight_col1:
            features = ["Reflow Peak Temp", "Humidity %", "Solder Paste Age", "Component Placement Accuracy", "Conveyor Speed", "Operator Experience", "Batch Size", "Time of Day"]
            importance = [0.23, 0.18, 0.15, 0.14, 0.11, 0.09, 0.06, 0.04]
            
            fig_importance = go.Figure(go.Bar(
                x=importance, y=features, orientation='h',
                marker_color=[TELIT_BLUE if i < 3 else TELIT_GREEN for i in range(len(features))],
                text=[f"{i:.0%}" for i in importance], textposition="outside"
            ))
            fig_importance.update_layout(
                height=300,
                margin=dict(l=20, r=60, t=10, b=40),
                xaxis_title="Feature Importance",
                yaxis=dict(autorange="reversed")
            )
            st.plotly_chart(fig_importance, use_container_width=True)
        
        with insight_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); border-radius: 12px; padding: 18px; height: 280px;">
                <div style="font-size: 14px; font-weight: 600; color: {TELIT_GREEN}; margin-bottom: 12px;">✅ Model Performance</div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; line-height: 2;">
                    <div><strong>Algorithm:</strong> LightGBM</div>
                    <div><strong>Training Data:</strong> 2.4M records</div>
                    <div><strong>Features:</strong> 47 signals</div>
                    <div><strong>MAE:</strong> 0.32%</div>
                    <div><strong>R² Score:</strong> 0.94</div>
                    <div><strong>Last Retrained:</strong> Dec 20</div>
                    <div><strong>Next Retrain:</strong> Dec 27</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with insight_col3:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #667eea15, #764ba205); border-radius: 12px; padding: 18px; height: 280px;">
                <div style="font-size: 14px; font-weight: 600; color: #667eea; margin-bottom: 12px;">🎯 Key Insights</div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; line-height: 1.6;">
                    <div style="margin-bottom: 10px;">• <strong>Reflow temp</strong> is #1 predictor - maintain ±2°C tolerance</div>
                    <div style="margin-bottom: 10px;">• <strong>Humidity >55%</strong> correlates with 2.3x defect rate</div>
                    <div style="margin-bottom: 10px;">• <strong>Solder paste >4hrs</strong> degrades yield by 0.8%</div>
                    <div>• <strong>Night shift</strong> shows 0.4% lower yield - training opportunity</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # AI Actions Summary
        st.subheader("📋 AI-Recommended Actions Queue")
        actions_queue = pd.DataFrame({
            "Priority": ["🔴 Critical", "🟡 High", "🟡 High", "🔵 Medium", "🔵 Medium", "⚪ Low"],
            "Recommendation": [
                "Replace AOI Station 2 camera before failure",
                "Increase SDX62 buffer stock for Q1 demand surge",
                "Optimize FN990A reflow profile (+3°C Zone 4)",
                "Rebalance ME310G1 production to Line 3",
                "Schedule SMT Line 2 preventive maintenance",
                "Update RF chamber calibration firmware"
            ],
            "Model": ["Pred. Maint.", "Demand Fcst", "Yield Opt.", "Capacity Opt.", "Pred. Maint.", "Anomaly Det."],
            "Confidence": ["94.2%", "91.8%", "89.7%", "91.3%", "87.5%", "85.2%"],
            "Est. Impact": ["$45K saved", "$120K revenue", "+1.3% yield", "+8% throughput", "$12K saved", "+0.2% yield"],
            "Status": ["Pending Approval", "In Review", "Testing", "Approved", "Scheduled", "Backlog"]
        })
        st.dataframe(actions_queue, use_container_width=True)

# =============================================================================
# PAGE: INVENTORY
# =============================================================================
elif page == "📦 Inventory & Shipments":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">📦 Inventory & Shipments</h1>
        <p style="opacity: 0.8; color: white;">Real-time stock levels and shipment tracking across global network</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("Total Units", "285,000", "+5.2%"),
        ("Total Value", "$48.2M", "+3.8%"),
        ("Low Stock", "12", "-3"),
        ("Days Supply", "18.5", "+2.1"),
        ("In Transit", "1,247", "+8.2%"),
        ("Transit Value", "$12.4M", "+5.1%"),
        ("On-Time Ship", "95.8%", "+1.8%"),
        ("Inv Turns", "8.4x", "+0.6")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    inv_tab1, inv_tab2, inv_tab3, inv_tab4, inv_tab5, inv_tab6, inv_tab7, inv_tab8, inv_tab9, inv_tab10, inv_tab11 = st.tabs([
        "🌍 Overview",
        "📊 Stock",
        "🚚 Shipments",
        "🔄 Replenish",
        "🎯 Demand",
        "💰 Valuation",
        "📱 Orders",
        "🏭 MRP",
        "🌐 E2E View",
        "📈 Analytics",
        "🤖 AI"
    ])
    
    # =================================================================
    # TAB 1: OVERVIEW
    # =================================================================
    with inv_tab1:
        map_col, health_col = st.columns([2, 1])
        
        with map_col:
            st.subheader("🌍 Global Warehouse Network")
            warehouses = pd.DataFrame({
                'Warehouse': ['Los Angeles', 'Frankfurt', 'Shanghai', 'Singapore', 'Trieste'],
                'lat': [34.05, 50.11, 31.23, 1.35, 45.65],
                'lon': [-118.24, 8.68, 121.47, 103.82, 13.78],
                'Units': [45000, 42000, 55000, 38000, 65000],
                'Value': [8.2, 7.8, 12.4, 6.5, 13.3]
            })
            st.map(warehouses[['lat', 'lon']], zoom=1)
            
            # Warehouse cards
            wh_cols = st.columns(5)
            wh_data = [
                ("🇺🇸 Los Angeles", 45000, 78, "$8.2M"),
                ("🇩🇪 Frankfurt", 42000, 82, "$7.8M"),
                ("🇨🇳 Shanghai", 55000, 92, "$12.4M"),
                ("🇸🇬 Singapore", 38000, 75, "$6.5M"),
                ("🇮🇹 Trieste (HQ)", 65000, 68, "$13.3M"),
            ]
            for col, (name, units, util, value) in zip(wh_cols, wh_data):
                color = TELIT_GREEN if util < 80 else TELIT_ORANGE if util < 90 else TELIT_RED
                col.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 10px; padding: 12px; text-align: center; border: 1px solid {color}30;">
                    <div style="font-size: 12px; font-weight: 600;">{name}</div>
                    <div style="font-size: 20px; font-weight: 700; color: {TELIT_BLUE};">{units:,}</div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">{util}% full | {value}</div>
                </div>
                """, unsafe_allow_html=True)
        
        with health_col:
            st.subheader("📊 Inventory Health")
            
            # Donut chart
            health_labels = ["Healthy", "Low Stock", "Overstock", "Critical"]
            health_values = [72, 15, 8, 5]
            health_colors = [TELIT_GREEN, TELIT_ORANGE, TELIT_BLUE, TELIT_RED]
            
            fig_health = go.Figure(go.Pie(
                labels=health_labels, values=health_values, hole=0.6,
                marker_colors=health_colors, textinfo="percent+label"
            ))
            fig_health.add_annotation(text="<b>72%</b><br>Healthy", x=0.5, y=0.5, font_size=16, showarrow=False)
            fig_health.update_layout(height=250, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_health, use_container_width=True)
            
            st.metric("Inventory Accuracy", "99.2%", "+0.3%")
            st.metric("Cycle Count Variance", "$12,400", "-$2,100")
        
        st.markdown("---")
        
        # Product Family Overview
        st.subheader("📦 Inventory by Product Family")
        pf_cols = st.columns(5)
        product_families = [
            ("LTE-M Modules", "ME310G1", 78000, 42, TELIT_BLUE),
            ("5G Modules", "FN990A", 35000, 28, TELIT_GREEN),
            ("LTE Cat 4", "LE910C4", 62000, 38, TELIT_ORANGE),
            ("GNSS Modules", "SE868K3", 45000, 52, "#6B5B95"),
            ("Legacy 2G/3G", "CC864/HE910", 25000, 85, TELIT_GRAY),
        ]
        for col, (family, sku, units, dos, color) in zip(pf_cols, product_families):
            dos_color = TELIT_GREEN if dos > 30 else TELIT_ORANGE if dos > 14 else TELIT_RED
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 12px; padding: 15px; border-left: 4px solid {color};">
                <div style="font-size: 13px; font-weight: 600; color: {color};">{family}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{sku}</div>
                <div style="font-size: 26px; font-weight: 700; margin: 10px 0;">{units:,}</div>
                <div style="font-size: 12px; color: {dos_color};">📅 {dos} days supply</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Component/BOM Inventory
        st.subheader("🔧 Critical Component Inventory (BOM)")
        comp_cols = st.columns(6)
        components = [
            ("Qualcomm MDM9207", "ME310G1", 45000, 12, "wks", TELIT_BLUE),
            ("Qualcomm SDX62", "FN990A", 8500, 14, "wks", TELIT_ORANGE),
            ("Qualcomm MDM9615", "LE910C4", 52000, 10, "wks", TELIT_GREEN),
            ("u-blox M10", "SE868K3", 38000, 8, "wks", "#6B5B95"),
            ("Skyworks PA", "All RF", 125000, 6, "wks", TELIT_GRAY),
            ("Murata MLCC", "All", 2400000, 4, "wks", "#88B04B"),
        ]
        for col, (comp, product, qty, lt, unit, color) in zip(comp_cols, components):
            status = "🟢" if qty > 30000 or comp == "Murata MLCC" else "🟡" if qty > 10000 else "🔴"
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 10px; padding: 12px; text-align: center; border: 1px solid {color}30;">
                <div style="font-size: 10px; font-weight: 600; color: {color};">{comp}</div>
                <div style="font-size: 9px; color: {TELIT_GRAY};">for {product}</div>
                <div style="font-size: 20px; font-weight: 700; margin: 8px 0;">{status} {qty:,}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">Lead: {lt} {unit}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Customer Hub / Consignment Inventory
        st.subheader("🤝 Customer Hub Inventory (VMI)")
        hub_cols = st.columns(4)
        hubs = [
            ("🚗 BMW Group", "Munich Hub", "FN990A 5G", 4500, 2800, TELIT_BLUE),
            ("⚡ Landis+Gyr", "Atlanta Hub", "ME310G1", 8200, 6500, TELIT_GREEN),
            ("🚛 Continental", "Hanover Hub", "LE910C4", 3800, 2100, TELIT_ORANGE),
            ("💧 Itron", "Liberty Lake", "SE868K3", 5200, 4800, "#6B5B95"),
        ]
        for col, (customer, location, product, capacity, current, color) in zip(hub_cols, hubs):
            pct = int((current / capacity) * 100)
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 12px; padding: 15px; border-left: 4px solid {color};">
                <div style="font-size: 14px; font-weight: 600; color: {color};">{customer}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{location} • {product}</div>
                <div style="font-size: 24px; font-weight: 700; margin: 10px 0;">{current:,}</div>
                <div style="background: #e0e5ec; border-radius: 4px; height: 8px; overflow: hidden; margin: 8px 0;">
                    <div style="background: {color}; width: {pct}%; height: 100%;"></div>
                </div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{pct}% of {capacity:,} capacity</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 2: STOCK LEVELS
    # =================================================================
    with inv_tab2:
        st.subheader("📊 Stock Levels by Product")
        
        # Product inventory table
        products = pd.DataFrame({
            "SKU": ["ME310G1-W1", "ME310G1-WW", "FN990A28-W1", "FN990A28-EU", "LE910C4-NF", "LE910C4-EU", "SE868K3-A", "CC864-DUAL"],
            "Product": ["ME310G1 LTE-M NA", "ME310G1 LTE-M Global", "FN990A 5G NA", "FN990A 5G EU", "LE910C4 LTE NA", "LE910C4 LTE EU", "SE868K3 GNSS", "CC864 2G Legacy"],
            "Los Angeles": [12500, 8200, 4500, 1200, 15000, 3200, 8500, 6200],
            "Frankfurt": [3200, 9800, 1800, 8500, 4200, 12500, 7200, 5100],
            "Shanghai": [8500, 12000, 6200, 4800, 9500, 8200, 14000, 8500],
            "Singapore": [6200, 7500, 3800, 2100, 8200, 5400, 9200, 4200],
            "Total": [30400, 37500, 16300, 16600, 36900, 29300, 38900, 24000],
            "Reorder Point": [25000, 30000, 15000, 15000, 30000, 25000, 35000, 20000],
            "Status": ["🟢 OK", "🟢 OK", "🟡 Low", "🟡 Low", "🟢 OK", "🟢 OK", "🟢 OK", "🟢 OK"]
        })
        st.dataframe(products, use_container_width=True)
        
        st.markdown("---")
        
        # Stock visualization
        stock_col1, stock_col2 = st.columns(2)
        
        with stock_col1:
            st.subheader("📈 Stock vs Reorder Point")
            fig_stock = go.Figure()
            fig_stock.add_trace(go.Bar(name="Current Stock", x=products["SKU"], y=products["Total"], marker_color=TELIT_BLUE))
            fig_stock.add_trace(go.Scatter(name="Reorder Point", x=products["SKU"], y=products["Reorder Point"], mode="lines+markers", line=dict(color=TELIT_RED, dash="dash")))
            fig_stock.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=60), barmode="group", xaxis_tickangle=-45)
            st.plotly_chart(fig_stock, use_container_width=True)
        
        with stock_col2:
            st.subheader("🏭 Stock by Warehouse")
            fig_wh = go.Figure()
            for wh, color in [("Los Angeles", TELIT_BLUE), ("Frankfurt", TELIT_GREEN), ("Shanghai", TELIT_ORANGE), ("Singapore", "#6B5B95")]:
                fig_wh.add_trace(go.Bar(name=wh, x=products["SKU"][:5], y=products[wh][:5], marker_color=color))
            fig_wh.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=60), barmode="stack", xaxis_tickangle=-45)
            st.plotly_chart(fig_wh, use_container_width=True)
        
        st.markdown("---")
        
        # Certification Matrix
        st.subheader("📡 Carrier & Regional Certification Matrix")
        cert_data = pd.DataFrame({
            "SKU": ["ME310G1-W1", "ME310G1-EU", "FN990A28-W1", "FN990A28-EU", "LE910C4-NF", "LE910C4-EU"],
            "FCC": ["✅", "—", "✅", "—", "✅", "—"],
            "CE": ["—", "✅", "—", "✅", "—", "✅"],
            "PTCRB": ["✅", "—", "✅", "—", "✅", "—"],
            "AT&T": ["✅", "—", "✅", "—", "✅", "—"],
            "Verizon": ["✅", "—", "✅", "—", "✅", "—"],
            "T-Mobile": ["✅", "—", "✅", "—", "✅", "—"],
            "Vodafone": ["—", "✅", "—", "✅", "—", "✅"],
            "DT": ["—", "✅", "—", "✅", "—", "✅"],
            "Stock": ["30,400", "18,200", "16,300", "16,600", "36,900", "29,300"]
        })
        st.dataframe(cert_data, use_container_width=True)
        
        # Regional stock breakdown
        st.subheader("🌐 Regional Variant Inventory")
        region_cols = st.columns(3)
        regions = [
            ("🇺🇸 Americas (NA)", "FCC/PTCRB Certified", 145000, ["AT&T", "Verizon", "T-Mobile", "Rogers"], TELIT_BLUE),
            ("🇪🇺 EMEA (EU)", "CE/RED Certified", 98000, ["Vodafone", "DT", "Orange", "Telefonica"], TELIT_GREEN),
            ("🌏 APAC", "Regional Certified", 72000, ["NTT", "Telstra", "Singtel", "China Mobile"], TELIT_ORANGE),
        ]
        for col, (region, cert, stock, carriers, color) in zip(region_cols, regions):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 12px; padding: 18px; border-top: 4px solid {color};">
                <div style="font-size: 18px; font-weight: 700; color: {color};">{region}</div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; margin: 5px 0;">{cert}</div>
                <div style="font-size: 32px; font-weight: 700; margin: 15px 0;">{stock:,}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">
                    <strong>Carriers:</strong> {", ".join(carriers)}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Firmware Version Inventory
        st.subheader("💾 Inventory by Firmware Version")
        fw_col1, fw_col2 = st.columns(2)
        
        with fw_col1:
            fw_versions = ["v25.00.123", "v25.00.122", "v24.10.456", "v24.10.455", "v24.00.789"]
            fw_stock = [95000, 45000, 32000, 18000, 5000]
            fw_status = ["Current", "Previous", "Stable", "Legacy", "EOL"]
            
            fig_fw = go.Figure(go.Bar(
                x=fw_versions, y=fw_stock,
                marker_color=[TELIT_GREEN, TELIT_BLUE, TELIT_BLUE, TELIT_ORANGE, TELIT_RED],
                text=[f"{s:,}" for s in fw_stock], textposition="outside"
            ))
            fig_fw.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=60), xaxis_title="Firmware Version", yaxis_title="Units")
            st.plotly_chart(fig_fw, use_container_width=True)
        
        with fw_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 16px; font-weight: 600; margin-bottom: 15px;">📋 Firmware Status</div>
                <div style="margin-bottom: 10px;">
                    <span style="background: {TELIT_GREEN}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px;">CURRENT</span>
                    <span style="margin-left: 10px;">v25.00.123 - 95,000 units</span>
                </div>
                <div style="margin-bottom: 10px;">
                    <span style="background: {TELIT_BLUE}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px;">STABLE</span>
                    <span style="margin-left: 10px;">v25.00.122 / v24.10.456 - 77,000 units</span>
                </div>
                <div style="margin-bottom: 10px;">
                    <span style="background: {TELIT_ORANGE}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px;">LEGACY</span>
                    <span style="margin-left: 10px;">v24.10.455 - 18,000 units</span>
                </div>
                <div style="margin-bottom: 10px;">
                    <span style="background: {TELIT_RED}; color: white; padding: 3px 10px; border-radius: 4px; font-size: 11px;">EOL</span>
                    <span style="margin-left: 10px;">v24.00.789 - 5,000 units (upgrade required)</span>
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: {TELIT_GRAY};">
                    ⚠️ 5,000 units require firmware upgrade before shipment
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 3: SHIPMENTS
    # =================================================================
    with inv_tab3:
        st.subheader("🗺️ Live Shipment Tracking")
        
        # Shipment map
        import plotly.express as px
        shipments_data = pd.DataFrame({
            'Shipment': ['SHP-10001', 'SHP-10002', 'SHP-10003', 'SHP-10004', 'SHP-10005'],
            'lat': [35.5, 48.2, 22.3, 1.3, 45.6],
            'lon': [-100.5, 5.5, 114.2, 103.8, 13.8],
            'Origin': ['Shanghai', 'Trieste', 'Singapore', 'Singapore', 'Trieste'],
            'Destination': ['Los Angeles', 'Munich', 'Tokyo', 'Shanghai', 'Tel Aviv'],
            'Status': ['In Transit', 'In Transit', 'At Hub', 'Delivered', 'In Transit'],
            'Product': ['FN990A 5G', 'ME310G1', 'LE910C4', 'SE868K3', 'FN990A 5G'],
            'Units': [5000, 8000, 3500, 4200, 2800],
            'Value': ['$625K', '$208K', '$147K', '$78K', '$350K']
        })
        
        fig_map = px.scatter_mapbox(
            shipments_data, lat='lat', lon='lon', 
            color='Status', hover_name='Shipment',
            hover_data=['Origin', 'Destination', 'Product', 'Units', 'Value'],
            color_discrete_map={'In Transit': TELIT_BLUE, 'At Hub': TELIT_ORANGE, 'Delivered': TELIT_GREEN},
            zoom=1, mapbox_style="carto-positron", size_max=15
        )
        fig_map.update_layout(height=350, margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)
        
        # Shipment KPIs
        ship_kpis = st.columns(5)
        ship_metrics = [
            ("Active Shipments", "1,247", "+8.2%"),
            ("In Transit", "847", "68%"),
            ("At Customs", "156", "12.5%"),
            ("Delivered Today", "89", "+15"),
            ("Avg Transit Time", "4.2 days", "-0.3 days")
        ]
        for col, (label, value, delta) in zip(ship_kpis, ship_metrics):
            col.metric(label, value, delta)
        
        st.markdown("---")
        
        # Shipment table
        st.subheader("📋 Active Shipments")
        shipment_table = pd.DataFrame({
            "Shipment ID": ["SHP-10001", "SHP-10002", "SHP-10003", "SHP-10004", "SHP-10005", "SHP-10006"],
            "Origin": ["Shanghai DC", "Trieste HQ", "Singapore Hub", "Singapore Hub", "Trieste HQ", "Shanghai DC"],
            "Destination": ["Los Angeles", "Munich Hub", "Tokyo DC", "Shanghai DC", "Tel Aviv R&D", "Irvine (Americas)"],
            "Customer": ["Internal Transfer", "BMW Group", "NTT DoCoMo", "Internal Transfer", "Internal Transfer", "Landis+Gyr"],
            "Product": ["FN990A 5G", "ME310G1", "LE910C4", "SE868K3", "FN990A 5G", "ME310G1"],
            "Units": [5000, 8000, 3500, 4200, 2800, 12000],
            "Carrier": ["Maersk", "DHL Express", "FedEx", "SF Express", "DHL Express", "Kuehne+Nagel"],
            "Status": ["🚢 Ocean Transit", "✈️ Air Freight", "📦 At Hub", "✅ Delivered", "✈️ Air Freight", "🚢 Ocean Transit"],
            "ETA": ["Jan 5", "Dec 28", "Dec 27", "Dec 24", "Dec 29", "Jan 8"],
            "Value": ["$625K", "$208K", "$147K", "$78K", "$350K", "$312K"]
        })
        st.dataframe(shipment_table, use_container_width=True)
        
        st.markdown("---")
        
        # Shipment analytics
        ship_col1, ship_col2 = st.columns(2)
        
        with ship_col1:
            st.subheader("📊 Shipments by Status")
            status_data = pd.DataFrame({
                'Status': ['In Transit', 'At Customs', 'At Hub', 'Out for Delivery', 'Delivered'],
                'Count': [847, 156, 124, 31, 89]
            })
            fig_status = px.pie(status_data, values='Count', names='Status', hole=0.5,
                               color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, '#6B5B95', TELIT_GREEN, TELIT_GRAY])
            fig_status.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_status, use_container_width=True)
        
        with ship_col2:
            st.subheader("📈 On-Time Delivery Trend")
            months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            otd_rate = [92.1, 93.5, 91.8, 94.2, 95.1, 94.7]
            fig_otd = go.Figure()
            fig_otd.add_trace(go.Scatter(x=months, y=otd_rate, mode='lines+markers', 
                                         line=dict(color=TELIT_BLUE, width=3), marker=dict(size=10)))
            fig_otd.add_hline(y=95, line_dash="dash", line_color=TELIT_GREEN, annotation_text="Target: 95%")
            fig_otd.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="OTD %", yaxis=dict(range=[88, 100]))
            st.plotly_chart(fig_otd, use_container_width=True)
        
        # Carrier performance
        st.subheader("🚚 Carrier Performance")
        carrier_data = pd.DataFrame({
            "Carrier": ["DHL Express", "FedEx", "Maersk", "Kuehne+Nagel", "SF Express"],
            "Shipments YTD": [342, 287, 198, 156, 89],
            "On-Time %": ["96.2%", "94.8%", "92.1%", "95.5%", "97.1%"],
            "Avg Transit": ["3.2 days", "3.8 days", "18.5 days", "5.2 days", "2.1 days"],
            "Damage Rate": ["0.02%", "0.05%", "0.08%", "0.03%", "0.01%"],
            "Cost Index": ["1.00", "0.95", "0.45", "0.72", "0.88"],
            "Rating": ["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]
        })
        st.dataframe(carrier_data, use_container_width=True)
    
    # =================================================================
    # TAB 4: REPLENISHMENT
    # =================================================================
    with inv_tab4:
        st.subheader("⚠️ Low Stock Alerts - Action Required")
        
        # Critical alerts
        alerts = [
            ("🔴", "FN990A28-W1", "5G NA Module", "Shanghai", 4500, 15000, 8, "Critical - Order NOW"),
            ("🔴", "FN990A28-EU", "5G EU Module", "Frankfurt", 8500, 15000, 12, "Critical - Below safety"),
            ("🟡", "ME310G1-W1", "LTE-M NA", "Los Angeles", 12500, 25000, 18, "Warning - Monitor"),
            ("🟡", "LE910C4-NF", "LTE Cat 4 NA", "Singapore", 8200, 12000, 21, "Warning - Reorder soon"),
        ]
        
        for icon, sku, name, wh, current, reorder, dos, status in alerts:
            color = TELIT_RED if icon == "🔴" else TELIT_ORANGE
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 12px; padding: 15px; margin-bottom: 10px; border-left: 5px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="font-size: 18px;">{icon}</span>
                        <span style="font-size: 16px; font-weight: 600; margin-left: 10px;">{sku}</span>
                        <span style="color: {TELIT_GRAY}; margin-left: 10px;">{name} @ {wh}</span>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-size: 22px; font-weight: 700; color: {color};">{current:,}</span>
                        <span style="color: {TELIT_GRAY};"> / {reorder:,}</span>
                        <div style="font-size: 12px; color: {TELIT_GRAY};">{dos} days supply | {status}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Replenishment schedule
        rep_col1, rep_col2 = st.columns(2)
        
        with rep_col1:
            st.subheader("📅 Pending Purchase Orders")
            po_data = pd.DataFrame({
                "PO #": ["PO-47823", "PO-47824", "PO-47825", "PO-47826"],
                "SKU": ["FN990A28-W1", "ME310G1-WW", "LE910C4-EU", "SE868K3-A"],
                "Quantity": [5000, 8000, 6000, 4000],
                "Supplier": ["Qualcomm", "Qualcomm", "Qualcomm", "u-blox"],
                "ETA": ["Dec 26", "Dec 28", "Jan 2", "Jan 5"],
                "Status": ["🚚 In Transit", "🚚 In Transit", "📦 Shipped", "⏳ Processing"]
            })
            st.dataframe(po_data, use_container_width=True)
        
        with rep_col2:
            st.subheader("📊 Safety Stock Analysis")
            safety_products = ["ME310G1", "FN990A", "LE910C4", "SE868K3", "CC864"]
            current_ss = [95, 62, 88, 105, 120]
            target_ss = [100, 100, 100, 100, 100]
            
            fig_safety = go.Figure()
            colors_ss = [TELIT_GREEN if c >= 90 else TELIT_ORANGE if c >= 70 else TELIT_RED for c in current_ss]
            fig_safety.add_trace(go.Bar(x=safety_products, y=current_ss, marker_color=colors_ss, text=[f"{c}%" for c in current_ss], textposition="outside"))
            fig_safety.add_hline(y=100, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target")
            fig_safety.add_hline(y=70, line_dash="dot", line_color=TELIT_RED, annotation_text="Critical")
            fig_safety.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="% of Target", yaxis=dict(range=[0, 130]))
            st.plotly_chart(fig_safety, use_container_width=True)
        
        st.markdown("---")
        
        # Quality Hold Inventory
        st.subheader("🚫 Quality Hold & RMA Inventory")
        qh_col1, qh_col2 = st.columns([2, 1])
        
        with qh_col1:
            hold_data = pd.DataFrame({
                "Hold ID": ["QH-2024-0892", "QH-2024-0891", "QH-2024-0890", "RMA-12847", "RMA-12846"],
                "SKU": ["FN990A28-W1", "ME310G1-WW", "LE910C4-NF", "FN990A28-EU", "SE868K3-A"],
                "Quantity": [312, 450, 180, 85, 42],
                "Reason": ["RF cal drift", "Firmware issue", "Visual defect", "Customer return", "DOA"],
                "Location": ["Shanghai", "Trieste", "Frankfurt", "Frankfurt", "Singapore"],
                "Hold Date": ["Dec 21", "Dec 20", "Dec 19", "Dec 18", "Dec 17"],
                "Status": ["🔬 Under Review", "🔧 Rework", "⏳ Pending", "📋 RMA Process", "🗑️ Scrap"],
                "Value": ["$28K", "$18K", "$9K", "$8K", "$2K"]
            })
            st.dataframe(hold_data, use_container_width=True)
        
        with qh_col2:
            # Quality hold summary
            hold_reasons = ["RF Issues", "Firmware", "Visual", "RMA", "Other"]
            hold_qty = [312, 450, 180, 127, 45]
            
            fig_hold = go.Figure(go.Pie(
                labels=hold_reasons, values=hold_qty, hole=0.5,
                marker_colors=[TELIT_RED, TELIT_ORANGE, TELIT_BLUE, "#6B5B95", TELIT_GRAY]
            ))
            fig_hold.add_annotation(text="<b>1,114</b><br>units", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_hold.update_layout(height=200, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_hold, use_container_width=True)
            
            st.metric("Total Hold Value", "$65K", "-$12K vs last week")
            st.metric("Avg Hold Duration", "4.2 days", "-0.8 days")
        
        st.markdown("---")
        
        # Date Code / Shelf Life
        st.subheader("⏳ Date Code & Shelf Life Tracking")
        shelf_cols = st.columns(4)
        shelf_data = [
            ("MSL 3 Components", "< 168 hrs exposure", 45000, 38, TELIT_GREEN),
            ("Solder Paste", "Expires in 14 days", 85, 12, TELIT_ORANGE),
            ("Flux (IPA)", "Expires in 30 days", 120, 28, TELIT_GREEN),
            ("Date Code > 2yrs", "Priority shipment", 8500, 100, TELIT_RED),
        ]
        for col, (item, status, qty, days, color) in zip(shelf_cols, shelf_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 10px; padding: 15px; text-align: center; border: 1px solid {color}30;">
                <div style="font-size: 12px; font-weight: 600; color: {color};">{item}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY}; margin: 5px 0;">{status}</div>
                <div style="font-size: 22px; font-weight: 700;">{qty:,}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{days} days remaining</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 5: DEMAND SENSING
    # =================================================================
    with inv_tab5:
        st.subheader("🎯 Real-Time Demand Intelligence")
        
        # Demand signals header
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">📡 Demand Signal Processing</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">Aggregating signals from EDI, APIs, POS data & market intelligence</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Last Updated</div>
                    <div style="font-size: 18px; font-weight: 600; color: {TELIT_GREEN};">🟢 Real-time</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Demand KPIs
        demand_kpis = st.columns(5)
        demand_kpis[0].metric("Demand This Week", "42,500", "+8.2%", help="Total units demanded")
        demand_kpis[1].metric("Forecast Accuracy", "87.3%", "+2.1%", help="Last 4 weeks MAPE")
        demand_kpis[2].metric("Demand vs Supply Gap", "-3,200", "⚠️ Short", help="Negative = shortage")
        demand_kpis[3].metric("Active Design Wins", "47", "+12 YTD", help="Producing demand signals")
        demand_kpis[4].metric("Customer Forecasts", "18", "EDI feeds", help="Active customer EDI")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Demand Signals by Source")
            signal_sources = pd.DataFrame({
                "Source": ["Customer EDI", "Design Win Pipeline", "Distributor POS", "Market Intelligence", "Historical Pattern"],
                "Volume (units)": [28500, 8200, 3500, 1800, 500],
                "Confidence": ["95%", "75%", "85%", "60%", "90%"],
                "Lead Time": ["2-4 weeks", "3-6 months", "1-2 weeks", "6-12 months", "N/A"]
            })
            
            fig_signals = px.pie(signal_sources, values="Volume (units)", names="Source",
                                color_discrete_sequence=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#6B5B95', TELIT_GRAY])
            fig_signals.update_traces(textposition='inside', textinfo='percent+label')
            fig_signals.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_signals, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Demand Trend (12 Weeks)")
            weeks = [f"W{i}" for i in range(1, 13)]
            actual_demand = [38500, 41200, 39800, 42500, 44100, 43200, 45800, 42300, 44500, 43800, 42500, None]
            forecast_demand = [39000, 40500, 41000, 42000, 43500, 44000, 45000, 43500, 44000, 43500, 43000, 44500]
            
            fig_demand = go.Figure()
            fig_demand.add_trace(go.Scatter(x=weeks, y=actual_demand, name="Actual", 
                                           line=dict(color=TELIT_BLUE, width=3), mode='lines+markers'))
            fig_demand.add_trace(go.Scatter(x=weeks, y=forecast_demand, name="Forecast",
                                           line=dict(color=TELIT_ORANGE, width=2, dash='dash'), mode='lines'))
            fig_demand.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), 
                                    yaxis_title="Units", legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_demand, use_container_width=True)
        
        # Customer demand breakdown
        st.markdown("##### 🏢 Top Customer Demand Signals")
        customer_demand = pd.DataFrame({
            "Customer": ["BMW Group", "Landis+Gyr", "Itron", "Continental", "Trimble", "Honeywell", "Delphi", "Bosch"],
            "Product": ["FN990A 5G", "ME310G1", "ME310G1", "LE910C4", "SE868K3", "ME310G1", "FN990A 5G", "LE910C4"],
            "Q1 Forecast": [12000, 18000, 15000, 8500, 6200, 9500, 4800, 7200],
            "Q2 Forecast": [15000, 20000, 16500, 9200, 7500, 10200, 6500, 8100],
            "Trend": ["📈 +25%", "📈 +11%", "📈 +10%", "📈 +8%", "📈 +21%", "📈 +7%", "📈 +35%", "📈 +12%"],
            "Confidence": ["🟢 High", "🟢 High", "🟢 High", "🟢 High", "🟡 Medium", "🟢 High", "🟡 Medium", "🟢 High"],
            "Source": ["EDI", "EDI", "EDI", "EDI", "Forecast", "EDI", "Design Win", "EDI"]
        })
        st.dataframe(customer_demand, use_container_width=True)
        
        st.markdown("---")
        
        # Market intelligence
        st.markdown("##### 🌐 Market Intelligence & Trends")
        market_cols = st.columns(4)
        market_data = [
            ("📱 5G IoT Adoption", "+42% YoY", "Automotive & Industrial leading adoption", TELIT_GREEN),
            ("⚡ Smart Meter Rollout", "Q4 Peak", "US/EU infrastructure bill deployments", TELIT_BLUE),
            ("🚗 Automotive Telematics", "+18% YoY", "Connected car mandates driving growth", TELIT_ORANGE),
            ("🏭 Industry 4.0", "+28% YoY", "Factory automation expanding rapidly", "#6B5B95"),
        ]
        for col, (trend, growth, desc, color) in zip(market_cols, market_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); 
                        border-radius: 10px; padding: 15px; border-left: 4px solid {color}; height: 140px;">
                <div style="font-size: 13px; font-weight: 600; color: {color};">{trend}</div>
                <div style="font-size: 24px; font-weight: 700; margin: 8px 0;">{growth}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Seasonality patterns
        st.markdown("##### 📅 Demand Seasonality Patterns")
        season_col1, season_col2 = st.columns(2)
        
        with season_col1:
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            seasonality = [85, 88, 95, 100, 105, 98, 92, 95, 110, 120, 115, 95]
            
            fig_season = go.Figure()
            fig_season.add_trace(go.Bar(x=months, y=seasonality, 
                                       marker_color=[TELIT_BLUE if s < 100 else TELIT_GREEN if s < 110 else TELIT_ORANGE for s in seasonality],
                                       text=[f"{s}%" for s in seasonality], textposition="outside"))
            fig_season.add_hline(y=100, line_dash="dash", line_color="gray", annotation_text="Baseline")
            fig_season.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="% of Average")
            st.plotly_chart(fig_season, use_container_width=True)
        
        with season_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 16px; font-weight: 600; margin-bottom: 15px;">📋 Key Seasonal Drivers</div>
                <div style="margin-bottom: 10px;">
                    <span style="font-size: 16px;">📈</span>
                    <strong>Q4 Peak (Oct-Nov):</strong> Smart meter deployments
                </div>
                <div style="margin-bottom: 10px;">
                    <span style="font-size: 16px;">🚗</span>
                    <strong>Q2 Ramp:</strong> Automotive production cycles
                </div>
                <div style="margin-bottom: 10px;">
                    <span style="font-size: 16px;">📉</span>
                    <strong>Q1 Low:</strong> Post-holiday slowdown, CNY impact
                </div>
                <div style="margin-bottom: 10px;">
                    <span style="font-size: 16px;">⚡</span>
                    <strong>Summer Dip:</strong> European factory closures
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 6: COST & VALUATION
    # =================================================================
    with inv_tab6:
        st.subheader("💰 Inventory Valuation & Cost Analysis")
        
        # Valuation summary
        val_kpis = st.columns(5)
        val_kpis[0].metric("Total Inventory Value", "$78.5M", "+$1.8M", help="At standard cost")
        val_kpis[1].metric("Carrying Cost (Annual)", "$5.8M", "-$0.3M", help="12% of inventory value")
        val_kpis[2].metric("Obsolescence Reserve", "$2.1M", "+$0.2M", help="For EOL/slow-moving")
        val_kpis[3].metric("Working Capital Tied", "$42.4M", "+$1.2M", help="Net inventory investment")
        val_kpis[4].metric("Days Inventory O/S", "52 days", "-3 days", help="DIO improvement")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Inventory Value by Category")
            categories = ["5G Modules", "LTE-M", "LTE Cat 4", "GNSS", "Legacy 2G/3G", "Components"]
            values = [15.8, 12.4, 8.5, 5.2, 3.1, 3.2]
            
            fig_val = go.Figure(go.Pie(
                labels=categories, values=values, hole=0.5,
                marker_colors=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#6B5B95', TELIT_GRAY, '#88B04B'],
                textinfo="label+percent"
            ))
            fig_val.add_annotation(text="<b>$48.2M</b><br>Total", x=0.5, y=0.5, font_size=16, showarrow=False)
            fig_val.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_val, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Carrying Cost Breakdown")
            cost_items = ["Capital Cost (8%)", "Storage & Handling", "Insurance", "Obsolescence", "Shrinkage"]
            cost_values = [3.86, 0.96, 0.48, 0.38, 0.12]
            
            fig_cost = go.Figure(go.Bar(
                x=cost_values, y=cost_items, orientation='h',
                marker_color=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, TELIT_RED, TELIT_GRAY],
                text=[f"${c}M" for c in cost_values], textposition="outside"
            ))
            fig_cost.update_layout(height=300, margin=dict(l=10, r=80, t=10, b=10), xaxis_title="$M / Year")
            st.plotly_chart(fig_cost, use_container_width=True)
        
        # Valuation by warehouse
        st.markdown("##### 🏭 Inventory Value by Warehouse")
        wh_val = pd.DataFrame({
            "Warehouse": ["🇮🇹 Trieste (HQ)", "🇨🇳 Shanghai", "🇺🇸 Los Angeles", "🇩🇪 Frankfurt", "🇸🇬 Singapore"],
            "Units": ["65,000", "55,000", "45,000", "42,000", "38,000"],
            "Value": ["$13.3M", "$12.4M", "$8.2M", "$7.8M", "$6.5M"],
            "Avg Cost/Unit": ["$204.62", "$225.45", "$182.22", "$185.71", "$171.05"],
            "Carrying Cost": ["$1.60M", "$1.49M", "$0.98M", "$0.94M", "$0.78M"],
            "Turns": ["7.2x", "9.8x", "8.4x", "7.8x", "6.5x"],
            "DIO": ["51 days", "37 days", "43 days", "47 days", "56 days"]
        })
        st.dataframe(wh_val, use_container_width=True)
        
        st.markdown("---")
        
        # Landed cost analysis
        st.markdown("##### 🚢 Landed Cost Analysis")
        landed_cols = st.columns(2)
        
        with landed_cols[0]:
            landed_breakdown = pd.DataFrame({
                "Cost Element": ["Product Cost (FOB)", "Ocean Freight", "Air Freight Premium", "Customs Duties", "Handling & Warehousing", "Insurance"],
                "% of Landed Cost": [78.5, 8.2, 5.1, 4.8, 2.5, 0.9],
                "Avg $/Unit": ["$168.45", "$17.60", "$10.95", "$10.30", "$5.37", "$1.93"]
            })
            st.dataframe(landed_breakdown, use_container_width=True)
        
        with landed_cols[1]:
            fig_landed = go.Figure(go.Waterfall(
                name="Landed Cost", orientation="v",
                measure=["absolute", "relative", "relative", "relative", "relative", "relative", "total"],
                x=["FOB Cost", "Freight", "Air Premium", "Duties", "Handling", "Insurance", "Landed Cost"],
                y=[168.45, 17.60, 10.95, 10.30, 5.37, 1.93, 0],
                text=["$168.45", "+$17.60", "+$10.95", "+$10.30", "+$5.37", "+$1.93", "$214.60"],
                textposition="outside",
                connector={"line": {"color": "rgb(63, 63, 63)"}}
            ))
            fig_landed.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=60), xaxis_tickangle=-30)
            st.plotly_chart(fig_landed, use_container_width=True)
        
        # Slow moving / obsolescence
        st.markdown("##### ⚠️ Slow-Moving & Obsolescence Risk")
        obs_cols = st.columns(4)
        obs_data = [
            ("0-90 Days", "$38.5M", "80%", TELIT_GREEN, "Active"),
            ("91-180 Days", "$6.2M", "13%", TELIT_BLUE, "Watch"),
            ("181-365 Days", "$2.4M", "5%", TELIT_ORANGE, "At Risk"),
            ("> 365 Days", "$1.1M", "2%", TELIT_RED, "Reserve"),
        ]
        for col, (age, value, pct, color, status) in zip(obs_cols, obs_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); 
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 4px solid {color};">
                <div style="font-size: 12px; font-weight: 600; color: {color};">{age}</div>
                <div style="font-size: 24px; font-weight: 700; margin: 8px 0;">{value}</div>
                <div style="font-size: 14px; color: {TELIT_GRAY};">{pct}</div>
                <div style="font-size: 11px; color: {color}; margin-top: 5px;">{status}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 7: CUSTOMER ORDERS
    # =================================================================
    with inv_tab7:
        st.subheader("📱 Customer Order Management")
        
        # Order KPIs
        order_kpis = st.columns(5)
        order_kpis[0].metric("Open Orders", "847", "+12", help="Active customer orders")
        order_kpis[1].metric("Order Value", "$28.5M", "+$2.1M", help="Total backlog value")
        order_kpis[2].metric("Shipped Today", "42", "+8", help="Orders shipped")
        order_kpis[3].metric("On-Time Promise", "95.8%", "+1.8%", help="Promise accuracy")
        order_kpis[4].metric("Avg Lead Time", "4.8 days", "-0.3 days", help="Order to ship")
        
        st.markdown("---")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("##### 📋 Open Orders Backlog")
            orders = pd.DataFrame({
                "Order #": ["SO-78452", "SO-78451", "SO-78450", "SO-78449", "SO-78448", "SO-78447", "SO-78446"],
                "Customer": ["BMW Group", "Landis+Gyr", "Itron", "Continental", "Trimble", "Honeywell", "NTT DoCoMo"],
                "Product": ["FN990A 5G", "ME310G1", "ME310G1", "LE910C4", "SE868K3", "ME310G1", "FN990A 5G"],
                "Qty": [5000, 8000, 6500, 3200, 2800, 4500, 3800],
                "Value": ["$625K", "$208K", "$169K", "$134K", "$52K", "$117K", "$475K"],
                "Request Date": ["Dec 30", "Jan 2", "Jan 3", "Jan 5", "Dec 29", "Jan 8", "Jan 10"],
                "Promise Date": ["Dec 30", "Jan 3", "Jan 4", "Jan 6", "Dec 30", "Jan 9", "Jan 12"],
                "Status": ["🟢 Ready", "🟢 Ready", "🟡 Partial", "🟢 Ready", "🟢 Ready", "🟡 Partial", "🔴 Short"],
                "Priority": ["⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐⭐", "⭐⭐⭐"]
            })
            st.dataframe(orders, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 Orders by Status")
            status_data = pd.DataFrame({
                "Status": ["Ready to Ship", "Partial Available", "Awaiting Stock", "On Hold"],
                "Count": [542, 187, 98, 20],
                "Value": ["$18.2M", "$6.8M", "$2.9M", "$0.6M"]
            })
            
            fig_status = go.Figure(go.Pie(
                labels=status_data["Status"], values=status_data["Count"], hole=0.6,
                marker_colors=[TELIT_GREEN, TELIT_ORANGE, TELIT_RED, TELIT_GRAY]
            ))
            fig_status.add_annotation(text="<b>847</b><br>Orders", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_status.update_layout(height=250, margin=dict(l=10, r=10, t=10, b=10), showlegend=True,
                                    legend=dict(orientation="h", y=-0.1, font=dict(size=10)))
            st.plotly_chart(fig_status, use_container_width=True)
        
        # Allocation matrix
        st.markdown("##### 🎯 Allocation Matrix (Scarce Products)")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05); 
                    border-radius: 8px; padding: 12px; margin-bottom: 15px; border-left: 4px solid {TELIT_ORANGE};">
            ⚠️ <strong>FN990A 5G modules are constrained.</strong> Current availability: 16,300 units. 
            Demand backlog: 22,800 units. Allocation required.
        </div>
        """, unsafe_allow_html=True)
        
        alloc_data = pd.DataFrame({
            "Customer": ["BMW Group", "NTT DoCoMo", "Delphi", "Continental", "Trimble"],
            "Tier": ["Tier 1", "Tier 1", "Tier 2", "Tier 1", "Tier 2"],
            "Requested": [5000, 3800, 2500, 2000, 1500],
            "Allocated": [5000, 3800, 1500, 2000, 800],
            "Fill Rate": ["100%", "100%", "60%", "100%", "53%"],
            "Backorder": [0, 0, 1000, 0, 700],
            "Priority": ["⭐⭐⭐", "⭐⭐⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐"]
        })
        st.dataframe(alloc_data, use_container_width=True)
        
        st.markdown("---")
        
        # Customer backlog aging
        st.markdown("##### ⏳ Backlog Aging")
        aging_cols = st.columns(2)
        
        with aging_cols[0]:
            aging = pd.DataFrame({
                "Age": ["0-7 Days", "8-14 Days", "15-30 Days", "31-60 Days", "> 60 Days"],
                "Orders": [425, 245, 112, 48, 17],
                "Value": ["$14.2M", "$8.5M", "$3.8M", "$1.5M", "$0.5M"]
            })
            
            fig_aging = go.Figure(go.Bar(
                x=aging["Age"], y=aging["Orders"],
                marker_color=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, TELIT_RED, '#8B0000'],
                text=aging["Orders"], textposition="outside"
            ))
            fig_aging.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Orders")
            st.plotly_chart(fig_aging, use_container_width=True)
        
        with aging_cols[1]:
            st.markdown("##### 🏆 Top Customers by Backlog")
            top_customers = [
                ("BMW Group", "$5.2M", "15 orders", TELIT_BLUE),
                ("Landis+Gyr", "$3.8M", "22 orders", TELIT_GREEN),
                ("NTT DoCoMo", "$2.9M", "8 orders", TELIT_ORANGE),
                ("Itron", "$2.1M", "18 orders", "#6B5B95"),
            ]
            for customer, value, orders, color in top_customers:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}15, {color}05);
                            padding: 10px 15px; margin: 5px 0; border-radius: 8px; border-left: 3px solid {color};">
                    <div style="display: flex; justify-content: space-between;">
                        <strong>{customer}</strong>
                        <span style="font-weight: 600; color: {color};">{value}</span>
                    </div>
                    <div style="font-size: 11px; color: {TELIT_GRAY};">{orders}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 8: MRP & PRODUCTION
    # =================================================================
    with inv_tab8:
        st.subheader("🏭 Material Requirements Planning")
        
        # MRP KPIs
        mrp_kpis = st.columns(5)
        mrp_kpis[0].metric("Build Plan (Week)", "12,500", "+1,200", help="Units planned")
        mrp_kpis[1].metric("Material Available", "96.5%", "+2.1%", help="BOM completeness")
        mrp_kpis[2].metric("Component Shortages", "3", "-1", help="Blocking items")
        mrp_kpis[3].metric("WIP Units", "8,450", "+320", help="Work in progress")
        mrp_kpis[4].metric("Production Capacity", "85%", "+5%", help="Utilization")
        
        st.markdown("---")
        
        # Build plan vs inventory
        st.markdown("##### 📅 Weekly Build Plan vs Material Availability")
        plan_data = pd.DataFrame({
            "Week": ["W1 (Dec 30)", "W2 (Jan 6)", "W3 (Jan 13)", "W4 (Jan 20)", "W5 (Jan 27)"],
            "ME310G1": [3500, 4000, 3800, 4200, 3500],
            "FN990A": [2000, 2500, 2200, 2800, 2400],
            "LE910C4": [2500, 2800, 2600, 3000, 2800],
            "SE868K3": [1500, 1800, 1600, 2000, 1800],
            "Material Status": ["🟢 Ready", "🟢 Ready", "🟡 92% OK", "🟡 88% OK", "🔴 75% OK"]
        })
        st.dataframe(plan_data, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🧩 Component Availability Check")
            components = pd.DataFrame({
                "Component": ["Qualcomm SDX55", "u-blox M10", "Skyworks PA", "Murata MLCC", "Samsung Flash", "PCB Assemblies"],
                "Required (4 wks)": [12000, 8500, 45000, 2800000, 48000, 12500],
                "Available": [11200, 9200, 52000, 3100000, 45000, 14000],
                "Coverage": ["93%", "108%", "116%", "111%", "94%", "112%"],
                "Status": ["🟡 Short 800", "🟢 OK", "🟢 OK", "🟢 OK", "🟡 Short 3000", "🟢 OK"],
                "ETA Next PO": ["Jan 8", "Jan 15", "—", "—", "Jan 5", "—"]
            })
            st.dataframe(components, use_container_width=True)
        
        with col2:
            st.markdown("##### ⚠️ Critical Shortages")
            shortages = [
                ("🔴 Qualcomm SDX55", "FN990A 5G", "800 units short", "Jan 8 PO arrival", TELIT_RED),
                ("🟡 Samsung Flash", "ME310G1", "3,000 units short", "Jan 5 PO arrival", TELIT_ORANGE),
                ("🟡 AOI Calibration", "All Lines", "Maintenance pending", "Dec 28 scheduled", TELIT_ORANGE),
            ]
            for item, product, qty, eta, color in shortages:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}15, {color}05);
                            padding: 12px; margin: 8px 0; border-radius: 8px; border-left: 4px solid {color};">
                    <div style="font-weight: 600;">{item}</div>
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Affects: {product} | {qty}</div>
                    <div style="font-size: 11px; color: {color};">📅 {eta}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # WIP tracking
        st.markdown("##### 🔄 Work-in-Progress (WIP) Tracking")
        wip_cols = st.columns(5)
        wip_stages = [
            ("SMT Assembly", 2450, "$312K", TELIT_BLUE),
            ("Reflow & Inspection", 1850, "$245K", TELIT_GREEN),
            ("Programming", 1680, "$218K", TELIT_ORANGE),
            ("Testing", 1520, "$198K", "#6B5B95"),
            ("Packaging", 950, "$124K", TELIT_GRAY),
        ]
        for col, (stage, units, value, color) in zip(wip_cols, wip_stages):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 11px; font-weight: 600; color: {color};">{stage}</div>
                <div style="font-size: 22px; font-weight: 700; margin: 8px 0;">{units:,}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{value}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Production capacity
        st.markdown("##### 📊 Production Capacity vs Demand")
        cap_col1, cap_col2 = st.columns(2)
        
        with cap_col1:
            weeks = ["W1", "W2", "W3", "W4"]
            capacity = [15000, 15000, 14500, 15000]
            planned = [12500, 13800, 12200, 14500]
            
            fig_cap = go.Figure()
            fig_cap.add_trace(go.Bar(name="Capacity", x=weeks, y=capacity, marker_color=TELIT_GRAY, opacity=0.5))
            fig_cap.add_trace(go.Bar(name="Planned", x=weeks, y=planned, marker_color=TELIT_BLUE))
            fig_cap.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40), barmode='overlay',
                                 yaxis_title="Units", legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_cap, use_container_width=True)
        
        with cap_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 16px; font-weight: 600; margin-bottom: 15px;">🏭 Capacity Summary</div>
                <div style="margin-bottom: 10px;">
                    <strong>Weekly Capacity:</strong> 15,000 units
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Current Utilization:</strong> 85%
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Bottleneck:</strong> AOI Station (93% utilized)
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: {TELIT_GREEN};">
                    ✅ Sufficient capacity for next 4 weeks
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 9: E2E VISIBILITY
    # =================================================================
    with inv_tab9:
        st.subheader("🌐 End-to-End Supply Chain Visibility")
        
        # E2E metrics
        e2e_kpis = st.columns(5)
        e2e_kpis[0].metric("Order Cycle Time", "18.5 days", "-2.1 days", help="PO to delivery")
        e2e_kpis[1].metric("Cash-to-Cash", "45 days", "-5 days", help="Working capital cycle")
        e2e_kpis[2].metric("Perfect Order Rate", "91.2%", "+2.3%", help="OTIF + quality")
        e2e_kpis[3].metric("Supply Chain Visibility", "87%", "+8%", help="Real-time tracking")
        e2e_kpis[4].metric("Risk Score", "Low", "🟢", help="Overall risk level")
        
        st.markdown("---")
        
        # Order lifecycle tracker
        st.markdown("##### 📍 Order Lifecycle Tracker")
        
        # Sample order journey
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}10, {TELIT_DARK}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="font-size: 18px; font-weight: 600; margin-bottom: 15px;">
                📦 Order SO-78452 (BMW Group - FN990A 5G - 5,000 units)
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <div style="text-align: center; flex: 1;">
                    <div style="background: {TELIT_GREEN}; color: white; width: 40px; height: 40px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 18px;">✓</div>
                    <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">Order Received</div>
                    <div style="font-size: 10px; color: {TELIT_GRAY};">Dec 22</div>
                </div>
                <div style="flex: 0.5; height: 3px; background: {TELIT_GREEN};"></div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: {TELIT_GREEN}; color: white; width: 40px; height: 40px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 18px;">✓</div>
                    <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">Allocation</div>
                    <div style="font-size: 10px; color: {TELIT_GRAY};">Dec 23</div>
                </div>
                <div style="flex: 0.5; height: 3px; background: {TELIT_GREEN};"></div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: {TELIT_GREEN}; color: white; width: 40px; height: 40px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 18px;">✓</div>
                    <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">Production</div>
                    <div style="font-size: 10px; color: {TELIT_GRAY};">Dec 24-27</div>
                </div>
                <div style="flex: 0.5; height: 3px; background: {TELIT_BLUE};"></div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: {TELIT_BLUE}; color: white; width: 40px; height: 40px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 16px;">📦</div>
                    <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">Packing</div>
                    <div style="font-size: 10px; color: {TELIT_GRAY};">Today</div>
                </div>
                <div style="flex: 0.5; height: 3px; background: {TELIT_GRAY};"></div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: {TELIT_GRAY}; color: white; width: 40px; height: 40px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 18px;">○</div>
                    <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">Shipped</div>
                    <div style="font-size: 10px; color: {TELIT_GRAY};">Dec 30</div>
                </div>
                <div style="flex: 0.5; height: 3px; background: {TELIT_GRAY};"></div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: {TELIT_GRAY}; color: white; width: 40px; height: 40px; border-radius: 50%; 
                                display: flex; align-items: center; justify-content: center; margin: 0 auto; font-size: 18px;">○</div>
                    <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">Delivered</div>
                    <div style="font-size: 10px; color: {TELIT_GRAY};">Jan 2</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🔗 Multi-Tier Supply Chain View")
            tiers = pd.DataFrame({
                "Tier": ["Tier 3", "Tier 2", "Tier 1", "Telit", "Customer"],
                "Example": ["Raw Materials", "Chip Fab (TSMC)", "Qualcomm Assembly", "Telit Production", "BMW"],
                "Lead Time": ["8-12 weeks", "12-16 weeks", "8-12 weeks", "2-4 weeks", "—"],
                "Visibility": ["⬜ Limited", "🟡 Partial", "🟢 Full", "🟢 Full", "🟢 Full"],
                "Risk Level": ["🟡 Medium", "🟡 Medium", "🟢 Low", "🟢 Low", "—"]
            })
            st.dataframe(tiers, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 Supplier Inventory Visibility (VMI)")
            supplier_inv = pd.DataFrame({
                "Supplier": ["Qualcomm", "u-blox", "Skyworks", "Murata"],
                "Component": ["SDX55 Modem", "M10 GNSS", "PA/LNA", "MLCC"],
                "Their Stock": ["45K units", "38K units", "125K units", "2.4M units"],
                "Our POs": ["12K units", "8K units", "—", "—"],
                "Risk": ["🟢 Low", "🟢 Low", "🟢 Low", "🟢 Low"]
            })
            st.dataframe(supplier_inv, use_container_width=True)
        
        st.markdown("---")
        
        # Risk heatmap
        st.markdown("##### 🔥 Supply Chain Risk Heatmap")
        risk_cols = st.columns(4)
        risk_areas = [
            ("🏭 Supplier Risk", "Low", "Dual sourcing in place", TELIT_GREEN, [
                "Qualcomm sole source for 5G",
                "Backup plans for critical parts"
            ]),
            ("🚢 Logistics Risk", "Medium", "Red Sea disruption", TELIT_ORANGE, [
                "Suez Canal delays +5-7 days",
                "Air freight backup ready"
            ]),
            ("📦 Inventory Risk", "Low", "Safety stock adequate", TELIT_GREEN, [
                "18.5 days supply average",
                "5G modules slightly constrained"
            ]),
            ("💹 Demand Risk", "Medium", "5G ramp uncertainty", TELIT_ORANGE, [
                "Automotive demand volatile",
                "Smart meter demand stable"
            ]),
        ]
        for col, (area, level, summary, color, details) in zip(risk_cols, risk_areas):
            details_html = "".join([f"<div style='font-size: 10px; color: {TELIT_GRAY}; margin: 3px 0;'>• {d}</div>" for d in details])
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 15px; border-top: 4px solid {color}; height: 180px;">
                <div style="font-size: 13px; font-weight: 600; color: {color};">{area}</div>
                <div style="font-size: 22px; font-weight: 700; margin: 8px 0;">{level}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin-bottom: 8px;">{summary}</div>
                {details_html}
            </div>
            """, unsafe_allow_html=True)
        
        # Customer hub consumption
        st.markdown("##### 🤝 Customer Hub Consumption Rates")
        hub_data = pd.DataFrame({
            "Customer Hub": ["BMW Munich", "Landis+Gyr Atlanta", "Continental Hanover", "Itron Liberty Lake"],
            "Product": ["FN990A 5G", "ME310G1", "LE910C4", "SE868K3"],
            "Stock Level": [2800, 6500, 2100, 4800],
            "Daily Consumption": [120, 280, 95, 210],
            "Days Supply": ["23 days", "23 days", "22 days", "23 days"],
            "Replenish Trigger": [2000, 5000, 1500, 3500],
            "Status": ["🟢 OK", "🟢 OK", "🟢 OK", "🟢 OK"]
        })
        st.dataframe(hub_data, use_container_width=True)
    
    # =================================================================
    # TAB 10: ANALYTICS
    # =================================================================
    with inv_tab10:
        # Inventory trends
        trend_col1, trend_col2 = st.columns(2)
        
        with trend_col1:
            st.subheader("📈 Inventory Value Trend (12 Months)")
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            inv_value = [42.1, 43.5, 41.8, 44.2, 45.8, 44.1, 46.5, 47.2, 45.8, 46.9, 47.8, 48.2]
            
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(x=months, y=inv_value, fill='tozeroy', fillcolor=f'rgba(0,167,225,0.2)', line=dict(color=TELIT_BLUE, width=3), mode='lines+markers'))
            fig_trend.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Value ($M)")
            st.plotly_chart(fig_trend, use_container_width=True)
        
        with trend_col2:
            st.subheader("🔄 Inventory Turnover by Category")
            categories = ["5G Modules", "LTE-M", "LTE Cat 4", "GNSS", "Legacy"]
            turns = [12.4, 9.2, 8.1, 6.5, 4.2]
            
            fig_turns = go.Figure(go.Bar(
                x=categories, y=turns,
                marker_color=[TELIT_GREEN if t > 8 else TELIT_ORANGE if t > 5 else TELIT_RED for t in turns],
                text=[f"{t}x" for t in turns], textposition="outside"
            ))
            fig_turns.add_hline(y=8, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target: 8x")
            fig_turns.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Turns/Year")
            st.plotly_chart(fig_turns, use_container_width=True)
        
        st.markdown("---")
        
        # ABC Analysis
        st.subheader("📊 ABC Analysis - Pareto Classification")
        abc_col1, abc_col2 = st.columns([2, 1])
        
        with abc_col1:
            abc_products = ["FN990A 5G", "ME310G1", "LE910C4", "SE868K3", "HE910", "CC864", "GE910", "Others"]
            abc_revenue = [35, 25, 18, 10, 5, 4, 2, 1]
            abc_cumulative = np.cumsum(abc_revenue)
            
            fig_abc = go.Figure()
            fig_abc.add_trace(go.Bar(x=abc_products, y=abc_revenue, name="Revenue %", marker_color=[TELIT_BLUE if i < 2 else TELIT_GREEN if i < 5 else TELIT_GRAY for i in range(len(abc_products))]))
            fig_abc.add_trace(go.Scatter(x=abc_products, y=abc_cumulative, name="Cumulative %", yaxis="y2", mode="lines+markers", line=dict(color=TELIT_RED, width=2)))
            fig_abc.add_hline(y=80, line_dash="dot", line_color=TELIT_ORANGE, yref="y2", annotation_text="80% (A items)")
            fig_abc.update_layout(
                height=300, margin=dict(l=20, r=60, t=10, b=60),
                yaxis=dict(title="Revenue %"), yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 105]),
                xaxis_tickangle=-30
            )
            st.plotly_chart(fig_abc, use_container_width=True)
        
        with abc_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 16px; font-weight: 600; margin-bottom: 15px;">Classification Summary</div>
                <div style="margin-bottom: 12px;">
                    <span style="background: {TELIT_BLUE}; color: white; padding: 4px 12px; border-radius: 4px; font-weight: 600;">A Items</span>
                    <span style="margin-left: 10px; color: {TELIT_GRAY};">2 SKUs | 60% revenue</span>
                </div>
                <div style="margin-bottom: 12px;">
                    <span style="background: {TELIT_GREEN}; color: white; padding: 4px 12px; border-radius: 4px; font-weight: 600;">B Items</span>
                    <span style="margin-left: 10px; color: {TELIT_GRAY};">3 SKUs | 28% revenue</span>
                </div>
                <div style="margin-bottom: 12px;">
                    <span style="background: {TELIT_GRAY}; color: white; padding: 4px 12px; border-radius: 4px; font-weight: 600;">C Items</span>
                    <span style="margin-left: 10px; color: {TELIT_GRAY};">47 SKUs | 12% revenue</span>
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: {TELIT_GRAY};">
                    Focus inventory investment on A & B items for maximum ROI
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Product Lifecycle Management
        st.subheader("📋 Product Lifecycle Status")
        
        lc_col1, lc_col2 = st.columns([2, 1])
        
        with lc_col1:
            lifecycle_data = pd.DataFrame({
                "Product Family": ["FN990A (5G)", "ME310G1 (LTE-M)", "LE910C4 (LTE)", "SE868K3 (GNSS)", "HE910 (3G)", "CC864 (2G)", "GE910 (2G)"],
                "Status": ["🟢 Active - Growth", "🟢 Active - Mature", "🟢 Active - Mature", "🟢 Active - Growth", "🟡 EOL Announced", "🟠 Last Time Buy", "🔴 Discontinued"],
                "Launch": ["2023", "2020", "2019", "2022", "2015", "2012", "2010"],
                "EOL Date": ["—", "—", "—", "—", "Jun 2025", "Mar 2024", "Dec 2023"],
                "Inventory": ["35,000", "78,000", "62,000", "45,000", "12,000", "25,000", "3,200"],
                "LTB Qty": ["—", "—", "—", "—", "50,000", "Done", "Done"],
                "Replacement": ["—", "—", "—", "—", "FN990A", "ME310G1", "ME310G1"]
            })
            st.dataframe(lifecycle_data, use_container_width=True)
        
        with lc_col2:
            # Lifecycle pie chart
            lc_status = ["Active-Growth", "Active-Mature", "EOL Announced", "LTB", "Discontinued"]
            lc_values = [80000, 140000, 12000, 25000, 3200]
            lc_colors = [TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, "#FF6B6B", TELIT_RED]
            
            fig_lc = go.Figure(go.Pie(
                labels=lc_status, values=lc_values, hole=0.5,
                marker_colors=lc_colors, textinfo="percent"
            ))
            fig_lc.update_layout(height=220, margin=dict(l=10, r=10, t=10, b=10), showlegend=True, legend=dict(font=dict(size=10)))
            st.plotly_chart(fig_lc, use_container_width=True)
        
        # EOL/LTB Alerts
        st.subheader("⚠️ End-of-Life & Last Time Buy Alerts")
        eol_cols = st.columns(3)
        eol_alerts = [
            ("🔴 URGENT", "CC864-DUAL", "Last Time Buy ends Mar 15, 2024", "Order within 82 days for 5-year buffer", "25,000 units needed", TELIT_RED),
            ("🟡 PLAN", "HE910-EUR", "EOL announced Jun 2025", "Migration path: FN990A (5G successor)", "12,000 units in stock", TELIT_ORANGE),
            ("🔵 INFO", "GE910-QUAD", "Discontinued Dec 2023", "No new orders accepted. 3,200 units remaining for warranty/repair", "Scrap after Q2 2024", TELIT_BLUE),
        ]
        for col, (urgency, sku, title, desc, qty, color) in zip(eol_cols, eol_alerts):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 12px; padding: 15px; border-top: 4px solid {color}; height: 180px;">
                <span style="background: {color}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">{urgency}</span>
                <div style="font-size: 16px; font-weight: 600; margin: 10px 0;">{sku}</div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; line-height: 1.4;">{title}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 8px;">{desc}</div>
                <div style="font-size: 11px; font-weight: 600; margin-top: 5px;">{qty}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 6: AI RECOMMENDATIONS
    # =================================================================
    with inv_tab11:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🧠</span>
                <div>
                    <div style="font-size: 24px; font-weight: 700; color: white;">Inventory Optimization Engine</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">ML-powered recommendations | Analyzing 285K units across 5 warehouses</div>
                </div>
                <div style="margin-left: auto; text-align: right;">
                    <div style="font-size: 28px; font-weight: 700; color: #00C48C;">$2.4M</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px;">Potential Savings</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Recommendations
        ai_col1, ai_col2 = st.columns(2)
        
        with ai_col1:
            st.subheader("🎯 AI-Generated Actions")
            
            recommendations = [
                ("🔴", "HIGH", "Expedite FN990A 5G shipment", "Stockout risk in 8 days. Expedite PO-47823 (5,000 units) via air freight. Cost: $12K, Avoids: $180K lost sales.", "95.2%", "$168K"),
                ("🔴", "HIGH", "Rebalance Shanghai inventory", "Shanghai at 92% capacity while Singapore at 75%. Transfer 8,000 ME310G1 units. Saves $45K in expedite fees.", "91.8%", "$45K"),
                ("🟡", "MEDIUM", "Reduce CC864 safety stock", "Legacy 2G demand declining 15% YoY. Reduce safety stock by 40% to free $320K working capital.", "88.4%", "$320K"),
                ("🟡", "MEDIUM", "Consolidate slow movers", "47 C-class SKUs spread across 5 warehouses. Consolidate to 2 locations. Annual savings: $85K.", "86.1%", "$85K"),
            ]
            
            for icon, priority, title, desc, confidence, impact in recommendations:
                color = TELIT_RED if priority == "HIGH" else TELIT_ORANGE
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}15, {color}05); border-radius: 12px; padding: 15px; margin-bottom: 12px; border-left: 5px solid {color};">
                    <div style="display: flex; justify-content: space-between; align-items: start;">
                        <div style="flex: 1;">
                            <span style="background: {color}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 10px; font-weight: 600;">{priority}</span>
                            <div style="font-size: 15px; font-weight: 600; margin: 8px 0;">{title}</div>
                            <div style="font-size: 12px; color: {TELIT_GRAY}; line-height: 1.4;">{desc}</div>
                        </div>
                    </div>
                    <div style="margin-top: 10px; padding-top: 10px; border-top: 1px solid {color}30; display: flex; gap: 20px; font-size: 11px;">
                        <div><span style="color: {TELIT_GRAY};">Confidence:</span> <strong>{confidence}</strong></div>
                        <div><span style="color: {TELIT_GRAY};">Impact:</span> <strong style="color: {TELIT_GREEN};">{impact}</strong></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        with ai_col2:
            st.subheader("📈 Demand Forecast vs Stock")
            
            weeks = [f"W{i}" for i in range(1, 9)]
            forecast = [12500, 13800, 15200, 14100, 13500, 14800, 16200, 15500]
            current_stock = [35000, 32500, 29300, 25200, 21700, 18900, 14100, 8600]
            reorder_line = [15000] * 8
            
            fig_forecast = go.Figure()
            fig_forecast.add_trace(go.Bar(name="Forecasted Demand", x=weeks, y=forecast, marker_color=TELIT_BLUE))
            fig_forecast.add_trace(go.Scatter(name="Projected Stock", x=weeks, y=current_stock, mode="lines+markers", line=dict(color=TELIT_GREEN, width=3)))
            fig_forecast.add_trace(go.Scatter(name="Reorder Point", x=weeks, y=reorder_line, mode="lines", line=dict(color=TELIT_RED, dash="dash")))
            fig_forecast.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), legend=dict(orientation="h", yanchor="bottom", y=1.02))
            st.plotly_chart(fig_forecast, use_container_width=True)
            
            st.warning("⚠️ **AI Alert:** FN990A stock will breach reorder point in Week 6. Recommended action: Place PO by Dec 28.")
            
            st.subheader("💰 Working Capital Optimization")
            wc_metrics = st.columns(3)
            wc_metrics[0].metric("Current Tied Capital", "$48.2M", "")
            wc_metrics[1].metric("Optimal Level", "$42.1M", "")
            wc_metrics[2].metric("Excess Inventory", "$6.1M", "-$1.2M vs Q3")
        
        st.markdown("---")
        
        # Model Performance
        st.subheader("🧪 AI Model Performance")
        model_cols = st.columns(4)
        models = [
            ("Demand Forecast", "94.5%", "Prophet + XGBoost"),
            ("Stock Optimization", "92.1%", "Reinforcement Learning"),
            ("Lead Time Prediction", "89.8%", "Gradient Boosting"),
            ("Anomaly Detection", "97.2%", "Isolation Forest")
        ]
        for col, (name, acc, algo) in zip(model_cols, models):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 10px; padding: 15px; text-align: center;">
                <div style="font-size: 11px; color: {TELIT_GRAY}; text-transform: uppercase;">{name}</div>
                <div style="font-size: 28px; font-weight: 700; color: {TELIT_GREEN}; margin: 8px 0;">{acc}</div>
                <div style="font-size: 10px; color: {TELIT_BLUE};">{algo}</div>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# PAGE: DEMAND FORECAST
# =============================================================================
elif page == "📈 Demand Forecast":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">📈 Demand Forecasting</h1>
        <p style="opacity: 0.8; color: white;">AI/ML-powered demand predictions for IoT modules</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("2025 Forecast", "4.2M units", "+18%"),
        ("Q1 2025", "985K", "+15%"),
        ("Revenue Forecast", "$892M", "+22%"),
        ("5G Growth", "+45%", "YoY"),
        ("Accuracy (MAPE)", "5.8%", "-0.4%"),
        ("Bias", "-1.2%", "Slight under"),
        ("Design Wins", "47", "+12 YTD"),
        ("Pipeline Value", "$245M", "+$32M")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    df_tab1, df_tab2, df_tab3, df_tab4, df_tab5, df_tab6, df_tab7, df_tab8, df_tab9, df_tab10, df_tab11, df_tab12, df_tab13 = st.tabs([
        "📊 Overview",
        "📈 Models",
        "🏭 Products",
        "🌍 Regions",
        "🏢 Customers",
        "📡 Design Wins",
        "📅 Calendar",
        "🔄 S&OP",
        "📊 Accuracy",
        "⚡ Signals",
        "🌡️ Heatmap",
        "🔮 Scenarios",
        "🤖 AI"
    ])
    
    # =================================================================
    # TAB 1: OVERVIEW
    # =================================================================
    with df_tab1:
        st.subheader("📊 Demand Forecast Overview")
        
        # Forecast summary header
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 22px; font-weight: 700;">🎯 2025 Demand Outlook</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">
                        Consolidated forecast across all product families, regions, and channels
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_GREEN};">4.2M</div>
                    <div style="color: {TELIT_GRAY}; font-size: 12px;">Units forecasted for 2025</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Monthly Demand Trend (2024-2025)")
            months = ['Jul 24', 'Aug 24', 'Sep 24', 'Oct 24', 'Nov 24', 'Dec 24', 
                     'Jan 25', 'Feb 25', 'Mar 25', 'Apr 25', 'May 25', 'Jun 25',
                     'Jul 25', 'Aug 25', 'Sep 25', 'Oct 25', 'Nov 25', 'Dec 25']
            actual = [285, 298, 312, 345, 358, 342, None, None, None, None, None, None, None, None, None, None, None, None]
            forecast = [None, None, None, None, None, 342, 328, 335, 365, 385, 398, 378, 365, 382, 405, 425, 438, 412]
            upper = [None, None, None, None, None, None, 352, 362, 398, 425, 442, 418, 402, 425, 455, 478, 495, 468]
            lower = [None, None, None, None, None, None, 304, 308, 332, 345, 354, 338, 328, 339, 355, 372, 381, 356]
            
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(x=months, y=upper, fill=None, mode='lines', 
                                          line=dict(color='rgba(0,167,225,0.1)'), name='Upper Bound', showlegend=False))
            fig_trend.add_trace(go.Scatter(x=months, y=lower, fill='tonexty', mode='lines',
                                          line=dict(color='rgba(0,167,225,0.1)'), fillcolor='rgba(0,167,225,0.2)', 
                                          name='Confidence Band'))
            fig_trend.add_trace(go.Scatter(x=months, y=actual, mode='lines+markers', name='Actual',
                                          line=dict(color=TELIT_BLUE, width=3), marker=dict(size=8)))
            fig_trend.add_trace(go.Scatter(x=months, y=forecast, mode='lines+markers', name='Forecast',
                                          line=dict(color=TELIT_ORANGE, width=2, dash='dash'), marker=dict(size=6)))
            fig_trend.update_layout(height=320, margin=dict(l=20, r=20, t=10, b=60),
                                   xaxis_tickangle=-45, yaxis_title="Units (K)",
                                   legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_trend, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 2025 Quarterly Breakdown")
            quarters = ["Q1 2025", "Q2 2025", "Q3 2025", "Q4 2025"]
            q_forecast = [985, 1045, 1078, 1092]
            q_growth = [15, 18, 20, 22]
            
            fig_quarterly = go.Figure()
            fig_quarterly.add_trace(go.Bar(x=quarters, y=q_forecast, name="Forecast (K units)",
                                          marker_color=TELIT_BLUE, text=[f"{q}K" for q in q_forecast], textposition="outside"))
            fig_quarterly.add_trace(go.Scatter(x=quarters, y=q_growth, name="YoY Growth %", yaxis="y2",
                                              mode='lines+markers', line=dict(color=TELIT_GREEN, width=3), marker=dict(size=10)))
            fig_quarterly.update_layout(height=320, margin=dict(l=20, r=60, t=10, b=40),
                                       yaxis=dict(title="Units (K)"), 
                                       yaxis2=dict(title="Growth %", overlaying="y", side="right", range=[0, 30]),
                                       legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_quarterly, use_container_width=True)
        
        # Forecast by product and region
        st.markdown("---")
        prod_col, reg_col = st.columns(2)
        
        with prod_col:
            st.markdown("##### 🏭 2025 Forecast by Product Family")
            products = ["5G (FN990A)", "LTE-M (ME310G1)", "LTE Cat 4 (LE910C4)", "GNSS (SE868K3)", "Legacy 2G/3G"]
            prod_forecast = [1.2, 1.5, 0.9, 0.5, 0.1]
            prod_colors = [TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, '#6B5B95', TELIT_GRAY]
            
            fig_prod = go.Figure(go.Pie(
                labels=products, values=prod_forecast, hole=0.55,
                marker_colors=prod_colors, textinfo="label+percent"
            ))
            fig_prod.add_annotation(text="<b>4.2M</b><br>Total", x=0.5, y=0.5, font_size=16, showarrow=False)
            fig_prod.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_prod, use_container_width=True)
        
        with reg_col:
            st.markdown("##### 🌍 2025 Forecast by Region")
            regions = ["Americas", "EMEA", "APAC"]
            reg_forecast = [1.68, 1.47, 1.05]
            reg_colors = [TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE]
            
            fig_reg = go.Figure(go.Pie(
                labels=regions, values=reg_forecast, hole=0.55,
                marker_colors=reg_colors, textinfo="label+percent"
            ))
            fig_reg.add_annotation(text="<b>4.2M</b><br>Total", x=0.5, y=0.5, font_size=16, showarrow=False)
            fig_reg.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_reg, use_container_width=True)
        
        # Forecast accuracy
        st.markdown("---")
        st.markdown("##### 📊 Forecast Accuracy Metrics")
        acc_cols = st.columns(5)
        acc_metrics = [
            ("MAPE", "5.8%", "Mean Absolute % Error", TELIT_GREEN, "Target: <8%"),
            ("Bias", "-1.2%", "Forecast Bias", TELIT_BLUE, "Slight under-forecast"),
            ("WMAPE", "6.2%", "Weighted MAPE", TELIT_GREEN, "By revenue"),
            ("Tracking Signal", "0.8", "Within control limits", TELIT_GREEN, "Range: -4 to +4"),
            ("R² Score", "0.92", "Model Fit", TELIT_GREEN, "Strong correlation"),
        ]
        for col, (metric, value, desc, color, note) in zip(acc_cols, acc_metrics):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 600; color: {color};">{metric}</div>
                <div style="font-size: 28px; font-weight: 700; margin: 8px 0;">{value}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{desc}</div>
                <div style="font-size: 9px; color: {color}; margin-top: 5px;">{note}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 2: FORECAST MODELS
    # =================================================================
    with df_tab2:
        st.subheader("📈 Forecasting Models & Methods")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea20, #764ba210); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="font-size: 18px; font-weight: 700;">🧠 Multi-Model Ensemble Approach</div>
            <div style="color: {TELIT_GRAY}; font-size: 14px; margin-top: 8px;">
                Telit uses a weighted ensemble of statistical and ML models for optimal accuracy. 
                Models are automatically selected based on product characteristics and data patterns.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🔬 Model Performance Comparison")
            models = pd.DataFrame({
                "Model": ["XGBoost Ensemble", "Prophet (Meta)", "ARIMA", "Exponential Smoothing", "Neural Network (LSTM)", "Naive (Baseline)"],
                "MAPE": [5.8, 6.2, 7.1, 6.8, 6.5, 12.4],
                "Bias": ["-1.2%", "+0.8%", "-2.1%", "+1.5%", "-0.5%", "+5.2%"],
                "Compute Time": ["8 sec", "12 sec", "2 sec", "1 sec", "45 sec", "0 sec"],
                "Status": ["🟢 Production", "🟢 Production", "🔵 Backup", "🔵 Backup", "🟡 Testing", "⚪ Benchmark"]
            })
            st.dataframe(models, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 Model Accuracy Trend")
            months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            xgb_mape = [6.5, 6.2, 5.9, 5.8, 5.7, 5.8]
            prophet_mape = [7.2, 6.8, 6.5, 6.3, 6.2, 6.2]
            ensemble_mape = [5.8, 5.5, 5.3, 5.2, 5.1, 5.2]
            
            fig_models = go.Figure()
            fig_models.add_trace(go.Scatter(x=months, y=xgb_mape, name="XGBoost", 
                                           line=dict(color=TELIT_BLUE, width=2)))
            fig_models.add_trace(go.Scatter(x=months, y=prophet_mape, name="Prophet",
                                           line=dict(color=TELIT_ORANGE, width=2)))
            fig_models.add_trace(go.Scatter(x=months, y=ensemble_mape, name="Ensemble",
                                           line=dict(color=TELIT_GREEN, width=3)))
            fig_models.add_hline(y=8, line_dash="dash", line_color="red", annotation_text="Target: 8%")
            fig_models.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40),
                                    yaxis_title="MAPE %", legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_models, use_container_width=True)
        
        # Feature importance
        st.markdown("---")
        st.markdown("##### 🎯 Key Demand Drivers (Feature Importance)")
        driver_cols = st.columns(2)
        
        with driver_cols[0]:
            features = ["Historical Shipments", "Design Win Pipeline", "Customer EDI Forecasts", 
                       "Seasonality Index", "Market Growth Rate", "Competitor Activity", 
                       "Economic Indicators", "Technology Transitions"]
            importance = [25, 22, 18, 12, 8, 6, 5, 4]
            
            fig_features = go.Figure(go.Bar(
                x=importance, y=features, orientation='h',
                marker_color=[TELIT_BLUE if i > 15 else TELIT_GREEN if i > 8 else TELIT_GRAY for i in importance],
                text=[f"{i}%" for i in importance], textposition="outside"
            ))
            fig_features.update_layout(height=320, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="Importance %")
            st.plotly_chart(fig_features, use_container_width=True)
        
        with driver_cols[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 16px; font-weight: 600; margin-bottom: 15px;">📋 Model Configuration</div>
                <div style="margin-bottom: 12px;">
                    <strong>Training Window:</strong> 24 months rolling
                </div>
                <div style="margin-bottom: 12px;">
                    <strong>Forecast Horizon:</strong> 12 months
                </div>
                <div style="margin-bottom: 12px;">
                    <strong>Refresh Frequency:</strong> Weekly (Sundays)
                </div>
                <div style="margin-bottom: 12px;">
                    <strong>Data Sources:</strong> SAP, EDI, Salesforce, Market Data
                </div>
                <div style="margin-bottom: 12px;">
                    <strong>Granularity:</strong> SKU × Region × Month
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: {TELIT_GREEN};">
                    ✅ Last model retrain: Dec 22, 2024
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Confidence intervals
        st.markdown("---")
        st.markdown("##### 📊 Forecast Confidence Intervals")
        conf_data = pd.DataFrame({
            "Product": ["FN990A 5G", "ME310G1", "LE910C4", "SE868K3", "All Products"],
            "Point Forecast": ["1.20M", "1.50M", "0.90M", "0.50M", "4.20M"],
            "Low (P10)": ["1.05M", "1.35M", "0.78M", "0.42M", "3.70M"],
            "High (P90)": ["1.38M", "1.68M", "1.05M", "0.58M", "4.75M"],
            "Confidence Width": ["±14%", "±11%", "±15%", "±16%", "±12%"],
            "Uncertainty": ["🟡 Medium", "🟢 Low", "🟡 Medium", "🟡 Medium", "🟢 Low"]
        })
        st.dataframe(conf_data, use_container_width=True)
    
    # =================================================================
    # TAB 3: PRODUCT FORECASTS
    # =================================================================
    with df_tab3:
        st.subheader("🏭 Forecast by Product Family")
        
        # Product selector
        selected_product = st.selectbox("Select Product Family", 
                                       ["All Products", "FN990A (5G)", "ME310G1 (LTE-M)", 
                                        "LE910C4 (LTE Cat 4)", "SE868K3 (GNSS)", "Legacy (2G/3G)"])
        
        st.markdown("---")
        
        # Product cards
        product_cards = st.columns(5)
        products_data = [
            ("FN990A", "5G", "1.20M", "+45%", TELIT_GREEN, "📈 High Growth"),
            ("ME310G1", "LTE-M", "1.50M", "+18%", TELIT_BLUE, "📊 Stable Growth"),
            ("LE910C4", "LTE Cat 4", "0.90M", "+8%", TELIT_ORANGE, "📊 Mature"),
            ("SE868K3", "GNSS", "0.50M", "+25%", '#6B5B95', "📈 Growing"),
            ("Legacy", "2G/3G", "0.10M", "-35%", TELIT_GRAY, "📉 Declining"),
        ]
        for col, (sku, tech, forecast, growth, color, status) in zip(product_cards, products_data):
            growth_color = TELIT_GREEN if not growth.startswith("-") else TELIT_RED
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 15px; text-align: center; border-top: 4px solid {color};">
                <div style="font-size: 14px; font-weight: 700; color: {color};">{sku}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{tech}</div>
                <div style="font-size: 26px; font-weight: 700; margin: 10px 0;">{forecast}</div>
                <div style="font-size: 14px; font-weight: 600; color: {growth_color};">{growth} YoY</div>
                <div style="font-size: 10px; color: {TELIT_GRAY}; margin-top: 5px;">{status}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Product Family Trends (12 Months)")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            
            fig_prod_trend = go.Figure()
            fig_prod_trend.add_trace(go.Scatter(x=months, y=[85, 92, 98, 105, 112, 118, 125, 132, 138, 145, 152, 160],
                                               name="FN990A (5G)", line=dict(color=TELIT_GREEN, width=3)))
            fig_prod_trend.add_trace(go.Scatter(x=months, y=[120, 122, 125, 128, 130, 132, 135, 138, 140, 142, 145, 148],
                                               name="ME310G1 (LTE-M)", line=dict(color=TELIT_BLUE, width=2)))
            fig_prod_trend.add_trace(go.Scatter(x=months, y=[78, 76, 75, 74, 73, 72, 71, 70, 69, 68, 68, 68],
                                               name="LE910C4", line=dict(color=TELIT_ORANGE, width=2)))
            fig_prod_trend.add_trace(go.Scatter(x=months, y=[38, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52],
                                               name="SE868K3", line=dict(color='#6B5B95', width=2)))
            fig_prod_trend.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40),
                                        yaxis_title="Units (K)", legend=dict(orientation="h", y=1.15))
            st.plotly_chart(fig_prod_trend, use_container_width=True)
        
        with col2:
            st.markdown("##### 🔄 Technology Transition Outlook")
            tech_data = pd.DataFrame({
                "Technology": ["5G", "LTE-M/NB-IoT", "LTE Cat 4/1", "3G", "2G"],
                "2024 Share": ["18%", "35%", "28%", "12%", "7%"],
                "2025 Share": ["29%", "38%", "22%", "8%", "3%"],
                "2026 Share": ["42%", "38%", "15%", "4%", "1%"],
                "Trend": ["📈📈📈", "📈", "📉", "📉📉", "📉📉📉"]
            })
            st.dataframe(tech_data, use_container_width=True)
            
            st.markdown(f"""
            <div style="background: {TELIT_GREEN}15; padding: 12px; border-radius: 8px; margin-top: 10px;">
                <strong>💡 Key Insight:</strong> 5G modules will surpass LTE Cat 4 in volume by Q3 2025. 
                Plan capacity and component sourcing accordingly.
            </div>
            """, unsafe_allow_html=True)
        
        # Detailed product table
        st.markdown("---")
        st.markdown("##### 📋 Detailed Product Forecast")
        detailed_products = pd.DataFrame({
            "SKU": ["FN990A28-W1", "FN990A28-EU", "ME310G1-W1", "ME310G1-WW", "LE910C4-NF", "LE910C4-EU", "SE868K3-A", "CC864-DUAL"],
            "Product": ["5G NA", "5G EU", "LTE-M NA", "LTE-M Global", "LTE Cat 4 NA", "LTE Cat 4 EU", "GNSS", "2G Legacy"],
            "Q1 2025": ["180K", "120K", "220K", "180K", "85K", "75K", "65K", "12K"],
            "Q2 2025": ["210K", "145K", "235K", "195K", "82K", "72K", "72K", "10K"],
            "Q3 2025": ["245K", "165K", "245K", "205K", "78K", "68K", "78K", "8K"],
            "Q4 2025": ["280K", "185K", "255K", "215K", "75K", "65K", "82K", "6K"],
            "Total 2025": ["915K", "615K", "955K", "795K", "320K", "280K", "297K", "36K"],
            "YoY Growth": ["+52%", "+38%", "+16%", "+20%", "+5%", "+3%", "+28%", "-42%"]
        })
        st.dataframe(detailed_products, use_container_width=True)
    
    # =================================================================
    # TAB 4: REGIONAL FORECASTS
    # =================================================================
    with df_tab4:
        st.subheader("🌍 Forecast by Region")
        
        # Regional summary cards
        region_cards = st.columns(3)
        regions_data = [
            ("🇺🇸 Americas", "1.68M", "+20%", "40%", TELIT_BLUE, ["Automotive telematics", "Smart metering", "Fleet management"]),
            ("🇪🇺 EMEA", "1.47M", "+15%", "35%", TELIT_GREEN, ["Smart energy", "Industrial IoT", "Connected vehicles"]),
            ("🌏 APAC", "1.05M", "+22%", "25%", TELIT_ORANGE, ["Smart cities", "Manufacturing", "Logistics"]),
        ]
        for col, (region, forecast, growth, share, color, drivers) in zip(region_cards, regions_data):
            drivers_html = "".join([f"<div style='font-size: 10px; margin: 2px 0;'>• {d}</div>" for d in drivers])
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 20px; border-left: 5px solid {color};">
                <div style="font-size: 18px; font-weight: 700; color: {color};">{region}</div>
                <div style="font-size: 32px; font-weight: 700; margin: 12px 0;">{forecast}</div>
                <div style="display: flex; gap: 15px; margin-bottom: 12px;">
                    <span style="color: {TELIT_GREEN}; font-weight: 600;">{growth} YoY</span>
                    <span style="color: {TELIT_GRAY};">{share} of total</span>
                </div>
                <div style="font-size: 11px; font-weight: 600; color: {TELIT_GRAY};">Key Drivers:</div>
                {drivers_html}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Regional Quarterly Trends")
            quarters = ["Q1 24", "Q2 24", "Q3 24", "Q4 24", "Q1 25", "Q2 25", "Q3 25", "Q4 25"]
            
            fig_regional = go.Figure()
            fig_regional.add_trace(go.Scatter(x=quarters, y=[320, 345, 365, 385, 395, 415, 435, 455],
                                             name="Americas", line=dict(color=TELIT_BLUE, width=2), mode='lines+markers'))
            fig_regional.add_trace(go.Scatter(x=quarters, y=[285, 298, 315, 330, 345, 362, 378, 395],
                                             name="EMEA", line=dict(color=TELIT_GREEN, width=2), mode='lines+markers'))
            fig_regional.add_trace(go.Scatter(x=quarters, y=[185, 198, 215, 235, 245, 260, 275, 290],
                                             name="APAC", line=dict(color=TELIT_ORANGE, width=2), mode='lines+markers'))
            fig_regional.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40),
                                      yaxis_title="Units (K)", legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_regional, use_container_width=True)
        
        with col2:
            st.markdown("##### 🗺️ Regional Mix Evolution")
            years = ["2023", "2024", "2025", "2026"]
            
            fig_mix = go.Figure()
            fig_mix.add_trace(go.Bar(x=years, y=[38, 39, 40, 41], name="Americas", marker_color=TELIT_BLUE))
            fig_mix.add_trace(go.Bar(x=years, y=[37, 36, 35, 34], name="EMEA", marker_color=TELIT_GREEN))
            fig_mix.add_trace(go.Bar(x=years, y=[25, 25, 25, 25], name="APAC", marker_color=TELIT_ORANGE))
            fig_mix.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40), barmode='stack',
                                 yaxis_title="% Share", legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_mix, use_container_width=True)
        
        # Country breakdown
        st.markdown("---")
        st.markdown("##### 🏳️ Top Countries by Forecast Volume")
        country_cols = st.columns(2)
        
        with country_cols[0]:
            countries = ["United States", "Germany", "China", "Japan", "UK", "France", "Canada", "Brazil", "Italy", "Australia"]
            country_forecast = [1120, 385, 325, 245, 195, 180, 165, 145, 135, 105]
            
            fig_countries = go.Figure(go.Bar(
                x=country_forecast, y=countries, orientation='h',
                marker_color=[TELIT_BLUE if i < 3 else TELIT_GREEN if i < 6 else TELIT_GRAY for i in range(len(countries))],
                text=[f"{c}K" for c in country_forecast], textposition="outside"
            ))
            fig_countries.update_layout(height=350, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="Units (K)")
            st.plotly_chart(fig_countries, use_container_width=True)
        
        with country_cols[1]:
            country_data = pd.DataFrame({
                "Country": ["🇺🇸 United States", "🇩🇪 Germany", "🇨🇳 China", "🇯🇵 Japan", "🇬🇧 United Kingdom"],
                "2025 Forecast": ["1.12M", "385K", "325K", "245K", "195K"],
                "YoY Growth": ["+22%", "+12%", "+28%", "+18%", "+15%"],
                "Top Vertical": ["Smart Meters", "Automotive", "Smart Cities", "Fleet Mgmt", "Utilities"],
                "Key Customer": ["Landis+Gyr", "BMW Group", "China Mobile", "NTT DoCoMo", "British Gas"]
            })
            st.dataframe(country_data, use_container_width=True)
    
    # =================================================================
    # TAB 5: CUSTOMER FORECASTS
    # =================================================================
    with df_tab5:
        st.subheader("🏢 Forecast by Customer")
        
        # Top customers
        st.markdown("##### 🏆 Top 10 Customers by 2025 Forecast")
        customer_data = pd.DataFrame({
            "Rank": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            "Customer": ["Landis+Gyr", "BMW Group", "Itron", "Continental", "NTT DoCoMo", "Honeywell", "Trimble", "Delphi", "Bosch", "Vodafone"],
            "Vertical": ["Smart Metering", "Automotive", "Smart Metering", "Automotive", "Telecom", "Industrial", "Telematics", "Automotive", "Industrial", "Telecom"],
            "Primary Product": ["ME310G1", "FN990A 5G", "ME310G1", "LE910C4", "FN990A 5G", "ME310G1", "SE868K3", "FN990A 5G", "LE910C4", "ME310G1"],
            "2025 Forecast": ["485K", "420K", "380K", "285K", "245K", "195K", "175K", "165K", "155K", "145K"],
            "Revenue": ["$82M", "$105M", "$64M", "$48M", "$61M", "$33M", "$18M", "$41M", "$26M", "$25M"],
            "YoY Growth": ["+15%", "+42%", "+12%", "+8%", "+35%", "+18%", "+28%", "+52%", "+5%", "+10%"],
            "Confidence": ["🟢 High", "🟢 High", "🟢 High", "🟢 High", "🟡 Medium", "🟢 High", "🟡 Medium", "🟡 Medium", "🟢 High", "🟢 High"]
        })
        st.dataframe(customer_data, use_container_width=True)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Customer Concentration")
            customers = ["Landis+Gyr", "BMW Group", "Itron", "Continental", "NTT DoCoMo", "Others"]
            cust_share = [11.5, 10.0, 9.0, 6.8, 5.8, 56.9]
            
            fig_cust = go.Figure(go.Pie(
                labels=customers, values=cust_share, hole=0.5,
                marker_colors=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#6B5B95', '#FF6B6B', TELIT_GRAY]
            ))
            fig_cust.add_annotation(text="<b>Top 5</b><br>43%", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_cust.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_cust, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Customer Growth Rates")
            growth_customers = ["Delphi", "BMW", "NTT", "Trimble", "Honeywell", "Landis+Gyr", "Itron", "Vodafone", "Continental", "Bosch"]
            growth_rates = [52, 42, 35, 28, 18, 15, 12, 10, 8, 5]
            
            fig_growth = go.Figure(go.Bar(
                x=growth_rates, y=growth_customers, orientation='h',
                marker_color=[TELIT_GREEN if g > 25 else TELIT_BLUE if g > 10 else TELIT_GRAY for g in growth_rates],
                text=[f"+{g}%" for g in growth_rates], textposition="outside"
            ))
            fig_growth.update_layout(height=280, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="YoY Growth %")
            st.plotly_chart(fig_growth, use_container_width=True)
        
        # Customer forecast by vertical
        st.markdown("---")
        st.markdown("##### 🏭 Forecast by Vertical Market")
        vertical_cols = st.columns(5)
        verticals = [
            ("⚡ Smart Metering", "1.25M", "+14%", "Landis+Gyr, Itron", TELIT_BLUE),
            ("🚗 Automotive", "0.95M", "+32%", "BMW, Continental, Delphi", TELIT_GREEN),
            ("🏭 Industrial IoT", "0.72M", "+18%", "Honeywell, Bosch, Siemens", TELIT_ORANGE),
            ("📡 Telecom/M2M", "0.55M", "+22%", "NTT, Vodafone, AT&T", '#6B5B95'),
            ("🚛 Telematics", "0.48M", "+25%", "Trimble, CalAmp, Geotab", '#88B04B'),
        ]
        for col, (vertical, forecast, growth, customers, color) in zip(vertical_cols, verticals):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 600; color: {color};">{vertical}</div>
                <div style="font-size: 24px; font-weight: 700; margin: 8px 0;">{forecast}</div>
                <div style="font-size: 12px; color: {TELIT_GREEN}; font-weight: 600;">{growth}</div>
                <div style="font-size: 9px; color: {TELIT_GRAY}; margin-top: 8px;">{customers}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 6: DESIGN WIN PIPELINE
    # =================================================================
    with df_tab6:
        st.subheader("📡 Design Win Pipeline → Future Demand")
        
        # Pipeline summary
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_GREEN};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">🎯 Design Win Pipeline Value</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">
                        47 active design wins converting to production demand over 12-36 months
                    </div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 36px; font-weight: 700; color: {TELIT_GREEN};">$245M</div>
                    <div style="color: {TELIT_GRAY}; font-size: 12px;">Lifetime revenue potential</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Pipeline KPIs
        pipe_kpis = st.columns(5)
        pipe_kpis[0].metric("Active Design Wins", "47", "+12 YTD")
        pipe_kpis[1].metric("Won This Quarter", "12", "+3 vs Q3")
        pipe_kpis[2].metric("Avg Win Size", "$5.2M", "+$0.4M")
        pipe_kpis[3].metric("Win Rate", "38%", "+5%")
        pipe_kpis[4].metric("Avg Time to Revenue", "18 months", "-2 months")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Pipeline by Stage")
            stages = ["Opportunity", "Evaluation", "Design-In", "Qualification", "Production"]
            stage_count = [45, 28, 18, 12, 47]
            stage_value = [85, 52, 38, 28, 245]
            
            fig_pipeline = go.Figure()
            fig_pipeline.add_trace(go.Funnel(
                y=stages, x=stage_value,
                textinfo="value+percent initial",
                marker_color=[TELIT_GRAY, TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN, TELIT_GREEN]
            ))
            fig_pipeline.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_pipeline, use_container_width=True)
        
        with col2:
            st.markdown("##### 📅 Expected Revenue Ramp")
            quarters = ["Q1 25", "Q2 25", "Q3 25", "Q4 25", "Q1 26", "Q2 26", "Q3 26", "Q4 26"]
            new_revenue = [8, 12, 18, 25, 32, 42, 48, 55]
            
            fig_ramp = go.Figure()
            fig_ramp.add_trace(go.Bar(x=quarters, y=new_revenue, marker_color=TELIT_GREEN,
                                     text=[f"${r}M" for r in new_revenue], textposition="outside"))
            fig_ramp.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="New Revenue ($M)")
            st.plotly_chart(fig_ramp, use_container_width=True)
        
        # Top design wins
        st.markdown("---")
        st.markdown("##### 🏆 Top Design Wins (Production Stage)")
        design_wins = pd.DataFrame({
            "Customer": ["BMW Group", "Landis+Gyr", "Continental", "NTT DoCoMo", "Trimble", "Honeywell"],
            "Application": ["5G Telematics", "Smart Meter Refresh", "V2X Platform", "5G Router", "Asset Tracker", "Industrial Gateway"],
            "Product": ["FN990A28", "ME310G1-WW", "FN990A28", "FN990A28", "SE868K3-A", "ME310G1-W1"],
            "Annual Volume": ["180K", "250K", "85K", "120K", "95K", "72K"],
            "Lifetime Value": ["$45M", "$38M", "$21M", "$30M", "$9.5M", "$12M"],
            "Production Start": ["Q1 2025", "Q2 2025", "Q3 2025", "Q2 2025", "Q1 2025", "Q4 2025"],
            "Status": ["🟢 Ramping", "🟢 Qualified", "🟡 Qual Testing", "🟢 Qualified", "🟢 Ramping", "🟡 Design-In"]
        })
        st.dataframe(design_wins, use_container_width=True)
        
        # Design win by product/vertical
        st.markdown("---")
        dw_col1, dw_col2 = st.columns(2)
        
        with dw_col1:
            st.markdown("##### 🏭 Pipeline by Product")
            dw_products = ["FN990A (5G)", "ME310G1 (LTE-M)", "LE910C4", "SE868K3 (GNSS)", "Other"]
            dw_values = [98, 72, 35, 28, 12]
            
            fig_dw_prod = go.Figure(go.Pie(
                labels=dw_products, values=dw_values, hole=0.5,
                marker_colors=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, '#6B5B95', TELIT_GRAY]
            ))
            fig_dw_prod.add_annotation(text="<b>$245M</b>", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_dw_prod.update_layout(height=250, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_dw_prod, use_container_width=True)
        
        with dw_col2:
            st.markdown("##### 🏢 Pipeline by Vertical")
            dw_verticals = ["Automotive", "Smart Metering", "Industrial", "Telematics", "Telecom"]
            dw_vert_values = [85, 68, 42, 32, 18]
            
            fig_dw_vert = go.Figure(go.Pie(
                labels=dw_verticals, values=dw_vert_values, hole=0.5,
                marker_colors=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, '#6B5B95', TELIT_GRAY]
            ))
            fig_dw_vert.add_annotation(text="<b>$245M</b>", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_dw_vert.update_layout(height=250, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_dw_vert, use_container_width=True)
    
    # =================================================================
    # TAB 7: DEMAND CALENDAR
    # =================================================================
    with df_tab7:
        st.subheader("📅 Demand Calendar & Key Events")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="font-size: 18px; font-weight: 700;">🗓️ 2025 Demand Event Calendar</div>
            <div style="color: {TELIT_GRAY}; font-size: 14px; margin-top: 8px;">
                Key events, milestones, and seasonality factors affecting IoT module demand
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Calendar view - Q1 2025
        st.markdown("##### 📆 Q1 2025 - Key Events")
        
        q1_events = [
            ("Jan 7-10", "CES 2025", "Las Vegas", "🎯 Product launches, customer meetings", TELIT_BLUE),
            ("Jan 15", "BMW 5G Telematics Ramp", "Production", "📈 +15K units/month start", TELIT_GREEN),
            ("Feb 24-27", "MWC Barcelona", "Barcelona", "🌐 Major IoT showcase, 50+ meetings", TELIT_BLUE),
            ("Feb 28", "Landis+Gyr Q1 Order", "EDI", "📦 Expected 85K units PO", TELIT_GREEN),
            ("Mar 1", "AT&T 3G Sunset", "Regulatory", "⚠️ Legacy migration deadline", TELIT_ORANGE),
            ("Mar 15", "FN990A EU Certification", "Milestone", "🏆 CE/RED approval expected", TELIT_GREEN),
            ("Mar 31", "Q1 Close", "Financial", "📊 Fiscal quarter end", TELIT_GRAY),
        ]
        
        for date, event, location, desc, color in q1_events:
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 15px; background: linear-gradient(135deg, {color}10, {color}05);
                        padding: 12px 15px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid {color};">
                <div style="min-width: 80px; font-weight: 600; color: {color};">{date}</div>
                <div style="flex: 1;">
                    <strong>{event}</strong>
                    <span style="color: {TELIT_GRAY}; margin-left: 10px;">📍 {location}</span>
                    <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 3px;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Seasonality patterns
        st.markdown("##### 📊 Monthly Seasonality Index")
        col1, col2 = st.columns([2, 1])
        
        with col1:
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            seasonality = [85, 88, 98, 100, 105, 95, 88, 92, 108, 118, 115, 92]
            
            colors = [TELIT_RED if s < 90 else TELIT_ORANGE if s < 95 else TELIT_BLUE if s <= 105 else TELIT_GREEN for s in seasonality]
            
            fig_season = go.Figure(go.Bar(
                x=months, y=seasonality, marker_color=colors,
                text=[f"{s}%" for s in seasonality], textposition="outside"
            ))
            fig_season.add_hline(y=100, line_dash="dash", line_color="gray", annotation_text="Baseline")
            fig_season.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="% of Average", yaxis=dict(range=[70, 130]))
            st.plotly_chart(fig_season, use_container_width=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">📋 Seasonality Drivers</div>
                <div style="margin-bottom: 10px; font-size: 13px;">
                    <span style="color: {TELIT_GREEN};">📈 Q4 Peak:</span> Smart meter deployments (Oct-Nov)
                </div>
                <div style="margin-bottom: 10px; font-size: 13px;">
                    <span style="color: {TELIT_GREEN};">📈 Sep Surge:</span> Post-summer ramp, auto production
                </div>
                <div style="margin-bottom: 10px; font-size: 13px;">
                    <span style="color: {TELIT_RED};">📉 Jan/Jul Dip:</span> Holiday slowdowns
                </div>
                <div style="margin-bottom: 10px; font-size: 13px;">
                    <span style="color: {TELIT_ORANGE};">⚠️ Feb:</span> Chinese New Year impact
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Upcoming milestones
        st.markdown("---")
        st.markdown("##### 🎯 Customer Milestones & Demand Triggers")
        milestone_cols = st.columns(4)
        milestones = [
            ("🚗 BMW iX5 Launch", "Q2 2025", "FN990A 5G", "+180K/year", TELIT_GREEN),
            ("⚡ US Smart Meter Mandate", "Q4 2025", "ME310G1", "+500K/year", TELIT_BLUE),
            ("🚛 EU Tachograph Update", "Q3 2025", "LE910C4", "+120K/year", TELIT_ORANGE),
            ("📡 5G SA Rollout", "2025", "FN990A", "+25% growth", TELIT_GREEN),
        ]
        for col, (event, timing, product, impact, color) in zip(milestone_cols, milestones):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color}; height: 150px;">
                <div style="font-size: 12px; font-weight: 600; color: {color};">{event}</div>
                <div style="font-size: 18px; font-weight: 700; margin: 10px 0;">{timing}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{product}</div>
                <div style="font-size: 13px; font-weight: 600; color: {TELIT_GREEN}; margin-top: 8px;">{impact}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Trade shows and events
        st.markdown("---")
        st.markdown("##### 🌐 2025 Trade Shows & Industry Events")
        events_data = pd.DataFrame({
            "Date": ["Jan 7-10", "Feb 24-27", "Mar 31-Apr 3", "Jun 10-12", "Sep 9-12", "Oct 14-16", "Nov 18-20"],
            "Event": ["CES 2025", "MWC Barcelona", "Hannover Messe", "IoT World", "IAA Munich", "Embedded World", "Electronica"],
            "Location": ["Las Vegas", "Barcelona", "Hannover", "Santa Clara", "Munich", "Nuremberg", "Munich"],
            "Focus": ["Consumer IoT", "5G/Telecom", "Industrial IoT", "IoT Ecosystem", "Automotive", "Embedded Systems", "Electronics"],
            "Telit Presence": ["🟢 Exhibiting", "🟢 Exhibiting", "🟢 Exhibiting", "🟢 Exhibiting", "🟢 Exhibiting", "🟢 Exhibiting", "🔵 Attending"],
            "Expected Leads": ["150+", "300+", "200+", "175+", "250+", "225+", "100+"]
        })
        st.dataframe(events_data, use_container_width=True)
    
    # =================================================================
    # TAB 8: S&OP CONSENSUS
    # =================================================================
    with df_tab8:
        st.subheader("🔄 Sales & Operations Planning (S&OP)")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">📊 Demand-Supply Consensus</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">Aligning Sales, Finance, and Operations forecasts</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Next S&OP Meeting</div>
                    <div style="font-size: 16px; font-weight: 600;">Jan 8, 2025</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Consensus comparison
        st.markdown("##### 📊 Q1 2025 Forecast Comparison (K units)")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            products = ["FN990A 5G", "ME310G1", "LE910C4", "SE868K3", "Total"]
            sales_fc = [305, 415, 165, 135, 1020]
            finance_fc = [285, 400, 160, 130, 975]
            ops_fc = [290, 395, 155, 128, 968]
            consensus = [295, 405, 160, 132, 992]
            
            fig_consensus = go.Figure()
            x_pos = list(range(len(products)))
            width = 0.2
            
            fig_consensus.add_trace(go.Bar(name='Sales', x=[p - 1.5*width for p in x_pos], y=sales_fc, width=width, marker_color=TELIT_BLUE))
            fig_consensus.add_trace(go.Bar(name='Finance', x=[p - 0.5*width for p in x_pos], y=finance_fc, width=width, marker_color=TELIT_ORANGE))
            fig_consensus.add_trace(go.Bar(name='Operations', x=[p + 0.5*width for p in x_pos], y=ops_fc, width=width, marker_color='#6B5B95'))
            fig_consensus.add_trace(go.Bar(name='Consensus', x=[p + 1.5*width for p in x_pos], y=consensus, width=width, marker_color=TELIT_GREEN))
            
            fig_consensus.update_layout(
                height=300, margin=dict(l=20, r=20, t=10, b=40),
                xaxis=dict(tickmode='array', tickvals=x_pos, ticktext=products),
                yaxis_title="Units (K)", barmode='group',
                legend=dict(orientation="h", y=1.1)
            )
            st.plotly_chart(fig_consensus, use_container_width=True)
        
        with col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">📋 Variance Summary</div>
                <div style="margin-bottom: 12px;">
                    <strong>Sales vs Consensus:</strong>
                    <span style="color: {TELIT_ORANGE};">+2.8%</span>
                </div>
                <div style="margin-bottom: 12px;">
                    <strong>Finance vs Consensus:</strong>
                    <span style="color: {TELIT_GREEN};">-1.7%</span>
                </div>
                <div style="margin-bottom: 12px;">
                    <strong>Ops vs Consensus:</strong>
                    <span style="color: {TELIT_GREEN};">-2.4%</span>
                </div>
                <div style="margin-top: 15px; padding: 10px; background: {TELIT_GREEN}20; border-radius: 8px;">
                    <strong>✅ Consensus:</strong> 992K units
                    <div style="font-size: 11px; color: {TELIT_GRAY};">Approved Dec 15, 2024</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Supply-Demand balance
        st.markdown("##### ⚖️ Supply-Demand Balance")
        balance_cols = st.columns(4)
        balance_data = [
            ("Consensus Demand", "992K", "Q1 2025", TELIT_BLUE),
            ("Supply Capacity", "1,050K", "Confirmed", TELIT_GREEN),
            ("Gap/Buffer", "+58K", "5.8% buffer", TELIT_GREEN),
            ("Constrained Items", "1", "FN990A (tight)", TELIT_ORANGE),
        ]
        for col, (label, value, sub, color) in zip(balance_cols, balance_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; color: {TELIT_GRAY};">{label}</div>
                <div style="font-size: 28px; font-weight: 700; color: {color}; margin: 8px 0;">{value}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{sub}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # S&OP decisions log
        st.markdown("##### 📝 Recent S&OP Decisions")
        decisions = pd.DataFrame({
            "Date": ["Dec 15", "Dec 15", "Dec 8", "Dec 1", "Nov 24"],
            "Decision": ["Increase FN990A Q2 capacity", "Approve safety stock for ME310G1", "Defer LE910C4 inventory reduction", "Accept BMW design win forecast", "Align on 2025 annual plan"],
            "Owner": ["Operations", "Finance", "Supply Chain", "Sales", "Executive"],
            "Impact": ["+25K units/month", "+$1.2M inventory", "Hold $800K", "+180K/year", "4.2M units approved"],
            "Status": ["🟢 Implemented", "🟡 In Progress", "🟢 Implemented", "🟢 Implemented", "🟢 Approved"]
        })
        st.dataframe(decisions, use_container_width=True)
        
        # Assumptions and risks
        st.markdown("---")
        ass_col, risk_col = st.columns(2)
        
        with ass_col:
            st.markdown("##### 📋 Key Assumptions")
            assumptions = [
                "5G adoption rate: 45% YoY growth",
                "Smart meter deployments on track",
                "No major supply disruptions",
                "EUR/USD stable at 1.08-1.12",
                "Automotive production recovery continues"
            ]
            for a in assumptions:
                st.markdown(f"✅ {a}")
        
        with risk_col:
            st.markdown("##### ⚠️ Key Risks")
            risks = [
                ("Qualcomm 5G chip allocation", "Medium", TELIT_ORANGE),
                ("Auto production volatility", "Medium", TELIT_ORANGE),
                ("Recession impact on industrial", "Low", TELIT_GREEN),
                ("Red Sea shipping delays", "Low", TELIT_GREEN),
            ]
            for risk, level, color in risks:
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; padding: 5px 0;">
                    <span>⚠️ {risk}</span>
                    <span style="background: {color}30; color: {color}; padding: 2px 8px; border-radius: 4px; font-size: 11px;">{level}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 9: FORECAST ACCURACY
    # =================================================================
    with df_tab9:
        st.subheader("📊 Forecast vs Actuals Analysis")
        
        # Accuracy KPIs
        acc_kpis = st.columns(5)
        acc_kpis[0].metric("Overall MAPE", "5.8%", "-0.4%", help="Mean Absolute % Error")
        acc_kpis[1].metric("Bias", "-1.2%", "+0.3%", help="Systematic under/over forecast")
        acc_kpis[2].metric("Hit Rate (±10%)", "87%", "+3%", help="% within 10% accuracy")
        acc_kpis[3].metric("Weighted MAPE", "6.2%", "-0.2%", help="Revenue-weighted accuracy")
        acc_kpis[4].metric("Forecast Value Add", "68%", "+5%", help="vs naive forecast")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Rolling 12-Month Accuracy Trend")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            mape_trend = [7.2, 6.8, 6.5, 6.3, 6.1, 5.9, 6.2, 5.8, 5.6, 5.5, 5.7, 5.8]
            bias_trend = [-2.5, -2.1, -1.8, -1.5, -1.3, -1.2, -1.5, -1.3, -1.1, -1.0, -1.1, -1.2]
            
            fig_acc = go.Figure()
            fig_acc.add_trace(go.Scatter(x=months, y=mape_trend, name="MAPE %", 
                                        line=dict(color=TELIT_BLUE, width=3), mode='lines+markers'))
            fig_acc.add_trace(go.Scatter(x=months, y=bias_trend, name="Bias %", yaxis="y2",
                                        line=dict(color=TELIT_ORANGE, width=2), mode='lines+markers'))
            fig_acc.add_hline(y=8, line_dash="dash", line_color="red", annotation_text="Target: 8%")
            fig_acc.update_layout(height=280, margin=dict(l=20, r=60, t=10, b=40),
                                 yaxis=dict(title="MAPE %", range=[0, 10]),
                                 yaxis2=dict(title="Bias %", overlaying="y", side="right", range=[-5, 5]),
                                 legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_acc, use_container_width=True)
        
        with col2:
            st.markdown("##### 🎯 Accuracy by Product Family")
            products = ["ME310G1", "FN990A", "LE910C4", "SE868K3", "Legacy"]
            prod_mape = [4.8, 7.2, 6.5, 8.1, 12.5]
            
            fig_prod_acc = go.Figure(go.Bar(
                x=products, y=prod_mape,
                marker_color=[TELIT_GREEN if m < 6 else TELIT_BLUE if m < 8 else TELIT_ORANGE if m < 10 else TELIT_RED for m in prod_mape],
                text=[f"{m}%" for m in prod_mape], textposition="outside"
            ))
            fig_prod_acc.add_hline(y=8, line_dash="dash", line_color="red", annotation_text="Target")
            fig_prod_acc.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="MAPE %", yaxis=dict(range=[0, 15]))
            st.plotly_chart(fig_prod_acc, use_container_width=True)
        
        # Error waterfall
        st.markdown("---")
        st.markdown("##### 📊 Forecast Error Decomposition (Dec 2024)")
        
        error_col1, error_col2 = st.columns([2, 1])
        
        with error_col1:
            fig_waterfall = go.Figure(go.Waterfall(
                name="Error Sources",
                orientation="v",
                measure=["absolute", "relative", "relative", "relative", "relative", "relative", "total"],
                x=["Forecast", "Timing Shift", "New Orders", "Cancellations", "Model Error", "Data Quality", "Actual"],
                y=[342000, -8500, 12000, -5200, -3800, -1500, 0],
                text=["+342K", "-8.5K", "+12K", "-5.2K", "-3.8K", "-1.5K", "335K"],
                textposition="outside",
                connector={"line": {"color": "rgb(63, 63, 63)"}}
            ))
            fig_waterfall.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=60), xaxis_tickangle=-30)
            st.plotly_chart(fig_waterfall, use_container_width=True)
        
        with error_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">📋 Error Analysis</div>
                <div style="margin-bottom: 10px;">
                    <strong>Forecast:</strong> 342K units
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Actual:</strong> 335K units
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Variance:</strong> <span style="color: {TELIT_RED};">-7K (-2.0%)</span>
                </div>
                <div style="margin-top: 15px; padding: 10px; background: {TELIT_BLUE}20; border-radius: 8px; font-size: 12px;">
                    <strong>Root Cause:</strong> BMW order shifted to Jan, offset by new Continental PO
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Customer-level accuracy
        st.markdown("---")
        st.markdown("##### 🏢 Accuracy by Top Customers")
        customer_acc = pd.DataFrame({
            "Customer": ["Landis+Gyr", "BMW Group", "Itron", "Continental", "NTT DoCoMo", "Honeywell"],
            "Forecast": ["42K", "38K", "35K", "28K", "22K", "18K"],
            "Actual": ["41K", "35K", "36K", "27K", "24K", "17K"],
            "Variance": ["-2.4%", "-7.9%", "+2.9%", "-3.6%", "+9.1%", "-5.6%"],
            "MAPE": ["3.2%", "8.5%", "4.1%", "5.2%", "9.8%", "6.1%"],
            "Status": ["🟢 On Track", "🟡 Review", "🟢 On Track", "🟢 On Track", "🟡 Review", "🟢 On Track"],
            "Trend": ["📈 Improving", "📉 Declining", "➡️ Stable", "📈 Improving", "📉 Volatile", "📈 Improving"]
        })
        st.dataframe(customer_acc, use_container_width=True)
    
    # =================================================================
    # TAB 10: REAL-TIME SIGNALS
    # =================================================================
    with df_tab10:
        st.subheader("⚡ Real-Time Demand Signals")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_GREEN};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">📡 Live Data Feeds</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">Real-time demand signals from customers, distributors, and market sources</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Last Refresh</div>
                    <div style="font-size: 16px; font-weight: 600; color: {TELIT_GREEN};">🟢 2 min ago</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Feed status
        st.markdown("##### 📊 Data Feed Status")
        feed_cols = st.columns(5)
        feeds = [
            ("🏢 Customer EDI", "18 feeds", "🟢 Active", "Last: 5 min", TELIT_GREEN),
            ("📦 Distributor POS", "6 feeds", "🟢 Active", "Daily", TELIT_GREEN),
            ("📈 Market Data", "3 sources", "🟢 Active", "Weekly", TELIT_GREEN),
            ("🔍 Web Scraping", "12 sites", "🟡 Partial", "Daily", TELIT_ORANGE),
            ("📡 IoT Telemetry", "deviceWISE", "🟢 Active", "Real-time", TELIT_GREEN),
        ]
        for col, (feed, count, status, freq, color) in zip(feed_cols, feeds):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 600; color: {color};">{feed}</div>
                <div style="font-size: 16px; font-weight: 700; margin: 6px 0;">{count}</div>
                <div style="font-size: 11px;">{status}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{freq}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Recent signals
        st.markdown("##### 🔔 Latest Demand Signals (Last 24 Hours)")
        signals = [
            ("⬆️", "BMW Group", "FN990A28", "EDI forecast revision +15K units for Q2", "2 hrs ago", TELIT_GREEN),
            ("📦", "Digi-Key", "ME310G1", "POS data: 2,400 units sold this week (+18%)", "4 hrs ago", TELIT_GREEN),
            ("⬇️", "Vodafone", "LE910C4", "Order push-out: 5K units to March", "6 hrs ago", TELIT_ORANGE),
            ("🆕", "Continental", "FN990A28", "New RFQ received: 50K/year potential", "8 hrs ago", TELIT_BLUE),
            ("📈", "Market Data", "5G Modules", "Analyst upgrade: IoT 5G market +48% in 2025", "12 hrs ago", TELIT_GREEN),
            ("⚠️", "Landis+Gyr", "ME310G1", "Supply concern: requesting 2-week safety stock", "18 hrs ago", TELIT_ORANGE),
        ]
        
        for icon, source, product, message, time, color in signals:
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 15px; background: linear-gradient(135deg, {color}10, {color}05);
                        padding: 12px 15px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid {color};">
                <div style="font-size: 24px;">{icon}</div>
                <div style="flex: 1;">
                    <div style="display: flex; gap: 10px; align-items: center;">
                        <strong>{source}</strong>
                        <span style="background: {TELIT_BLUE}30; padding: 2px 8px; border-radius: 4px; font-size: 11px;">{product}</span>
                    </div>
                    <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 3px;">{message}</div>
                </div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{time}</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Distributor POS data
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📦 Distributor POS Trends (Weekly)")
            weeks = ['W48', 'W49', 'W50', 'W51', 'W52']
            
            fig_pos = go.Figure()
            fig_pos.add_trace(go.Scatter(x=weeks, y=[8200, 8500, 9100, 8800, 7200], name="Digi-Key",
                                        line=dict(color=TELIT_BLUE, width=2), mode='lines+markers'))
            fig_pos.add_trace(go.Scatter(x=weeks, y=[5800, 6200, 6500, 6100, 5500], name="Mouser",
                                        line=dict(color=TELIT_GREEN, width=2), mode='lines+markers'))
            fig_pos.add_trace(go.Scatter(x=weeks, y=[4200, 4500, 4800, 4600, 4100], name="Arrow",
                                        line=dict(color=TELIT_ORANGE, width=2), mode='lines+markers'))
            fig_pos.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40),
                                 yaxis_title="Units Sold", legend=dict(orientation="h", y=1.1))
            st.plotly_chart(fig_pos, use_container_width=True)
        
        with col2:
            st.markdown("##### 🔍 Market Sentiment Indicators")
            indicators = pd.DataFrame({
                "Indicator": ["Google Trends: 'IoT module'", "Google Trends: '5G IoT'", "LinkedIn Job Posts: IoT", "News Sentiment: Telit"],
                "Current": ["78", "92", "1,245", "Positive"],
                "vs Last Month": ["+5%", "+12%", "+8%", "Stable"],
                "Signal": ["📈 Growing", "📈 Strong", "📈 Growing", "✅ Healthy"]
            })
            st.dataframe(indicators, use_container_width=True)
        
        # Competitor activity
        st.markdown("---")
        st.markdown("##### 🏁 Competitor Activity Monitor")
        competitor_cols = st.columns(4)
        competitors = [
            ("Quectel", "New 5G module announced", "Dec 20", "🟡 Monitor", TELIT_ORANGE),
            ("Sierra Wireless", "Q4 guidance lowered", "Dec 18", "🟢 Opportunity", TELIT_GREEN),
            ("u-blox", "Automotive win at VW", "Dec 15", "🟡 Monitor", TELIT_ORANGE),
            ("Fibocom", "Price cut on LTE-M", "Dec 12", "🔴 Threat", TELIT_RED),
        ]
        for col, (comp, news, date, action, color) in zip(competitor_cols, competitors):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; border-top: 3px solid {color};">
                <div style="font-size: 13px; font-weight: 600;">{comp}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin: 8px 0;">{news}</div>
                <div style="display: flex; justify-content: space-between; font-size: 10px;">
                    <span>{date}</span>
                    <span style="color: {color}; font-weight: 600;">{action}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 11: DEMAND HEATMAP
    # =================================================================
    with df_tab11:
        st.subheader("🌡️ Demand Heatmap Visualization")
        
        # Heatmap controls
        heat_col1, heat_col2 = st.columns([3, 1])
        
        with heat_col1:
            st.markdown("##### 📊 Product × Region × Month Demand Heatmap (2025, K units)")
            
            # Create heatmap data
            products = ["FN990A 5G", "ME310G1", "LE910C4", "SE868K3", "Legacy"]
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            
            # Generate heatmap data
            heatmap_data = [
                [85, 92, 98, 105, 112, 118, 115, 122, 128, 135, 142, 148],  # FN990A
                [120, 122, 128, 132, 135, 130, 125, 132, 138, 145, 148, 140],  # ME310G1
                [75, 72, 74, 76, 78, 75, 72, 74, 76, 78, 75, 72],  # LE910C4
                [38, 40, 42, 44, 45, 43, 42, 44, 46, 48, 50, 48],  # SE868K3
                [12, 11, 10, 9, 8, 8, 7, 7, 6, 6, 5, 5],  # Legacy
            ]
            
            fig_heatmap = go.Figure(data=go.Heatmap(
                z=heatmap_data,
                x=months,
                y=products,
                colorscale=[[0, '#e8f4f8'], [0.5, TELIT_BLUE], [1, TELIT_GREEN]],
                text=[[f"{v}K" for v in row] for row in heatmap_data],
                texttemplate="%{text}",
                textfont={"size": 11},
                hovertemplate="Product: %{y}<br>Month: %{x}<br>Demand: %{z}K<extra></extra>"
            ))
            fig_heatmap.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=40))
            st.plotly_chart(fig_heatmap, use_container_width=True)
        
        with heat_col2:
            st.markdown("##### 🎨 Legend")
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="width: 20px; height: 20px; background: {TELIT_GREEN}; border-radius: 4px;"></div>
                    <span>High Demand</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="width: 20px; height: 20px; background: {TELIT_BLUE}; border-radius: 4px;"></div>
                    <span>Medium Demand</span>
                </div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                    <div style="width: 20px; height: 20px; background: #e8f4f8; border-radius: 4px; border: 1px solid #ccc;"></div>
                    <span>Low Demand</span>
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: {TELIT_GRAY};">
                    <strong>Insights:</strong>
                    <div style="margin-top: 5px;">• 5G ramping strongly</div>
                    <div>• Q4 peak visible</div>
                    <div>• Legacy declining</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Regional heatmap
        st.markdown("##### 🌍 Regional Demand Heatmap (Q1 2025, K units)")
        
        regions = ["Americas", "EMEA", "APAC"]
        products_short = ["FN990A", "ME310G1", "LE910C4", "SE868K3"]
        
        regional_data = [
            [125, 105, 75],  # FN990A
            [165, 145, 95],  # ME310G1
            [68, 58, 38],   # LE910C4
            [52, 42, 38],   # SE868K3
        ]
        
        fig_regional_heat = go.Figure(data=go.Heatmap(
            z=regional_data,
            x=regions,
            y=products_short,
            colorscale=[[0, '#ffeee8'], [0.5, TELIT_ORANGE], [1, TELIT_GREEN]],
            text=[[f"{v}K" for v in row] for row in regional_data],
            texttemplate="%{text}",
            textfont={"size": 14},
        ))
        fig_regional_heat.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=40))
        st.plotly_chart(fig_regional_heat, use_container_width=True)
        
        # Customer heatmap
        st.markdown("---")
        st.markdown("##### 🏢 Top Customer × Product Demand Matrix (2025, K units)")
        
        customers_short = ["Landis+Gyr", "BMW", "Itron", "Continental", "NTT", "Honeywell"]
        
        customer_product_data = [
            [0, 420, 0, 0, 0, 0],     # FN990A
            [485, 0, 380, 0, 0, 195],  # ME310G1
            [0, 0, 0, 285, 0, 0],     # LE910C4
            [0, 0, 0, 0, 0, 0],       # SE868K3 (different customers)
        ]
        
        fig_cust_heat = go.Figure(data=go.Heatmap(
            z=customer_product_data,
            x=customers_short,
            y=products_short,
            colorscale=[[0, '#f8f8f8'], [0.3, '#b8dcf0'], [0.6, TELIT_BLUE], [1, TELIT_GREEN]],
            text=[[f"{v}K" if v > 0 else "—" for v in row] for row in customer_product_data],
            texttemplate="%{text}",
            textfont={"size": 12},
        ))
        fig_cust_heat.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=40))
        st.plotly_chart(fig_cust_heat, use_container_width=True)
    
    # =================================================================
    # TAB 12: SCENARIO PLANNING
    # =================================================================
    with df_tab12:
        st.subheader("🔮 Scenario Planning & What-If Analysis")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea20, #764ba210); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="font-size: 18px; font-weight: 700;">⚙️ Adjust Scenario Parameters</div>
            <div style="color: {TELIT_GRAY}; font-size: 14px; margin-top: 8px;">
                Model different market conditions to understand demand sensitivity and plan accordingly.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Scenario inputs
        scenario_col1, scenario_col2, scenario_col3 = st.columns(3)
        
        with scenario_col1:
            st.markdown("##### 📈 Market Assumptions")
            market_growth = st.slider("IoT Market Growth (%)", 5, 25, 15)
            auto_growth = st.slider("Automotive Telematics Growth (%)", 10, 50, 32)
            meter_growth = st.slider("Smart Meter Deployment (%)", 5, 20, 12)
        
        with scenario_col2:
            st.markdown("##### 🏭 Supply Assumptions")
            supply_constraint = st.selectbox("5G Chipset Supply", ["Normal", "Constrained (-15%)", "Severe (-30%)"])
            capacity_util = st.slider("Production Capacity (%)", 70, 100, 85)
            lead_time = st.selectbox("Avg Lead Time", ["Normal (8 weeks)", "Extended (12 weeks)", "Expedited (4 weeks)"])
        
        with scenario_col3:
            st.markdown("##### 💱 Economic Assumptions")
            fx_impact = st.slider("EUR/USD Impact (%)", -10, 10, 0)
            inflation = st.slider("Input Cost Inflation (%)", 0, 15, 5)
            recession_risk = st.selectbox("Recession Scenario", ["None", "Mild (-5%)", "Moderate (-15%)", "Severe (-25%)"])
        
        st.markdown("---")
        
        # Calculate scenario impact
        base_forecast = 4200  # 4.2M units
        market_impact = (market_growth - 15) * 20  # K units per % deviation
        auto_impact = (auto_growth - 32) * 8
        meter_impact = (meter_growth - 12) * 12
        
        supply_impact = 0 if supply_constraint == "Normal" else (-630 if supply_constraint == "Constrained (-15%)" else -1260)
        capacity_impact = (capacity_util - 85) * 15
        
        recession_impact = 0 if recession_risk == "None" else (-210 if recession_risk == "Mild (-5%)" else (-630 if recession_risk == "Moderate (-15%)" else -1050))
        
        scenario_forecast = base_forecast + market_impact + auto_impact + meter_impact + supply_impact + capacity_impact + recession_impact
        
        # Scenario results
        st.markdown("##### 📊 Scenario Results")
        result_cols = st.columns(4)
        
        delta = scenario_forecast - base_forecast
        delta_pct = (delta / base_forecast) * 100
        result_cols[0].metric("Base Forecast", f"{base_forecast/1000:.1f}M units", "Current plan")
        result_cols[1].metric("Scenario Forecast", f"{scenario_forecast/1000:.2f}M units", 
                             f"{'+' if delta > 0 else ''}{delta_pct:.1f}%")
        result_cols[2].metric("Revenue Impact", f"${scenario_forecast * 212 / 1000:.0f}M", 
                             f"{'+' if delta > 0 else ''}{delta * 212 / 1000:.0f}M")
        result_cols[3].metric("Risk Level", "🟢 Low" if abs(delta_pct) < 5 else ("🟡 Medium" if abs(delta_pct) < 15 else "🔴 High"))
        
        # Scenario comparison chart
        st.markdown("---")
        scen_col1, scen_col2 = st.columns(2)
        
        with scen_col1:
            st.markdown("##### 📊 Scenario Comparison")
            scenarios = ["Pessimistic", "Base Case", "Current Scenario", "Optimistic"]
            scen_values = [3400, 4200, scenario_forecast, 5100]
            
            fig_scenarios = go.Figure(go.Bar(
                x=scenarios, y=scen_values,
                marker_color=[TELIT_RED, TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN],
                text=[f"{v/1000:.2f}M" for v in scen_values], textposition="outside"
            ))
            fig_scenarios.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Units (K)")
            st.plotly_chart(fig_scenarios, use_container_width=True)
        
        with scen_col2:
            st.markdown("##### 📋 Impact Breakdown")
            impacts = pd.DataFrame({
                "Factor": ["Market Growth", "Automotive", "Smart Meters", "Supply Constraints", "Capacity", "Economic"],
                "Impact (K units)": [f"{'+' if market_impact >= 0 else ''}{market_impact}", 
                                    f"{'+' if auto_impact >= 0 else ''}{auto_impact}",
                                    f"{'+' if meter_impact >= 0 else ''}{meter_impact}",
                                    f"{supply_impact}" if supply_impact != 0 else "0",
                                    f"{'+' if capacity_impact >= 0 else ''}{capacity_impact}",
                                    f"{recession_impact}" if recession_impact != 0 else "0"],
                "Direction": ["📈" if market_impact > 0 else "📉" if market_impact < 0 else "➡️",
                             "📈" if auto_impact > 0 else "📉" if auto_impact < 0 else "➡️",
                             "📈" if meter_impact > 0 else "📉" if meter_impact < 0 else "➡️",
                             "📉" if supply_impact < 0 else "➡️",
                             "📈" if capacity_impact > 0 else "📉" if capacity_impact < 0 else "➡️",
                             "📉" if recession_impact < 0 else "➡️"]
            })
            st.dataframe(impacts, use_container_width=True)
        
        # Pre-defined scenarios
        st.markdown("---")
        st.markdown("##### 📋 Pre-Defined Scenarios")
        predef_cols = st.columns(4)
        predef_scenarios = [
            ("🌟 Bull Case", "+22%", "5.1M units", "Strong 5G adoption, auto recovery", TELIT_GREEN),
            ("📊 Base Case", "—", "4.2M units", "Current trajectory continues", TELIT_BLUE),
            ("⚠️ Mild Recession", "-12%", "3.7M units", "Economic slowdown, delayed projects", TELIT_ORANGE),
            ("🔴 Supply Crisis", "-25%", "3.2M units", "Severe chip shortage + recession", TELIT_RED),
        ]
        for col, (name, change, forecast, desc, color) in zip(predef_cols, predef_scenarios):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 13px; font-weight: 600; color: {color};">{name}</div>
                <div style="font-size: 20px; font-weight: 700; margin: 8px 0;">{forecast}</div>
                <div style="font-size: 14px; color: {TELIT_GREEN if '+' in change else TELIT_RED if '-' in change else TELIT_GRAY};">{change}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY}; margin-top: 8px;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 8: AI INSIGHTS
    # =================================================================
    with df_tab13:
        st.subheader("🤖 AI-Powered Demand Insights")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🧠</span>
                <div>
                    <div style="font-size: 22px; font-weight: 700; color: white;">Snowflake Cortex AI</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Advanced demand sensing and anomaly detection</div>
                </div>
                <div style="margin-left: auto; text-align: right;">
                    <div style="font-size: 12px; color: rgba(255,255,255,0.7);">Last Analysis</div>
                    <div style="font-size: 16px; font-weight: 600; color: white;">Today, 6:00 AM</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Insights
        st.markdown("##### 💡 Key Insights & Recommendations")
        insights = [
            ("🚀", "5G Demand Acceleration", "FN990A demand is outpacing forecast by 12% in automotive segment. Consider increasing Q2 production plan by 25K units.", TELIT_GREEN, "High Confidence"),
            ("⚠️", "Smart Meter Seasonality", "Q4 2025 smart meter demand may be 15% higher than modeled due to US infrastructure bill deadlines. Recommend safety stock build.", TELIT_ORANGE, "Medium Confidence"),
            ("📉", "Legacy Product Decline", "2G/3G demand declining faster than expected. Recommend accelerating EOL timeline and customer migration programs.", TELIT_RED, "High Confidence"),
            ("🔍", "New Market Opportunity", "Agricultural IoT segment showing 45% growth in APAC. SE868K3 GNSS well-positioned. Consider targeted sales push.", TELIT_BLUE, "Medium Confidence"),
            ("🏭", "Supply-Demand Mismatch", "ME310G1 demand in Americas exceeds regional inventory. Recommend inter-warehouse transfer from Shanghai.", TELIT_ORANGE, "High Confidence"),
        ]
        
        for icon, title, desc, color, confidence in insights:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; margin-bottom: 12px; border-left: 4px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <span style="font-size: 20px; margin-right: 10px;">{icon}</span>
                        <strong style="font-size: 15px;">{title}</strong>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; margin-top: 8px; margin-left: 32px;">{desc}</div>
                    </div>
                    <span style="background: {color}30; color: {color}; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600;">{confidence}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Anomaly detection
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🔔 Demand Anomalies Detected")
            anomalies = pd.DataFrame({
                "Date": ["Dec 23", "Dec 20", "Dec 18", "Dec 15"],
                "Product": ["FN990A28-W1", "ME310G1-WW", "LE910C4-EU", "SE868K3-A"],
                "Customer": ["BMW Group", "Landis+Gyr", "Vodafone", "Trimble"],
                "Anomaly": ["Demand spike +35%", "Order cancellation", "Forecast revision +20%", "New PO +15K units"],
                "Impact": ["🟢 Positive", "🔴 Negative", "🟢 Positive", "🟢 Positive"],
                "Action": ["Increase supply", "Investigate", "Update forecast", "Confirm capacity"]
            })
            st.dataframe(anomalies, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 Forecast Accuracy by Segment")
            segments = ["5G Modules", "LTE-M", "LTE Cat 4", "GNSS", "Legacy"]
            accuracy = [92, 95, 88, 85, 78]
            
            fig_acc = go.Figure(go.Bar(
                x=segments, y=accuracy,
                marker_color=[TELIT_GREEN if a > 90 else TELIT_BLUE if a > 85 else TELIT_ORANGE if a > 80 else TELIT_RED for a in accuracy],
                text=[f"{a}%" for a in accuracy], textposition="outside"
            ))
            fig_acc.add_hline(y=90, line_dash="dash", line_color="green", annotation_text="Target: 90%")
            fig_acc.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Accuracy %", yaxis=dict(range=[70, 100]))
            st.plotly_chart(fig_acc, use_container_width=True)
        
        # AI recommendations summary
        st.markdown("---")
        st.markdown("##### 🎯 AI Action Summary")
        action_cols = st.columns(3)
        actions = [
            ("📈 Upside Opportunities", "3", "+$8.2M potential revenue", TELIT_GREEN, ["Increase FN990A production", "Expand APAC coverage", "Smart meter safety stock"]),
            ("⚠️ Risks to Monitor", "2", "$3.5M at risk", TELIT_ORANGE, ["Legacy migration delays", "Supply constraints"]),
            ("✅ Actions Taken", "5", "This week", TELIT_BLUE, ["Forecast updated", "Alerts generated", "Reports published"]),
        ]
        for col, (title, count, subtitle, color, items) in zip(action_cols, actions):
            items_html = "".join([f"<div style='font-size: 10px; margin: 3px 0;'>• {item}</div>" for item in items])
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 18px; border-top: 4px solid {color};">
                <div style="font-size: 14px; font-weight: 600; color: {color};">{title}</div>
                <div style="font-size: 32px; font-weight: 700; margin: 10px 0;">{count}</div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; margin-bottom: 10px;">{subtitle}</div>
                {items_html}
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# PAGE: SUPPLIERS
# =============================================================================
elif page == "🤝 Suppliers":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">🤝 Supplier Performance Management</h1>
        <p style="opacity: 0.8; color: white;">Comprehensive supplier scorecards, risk assessment, and analytics</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("Active Suppliers", "47", "+3"),
        ("Avg Score", "94.2/100", "+1.8"),
        ("On-Time", "95.8%", "+2.3%"),
        ("Quality", "97.2%", "+1.1%"),
        ("Lead Time", "24 days", "-3 days"),
        ("YTD Spend", "$18.5M", "+12%"),
        ("At Risk", "2", "-1"),
        ("Contracts Due", "5", "90 days")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    sup_tab1, sup_tab2, sup_tab3, sup_tab4, sup_tab5, sup_tab6, sup_tab7, sup_tab8, sup_tab9 = st.tabs([
        "📊 Overview",
        "🏆 Scorecards",
        "📦 Delivery",
        "✅ Quality",
        "💰 Commercial",
        "⚠️ Risk",
        "📋 Contracts",
        "📈 Trends",
        "🤖 AI Insights"
    ])
    
    # =================================================================
    # TAB 1: OVERVIEW
    # =================================================================
    with sup_tab1:
        st.subheader("📊 Supplier Portfolio Overview")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("##### 🌍 Global Supplier Network")
            supplier_locations = pd.DataFrame({
                'Supplier': ['Qualcomm', 'u-blox', 'Skyworks', 'Murata', 'JCET', 'Samsung', 'Infineon', 'STMicro'],
                'lat': [32.88, 47.38, 42.36, 34.69, 31.23, 37.56, 48.26, 45.46],
                'lon': [-117.16, 8.54, -71.06, 135.50, 121.47, 126.98, 11.67, 9.19],
                'Country': ['USA', 'Switzerland', 'USA', 'Japan', 'China', 'South Korea', 'Germany', 'Italy'],
                'Category': ['Chipsets', 'GNSS', 'RF', 'Passives', 'Assembly', 'Memory', 'Power', 'MCU']
            })
            st.map(supplier_locations[['lat', 'lon']], zoom=1)
        
        with col2:
            st.markdown("##### 📊 Supplier Health Distribution")
            health_data = pd.DataFrame({
                "Status": ["🟢 Excellent (>95)", "🟡 Good (85-95)", "🟠 At Risk (70-85)", "🔴 Critical (<70)"],
                "Count": [28, 14, 4, 1]
            })
            
            fig_health = go.Figure(go.Pie(
                labels=health_data["Status"], values=health_data["Count"], hole=0.6,
                marker_colors=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, TELIT_RED]
            ))
            fig_health.add_annotation(text="<b>47</b><br>Suppliers", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_health.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10), showlegend=True,
                                    legend=dict(orientation="h", y=-0.1, font=dict(size=10)))
            st.plotly_chart(fig_health, use_container_width=True)
        
        # Supplier cards - top 6
        st.markdown("---")
        st.markdown("##### 🏆 Strategic Suppliers")
        supplier_cards = st.columns(6)
        strategic_suppliers = [
            ("Qualcomm", "🇺🇸", "Chipsets", 94, "$5.2M", "12 weeks", TELIT_BLUE),
            ("u-blox", "🇨🇭", "GNSS", 96, "$1.8M", "8 weeks", TELIT_GREEN),
            ("Skyworks", "🇺🇸", "RF/PA", 92, "$1.2M", "6 weeks", TELIT_ORANGE),
            ("Murata", "🇯🇵", "Passives", 98, "$0.8M", "4 weeks", TELIT_GREEN),
            ("JCET", "🇨🇳", "Assembly", 91, "$2.4M", "3 weeks", TELIT_ORANGE),
            ("Samsung", "🇰🇷", "Memory", 95, "$1.1M", "8 weeks", TELIT_GREEN),
        ]
        for col, (name, flag, category, score, spend, lead, color) in zip(supplier_cards, strategic_suppliers):
            score_color = TELIT_GREEN if score >= 95 else TELIT_BLUE if score >= 90 else TELIT_ORANGE
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 15px; text-align: center; border-top: 4px solid {color};">
                <div style="font-size: 18px;">{flag}</div>
                <div style="font-size: 14px; font-weight: 700; margin: 5px 0;">{name}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{category}</div>
                <div style="font-size: 24px; font-weight: 700; color: {score_color}; margin: 8px 0;">{score}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{spend} | {lead}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Category breakdown
        st.markdown("---")
        cat_col1, cat_col2 = st.columns(2)
        
        with cat_col1:
            st.markdown("##### 📦 Suppliers by Category")
            categories = ["Chipsets/Modems", "RF Components", "GNSS", "Passives", "Memory", "Assembly/Test", "Connectors", "PCB"]
            cat_counts = [8, 6, 4, 12, 5, 4, 5, 3]
            
            fig_cat = go.Figure(go.Bar(
                x=cat_counts, y=categories, orientation='h',
                marker_color=[TELIT_BLUE, TELIT_GREEN, '#6B5B95', TELIT_ORANGE, '#88B04B', TELIT_GRAY, '#FF6B6B', '#4ECDC4'],
                text=cat_counts, textposition="outside"
            ))
            fig_cat.update_layout(height=300, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="# Suppliers")
            st.plotly_chart(fig_cat, use_container_width=True)
        
        with cat_col2:
            st.markdown("##### 💰 Spend by Category")
            cat_spend = [5.8, 1.8, 1.9, 1.2, 1.5, 3.2, 0.8, 2.3]
            
            fig_spend = go.Figure(go.Pie(
                labels=categories, values=cat_spend, hole=0.5,
                marker_colors=[TELIT_BLUE, TELIT_GREEN, '#6B5B95', TELIT_ORANGE, '#88B04B', TELIT_GRAY, '#FF6B6B', '#4ECDC4']
            ))
            fig_spend.add_annotation(text="<b>$18.5M</b><br>YTD", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_spend.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10), showlegend=False)
            st.plotly_chart(fig_spend, use_container_width=True)
    
    # =================================================================
    # TAB 2: SCORECARDS
    # =================================================================
    with sup_tab2:
        st.subheader("🏆 Supplier Scorecards")
        
        # Supplier selector
        selected_supplier = st.selectbox("Select Supplier", 
            ["Qualcomm", "u-blox", "Skyworks", "Murata", "JCET", "Samsung", "Infineon", "STMicro"])
        
        st.markdown("---")
        
        # Scorecard header
        supplier_data = {
            "Qualcomm": {"flag": "🇺🇸", "category": "Modem Chipsets", "score": 94, "tier": "Strategic", 
                        "metrics": {"Quality": 96, "Delivery": 92, "Cost": 88, "Innovation": 98, "Responsiveness": 95, "Sustainability": 90}},
            "u-blox": {"flag": "🇨🇭", "category": "GNSS Modules", "score": 96, "tier": "Strategic",
                      "metrics": {"Quality": 98, "Delivery": 95, "Cost": 92, "Innovation": 96, "Responsiveness": 97, "Sustainability": 94}},
        }
        
        # Default data for demo
        sup_info = supplier_data.get(selected_supplier, {
            "flag": "🏢", "category": "Components", "score": 92, "tier": "Preferred",
            "metrics": {"Quality": 94, "Delivery": 90, "Cost": 88, "Innovation": 92, "Responsiveness": 93, "Sustainability": 88}
        })
        
        header_col1, header_col2, header_col3 = st.columns([1, 2, 1])
        
        with header_col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10);
                        border-radius: 12px; padding: 20px; text-align: center;">
                <div style="font-size: 48px;">{sup_info['flag']}</div>
                <div style="font-size: 24px; font-weight: 700; margin-top: 10px;">{selected_supplier}</div>
                <div style="font-size: 14px; color: {TELIT_GRAY};">{sup_info['category']}</div>
                <div style="margin-top: 10px;">
                    <span style="background: {TELIT_BLUE}30; color: {TELIT_BLUE}; padding: 4px 12px; border-radius: 12px; font-size: 12px;">
                        {sup_info['tier']}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with header_col2:
            # Radar chart
            categories_radar = list(sup_info['metrics'].keys())
            values_radar = list(sup_info['metrics'].values())
            
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=values_radar + [values_radar[0]],
                theta=categories_radar + [categories_radar[0]],
                fill='toself',
                fillcolor=f'rgba(0, 167, 225, 0.3)',
                line=dict(color=TELIT_BLUE, width=2),
                name=selected_supplier
            ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                height=280, margin=dict(l=60, r=60, t=30, b=30),
                showlegend=False
            )
            st.plotly_chart(fig_radar, use_container_width=True)
        
        with header_col3:
            overall_score = sup_info['score']
            score_color = TELIT_GREEN if overall_score >= 95 else TELIT_BLUE if overall_score >= 90 else TELIT_ORANGE
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {score_color}15, {score_color}05);
                        border-radius: 12px; padding: 20px; text-align: center;">
                <div style="font-size: 14px; color: {TELIT_GRAY};">Overall Score</div>
                <div style="font-size: 56px; font-weight: 700; color: {score_color}; margin: 10px 0;">{overall_score}</div>
                <div style="font-size: 12px; color: {TELIT_GRAY};">/100</div>
                <div style="margin-top: 15px; font-size: 13px; color: {TELIT_GREEN};">📈 +2.3 vs last quarter</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Detailed metrics
        st.markdown("##### 📊 Performance Metrics Detail")
        metric_cols = st.columns(6)
        for col, (metric, value) in zip(metric_cols, sup_info['metrics'].items()):
            color = TELIT_GREEN if value >= 95 else TELIT_BLUE if value >= 90 else TELIT_ORANGE if value >= 80 else TELIT_RED
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 11px; color: {TELIT_GRAY};">{metric}</div>
                <div style="font-size: 28px; font-weight: 700; color: {color}; margin: 5px 0;">{value}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # All suppliers ranking
        st.markdown("---")
        st.markdown("##### 🏅 All Suppliers Ranking")
        all_suppliers = pd.DataFrame({
            "Rank": ["1", "2", "3", "4", "5", "6", "7", "8"],
            "Supplier": ["Murata", "u-blox", "Samsung", "Qualcomm", "Infineon", "STMicro", "Skyworks", "JCET"],
            "Category": ["Passives", "GNSS", "Memory", "Chipsets", "Power", "MCU", "RF", "Assembly"],
            "Score": [98, 96, 95, 94, 93, 92, 92, 91],
            "Quality": ["99%", "98%", "97%", "96%", "95%", "94%", "93%", "92%"],
            "Delivery": ["97%", "95%", "94%", "92%", "94%", "93%", "91%", "90%"],
            "Trend": ["📈 +1", "📈 +2", "➡️ 0", "📈 +1", "📉 -1", "➡️ 0", "📈 +2", "📉 -2"],
            "Status": ["🟢 Excellent", "🟢 Excellent", "🟢 Excellent", "🟢 Excellent", "🟢 Excellent", "🟢 Excellent", "🟡 Good", "🟡 Good"]
        })
        st.dataframe(all_suppliers, use_container_width=True)
    
    # =================================================================
    # TAB 3: DELIVERY PERFORMANCE
    # =================================================================
    with sup_tab3:
        st.subheader("📦 Delivery Performance")
        
        # Delivery KPIs
        del_kpis = st.columns(5)
        del_kpis[0].metric("On-Time Delivery", "95.8%", "+2.3%", help="OTD rate")
        del_kpis[1].metric("In-Full Delivery", "98.2%", "+0.5%", help="OTIF rate")
        del_kpis[2].metric("Avg Lead Time", "24 days", "-3 days", help="Average LT")
        del_kpis[3].metric("Lead Time Variance", "±3.2 days", "-0.8 days", help="Consistency")
        del_kpis[4].metric("Expedite Rate", "4.2%", "-1.1%", help="Rush orders needed")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 On-Time Delivery Trend (12 Months)")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            otd_trend = [92.5, 93.2, 93.8, 94.5, 94.2, 94.8, 95.1, 94.8, 95.5, 95.8, 95.2, 95.8]
            
            fig_otd = go.Figure()
            fig_otd.add_trace(go.Scatter(x=months, y=otd_trend, mode='lines+markers',
                                        line=dict(color=TELIT_BLUE, width=3), fill='tozeroy',
                                        fillcolor='rgba(0, 167, 225, 0.2)'))
            fig_otd.add_hline(y=95, line_dash="dash", line_color=TELIT_GREEN, annotation_text="Target: 95%")
            fig_otd.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="OTD %", yaxis=dict(range=[88, 100]))
            st.plotly_chart(fig_otd, use_container_width=True)
        
        with col2:
            st.markdown("##### 🏆 OTD by Supplier")
            suppliers = ["Murata", "u-blox", "Samsung", "Infineon", "Qualcomm", "Skyworks", "STMicro", "JCET"]
            otd_by_supplier = [98.5, 97.2, 96.8, 95.5, 94.2, 93.8, 92.5, 90.2]
            
            fig_otd_sup = go.Figure(go.Bar(
                x=otd_by_supplier, y=suppliers, orientation='h',
                marker_color=[TELIT_GREEN if o >= 95 else TELIT_BLUE if o >= 92 else TELIT_ORANGE for o in otd_by_supplier],
                text=[f"{o}%" for o in otd_by_supplier], textposition="outside"
            ))
            fig_otd_sup.add_vline(x=95, line_dash="dash", line_color="green", annotation_text="Target")
            fig_otd_sup.update_layout(height=280, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="OTD %", xaxis=dict(range=[85, 102]))
            st.plotly_chart(fig_otd_sup, use_container_width=True)
        
        # Lead time analysis
        st.markdown("---")
        st.markdown("##### ⏱️ Lead Time Analysis")
        lt_cols = st.columns(2)
        
        with lt_cols[0]:
            st.markdown("###### Lead Time by Category")
            lt_categories = ["Chipsets", "Assembly", "Memory", "GNSS", "RF", "Passives"]
            lt_values = [12, 3, 8, 8, 6, 4]
            lt_target = [10, 4, 6, 6, 5, 3]
            
            fig_lt = go.Figure()
            fig_lt.add_trace(go.Bar(name="Actual", x=lt_categories, y=lt_values, marker_color=TELIT_BLUE))
            fig_lt.add_trace(go.Scatter(name="Target", x=lt_categories, y=lt_target, mode='lines+markers',
                                       line=dict(color=TELIT_GREEN, width=2, dash='dash')))
            fig_lt.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Weeks", barmode='group')
            st.plotly_chart(fig_lt, use_container_width=True)
        
        with lt_cols[1]:
            lt_data = pd.DataFrame({
                "Supplier": ["Qualcomm", "JCET", "u-blox", "Samsung", "Murata", "Skyworks"],
                "Standard LT": ["12 weeks", "3 weeks", "8 weeks", "8 weeks", "4 weeks", "6 weeks"],
                "Current LT": ["12 weeks", "3 weeks", "7 weeks", "9 weeks", "4 weeks", "5 weeks"],
                "Variance": ["✅ On Target", "✅ On Target", "🟢 -1 week", "🔴 +1 week", "✅ On Target", "🟢 -1 week"],
                "Expedite": ["$15/unit", "$8/unit", "$12/unit", "$5/unit", "$3/unit", "$10/unit"]
            })
            st.dataframe(lt_data, use_container_width=True)
        
        # Late delivery analysis
        st.markdown("---")
        st.markdown("##### ⚠️ Late Deliveries Analysis (Last 30 Days)")
        late_data = pd.DataFrame({
            "PO #": ["PO-47821", "PO-47815", "PO-47808", "PO-47792", "PO-47785"],
            "Supplier": ["JCET", "Qualcomm", "STMicro", "JCET", "Skyworks"],
            "Part": ["Assembly Service", "SDX55 Modem", "STM32 MCU", "Test Service", "SKY66112 PA"],
            "Days Late": [5, 3, 4, 2, 1],
            "Root Cause": ["Capacity constraint", "Allocation limit", "Raw material delay", "Test equipment down", "Transit delay"],
            "Impact": ["🔴 High", "🔴 High", "🟡 Medium", "🟡 Medium", "🟢 Low"],
            "CAPA": ["Capacity review", "Escalated to VP", "Alternate source", "PM review", "Carrier change"]
        })
        st.dataframe(late_data, use_container_width=True)
    
    # =================================================================
    # TAB 4: QUALITY PERFORMANCE
    # =================================================================
    with sup_tab4:
        st.subheader("✅ Supplier Quality Performance")
        
        # Quality KPIs
        qual_kpis = st.columns(5)
        qual_kpis[0].metric("Incoming Quality", "97.2%", "+1.1%", help="IQC pass rate")
        qual_kpis[1].metric("Avg PPM", "850", "-120", help="Parts per million defects")
        qual_kpis[2].metric("Lot Acceptance", "99.1%", "+0.3%", help="Lots accepted")
        qual_kpis[3].metric("SCAR Open", "3", "-2", help="Supplier corrective actions")
        qual_kpis[4].metric("Cert Compliance", "100%", "—", help="ISO/IATF compliance")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Quality Trend (PPM)")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            ppm_trend = [1200, 1150, 1080, 1020, 980, 950, 920, 900, 880, 860, 850, 850]
            
            fig_ppm = go.Figure()
            fig_ppm.add_trace(go.Scatter(x=months, y=ppm_trend, mode='lines+markers',
                                        line=dict(color=TELIT_GREEN, width=3), fill='tozeroy',
                                        fillcolor='rgba(0, 200, 140, 0.2)'))
            fig_ppm.add_hline(y=1000, line_dash="dash", line_color=TELIT_ORANGE, annotation_text="Target: 1000 PPM")
            fig_ppm.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="PPM")
            st.plotly_chart(fig_ppm, use_container_width=True)
        
        with col2:
            st.markdown("##### 🏆 Quality by Supplier (PPM)")
            suppliers = ["Murata", "Samsung", "u-blox", "Infineon", "Skyworks", "Qualcomm", "STMicro", "JCET"]
            ppm_by_supplier = [150, 320, 450, 580, 720, 890, 1050, 1420]
            
            fig_ppm_sup = go.Figure(go.Bar(
                x=ppm_by_supplier, y=suppliers, orientation='h',
                marker_color=[TELIT_GREEN if p < 500 else TELIT_BLUE if p < 1000 else TELIT_ORANGE if p < 1500 else TELIT_RED for p in ppm_by_supplier],
                text=[f"{p} PPM" for p in ppm_by_supplier], textposition="outside"
            ))
            fig_ppm_sup.add_vline(x=1000, line_dash="dash", line_color="orange", annotation_text="Target")
            fig_ppm_sup.update_layout(height=280, margin=dict(l=10, r=80, t=10, b=10), xaxis_title="PPM")
            st.plotly_chart(fig_ppm_sup, use_container_width=True)
        
        # Defect analysis
        st.markdown("---")
        st.markdown("##### 🔍 Defect Pareto Analysis (YTD)")
        defect_col1, defect_col2 = st.columns([2, 1])
        
        with defect_col1:
            defects = ["Visual/Cosmetic", "Functional Fail", "Dimension OOS", "Documentation", "Packaging", "Marking Error"]
            defect_counts = [245, 180, 142, 98, 65, 42]
            cumulative = np.cumsum(defect_counts) / sum(defect_counts) * 100
            
            fig_pareto = go.Figure()
            fig_pareto.add_trace(go.Bar(x=defects, y=defect_counts, name="Count", marker_color=TELIT_BLUE))
            fig_pareto.add_trace(go.Scatter(x=defects, y=cumulative, name="Cumulative %", yaxis="y2",
                                           mode='lines+markers', line=dict(color=TELIT_ORANGE, width=2)))
            fig_pareto.add_hline(y=80, line_dash="dot", line_color="red", yref="y2", annotation_text="80%")
            fig_pareto.update_layout(height=280, margin=dict(l=20, r=60, t=10, b=60),
                                    yaxis=dict(title="Defect Count"), yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 105]),
                                    xaxis_tickangle=-30)
            st.plotly_chart(fig_pareto, use_container_width=True)
        
        with defect_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">📋 Defect Summary</div>
                <div style="margin-bottom: 10px;">
                    <strong>Total Defects:</strong> 772
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Lots Affected:</strong> 23 (0.9%)
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Top Issue:</strong> Visual/Cosmetic (32%)
                </div>
                <div style="margin-top: 15px; padding: 10px; background: {TELIT_GREEN}20; border-radius: 8px; font-size: 12px;">
                    <strong>Trend:</strong> PPM improving 12% QoQ
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Open SCARs
        st.markdown("---")
        st.markdown("##### 📝 Open Supplier Corrective Actions (SCAR)")
        scar_data = pd.DataFrame({
            "SCAR #": ["SCAR-2024-042", "SCAR-2024-038", "SCAR-2024-035"],
            "Supplier": ["JCET", "STMicro", "Skyworks"],
            "Issue": ["Solder void rate >5%", "MCU firmware bug", "PA gain out of spec"],
            "Severity": ["🔴 Major", "🟡 Minor", "🟡 Minor"],
            "Open Date": ["Dec 15", "Dec 8", "Nov 28"],
            "Due Date": ["Jan 15", "Jan 8", "Dec 28"],
            "Status": ["🔵 In Progress", "🔵 In Progress", "🟢 Pending Closure"],
            "Owner": ["Quality Eng", "R&D", "Quality Eng"]
        })
        st.dataframe(scar_data, use_container_width=True)
    
    # =================================================================
    # TAB 5: COMMERCIAL
    # =================================================================
    with sup_tab5:
        st.subheader("💰 Commercial & Spend Analysis")
        
        # Commercial KPIs
        comm_kpis = st.columns(5)
        comm_kpis[0].metric("YTD Spend", "$18.5M", "+12%", help="Total supplier spend")
        comm_kpis[1].metric("Cost Savings", "$1.2M", "+$0.3M", help="Negotiated savings")
        comm_kpis[2].metric("Avg Price Change", "+2.8%", "vs last year", help="Price inflation")
        comm_kpis[3].metric("Payment Terms", "Net 45", "Avg", help="Average payment terms")
        comm_kpis[4].metric("Open POs", "$8.2M", "124 POs", help="Outstanding orders")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 💵 Monthly Spend Trend")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            spend_trend = [1.2, 1.4, 1.6, 1.8, 1.5, 1.6, 1.8, 1.7, 1.5, 1.6, 1.4, 1.4]
            
            fig_spend = go.Figure()
            fig_spend.add_trace(go.Bar(x=months, y=spend_trend, marker_color=TELIT_BLUE,
                                      text=[f"${s}M" for s in spend_trend], textposition="outside"))
            fig_spend.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Spend ($M)")
            st.plotly_chart(fig_spend, use_container_width=True)
        
        with col2:
            st.markdown("##### 🏢 Spend by Supplier (Top 8)")
            suppliers = ["Qualcomm", "JCET", "u-blox", "PCB Vendor", "Samsung", "Skyworks", "Murata", "Infineon"]
            supplier_spend = [5.2, 2.4, 1.8, 2.3, 1.1, 1.2, 0.8, 0.9]
            
            fig_sup_spend = go.Figure(go.Pie(
                labels=suppliers, values=supplier_spend, hole=0.5,
                marker_colors=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#6B5B95', '#88B04B', TELIT_GRAY, '#FF6B6B', '#4ECDC4']
            ))
            fig_sup_spend.add_annotation(text="<b>$18.5M</b>", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_sup_spend.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_sup_spend, use_container_width=True)
        
        # Price trend analysis
        st.markdown("---")
        st.markdown("##### 📈 Component Price Trends (vs 12 Months Ago)")
        price_cols = st.columns(5)
        price_data = [
            ("Qualcomm SDX55", "+5.2%", "Demand driven", TELIT_RED),
            ("u-blox M10", "+2.1%", "New generation", TELIT_ORANGE),
            ("Murata MLCC", "-3.5%", "Volume discount", TELIT_GREEN),
            ("Samsung Flash", "-8.2%", "Market decline", TELIT_GREEN),
            ("PCB Assembly", "+4.8%", "Labor inflation", TELIT_RED),
        ]
        for col, (component, change, reason, color) in zip(price_cols, price_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 11px; color: {TELIT_GRAY};">{component}</div>
                <div style="font-size: 22px; font-weight: 700; color: {color}; margin: 5px 0;">{change}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{reason}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Savings tracker
        st.markdown("---")
        st.markdown("##### 💰 Cost Savings Initiatives")
        savings_data = pd.DataFrame({
            "Initiative": ["Qualcomm volume tier", "MLCC consolidation", "PCB supplier switch", "Assembly optimization", "Payment term extension"],
            "Supplier": ["Qualcomm", "Murata", "New Vendor", "JCET", "All"],
            "Annual Savings": ["$450K", "$280K", "$220K", "$180K", "$120K"],
            "Status": ["🟢 Achieved", "🟢 Achieved", "🔵 In Progress", "🟡 Negotiating", "🟢 Achieved"],
            "Start Date": ["Jan 2024", "Mar 2024", "Q1 2025", "Q2 2025", "Jul 2024"]
        })
        st.dataframe(savings_data, use_container_width=True)
    
    # =================================================================
    # TAB 6: RISK ASSESSMENT
    # =================================================================
    with sup_tab6:
        st.subheader("⚠️ Supplier Risk Assessment")
        
        # Risk summary
        risk_kpis = st.columns(5)
        risk_kpis[0].metric("Overall Risk", "Medium", "—", help="Portfolio risk level")
        risk_kpis[1].metric("Single Source", "3", "Critical", help="No alternate supplier")
        risk_kpis[2].metric("Geo Concentration", "42%", "Asia", help="Regional concentration")
        risk_kpis[3].metric("Financial Risk", "2", "Suppliers", help="Credit concerns")
        risk_kpis[4].metric("Capacity Risk", "1", "Supplier", help="Allocation constraints")
        
        st.markdown("---")
        
        # Risk matrix
        st.markdown("##### 🎯 Supplier Risk Matrix")
        risk_col1, risk_col2 = st.columns([2, 1])
        
        with risk_col1:
            # Scatter plot risk matrix
            risk_df = pd.DataFrame({
                "Supplier": ["Qualcomm", "u-blox", "Murata", "JCET", "Samsung", "Skyworks", "STMicro", "Infineon"],
                "Impact": [95, 75, 60, 80, 70, 65, 55, 50],  # Business impact if disrupted
                "Probability": [35, 20, 15, 45, 25, 30, 25, 20],  # Probability of issue
                "Spend": [5.2, 1.8, 0.8, 2.4, 1.1, 1.2, 0.9, 0.9]
            })
            
            fig_risk = px.scatter(risk_df, x="Probability", y="Impact", size="Spend", color="Supplier",
                                 hover_data=["Spend"], size_max=40)
            fig_risk.add_hline(y=70, line_dash="dash", line_color="orange")
            fig_risk.add_vline(x=30, line_dash="dash", line_color="orange")
            fig_risk.add_annotation(x=45, y=85, text="HIGH RISK", font=dict(color="red", size=12))
            fig_risk.add_annotation(x=15, y=85, text="WATCH", font=dict(color="orange", size=12))
            fig_risk.add_annotation(x=15, y=35, text="LOW RISK", font=dict(color="green", size=12))
            fig_risk.update_layout(height=350, margin=dict(l=20, r=20, t=10, b=40),
                                  xaxis_title="Risk Probability (%)", yaxis_title="Business Impact (%)")
            st.plotly_chart(fig_risk, use_container_width=True)
        
        with risk_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">🎯 Risk Zones</div>
                <div style="margin-bottom: 12px; padding: 8px; background: {TELIT_RED}20; border-radius: 6px;">
                    <strong style="color: {TELIT_RED};">High Risk:</strong> Immediate action
                </div>
                <div style="margin-bottom: 12px; padding: 8px; background: {TELIT_ORANGE}20; border-radius: 6px;">
                    <strong style="color: {TELIT_ORANGE};">Watch:</strong> Mitigation plan needed
                </div>
                <div style="margin-bottom: 12px; padding: 8px; background: {TELIT_GREEN}20; border-radius: 6px;">
                    <strong style="color: {TELIT_GREEN};">Low Risk:</strong> Monitor quarterly
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Single source analysis
        st.markdown("---")
        st.markdown("##### 🔴 Single Source Components (Critical)")
        single_source = pd.DataFrame({
            "Component": ["Qualcomm SDX55", "Qualcomm SDX62", "u-blox M10 GNSS"],
            "Supplier": ["Qualcomm", "Qualcomm", "u-blox"],
            "Used In": ["FN990A, ME310G1", "FN990A28", "SE868K3"],
            "Annual Spend": ["$4.2M", "$1.8M", "$1.5M"],
            "Risk Level": ["🔴 Critical", "🔴 Critical", "🟡 High"],
            "Mitigation": ["Safety stock 12 weeks", "Dual source evaluation", "MediaTek qualification"],
            "Status": ["🟢 Active", "🔵 In Progress", "🔵 In Progress"]
        })
        st.dataframe(single_source, use_container_width=True)
        
        # Geographic concentration
        st.markdown("---")
        geo_col1, geo_col2 = st.columns(2)
        
        with geo_col1:
            st.markdown("##### 🌍 Geographic Concentration")
            regions = ["Asia (CN, JP, KR)", "North America", "Europe", "Other"]
            geo_spend = [7.8, 6.4, 3.8, 0.5]
            
            fig_geo = go.Figure(go.Pie(
                labels=regions, values=geo_spend, hole=0.5,
                marker_colors=[TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN, TELIT_GRAY]
            ))
            fig_geo.update_layout(height=250, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_geo, use_container_width=True)
        
        with geo_col2:
            st.markdown("##### ⚠️ Geopolitical Risk Factors")
            geo_risks = [
                ("🇨🇳 China supply chain", "Medium", "Tariffs, export controls", TELIT_ORANGE),
                ("🇹🇼 Taiwan concentration", "High", "Semiconductor fab risk", TELIT_RED),
                ("🚢 Red Sea shipping", "Medium", "Transit delays +5-7 days", TELIT_ORANGE),
                ("🇺🇸 US export controls", "Low", "Compliance in place", TELIT_GREEN),
            ]
            for risk, level, impact, color in geo_risks:
                st.markdown(f"""
                <div style="display: flex; justify-content: space-between; align-items: center; 
                            padding: 8px; margin: 5px 0; background: {color}10; border-radius: 6px; border-left: 3px solid {color};">
                    <span>{risk}</span>
                    <span style="background: {color}30; padding: 2px 8px; border-radius: 4px; font-size: 11px; color: {color};">{level}</span>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 7: CONTRACTS
    # =================================================================
    with sup_tab7:
        st.subheader("📋 Contract Management")
        
        # Contract summary
        contract_kpis = st.columns(5)
        contract_kpis[0].metric("Active Contracts", "42", "+3", help="Current contracts")
        contract_kpis[1].metric("Expiring <90 Days", "5", "⚠️", help="Renewals needed")
        contract_kpis[2].metric("Avg Contract Term", "2.4 years", "—", help="Average duration")
        contract_kpis[3].metric("Total Contracted", "$52M", "Annual", help="Contracted spend")
        contract_kpis[4].metric("LTA Coverage", "78%", "+5%", help="Long-term agreements")
        
        st.markdown("---")
        
        # Contracts due for renewal
        st.markdown("##### ⏰ Contracts Expiring Soon")
        expiring = pd.DataFrame({
            "Supplier": ["Skyworks", "JCET", "PCB Vendor", "Infineon", "Connector Co"],
            "Contract Type": ["Supply Agreement", "Assembly MSA", "Frame Agreement", "Supply Agreement", "Distribution"],
            "Expiry Date": ["Jan 31, 2025", "Feb 15, 2025", "Feb 28, 2025", "Mar 15, 2025", "Mar 31, 2025"],
            "Days Left": ["32", "47", "60", "75", "90"],
            "Annual Value": ["$1.2M", "$2.4M", "$2.3M", "$0.9M", "$0.4M"],
            "Renewal Status": ["🟡 Negotiating", "🔵 Draft Review", "🟡 Negotiating", "⚪ Not Started", "⚪ Not Started"],
            "Owner": ["Procurement", "Legal", "Procurement", "Procurement", "Procurement"]
        })
        st.dataframe(expiring, use_container_width=True)
        
        # Contract status overview
        st.markdown("---")
        cont_col1, cont_col2 = st.columns(2)
        
        with cont_col1:
            st.markdown("##### 📊 Contract Status Distribution")
            status_labels = ["Active - Good", "Active - Expiring", "In Renewal", "New Negotiation"]
            status_counts = [32, 5, 3, 2]
            
            fig_status = go.Figure(go.Pie(
                labels=status_labels, values=status_counts, hole=0.5,
                marker_colors=[TELIT_GREEN, TELIT_ORANGE, TELIT_BLUE, TELIT_GRAY]
            ))
            fig_status.add_annotation(text="<b>42</b><br>Contracts", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_status.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_status, use_container_width=True)
        
        with cont_col2:
            st.markdown("##### 📅 Contract Terms")
            terms_data = pd.DataFrame({
                "Term": ["< 1 year", "1-2 years", "2-3 years", "> 3 years"],
                "Count": [8, 15, 12, 7],
                "Value": ["$4.2M", "$18.5M", "$22.1M", "$7.2M"]
            })
            st.dataframe(terms_data, use_container_width=True)
            
            st.markdown(f"""
            <div style="background: {TELIT_BLUE}15; padding: 12px; border-radius: 8px; margin-top: 10px;">
                <strong>💡 Recommendation:</strong> Extend strategic supplier contracts to 3+ years 
                to lock in pricing and secure capacity.
            </div>
            """, unsafe_allow_html=True)
        
        # SLA performance
        st.markdown("---")
        st.markdown("##### 📋 SLA Compliance")
        sla_data = pd.DataFrame({
            "Supplier": ["Qualcomm", "u-blox", "Murata", "JCET", "Samsung"],
            "On-Time SLA": ["≥95%", "≥95%", "≥97%", "≥92%", "≥95%"],
            "Actual": ["94.2%", "97.2%", "98.5%", "90.2%", "96.8%"],
            "Status": ["🟡 Below", "🟢 Met", "🟢 Met", "🔴 Below", "🟢 Met"],
            "Quality SLA": ["<1000 PPM", "<500 PPM", "<200 PPM", "<1500 PPM", "<500 PPM"],
            "Actual PPM": ["890", "450", "150", "1420", "320"],
            "Q Status": ["🟢 Met", "🟢 Met", "🟢 Met", "🟢 Met", "🟢 Met"]
        })
        st.dataframe(sla_data, use_container_width=True)
    
    # =================================================================
    # TAB 8: PERFORMANCE TRENDS
    # =================================================================
    with sup_tab8:
        st.subheader("📈 Historical Performance Trends")
        
        # Trend selector
        trend_supplier = st.selectbox("Select Supplier for Trend Analysis", 
                                     ["All Suppliers", "Qualcomm", "u-blox", "Murata", "JCET", "Samsung"])
        
        st.markdown("---")
        
        # Multi-metric trend
        st.markdown("##### 📊 12-Month Performance Trend")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        fig_trends = go.Figure()
        fig_trends.add_trace(go.Scatter(x=months, y=[92, 93, 93, 94, 94, 95, 95, 95, 96, 96, 95, 96],
                                       name="On-Time %", line=dict(color=TELIT_BLUE, width=2)))
        fig_trends.add_trace(go.Scatter(x=months, y=[95, 95, 96, 96, 96, 97, 97, 97, 97, 97, 97, 97],
                                       name="Quality %", line=dict(color=TELIT_GREEN, width=2)))
        fig_trends.add_trace(go.Scatter(x=months, y=[88, 89, 90, 90, 91, 91, 92, 92, 93, 93, 94, 94],
                                       name="Overall Score", line=dict(color=TELIT_ORANGE, width=2)))
        fig_trends.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40),
                                yaxis_title="Score/Percentage", legend=dict(orientation="h", y=1.1))
        st.plotly_chart(fig_trends, use_container_width=True)
        
        # Quarterly comparison
        st.markdown("---")
        st.markdown("##### 📊 Quarterly Score Comparison")
        
        quarterly_data = pd.DataFrame({
            "Supplier": ["Qualcomm", "u-blox", "Murata", "JCET", "Samsung", "Skyworks", "STMicro", "Infineon"],
            "Q1 2024": [91, 94, 97, 88, 93, 89, 90, 91],
            "Q2 2024": [92, 95, 97, 89, 94, 90, 91, 92],
            "Q3 2024": [93, 95, 98, 90, 94, 91, 91, 92],
            "Q4 2024": [94, 96, 98, 91, 95, 92, 92, 93],
            "Trend": ["📈 +3", "📈 +2", "📈 +1", "📈 +3", "📈 +2", "📈 +3", "📈 +2", "📈 +2"],
            "YoY Change": ["+4.2%", "+2.8%", "+1.5%", "+5.1%", "+3.2%", "+4.5%", "+2.8%", "+2.5%"]
        })
        st.dataframe(quarterly_data, use_container_width=True)
        
        # Improvement tracking
        st.markdown("---")
        imp_col1, imp_col2 = st.columns(2)
        
        with imp_col1:
            st.markdown("##### 📈 Biggest Improvers (YoY)")
            improvers = ["JCET", "Skyworks", "Qualcomm", "Samsung", "STMicro"]
            improvements = [5.1, 4.5, 4.2, 3.2, 2.8]
            
            fig_improve = go.Figure(go.Bar(
                x=improvements, y=improvers, orientation='h',
                marker_color=TELIT_GREEN, text=[f"+{i}%" for i in improvements], textposition="outside"
            ))
            fig_improve.update_layout(height=220, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="YoY Improvement %")
            st.plotly_chart(fig_improve, use_container_width=True)
        
        with imp_col2:
            st.markdown("##### 📉 Needs Improvement")
            st.markdown(f"""
            <div style="background: {TELIT_ORANGE}15; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid {TELIT_ORANGE};">
                <strong>JCET Assembly</strong>
                <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 5px;">
                    On-time delivery below target (90.2% vs 92% SLA). Root cause: capacity constraints.
                </div>
                <div style="font-size: 11px; color: {TELIT_ORANGE}; margin-top: 5px;">Action: Capacity review Q1 2025</div>
            </div>
            <div style="background: {TELIT_ORANGE}15; padding: 15px; border-radius: 10px; border-left: 4px solid {TELIT_ORANGE};">
                <strong>STMicro</strong>
                <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 5px;">
                    Quality PPM above target (1050 vs 1000). Open SCAR for MCU issue.
                </div>
                <div style="font-size: 11px; color: {TELIT_ORANGE}; margin-top: 5px;">Action: SCAR closure by Jan 8</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 9: AI INSIGHTS
    # =================================================================
    with sup_tab9:
        st.subheader("🤖 AI-Powered Supplier Insights")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🧠</span>
                <div>
                    <div style="font-size: 22px; font-weight: 700; color: white;">Supplier Intelligence Engine</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">ML-powered risk detection and optimization recommendations</div>
                </div>
                <div style="margin-left: auto; text-align: right;">
                    <div style="font-size: 12px; color: rgba(255,255,255,0.7);">Insights Generated</div>
                    <div style="font-size: 16px; font-weight: 600; color: white;">Today, 6:00 AM</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Insights
        st.markdown("##### 💡 Key Insights & Recommendations")
        insights = [
            ("🚨", "JCET Capacity Alert", "ML model predicts 85% probability of delivery delays in Q2 due to capacity constraints. Recommend engaging alternate assembly partner.", TELIT_RED, "High Priority"),
            ("💰", "Cost Optimization", "Murata MLCC consolidation opportunity: bundling 5 part numbers could save $180K/year based on volume tier analysis.", TELIT_GREEN, "Action Item"),
            ("📈", "Performance Recognition", "u-blox has maintained 97%+ scores for 4 consecutive quarters. Consider for 'Preferred Supplier' tier upgrade.", TELIT_BLUE, "Positive"),
            ("⚠️", "Single Source Risk", "Qualcomm SDX55 sole source risk elevated. Recommend 16-week safety stock vs current 12 weeks based on demand volatility.", TELIT_ORANGE, "Monitor"),
            ("🔮", "Market Intelligence", "Samsung memory prices projected to drop 12% in Q2 2025. Recommend delaying large POs until Q2 for $95K savings.", TELIT_GREEN, "Opportunity"),
        ]
        
        for icon, title, desc, color, priority in insights:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; margin-bottom: 12px; border-left: 4px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <span style="font-size: 20px; margin-right: 10px;">{icon}</span>
                        <strong style="font-size: 15px;">{title}</strong>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; margin-top: 8px; margin-left: 32px;">{desc}</div>
                    </div>
                    <span style="background: {color}30; color: {color}; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600;">{priority}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Predictive analytics
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Predicted Score Changes (Next Quarter)")
            pred_suppliers = ["JCET", "Skyworks", "Samsung", "Qualcomm", "u-blox"]
            current_scores = [91, 92, 95, 94, 96]
            predicted_scores = [88, 94, 96, 95, 97]
            
            fig_pred = go.Figure()
            fig_pred.add_trace(go.Bar(name="Current", x=pred_suppliers, y=current_scores, marker_color=TELIT_BLUE))
            fig_pred.add_trace(go.Bar(name="Predicted", x=pred_suppliers, y=predicted_scores, marker_color=TELIT_ORANGE))
            fig_pred.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), barmode='group', yaxis=dict(range=[80, 100]))
            st.plotly_chart(fig_pred, use_container_width=True)
        
        with col2:
            st.markdown("##### 🎯 Recommended Actions")
            actions = pd.DataFrame({
                "Priority": ["1", "2", "3", "4", "5"],
                "Action": ["JCET capacity review", "Extend Murata contract", "Dual source SDX55", "Samsung Q2 PO timing", "u-blox tier upgrade"],
                "Expected Benefit": ["Risk mitigation", "$180K savings", "Risk reduction", "$95K savings", "Better pricing"],
                "Owner": ["Supply Chain", "Procurement", "Engineering", "Procurement", "Supplier Mgmt"],
                "Due": ["Jan 15", "Jan 31", "Q1 2025", "Q2 2025", "Feb 1"]
            })
            st.dataframe(actions, use_container_width=True)

# =============================================================================
# PAGE: QUALITY
# =============================================================================
elif page == "✅ Quality":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">✅ Quality Control & Analytics</h1>
        <p style="opacity: 0.8; color: white;">SPC, defect tracking, and continuous improvement for IoT modules</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("First Pass Yield", "98.7%", "+0.3%"),
        ("Final Yield", "99.4%", "+0.2%"),
        ("Defect Rate", "0.8%", "-0.2%"),
        ("DPMO", "3,200", "-180"),
        ("Scrap Rate", "0.3%", "-0.1%"),
        ("Returns (ppm)", "120", "-15"),
        ("Cp Index", "1.42", "+0.08"),
        ("Cpk Index", "1.35", "+0.05")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    q_tab1, q_tab2, q_tab3, q_tab4, q_tab5, q_tab6, q_tab7, q_tab8, q_tab9 = st.tabs([
        "📊 Overview",
        "🔬 SPC Control",
        "🛠️ Defects",
        "🏭 Lines",
        "📦 Incoming",
        "🔍 Testing",
        "📋 NCR/CAPA",
        "📈 Trends",
        "🤖 AI Insights"
    ])
    
    # =================================================================
    # TAB 1: OVERVIEW
    # =================================================================
    with q_tab1:
        st.subheader("📊 Quality Dashboard Overview")
        
        # Quality scorecard
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_GREEN};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">🏆 Quality Performance: EXCELLENT</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">All key metrics within target. Zero customer escapes this month.</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 48px; font-weight: 700; color: {TELIT_GREEN};">A+</div>
                    <div style="color: {TELIT_GRAY}; font-size: 12px;">Quality Grade</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 First Pass Yield Trend (12 Months)")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            fpy_trend = [97.8, 98.0, 98.1, 98.2, 98.3, 98.4, 98.5, 98.5, 98.6, 98.6, 98.7, 98.7]
            
            fig_fpy = go.Figure()
            fig_fpy.add_trace(go.Scatter(x=months, y=fpy_trend, mode='lines+markers',
                                        line=dict(color=TELIT_GREEN, width=3), fill='tozeroy',
                                        fillcolor='rgba(0, 200, 140, 0.2)'))
            fig_fpy.add_hline(y=98.5, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target: 98.5%")
            fig_fpy.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="FPY %", yaxis=dict(range=[97, 100]))
            st.plotly_chart(fig_fpy, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 Quality by Product Family")
            products = ["ME310G1", "FN990A", "LE910C4", "SE868K3"]
            prod_fpy = [99.1, 98.5, 98.8, 99.2]
            prod_colors = [TELIT_GREEN if f >= 98.5 else TELIT_ORANGE for f in prod_fpy]
            
            fig_prod = go.Figure(go.Bar(
                x=products, y=prod_fpy, marker_color=prod_colors,
                text=[f"{f}%" for f in prod_fpy], textposition="outside"
            ))
            fig_prod.add_hline(y=98.5, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target")
            fig_prod.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="FPY %", yaxis=dict(range=[97, 100]))
            st.plotly_chart(fig_prod, use_container_width=True)
        
        # Quality metrics cards
        st.markdown("---")
        st.markdown("##### 🎯 Key Quality Indicators")
        qual_cards = st.columns(5)
        quality_data = [
            ("First Pass Yield", "98.7%", "Target: 98.5%", "🟢 Above", TELIT_GREEN),
            ("DPMO", "3,200", "Target: 4,000", "🟢 Below", TELIT_GREEN),
            ("Customer Returns", "120 ppm", "Target: 200 ppm", "🟢 Below", TELIT_GREEN),
            ("Scrap Cost", "$42K/mo", "Target: $60K", "🟢 Below", TELIT_GREEN),
            ("COPQ", "0.8%", "Target: 1.0%", "🟢 Below", TELIT_GREEN),
        ]
        for col, (metric, value, target, status, color) in zip(qual_cards, quality_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 11px; color: {TELIT_GRAY};">{metric}</div>
                <div style="font-size: 26px; font-weight: 700; color: {color}; margin: 5px 0;">{value}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{target}</div>
                <div style="font-size: 10px; color: {color}; margin-top: 5px;">{status}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Quality summary by stage
        st.markdown("---")
        st.markdown("##### 🔄 Quality by Production Stage")
        stage_cols = st.columns(6)
        stages = [
            ("SMT Assembly", "99.2%", "0.8% reject", TELIT_GREEN),
            ("Reflow Solder", "99.5%", "0.5% rework", TELIT_GREEN),
            ("AOI Inspection", "97.8%", "2.2% false call", TELIT_ORANGE),
            ("Programming", "99.8%", "0.2% fail", TELIT_GREEN),
            ("RF Testing", "99.1%", "0.9% fail", TELIT_GREEN),
            ("Final Test", "99.6%", "0.4% fail", TELIT_GREEN),
        ]
        for col, (stage, yield_val, reject, color) in zip(stage_cols, stages):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 10px; font-weight: 600; color: {color};">{stage}</div>
                <div style="font-size: 22px; font-weight: 700; margin: 5px 0;">{yield_val}</div>
                <div style="font-size: 9px; color: {TELIT_GRAY};">{reject}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 2: SPC CONTROL CHARTS
    # =================================================================
    with q_tab2:
        st.subheader("🔬 Statistical Process Control")
        
        # SPC parameter selector
        spc_col1, spc_col2 = st.columns([1, 3])
        with spc_col1:
            spc_param = st.selectbox("Select Parameter", 
                ["RF Sensitivity (dBm)", "TX Power (dBm)", "Current Draw (mA)", "Solder Paste Height (μm)"])
        
        st.markdown("---")
        
        # X-bar chart
        st.markdown("##### 📊 X-bar Control Chart (Last 25 Subgroups)")
        np.random.seed(42)
        subgroups = list(range(1, 26))
        x_bar_data = [-107.5 + np.random.normal(0, 0.3) for _ in subgroups]
        ucl, lcl, cl = -106.8, -108.2, -107.5
        
        fig_xbar = go.Figure()
        fig_xbar.add_trace(go.Scatter(x=subgroups, y=x_bar_data, mode='lines+markers',
                                     line=dict(color=TELIT_BLUE, width=2), name='X-bar'))
        fig_xbar.add_hline(y=ucl, line_dash="dash", line_color="red", annotation_text="UCL")
        fig_xbar.add_hline(y=lcl, line_dash="dash", line_color="red", annotation_text="LCL")
        fig_xbar.add_hline(y=cl, line_dash="solid", line_color="green", annotation_text="CL")
        
        # Add warning zones
        fig_xbar.add_hrect(y0=cl, y1=ucl, fillcolor="rgba(255,165,0,0.1)", line_width=0)
        fig_xbar.add_hrect(y0=lcl, y1=cl, fillcolor="rgba(255,165,0,0.1)", line_width=0)
        
        fig_xbar.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), 
                              xaxis_title="Subgroup", yaxis_title="X-bar (dBm)")
        st.plotly_chart(fig_xbar, use_container_width=True)
        
        # R chart and capability
        rchart_col, cap_col = st.columns(2)
        
        with rchart_col:
            st.markdown("##### 📈 Range (R) Chart")
            r_data = [0.4 + np.random.normal(0, 0.1) for _ in subgroups]
            r_ucl, r_cl = 0.85, 0.4
            
            fig_r = go.Figure()
            fig_r.add_trace(go.Scatter(x=subgroups, y=r_data, mode='lines+markers',
                                      line=dict(color=TELIT_ORANGE, width=2), name='Range'))
            fig_r.add_hline(y=r_ucl, line_dash="dash", line_color="red", annotation_text="UCL")
            fig_r.add_hline(y=r_cl, line_dash="solid", line_color="green", annotation_text="CL")
            fig_r.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40), 
                               xaxis_title="Subgroup", yaxis_title="Range (dB)")
            st.plotly_chart(fig_r, use_container_width=True)
        
        with cap_col:
            st.markdown("##### 📊 Process Capability")
            # Histogram with spec limits
            capability_data = np.random.normal(-107.5, 0.35, 500)
            
            fig_cap = go.Figure()
            fig_cap.add_trace(go.Histogram(x=capability_data, nbinsx=30, marker_color=TELIT_BLUE, opacity=0.7))
            fig_cap.add_vline(x=-106.5, line_dash="dash", line_color="red", annotation_text="USL")
            fig_cap.add_vline(x=-108.5, line_dash="dash", line_color="red", annotation_text="LSL")
            fig_cap.add_vline(x=-107.5, line_dash="solid", line_color="green", annotation_text="Target")
            fig_cap.update_layout(height=250, margin=dict(l=20, r=20, t=10, b=40), 
                                 xaxis_title="RF Sensitivity (dBm)", yaxis_title="Frequency")
            st.plotly_chart(fig_cap, use_container_width=True)
        
        # Capability indices
        st.markdown("---")
        st.markdown("##### 📋 Process Capability Summary")
        cap_cols = st.columns(4)
        cap_metrics = [
            ("Cp", "1.42", "Process Potential", "🟢 Capable (>1.33)", TELIT_GREEN),
            ("Cpk", "1.35", "Process Capability", "🟢 Capable (>1.33)", TELIT_GREEN),
            ("Pp", "1.38", "Performance Potential", "🟢 Good (>1.25)", TELIT_GREEN),
            ("Ppk", "1.31", "Performance Capability", "🟡 Acceptable (>1.0)", TELIT_ORANGE),
        ]
        for col, (index, value, desc, status, color) in zip(cap_cols, cap_metrics):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 13px; font-weight: 600; color: {color};">{index}</div>
                <div style="font-size: 32px; font-weight: 700; margin: 8px 0;">{value}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{desc}</div>
                <div style="font-size: 10px; color: {color}; margin-top: 5px;">{status}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 3: DEFECT ANALYSIS
    # =================================================================
    with q_tab3:
        st.subheader("🛠️ Defect Analysis")
        
        # Defect KPIs
        def_kpis = st.columns(5)
        def_kpis[0].metric("Total Defects (MTD)", "665", "-45", help="Month to date")
        def_kpis[1].metric("DPMO", "3,200", "-180", help="Defects per million opportunities")
        def_kpis[2].metric("Defect Rate", "0.8%", "-0.2%", help="As % of production")
        def_kpis[3].metric("Top Defect", "Solder Bridge", "32%", help="Most common")
        def_kpis[4].metric("Rework Rate", "1.2%", "-0.3%", help="Units requiring rework")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Defect Pareto Analysis")
            defects = ["Solder Bridge", "Missing Part", "Misalignment", "Cold Solder", "Tombstone", "Insufficient Solder", "Other"]
            defect_counts = [215, 148, 112, 85, 52, 38, 15]
            cumulative = np.cumsum(defect_counts) / sum(defect_counts) * 100
            
            fig_pareto = go.Figure()
            fig_pareto.add_trace(go.Bar(x=defects, y=defect_counts, name="Count", marker_color=TELIT_BLUE))
            fig_pareto.add_trace(go.Scatter(x=defects, y=cumulative, name="Cumulative %", yaxis="y2",
                                           mode='lines+markers', line=dict(color=TELIT_ORANGE, width=2)))
            fig_pareto.add_hline(y=80, line_dash="dot", line_color="red", yref="y2")
            fig_pareto.update_layout(height=300, margin=dict(l=20, r=60, t=10, b=80),
                                    yaxis=dict(title="Count"), yaxis2=dict(title="Cumulative %", overlaying="y", side="right", range=[0, 105]),
                                    xaxis_tickangle=-30)
            st.plotly_chart(fig_pareto, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Defect Trend (Weekly)")
            weeks = [f"W{i}" for i in range(48, 53)] + ["W1", "W2"]
            weekly_defects = [185, 172, 165, 158, 148, 142, 135]
            
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(x=weeks, y=weekly_defects, mode='lines+markers',
                                          line=dict(color=TELIT_GREEN, width=3), fill='tozeroy',
                                          fillcolor='rgba(0, 200, 140, 0.2)'))
            fig_trend.add_hline(y=150, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target")
            fig_trend.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Defects")
            st.plotly_chart(fig_trend, use_container_width=True)
        
        # Defect by location
        st.markdown("---")
        st.markdown("##### 🗺️ Defect Heatmap by PCB Location")
        loc_col1, loc_col2 = st.columns([2, 1])
        
        with loc_col1:
            # Create a simple board representation
            locations = ["U1 (Modem)", "U2 (GNSS)", "U3 (PA)", "U4 (Flash)", "J1 (Antenna)", "C-Array", "L-Section", "Crystal"]
            loc_defects = [45, 28, 52, 18, 35, 85, 42, 12]
            
            fig_loc = go.Figure(go.Bar(
                x=loc_defects, y=locations, orientation='h',
                marker_color=[TELIT_RED if d > 50 else TELIT_ORANGE if d > 30 else TELIT_GREEN for d in loc_defects],
                text=loc_defects, textposition="outside"
            ))
            fig_loc.update_layout(height=300, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="Defect Count")
            st.plotly_chart(fig_loc, use_container_width=True)
        
        with loc_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">🔍 Root Cause Summary</div>
                <div style="margin-bottom: 10px; padding: 8px; background: {TELIT_RED}20; border-radius: 6px;">
                    <strong>C-Array:</strong> Paste volume issue
                </div>
                <div style="margin-bottom: 10px; padding: 8px; background: {TELIT_ORANGE}20; border-radius: 6px;">
                    <strong>U3 (PA):</strong> Component coplanarity
                </div>
                <div style="margin-bottom: 10px; padding: 8px; background: {TELIT_ORANGE}20; border-radius: 6px;">
                    <strong>J1 (Antenna):</strong> Placement accuracy
                </div>
                <div style="margin-top: 15px; font-size: 12px; color: {TELIT_GREEN};">
                    📉 Trend: -18% vs last month
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Defect details table
        st.markdown("---")
        st.markdown("##### 📋 Recent Defects (Last 7 Days)")
        defect_table = pd.DataFrame({
            "Date": ["Dec 28", "Dec 28", "Dec 27", "Dec 27", "Dec 26", "Dec 26", "Dec 25"],
            "Line": ["SMT-1", "SMT-2", "SMT-1", "SMT-2", "SMT-1", "SMT-2", "SMT-1"],
            "Product": ["ME310G1", "FN990A", "ME310G1", "LE910C4", "FN990A", "ME310G1", "SE868K3"],
            "Defect": ["Solder Bridge", "Missing Part", "Cold Solder", "Misalignment", "Solder Bridge", "Tombstone", "Solder Bridge"],
            "Location": ["C-Array", "U2", "L5", "J1", "C-Array", "C12", "C-Array"],
            "Qty": [12, 8, 5, 6, 15, 3, 9],
            "Root Cause": ["Stencil wear", "Feeder jam", "Reflow profile", "Vision cal", "Stencil wear", "Paste issue", "Stencil wear"],
            "Status": ["🟢 Fixed", "🟢 Fixed", "🟢 Fixed", "🔵 In Progress", "🟢 Fixed", "🟢 Fixed", "🟢 Fixed"]
        })
        st.dataframe(defect_table, use_container_width=True)
    
    # =================================================================
    # TAB 4: LINE PERFORMANCE
    # =================================================================
    with q_tab4:
        st.subheader("🏭 Production Line Quality")
        
        # Line selector
        selected_line = st.selectbox("Select Production Line", ["All Lines", "SMT Line 1", "SMT Line 2", "Assembly Line", "Test Line 1"])
        
        st.markdown("---")
        
        # Line comparison
        st.markdown("##### 📊 Line Quality Comparison")
        lines = ["SMT Line 1", "SMT Line 2", "Assembly", "Test Line 1", "Test Line 2"]
        line_fpy = [98.9, 98.5, 99.2, 99.5, 99.4]
        line_dpmo = [2800, 3500, 1800, 1200, 1400]
        
        line_col1, line_col2 = st.columns(2)
        
        with line_col1:
            fig_line_fpy = go.Figure(go.Bar(
                x=lines, y=line_fpy,
                marker_color=[TELIT_GREEN if f >= 98.5 else TELIT_ORANGE for f in line_fpy],
                text=[f"{f}%" for f in line_fpy], textposition="outside"
            ))
            fig_line_fpy.add_hline(y=98.5, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target")
            fig_line_fpy.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=60), yaxis_title="FPY %", 
                                      yaxis=dict(range=[97, 100]), xaxis_tickangle=-30, title_text="First Pass Yield by Line")
            st.plotly_chart(fig_line_fpy, use_container_width=True)
        
        with line_col2:
            fig_line_dpmo = go.Figure(go.Bar(
                x=lines, y=line_dpmo,
                marker_color=[TELIT_GREEN if d <= 3000 else TELIT_ORANGE for d in line_dpmo],
                text=line_dpmo, textposition="outside"
            ))
            fig_line_dpmo.add_hline(y=4000, line_dash="dash", line_color=TELIT_RED, annotation_text="Limit")
            fig_line_dpmo.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=60), yaxis_title="DPMO",
                                       xaxis_tickangle=-30, title_text="DPMO by Line")
            st.plotly_chart(fig_line_dpmo, use_container_width=True)
        
        # Shift comparison
        st.markdown("---")
        st.markdown("##### 🕐 Quality by Shift")
        shift_cols = st.columns(3)
        shifts = [
            ("Day Shift (A)", "98.9%", "2,850 DPMO", "Chen Wei, Maria Santos", TELIT_GREEN),
            ("Evening Shift (B)", "98.6%", "3,200 DPMO", "James Wilson, Yuki Tanaka", TELIT_GREEN),
            ("Night Shift (C)", "98.2%", "3,850 DPMO", "Ahmed Hassan, Klaus Mueller", TELIT_ORANGE),
        ]
        for col, (shift, fpy, dpmo, operators, color) in zip(shift_cols, shifts):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 18px; text-align: center; border-top: 4px solid {color};">
                <div style="font-size: 14px; font-weight: 700; color: {color};">{shift}</div>
                <div style="font-size: 32px; font-weight: 700; margin: 10px 0;">{fpy}</div>
                <div style="font-size: 13px; color: {TELIT_GRAY};">{dpmo}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 10px;">👷 {operators}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Product quality
        st.markdown("---")
        st.markdown("##### 📦 Quality by Product")
        product_quality = pd.DataFrame({
            "Product": ["ME310G1-W1", "ME310G1-WW", "FN990A28-W1", "FN990A28-EU", "LE910C4-NF", "SE868K3-A"],
            "Units Produced": ["12,500", "8,200", "4,500", "3,800", "5,200", "3,100"],
            "FPY": ["99.1%", "99.0%", "98.5%", "98.6%", "98.8%", "99.2%"],
            "DPMO": ["2,400", "2,650", "3,800", "3,500", "3,100", "2,100"],
            "Top Defect": ["Cold Solder", "Solder Bridge", "Misalignment", "Missing Part", "Tombstone", "Solder Bridge"],
            "Trend": ["📈 +0.2%", "📈 +0.1%", "📈 +0.3%", "📈 +0.2%", "📈 +0.1%", "📈 +0.3%"],
            "Status": ["🟢 Excellent", "🟢 Excellent", "🟡 Good", "🟡 Good", "🟢 Excellent", "🟢 Excellent"]
        })
        st.dataframe(product_quality, use_container_width=True)
    
    # =================================================================
    # TAB 5: INCOMING QUALITY
    # =================================================================
    with q_tab5:
        st.subheader("📦 Incoming Quality Control (IQC)")
        
        # IQC KPIs
        iqc_kpis = st.columns(5)
        iqc_kpis[0].metric("Lots Received", "342", "This month")
        iqc_kpis[1].metric("Lots Accepted", "339", "99.1%")
        iqc_kpis[2].metric("Lots Rejected", "3", "0.9%")
        iqc_kpis[3].metric("Supplier PPM", "850", "-120")
        iqc_kpis[4].metric("Skip Lot Rate", "45%", "+5%")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 IQC Results by Supplier")
            suppliers = ["Murata", "u-blox", "Samsung", "Qualcomm", "Skyworks", "JCET"]
            supplier_accept = [99.8, 99.5, 99.2, 98.8, 98.5, 97.2]
            
            fig_iqc = go.Figure(go.Bar(
                x=supplier_accept, y=suppliers, orientation='h',
                marker_color=[TELIT_GREEN if a >= 99 else TELIT_BLUE if a >= 98 else TELIT_ORANGE for a in supplier_accept],
                text=[f"{a}%" for a in supplier_accept], textposition="outside"
            ))
            fig_iqc.add_vline(x=98, line_dash="dash", line_color="orange", annotation_text="Min")
            fig_iqc.update_layout(height=280, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="Acceptance Rate %", xaxis=dict(range=[95, 101]))
            st.plotly_chart(fig_iqc, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Monthly IQC Trend")
            months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            accept_trend = [98.2, 98.5, 98.7, 98.9, 99.0, 99.1]
            
            fig_iqc_trend = go.Figure()
            fig_iqc_trend.add_trace(go.Scatter(x=months, y=accept_trend, mode='lines+markers',
                                              line=dict(color=TELIT_GREEN, width=3)))
            fig_iqc_trend.add_hline(y=99, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target")
            fig_iqc_trend.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Acceptance %", yaxis=dict(range=[97, 100]))
            st.plotly_chart(fig_iqc_trend, use_container_width=True)
        
        # Recent rejections
        st.markdown("---")
        st.markdown("##### ⚠️ Recent Lot Rejections")
        rejections = pd.DataFrame({
            "Date": ["Dec 26", "Dec 22", "Dec 18"],
            "Supplier": ["JCET", "Skyworks", "JCET"],
            "Part Number": ["Assembly Service", "SKY66112 PA", "Assembly Service"],
            "Lot": ["JC-2024-1247", "SK-2024-8821", "JC-2024-1238"],
            "Qty": ["5,000", "2,500", "3,200"],
            "Defect": ["Solder void >5%", "Gain out of spec", "Visual defects"],
            "Action": ["SCAR-042 opened", "RTV to supplier", "SCAR-035 pending"],
            "Status": ["🔵 In Progress", "🟢 Resolved", "🔵 In Progress"]
        })
        st.dataframe(rejections, use_container_width=True)
        
        # Inspection status
        st.markdown("---")
        st.markdown("##### 📋 Today's IQC Queue")
        queue_cols = st.columns(4)
        queue_data = [
            ("Awaiting Inspection", "12 lots", "Est. 4 hours", TELIT_ORANGE),
            ("In Progress", "3 lots", "2 inspectors", TELIT_BLUE),
            ("Passed Today", "18 lots", "98.5% rate", TELIT_GREEN),
            ("On Hold", "2 lots", "Pending docs", TELIT_RED),
        ]
        for col, (status, count, detail, color) in zip(queue_cols, queue_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 11px; color: {TELIT_GRAY};">{status}</div>
                <div style="font-size: 24px; font-weight: 700; color: {color}; margin: 5px 0;">{count}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{detail}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 6: TEST RESULTS
    # =================================================================
    with q_tab6:
        st.subheader("🔍 Test Results & Analysis")
        
        # Test KPIs
        test_kpis = st.columns(5)
        test_kpis[0].metric("Units Tested (MTD)", "37,500", "+8%")
        test_kpis[1].metric("Test Yield", "99.4%", "+0.2%")
        test_kpis[2].metric("RF Test Pass", "99.1%", "+0.1%")
        test_kpis[3].metric("Functional Pass", "99.6%", "+0.2%")
        test_kpis[4].metric("Avg Test Time", "42 sec", "-3 sec")
        
        st.markdown("---")
        
        # Test results by type
        st.markdown("##### 📊 Test Results by Test Type")
        test_col1, test_col2 = st.columns(2)
        
        with test_col1:
            test_types = ["RF Sensitivity", "TX Power", "Current Draw", "GNSS Fix", "Functional", "Programming"]
            test_pass = [99.1, 99.3, 99.5, 99.2, 99.6, 99.8]
            
            fig_test = go.Figure(go.Bar(
                x=test_types, y=test_pass,
                marker_color=[TELIT_GREEN if t >= 99.5 else TELIT_BLUE if t >= 99 else TELIT_ORANGE for t in test_pass],
                text=[f"{t}%" for t in test_pass], textposition="outside"
            ))
            fig_test.add_hline(y=99, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target: 99%")
            fig_test.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=60), yaxis_title="Pass Rate %", 
                                  yaxis=dict(range=[98, 100.5]), xaxis_tickangle=-30)
            st.plotly_chart(fig_test, use_container_width=True)
        
        with test_col2:
            st.markdown("##### 📈 Test Parameter Distribution")
            # RF Sensitivity histogram
            np.random.seed(42)
            rf_data = np.random.normal(-107.5, 0.4, 1000)
            
            fig_rf = go.Figure()
            fig_rf.add_trace(go.Histogram(x=rf_data, nbinsx=40, marker_color=TELIT_BLUE, opacity=0.7, name="RF Sensitivity"))
            fig_rf.add_vline(x=-107, line_dash="dash", line_color="red", annotation_text="Spec: -107 dBm")
            fig_rf.add_vline(x=-107.5, line_dash="solid", line_color="green", annotation_text="Target")
            fig_rf.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), xaxis_title="RF Sensitivity (dBm)", yaxis_title="Count")
            st.plotly_chart(fig_rf, use_container_width=True)
        
        # Test failure analysis
        st.markdown("---")
        st.markdown("##### ⚠️ Test Failure Pareto")
        fail_col1, fail_col2 = st.columns([2, 1])
        
        with fail_col1:
            failures = ["RF Sensitivity Low", "TX Power High", "Current >150mA", "GNSS No Fix", "I2C Fail", "Other"]
            fail_counts = [85, 52, 38, 28, 18, 12]
            
            fig_fail = go.Figure(go.Bar(
                x=failures, y=fail_counts,
                marker_color=[TELIT_RED if f > 50 else TELIT_ORANGE if f > 25 else TELIT_BLUE for f in fail_counts],
                text=fail_counts, textposition="outside"
            ))
            fig_fail.update_layout(height=260, margin=dict(l=20, r=20, t=10, b=80), yaxis_title="Failures", xaxis_tickangle=-30)
            st.plotly_chart(fig_fail, use_container_width=True)
        
        with fail_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">📋 Failure Analysis</div>
                <div style="margin-bottom: 10px;">
                    <strong>Total Failures:</strong> 233
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Fail Rate:</strong> 0.6%
                </div>
                <div style="margin-bottom: 10px;">
                    <strong>Top Issue:</strong> RF Sensitivity (37%)
                </div>
                <div style="margin-top: 15px; padding: 10px; background: {TELIT_BLUE}20; border-radius: 8px; font-size: 12px;">
                    <strong>Root Cause:</strong> Antenna impedance mismatch on batch B-1247
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Test station status
        st.markdown("---")
        st.markdown("##### 🖥️ Test Station Status")
        station_cols = st.columns(5)
        stations = [
            ("RF Test 1", "🟢 Running", "ME310G1", "42 UPH", TELIT_GREEN),
            ("RF Test 2", "🟢 Running", "FN990A", "38 UPH", TELIT_GREEN),
            ("RF Test 3", "🟡 Calibrating", "—", "Est. 15 min", TELIT_ORANGE),
            ("Func Test 1", "🟢 Running", "LE910C4", "65 UPH", TELIT_GREEN),
            ("Func Test 2", "🔴 Down", "Maintenance", "Est. 2 hrs", TELIT_RED),
        ]
        for col, (station, status, product, throughput, color) in zip(station_cols, stations):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-left: 4px solid {color};">
                <div style="font-size: 12px; font-weight: 600;">{station}</div>
                <div style="font-size: 11px; color: {color}; margin: 5px 0;">{status}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{product}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{throughput}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 7: NCR & CAPA
    # =================================================================
    with q_tab7:
        st.subheader("📋 Non-Conformance & Corrective Actions")
        
        # NCR/CAPA KPIs
        ncr_kpis = st.columns(5)
        ncr_kpis[0].metric("Open NCRs", "8", "-2")
        ncr_kpis[1].metric("Open CAPAs", "5", "-1")
        ncr_kpis[2].metric("Avg Closure Time", "12 days", "-3 days")
        ncr_kpis[3].metric("Overdue", "1", "⚠️")
        ncr_kpis[4].metric("Effectiveness", "92%", "+5%")
        
        st.markdown("---")
        
        # NCR status
        st.markdown("##### 📋 Open Non-Conformance Reports")
        ncr_data = pd.DataFrame({
            "NCR #": ["NCR-2024-0892", "NCR-2024-0891", "NCR-2024-0890", "NCR-2024-0888", "NCR-2024-0885"],
            "Date": ["Dec 26", "Dec 24", "Dec 22", "Dec 20", "Dec 18"],
            "Product": ["FN990A", "ME310G1", "LE910C4", "FN990A", "SE868K3"],
            "Issue": ["RF sensitivity OOS", "Solder void >5%", "Visual defect", "TX power drift", "GNSS accuracy"],
            "Qty Affected": ["312", "450", "180", "85", "42"],
            "Disposition": ["Rework", "MRB Review", "Scrap", "Engineering Eval", "Use As-Is"],
            "Owner": ["Quality Eng", "Prod Mgr", "Quality Eng", "RF Eng", "GNSS Eng"],
            "Status": ["🔵 In Progress", "🟡 Pending", "🟢 Closed", "🔵 In Progress", "🟢 Closed"],
            "Days Open": ["2", "4", "6", "8", "10"]
        })
        st.dataframe(ncr_data, use_container_width=True)
        
        # CAPA tracking
        st.markdown("---")
        st.markdown("##### 🔧 Corrective/Preventive Actions (CAPA)")
        capa_col1, capa_col2 = st.columns([2, 1])
        
        with capa_col1:
            capa_data = pd.DataFrame({
                "CAPA #": ["CAPA-2024-042", "CAPA-2024-038", "CAPA-2024-035", "CAPA-2024-032", "CAPA-2024-028"],
                "Source": ["NCR-0892", "Customer", "Audit", "NCR-0880", "Process"],
                "Issue": ["RF cal process", "Field return analysis", "Documentation gap", "Solder profile", "Training gap"],
                "Root Cause": ["Equipment drift", "ESD damage", "Procedure outdated", "Profile mismatch", "New operator"],
                "Action": ["Calibration SOP update", "ESD controls enhanced", "Procedure revision", "Profile optimization", "Training program"],
                "Due Date": ["Jan 15", "Jan 8", "Dec 28", "Closed", "Closed"],
                "Status": ["🔵 In Progress", "🔵 In Progress", "🟢 Verify", "🟢 Closed", "🟢 Closed"],
                "Effectiveness": ["—", "—", "Pending", "95%", "100%"]
            })
            st.dataframe(capa_data, use_container_width=True)
        
        with capa_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0); border-radius: 12px; padding: 20px;">
                <div style="font-size: 15px; font-weight: 600; margin-bottom: 15px;">📊 CAPA Summary</div>
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>Open:</span><strong>5</strong>
                    </div>
                </div>
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>Overdue:</span><strong style="color: {TELIT_RED};">1</strong>
                    </div>
                </div>
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>Closed YTD:</span><strong>42</strong>
                    </div>
                </div>
                <div style="margin-bottom: 12px;">
                    <div style="display: flex; justify-content: space-between;">
                        <span>Effectiveness:</span><strong style="color: {TELIT_GREEN};">92%</strong>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # CAPA aging
        st.markdown("---")
        aging_col1, aging_col2 = st.columns(2)
        
        with aging_col1:
            st.markdown("##### ⏱️ CAPA Aging Distribution")
            aging = ["< 7 days", "7-14 days", "15-30 days", "> 30 days"]
            aging_counts = [2, 2, 0, 1]
            
            fig_aging = go.Figure(go.Bar(
                x=aging, y=aging_counts,
                marker_color=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, TELIT_RED]
            ))
            fig_aging.update_layout(height=220, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Count")
            st.plotly_chart(fig_aging, use_container_width=True)
        
        with aging_col2:
            st.markdown("##### 📈 CAPA Trend (Monthly)")
            months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            opened = [8, 7, 6, 5, 6, 4]
            closed = [7, 8, 7, 6, 7, 5]
            
            fig_capa_trend = go.Figure()
            fig_capa_trend.add_trace(go.Bar(name="Opened", x=months, y=opened, marker_color=TELIT_ORANGE))
            fig_capa_trend.add_trace(go.Bar(name="Closed", x=months, y=closed, marker_color=TELIT_GREEN))
            fig_capa_trend.update_layout(height=220, margin=dict(l=20, r=20, t=10, b=40), barmode='group')
            st.plotly_chart(fig_capa_trend, use_container_width=True)
    
    # =================================================================
    # TAB 8: TRENDS
    # =================================================================
    with q_tab8:
        st.subheader("📈 Quality Trends & Benchmarks")
        
        # Long-term trends
        st.markdown("##### 📊 12-Month Quality Trend")
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        
        fig_trends = go.Figure()
        fig_trends.add_trace(go.Scatter(x=months, y=[97.8, 98.0, 98.1, 98.2, 98.3, 98.4, 98.5, 98.5, 98.6, 98.6, 98.7, 98.7],
                                       name="FPY %", line=dict(color=TELIT_GREEN, width=3)))
        fig_trends.add_trace(go.Scatter(x=months, y=[1.2, 1.1, 1.0, 0.95, 0.92, 0.90, 0.88, 0.85, 0.82, 0.80, 0.78, 0.80],
                                       name="Defect Rate %", yaxis="y2", line=dict(color=TELIT_ORANGE, width=2)))
        fig_trends.update_layout(height=300, margin=dict(l=20, r=60, t=10, b=40),
                                yaxis=dict(title="FPY %", range=[97, 100]),
                                yaxis2=dict(title="Defect Rate %", overlaying="y", side="right", range=[0, 1.5]),
                                legend=dict(orientation="h", y=1.1))
        st.plotly_chart(fig_trends, use_container_width=True)
        
        # YoY comparison
        st.markdown("---")
        st.markdown("##### 📊 Year-over-Year Comparison")
        yoy_data = pd.DataFrame({
            "Metric": ["First Pass Yield", "Final Yield", "Defect Rate", "DPMO", "Scrap Rate", "Customer Returns", "COPQ"],
            "2023": ["97.5%", "98.8%", "1.2%", "4,500", "0.5%", "180 ppm", "1.2%"],
            "2024": ["98.7%", "99.4%", "0.8%", "3,200", "0.3%", "120 ppm", "0.8%"],
            "Change": ["📈 +1.2%", "📈 +0.6%", "📉 -0.4%", "📉 -1,300", "📉 -0.2%", "📉 -60 ppm", "📉 -0.4%"],
            "Status": ["🟢 Improved", "🟢 Improved", "🟢 Improved", "🟢 Improved", "🟢 Improved", "🟢 Improved", "🟢 Improved"]
        })
        st.dataframe(yoy_data, use_container_width=True)
        
        # Benchmark comparison
        st.markdown("---")
        st.markdown("##### 🏆 Industry Benchmark Comparison")
        bench_col1, bench_col2 = st.columns(2)
        
        with bench_col1:
            metrics = ["FPY", "DPMO", "Scrap", "Returns"]
            telit = [98.7, 3200, 0.3, 120]
            benchmark = [97.5, 5000, 0.5, 200]
            best_class = [99.2, 2000, 0.2, 80]
            
            fig_bench = go.Figure()
            x = np.arange(len(metrics))
            fig_bench.add_trace(go.Bar(name="Telit", x=metrics, y=[100, 100, 100, 100], marker_color=TELIT_GREEN))
            fig_bench.add_trace(go.Bar(name="Industry Avg", x=metrics, y=[97.5/98.7*100, 3200/5000*100, 0.3/0.5*100, 120/200*100], marker_color=TELIT_GRAY))
            fig_bench.update_layout(height=260, margin=dict(l=20, r=20, t=10, b=40), barmode='group',
                                   yaxis_title="% (Telit = 100)", title_text="Performance vs Industry (Higher = Better)")
            st.plotly_chart(fig_bench, use_container_width=True)
        
        with bench_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); border-radius: 12px; padding: 20px; border-left: 5px solid {TELIT_GREEN};">
                <div style="font-size: 16px; font-weight: 700; color: {TELIT_GREEN}; margin-bottom: 15px;">🏆 Telit vs Benchmark</div>
                <div style="margin-bottom: 10px;">
                    ✅ <strong>FPY:</strong> 1.2% above industry average
                </div>
                <div style="margin-bottom: 10px;">
                    ✅ <strong>DPMO:</strong> 36% better than average
                </div>
                <div style="margin-bottom: 10px;">
                    ✅ <strong>Scrap:</strong> 40% lower than average
                </div>
                <div style="margin-bottom: 10px;">
                    ✅ <strong>Returns:</strong> 40% lower than average
                </div>
                <div style="margin-top: 15px; font-size: 13px; color: {TELIT_GRAY};">
                    Source: IPC Industry Benchmark 2024
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 9: AI INSIGHTS
    # =================================================================
    with q_tab9:
        st.subheader("🤖 AI-Powered Quality Insights")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🧠</span>
                <div>
                    <div style="font-size: 22px; font-weight: 700; color: white;">Quality Intelligence Engine</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">Predictive defect detection and process optimization</div>
                </div>
                <div style="margin-left: auto; text-align: right;">
                    <div style="font-size: 12px; color: rgba(255,255,255,0.7);">Last Analysis</div>
                    <div style="font-size: 16px; font-weight: 600; color: white;">Today, 6:00 AM</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Insights
        st.markdown("##### 💡 Key Insights & Predictions")
        insights = [
            ("🔮", "Predictive Alert", "ML model detects elevated solder bridge risk on SMT Line 2. Stencil approaching 80% lifecycle. Recommend replacement within 48 hours.", TELIT_ORANGE, "High Priority"),
            ("📉", "Trend Detection", "RF test failures increased 0.3% in last 3 days. Pattern matches antenna impedance drift. Recommend fixture calibration check.", TELIT_ORANGE, "Monitor"),
            ("🟢", "Process Improvement", "Reflow profile optimization on Line 1 reduced cold solder defects by 42%. Recommend rolling out to Line 2.", TELIT_GREEN, "Positive"),
            ("📊", "Capability Shift", "Cpk for TX power has decreased from 1.45 to 1.35 over 2 weeks. Still within spec but trending. Root cause: ambient temperature variation.", TELIT_BLUE, "Watch"),
            ("💡", "Efficiency Gain", "AI analysis shows 15% test time reduction possible by optimizing RF test sequence. Estimated $45K annual savings.", TELIT_GREEN, "Opportunity"),
        ]
        
        for icon, title, desc, color, priority in insights:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; margin-bottom: 12px; border-left: 4px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <span style="font-size: 20px; margin-right: 10px;">{icon}</span>
                        <strong style="font-size: 15px;">{title}</strong>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; margin-top: 8px; margin-left: 32px;">{desc}</div>
                    </div>
                    <span style="background: {color}30; color: {color}; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600;">{priority}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Predictive quality
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Predicted FPY (Next 7 Days)")
            days = ['Today', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
            predicted_fpy = [98.7, 98.6, 98.5, 98.4, 98.5, 98.6, 98.7]
            confidence_upper = [98.9, 98.9, 98.8, 98.7, 98.8, 98.9, 99.0]
            confidence_lower = [98.5, 98.3, 98.2, 98.1, 98.2, 98.3, 98.4]
            
            fig_pred = go.Figure()
            fig_pred.add_trace(go.Scatter(x=days, y=confidence_upper, fill=None, mode='lines',
                                         line=dict(color='rgba(0,167,225,0.1)'), showlegend=False))
            fig_pred.add_trace(go.Scatter(x=days, y=confidence_lower, fill='tonexty', mode='lines',
                                         line=dict(color='rgba(0,167,225,0.1)'), fillcolor='rgba(0,167,225,0.2)', name='95% CI'))
            fig_pred.add_trace(go.Scatter(x=days, y=predicted_fpy, mode='lines+markers',
                                         line=dict(color=TELIT_BLUE, width=3), name='Predicted FPY'))
            fig_pred.add_hline(y=98.5, line_dash="dash", line_color="green", annotation_text="Target")
            fig_pred.update_layout(height=260, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="FPY %", yaxis=dict(range=[97.5, 99.5]))
            st.plotly_chart(fig_pred, use_container_width=True)
        
        with col2:
            st.markdown("##### 🎯 AI Recommended Actions")
            actions = pd.DataFrame({
                "Priority": ["1", "2", "3", "4"],
                "Action": ["Replace SMT-2 stencil", "Calibrate RF test fixture", "Roll out reflow profile", "Optimize test sequence"],
                "Expected Impact": ["-45 defects/week", "-0.3% fail rate", "-42% cold solder", "15% faster"],
                "Effort": ["Low", "Medium", "Low", "High"],
                "Due": ["Dec 30", "Jan 2", "Jan 5", "Jan 15"]
            })
            st.dataframe(actions, use_container_width=True)

# =============================================================================
# PAGE: TRACEABILITY
# =============================================================================
elif page == "🔗 Traceability":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">🔗 Component Traceability</h1>
        <p style="opacity: 0.8; color: white;">End-to-end tracking from raw materials to customer delivery</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("Units Traced", "2.8M", "YTD"),
        ("Lots Active", "1,247", "+42"),
        ("Components", "85", "unique"),
        ("Suppliers", "47", "tracked"),
        ("Trace Time", "<2 sec", "avg"),
        ("Data Points", "12.5M", "+850K"),
        ("Recalls", "0", "YTD"),
        ("Compliance", "100%", "✓")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    tr_tab1, tr_tab2, tr_tab3, tr_tab4, tr_tab5, tr_tab6, tr_tab7 = st.tabs([
        "🔍 Lookup",
        "📦 Genealogy",
        "🏭 Production",
        "📋 BOM",
        "🚚 Shipments",
        "⚠️ Recalls",
        "📊 Analytics"
    ])
    
    # =================================================================
    # TAB 1: UNIT LOOKUP
    # =================================================================
    with tr_tab1:
        st.subheader("🔍 Unit Traceability Lookup")
        
        # Search interface
        search_col1, search_col2, search_col3 = st.columns([2, 1, 1])
        with search_col1:
            serial_search = st.text_input("🔍 Enter Serial Number, Lot ID, or Work Order", value="ME310G1-W1-2024-12847")
        with search_col2:
            search_type = st.selectbox("Search Type", ["Serial Number", "Lot ID", "Work Order", "Customer PO"])
        with search_col3:
            st.write("")
            st.write("")
            st.button("🔍 Search", use_container_width=True)
        
        st.markdown("---")
        
        if serial_search:
            # Unit card
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10);
                        border-radius: 12px; padding: 20px; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-size: 12px; color: {TELIT_GRAY};">Serial Number</div>
                        <div style="font-size: 24px; font-weight: 700;">{serial_search}</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 12px; color: {TELIT_GRAY};">Product</div>
                        <div style="font-size: 18px; font-weight: 600;">ME310G1-W1</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 12px; color: {TELIT_GRAY};">Build Date</div>
                        <div style="font-size: 18px; font-weight: 600;">Dec 28, 2024</div>
                    </div>
                    <div style="text-align: center;">
                        <div style="font-size: 12px; color: {TELIT_GRAY};">Status</div>
                        <div style="font-size: 18px; font-weight: 600; color: {TELIT_GREEN};">✅ Shipped</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("##### 🧩 Component Genealogy")
                components = pd.DataFrame({
                    "Component": ["Qualcomm MDM9207", "Samsung K4B4G16", "u-blox M10", "Skyworks PA", "Murata MLCC Array", "PCB Assembly"],
                    "Supplier Lot": ["QC-2024-A4521", "SS-2024-M8832", "UB-2024-G2341", "SK-2024-P9912", "MU-2024-C5521", "PCB-2024-12847"],
                    "Date Code": ["2448", "2447", "2448", "2446", "2448", "2449"],
                    "Country": ["🇺🇸 USA", "🇰🇷 Korea", "🇨🇭 Swiss", "🇺🇸 USA", "🇯🇵 Japan", "🇨🇳 China"],
                    "Status": ["✅", "✅", "✅", "✅", "✅", "✅"]
                })
                st.dataframe(components, use_container_width=True)
            
            with col2:
                st.markdown("##### 🔄 Process History")
                process = pd.DataFrame({
                    "Step": ["1. SMT Assembly", "2. Reflow Solder", "3. AOI Inspection", "4. Programming", "5. RF Calibration", "6. Functional Test", "7. Final QC", "8. Packaging"],
                    "Station": ["SMT-L1", "RO-1", "AOI-1", "PRG-2", "RF-3", "FT-1", "QC-2", "PKG-1"],
                    "Time": ["08:15", "08:42", "08:48", "09:05", "09:28", "09:52", "10:08", "10:15"],
                    "Result": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"],
                    "Operator": ["Chen W.", "Auto", "Auto", "Maria S.", "James W.", "Yuki T.", "Priya P.", "Lisa C."]
                })
                st.dataframe(process, use_container_width=True)
            
            # Test results
            st.markdown("---")
            st.markdown("##### 📊 Test Results")
            test_cols = st.columns(6)
            test_results = [
                ("RF Sensitivity", "-108.2 dBm", "Spec: ≥-107", TELIT_GREEN),
                ("TX Power", "23.1 dBm", "Spec: 23±1", TELIT_GREEN),
                ("Current Draw", "142 mA", "Spec: <150", TELIT_GREEN),
                ("GNSS TTFF", "28 sec", "Spec: <35", TELIT_GREEN),
                ("EVM", "-38 dB", "Spec: <-35", TELIT_GREEN),
                ("Overall", "PASS", "47/47 tests", TELIT_GREEN),
            ]
            for col, (test, value, spec, color) in zip(test_cols, test_results):
                col.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}15, {color}05);
                            border-radius: 8px; padding: 10px; text-align: center; border-top: 3px solid {color};">
                    <div style="font-size: 10px; color: {TELIT_GRAY};">{test}</div>
                    <div style="font-size: 18px; font-weight: 700; color: {color};">{value}</div>
                    <div style="font-size: 9px; color: {TELIT_GRAY};">{spec}</div>
                </div>
                """, unsafe_allow_html=True)
            
            # Shipping info
            st.markdown("---")
            st.markdown("##### 🚚 Shipping & Customer")
            ship_cols = st.columns(5)
            ship_cols[0].metric("Customer", "Landis+Gyr")
            ship_cols[1].metric("Ship Date", "Dec 28, 2024")
            ship_cols[2].metric("Carrier", "DHL Express")
            ship_cols[3].metric("Tracking", "1234567890")
            ship_cols[4].metric("Delivered", "Dec 30, 2024")
    
    # =================================================================
    # TAB 2: GENEALOGY
    # =================================================================
    with tr_tab2:
        st.subheader("📦 Product Genealogy Tree")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10);
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="font-size: 18px; font-weight: 700;">🌳 Genealogy for Lot: LOT-2024-12847</div>
            <div style="color: {TELIT_GRAY}; font-size: 14px;">ME310G1-W1 • 5,000 units • Build Date: Dec 28, 2024</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visual genealogy tree
        st.markdown("##### 📊 Component Hierarchy")
        genealogy_data = pd.DataFrame({
            "Level": ["L0 - Finished Good", "L1 - Sub-Assembly", "L1 - Sub-Assembly", "L2 - Component", "L2 - Component", "L2 - Component", "L2 - Component", "L3 - Raw Material"],
            "Item": ["ME310G1-W1 Module", "RF Front-End Assy", "Digital Core Assy", "Qualcomm MDM9207", "u-blox M10 GNSS", "Samsung Flash", "Skyworks PA", "Silicon Wafer"],
            "Supplier/Source": ["Telit Trieste", "Telit Shanghai", "Telit Shanghai", "Qualcomm USA", "u-blox Switzerland", "Samsung Korea", "Skyworks USA", "TSMC Taiwan"],
            "Lot/Batch": ["LOT-2024-12847", "RF-2024-8821", "DC-2024-7712", "QC-2024-A4521", "UB-2024-G2341", "SS-2024-M8832", "SK-2024-P9912", "TS-2024-W4421"],
            "Quantity": ["5,000", "5,000", "5,000", "5,000", "5,000", "5,000", "5,000", "12 wafers"],
            "Status": ["✅ Complete", "✅ Complete", "✅ Complete", "✅ Verified", "✅ Verified", "✅ Verified", "✅ Verified", "✅ Verified"]
        })
        st.dataframe(genealogy_data, use_container_width=True)
        
        # Where-used analysis
        st.markdown("---")
        st.markdown("##### 🔍 Where-Used Analysis (Qualcomm MDM9207 Lot QC-2024-A4521)")
        where_used = pd.DataFrame({
            "Product": ["ME310G1-W1", "ME310G1-WW", "ME310G1-EU"],
            "Lot": ["LOT-2024-12847", "LOT-2024-12852", "LOT-2024-12861"],
            "Quantity": ["5,000", "3,200", "2,800"],
            "Build Date": ["Dec 28", "Dec 29", "Dec 30"],
            "Customer": ["Landis+Gyr", "Itron", "Vodafone"],
            "Status": ["✅ Shipped", "📦 In Transit", "🏭 Production"]
        })
        st.dataframe(where_used, use_container_width=True)
    
    # =================================================================
    # TAB 3: PRODUCTION TRACEABILITY
    # =================================================================
    with tr_tab3:
        st.subheader("🏭 Production Traceability")
        
        # Production KPIs
        prod_kpis = st.columns(5)
        prod_kpis[0].metric("Today's Production", "4,250", "+320")
        prod_kpis[1].metric("Lots in Progress", "12", "+2")
        prod_kpis[2].metric("Lots Completed", "8", "Today")
        prod_kpis[3].metric("Avg Cycle Time", "4.2 hrs", "-0.3 hrs")
        prod_kpis[4].metric("Trace Accuracy", "99.98%", "+0.02%")
        
        st.markdown("---")
        
        # Live production
        st.markdown("##### 📊 Active Production Lots")
        active_lots = pd.DataFrame({
            "Lot ID": ["LOT-2024-12892", "LOT-2024-12891", "LOT-2024-12890", "LOT-2024-12889", "LOT-2024-12888"],
            "Product": ["FN990A28-W1", "ME310G1-W1", "LE910C4-NF", "SE868K3-A", "ME310G1-WW"],
            "Qty": ["2,500", "5,000", "3,200", "1,800", "4,500"],
            "Current Stage": ["🔧 RF Calibration", "📋 Final QC", "⚡ Programming", "🔬 Testing", "📦 Packaging"],
            "Progress": ["65%", "92%", "45%", "78%", "98%"],
            "Start Time": ["06:00", "04:30", "07:15", "05:45", "03:00"],
            "ETA Complete": ["14:00", "11:30", "15:45", "12:30", "10:00"],
            "Operator": ["Team A", "Team A", "Team B", "Team A", "Team A"]
        })
        st.dataframe(active_lots, use_container_width=True)
        
        # Production flow visualization
        st.markdown("---")
        st.markdown("##### 🔄 Production Flow (LOT-2024-12891)")
        flow_cols = st.columns(8)
        stages = [
            ("SMT", "✅", "08:15", TELIT_GREEN),
            ("Reflow", "✅", "08:42", TELIT_GREEN),
            ("AOI", "✅", "08:58", TELIT_GREEN),
            ("Program", "✅", "09:25", TELIT_GREEN),
            ("RF Cal", "✅", "09:52", TELIT_GREEN),
            ("Test", "✅", "10:28", TELIT_GREEN),
            ("QC", "🔄", "Now", TELIT_BLUE),
            ("Pack", "⏳", "—", TELIT_GRAY),
        ]
        for col, (stage, status, time, color) in zip(flow_cols, stages):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}20, {color}10);
                        border-radius: 8px; padding: 10px; text-align: center;">
                <div style="font-size: 20px;">{status}</div>
                <div style="font-size: 11px; font-weight: 600;">{stage}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{time}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 4: BOM TRACEABILITY
    # =================================================================
    with tr_tab4:
        st.subheader("📋 Bill of Materials Traceability")
        
        product_select = st.selectbox("Select Product", ["ME310G1-W1", "FN990A28-W1", "LE910C4-NF", "SE868K3-A"])
        
        st.markdown("---")
        
        st.markdown(f"##### 📦 BOM for {product_select}")
        bom_data = pd.DataFrame({
            "Item #": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            "Component": ["Qualcomm MDM9207", "u-blox M10 GNSS", "Samsung K4B4G16", "Skyworks SKY78130", "Murata MLCC Array", "TDK Ferrite", "PCB (6-layer)", "RF Shield", "Antenna Connector", "ESD Protection"],
            "Supplier": ["Qualcomm", "u-blox", "Samsung", "Skyworks", "Murata", "TDK", "PCB Vendor", "Laird", "Hirose", "Nexperia"],
            "Qty/Unit": ["1", "1", "1", "1", "45", "12", "1", "1", "1", "4"],
            "Unit Cost": ["$42.50", "$8.20", "$3.15", "$2.80", "$0.85", "$0.12", "$4.50", "$0.95", "$0.45", "$0.08"],
            "Lead Time": ["12 wks", "8 wks", "8 wks", "6 wks", "4 wks", "4 wks", "3 wks", "2 wks", "2 wks", "4 wks"],
            "Alt Source": ["—", "MediaTek", "Micron", "Qorvo", "Yageo", "—", "Yes", "Yes", "—", "Yes"],
            "Critical": ["🔴 Yes", "🟡 Med", "🟢 No", "🟢 No", "🟢 No", "🟢 No", "🟢 No", "🟢 No", "🟢 No", "🟢 No"]
        })
        st.dataframe(bom_data, use_container_width=True)
        
        # BOM cost breakdown
        st.markdown("---")
        bom_col1, bom_col2 = st.columns(2)
        
        with bom_col1:
            st.markdown("##### 💰 BOM Cost Breakdown")
            cost_items = ["Modem/Chipset", "GNSS", "Memory", "RF Components", "Passives", "PCB/Mechanical", "Other"]
            cost_values = [42.50, 8.20, 3.15, 3.75, 4.20, 5.90, 2.30]
            
            fig_bom = go.Figure(go.Pie(
                labels=cost_items, values=cost_values, hole=0.5,
                marker_colors=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#6B5B95', '#88B04B', TELIT_GRAY, '#FF6B6B']
            ))
            fig_bom.add_annotation(text="<b>$70.00</b><br>Total", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_bom.update_layout(height=280, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_bom, use_container_width=True)
        
        with bom_col2:
            st.markdown("##### 📊 Supplier Concentration")
            suppliers = ["Qualcomm", "u-blox", "Samsung", "Others"]
            supplier_pct = [61, 12, 5, 22]
            
            fig_supplier = go.Figure(go.Bar(
                x=suppliers, y=supplier_pct, marker_color=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, TELIT_GRAY],
                text=[f"{p}%" for p in supplier_pct], textposition="outside"
            ))
            fig_supplier.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="% of BOM Cost")
            st.plotly_chart(fig_supplier, use_container_width=True)
    
    # =================================================================
    # TAB 5: SHIPMENT TRACEABILITY
    # =================================================================
    with tr_tab5:
        st.subheader("🚚 Shipment Traceability")
        
        # Recent shipments
        st.markdown("##### 📦 Recent Shipments")
        shipments = pd.DataFrame({
            "Shipment ID": ["SHP-2024-10892", "SHP-2024-10891", "SHP-2024-10890", "SHP-2024-10889", "SHP-2024-10888"],
            "Lots Included": ["LOT-12847, 12848", "LOT-12845, 12846", "LOT-12841", "LOT-12838, 12839, 12840", "LOT-12835"],
            "Units": ["10,000", "8,500", "5,000", "15,000", "3,200"],
            "Customer": ["Landis+Gyr", "BMW Group", "Itron", "Continental", "NTT DoCoMo"],
            "Destination": ["Atlanta, GA", "Munich, Germany", "Liberty Lake, WA", "Hanover, Germany", "Tokyo, Japan"],
            "Carrier": ["DHL", "DHL", "FedEx", "Kuehne+Nagel", "DHL"],
            "Ship Date": ["Dec 28", "Dec 27", "Dec 26", "Dec 25", "Dec 24"],
            "Status": ["🚚 In Transit", "✅ Delivered", "✅ Delivered", "🚚 In Transit", "✅ Delivered"],
            "ETA": ["Dec 31", "Dec 30", "Dec 28", "Jan 2", "Dec 27"]
        })
        st.dataframe(shipments, use_container_width=True)
        
        # Shipment details
        st.markdown("---")
        st.markdown("##### 📍 Shipment Tracking: SHP-2024-10892")
        tracking_cols = st.columns(5)
        tracking_steps = [
            ("📦 Packed", "Dec 28, 10:15", "Trieste, Italy", "✅", TELIT_GREEN),
            ("🚚 Picked Up", "Dec 28, 14:30", "Trieste Hub", "✅", TELIT_GREEN),
            ("✈️ In Transit", "Dec 29, 08:00", "Frankfurt Hub", "✅", TELIT_GREEN),
            ("🛬 Customs", "Dec 30, 06:00", "Atlanta, GA", "🔄", TELIT_BLUE),
            ("📬 Delivered", "Dec 31 (Est)", "Customer Site", "⏳", TELIT_GRAY),
        ]
        for col, (step, time, location, status, color) in zip(tracking_cols, tracking_steps):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 18px;">{status}</div>
                <div style="font-size: 11px; font-weight: 600;">{step}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{time}</div>
                <div style="font-size: 9px; color: {TELIT_GRAY};">{location}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 6: RECALLS
    # =================================================================
    with tr_tab6:
        st.subheader("⚠️ Recall Management")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_GREEN};">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">✅</span>
                <div>
                    <div style="font-size: 20px; font-weight: 700; color: {TELIT_GREEN};">No Active Recalls</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">Zero recalls in the last 24 months. All products meeting quality standards.</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recall simulation tool
        st.markdown("##### 🔍 Recall Impact Simulator")
        sim_col1, sim_col2 = st.columns([1, 2])
        
        with sim_col1:
            affected_lot = st.text_input("Affected Lot/Component", "QC-2024-A4521")
            recall_type = st.selectbox("Recall Type", ["Component Issue", "Quality Escape", "Safety Concern", "Regulatory"])
        
        with sim_col2:
            if affected_lot:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05);
                            border-radius: 12px; padding: 20px;">
                    <div style="font-size: 16px; font-weight: 700; margin-bottom: 15px;">📊 Impact Assessment</div>
                    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">
                        <div><strong>Affected Units:</strong> 11,000</div>
                        <div><strong>Affected Lots:</strong> 3</div>
                        <div><strong>Customers:</strong> 3</div>
                        <div><strong>Already Shipped:</strong> 8,000 (73%)</div>
                        <div><strong>In Production:</strong> 3,000 (27%)</div>
                        <div><strong>Est. Cost:</strong> $185,000</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Historical recalls
        st.markdown("---")
        st.markdown("##### 📋 Recall History (Last 5 Years)")
        recall_history = pd.DataFrame({
            "Year": ["2023", "2022", "2021", "2020", "2019"],
            "Recalls": ["0", "0", "1 (minor)", "0", "0"],
            "Units Affected": ["0", "0", "2,500", "0", "0"],
            "Root Cause": ["—", "—", "Firmware bug", "—", "—"],
            "Resolution": ["—", "—", "OTA update", "—", "—"],
            "Customer Impact": ["None", "None", "Minimal", "None", "None"]
        })
        st.dataframe(recall_history, use_container_width=True)
    
    # =================================================================
    # TAB 7: ANALYTICS
    # =================================================================
    with tr_tab7:
        st.subheader("📊 Traceability Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Monthly Traced Units")
            months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            traced_units = [185, 198, 215, 232, 248, 265]
            
            fig_traced = go.Figure()
            fig_traced.add_trace(go.Bar(x=months, y=traced_units, marker_color=TELIT_BLUE,
                                       text=[f"{t}K" for t in traced_units], textposition="outside"))
            fig_traced.update_layout(height=260, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Units (K)")
            st.plotly_chart(fig_traced, use_container_width=True)
        
        with col2:
            st.markdown("##### 📊 Trace Queries by Type")
            query_types = ["Serial Lookup", "Lot Trace", "Where-Used", "Customer Query", "Audit"]
            query_counts = [4250, 1850, 980, 420, 185]
            
            fig_queries = go.Figure(go.Pie(
                labels=query_types, values=query_counts, hole=0.5,
                marker_colors=[TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE, '#6B5B95', TELIT_GRAY]
            ))
            fig_queries.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_queries, use_container_width=True)
        
        # Compliance metrics
        st.markdown("---")
        st.markdown("##### ✅ Compliance & Audit Readiness")
        compliance_cols = st.columns(4)
        compliance_data = [
            ("ISO 9001:2015", "✅ Certified", "Last Audit: Oct 2024", TELIT_GREEN),
            ("IATF 16949", "✅ Certified", "Last Audit: Sep 2024", TELIT_GREEN),
            ("IPC-A-610", "✅ Compliant", "Class 3 Standard", TELIT_GREEN),
            ("REACH/RoHS", "✅ Compliant", "All products", TELIT_GREEN),
        ]
        for col, (cert, status, detail, color) in zip(compliance_cols, compliance_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 600;">{cert}</div>
                <div style="font-size: 16px; font-weight: 700; color: {color}; margin: 8px 0;">{status}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{detail}</div>
            </div>
            """, unsafe_allow_html=True)

# =============================================================================
# PAGE: CERTIFICATIONS
# =============================================================================
elif page == "📱 Certifications":
    st.title("📱 Certification & Compliance")
    st.markdown("*Carrier certifications, regional approvals, and compliance tracking for IoT modules*")
    
    # KPI Summary
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Active Certifications", "847", "+23 this quarter")
    c2.metric("Pending Approvals", "34", "in progress")
    c3.metric("Expiring <90 days", "12", "⚠️ action needed")
    c4.metric("Certification Cost YTD", "$1.2M", "+8% vs budget")
    c5.metric("Avg Approval Time", "45 days", "-5 days")
    
    st.markdown("---")
    
    cert_tab1, cert_tab2, cert_tab3, cert_tab4, cert_tab5, cert_tab6 = st.tabs([
        "📊 Overview", "📡 Carrier Certs", "🌍 Regional", "📅 Calendar", "💰 Costs", "📋 Compliance"
    ])
    
    with cert_tab1:
        st.markdown("### Certification Status Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            # Certification by type
            cert_types = pd.DataFrame({
                "Type": ["Carrier (NA)", "Carrier (EMEA)", "Carrier (APAC)", "Regional (FCC/CE)", "PTCRB/GCF", "Industry (Auto)"],
                "Active": [156, 134, 98, 245, 178, 36],
                "Pending": [8, 5, 12, 4, 3, 2],
                "Expired": [3, 2, 5, 1, 2, 0]
            })
            fig = px.bar(cert_types, x="Type", y=["Active", "Pending", "Expired"],
                        title="Certifications by Type",
                        barmode="stack",
                        color_discrete_sequence=[TELIT_GREEN, TELIT_ORANGE, TELIT_RED])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Certification by product family
            prod_certs = pd.DataFrame({
                "Product Family": ["ME910", "LE910", "FN920", "ME310", "NE310", "Other"],
                "Certifications": [187, 156, 134, 145, 98, 127]
            })
            fig = px.pie(prod_certs, values="Certifications", names="Product Family",
                        title="Certifications by Product Family",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
        
        # Certification matrix
        st.markdown("### Module × Carrier Certification Matrix")
        matrix_data = {
            "Module": ["ME910C1", "LE910Cx", "FN920A", "ME310G1", "NE310H2"],
            "AT&T": ["✅", "✅", "✅", "✅", "🔄"],
            "Verizon": ["✅", "✅", "✅", "🔄", "❌"],
            "T-Mobile": ["✅", "✅", "✅", "✅", "✅"],
            "Vodafone": ["✅", "✅", "🔄", "✅", "✅"],
            "Deutsche Telekom": ["✅", "✅", "✅", "✅", "🔄"],
            "NTT DoCoMo": ["✅", "🔄", "❌", "✅", "❌"]
        }
        st.dataframe(pd.DataFrame(matrix_data), use_container_width=True)
        st.caption("✅ Certified | 🔄 In Progress | ❌ Not Planned")
    
    with cert_tab2:
        st.markdown("### Carrier Certifications")
        
        # NA Carriers
        st.markdown("#### 🇺🇸 North America")
        na_carriers = pd.DataFrame({
            "Carrier": ["AT&T", "Verizon", "T-Mobile USA", "Bell Canada", "Rogers", "Telus"],
            "Modules Certified": [45, 42, 48, 38, 35, 32],
            "Pending": [3, 5, 2, 2, 3, 1],
            "Last Update": ["2024-12-15", "2024-12-10", "2024-12-18", "2024-11-28", "2024-12-01", "2024-11-25"],
            "Status": ["🟢 Current", "🟢 Current", "🟢 Current", "🟢 Current", "🟢 Current", "🟢 Current"]
        })
        st.dataframe(na_carriers, use_container_width=True)
        
        # EMEA Carriers
        st.markdown("#### 🇪🇺 EMEA")
        emea_carriers = pd.DataFrame({
            "Carrier": ["Vodafone", "Deutsche Telekom", "Orange", "Telefonica", "Swisscom", "KPN"],
            "Modules Certified": [52, 48, 44, 41, 28, 25],
            "Pending": [2, 3, 4, 2, 1, 2],
            "Last Update": ["2024-12-12", "2024-12-08", "2024-12-05", "2024-11-30", "2024-12-01", "2024-11-28"],
            "Status": ["🟢 Current", "🟢 Current", "🟢 Current", "🟢 Current", "🟢 Current", "🟢 Current"]
        })
        st.dataframe(emea_carriers, use_container_width=True)
        
        # APAC
        st.markdown("#### 🌏 APAC")
        apac_carriers = pd.DataFrame({
            "Carrier": ["NTT DoCoMo", "KDDI", "SoftBank", "China Mobile", "Singtel", "Telstra"],
            "Modules Certified": [28, 25, 22, 18, 20, 18],
            "Pending": [4, 3, 2, 5, 2, 3],
            "Last Update": ["2024-12-10", "2024-12-05", "2024-11-28", "2024-12-01", "2024-11-25", "2024-12-08"],
            "Status": ["🟢 Current", "🟢 Current", "🟢 Current", "🟡 Review", "🟢 Current", "🟢 Current"]
        })
        st.dataframe(apac_carriers, use_container_width=True)
    
    with cert_tab3:
        st.markdown("### Regional Certifications")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Regulatory Bodies")
            reg_data = pd.DataFrame({
                "Region": ["FCC (USA)", "CE (Europe)", "IC (Canada)", "TELEC (Japan)", "ACMA (Australia)", "SRRC (China)"],
                "Active Certs": [89, 92, 78, 45, 38, 28],
                "Compliance Rate": ["100%", "100%", "100%", "98%", "100%", "95%"],
                "Next Audit": ["2025-03", "2025-06", "2025-04", "2025-02", "2025-05", "2025-01"]
            })
            st.dataframe(reg_data, use_container_width=True)
        
        with col2:
            st.markdown("#### Industry Standards")
            ind_data = pd.DataFrame({
                "Standard": ["PTCRB", "GCF", "IATF 16949", "ISO 9001", "ISO 14001", "AEC-Q100"],
                "Status": ["✅ Certified", "✅ Certified", "✅ Certified", "✅ Certified", "✅ Certified", "🔄 In Progress"],
                "Valid Until": ["2025-08", "2025-09", "2025-12", "2026-03", "2026-01", "2025-06"],
                "Scope": ["All modules", "All modules", "Auto modules", "All products", "All sites", "Auto ICs"]
            })
            st.dataframe(ind_data, use_container_width=True)
    
    with cert_tab4:
        st.markdown("### Certification Calendar")
        
        # Upcoming expirations
        st.markdown("#### ⚠️ Expiring Certifications (Next 90 Days)")
        expiring = pd.DataFrame({
            "Module": ["ME910C1", "LE910Cx", "ME310G1", "FN920", "NE310H2"],
            "Certification": ["AT&T PTCRB", "Verizon ODP", "T-Mobile", "FCC Part 22", "CE RED"],
            "Expiry Date": ["2025-01-15", "2025-01-28", "2025-02-10", "2025-02-25", "2025-03-05"],
            "Days Left": [17, 30, 43, 58, 66],
            "Renewal Status": ["🔄 Submitted", "📋 Preparing", "🔄 Submitted", "✅ Approved", "📋 Preparing"],
            "Owner": ["J. Smith", "M. Chen", "A. Mueller", "K. Tanaka", "L. Costa"]
        })
        st.dataframe(expiring, use_container_width=True)
        
        # Timeline
        st.markdown("#### 📅 Certification Timeline (Next 6 Months)")
        timeline_data = pd.DataFrame({
            "Task": ["ME910C1 AT&T Renewal", "LE910Cx Verizon Renewal", "FN990 New PTCRB", "FN990 GCF", "ME510 FCC", "NE310H2 CE"],
            "Start": pd.to_datetime(["2024-12-01", "2024-12-15", "2025-01-05", "2025-01-20", "2025-02-01", "2025-02-15"]),
            "End": pd.to_datetime(["2025-01-15", "2025-02-15", "2025-03-15", "2025-04-01", "2025-04-15", "2025-05-01"]),
            "Type": ["Renewal", "Renewal", "New", "New", "New", "New"]
        })
        fig = px.timeline(timeline_data, x_start="Start", x_end="End", y="Task", color="Type",
                         title="Certification Projects Timeline",
                         color_discrete_map={"Renewal": TELIT_BLUE, "New": TELIT_GREEN})
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    
    with cert_tab5:
        st.markdown("### Certification Costs")
        
        col1, col2 = st.columns(2)
        with col1:
            # Cost by type
            cost_data = pd.DataFrame({
                "Category": ["Carrier Fees", "Lab Testing", "Regulatory Fees", "Consultants", "Travel", "Equipment"],
                "YTD Spend": [380000, 420000, 180000, 120000, 55000, 45000],
                "Budget": [400000, 450000, 200000, 130000, 60000, 50000]
            })
            fig = px.bar(cost_data, x="Category", y=["YTD Spend", "Budget"],
                        title="Certification Costs vs Budget",
                        barmode="group",
                        color_discrete_sequence=[TELIT_BLUE, "#94a3b8"])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Cost trend
            months = pd.date_range(start="2024-01-01", periods=12, freq="M")
            cost_trend = pd.DataFrame({
                "Month": months,
                "Cost": [85, 92, 78, 105, 88, 95, 110, 98, 102, 115, 108, 124]
            })
            fig = px.line(cost_trend, x="Month", y="Cost",
                         title="Monthly Certification Spend ($K)",
                         markers=True)
            fig.update_traces(line_color=TELIT_BLUE)
            st.plotly_chart(fig, use_container_width=True)
        
        # Cost per module
        st.markdown("#### Cost per Module Family")
        module_cost = pd.DataFrame({
            "Module Family": ["ME910", "LE910", "FN920", "ME310", "NE310"],
            "Total Certs": [187, 156, 134, 145, 98],
            "Total Cost": ["$245K", "$198K", "$312K", "$178K", "$145K"],
            "Avg Cost/Cert": ["$1,310", "$1,269", "$2,328", "$1,228", "$1,480"]
        })
        st.dataframe(module_cost, use_container_width=True)
    
    with cert_tab6:
        st.markdown("### Compliance Dashboard")
        
        # Compliance scorecard
        st.markdown("#### Compliance Scorecard")
        comp_col1, comp_col2, comp_col3, comp_col4 = st.columns(4)
        comp_col1.metric("Overall Compliance", "98.5%", "+0.3%")
        comp_col2.metric("Documentation", "97.2%", "+1.1%")
        comp_col3.metric("Testing Coverage", "99.1%", "+0.2%")
        comp_col4.metric("Audit Findings", "3", "-2 vs LQ")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Recent Audit Results")
            audits = pd.DataFrame({
                "Audit": ["IATF 16949 Surveillance", "ISO 9001 Internal", "Carrier Audit - AT&T", "PTCRB Witness Test"],
                "Date": ["2024-11-15", "2024-10-28", "2024-09-20", "2024-08-15"],
                "Result": ["✅ Pass", "✅ Pass", "✅ Pass", "✅ Pass"],
                "Findings": [1, 2, 0, 0],
                "Status": ["Closed", "1 Open", "Closed", "Closed"]
            })
            st.dataframe(audits, use_container_width=True)
        
        with col2:
            st.markdown("#### Open Compliance Actions")
            actions = pd.DataFrame({
                "ID": ["CA-2024-045", "CA-2024-048", "CA-2024-052"],
                "Description": ["Update test procedure TP-RF-012", "Calibration records gap", "Supplier audit schedule"],
                "Due Date": ["2025-01-15", "2025-01-30", "2025-02-15"],
                "Owner": ["Quality", "Lab", "Procurement"],
                "Status": ["🔄 In Progress", "📋 Planned", "📋 Planned"]
            })
            st.dataframe(actions, use_container_width=True)

# =============================================================================
# PAGE: PRODUCT LIFECYCLE
# =============================================================================
elif page == "🔄 Product Lifecycle":
    st.title("🔄 Product Lifecycle Management")
    st.markdown("*Technology transitions, EOL management, and new product introduction tracking*")
    
    # KPI Summary
    p1, p2, p3, p4, p5 = st.columns(5)
    p1.metric("Active Products", "156", "in production")
    p2.metric("NPI Pipeline", "12", "in development")
    p3.metric("NRND Products", "28", "last-time-buy")
    p4.metric("EOL This Year", "8", "phase-out planned")
    p5.metric("Tech Transitions", "3", "4G→5G, LTE-M")
    
    st.markdown("---")
    
    plm_tab1, plm_tab2, plm_tab3, plm_tab4, plm_tab5, plm_tab6 = st.tabs([
        "📊 Overview", "🆕 NPI", "🔄 Transitions", "📉 EOL", "📋 ECO", "📈 Roadmap"
    ])
    
    with plm_tab1:
        st.markdown("### Product Portfolio Status")
        
        col1, col2 = st.columns(2)
        with col1:
            # Lifecycle status
            lifecycle = pd.DataFrame({
                "Status": ["Active", "Ramp-Up", "NRND", "EOL Announced", "Discontinued"],
                "Count": [156, 8, 28, 8, 45],
                "Revenue %": [78, 5, 12, 4, 1]
            })
            fig = px.pie(lifecycle, values="Count", names="Status",
                        title="Products by Lifecycle Stage",
                        color_discrete_sequence=[TELIT_GREEN, TELIT_BLUE, TELIT_ORANGE, TELIT_RED, "#94a3b8"])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Technology mix
            tech_mix = pd.DataFrame({
                "Technology": ["LTE Cat-1", "LTE Cat-M", "NB-IoT", "5G Sub-6", "5G mmWave", "2G/3G Legacy"],
                "Products": [48, 42, 28, 18, 8, 12],
                "Revenue $M": [125, 98, 45, 85, 32, 18]
            })
            fig = px.bar(tech_mix, x="Technology", y=["Products", "Revenue $M"],
                        title="Portfolio by Technology",
                        barmode="group",
                        color_discrete_sequence=[TELIT_BLUE, TELIT_GREEN])
            st.plotly_chart(fig, use_container_width=True)
        
        # Product matrix
        st.markdown("### Product Family Matrix")
        matrix = pd.DataFrame({
            "Family": ["ME910", "LE910", "FN920", "ME310", "NE310", "FN990"],
            "Technology": ["LTE Cat-M", "LTE Cat-1", "5G Sub-6", "LTE Cat-M", "NB-IoT", "5G mmWave"],
            "Status": ["🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active", "🔵 Ramp-Up"],
            "Launch": ["2019", "2018", "2022", "2020", "2021", "2024"],
            "Revenue $M": [45.2, 68.5, 42.8, 38.4, 22.1, 8.5],
            "Units (K)": [2850, 3420, 890, 2150, 1820, 180],
            "Key Vertical": ["Utilities", "Automotive", "Industrial", "Asset Track", "Smart City", "Industrial"]
        })
        st.dataframe(matrix, use_container_width=True)
    
    with plm_tab2:
        st.markdown("### New Product Introduction (NPI) Pipeline")
        
        # NPI summary
        npi_col1, npi_col2, npi_col3, npi_col4 = st.columns(4)
        npi_col1.metric("Concept", "3", "projects")
        npi_col2.metric("Development", "5", "projects")
        npi_col3.metric("Qualification", "2", "projects")
        npi_col4.metric("Ramp-Up", "2", "projects")
        
        st.markdown("---")
        
        # NPI project list
        st.markdown("#### Active NPI Projects")
        npi_projects = pd.DataFrame({
            "Project": ["FN995", "ME920", "LE920", "NE320", "ME515"],
            "Technology": ["5G RedCap", "LTE Cat-1bis", "LTE Cat-4", "NB-IoT R16", "LTE Cat-M2"],
            "Phase": ["Development", "Qualification", "Development", "Concept", "Ramp-Up"],
            "Target Launch": ["Q3 2025", "Q1 2025", "Q2 2025", "Q4 2025", "Q1 2025"],
            "Progress": [45, 78, 52, 15, 92],
            "Risk": ["🟢 Low", "🟢 Low", "🟡 Medium", "🟢 Low", "🟢 Low"],
            "Revenue Target": ["$25M Y1", "$18M Y1", "$22M Y1", "$12M Y1", "$15M Y1"]
        })
        st.dataframe(npi_projects, use_container_width=True)
        
        # NPI timeline
        st.markdown("#### NPI Gantt Chart")
        npi_gantt = pd.DataFrame({
            "Task": ["FN995 Development", "FN995 Certification", "ME920 Qual", "ME920 Ramp", "LE920 Dev", "NE320 Concept"],
            "Start": pd.to_datetime(["2024-06-01", "2025-03-01", "2024-10-01", "2025-02-01", "2024-08-01", "2024-11-01"]),
            "End": pd.to_datetime(["2025-02-28", "2025-08-31", "2025-01-31", "2025-06-30", "2025-05-31", "2025-03-31"]),
            "Phase": ["Development", "Certification", "Qualification", "Ramp-Up", "Development", "Concept"]
        })
        fig = px.timeline(npi_gantt, x_start="Start", x_end="End", y="Task", color="Phase",
                         title="NPI Project Timeline")
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)
    
    with plm_tab3:
        st.markdown("### Technology Transitions")
        
        st.info("🔄 **Active Transitions:** 4G LTE → 5G, 2G/3G → LTE-M/NB-IoT")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 2G/3G Sunset Impact")
            sunset_data = pd.DataFrame({
                "Region": ["North America", "Europe", "Japan", "Australia", "Global"],
                "2G Status": ["🔴 Sunset", "🟡 2025", "🔴 Sunset", "🔴 Sunset", "🟡 Ongoing"],
                "3G Status": ["🔴 Sunset", "🟡 2025-2027", "🔴 Sunset", "🔴 2024", "🟡 Ongoing"],
                "Affected Modules": [8, 12, 4, 3, 27],
                "Migration Plan": ["✅ Complete", "🔄 In Progress", "✅ Complete", "✅ Complete", "🔄 80%"]
            })
            st.dataframe(sunset_data, use_container_width=True)
        
        with col2:
            st.markdown("#### 5G Transition Roadmap")
            transition_5g = pd.DataFrame({
                "Product": ["FN920 → FN990", "Industrial Gateway", "Automotive TCU", "Fixed Wireless"],
                "Current": ["5G Sub-6", "LTE Cat-1", "LTE Cat-4", "LTE Cat-12"],
                "Target": ["5G mmWave", "5G RedCap", "5G C-V2X", "5G FWA"],
                "Timeline": ["Q2 2025", "Q3 2025", "Q4 2025", "Q1 2026"],
                "Status": ["🔄 Dev", "📋 Plan", "📋 Plan", "💡 Concept"]
            })
            st.dataframe(transition_5g, use_container_width=True)
        
        # Transition revenue impact
        st.markdown("#### Revenue Transition Forecast")
        years = ["2024", "2025", "2026", "2027", "2028"]
        tech_forecast = pd.DataFrame({
            "Year": years,
            "2G/3G": [18, 8, 2, 0, 0],
            "LTE": [285, 310, 295, 260, 220],
            "5G": [95, 145, 210, 280, 350],
            "LPWAN": [65, 85, 105, 125, 145]
        })
        fig = px.area(tech_forecast, x="Year", y=["2G/3G", "LTE", "5G", "LPWAN"],
                     title="Revenue by Technology ($M)",
                     color_discrete_sequence=["#94a3b8", TELIT_BLUE, TELIT_GREEN, TELIT_ORANGE])
        st.plotly_chart(fig, use_container_width=True)
    
    with plm_tab4:
        st.markdown("### End-of-Life Management")
        
        # EOL summary
        st.warning("⚠️ **8 products** scheduled for EOL announcement in next 12 months")
        
        # EOL products
        st.markdown("#### EOL Schedule")
        eol_products = pd.DataFrame({
            "Product": ["GE910", "UE910", "HE910", "CE910", "DE910", "UL865", "GL865", "GC864"],
            "Technology": ["2G", "3G", "3G", "2G", "2G", "3G", "2G", "2G"],
            "EOL Announced": ["2024-01", "2024-03", "2024-06", "2024-09", "2024-09", "2024-06", "2024-01", "2023-09"],
            "Last Order": ["2024-12", "2025-03", "2025-06", "2025-09", "2025-09", "2025-06", "2024-12", "2024-06"],
            "Last Ship": ["2025-06", "2025-09", "2025-12", "2026-03", "2026-03", "2025-12", "2025-06", "2025-01"],
            "Active Customers": [12, 28, 45, 18, 8, 22, 15, 5],
            "Migration": ["ME910", "LE910", "LE910", "ME910", "ME910", "LE910", "ME910", "ME910"]
        })
        st.dataframe(eol_products, use_container_width=True)
        
        # LTB tracking
        st.markdown("#### Last-Time-Buy Orders")
        ltb_orders = pd.DataFrame({
            "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "CalAmp"],
            "Product": ["HE910", "GE910", "UE910", "CE910"],
            "LTB Qty": [50000, 25000, 35000, 18000],
            "Ordered": [45000, 25000, 28000, 12000],
            "Shipped": [42000, 22000, 25000, 8000],
            "Remaining": [8000, 3000, 10000, 10000],
            "Due Date": ["2025-03", "2024-12", "2025-06", "2025-09"]
        })
        st.dataframe(ltb_orders, use_container_width=True)
    
    with plm_tab5:
        st.markdown("### Engineering Change Orders (ECO)")
        
        # ECO summary
        eco_col1, eco_col2, eco_col3, eco_col4 = st.columns(4)
        eco_col1.metric("Open ECOs", "18", "in review")
        eco_col2.metric("Implemented MTD", "12", "+3 vs target")
        eco_col3.metric("Avg Cycle Time", "28 days", "-5 days")
        eco_col4.metric("Cost Impact", "$125K", "YTD")
        
        st.markdown("---")
        
        # ECO list
        st.markdown("#### Active ECOs")
        ecos = pd.DataFrame({
            "ECO #": ["ECO-2024-089", "ECO-2024-092", "ECO-2024-095", "ECO-2024-098", "ECO-2024-101"],
            "Product": ["ME910C1", "LE910Cx", "FN920", "ME310G1", "NE310H2"],
            "Type": ["Component Change", "Firmware Update", "Design Change", "Component Change", "Process Change"],
            "Reason": ["Supplier EOL", "Security Patch", "Performance", "Cost Reduction", "Yield Improve"],
            "Status": ["🔄 Implementation", "✅ Released", "📋 Review", "🔄 Validation", "📋 Review"],
            "Impact": ["Medium", "Low", "High", "Low", "Medium"],
            "Target Date": ["2025-01-15", "2024-12-20", "2025-02-28", "2025-01-30", "2025-02-15"]
        })
        st.dataframe(ecos, use_container_width=True)
    
    with plm_tab6:
        st.markdown("### Product Roadmap")
        
        # Roadmap visual
        st.markdown("#### 3-Year Product Roadmap")
        roadmap_data = []
        products = [
            ("FN995 5G RedCap", "2025-Q2", "2025-Q4", "New"),
            ("ME920 Cat-1bis", "2025-Q1", "2025-Q2", "New"),
            ("LE920 Cat-4", "2025-Q2", "2025-Q3", "New"),
            ("FN920 Gen2", "2025-Q3", "2025-Q4", "Refresh"),
            ("NE320 R16", "2025-Q4", "2026-Q2", "New"),
            ("ME925 Cat-M2", "2026-Q1", "2026-Q3", "New"),
            ("FN998 6G Prep", "2026-Q3", "2027-Q2", "New")
        ]
        
        for prod, start, end, ptype in products:
            start_date = pd.to_datetime(start.replace("Q1", "01-01").replace("Q2", "04-01").replace("Q3", "07-01").replace("Q4", "10-01"))
            end_date = pd.to_datetime(end.replace("Q1", "03-31").replace("Q2", "06-30").replace("Q3", "09-30").replace("Q4", "12-31"))
            roadmap_data.append({"Product": prod, "Start": start_date, "End": end_date, "Type": ptype})
        
        roadmap_df = pd.DataFrame(roadmap_data)
        fig = px.timeline(roadmap_df, x_start="Start", x_end="End", y="Product", color="Type",
                         title="Product Launch Roadmap",
                         color_discrete_map={"New": TELIT_GREEN, "Refresh": TELIT_BLUE})
        fig.update_yaxes(autorange="reversed")
        st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# PAGE: CUSTOMER ORDERS
# =============================================================================
elif page == "📋 Customer Orders":
    st.title("📋 Customer Order Management")
    st.markdown("*Order tracking, backlog management, and customer fulfillment*")
    
    # KPI Summary
    o1, o2, o3, o4, o5 = st.columns(5)
    o1.metric("Open Orders", "$42.3M", "+$5.2M vs LM")
    o2.metric("Backlog", "$128M", "12 weeks")
    o3.metric("On-Time Delivery", "95.8%", "+1.2%")
    o4.metric("Order Fill Rate", "94.2%", "+0.8%")
    o5.metric("Avg Lead Time", "6.2 wks", "-0.5 wks")
    
    st.markdown("---")
    
    ord_tab1, ord_tab2, ord_tab3, ord_tab4, ord_tab5, ord_tab6 = st.tabs([
        "📊 Overview", "📋 Open Orders", "📅 Backlog", "🎯 Design Wins", "📈 Customer Hub", "⚡ Expedites"
    ])
    
    with ord_tab1:
        st.markdown("### Order Management Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            # Orders by status
            order_status = pd.DataFrame({
                "Status": ["Confirmed", "Scheduled", "In Production", "Ready to Ship", "In Transit", "On Hold"],
                "Value ($M)": [18.5, 12.8, 8.2, 3.5, 4.8, 2.2],
                "Lines": [245, 186, 98, 45, 62, 28]
            })
            fig = px.bar(order_status, x="Status", y="Value ($M)",
                        title="Open Orders by Status",
                        color="Value ($M)",
                        color_continuous_scale=[[0, TELIT_BLUE], [1, TELIT_GREEN]])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Orders by region
            order_region = pd.DataFrame({
                "Region": ["Americas", "EMEA", "APAC", "Japan"],
                "Value ($M)": [15.8, 14.2, 8.5, 3.8]
            })
            fig = px.pie(order_region, values="Value ($M)", names="Region",
                        title="Open Orders by Region",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
        
        # Order trend
        st.markdown("#### Order Intake Trend")
        months = pd.date_range(start="2024-01-01", periods=12, freq="M")
        order_trend = pd.DataFrame({
            "Month": months,
            "Intake": [38, 42, 45, 52, 48, 55, 58, 52, 62, 58, 65, 68],
            "Shipments": [35, 38, 42, 48, 45, 52, 55, 50, 58, 55, 60, 62]
        })
        fig = px.line(order_trend, x="Month", y=["Intake", "Shipments"],
                     title="Monthly Orders vs Shipments ($M)",
                     markers=True,
                     color_discrete_sequence=[TELIT_BLUE, TELIT_GREEN])
        st.plotly_chart(fig, use_container_width=True)
    
    with ord_tab2:
        st.markdown("### Open Orders Detail")
        
        # Filter options
        filter_col1, filter_col2, filter_col3 = st.columns(3)
        with filter_col1:
            st.selectbox("Customer", ["All", "Continental AG", "Landis+Gyr", "Honeywell"], key="ord_cust")
        with filter_col2:
            st.selectbox("Product Family", ["All", "ME910", "LE910", "FN920", "ME310"], key="ord_prod")
        with filter_col3:
            st.selectbox("Status", ["All", "Confirmed", "Scheduled", "In Production"], key="ord_stat")
        
        # Orders table
        orders = pd.DataFrame({
            "Order #": ["SO-2024-12845", "SO-2024-12852", "SO-2024-12861", "SO-2024-12878", "SO-2024-12885"],
            "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "CalAmp", "Itron"],
            "Product": ["LE910C4", "ME310G1", "FN990A", "ME310G1", "ME310G1"],
            "Qty": [25000, 50000, 5000, 35000, 80000],
            "Value": ["$312K", "$425K", "$185K", "$245K", "$520K"],
            "Request Date": ["2025-01-15", "2025-01-20", "2025-02-01", "2025-01-25", "2025-02-10"],
            "Commit Date": ["2025-01-18", "2025-01-22", "2025-02-05", "2025-01-28", "2025-02-12"],
            "Status": ["🟢 On Track", "🟢 On Track", "🟡 At Risk", "🟢 On Track", "🟢 On Track"],
            "Priority": ["High", "Medium", "High", "Medium", "Low"]
        })
        st.dataframe(orders, use_container_width=True)
    
    with ord_tab3:
        st.markdown("### Backlog Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            # Backlog by month
            backlog_months = pd.DataFrame({
                "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "Backlog ($M)": [42, 38, 28, 18, 12, 8]
            })
            fig = px.bar(backlog_months, x="Month", y="Backlog ($M)",
                        title="Backlog by Scheduled Ship Month",
                        color_discrete_sequence=[TELIT_BLUE])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Backlog aging
            backlog_aging = pd.DataFrame({
                "Aging": ["Current", "1-2 weeks late", "3-4 weeks late", ">4 weeks late"],
                "Value ($M)": [35.2, 4.5, 1.8, 0.8]
            })
            fig = px.pie(backlog_aging, values="Value ($M)", names="Aging",
                        title="Backlog Aging",
                        color_discrete_sequence=[TELIT_GREEN, TELIT_ORANGE, "#f59e0b", TELIT_RED])
            st.plotly_chart(fig, use_container_width=True)
        
        # Backlog by customer
        st.markdown("#### Top 10 Customers by Backlog")
        top_backlog = pd.DataFrame({
            "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "CalAmp", "Itron", 
                        "Geotab", "Philips Healthcare", "British Gas", "NCR Corp", "Trimble"],
            "Backlog ($M)": [18.5, 15.2, 12.8, 10.5, 9.2, 8.5, 7.8, 6.5, 5.8, 5.2],
            "Weeks Coverage": [14, 12, 10, 8, 7, 8, 6, 5, 5, 4],
            "Trend": ["↑", "↑", "→", "↑", "→", "↓", "↑", "→", "↓", "→"]
        })
        st.dataframe(top_backlog, use_container_width=True)
    
    with ord_tab4:
        st.markdown("### Design Win to Revenue Tracking")
        
        # Design win funnel
        st.markdown("#### Design Win Pipeline")
        dw_pipeline = pd.DataFrame({
            "Stage": ["Qualified Opportunity", "Design-In", "Sample", "Pre-Production", "Production"],
            "Count": [125, 85, 52, 28, 47],
            "Value ($M)": [180, 145, 98, 65, 128]
        })
        fig = px.funnel(dw_pipeline, x="Count", y="Stage",
                       title="Design Win Pipeline",
                       color_discrete_sequence=[TELIT_BLUE])
        st.plotly_chart(fig, use_container_width=True)
        
        # Active design wins
        st.markdown("#### Recent Design Wins Ramping")
        dw_ramp = pd.DataFrame({
            "Design Win": ["DW-2023-145 Auto TCU", "DW-2023-158 Smart Meter", "DW-2024-012 Asset Track", 
                         "DW-2024-025 Industrial", "DW-2024-038 Fleet"],
            "Customer": ["Continental AG", "Landis+Gyr", "Trimble", "Honeywell", "Geotab"],
            "Module": ["LE910C4", "ME310G1", "ME310G1", "FN990A", "LE910C4"],
            "Annual Volume": ["250K", "500K", "150K", "25K", "80K"],
            "Ramp Status": ["🟢 On Track", "🟢 On Track", "🟡 Delayed", "🔄 Sampling", "🟢 On Track"],
            "First Revenue": ["Q2 2024", "Q3 2024", "Q1 2025", "Q2 2025", "Q4 2024"]
        })
        st.dataframe(dw_ramp, use_container_width=True)
    
    with ord_tab5:
        st.markdown("### Customer Hub Inventory (VMI)")
        
        st.info("📦 **VMI Program:** Consignment inventory at customer locations for JIT delivery")
        
        # Hub inventory summary
        hub_col1, hub_col2, hub_col3, hub_col4 = st.columns(4)
        hub_col1.metric("Total Hub Value", "$8.5M", "across 12 customers")
        hub_col2.metric("Avg Days of Supply", "15 days", "target: 14")
        hub_col3.metric("Consumption Rate", "$2.1M/week", "+8%")
        hub_col4.metric("Replenishment Alerts", "3", "action needed")
        
        st.markdown("---")
        
        # Hub detail
        hub_data = pd.DataFrame({
            "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "NTT DoCoMo", "Itron"],
            "Location": ["Hanover, DE", "Atlanta, GA", "Charlotte, NC", "Tokyo, JP", "Singapore"],
            "Products": [3, 2, 4, 2, 3],
            "Value ($K)": [1850, 1420, 1280, 980, 750],
            "DOS": [18, 14, 12, 16, 15],
            "Weekly Pull": ["$425K", "$380K", "$290K", "$210K", "$185K"],
            "Status": ["🟢 OK", "🟢 OK", "🟡 Low", "🟢 OK", "🟢 OK"]
        })
        st.dataframe(hub_data, use_container_width=True)
    
    with ord_tab6:
        st.markdown("### Expedite Requests")
        
        # Expedite summary
        exp_col1, exp_col2, exp_col3 = st.columns(3)
        exp_col1.metric("Active Expedites", "8", "requests")
        exp_col2.metric("Success Rate", "85%", "+5%")
        exp_col3.metric("Avg Days Pulled In", "5.2", "days")
        
        st.markdown("---")
        
        # Expedite list
        expedites = pd.DataFrame({
            "Request #": ["EXP-2024-089", "EXP-2024-092", "EXP-2024-095", "EXP-2024-098"],
            "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "Geotab"],
            "Order": ["SO-2024-12845", "SO-2024-12852", "SO-2024-12861", "SO-2024-12885"],
            "Original Date": ["2025-01-25", "2025-02-05", "2025-02-15", "2025-02-20"],
            "Requested Date": ["2025-01-15", "2025-01-25", "2025-02-01", "2025-02-10"],
            "Days Pull-In": [10, 11, 14, 10],
            "Status": ["✅ Approved", "🔄 Review", "❌ Declined", "🔄 Review"],
            "Reason": ["Line down", "Customer launch", "Capacity", "Design win"]
        })
        st.dataframe(expedites, use_container_width=True)

# =============================================================================
# PAGE: RETURNS & RMA
# =============================================================================
elif page == "🔁 Returns & RMA":
    st.title("🔁 Returns & RMA Management")
    st.markdown("*Return merchandise authorization, failure analysis, and warranty tracking*")
    
    # KPI Summary
    r1, r2, r3, r4, r5 = st.columns(5)
    r1.metric("Open RMAs", "45", "+3 this week")
    r2.metric("Return Rate", "0.8%", "-0.1%", delta_color="inverse")
    r3.metric("Avg Resolution", "12 days", "-2 days")
    r4.metric("Warranty Cost YTD", "$285K", "+5% vs LY")
    r5.metric("NFF Rate", "32%", "no fault found")
    
    st.markdown("---")
    
    rma_tab1, rma_tab2, rma_tab3, rma_tab4, rma_tab5, rma_tab6 = st.tabs([
        "📊 Overview", "📋 Open RMAs", "🔬 Failure Analysis", "📈 Trends", "💰 Warranty", "📊 Pareto"
    ])
    
    with rma_tab1:
        st.markdown("### RMA Dashboard Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            # RMA by status
            rma_status = pd.DataFrame({
                "Status": ["Received", "In Analysis", "Pending Parts", "Repair Complete", "Shipped Back"],
                "Count": [12, 18, 5, 8, 2]
            })
            fig = px.pie(rma_status, values="Count", names="Status",
                        title="Open RMAs by Status",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # RMA trend
            months = pd.date_range(start="2024-01-01", periods=12, freq="M")
            rma_trend = pd.DataFrame({
                "Month": months,
                "RMAs": [42, 38, 45, 52, 48, 44, 50, 46, 42, 48, 45, 45],
                "Return Rate %": [0.9, 0.85, 0.95, 1.05, 0.92, 0.88, 0.95, 0.9, 0.85, 0.92, 0.88, 0.8]
            })
            fig = px.line(rma_trend, x="Month", y="Return Rate %",
                         title="Monthly Return Rate Trend",
                         markers=True)
            fig.update_traces(line_color=TELIT_BLUE)
            st.plotly_chart(fig, use_container_width=True)
        
        # Return by reason
        st.markdown("#### Returns by Failure Category")
        failure_cat = pd.DataFrame({
            "Category": ["NFF", "DOA", "Field Failure", "Cosmetic", "Firmware", "Customer Damage"],
            "Count": [145, 85, 120, 25, 45, 35],
            "% of Total": [32, 19, 26, 5, 10, 8]
        })
        fig = px.bar(failure_cat, x="Category", y="Count",
                    title="Returns by Category (YTD)",
                    color="Count",
                    color_continuous_scale=[[0, TELIT_GREEN], [1, TELIT_RED]])
        st.plotly_chart(fig, use_container_width=True)
    
    with rma_tab2:
        st.markdown("### Open RMA List")
        
        # Filter
        filter_col1, filter_col2 = st.columns(2)
        with filter_col1:
            st.selectbox("Status Filter", ["All", "Received", "In Analysis", "Pending Parts"], key="rma_filter")
        with filter_col2:
            st.selectbox("Priority", ["All", "Critical", "High", "Medium", "Low"], key="rma_priority")
        
        # RMA table
        rmas = pd.DataFrame({
            "RMA #": ["RMA-2024-1245", "RMA-2024-1252", "RMA-2024-1258", "RMA-2024-1265", "RMA-2024-1271"],
            "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "Geotab", "Itron"],
            "Product": ["LE910C4", "ME310G1", "FN990A", "ME310G1", "ME310G1"],
            "Qty": [25, 100, 5, 50, 200],
            "Failure Mode": ["No Network", "Dead Unit", "Overheating", "Firmware", "NFF"],
            "Received": ["2024-12-15", "2024-12-18", "2024-12-20", "2024-12-22", "2024-12-24"],
            "Status": ["🔬 Analysis", "📦 Received", "🔧 Repair", "🔬 Analysis", "📦 Received"],
            "Priority": ["🔴 Critical", "🟡 High", "🟡 High", "🟢 Medium", "🟢 Medium"],
            "Owner": ["J. Smith", "M. Chen", "A. Mueller", "K. Tanaka", "L. Costa"]
        })
        st.dataframe(rmas, use_container_width=True)
    
    with rma_tab3:
        st.markdown("### Failure Analysis Results")
        
        # Recent FA reports
        st.markdown("#### Recent Failure Analysis Reports")
        fa_reports = pd.DataFrame({
            "FA #": ["FA-2024-892", "FA-2024-895", "FA-2024-898", "FA-2024-901"],
            "RMA": ["RMA-2024-1198", "RMA-2024-1205", "RMA-2024-1212", "RMA-2024-1225"],
            "Product": ["ME910C1", "LE910Cx", "FN920", "ME310G1"],
            "Failure Mode": ["RF Performance", "Power Management", "Thermal", "Memory"],
            "Root Cause": ["Solder joint crack", "IC failure", "Design margin", "ESD damage"],
            "Corrective Action": ["Process update", "Supplier SCAR", "Design change", "Handling procedure"],
            "Status": ["✅ Closed", "🔄 Open", "✅ Closed", "🔄 Open"]
        })
        st.dataframe(fa_reports, use_container_width=True)
        
        # FA summary
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Root Cause Distribution")
            rc_data = pd.DataFrame({
                "Root Cause": ["Manufacturing", "Design", "Component", "Customer Use", "Unknown/NFF"],
                "Count": [85, 45, 65, 35, 145]
            })
            fig = px.pie(rc_data, values="Count", names="Root Cause",
                        title="Root Cause Analysis (YTD)",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("#### FA Cycle Time")
            cycle_data = pd.DataFrame({
                "Type": ["Standard", "Expedited", "Complex"],
                "Target (days)": [14, 5, 30],
                "Actual (days)": [12, 4, 28]
            })
            fig = px.bar(cycle_data, x="Type", y=["Target (days)", "Actual (days)"],
                        title="FA Cycle Time vs Target",
                        barmode="group",
                        color_discrete_sequence=["#94a3b8", TELIT_GREEN])
            st.plotly_chart(fig, use_container_width=True)
    
    with rma_tab4:
        st.markdown("### Return Trends")
        
        # Monthly trend by product
        st.markdown("#### Returns by Product Family (Monthly)")
        months = pd.date_range(start="2024-07-01", periods=6, freq="M")
        product_returns = pd.DataFrame({
            "Month": months.tolist() * 4,
            "Product": ["ME910"] * 6 + ["LE910"] * 6 + ["FN920"] * 6 + ["Other"] * 6,
            "Returns": [15, 12, 18, 14, 12, 10, 20, 18, 22, 19, 16, 15, 5, 8, 6, 7, 5, 6, 8, 6, 9, 8, 7, 8]
        })
        fig = px.line(product_returns, x="Month", y="Returns", color="Product",
                     title="Return Trend by Product Family",
                     markers=True)
        st.plotly_chart(fig, use_container_width=True)
        
        # YoY comparison
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Year-over-Year Comparison")
            yoy_data = pd.DataFrame({
                "Metric": ["Total Returns", "Return Rate", "Avg Resolution", "NFF Rate", "Warranty Cost"],
                "2023": [485, "0.95%", "14 days", "28%", "$310K"],
                "2024": [455, "0.80%", "12 days", "32%", "$285K"],
                "Change": ["-6%", "-0.15pts", "-2 days", "+4pts", "-8%"]
            })
            st.dataframe(yoy_data, use_container_width=True)
    
    with rma_tab5:
        st.markdown("### Warranty Analysis")
        
        # Warranty metrics
        war_col1, war_col2, war_col3, war_col4 = st.columns(4)
        war_col1.metric("Warranty Reserve", "$1.2M", "balance")
        war_col2.metric("Claims YTD", "$285K", "vs $310K LY")
        war_col3.metric("Avg Claim Value", "$185", "-$12")
        war_col4.metric("Open Claims", "28", "in process")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            # Warranty cost by product
            warranty_prod = pd.DataFrame({
                "Product": ["ME910", "LE910", "FN920", "ME310", "NE310"],
                "Claims": [85, 72, 45, 58, 25],
                "Cost ($K)": [95, 82, 58, 35, 15]
            })
            fig = px.bar(warranty_prod, x="Product", y="Cost ($K)",
                        title="Warranty Cost by Product",
                        color_discrete_sequence=[TELIT_BLUE])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Warranty by failure type
            warranty_type = pd.DataFrame({
                "Type": ["Replacement", "Repair", "Credit", "No Charge"],
                "Count": [180, 95, 45, 135]
            })
            fig = px.pie(warranty_type, values="Count", names="Type",
                        title="Warranty Resolution Type",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
    
    with rma_tab6:
        st.markdown("### Pareto Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            # Failure mode Pareto
            st.markdown("#### Top Failure Modes")
            failure_pareto = pd.DataFrame({
                "Failure Mode": ["No Network Connect", "Dead on Arrival", "Firmware Issue", "RF Performance", 
                                "Power Failure", "Overheating", "Mechanical", "Other"],
                "Count": [85, 72, 58, 45, 38, 32, 25, 100],
                "Cumulative %": [19, 35, 48, 58, 66, 73, 79, 100]
            })
            fig = px.bar(failure_pareto, x="Failure Mode", y="Count",
                        title="Failure Mode Pareto",
                        color_discrete_sequence=[TELIT_BLUE])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Customer Pareto
            st.markdown("#### Returns by Customer")
            customer_pareto = pd.DataFrame({
                "Customer": ["Continental AG", "Landis+Gyr", "Honeywell", "Geotab", "Other"],
                "Returns": [125, 95, 78, 52, 105]
            })
            fig = px.bar(customer_pareto, x="Customer", y="Returns",
                        title="Returns by Customer",
                        color_discrete_sequence=[TELIT_ORANGE])
            st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# PAGE: CM PORTAL
# =============================================================================
elif page == "🏭 CM Portal":
    st.title("🏭 Contract Manufacturer Portal")
    st.markdown("*CM performance, capacity, quality, and production visibility*")
    
    # KPI Summary
    cm1, cm2, cm3, cm4, cm5 = st.columns(5)
    cm1.metric("Active CMs", "4", "manufacturing partners")
    cm2.metric("Monthly Output", "2.8M", "units")
    cm3.metric("Avg Yield", "98.2%", "+0.3%")
    cm4.metric("On-Time Delivery", "96.5%", "+1.2%")
    cm5.metric("Quality (DPPM)", "125", "-15")
    
    st.markdown("---")
    
    cm_tab1, cm_tab2, cm_tab3, cm_tab4, cm_tab5, cm_tab6 = st.tabs([
        "📊 Overview", "🏭 Capacity", "✅ Quality", "📦 Inventory", "📅 Production", "📈 Scorecards"
    ])
    
    with cm_tab1:
        st.markdown("### CM Partner Overview")
        
        # CM summary
        cm_summary = pd.DataFrame({
            "CM Partner": ["Foxconn (TW)", "Flex (MY)", "Jabil (CN)", "Pegatron (TW)"],
            "Location": ["Taiwan", "Malaysia", "China", "Taiwan"],
            "Products": ["ME910, LE910", "FN920, FN990", "ME310, NE310", "Accessories"],
            "Monthly Capacity": ["1.5M", "800K", "600K", "400K"],
            "Utilization": ["78%", "85%", "72%", "65%"],
            "Quality Score": [98.5, 97.8, 98.2, 96.5],
            "OTD": ["97%", "95%", "96%", "98%"],
            "Status": ["🟢 Active", "🟢 Active", "🟢 Active", "🟢 Active"]
        })
        st.dataframe(cm_summary, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            # Volume by CM
            cm_volume = pd.DataFrame({
                "CM": ["Foxconn", "Flex", "Jabil", "Pegatron"],
                "Volume (K)": [1170, 680, 432, 260]
            })
            fig = px.pie(cm_volume, values="Volume (K)", names="CM",
                        title="Production Volume by CM (Monthly)",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Performance comparison
            cm_perf = pd.DataFrame({
                "Metric": ["Quality", "Delivery", "Cost", "Flexibility"],
                "Foxconn": [98, 97, 85, 90],
                "Flex": [96, 95, 92, 88],
                "Jabil": [97, 96, 88, 85],
                "Pegatron": [94, 98, 95, 82]
            })
            fig = go.Figure()
            for cm in ["Foxconn", "Flex", "Jabil", "Pegatron"]:
                fig.add_trace(go.Scatterpolar(r=cm_perf[cm].tolist() + [cm_perf[cm].iloc[0]],
                                              theta=cm_perf["Metric"].tolist() + [cm_perf["Metric"].iloc[0]],
                                              name=cm))
            fig.update_layout(title="CM Performance Radar", polar=dict(radialaxis=dict(range=[70, 100])))
            st.plotly_chart(fig, use_container_width=True)
    
    with cm_tab2:
        st.markdown("### Capacity Planning")
        
        # Capacity summary
        cap_col1, cap_col2, cap_col3, cap_col4 = st.columns(4)
        cap_col1.metric("Total Capacity", "3.3M/mo", "units")
        cap_col2.metric("Current Load", "2.54M/mo", "77%")
        cap_col3.metric("Available", "760K/mo", "headroom")
        cap_col4.metric("Q1 Forecast", "2.8M/mo", "+10%")
        
        st.markdown("---")
        
        # Capacity by CM
        st.markdown("#### Capacity Utilization by CM")
        capacity_data = pd.DataFrame({
            "CM": ["Foxconn", "Flex", "Jabil", "Pegatron"],
            "Capacity (K)": [1500, 800, 600, 400],
            "Current (K)": [1170, 680, 432, 260],
            "Available (K)": [330, 120, 168, 140]
        })
        fig = px.bar(capacity_data, x="CM", y=["Current (K)", "Available (K)"],
                    title="CM Capacity Utilization",
                    barmode="stack",
                    color_discrete_sequence=[TELIT_BLUE, "#e2e8f0"])
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast
        st.markdown("#### 6-Month Capacity Forecast")
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        forecast_data = pd.DataFrame({
            "Month": months,
            "Demand": [2.5, 2.7, 2.9, 3.0, 2.8, 2.6],
            "Capacity": [3.3, 3.3, 3.3, 3.5, 3.5, 3.5]
        })
        fig = px.line(forecast_data, x="Month", y=["Demand", "Capacity"],
                     title="Demand vs Capacity (M units)",
                     markers=True,
                     color_discrete_sequence=[TELIT_ORANGE, TELIT_GREEN])
        st.plotly_chart(fig, use_container_width=True)
    
    with cm_tab3:
        st.markdown("### CM Quality Performance")
        
        # Quality metrics
        qual_col1, qual_col2, qual_col3, qual_col4 = st.columns(4)
        qual_col1.metric("Avg FPY", "98.2%", "+0.3%")
        qual_col2.metric("DPPM", "125", "-15")
        qual_col3.metric("Escapes", "2", "this month")
        qual_col4.metric("SCARs Open", "5", "supplier issues")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            # Quality trend
            months = pd.date_range(start="2024-07-01", periods=6, freq="M")
            qual_trend = pd.DataFrame({
                "Month": months,
                "FPY %": [97.5, 97.8, 98.0, 98.1, 98.3, 98.2]
            })
            fig = px.line(qual_trend, x="Month", y="FPY %",
                         title="First Pass Yield Trend",
                         markers=True)
            fig.update_traces(line_color=TELIT_GREEN)
            fig.add_hline(y=98.0, line_dash="dash", line_color="red", annotation_text="Target")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Defect Pareto
            defect_data = pd.DataFrame({
                "Defect": ["Solder", "Component", "Visual", "Functional", "Other"],
                "Count": [45, 32, 25, 18, 12]
            })
            fig = px.bar(defect_data, x="Defect", y="Count",
                        title="Defect Pareto (This Month)",
                        color_discrete_sequence=[TELIT_RED])
            st.plotly_chart(fig, use_container_width=True)
    
    with cm_tab4:
        st.markdown("### CM Inventory Visibility")
        
        # Inventory at CMs
        st.markdown("#### Raw Material & WIP at CM Sites")
        cm_inv = pd.DataFrame({
            "CM": ["Foxconn", "Flex", "Jabil", "Pegatron"],
            "Raw Material ($M)": [4.2, 2.8, 2.1, 1.2],
            "WIP ($M)": [1.8, 1.2, 0.9, 0.4],
            "Finished ($M)": [2.5, 1.5, 1.2, 0.8],
            "Total ($M)": [8.5, 5.5, 4.2, 2.4],
            "DOS": [12, 14, 15, 18]
        })
        st.dataframe(cm_inv, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            # Inventory by stage
            inv_stage = pd.DataFrame({
                "Stage": ["Raw Material", "WIP", "Finished Goods"],
                "Value ($M)": [10.3, 4.3, 6.0]
            })
            fig = px.pie(inv_stage, values="Value ($M)", names="Stage",
                        title="Inventory by Stage",
                        color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Critical components
            st.markdown("#### Critical Component Status")
            crit_comp = pd.DataFrame({
                "Component": ["Qualcomm MDM9207", "Sequans Monarch", "Infineon PMU", "Skyworks PA"],
                "CM Stock (wks)": [4, 6, 8, 5],
                "Status": ["🟡 Low", "🟢 OK", "🟢 OK", "🟡 Low"],
                "Action": ["PO expedite", "-", "-", "Alt source"]
            })
            st.dataframe(crit_comp, use_container_width=True)
    
    with cm_tab5:
        st.markdown("### Production Schedule")
        
        # Current week production
        st.markdown("#### This Week's Production Plan")
        prod_plan = pd.DataFrame({
            "CM": ["Foxconn", "Foxconn", "Flex", "Flex", "Jabil", "Pegatron"],
            "Product": ["ME910C1", "LE910Cx", "FN920", "FN990", "ME310G1", "Accessories"],
            "Plan (K)": [180, 112, 85, 42, 65, 45],
            "Actual (K)": [175, 108, 82, 40, 62, 44],
            "Variance": ["-3%", "-4%", "-4%", "-5%", "-5%", "-2%"],
            "Status": ["🟢 On Track", "🟢 On Track", "🟢 On Track", "🟡 Behind", "🟢 On Track", "🟢 On Track"]
        })
        st.dataframe(prod_plan, use_container_width=True)
        
        # Production trend
        st.markdown("#### Weekly Production Output")
        weeks = ["W48", "W49", "W50", "W51", "W52", "W1"]
        prod_trend = pd.DataFrame({
            "Week": weeks,
            "Plan (K)": [650, 680, 700, 620, 550, 680],
            "Actual (K)": [642, 668, 685, 615, 545, 665]
        })
        fig = px.bar(prod_trend, x="Week", y=["Plan (K)", "Actual (K)"],
                    title="Weekly Production vs Plan",
                    barmode="group",
                    color_discrete_sequence=["#94a3b8", TELIT_GREEN])
        st.plotly_chart(fig, use_container_width=True)
    
    with cm_tab6:
        st.markdown("### CM Scorecards")
        
        # Quarterly scorecard
        st.markdown("#### Q4 2024 Performance Scorecard")
        scorecard = pd.DataFrame({
            "Metric": ["Quality (FPY)", "On-Time Delivery", "Cost Competitiveness", "Responsiveness", 
                      "Inventory Accuracy", "Overall Score"],
            "Weight": ["25%", "25%", "20%", "15%", "15%", "100%"],
            "Foxconn": [98.5, 97, 85, 90, 96, 93.8],
            "Flex": [97.8, 95, 92, 88, 94, 93.1],
            "Jabil": [98.2, 96, 88, 85, 95, 92.5],
            "Pegatron": [96.5, 98, 95, 82, 92, 92.4]
        })
        st.dataframe(scorecard, use_container_width=True)
        
        # Score trend
        st.markdown("#### Overall Score Trend")
        quarters = ["Q1", "Q2", "Q3", "Q4"]
        score_trend = pd.DataFrame({
            "Quarter": quarters * 4,
            "CM": ["Foxconn"] * 4 + ["Flex"] * 4 + ["Jabil"] * 4 + ["Pegatron"] * 4,
            "Score": [92.1, 92.8, 93.2, 93.8, 91.5, 92.2, 92.8, 93.1, 91.8, 92.0, 92.2, 92.5, 90.5, 91.2, 91.8, 92.4]
        })
        fig = px.line(score_trend, x="Quarter", y="Score", color="CM",
                     title="CM Performance Score Trend",
                     markers=True)
        st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# PAGE: FINANCIAL & COSTING
# =============================================================================
elif page == "💱 Financial & Costing":
    st.title("💱 Financial & Costing Analysis")
    st.markdown("*Landed cost, currency exposure, tariffs, and cost analytics*")
    
    # KPI Summary
    f1, f2, f3, f4, f5 = st.columns(5)
    f1.metric("Total COGS", "$313M", "YTD")
    f2.metric("Gross Margin", "38.5%", "+1.2 pts")
    f3.metric("Landed Cost Avg", "$12.85", "-$0.42")
    f4.metric("Tariff Exposure", "$8.2M", "Section 301")
    f5.metric("FX Impact", "-$2.1M", "EUR/USD")
    
    st.markdown("---")
    
    fin_tab1, fin_tab2, fin_tab3, fin_tab4, fin_tab5, fin_tab6 = st.tabs([
        "📊 Overview", "💵 Landed Cost", "🌍 Currency", "📦 Tariffs", "📈 Variance", "🎯 Savings"
    ])
    
    with fin_tab1:
        st.markdown("### Financial Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            # Cost breakdown
            cost_breakdown = pd.DataFrame({
                "Category": ["Materials", "Labor", "Overhead", "Logistics", "Tariffs/Duties"],
                "Cost ($M)": [185, 42, 35, 28, 23]
            })
            fig = px.pie(cost_breakdown, values="Cost ($M)", names="Category",
                        title="COGS Breakdown",
                        color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Margin trend
            months = pd.date_range(start="2024-01-01", periods=12, freq="M")
            margin_trend = pd.DataFrame({
                "Month": months,
                "Gross Margin %": [36.8, 37.2, 37.5, 37.8, 38.0, 38.2, 38.1, 38.3, 38.4, 38.5, 38.6, 38.5]
            })
            fig = px.line(margin_trend, x="Month", y="Gross Margin %",
                         title="Gross Margin Trend",
                         markers=True)
            fig.update_traces(line_color=TELIT_GREEN)
            st.plotly_chart(fig, use_container_width=True)
        
        # Margin by product
        st.markdown("#### Margin by Product Family")
        margin_prod = pd.DataFrame({
            "Product": ["ME910", "LE910", "FN920", "ME310", "NE310", "FN990"],
            "Revenue ($M)": [45.2, 68.5, 42.8, 38.4, 22.1, 8.5],
            "COGS ($M)": [27.1, 42.5, 25.7, 24.2, 14.4, 5.5],
            "Gross Margin": ["40.0%", "38.0%", "40.0%", "37.0%", "35.0%", "35.3%"],
            "vs Target": ["+2.0%", "On Target", "+2.0%", "-1.0%", "-3.0%", "-2.7%"]
        })
        st.dataframe(margin_prod, use_container_width=True)
    
    with fin_tab2:
        st.markdown("### Landed Cost Analysis")
        
        # Landed cost components
        st.markdown("#### Landed Cost Breakdown (per unit avg)")
        landed_cost = pd.DataFrame({
            "Component": ["FOB Cost", "Ocean Freight", "Insurance", "Customs/Duties", "Inland Transport", "Handling"],
            "Cost ($)": [10.50, 0.85, 0.12, 0.95, 0.28, 0.15],
            "% of Total": [81.7, 6.6, 0.9, 7.4, 2.2, 1.2]
        })
        fig = px.bar(landed_cost, x="Component", y="Cost ($)",
                    title="Landed Cost Components",
                    color_discrete_sequence=[TELIT_BLUE])
        st.plotly_chart(fig, use_container_width=True)
        
        # By origin
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Landed Cost by Origin")
            origin_cost = pd.DataFrame({
                "Origin": ["Taiwan", "Malaysia", "China", "Europe"],
                "Volume %": [45, 25, 22, 8],
                "Landed Cost": ["$12.45", "$12.25", "$13.85", "$14.20"],
                "Transit Days": [18, 22, 28, 12]
            })
            st.dataframe(origin_cost, use_container_width=True)
        
        with col2:
            st.markdown("#### Landed Cost by Destination")
            dest_cost = pd.DataFrame({
                "Destination": ["US (West)", "US (East)", "Europe", "APAC"],
                "Volume %": [35, 25, 28, 12],
                "Landed Cost": ["$12.15", "$12.95", "$12.45", "$11.85"],
                "Transit Days": [15, 22, 25, 8]
            })
            st.dataframe(dest_cost, use_container_width=True)
    
    with fin_tab3:
        st.markdown("### Currency Exposure")
        
        # FX summary
        fx_col1, fx_col2, fx_col3, fx_col4 = st.columns(4)
        fx_col1.metric("EUR Exposure", "$125M", "40% of Rev")
        fx_col2.metric("CNY Exposure", "$85M", "COGS")
        fx_col3.metric("JPY Exposure", "$28M", "Components")
        fx_col4.metric("Hedged %", "65%", "of exposure")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            # FX rates trend
            months = pd.date_range(start="2024-07-01", periods=6, freq="M")
            fx_trend = pd.DataFrame({
                "Month": months,
                "EUR/USD": [1.08, 1.09, 1.10, 1.08, 1.07, 1.09],
                "USD/CNY": [7.18, 7.15, 7.12, 7.10, 7.08, 7.12]
            })
            fig = px.line(fx_trend, x="Month", y=["EUR/USD"],
                         title="EUR/USD Exchange Rate",
                         markers=True)
            fig.update_traces(line_color=TELIT_BLUE)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Hedge position
            hedge_data = pd.DataFrame({
                "Currency": ["EUR", "CNY", "JPY", "TWD"],
                "Exposure ($M)": [125, 85, 28, 45],
                "Hedged ($M)": [95, 50, 15, 25],
                "Hedge %": ["76%", "59%", "54%", "56%"]
            })
            fig = px.bar(hedge_data, x="Currency", y=["Exposure ($M)", "Hedged ($M)"],
                        title="Currency Hedge Position",
                        barmode="group",
                        color_discrete_sequence=[TELIT_ORANGE, TELIT_GREEN])
            st.plotly_chart(fig, use_container_width=True)
    
    with fin_tab4:
        st.markdown("### Tariff & Duty Analysis")
        
        st.warning("⚠️ **Section 301 Tariffs:** $8.2M annual exposure on China-origin products")
        
        # Tariff summary
        tariff_data = pd.DataFrame({
            "Origin": ["China", "Taiwan", "Malaysia", "Mexico"],
            "HTS Code": ["8517.62", "8517.62", "8517.62", "8517.62"],
            "MFN Rate": ["0%", "0%", "0%", "0%"],
            "Section 301": ["25%", "0%", "0%", "0%"],
            "Other": ["0%", "0%", "0%", "0%"],
            "Annual Volume ($M)": [32.8, 145.2, 82.5, 18.5],
            "Duty Cost ($M)": [8.2, 0, 0, 0]
        })
        st.dataframe(tariff_data, use_container_width=True)
        
        # Mitigation
        st.markdown("#### Tariff Mitigation Strategies")
        mit_col1, mit_col2 = st.columns(2)
        with mit_col1:
            st.markdown("""
            **Active Strategies:**
            - 🔄 **Production Shift:** Moving 40% of China volume to Malaysia
            - 📋 **Exclusion Requests:** 3 pending with USTR
            - 🏭 **USMCA Origin:** Qualifying products for Mexico origin
            - 📦 **FTZ Usage:** Using Foreign Trade Zones for deferral
            """)
        with mit_col2:
            savings_data = pd.DataFrame({
                "Strategy": ["Malaysia Shift", "Exclusions", "USMCA", "FTZ"],
                "Savings ($M)": [3.2, 1.5, 0.8, 0.4],
                "Status": ["🔄 In Progress", "📋 Pending", "✅ Active", "✅ Active"]
            })
            st.dataframe(savings_data, use_container_width=True)
    
    with fin_tab5:
        st.markdown("### Cost Variance Analysis")
        
        # Variance summary
        var_col1, var_col2, var_col3, var_col4 = st.columns(4)
        var_col1.metric("Material Variance", "-$1.2M", "favorable")
        var_col2.metric("Labor Variance", "+$0.3M", "unfavorable")
        var_col3.metric("Overhead Variance", "-$0.5M", "favorable")
        var_col4.metric("Net Variance", "-$1.4M", "favorable")
        
        st.markdown("---")
        
        # Variance by product
        st.markdown("#### Standard Cost vs Actual by Product")
        variance_prod = pd.DataFrame({
            "Product": ["ME910", "LE910", "FN920", "ME310", "NE310"],
            "Std Cost": ["$8.50", "$11.20", "$28.50", "$7.80", "$5.20"],
            "Actual Cost": ["$8.35", "$11.45", "$27.80", "$7.65", "$5.35"],
            "Variance": ["-$0.15", "+$0.25", "-$0.70", "-$0.15", "+$0.15"],
            "Variance %": ["-1.8%", "+2.2%", "-2.5%", "-1.9%", "+2.9%"],
            "Root Cause": ["Material", "Labor", "Material", "Material", "Yield"]
        })
        st.dataframe(variance_prod, use_container_width=True)
        
        # Trend
        months = pd.date_range(start="2024-07-01", periods=6, freq="M")
        var_trend = pd.DataFrame({
            "Month": months,
            "Material": [-150, -120, -180, -200, -220, -280],
            "Labor": [20, 35, 45, 30, 25, 45],
            "Overhead": [-50, -80, -65, -90, -75, -85]
        })
        fig = px.bar(var_trend, x="Month", y=["Material", "Labor", "Overhead"],
                    title="Cost Variance Trend ($K)",
                    barmode="relative",
                    color_discrete_sequence=[TELIT_GREEN, TELIT_RED, TELIT_BLUE])
        st.plotly_chart(fig, use_container_width=True)
    
    with fin_tab6:
        st.markdown("### Cost Savings Initiatives")
        
        # Savings summary
        sav_col1, sav_col2, sav_col3 = st.columns(3)
        sav_col1.metric("YTD Savings", "$4.8M", "vs target $5.0M")
        sav_col2.metric("Pipeline", "$2.5M", "identified")
        sav_col3.metric("% of COGS", "1.5%", "savings rate")
        
        st.markdown("---")
        
        # Savings projects
        st.markdown("#### Active Cost Reduction Projects")
        savings_projects = pd.DataFrame({
            "Project": ["Supplier Consolidation", "Design-for-Cost FN990", "Logistics Optimization", 
                       "Component Re-source", "Yield Improvement"],
            "Category": ["Procurement", "Engineering", "Logistics", "Procurement", "Manufacturing"],
            "Target ($K)": [850, 620, 380, 450, 280],
            "Achieved ($K)": [780, 520, 350, 280, 250],
            "Status": ["🟢 On Track", "🟢 On Track", "🟢 On Track", "🟡 Behind", "🟢 On Track"],
            "Owner": ["Procurement", "Engineering", "Supply Chain", "Procurement", "Operations"]
        })
        st.dataframe(savings_projects, use_container_width=True)
        
        # Savings trend
        st.markdown("#### Cumulative Savings vs Target")
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        savings_trend = pd.DataFrame({
            "Month": months,
            "Target": [0.4, 0.8, 1.3, 1.8, 2.3, 2.8, 3.3, 3.8, 4.2, 4.6, 4.8, 5.0],
            "Actual": [0.3, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.6, 4.0, 4.4, 4.6, 4.8]
        })
        fig = px.line(savings_trend, x="Month", y=["Target", "Actual"],
                     title="Cumulative Savings ($M)",
                     markers=True,
                     color_discrete_sequence=["#94a3b8", TELIT_GREEN])
        st.plotly_chart(fig, use_container_width=True)

# =============================================================================
# PAGE: CARBON ESG
# =============================================================================
elif page == "🌱 Carbon ESG":
    st.markdown(f"""<div class="hero-section" style="background: linear-gradient(135deg, #2d5a27 0%, #1a3d1a 100%);">
        <h1 style="margin: 0; color: white;">🌱 Carbon Footprint & ESG</h1>
        <p style="opacity: 0.9; color: white;">Sustainability metrics, environmental impact, and ESG reporting</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("Total CO₂", "12,450 t", "-8.5%"),
        ("Intensity", "312 g/unit", "-12%"),
        ("Renewable", "62%", "+8%"),
        ("Waste Diverted", "78%", "+5%"),
        ("Water Recycled", "45%", "+12%"),
        ("ESG Score", "B+", "↑"),
        ("Suppliers Audited", "85%", "+10%"),
        ("Net Zero Target", "2035", "On Track")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    esg_tab1, esg_tab2, esg_tab3, esg_tab4, esg_tab5, esg_tab6, esg_tab7 = st.tabs([
        "📊 Overview",
        "🏭 Emissions",
        "⚡ Energy",
        "♻️ Waste & Water",
        "🌍 Supply Chain",
        "📋 Reporting",
        "🎯 Goals"
    ])
    
    # =================================================================
    # TAB 1: OVERVIEW
    # =================================================================
    with esg_tab1:
        st.subheader("📊 ESG Dashboard Overview")
        
        # ESG scorecard
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #2d5a2720, #1a3d1a10); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_GREEN};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">🏆 ESG Performance: STRONG</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">Above industry average in all three pillars. On track for 2025 targets.</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 48px; font-weight: 700; color: {TELIT_GREEN};">B+</div>
                    <div style="color: {TELIT_GRAY}; font-size: 12px;">MSCI ESG Rating</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Three pillars
        pillar_cols = st.columns(3)
        pillars = [
            ("🌍 Environmental", "B+", "Carbon reduction ahead of plan, renewable energy adoption strong", TELIT_GREEN, [
                ("Carbon Intensity", "-12% YoY"),
                ("Renewable Energy", "62%"),
                ("Waste Diversion", "78%")
            ]),
            ("👥 Social", "A-", "Strong workforce development, community programs expanding", TELIT_BLUE, [
                ("Employee Safety", "0.8 TRIR"),
                ("Training Hours", "42 avg/emp"),
                ("Diversity", "38% female")
            ]),
            ("🏛️ Governance", "A", "Robust policies, transparent reporting, ethical supply chain", TELIT_GREEN, [
                ("Board Independence", "80%"),
                ("Ethics Training", "100%"),
                ("Audit Compliance", "100%")
            ]),
        ]
        for col, (pillar, score, desc, color, metrics) in zip(pillar_cols, pillars):
            metrics_html = "".join([f"<div style='display: flex; justify-content: space-between; font-size: 11px; margin: 3px 0;'><span>{m[0]}</span><strong>{m[1]}</strong></div>" for m in metrics])
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 18px; border-top: 4px solid {color}; height: 220px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-size: 16px; font-weight: 700; color: {color};">{pillar}</div>
                    <div style="font-size: 24px; font-weight: 700; color: {color};">{score}</div>
                </div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin: 10px 0;">{desc}</div>
                <div style="margin-top: 12px; border-top: 1px solid {color}30; padding-top: 10px;">
                    {metrics_html}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Progress toward goals
        st.markdown("---")
        st.markdown("##### 🎯 2025 Target Progress")
        goal_cols = st.columns(4)
        goals = [
            ("Carbon Reduction", 75, "30% reduction", "22.5% achieved", TELIT_GREEN),
            ("Renewable Energy", 82, "75% by 2025", "62% current", TELIT_GREEN),
            ("Zero Waste", 65, "90% diversion", "78% current", TELIT_ORANGE),
            ("Supplier ESG Audit", 85, "100% Tier 1", "85% complete", TELIT_GREEN),
        ]
        for col, (goal, progress, target, current, color) in zip(goal_cols, goals):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center;">
                <div style="font-size: 12px; font-weight: 600;">{goal}</div>
                <div style="font-size: 28px; font-weight: 700; color: {color}; margin: 8px 0;">{progress}%</div>
                <div style="background: #e0e5ec; border-radius: 4px; height: 8px; overflow: hidden; margin: 8px 0;">
                    <div style="background: {color}; width: {progress}%; height: 100%;"></div>
                </div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{current}</div>
                <div style="font-size: 9px; color: {color};">{target}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 2: EMISSIONS
    # =================================================================
    with esg_tab2:
        st.subheader("🏭 Carbon Emissions")
        
        # Emissions KPIs
        em_kpis = st.columns(5)
        em_kpis[0].metric("Total Emissions", "12,450 tCO₂e", "-8.5%")
        em_kpis[1].metric("Scope 1", "3,200 tCO₂e", "-5%")
        em_kpis[2].metric("Scope 2", "7,800 tCO₂e", "-12%")
        em_kpis[3].metric("Scope 3", "1,450 tCO₂e", "-3%")
        em_kpis[4].metric("Intensity", "312 g/unit", "-12%")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Emissions by Scope")
            scopes = pd.DataFrame({
                'Scope': ['Scope 1 (Direct)', 'Scope 2 (Energy)', 'Scope 3 (Value Chain)'],
                'Emissions': [3200, 7800, 1450],
                'Description': ['On-site fuel combustion', 'Purchased electricity', 'Supply chain & logistics']
            })
            
            fig_scope = go.Figure(go.Pie(
                labels=scopes['Scope'], values=scopes['Emissions'], hole=0.55,
                marker_colors=[TELIT_ORANGE, TELIT_BLUE, TELIT_GREEN]
            ))
            fig_scope.add_annotation(text="<b>12,450</b><br>tCO₂e", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_scope.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_scope, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Emissions Trend (YoY)")
            years = ['2020', '2021', '2022', '2023', '2024']
            emissions = [16500, 15200, 14100, 13600, 12450]
            target = [16500, 15675, 14850, 14025, 13200]
            
            fig_trend = go.Figure()
            fig_trend.add_trace(go.Scatter(x=years, y=emissions, name="Actual", mode='lines+markers',
                                          line=dict(color=TELIT_GREEN, width=3)))
            fig_trend.add_trace(go.Scatter(x=years, y=target, name="Target Path", mode='lines',
                                          line=dict(color=TELIT_ORANGE, width=2, dash='dash')))
            fig_trend.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="tCO₂e")
            st.plotly_chart(fig_trend, use_container_width=True)
        
        # Emissions by facility
        st.markdown("---")
        st.markdown("##### 🏭 Emissions by Facility")
        facility_data = pd.DataFrame({
            "Facility": ["🇮🇹 Trieste HQ", "🇨🇳 Shanghai", "🇺🇸 Irvine", "🇮🇱 Tel Aviv R&D", "🇬🇧 Cambridge R&D"],
            "Scope 1": ["850", "1,200", "420", "380", "350"],
            "Scope 2": ["2,100", "3,500", "980", "650", "570"],
            "Total": ["2,950", "4,700", "1,400", "1,030", "920"],
            "Intensity": ["285 g/unit", "342 g/unit", "298 g/unit", "N/A", "N/A"],
            "Trend": ["📉 -10%", "📉 -8%", "📉 -12%", "📉 -5%", "📉 -7%"],
            "Renewable": ["72%", "45%", "85%", "68%", "92%"]
        })
        st.dataframe(facility_data, use_container_width=True)
    
    # =================================================================
    # TAB 3: ENERGY
    # =================================================================
    with esg_tab3:
        st.subheader("⚡ Energy Management")
        
        # Energy KPIs
        energy_kpis = st.columns(5)
        energy_kpis[0].metric("Total Energy", "42.5 GWh", "-5%")
        energy_kpis[1].metric("Renewable", "62%", "+8%")
        energy_kpis[2].metric("Solar On-site", "8.5 MW", "+2 MW")
        energy_kpis[3].metric("Energy/Unit", "0.42 kWh", "-8%")
        energy_kpis[4].metric("PPA Coverage", "45%", "+15%")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### ⚡ Energy Mix")
            sources = ["Grid (Non-Renewable)", "Grid (Renewable)", "On-site Solar", "PPAs"]
            values = [38, 17, 20, 25]
            
            fig_mix = go.Figure(go.Pie(
                labels=sources, values=values, hole=0.55,
                marker_colors=[TELIT_GRAY, TELIT_BLUE, '#FFD700', TELIT_GREEN]
            ))
            fig_mix.add_annotation(text="<b>62%</b><br>Renewable", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_mix.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_mix, use_container_width=True)
        
        with col2:
            st.markdown("##### 📈 Renewable Energy Growth")
            years = ['2020', '2021', '2022', '2023', '2024', '2025 (T)']
            renewable_pct = [28, 35, 42, 54, 62, 75]
            
            fig_renewable = go.Figure()
            fig_renewable.add_trace(go.Bar(x=years, y=renewable_pct, marker_color=TELIT_GREEN,
                                          text=[f"{r}%" for r in renewable_pct], textposition="outside"))
            fig_renewable.add_hline(y=75, line_dash="dash", line_color=TELIT_ORANGE, annotation_text="2025 Target")
            fig_renewable.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="% Renewable")
            st.plotly_chart(fig_renewable, use_container_width=True)
        
        # Energy efficiency projects
        st.markdown("---")
        st.markdown("##### 🔧 Energy Efficiency Projects")
        projects = pd.DataFrame({
            "Project": ["Shanghai Solar Expansion", "Trieste LED Retrofit", "HVAC Optimization", "Smart Building System", "Motor VFD Upgrades"],
            "Facility": ["Shanghai", "Trieste", "All Sites", "Irvine", "Shanghai"],
            "Investment": ["$1.2M", "$180K", "$350K", "$420K", "$95K"],
            "Annual Savings": ["$280K", "$45K", "$120K", "$85K", "$32K"],
            "CO₂ Reduction": ["850 t/yr", "120 t/yr", "380 t/yr", "210 t/yr", "95 t/yr"],
            "Status": ["🟢 Complete", "🟢 Complete", "🔵 In Progress", "🔵 In Progress", "🟢 Complete"],
            "Payback": ["4.3 yrs", "4.0 yrs", "2.9 yrs", "4.9 yrs", "3.0 yrs"]
        })
        st.dataframe(projects, use_container_width=True)
    
    # =================================================================
    # TAB 4: WASTE & WATER
    # =================================================================
    with esg_tab4:
        st.subheader("♻️ Waste & Water Management")
        
        # Waste/Water KPIs
        ww_kpis = st.columns(5)
        ww_kpis[0].metric("Waste Generated", "1,850 t", "-12%")
        ww_kpis[1].metric("Diversion Rate", "78%", "+5%")
        ww_kpis[2].metric("Recycled", "1,145 t", "+8%")
        ww_kpis[3].metric("Water Used", "125M L", "-8%")
        ww_kpis[4].metric("Water Recycled", "45%", "+12%")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### ♻️ Waste Breakdown")
            waste_types = ["Recycled Electronics", "Recycled Packaging", "Recycled Metal", "Composted", "Landfill", "Hazardous (Treated)"]
            waste_amounts = [420, 385, 280, 60, 407, 298]
            
            fig_waste = go.Figure(go.Pie(
                labels=waste_types, values=waste_amounts, hole=0.55,
                marker_colors=[TELIT_GREEN, TELIT_BLUE, '#88B04B', '#6B5B95', TELIT_GRAY, TELIT_ORANGE]
            ))
            fig_waste.add_annotation(text="<b>78%</b><br>Diverted", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_waste.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_waste, use_container_width=True)
        
        with col2:
            st.markdown("##### 💧 Water Usage by Facility")
            facilities = ["Shanghai", "Trieste", "Irvine", "Tel Aviv", "Cambridge"]
            water_used = [52, 38, 18, 10, 7]
            water_recycled = [48, 42, 52, 38, 45]
            
            fig_water = go.Figure()
            fig_water.add_trace(go.Bar(name="Water Used (M L)", x=facilities, y=water_used, marker_color=TELIT_BLUE))
            fig_water.add_trace(go.Scatter(name="% Recycled", x=facilities, y=water_recycled, yaxis="y2",
                                          mode='lines+markers', line=dict(color=TELIT_GREEN, width=2)))
            fig_water.update_layout(height=300, margin=dict(l=20, r=60, t=10, b=40),
                                   yaxis=dict(title="Million Liters"),
                                   yaxis2=dict(title="% Recycled", overlaying="y", side="right", range=[0, 100]))
            st.plotly_chart(fig_water, use_container_width=True)
        
        # Circular economy initiatives
        st.markdown("---")
        st.markdown("##### 🔄 Circular Economy Initiatives")
        circular_cols = st.columns(4)
        circular_data = [
            ("♻️ E-Waste Program", "95%", "Recovery rate for end-of-life products", TELIT_GREEN),
            ("📦 Packaging Reduction", "-35%", "Plastic packaging eliminated", TELIT_GREEN),
            ("🔧 Refurbishment", "12,500", "Units refurbished vs scrapped", TELIT_BLUE),
            ("🏭 Closed-Loop", "42%", "Recycled content in new products", TELIT_ORANGE),
        ]
        for col, (initiative, value, desc, color) in zip(circular_cols, circular_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 600;">{initiative}</div>
                <div style="font-size: 26px; font-weight: 700; color: {color}; margin: 8px 0;">{value}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 5: SUPPLY CHAIN ESG
    # =================================================================
    with esg_tab5:
        st.subheader("🌍 Supply Chain Sustainability")
        
        # Supply chain KPIs
        sc_kpis = st.columns(5)
        sc_kpis[0].metric("Suppliers Audited", "40/47", "85%")
        sc_kpis[1].metric("Compliant", "38", "95%")
        sc_kpis[2].metric("High ESG Score", "28", "70%")
        sc_kpis[3].metric("Conflict-Free", "100%", "Minerals")
        sc_kpis[4].metric("Scope 3 Mapped", "72%", "+15%")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Supplier ESG Performance")
            suppliers = ["Murata", "u-blox", "Samsung", "Qualcomm", "Skyworks", "JCET", "Infineon", "STMicro"]
            esg_scores = [92, 88, 85, 82, 78, 72, 85, 80]
            
            fig_supplier_esg = go.Figure(go.Bar(
                x=esg_scores, y=suppliers, orientation='h',
                marker_color=[TELIT_GREEN if s >= 80 else TELIT_ORANGE if s >= 70 else TELIT_RED for s in esg_scores],
                text=esg_scores, textposition="outside"
            ))
            fig_supplier_esg.add_vline(x=80, line_dash="dash", line_color="green", annotation_text="Target")
            fig_supplier_esg.update_layout(height=300, margin=dict(l=10, r=60, t=10, b=10), xaxis_title="ESG Score", xaxis=dict(range=[60, 100]))
            st.plotly_chart(fig_supplier_esg, use_container_width=True)
        
        with col2:
            st.markdown("##### 🌍 Scope 3 Emissions Breakdown")
            scope3_categories = ["Purchased Goods", "Transportation", "Business Travel", "Employee Commute", "Other"]
            scope3_values = [680, 420, 180, 120, 50]
            
            fig_scope3 = go.Figure(go.Pie(
                labels=scope3_categories, values=scope3_values, hole=0.55,
                marker_colors=[TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN, '#6B5B95', TELIT_GRAY]
            ))
            fig_scope3.add_annotation(text="<b>1,450</b><br>tCO₂e", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_scope3.update_layout(height=300, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_scope3, use_container_width=True)
        
        # Supplier audit results
        st.markdown("---")
        st.markdown("##### 📋 Recent Supplier ESG Audits")
        audits = pd.DataFrame({
            "Supplier": ["Murata", "u-blox", "JCET", "Samsung", "Skyworks"],
            "Audit Date": ["Dec 2024", "Nov 2024", "Oct 2024", "Sep 2024", "Aug 2024"],
            "Score": ["92", "88", "72", "85", "78"],
            "Status": ["🟢 Excellent", "🟢 Good", "🟡 Needs Improvement", "🟢 Good", "🟡 Needs Improvement"],
            "Key Findings": ["None", "Minor documentation", "Worker hours concern", "Energy efficiency gap", "Waste handling"],
            "CAPA": ["—", "Closed", "In Progress", "Closed", "In Progress"],
            "Next Audit": ["Dec 2025", "Nov 2025", "Apr 2025", "Sep 2025", "Feb 2025"]
        })
        st.dataframe(audits, use_container_width=True)
    
    # =================================================================
    # TAB 6: REPORTING
    # =================================================================
    with esg_tab6:
        st.subheader("📋 ESG Reporting & Disclosure")
        
        # Reporting frameworks
        st.markdown("##### 📊 Reporting Frameworks")
        framework_cols = st.columns(4)
        frameworks = [
            ("🌐 GRI Standards", "✅ Aligned", "Global Reporting Initiative", TELIT_GREEN),
            ("📊 SASB", "✅ Aligned", "Industry-specific disclosure", TELIT_GREEN),
            ("🌡️ TCFD", "✅ Aligned", "Climate-related disclosure", TELIT_GREEN),
            ("🎯 CDP", "B Score", "Carbon Disclosure Project", TELIT_BLUE),
        ]
        for col, (framework, status, desc, color) in zip(framework_cols, frameworks):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 14px; font-weight: 600;">{framework}</div>
                <div style="font-size: 20px; font-weight: 700; color: {color}; margin: 8px 0;">{status}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Recent reports
        st.markdown("---")
        st.markdown("##### 📄 Published Reports")
        reports = pd.DataFrame({
            "Report": ["Annual ESG Report 2024", "CDP Climate Response", "GRI Index 2024", "TCFD Report", "Conflict Minerals Report"],
            "Type": ["Comprehensive", "Climate", "Standards Index", "Climate Risk", "Due Diligence"],
            "Published": ["Mar 2024", "Jul 2024", "Mar 2024", "Mar 2024", "May 2024"],
            "Pages": ["85", "42", "28", "35", "18"],
            "Assurance": ["Limited (EY)", "Self-declared", "Self-declared", "Self-declared", "Third-party"],
            "Download": ["📥 PDF", "📥 PDF", "📥 PDF", "📥 PDF", "📥 PDF"]
        })
        st.dataframe(reports, use_container_width=True)
        
        # Data quality
        st.markdown("---")
        st.markdown("##### 📊 ESG Data Quality Metrics")
        quality_cols = st.columns(4)
        quality_data = [
            ("Data Coverage", "95%", "of operations", TELIT_GREEN),
            ("Third-Party Verified", "72%", "of emissions data", TELIT_GREEN),
            ("Real-Time Monitoring", "65%", "of energy data", TELIT_BLUE),
            ("Automated Collection", "80%", "of metrics", TELIT_GREEN),
        ]
        for col, (metric, value, desc, color) in zip(quality_cols, quality_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; color: {TELIT_GRAY};">{metric}</div>
                <div style="font-size: 28px; font-weight: 700; color: {color}; margin: 5px 0;">{value}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 7: GOALS & TARGETS
    # =================================================================
    with esg_tab7:
        st.subheader("🎯 Sustainability Goals & Targets")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_GREEN};">
            <div style="font-size: 20px; font-weight: 700;">🌍 Net Zero by 2035</div>
            <div style="color: {TELIT_GRAY}; font-size: 14px; margin-top: 8px;">
                Committed to achieving net-zero greenhouse gas emissions across all scopes by 2035, 
                aligned with Science-Based Targets initiative (SBTi).
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Goals timeline
        st.markdown("##### 📅 Goals Roadmap")
        goals_data = pd.DataFrame({
            "Goal": ["50% Carbon Reduction", "75% Renewable Energy", "Zero Waste to Landfill", "100% Supplier ESG Audits", "Net Zero Operations"],
            "Target Year": ["2028", "2025", "2030", "2025", "2035"],
            "Baseline": ["16,500 tCO₂e (2020)", "28% (2020)", "45% diversion (2020)", "52% (2022)", "16,500 tCO₂e (2020)"],
            "Current": ["12,450 tCO₂e (25% reduction)", "62%", "78% diversion", "85%", "12,450 tCO₂e"],
            "Progress": ["50%", "82%", "65%", "85%", "25%"],
            "Status": ["🟢 On Track", "🟢 On Track", "🟡 At Risk", "🟢 On Track", "🟢 On Track"]
        })
        st.dataframe(goals_data, use_container_width=True)
        
        # Net zero pathway
        st.markdown("---")
        st.markdown("##### 📈 Net Zero Pathway")
        years = ['2020', '2022', '2024', '2026', '2028', '2030', '2032', '2034', '2035']
        emissions_path = [16500, 14100, 12450, 10500, 8250, 6000, 3500, 1500, 0]
        target_path = [16500, 14850, 13200, 11550, 9900, 8250, 5500, 2750, 0]
        
        fig_netzero = go.Figure()
        fig_netzero.add_trace(go.Scatter(x=years, y=emissions_path, name="Actual/Projected", mode='lines+markers',
                                        line=dict(color=TELIT_GREEN, width=3), fill='tozeroy',
                                        fillcolor='rgba(0, 200, 140, 0.2)'))
        fig_netzero.add_trace(go.Scatter(x=years, y=target_path, name="Target Path", mode='lines',
                                        line=dict(color=TELIT_ORANGE, width=2, dash='dash')))
        fig_netzero.update_layout(height=300, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="tCO₂e")
        st.plotly_chart(fig_netzero, use_container_width=True)

# =============================================================================
# PAGE: RISK & MAINTENANCE (MERGED)
# =============================================================================
elif page == "⚠️ Risk & Maintenance":
    st.markdown(f"""<div class="hero-section">
        <h1 style="margin: 0; color: white;">⚠️ Risk Intelligence & Predictive Maintenance</h1>
        <p style="opacity: 0.8; color: white;">Proactive risk monitoring and AI-powered equipment health management</p>
    </div>""", unsafe_allow_html=True)
    
    # Top KPIs
    kpi_cols = st.columns(8)
    for col, (label, value, delta) in zip(kpi_cols, [
        ("Risk Score", "6.2/10", "-0.4"),
        ("Active Alerts", "5", "-2"),
        ("Equipment", "12", "machines"),
        ("Healthy", "8", "67%"),
        ("Warning", "3", "25%"),
        ("Critical", "1", "AOI-2"),
        ("Uptime", "94.2%", "+1.2%"),
        ("MTBF", "847 hrs", "+12 hrs")
    ]):
        col.metric(label, value, delta)
    
    st.markdown("---")
    
    # Tabbed Interface
    rm_tab1, rm_tab2, rm_tab3, rm_tab4, rm_tab5, rm_tab6, rm_tab7, rm_tab8 = st.tabs([
        "📊 Overview",
        "⚠️ Supply Chain",
        "🌍 Geopolitical",
        "💻 Cyber",
        "🔧 Equipment",
        "📅 Maintenance",
        "📈 Analytics",
        "🤖 AI Insights"
    ])
    
    # =================================================================
    # TAB 1: OVERVIEW
    # =================================================================
    with rm_tab1:
        st.subheader("📊 Risk & Maintenance Overview")
        
        # Overall status
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px; border-left: 5px solid {TELIT_ORANGE};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 20px; font-weight: 700;">⚠️ Overall Status: ELEVATED</div>
                    <div style="color: {TELIT_GRAY}; font-size: 14px;">Geopolitical risks elevated. Equipment health stable. 1 critical maintenance required.</div>
                </div>
                <div style="text-align: right;">
                    <div style="font-size: 48px; font-weight: 700; color: {TELIT_ORANGE};">6.2</div>
                    <div style="color: {TELIT_GRAY}; font-size: 12px;">/10 Risk Score</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Critical alerts
        st.markdown("##### 🚨 Critical Alerts Requiring Attention")
        alerts = [
            ("🔴", "AOI Station 2", "Equipment", "Health at 65.2% - Predicted failure in 5 days", "Maintenance", TELIT_RED),
            ("🔴", "Taiwan Semiconductor", "Geopolitical", "Elevated tensions affecting chip supply", "Monitor", TELIT_RED),
            ("🟡", "JCET Capacity", "Supplier", "Assembly capacity constraints for Q1", "Mitigation", TELIT_ORANGE),
        ]
        for icon, source, category, desc, action, color in alerts:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        padding: 12px 15px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="font-size: 18px;">{icon}</span>
                        <strong style="margin-left: 10px;">{source}</strong>
                        <span style="background: {color}30; padding: 2px 8px; border-radius: 4px; font-size: 10px; margin-left: 10px;">{category}</span>
                    </div>
                    <span style="background: {TELIT_BLUE}30; padding: 3px 10px; border-radius: 4px; font-size: 11px;">Action: {action}</span>
                </div>
                <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 8px; margin-left: 32px;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Summary cards
        st.markdown("---")
        summary_cols = st.columns(4)
        summaries = [
            ("⚠️ Supply Chain Risk", "6.5/10", "3 high-risk suppliers", TELIT_ORANGE),
            ("🌍 Geopolitical Risk", "7.8/10", "APAC region elevated", TELIT_RED),
            ("🔧 Equipment Health", "87.2%", "1 critical, 3 warning", TELIT_BLUE),
            ("📅 Maintenance", "5 due", "1 emergency, 4 scheduled", TELIT_ORANGE),
        ]
        for col, (title, value, detail, color) in zip(summary_cols, summaries):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 18px; text-align: center; border-top: 4px solid {color};">
                <div style="font-size: 13px; font-weight: 600; color: {color};">{title}</div>
                <div style="font-size: 28px; font-weight: 700; margin: 10px 0;">{value}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{detail}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Risk trend
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Risk Score Trend (6 Months)")
            months = ['Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            risk_trend = [5.2, 5.5, 5.8, 6.5, 6.8, 6.2]
            
            fig_risk = go.Figure()
            fig_risk.add_trace(go.Scatter(x=months, y=risk_trend, mode='lines+markers',
                                         line=dict(color=TELIT_ORANGE, width=3), fill='tozeroy',
                                         fillcolor='rgba(255, 165, 0, 0.2)'))
            fig_risk.add_hline(y=5, line_dash="dash", line_color=TELIT_GREEN, annotation_text="Low Risk")
            fig_risk.add_hline(y=7, line_dash="dash", line_color=TELIT_RED, annotation_text="High Risk")
            fig_risk.update_layout(height=260, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Risk Score", yaxis=dict(range=[0, 10]))
            st.plotly_chart(fig_risk, use_container_width=True)
        
        with col2:
            st.markdown("##### 🔧 Equipment Health Distribution")
            health_status = ["🟢 Healthy (>85%)", "🟡 Warning (70-85%)", "🔴 Critical (<70%)"]
            health_counts = [8, 3, 1]
            
            fig_health = go.Figure(go.Pie(
                labels=health_status, values=health_counts, hole=0.6,
                marker_colors=[TELIT_GREEN, TELIT_ORANGE, TELIT_RED]
            ))
            fig_health.add_annotation(text="<b>12</b><br>Machines", x=0.5, y=0.5, font_size=14, showarrow=False)
            fig_health.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10))
            st.plotly_chart(fig_health, use_container_width=True)
    
    # =================================================================
    # TAB 2: SUPPLY CHAIN RISK
    # =================================================================
    with rm_tab2:
        st.subheader("⚠️ Supply Chain Risk Assessment")
        
        # Risk KPIs
        sc_kpis = st.columns(5)
        sc_kpis[0].metric("Overall SC Risk", "6.5/10", "+0.3")
        sc_kpis[1].metric("Single Source", "3", "Components")
        sc_kpis[2].metric("High Risk Suppliers", "2", "-1")
        sc_kpis[3].metric("Lead Time Risk", "Medium", "Chipsets")
        sc_kpis[4].metric("Inventory Buffer", "18.5 days", "+2.1")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Risk by Category")
            categories = ["Single Source", "Lead Time", "Quality", "Financial", "Capacity", "Logistics"]
            scores = [8.2, 7.5, 4.5, 5.8, 6.2, 5.5]
            
            fig_cat = go.Figure(go.Bar(
                x=scores, y=categories, orientation='h',
                marker_color=[TELIT_RED if s > 7 else TELIT_ORANGE if s > 5 else TELIT_GREEN for s in scores],
                text=[f"{s}/10" for s in scores], textposition="outside"
            ))
            fig_cat.add_vline(x=7, line_dash="dash", line_color="red", annotation_text="High")
            fig_cat.add_vline(x=5, line_dash="dash", line_color="orange", annotation_text="Medium")
            fig_cat.update_layout(height=280, margin=dict(l=10, r=60, t=10, b=10), xaxis=dict(range=[0, 10]))
            st.plotly_chart(fig_cat, use_container_width=True)
        
        with col2:
            st.markdown("##### 🏢 Supplier Risk Ranking")
            supplier_risk = pd.DataFrame({
                "Supplier": ["Qualcomm", "JCET", "u-blox", "Samsung", "Murata"],
                "Risk Score": ["7.2", "6.8", "4.5", "4.2", "3.8"],
                "Risk Factors": ["Single source, lead time", "Capacity, quality", "Lead time", "Low risk", "Low risk"],
                "Mitigation": ["Safety stock, alt qual", "Capacity review", "Monitor", "None needed", "None needed"],
                "Status": ["🔴 High", "🟡 Medium", "🟡 Medium", "🟢 Low", "🟢 Low"]
            })
            st.dataframe(supplier_risk, use_container_width=True)
        
        # Single source components
        st.markdown("---")
        st.markdown("##### 🔴 Single Source Components (Critical)")
        single_source = pd.DataFrame({
            "Component": ["Qualcomm SDX55", "Qualcomm SDX62", "u-blox M10"],
            "Supplier": ["Qualcomm", "Qualcomm", "u-blox"],
            "Products Affected": ["ME310G1, FN920A", "FN990A28", "SE868K3"],
            "Annual Spend": ["$4.2M", "$1.8M", "$1.5M"],
            "Risk Score": ["8.5", "8.2", "6.5"],
            "Mitigation Status": ["🔵 Alt under qualification", "🔵 Evaluating MediaTek", "🟢 Dual source planned"],
            "Buffer Stock": ["12 weeks", "8 weeks", "6 weeks"]
        })
        st.dataframe(single_source, use_container_width=True)
    
    # =================================================================
    # TAB 3: GEOPOLITICAL RISK
    # =================================================================
    with rm_tab3:
        st.subheader("🌍 Geopolitical Risk Monitor")
        
        # Geopolitical KPIs
        geo_kpis = st.columns(5)
        geo_kpis[0].metric("Overall Geo Risk", "7.8/10", "+0.5")
        geo_kpis[1].metric("APAC Risk", "8.2/10", "Elevated")
        geo_kpis[2].metric("EMEA Risk", "5.5/10", "Moderate")
        geo_kpis[3].metric("Americas Risk", "4.2/10", "Low")
        geo_kpis[4].metric("Active Alerts", "3", "+1")
        
        st.markdown("---")
        
        # Active geopolitical risks
        st.markdown("##### 🚨 Active Geopolitical Alerts")
        geo_alerts = [
            ("🔴 Critical", "Taiwan Strait Tensions", "Semiconductor supply at risk if tensions escalate. Qualcomm, TSMC exposure.", "Increased safety stock to 16 weeks. Alternate supplier qualification accelerated.", TELIT_RED),
            ("🟡 Elevated", "US-China Trade", "Potential new export controls on advanced chips. Monitoring CHIPS Act implementation.", "Compliance review complete. No immediate action required.", TELIT_ORANGE),
            ("🟡 Elevated", "Red Sea Shipping", "Suez Canal disruption adding 7-10 days to APAC-EU shipments.", "Air freight contingency for critical shipments. Route diversification.", TELIT_ORANGE),
        ]
        
        for level, title, desc, mitigation, color in geo_alerts:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; margin-bottom: 12px; border-left: 4px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <span style="background: {color}30; padding: 2px 8px; border-radius: 4px; font-size: 11px; color: {color};">{level}</span>
                        <strong style="margin-left: 10px; font-size: 15px;">{title}</strong>
                        <div style="font-size: 12px; color: {TELIT_GRAY}; margin-top: 8px;">{desc}</div>
                        <div style="font-size: 11px; color: {TELIT_BLUE}; margin-top: 8px;"><strong>Mitigation:</strong> {mitigation}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Regional risk map
        st.markdown("---")
        st.markdown("##### 🗺️ Regional Risk Assessment")
        region_cols = st.columns(3)
        regions = [
            ("🌏 Asia-Pacific", "8.2/10", "Elevated", ["Taiwan tensions", "China trade policy", "Component concentration"], TELIT_RED),
            ("🌍 EMEA", "5.5/10", "Moderate", ["Red Sea shipping", "EU regulations", "Energy prices"], TELIT_ORANGE),
            ("🌎 Americas", "4.2/10", "Low", ["CHIPS Act positive", "Stable trade", "Reshoring benefits"], TELIT_GREEN),
        ]
        for col, (region, score, level, factors, color) in zip(region_cols, regions):
            factors_html = "".join([f"<div style='font-size: 10px; margin: 2px 0;'>• {f}</div>" for f in factors])
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 18px; border-top: 4px solid {color};">
                <div style="font-size: 16px; font-weight: 700; color: {color};">{region}</div>
                <div style="font-size: 28px; font-weight: 700; margin: 10px 0;">{score}</div>
                <div style="font-size: 12px; margin-bottom: 10px;">Status: <strong>{level}</strong></div>
                <div style="font-size: 11px; font-weight: 600;">Risk Factors:</div>
                {factors_html}
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 4: CYBER RISK
    # =================================================================
    with rm_tab4:
        st.subheader("💻 Cybersecurity Risk Management")
        
        # Cyber KPIs
        cyber_kpis = st.columns(5)
        cyber_kpis[0].metric("Security Score", "B+", "—")
        cyber_kpis[1].metric("Threats Blocked", "12,450", "This month")
        cyber_kpis[2].metric("Vulnerabilities", "3", "Open")
        cyber_kpis[3].metric("Patch Compliance", "98.5%", "+1.2%")
        cyber_kpis[4].metric("Last Incident", "0 days", "None active")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 🛡️ Security Posture by Domain")
            domains = ["Network Security", "Endpoint Protection", "Data Security", "Access Control", "Vendor Security", "Incident Response"]
            scores = [92, 88, 95, 90, 78, 85]
            
            fig_cyber = go.Figure(go.Bar(
                x=domains, y=scores,
                marker_color=[TELIT_GREEN if s >= 85 else TELIT_ORANGE if s >= 75 else TELIT_RED for s in scores],
                text=[f"{s}%" for s in scores], textposition="outside"
            ))
            fig_cyber.add_hline(y=85, line_dash="dash", line_color="green", annotation_text="Target")
            fig_cyber.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=80), yaxis_title="Score %", xaxis_tickangle=-30)
            st.plotly_chart(fig_cyber, use_container_width=True)
        
        with col2:
            st.markdown("##### ⚠️ Open Vulnerabilities")
            vulns = pd.DataFrame({
                "ID": ["CVE-2024-1234", "CVE-2024-5678", "CVE-2024-9012"],
                "System": ["ERP Server", "VPN Gateway", "IoT Devices"],
                "Severity": ["🟡 Medium", "🟡 Medium", "🟢 Low"],
                "CVSS": ["6.5", "5.8", "3.2"],
                "Status": ["Patching scheduled", "Workaround applied", "Assessment"],
                "Due Date": ["Dec 30", "Jan 5", "Jan 15"]
            })
            st.dataframe(vulns, use_container_width=True)
        
        # Threat intelligence
        st.markdown("---")
        st.markdown("##### 🔍 Threat Intelligence")
        threat_cols = st.columns(4)
        threats = [
            ("🎣 Phishing Attempts", "245", "Blocked this month", TELIT_ORANGE),
            ("🔒 Ransomware Campaigns", "3", "Industry targeting", TELIT_RED),
            ("🌐 DDoS Attempts", "12", "Mitigated", TELIT_GREEN),
            ("🕵️ Supply Chain Attacks", "1", "Under monitoring", TELIT_ORANGE),
        ]
        for col, (threat, count, detail, color) in zip(threat_cols, threats):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 600;">{threat}</div>
                <div style="font-size: 26px; font-weight: 700; color: {color}; margin: 8px 0;">{count}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{detail}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 5: EQUIPMENT HEALTH
    # =================================================================
    with rm_tab5:
        st.subheader("🔧 Equipment Health Monitoring")
        
        # Equipment KPIs
        eq_kpis = st.columns(5)
        eq_kpis[0].metric("Avg Health", "87.2%", "+1.5%")
        eq_kpis[1].metric("Healthy", "8/12", "67%")
        eq_kpis[2].metric("Warning", "3/12", "25%")
        eq_kpis[3].metric("Critical", "1/12", "8%")
        eq_kpis[4].metric("OEE", "82.5%", "+2.3%")
        
        st.markdown("---")
        
        # Equipment health status
        st.markdown("##### 📊 Equipment Health Status")
        equipment_data = pd.DataFrame({
            "Equipment": ["SMT Line 1", "SMT Line 2", "Reflow Oven 1", "Reflow Oven 2", "AOI Station 1", "AOI Station 2", "Wire Bonder", "Functional Tester", "RF Tester", "Flying Probe", "Packaging Line", "Labeling System"],
            "Health %": [92.5, 78.3, 95.1, 91.2, 88.7, 65.2, 82.5, 94.8, 89.2, 91.5, 97.2, 93.8],
            "Status": ["🟢 Good", "🟡 Warning", "🟢 Good", "🟢 Good", "🟢 Good", "🔴 Critical", "🟡 Warning", "🟢 Good", "🟢 Good", "🟢 Good", "🟢 Good", "🟢 Good"],
            "RUL (hrs)": ["2,850", "980", "4,200", "2,100", "1,850", "120", "650", "3,100", "2,400", "2,800", "5,200", "3,400"],
            "Last Maint": ["Dec 15", "Dec 10", "Nov 28", "Dec 18", "Dec 5", "Nov 15", "Dec 8", "Dec 20", "Dec 12", "Dec 22", "Nov 30", "Dec 18"],
            "Next Maint": ["Jan 15", "Dec 28", "Jan 28", "Jan 18", "Jan 5", "NOW", "Dec 30", "Jan 20", "Jan 12", "Jan 22", "Jan 30", "Jan 18"]
        })
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig_eq = go.Figure(go.Bar(
                x=equipment_data["Health %"], y=equipment_data["Equipment"], orientation='h',
                marker_color=[TELIT_GREEN if h >= 85 else TELIT_ORANGE if h >= 70 else TELIT_RED for h in equipment_data["Health %"]],
                text=[f"{h}%" for h in equipment_data["Health %"]], textposition="outside"
            ))
            fig_eq.add_vline(x=85, line_dash="dash", line_color="green", annotation_text="Healthy")
            fig_eq.add_vline(x=70, line_dash="dash", line_color="orange", annotation_text="Warning")
            fig_eq.update_layout(height=450, margin=dict(l=10, r=60, t=10, b=10), xaxis=dict(range=[0, 105]))
            st.plotly_chart(fig_eq, use_container_width=True)
        
        with col2:
            st.markdown("##### ⚠️ Attention Required")
            for _, row in equipment_data[equipment_data["Health %"] < 85].iterrows():
                color = TELIT_RED if row["Health %"] < 70 else TELIT_ORANGE
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {color}15, {color}05);
                            padding: 12px; margin: 8px 0; border-radius: 8px; border-left: 4px solid {color};">
                    <strong>{row['Equipment']}</strong>
                    <div style="font-size: 12px; color: {TELIT_GRAY};">Health: {row['Health %']}%</div>
                    <div style="font-size: 11px; color: {color};">RUL: {row['RUL (hrs)']} hrs</div>
                    <div style="font-size: 11px;">Next: {row['Next Maint']}</div>
                </div>
                """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 6: MAINTENANCE SCHEDULE
    # =================================================================
    with rm_tab6:
        st.subheader("📅 Maintenance Management")
        
        # Maintenance KPIs
        maint_kpis = st.columns(5)
        maint_kpis[0].metric("Scheduled", "8", "Next 30 days")
        maint_kpis[1].metric("Overdue", "1", "⚠️ AOI-2")
        maint_kpis[2].metric("Completed MTD", "12", "+3")
        maint_kpis[3].metric("Planned vs Unplanned", "85/15%", "+5%")
        maint_kpis[4].metric("MTTR", "2.3 hrs", "-0.4 hrs")
        
        st.markdown("---")
        
        # Maintenance schedule
        st.markdown("##### 📅 Upcoming Maintenance Schedule")
        schedule = pd.DataFrame({
            "Equipment": ["AOI Station 2", "SMT Line 2", "Wire Bonder", "Reflow Oven 1", "RF Tester", "Packaging Line", "SMT Line 1", "Functional Tester"],
            "Type": ["🔴 Emergency", "🟡 Preventive", "🟡 Preventive", "🟢 Scheduled", "🟢 Scheduled", "🟢 Scheduled", "🟢 Scheduled", "🟢 Scheduled"],
            "Priority": ["Critical", "High", "High", "Medium", "Medium", "Low", "Medium", "Low"],
            "Due Date": ["OVERDUE", "Dec 28", "Dec 30", "Jan 5", "Jan 12", "Jan 15", "Jan 15", "Jan 20"],
            "Duration": ["4 hrs", "2 hrs", "3 hrs", "1 hr", "2 hrs", "1 hr", "2 hrs", "30 min"],
            "Technician": ["Assigned", "Pending", "Pending", "Scheduled", "Scheduled", "Scheduled", "Scheduled", "Scheduled"],
            "Parts Required": ["CAM-AOI-V3", "Conveyor belt", "Wire spools", "Filters", "RF cables", "Sensors", "Nozzles", "Probes"],
            "Cost Est.": ["$3,200", "$850", "$1,200", "$450", "$680", "$320", "$1,100", "$280"]
        })
        st.dataframe(schedule, use_container_width=True)
        
        # Maintenance calendar view
        st.markdown("---")
        st.markdown("##### 📆 30-Day Maintenance Calendar")
        cal_cols = st.columns(4)
        weeks = [
            ("Week 1 (Dec 23-29)", [("Dec 28", "SMT Line 2", "Preventive", TELIT_ORANGE)]),
            ("Week 2 (Dec 30-Jan 5)", [("Dec 30", "Wire Bonder", "Preventive", TELIT_ORANGE), ("Jan 5", "Reflow Oven 1", "Scheduled", TELIT_GREEN)]),
            ("Week 3 (Jan 6-12)", [("Jan 12", "RF Tester", "Scheduled", TELIT_GREEN)]),
            ("Week 4 (Jan 13-19)", [("Jan 15", "SMT Line 1", "Scheduled", TELIT_GREEN), ("Jan 15", "Packaging", "Scheduled", TELIT_GREEN)]),
        ]
        for col, (week, events) in zip(cal_cols, weeks):
            events_html = "".join([f"<div style='background: {color}20; padding: 5px; margin: 3px 0; border-radius: 4px; font-size: 10px;'>{date}: {eq}</div>" for date, eq, typ, color in events])
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);
                        border-radius: 10px; padding: 12px; min-height: 120px;">
                <div style="font-size: 11px; font-weight: 600; margin-bottom: 8px;">{week}</div>
                {events_html if events_html else '<div style="font-size: 10px; color: #888;">No maintenance</div>'}
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 7: ANALYTICS
    # =================================================================
    with rm_tab7:
        st.subheader("📈 Risk & Maintenance Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📊 Risk Score Trend (12 Months)")
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            risk_scores = [4.5, 4.8, 5.0, 5.2, 5.0, 4.8, 5.2, 5.5, 5.8, 6.5, 6.8, 6.2]
            
            fig_risk_trend = go.Figure()
            fig_risk_trend.add_trace(go.Scatter(x=months, y=risk_scores, mode='lines+markers',
                                               line=dict(color=TELIT_ORANGE, width=3)))
            fig_risk_trend.add_hline(y=5, line_dash="dash", line_color=TELIT_GREEN, annotation_text="Low")
            fig_risk_trend.add_hline(y=7, line_dash="dash", line_color=TELIT_RED, annotation_text="High")
            fig_risk_trend.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Risk Score", yaxis=dict(range=[0, 10]))
            st.plotly_chart(fig_risk_trend, use_container_width=True)
        
        with col2:
            st.markdown("##### 🔧 Equipment Uptime Trend")
            uptime = [92.5, 93.2, 91.8, 94.5, 93.8, 94.2, 93.5, 94.8, 92.8, 93.5, 94.0, 94.2]
            
            fig_uptime = go.Figure()
            fig_uptime.add_trace(go.Scatter(x=months, y=uptime, mode='lines+markers',
                                           line=dict(color=TELIT_GREEN, width=3), fill='tozeroy',
                                           fillcolor='rgba(0, 200, 140, 0.2)'))
            fig_uptime.add_hline(y=95, line_dash="dash", line_color=TELIT_BLUE, annotation_text="Target: 95%")
            fig_uptime.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), yaxis_title="Uptime %", yaxis=dict(range=[88, 100]))
            st.plotly_chart(fig_uptime, use_container_width=True)
        
        # Maintenance metrics
        st.markdown("---")
        st.markdown("##### 📊 Maintenance Performance")
        perf_cols = st.columns(4)
        perf_data = [
            ("MTBF", "847 hrs", "+12 hrs", "Mean Time Between Failures", TELIT_GREEN),
            ("MTTR", "2.3 hrs", "-0.4 hrs", "Mean Time To Repair", TELIT_GREEN),
            ("OEE", "82.5%", "+2.3%", "Overall Equipment Effectiveness", TELIT_BLUE),
            ("PM Compliance", "94%", "+3%", "Preventive Maintenance", TELIT_GREEN),
        ]
        for col, (metric, value, change, desc, color) in zip(perf_cols, perf_data):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; color: {TELIT_GRAY};">{metric}</div>
                <div style="font-size: 26px; font-weight: 700; color: {color}; margin: 5px 0;">{value}</div>
                <div style="font-size: 12px; color: {TELIT_GREEN};">{change}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 8: AI INSIGHTS
    # =================================================================
    with rm_tab8:
        st.subheader("🤖 AI-Powered Risk & Maintenance Insights")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🧠</span>
                <div>
                    <div style="font-size: 22px; font-weight: 700; color: white;">Predictive Intelligence Engine</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">ML-powered failure prediction and risk forecasting</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # AI Insights
        st.markdown("##### 💡 AI Recommendations")
        insights = [
            ("🚨", "AOI Station 2 - Urgent", "92% probability of camera failure within 5 days. Preventive replacement cost: $3,200. Unplanned failure cost: $45,000.", TELIT_RED, "Critical"),
            ("⚠️", "SMT Line 2 - Watch", "Conveyor belt wear detected. Recommend replacement during scheduled maintenance Dec 28.", TELIT_ORANGE, "High"),
            ("📊", "Taiwan Risk Elevated", "ML model predicts 35% probability of supply disruption in Q1. Recommend increasing buffer stock.", TELIT_ORANGE, "Monitor"),
            ("🔧", "Wire Bonder Optimization", "AI analysis shows 12% throughput improvement possible with parameter adjustment.", TELIT_GREEN, "Opportunity"),
            ("💡", "Preventive Schedule", "Optimized PM schedule could reduce unplanned downtime by 22% and save $85K annually.", TELIT_GREEN, "Opportunity"),
        ]
        
        for icon, title, desc, color, priority in insights:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; margin-bottom: 12px; border-left: 4px solid {color};">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <span style="font-size: 20px; margin-right: 10px;">{icon}</span>
                        <strong style="font-size: 15px;">{title}</strong>
                        <div style="font-size: 13px; color: {TELIT_GRAY}; margin-top: 8px; margin-left: 32px;">{desc}</div>
                    </div>
                    <span style="background: {color}30; color: {color}; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: 600;">{priority}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Failure prediction
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("##### 📈 Equipment Failure Probability (Next 30 Days)")
            days = list(range(1, 31))
            aoi2_prob = [0.15 + i*0.027 for i in range(30)]
            smt2_prob = [0.05 + i*0.008 for i in range(30)]
            bonder_prob = [0.08 + i*0.012 for i in range(30)]
            
            fig_prob = go.Figure()
            fig_prob.add_trace(go.Scatter(x=days, y=aoi2_prob, name="AOI Station 2", line=dict(color=TELIT_RED, width=2)))
            fig_prob.add_trace(go.Scatter(x=days, y=smt2_prob, name="SMT Line 2", line=dict(color=TELIT_ORANGE, width=2)))
            fig_prob.add_trace(go.Scatter(x=days, y=bonder_prob, name="Wire Bonder", line=dict(color=TELIT_BLUE, width=2)))
            fig_prob.add_hline(y=0.5, line_dash="dash", line_color="red", annotation_text="High Risk (50%)")
            fig_prob.update_layout(height=280, margin=dict(l=20, r=20, t=10, b=40), xaxis_title="Days", yaxis_title="Failure Probability")
            st.plotly_chart(fig_prob, use_container_width=True)
        
        with col2:
            st.markdown("##### 🎯 Recommended Actions")
            actions = pd.DataFrame({
                "Priority": ["1", "2", "3", "4", "5"],
                "Action": ["Replace AOI-2 camera", "SMT-2 conveyor belt", "Increase Taiwan buffer", "Wire bonder calibration", "Optimize PM schedule"],
                "Impact": ["Avoid $45K loss", "Prevent downtime", "Risk mitigation", "+12% throughput", "$85K savings/yr"],
                "Effort": ["4 hours", "2 hours", "Procurement", "1 hour", "Analysis"],
                "Due": ["Dec 26", "Dec 28", "Jan 5", "Dec 30", "Jan 15"]
            })
            st.dataframe(actions, use_container_width=True)

# =============================================================================
# PAGE: ARCHITECTURE
# =============================================================================
elif page == "🏗️ Architecture":
    st.markdown(f"""<div class="hero-section" style="background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);">
        <h1 style="margin: 0; color: white;">🏗️ Technical Architecture</h1>
        <p style="opacity: 0.9; color: white;">Complete implementation blueprint for Telit Supply Chain Intelligence Platform</p>
    </div>""", unsafe_allow_html=True)
    
    # Top Stats
    arch_stats = st.columns(8)
    for col, (label, value) in zip(arch_stats, [
        ("Dashboards", "17"),
        ("Data Sources", "18"),
        ("Tables", "85+"),
        ("ML Models", "12"),
        ("Pipelines", "24"),
        ("APIs", "10"),
        ("Users", "500+"),
        ("Uptime SLA", "99.9%")
    ]):
        col.metric(label, value)
    
    st.markdown("---")
    
    # Tabbed Interface
    arch_tab1, arch_tab2, arch_tab3, arch_tab4, arch_tab5, arch_tab6, arch_tab7, arch_tab8, arch_tab9, arch_tab10 = st.tabs([
        "🏛️ Overview",
        "🗄️ Data Sources",
        "📐 Data Model",
        "🔄 ETL/Pipelines",
        "❄️ Snowflake",
        "🤖 ML/Analytics",
        "🖥️ Infrastructure",
        "🔌 Integrations",
        "📁 Code Structure",
        "🔐 Governance"
    ])
    
    # =================================================================
    # TAB 1: ARCHITECTURE OVERVIEW
    # =================================================================
    with arch_tab1:
        st.subheader("🏛️ High-Level Architecture")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_DARK}10); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="font-size: 18px; font-weight: 700;">📋 Architecture Overview</div>
            <div style="color: {TELIT_GRAY}; font-size: 14px; margin-top: 10px;">
                Modern cloud-native data platform built on Snowflake, leveraging Snowflake Native Apps and Streamlit for 
                real-time supply chain visibility, predictive analytics, and AI-powered decision support.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # High-level architecture diagram
        st.markdown("##### 🏗️ System Architecture Diagram")
        
        arch_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            edge [fontname="Arial", fontsize=9];
            
            subgraph cluster_sources {
                label="Data Sources";
                style=filled;
                color="#e3f2fd";
                
                SAP [label="SAP ERP\\n(Orders, Inventory)", fillcolor="#ff9800"];
                MES [label="MES\\n(Production Data)", fillcolor="#ff9800"];
                IoT [label="IoT Sensors\\n(Equipment, Environment)", fillcolor="#4caf50"];
                APIs [label="External APIs\\n(Weather, Shipping)", fillcolor="#2196f3"];
                Files [label="Files\\n(Excel, CSV)", fillcolor="#9c27b0"];
                EDI [label="EDI\\n(Customer Orders)", fillcolor="#f44336"];
            }
            
            subgraph cluster_ingestion {
                label="Ingestion Layer";
                style=filled;
                color="#fff3e0";
                
                Snowpipe [label="Snowpipe\\n(Streaming)", fillcolor="#00bcd4"];
                Kafka [label="Kafka Connect\\n(Real-time)", fillcolor="#00bcd4"];
                Fivetran [label="Fivetran\\n(Batch)", fillcolor="#00bcd4"];
            }
            
            subgraph cluster_snowflake {
                label="Snowflake Data Cloud";
                style=filled;
                color="#e8f5e9";
                
                subgraph cluster_storage {
                    label="Storage Layer";
                    Raw [label="RAW\\n(Landing Zone)", fillcolor="#90caf9"];
                    Staging [label="STAGING\\n(Cleansed)", fillcolor="#90caf9"];
                    Curated [label="CURATED\\n(Business Ready)", fillcolor="#90caf9"];
                    Mart [label="DATA MARTS\\n(Analytics)", fillcolor="#64b5f6"];
                }
                
                subgraph cluster_compute {
                    label="Compute Layer";
                    DynamicTables [label="Dynamic Tables\\n(Transformations)", fillcolor="#a5d6a7"];
                    Snowpark [label="Snowpark\\n(Python/ML)", fillcolor="#a5d6a7"];
                    Cortex [label="Cortex AI\\n(LLM/ML)", fillcolor="#ce93d8"];
                    Tasks [label="Tasks\\n(Orchestration)", fillcolor="#a5d6a7"];
                }
            }
            
            subgraph cluster_app {
                label="Application Layer";
                style=filled;
                color="#fce4ec";
                
                Streamlit [label="Streamlit\\n(Dashboards)", fillcolor="#f48fb1"];
                NativeApp [label="Native App\\n(Marketplace)", fillcolor="#f48fb1"];
                API [label="REST API\\n(External)", fillcolor="#f48fb1"];
            }
            
            subgraph cluster_users {
                label="Users";
                style=filled;
                color="#f3e5f5";
                
                Exec [label="Executives", fillcolor="#e1bee7"];
                Ops [label="Operations", fillcolor="#e1bee7"];
                Analysts [label="Analysts", fillcolor="#e1bee7"];
                External [label="Partners", fillcolor="#e1bee7"];
            }
            
            SAP -> Fivetran;
            MES -> Kafka;
            IoT -> Snowpipe;
            APIs -> Snowpipe;
            Files -> Fivetran;
            EDI -> Kafka;
            
            Snowpipe -> Raw;
            Kafka -> Raw;
            Fivetran -> Raw;
            
            Raw -> Staging [label="Cleanse"];
            Staging -> Curated [label="Transform"];
            Curated -> Mart [label="Aggregate"];
            
            Staging -> DynamicTables;
            DynamicTables -> Curated;
            
            Curated -> Snowpark;
            Snowpark -> Cortex;
            Cortex -> Mart;
            
            Tasks -> DynamicTables [style=dashed];
            
            Mart -> Streamlit;
            Mart -> NativeApp;
            Mart -> API;
            
            Streamlit -> Exec;
            Streamlit -> Ops;
            Streamlit -> Analysts;
            API -> External;
        }
        """
        st.graphviz_chart(arch_diagram, use_container_width=True)
        
        # Key components
        st.markdown("---")
        st.markdown("##### 🧩 Key Components")
        comp_cols = st.columns(4)
        components = [
            ("🗄️ Data Platform", "Snowflake", "Enterprise data warehouse with native streaming, ML, and app hosting", TELIT_BLUE),
            ("📊 Visualization", "Streamlit", "Python-based interactive dashboards with native Snowflake integration", TELIT_GREEN),
            ("🤖 AI/ML", "Cortex AI", "LLM-powered insights, forecasting, and anomaly detection", '#ce93d8'),
            ("🔄 Orchestration", "Tasks + dbt", "Automated data pipelines with dependency management", TELIT_ORANGE),
        ]
        for col, (title, tech, desc, color) in zip(comp_cols, components):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 12px; padding: 18px; border-top: 4px solid {color}; height: 160px;">
                <div style="font-size: 14px; font-weight: 700; color: {color};">{title}</div>
                <div style="font-size: 20px; font-weight: 700; margin: 8px 0;">{tech}</div>
                <div style="font-size: 11px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Tech stack summary
        st.markdown("---")
        st.markdown("##### 🛠️ Technology Stack")
        stack_data = pd.DataFrame({
            "Layer": ["Data Platform", "Data Platform", "Ingestion", "Ingestion", "Transformation", "ML/AI", "Application", "DevOps", "Monitoring"],
            "Technology": ["Snowflake", "Snowflake Cortex", "Snowpipe", "Fivetran", "dbt + Dynamic Tables", "Snowpark ML + Cortex", "Streamlit", "GitHub Actions + Terraform", "Snowflake Query History + Datadog"],
            "Purpose": ["Data warehouse, compute, storage", "LLM and ML functions", "Real-time streaming ingestion", "Batch ETL for SAP/ERP", "Data transformation & modeling", "Predictive analytics", "Interactive dashboards", "CI/CD and IaC", "Performance & usage monitoring"],
            "License": ["Enterprise", "Included", "Included", "Paid", "Open Source + Included", "Included", "Included", "Free + Paid", "Paid"]
        })
        st.dataframe(stack_data, use_container_width=True)
    
    # =================================================================
    # TAB 2: DATA SOURCES
    # =================================================================
    with arch_tab2:
        st.subheader("🗄️ Data Sources & Connections")
        
        # Data source diagram
        st.markdown("##### 📊 Data Source Landscape")
        
        source_diagram = """
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            subgraph cluster_erp {
                label="ERP Systems";
                style=filled;
                color="#fff3e0";
                
                SAP [label="SAP S/4HANA\\nOrders, Inventory, Finance", fillcolor="#ff9800"];
                Oracle [label="Oracle EBS\\n(Legacy)", fillcolor="#ff9800"];
            }
            
            subgraph cluster_ops {
                label="Operations";
                style=filled;
                color="#e8f5e9";
                
                MES [label="MES\\nProduction, Quality", fillcolor="#4caf50"];
                SCADA [label="SCADA\\nEquipment Sensors", fillcolor="#4caf50"];
                WMS [label="WMS\\nWarehouse Ops", fillcolor="#4caf50"];
            }
            
            subgraph cluster_iot {
                label="IoT & Sensors";
                style=filled;
                color="#e3f2fd";
                
                Telit [label="Telit IoT\\ndeviceWISE", fillcolor="#2196f3"];
                MQTT [label="MQTT\\nSensor Data", fillcolor="#2196f3"];
            }
            
            subgraph cluster_external {
                label="External APIs";
                style=filled;
                color="#fce4ec";
                
                Weather [label="Weather API\\nOpenWeather", fillcolor="#f48fb1"];
                Shipping [label="Shipping APIs\\nDHL, FedEx", fillcolor="#f48fb1"];
                Market [label="Market Data\\nBloomberg", fillcolor="#f48fb1"];
            }
            
            subgraph cluster_files {
                label="File Sources";
                style=filled;
                color="#f3e5f5";
                
                Excel [label="Excel/CSV\\nForecasts, Plans", fillcolor="#9c27b0"];
                EDI [label="EDI X12\\nCustomer Orders", fillcolor="#9c27b0"];
            }
            
            Snowflake [label="Snowflake\\nData Cloud", shape=cylinder, fillcolor="#29b5e8", fontcolor=white];
            
            SAP -> Snowflake [label="Fivetran"];
            Oracle -> Snowflake [label="Fivetran"];
            MES -> Snowflake [label="Kafka"];
            SCADA -> Snowflake [label="Snowpipe"];
            WMS -> Snowflake [label="Kafka"];
            Telit -> Snowflake [label="REST API"];
            MQTT -> Snowflake [label="Snowpipe"];
            Weather -> Snowflake [label="Snowpipe"];
            Shipping -> Snowflake [label="REST API"];
            Market -> Snowflake [label="Marketplace"];
            Excel -> Snowflake [label="Stage"];
            EDI -> Snowflake [label="Snowpipe"];
        }
        """
        st.graphviz_chart(source_diagram, use_container_width=True)
        
        # Data source details
        st.markdown("---")
        st.markdown("##### 📋 Data Source Specifications")
        
        sources = pd.DataFrame({
            "Source": ["SAP S/4HANA", "SAP MM/PP", "MES (Camstar)", "PLM (Teamcenter)", "Salesforce CRM", "IoT Sensors", "WMS", "Carrier Cert Portal", "DHL/FedEx APIs", "EDI X12", "Customer Hub Files", "CM Portal (Foxconn)", "CM Portal (Flex)", "Financial System", "Carbon Tracking", "Quality LIMS", "RMA System", "Market Data"],
            "Type": ["ERP - SD", "ERP - Ops", "Manufacturing", "Engineering", "CRM", "IoT", "Warehouse", "Certification", "Logistics", "B2B", "Files", "CM", "CM", "Finance", "ESG", "Quality", "Service", "Marketplace"],
            "Connection": ["Fivetran SAP", "Fivetran SAP", "Kafka Connect", "REST API", "Fivetran", "Snowpipe + MQTT", "Kafka Connect", "REST API", "REST API", "Snowpipe", "Internal Stage", "SFTP + Snowpipe", "SFTP + Snowpipe", "Fivetran", "REST API", "Kafka", "REST API", "Data Share"],
            "Frequency": ["15 min", "15 min", "Real-time", "Hourly", "30 min", "1 sec", "5 min", "Daily", "On-event", "Real-time", "Daily", "Hourly", "Hourly", "Daily", "Weekly", "Real-time", "Real-time", "Daily"],
            "Volume/Day": ["~2M rows", "~1.5M rows", "~5M rows", "~50K rows", "~200K rows", "~50M events", "~500K rows", "~5K records", "~100K records", "~50K orders", "Variable", "~300K rows", "~250K rows", "~100K rows", "~10K records", "~200K tests", "~5K tickets", "~1M records"],
            "Format": ["OData/BAPI", "OData/BAPI", "JSON", "REST/JSON", "REST", "MQTT/JSON", "JSON", "JSON/XML", "JSON/XML", "X12 850/856", "CSV/XLSX", "CSV/JSON", "CSV/JSON", "JSON", "JSON", "JSON", "JSON", "Parquet"],
            "Owner": ["IT - ERP", "IT - ERP", "IT - MES", "Engineering", "IT - CRM", "IoT Team", "Logistics", "Quality", "Logistics", "EDI Team", "Planning", "CM Mgmt", "CM Mgmt", "Finance IT", "ESG Team", "Quality", "Service", "Data Eng"]
        })
        st.dataframe(sources, use_container_width=True)
        
        # Connection status
        st.markdown("---")
        st.markdown("##### 🔌 Connection Status")
        conn_cols = st.columns(4)
        connections = [
            ("SAP S/4HANA", "🟢 Connected", "Last sync: 5 min ago", "Fivetran", TELIT_GREEN),
            ("MES Kafka", "🟢 Streaming", "Lag: 2.3 sec", "Confluent", TELIT_GREEN),
            ("IoT Snowpipe", "🟢 Active", "95K events/min", "Snowpipe", TELIT_GREEN),
            ("Weather API", "🟢 Healthy", "Rate: 1K req/hr", "REST", TELIT_GREEN),
        ]
        for col, (source, status, detail, connector, color) in zip(conn_cols, connections):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {color};">
                <div style="font-size: 13px; font-weight: 600;">{source}</div>
                <div style="font-size: 16px; font-weight: 700; color: {color}; margin: 5px 0;">{status}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">{detail}</div>
                <div style="font-size: 10px; color: {TELIT_BLUE};">via {connector}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 3: DATA MODEL
    # =================================================================
    with arch_tab3:
        st.subheader("📐 Data Model & Schema")
        
        # Data model diagram
        st.markdown("##### 📊 Entity Relationship Diagram")
        
        erd_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=record, style="filled", fontname="Arial", fontsize=9];
            edge [fontname="Arial", fontsize=8];
            
            subgraph cluster_dim {
                label="Dimension Tables";
                style=filled;
                color="#e3f2fd";
                
                DIM_PRODUCT [label="{DIM_PRODUCT|product_key PK\\lproduct_id\\lproduct_name\\lfamily\\lsku\\lbom_id FK\\l}", fillcolor="#90caf9"];
                DIM_SUPPLIER [label="{DIM_SUPPLIER|supplier_key PK\\lsupplier_id\\lsupplier_name\\lregion\\ltier\\lrisk_score\\l}", fillcolor="#90caf9"];
                DIM_CUSTOMER [label="{DIM_CUSTOMER|customer_key PK\\lcustomer_id\\lcustomer_name\\lsegment\\lregion\\l}", fillcolor="#90caf9"];
                DIM_LOCATION [label="{DIM_LOCATION|location_key PK\\llocation_id\\lfacility_name\\lcountry\\ltype\\l}", fillcolor="#90caf9"];
                DIM_DATE [label="{DIM_DATE|date_key PK\\lfull_date\\lyear\\lquarter\\lmonth\\lweek\\l}", fillcolor="#90caf9"];
                DIM_EQUIPMENT [label="{DIM_EQUIPMENT|equipment_key PK\\lequipment_id\\lname\\ltype\\lline\\l}", fillcolor="#90caf9"];
            }
            
            subgraph cluster_fact {
                label="Fact Tables";
                style=filled;
                color="#e8f5e9";
                
                FACT_INVENTORY [label="{FACT_INVENTORY|inventory_key PK\\lproduct_key FK\\llocation_key FK\\ldate_key FK\\lqty_on_hand\\lqty_in_transit\\lqty_reserved\\l}", fillcolor="#a5d6a7"];
                FACT_ORDERS [label="{FACT_ORDERS|order_key PK\\lproduct_key FK\\lcustomer_key FK\\ldate_key FK\\lqty_ordered\\lqty_shipped\\lrevenue\\l}", fillcolor="#a5d6a7"];
                FACT_PRODUCTION [label="{FACT_PRODUCTION|production_key PK\\lproduct_key FK\\llocation_key FK\\lequipment_key FK\\ldate_key FK\\lqty_produced\\lyield_rate\\l}", fillcolor="#a5d6a7"];
                FACT_QUALITY [label="{FACT_QUALITY|quality_key PK\\lproduct_key FK\\llocation_key FK\\ldate_key FK\\ldefect_count\\lfpy_rate\\ldpmo\\l}", fillcolor="#a5d6a7"];
                FACT_SHIPMENTS [label="{FACT_SHIPMENTS|shipment_key PK\\lorder_key FK\\lsupplier_key FK\\ldate_key FK\\lqty_shipped\\lcarrier\\ltrack_status\\l}", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_bridge {
                label="Bridge Tables";
                style=filled;
                color="#fff3e0";
                
                BOM [label="{BRIDGE_BOM|bom_id PK\\lparent_product_key FK\\lchild_product_key FK\\lqty_per\\l}", fillcolor="#ffcc80"];
                SUPPLIER_PRODUCT [label="{BRIDGE_SUPPLIER_PRODUCT|supplier_key FK\\lproduct_key FK\\llead_time\\lunit_cost\\l}", fillcolor="#ffcc80"];
            }
            
            DIM_PRODUCT -> FACT_INVENTORY;
            DIM_PRODUCT -> FACT_ORDERS;
            DIM_PRODUCT -> FACT_PRODUCTION;
            DIM_PRODUCT -> FACT_QUALITY;
            DIM_LOCATION -> FACT_INVENTORY;
            DIM_LOCATION -> FACT_PRODUCTION;
            DIM_LOCATION -> FACT_QUALITY;
            DIM_CUSTOMER -> FACT_ORDERS;
            DIM_SUPPLIER -> FACT_SHIPMENTS;
            DIM_DATE -> FACT_INVENTORY;
            DIM_DATE -> FACT_ORDERS;
            DIM_DATE -> FACT_PRODUCTION;
            DIM_DATE -> FACT_QUALITY;
            DIM_DATE -> FACT_SHIPMENTS;
            DIM_EQUIPMENT -> FACT_PRODUCTION;
            
            DIM_PRODUCT -> BOM [dir=both];
            DIM_PRODUCT -> SUPPLIER_PRODUCT;
            DIM_SUPPLIER -> SUPPLIER_PRODUCT;
        }
        """
        st.graphviz_chart(erd_diagram, use_container_width=True)
        
        # Schema details
        st.markdown("---")
        st.markdown("##### 📋 Schema Inventory")
        
        schemas = pd.DataFrame({
            "Schema": ["RAW", "STAGING", "CURATED", "ANALYTICS", "ML", "APP", "SECURITY", "EXTERNAL"],
            "Purpose": ["Landing zone for raw data", "Cleansed and validated data", "Business-ready transformed data", "Aggregated data marts", "ML features and predictions", "Application-specific views", "RLS mappings and policies", "Partner/customer shares"],
            "Tables": ["48", "42", "65", "35", "18", "12", "8", "15"],
            "Refresh": ["Real-time/Batch", "Near real-time", "Hourly", "Hourly", "Daily", "Real-time", "On-change", "Hourly"],
            "Retention": ["7 days", "30 days", "7 years", "3 years", "1 year", "N/A", "Indefinite", "90 days"],
            "Access": ["Data Engineers", "Data Engineers", "Analysts, Apps", "Analysts, Execs", "Data Scientists", "Application", "Security Admin", "External Roles"],
            "Owner": ["Data Engineering", "Data Engineering", "Analytics", "BI Team", "Data Science", "App Dev", "Security", "Data Eng"]
        })
        st.dataframe(schemas, use_container_width=True)
        
        # Key tables
        st.markdown("---")
        st.markdown("##### 📊 Key Tables by Domain")
        
        table_cols = st.columns(3)
        
        with table_cols[0]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_BLUE}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_BLUE};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_BLUE};">📦 Inventory Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_INVENTORY</code><br>
                    <code>FACT_INVENTORY_SNAPSHOTS</code><br>
                    <code>DIM_PRODUCT</code><br>
                    <code>DIM_LOCATION</code><br>
                    <code>AGG_INVENTORY_DAILY</code><br>
                    <code>V_INVENTORY_POSITION</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with table_cols[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_GREEN};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_GREEN};">🏭 Production Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_PRODUCTION</code><br>
                    <code>FACT_QUALITY</code><br>
                    <code>FACT_EQUIPMENT_TELEMETRY</code><br>
                    <code>DIM_EQUIPMENT</code><br>
                    <code>DIM_WORK_ORDER</code><br>
                    <code>V_PRODUCTION_KPI</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with table_cols[2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_ORANGE};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_ORANGE};">🤝 Supply Chain Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_ORDERS</code><br>
                    <code>FACT_SHIPMENTS</code><br>
                    <code>FACT_SUPPLIER_PERF</code><br>
                    <code>DIM_SUPPLIER</code><br>
                    <code>DIM_CUSTOMER</code><br>
                    <code>V_ORDER_FULFILLMENT</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional domains row
        st.markdown("")
        table_cols2 = st.columns(3)
        
        with table_cols2[0]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #9c27b015, #9c27b005);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #9c27b0;">
                <div style="font-size: 14px; font-weight: 700; color: #9c27b0;">📱 Certification Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_CERTIFICATIONS</code><br>
                    <code>FACT_CERT_TESTS</code><br>
                    <code>DIM_CARRIER</code><br>
                    <code>DIM_CERTIFICATION_TYPE</code><br>
                    <code>BRIDGE_PRODUCT_CARRIER</code><br>
                    <code>V_CERT_STATUS</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with table_cols2[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #00968815, #00968805);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #009688;">
                <div style="font-size: 14px; font-weight: 700; color: #009688;">🔄 Product Lifecycle Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_PRODUCT_LIFECYCLE</code><br>
                    <code>FACT_NPI_MILESTONES</code><br>
                    <code>DIM_LIFECYCLE_STAGE</code><br>
                    <code>FACT_EOL_IMPACT</code><br>
                    <code>FACT_LTB_ORDERS</code><br>
                    <code>V_LIFECYCLE_TIMELINE</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with table_cols2[2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f4433615, #f4433605);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #f44336;">
                <div style="font-size: 14px; font-weight: 700; color: #f44336;">🔁 Returns & RMA Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_RMA_TICKETS</code><br>
                    <code>FACT_FAILURE_ANALYSIS</code><br>
                    <code>DIM_FAILURE_MODE</code><br>
                    <code>DIM_DISPOSITION</code><br>
                    <code>AGG_RMA_BY_PRODUCT</code><br>
                    <code>V_WARRANTY_STATUS</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Third row of domains
        st.markdown("")
        table_cols3 = st.columns(3)
        
        with table_cols3[0]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #3f51b515, #3f51b505);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #3f51b5;">
                <div style="font-size: 14px; font-weight: 700; color: #3f51b5;">🏭 CM Portal Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_CM_PRODUCTION</code><br>
                    <code>FACT_CM_WIP</code><br>
                    <code>DIM_CM_SITE</code><br>
                    <code>DIM_PRODUCTION_LINE</code><br>
                    <code>AGG_CM_CAPACITY</code><br>
                    <code>V_CM_SCORECARD</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with table_cols3[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #ff980015, #ff980005);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #ff9800;">
                <div style="font-size: 14px; font-weight: 700; color: #ff9800;">💱 Financial Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_PRODUCT_COSTS</code><br>
                    <code>FACT_COST_VARIANCES</code><br>
                    <code>DIM_COST_CENTER</code><br>
                    <code>DIM_COST_ELEMENT</code><br>
                    <code>AGG_MARGIN_BY_PRODUCT</code><br>
                    <code>V_COST_BREAKDOWN</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with table_cols3[2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #4caf5015, #4caf5005);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #4caf50;">
                <div style="font-size: 14px; font-weight: 700; color: #4caf50;">🌱 ESG & Carbon Domain</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <code>FACT_CARBON_EMISSIONS</code><br>
                    <code>FACT_ENERGY_USAGE</code><br>
                    <code>DIM_EMISSION_SCOPE</code><br>
                    <code>DIM_SUSTAINABILITY_GOAL</code><br>
                    <code>AGG_CARBON_BY_SITE</code><br>
                    <code>V_ESG_SCORECARD</code>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 4: ETL / PIPELINES
    # =================================================================
    with arch_tab4:
        st.subheader("🔄 ETL & Data Pipelines")
        
        # Pipeline diagram
        st.markdown("##### 📊 Data Pipeline Flow")
        
        pipeline_diagram = """
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            edge [fontname="Arial", fontsize=9];
            
            subgraph cluster_extract {
                label="Extract";
                style=filled;
                color="#ffebee";
                
                E1 [label="SAP Extractor\\n(Fivetran)", fillcolor="#ef9a9a"];
                E2 [label="MES Kafka\\nConsumer", fillcolor="#ef9a9a"];
                E3 [label="IoT Snowpipe\\nIngestion", fillcolor="#ef9a9a"];
                E4 [label="API Collectors\\n(REST)", fillcolor="#ef9a9a"];
            }
            
            subgraph cluster_raw {
                label="RAW Layer";
                style=filled;
                color="#e3f2fd";
                
                R1 [label="raw.sap_*", fillcolor="#90caf9"];
                R2 [label="raw.mes_*", fillcolor="#90caf9"];
                R3 [label="raw.iot_*", fillcolor="#90caf9"];
                R4 [label="raw.api_*", fillcolor="#90caf9"];
            }
            
            subgraph cluster_transform {
                label="Transform (dbt)";
                style=filled;
                color="#fff3e0";
                
                T1 [label="stg_* models\\n(Cleansing)", fillcolor="#ffcc80"];
                T2 [label="int_* models\\n(Joins)", fillcolor="#ffcc80"];
                T3 [label="fct_* models\\n(Facts)", fillcolor="#ffcc80"];
                T4 [label="dim_* models\\n(Dimensions)", fillcolor="#ffcc80"];
            }
            
            subgraph cluster_curated {
                label="CURATED Layer";
                style=filled;
                color="#e8f5e9";
                
                C1 [label="curated.fact_*", fillcolor="#a5d6a7"];
                C2 [label="curated.dim_*", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_analytics {
                label="ANALYTICS Layer";
                style=filled;
                color="#f3e5f5";
                
                A1 [label="analytics.agg_*", fillcolor="#ce93d8"];
                A2 [label="analytics.v_*", fillcolor="#ce93d8"];
            }
            
            E1 -> R1;
            E2 -> R2;
            E3 -> R3;
            E4 -> R4;
            
            R1 -> T1;
            R2 -> T1;
            R3 -> T1;
            R4 -> T1;
            
            T1 -> T2;
            T2 -> T3;
            T2 -> T4;
            
            T3 -> C1;
            T4 -> C2;
            
            C1 -> A1;
            C2 -> A1;
            C1 -> A2;
            C2 -> A2;
        }
        """
        st.graphviz_chart(pipeline_diagram, use_container_width=True)
        
        # Pipeline inventory
        st.markdown("---")
        st.markdown("##### 📋 Pipeline Inventory")
        
        pipelines = pd.DataFrame({
            "Pipeline": ["SAP Orders Sync", "SAP Inventory Sync", "SAP Finance Sync", "MES Production Stream", "IoT Telemetry", "Quality/LIMS Data", "Salesforce CRM", "Forecast Ingestion", "Weather Data", "Shipping Updates", "Market Data", "EDI Orders", "CM Foxconn Feed", "CM Flex Feed", "RMA/Returns", "Certification Status", "PLM/Engineering", "Carbon Metrics", "Customer Hub Inv", "Supplier Scorecards", "Cost Actuals", "Design Win Pipeline", "Carrier Cert Updates", "Equipment Telemetry"],
            "Type": ["Batch", "Batch", "Batch", "Streaming", "Streaming", "Streaming", "Batch", "Batch", "API", "API", "Marketplace", "Streaming", "Batch", "Batch", "Streaming", "Batch", "Batch", "Batch", "Batch", "Batch", "Batch", "Batch", "Batch", "Streaming"],
            "Source": ["SAP S/4HANA", "SAP S/4HANA", "SAP FI/CO", "Camstar MES", "deviceWISE", "LIMS", "Salesforce", "Excel/Planning", "OpenWeather", "DHL/FedEx", "Bloomberg", "EDI X12", "Foxconn SFTP", "Flex SFTP", "RMA System", "Carrier Portals", "Teamcenter", "Carbon API", "Customer Files", "Supplier Portal", "SAP CO", "Salesforce", "PTCRB/GCF", "SCADA"],
            "Frequency": ["15 min", "15 min", "1 hour", "Real-time", "1 sec", "Real-time", "30 min", "Daily", "Hourly", "On-event", "Daily", "Real-time", "Hourly", "Hourly", "Real-time", "Daily", "Hourly", "Weekly", "Daily", "Weekly", "Daily", "Daily", "Daily", "1 sec"],
            "Tool": ["Fivetran", "Fivetran", "Fivetran", "Kafka + Snowpipe", "Snowpipe", "Kafka", "Fivetran", "Internal Stage", "Snowpipe REST", "REST API", "Data Share", "Snowpipe", "Snowpipe", "Snowpipe", "REST API", "REST API", "REST API", "REST API", "Internal Stage", "Snowpipe", "Fivetran", "Fivetran", "REST API", "Snowpipe"],
            "SLA": ["<5 min", "<5 min", "<1 hr", "<10 sec", "<5 sec", "<10 sec", "<5 min", "By 6 AM", "<1 hr", "<5 min", "By 8 AM", "<1 min", "<30 min", "<30 min", "<5 min", "<24 hr", "<1 hr", "<1 wk", "By 6 AM", "<1 wk", "<24 hr", "<24 hr", "<24 hr", "<5 sec"],
            "Owner": ["Data Eng", "Data Eng", "Finance IT", "Data Eng", "IoT Team", "Quality", "Data Eng", "Planning", "Data Eng", "Logistics", "Data Eng", "EDI Team", "CM Mgmt", "CM Mgmt", "Service", "Quality", "Engineering", "ESG Team", "Planning", "Procurement", "Finance IT", "Sales Ops", "Quality", "IoT Team"]
        })
        st.dataframe(pipelines, use_container_width=True)
        
        # dbt project structure
        st.markdown("---")
        st.markdown("##### 🛠️ dbt Project Structure")
        
        dbt_col1, dbt_col2 = st.columns(2)
        
        with dbt_col1:
            st.code("""
telit_supply_chain/
├── dbt_project.yml
├── profiles.yml
├── models/
│   ├── staging/
│   │   ├── sap/
│   │   │   ├── stg_sap_orders.sql
│   │   │   ├── stg_sap_inventory.sql
│   │   │   └── stg_sap_costs.sql
│   │   ├── mes/
│   │   │   ├── stg_mes_production.sql
│   │   │   └── stg_mes_quality.sql
│   │   ├── cm/
│   │   │   ├── stg_foxconn_wip.sql
│   │   │   └── stg_flex_output.sql
│   │   └── external/
│   │       ├── stg_carrier_certs.sql
│   │       └── stg_rma_tickets.sql
│   ├── intermediate/
│   │   ├── int_order_fulfillment.sql
│   │   ├── int_inventory_position.sql
│   │   ├── int_cm_consolidated.sql
│   │   └── int_product_lifecycle.sql
│   ├── marts/
│   │   ├── core/          (dims & facts)
│   │   ├── supply_chain/  (orders, inventory)
│   │   ├── manufacturing/ (production, quality)
│   │   ├── finance/       (costs, margins)
│   │   └── compliance/    (certs, esg)
│   └── schema.yml
├── tests/
├── macros/
└── snapshots/
            """, language="text")
        
        with dbt_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);
                        border-radius: 10px; padding: 15px;">
                <div style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">📊 dbt Metrics</div>
                <div style="font-size: 12px; margin: 8px 0;"><strong>Models:</strong> 125</div>
                <div style="font-size: 12px; margin: 8px 0;"><strong>Tests:</strong> 380</div>
                <div style="font-size: 12px; margin: 8px 0;"><strong>Sources:</strong> 18</div>
                <div style="font-size: 12px; margin: 8px 0;"><strong>Snapshots:</strong> 12</div>
                <div style="font-size: 12px; margin: 8px 0;"><strong>Run Time:</strong> ~18 min</div>
                <div style="font-size: 12px; margin: 8px 0;"><strong>Schedule:</strong> Hourly</div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 5: SNOWFLAKE SPECIFICS
    # =================================================================
    with arch_tab5:
        st.subheader("❄️ Snowflake Configuration")
        
        # Snowflake features diagram
        st.markdown("##### 📊 Snowflake Features Used")
        
        sf_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            Snowflake [label="Snowflake Data Cloud", shape=cylinder, fillcolor="#29b5e8", fontcolor=white, fontsize=14];
            
            subgraph cluster_ingest {
                label="Ingestion";
                style=filled;
                color="#e3f2fd";
                
                Snowpipe [label="Snowpipe\\nReal-time streaming", fillcolor="#90caf9"];
                Stage [label="Stages\\nFile ingestion", fillcolor="#90caf9"];
            }
            
            subgraph cluster_storage {
                label="Storage";
                style=filled;
                color="#e8f5e9";
                
                Tables [label="Tables\\nStructured data", fillcolor="#a5d6a7"];
                Iceberg [label="Iceberg Tables\\nOpen format", fillcolor="#a5d6a7"];
                TimeTravel [label="Time Travel\\n90 days history", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_compute {
                label="Compute";
                style=filled;
                color="#fff3e0";
                
                Warehouses [label="Warehouses\\nETL, BI, ML", fillcolor="#ffcc80"];
                DynamicTables [label="Dynamic Tables\\nIncremental transforms", fillcolor="#ffcc80"];
                Tasks [label="Tasks & Streams\\nOrchestration", fillcolor="#ffcc80"];
            }
            
            subgraph cluster_ml {
                label="ML & AI";
                style=filled;
                color="#fce4ec";
                
                Cortex [label="Cortex AI\\nLLM functions", fillcolor="#f48fb1"];
                SnowparkML [label="Snowpark ML\\nModel training", fillcolor="#f48fb1"];
                Features [label="Feature Store\\nML features", fillcolor="#f48fb1"];
            }
            
            subgraph cluster_app {
                label="Applications";
                style=filled;
                color="#f3e5f5";
                
                Streamlit [label="Streamlit\\nDashboards", fillcolor="#ce93d8"];
                NativeApp [label="Native Apps\\nMarketplace", fillcolor="#ce93d8"];
                DataShare [label="Data Sharing\\nSecure shares", fillcolor="#ce93d8"];
            }
            
            Snowflake -> Snowpipe;
            Snowflake -> Stage;
            Snowflake -> Tables;
            Snowflake -> Iceberg;
            Snowflake -> TimeTravel;
            Snowflake -> Warehouses;
            Snowflake -> DynamicTables;
            Snowflake -> Tasks;
            Snowflake -> Cortex;
            Snowflake -> SnowparkML;
            Snowflake -> Features;
            Snowflake -> Streamlit;
            Snowflake -> NativeApp;
            Snowflake -> DataShare;
        }
        """
        st.graphviz_chart(sf_diagram, use_container_width=True)
        
        # Warehouse configuration
        st.markdown("---")
        st.markdown("##### 🏭 Warehouse Configuration")
        
        warehouses = pd.DataFrame({
            "Warehouse": ["WH_ETL_XS", "WH_ETL_M", "WH_BI_S", "WH_ML_L", "WH_STREAMLIT_XS", "WH_STREAMLIT_S", "WH_ADHOC_S", "WH_EXTERNAL_XS"],
            "Size": ["X-Small", "Medium", "Small", "Large", "X-Small", "Small", "Small", "X-Small"],
            "Min/Max Clusters": ["1/2", "1/4", "1/3", "1/2", "1/1", "1/2", "1/2", "1/1"],
            "Auto-Suspend": ["60s", "120s", "60s", "300s", "60s", "60s", "120s", "30s"],
            "Scaling Policy": ["Standard", "Economy", "Standard", "Standard", "Standard", "Standard", "Economy", "Standard"],
            "Purpose": ["Light ETL, dynamic tables", "Heavy transforms, dbt", "BI/Tableau queries", "ML training, Cortex", "Streamlit (internal)", "Streamlit (heavy)", "Analyst ad-hoc", "Partner/customer access"],
            "Monthly Cost Est.": ["$180", "$950", "$450", "$1,400", "$120", "$350", "$300", "$80"]
        })
        st.dataframe(warehouses, use_container_width=True)
        
        # Cortex AI functions
        st.markdown("---")
        st.markdown("##### 🤖 Cortex AI Functions Used")
        
        cortex_cols = st.columns(4)
        cortex_funcs = [
            ("COMPLETE", "Text generation", "AI insights, recommendations", TELIT_BLUE),
            ("SUMMARIZE", "Text summarization", "Risk summaries, alerts", TELIT_GREEN),
            ("SENTIMENT", "Sentiment analysis", "Customer feedback", TELIT_ORANGE),
            ("FORECAST", "Time series forecast", "Demand prediction", '#ce93d8'),
        ]
        for col, (func, desc, usage, color) in zip(cortex_cols, cortex_funcs):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {color};">
                <div style="font-size: 13px; font-weight: 700; color: {color};">SNOWFLAKE.CORTEX.{func}</div>
                <div style="font-size: 11px; margin-top: 8px;">{desc}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY}; margin-top: 5px;">Usage: {usage}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Dynamic tables
        st.markdown("---")
        st.markdown("##### 📊 Dynamic Tables")
        
        dyn_tables = pd.DataFrame({
            "Table": ["DYN_INVENTORY_POSITION", "DYN_ORDER_STATUS", "DYN_PRODUCTION_KPI", "DYN_SUPPLIER_SCORECARD", "DYN_QUALITY_METRICS", "DYN_CERT_STATUS", "DYN_CM_CAPACITY", "DYN_RMA_SUMMARY", "DYN_PRODUCT_COSTS", "DYN_DEMAND_SIGNAL"],
            "Target Lag": ["1 minute", "5 minutes", "5 minutes", "1 hour", "15 minutes", "1 hour", "30 minutes", "15 minutes", "1 hour", "5 minutes"],
            "Warehouse": ["WH_ETL_XS", "WH_ETL_XS", "WH_ETL_XS", "WH_ETL_M", "WH_ETL_XS", "WH_ETL_XS", "WH_ETL_XS", "WH_ETL_XS", "WH_ETL_M", "WH_ETL_XS"],
            "Refresh Mode": ["Incremental", "Incremental", "Full", "Full", "Incremental", "Full", "Full", "Incremental", "Full", "Incremental"],
            "Downstream": ["3 views", "4 views", "5 views", "2 views", "4 views", "2 views", "3 views", "2 views", "3 views", "4 views"],
            "Avg Refresh": ["8 sec", "12 sec", "45 sec", "2 min", "15 sec", "30 sec", "45 sec", "10 sec", "1.5 min", "8 sec"]
        })
        st.dataframe(dyn_tables, use_container_width=True)
    
    # =================================================================
    # TAB 6: ML / ANALYTICS
    # =================================================================
    with arch_tab6:
        st.subheader("🤖 ML Models & Analytics")
        
        # ML pipeline diagram
        st.markdown("##### 📊 ML Pipeline Architecture")
        
        ml_diagram = """
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            subgraph cluster_features {
                label="Feature Engineering";
                style=filled;
                color="#e3f2fd";
                
                Raw [label="Raw Data", fillcolor="#90caf9"];
                Features [label="Feature Store\\n(Snowpark)", fillcolor="#90caf9"];
            }
            
            subgraph cluster_train {
                label="Training";
                style=filled;
                color="#fff3e0";
                
                SnowparkML [label="Snowpark ML\\nModel Training", fillcolor="#ffcc80"];
                Registry [label="Model Registry\\nVersioning", fillcolor="#ffcc80"];
            }
            
            subgraph cluster_serve {
                label="Serving";
                style=filled;
                color="#e8f5e9";
                
                UDF [label="Python UDFs\\nScoring", fillcolor="#a5d6a7"];
                Cortex [label="Cortex AI\\nLLM/Built-in", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_monitor {
                label="Monitoring";
                style=filled;
                color="#fce4ec";
                
                Drift [label="Drift Detection", fillcolor="#f48fb1"];
                Metrics [label="Model Metrics", fillcolor="#f48fb1"];
            }
            
            Raw -> Features [label="Transform"];
            Features -> SnowparkML [label="Train"];
            SnowparkML -> Registry [label="Version"];
            Registry -> UDF [label="Deploy"];
            Registry -> Cortex [label="Enhance"];
            UDF -> Drift [label="Monitor"];
            Cortex -> Drift;
            Drift -> Metrics;
        }
        """
        st.graphviz_chart(ml_diagram, use_container_width=True)
        
        # Model inventory
        st.markdown("---")
        st.markdown("##### 📋 ML Model Inventory")
        
        models = pd.DataFrame({
            "Model": ["Demand Forecast", "Equipment Failure", "Quality Prediction", "Lead Time Prediction", "Supplier Risk Score", "Inventory Optimization", "Anomaly Detection", "RMA Root Cause", "EOL Impact Predictor", "Certification Delay Risk", "CM Capacity Forecast", "Cost Variance Predictor"],
            "Type": ["Time Series", "Classification", "Classification", "Regression", "Ensemble", "Optimization", "Unsupervised", "NLP + Classification", "Survival Analysis", "Classification", "Time Series", "Regression"],
            "Algorithm": ["Prophet + Cortex", "XGBoost", "Random Forest", "Gradient Boost", "Weighted Ensemble", "Linear Prog", "Isolation Forest", "Cortex LLM + RF", "Cox Proportional", "Logistic Reg", "ARIMA", "XGBoost"],
            "Framework": ["Cortex FORECAST", "Snowpark ML", "Snowpark ML", "Snowpark ML", "Python UDF", "Snowpark", "Snowpark ML", "Cortex + Snowpark", "Snowpark ML", "Snowpark ML", "Snowpark ML", "Snowpark ML"],
            "Features": ["45", "28", "32", "18", "22", "35", "15", "42", "25", "18", "22", "30"],
            "Accuracy/Metric": ["MAPE: 8.2%", "AUC: 0.92", "F1: 0.89", "R²: 0.87", "—", "—", "—", "F1: 0.84", "C-Index: 0.81", "AUC: 0.88", "MAPE: 6.5%", "R²: 0.82"],
            "Refresh": ["Daily", "Hourly", "Hourly", "Daily", "Weekly", "Daily", "Real-time", "On-demand", "Weekly", "Daily", "Daily", "Weekly"],
            "Owner": ["Data Science", "Data Science", "Data Science", "Data Science", "Analytics", "Data Science", "Data Science", "Data Science", "Data Science", "Quality Team", "CM Mgmt", "Finance"]
        })
        st.dataframe(models, use_container_width=True)
        
        # Feature store
        st.markdown("---")
        st.markdown("##### 📊 Feature Store Schema")
        
        feature_cols = st.columns(3)
        
        with feature_cols[0]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_BLUE}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_BLUE};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_BLUE};">📈 Demand Features</div>
                <div style="font-size: 10px; margin-top: 10px;">
                    • rolling_avg_7d<br>
                    • rolling_avg_30d<br>
                    • yoy_growth<br>
                    • seasonality_index<br>
                    • promo_flag<br>
                    • weather_impact
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with feature_cols[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_GREEN};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_GREEN};">🔧 Equipment Features</div>
                <div style="font-size: 10px; margin-top: 10px;">
                    • operating_hours<br>
                    • vibration_rms<br>
                    • temperature_delta<br>
                    • power_consumption<br>
                    • cycle_count<br>
                    • maintenance_age
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with feature_cols[2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_ORANGE};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_ORANGE};">🤝 Supplier Features</div>
                <div style="font-size: 10px; margin-top: 10px;">
                    • on_time_delivery_rate<br>
                    • quality_score<br>
                    • lead_time_variance<br>
                    • financial_risk_score<br>
                    • geo_risk_score<br>
                    • concentration_ratio
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Additional feature domains
        st.markdown("")
        feature_cols2 = st.columns(3)
        
        with feature_cols2[0]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #9c27b015, #9c27b005);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #9c27b0;">
                <div style="font-size: 14px; font-weight: 700; color: #9c27b0;">📱 Certification Features</div>
                <div style="font-size: 10px; margin-top: 10px;">
                    • cert_age_days<br>
                    • renewal_countdown<br>
                    • test_pass_rate<br>
                    • carrier_priority<br>
                    • region_compliance<br>
                    • cert_delay_history
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with feature_cols2[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f4433615, #f4433605);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #f44336;">
                <div style="font-size: 14px; font-weight: 700; color: #f44336;">🔁 RMA Features</div>
                <div style="font-size: 10px; margin-top: 10px;">
                    • failure_mode_freq<br>
                    • return_rate_30d<br>
                    • avg_resolution_days<br>
                    • repeat_failure_flag<br>
                    • warranty_coverage<br>
                    • root_cause_cluster
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with feature_cols2[2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #ff980015, #ff980005);
                        border-radius: 10px; padding: 15px; border-top: 3px solid #ff9800;">
                <div style="font-size: 14px; font-weight: 700; color: #ff9800;">💱 Cost Features</div>
                <div style="font-size: 10px; margin-top: 10px;">
                    • material_cost_ratio<br>
                    • labor_cost_pct<br>
                    • overhead_allocation<br>
                    • variance_trend<br>
                    • margin_by_customer<br>
                    • cost_driver_rank
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # =================================================================
    # TAB 7: INFRASTRUCTURE
    # =================================================================
    with arch_tab7:
        st.subheader("🖥️ Infrastructure & DevOps")
        
        # Infrastructure diagram
        st.markdown("##### 📊 Deployment Architecture")
        
        infra_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            subgraph cluster_dev {
                label="Development";
                style=filled;
                color="#e3f2fd";
                
                IDE [label="VS Code\\n+ Extensions", fillcolor="#90caf9"];
                Git [label="GitHub\\nVersion Control", fillcolor="#90caf9"];
                CI [label="GitHub Actions\\nCI/CD", fillcolor="#90caf9"];
            }
            
            subgraph cluster_env {
                label="Environments";
                style=filled;
                color="#fff3e0";
                
                Dev [label="DEV\\nSnowflake Account", fillcolor="#ffcc80"];
                QA [label="QA\\nSnowflake Account", fillcolor="#ffcc80"];
                Prod [label="PROD\\nSnowflake Account", fillcolor="#ffcc80"];
            }
            
            subgraph cluster_infra {
                label="Infrastructure as Code";
                style=filled;
                color="#e8f5e9";
                
                Terraform [label="Terraform\\nSnowflake Provider", fillcolor="#a5d6a7"];
                dbt [label="dbt\\nData Models", fillcolor="#a5d6a7"];
                Schemachange [label="Schemachange\\nMigrations", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_monitor {
                label="Monitoring";
                style=filled;
                color="#fce4ec";
                
                QueryHist [label="Query History\\nPerformance", fillcolor="#f48fb1"];
                Alerts [label="Alerts\\nNotifications", fillcolor="#f48fb1"];
                Datadog [label="Datadog\\nAPM", fillcolor="#f48fb1"];
            }
            
            IDE -> Git;
            Git -> CI;
            CI -> Terraform;
            CI -> dbt;
            CI -> Schemachange;
            
            Terraform -> Dev;
            Terraform -> QA;
            Terraform -> Prod;
            
            dbt -> Dev;
            dbt -> QA;
            dbt -> Prod;
            
            Prod -> QueryHist;
            Prod -> Alerts;
            Prod -> Datadog;
        }
        """
        st.graphviz_chart(infra_diagram, use_container_width=True)
        
        # Environment details
        st.markdown("---")
        st.markdown("##### 🌐 Environment Configuration")
        
        envs = pd.DataFrame({
            "Environment": ["Development", "QA/Staging", "Production"],
            "Snowflake Account": ["telit_dev.us-east-1", "telit_qa.us-east-1", "telit_prod.us-east-1"],
            "Edition": ["Enterprise", "Enterprise", "Enterprise"],
            "Databases": ["5", "5", "8"],
            "Warehouses": ["3", "4", "6"],
            "Users": ["25", "15", "500+"],
            "Data Retention": ["7 days", "14 days", ["90 days"]],
            "Backup": ["Daily", "Daily", "Continuous + Failsafe"]
        })
        st.dataframe(envs, use_container_width=True)
        
        # CI/CD pipeline
        st.markdown("---")
        st.markdown("##### 🔄 CI/CD Pipeline")
        
        cicd_cols = st.columns(5)
        cicd_steps = [
            ("1. Commit", "GitHub", "Push to branch", TELIT_BLUE),
            ("2. Build", "GitHub Actions", "Lint, compile, test", TELIT_ORANGE),
            ("3. Deploy DEV", "Terraform + dbt", "Auto deploy to DEV", TELIT_GREEN),
            ("4. Test", "dbt test + pytest", "Integration tests", TELIT_BLUE),
            ("5. Deploy PROD", "Manual approval", "Release to PROD", TELIT_GREEN),
        ]
        for col, (step, tool, desc, color) in zip(cicd_cols, cicd_steps):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 700; color: {color};">{step}</div>
                <div style="font-size: 11px; font-weight: 600; margin: 5px 0;">{tool}</div>
                <div style="font-size: 9px; color: {TELIT_GRAY};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Security
        st.markdown("---")
        st.markdown("##### 🔐 Security Configuration")
        
        security = pd.DataFrame({
            "Control": ["Authentication", "Authorization", "Encryption at Rest", "Encryption in Transit", "Network Policy", "Key Management", "Audit Logging", "Data Masking"],
            "Implementation": ["SSO (Okta)", "RBAC + Row-Level Security", "AES-256", "TLS 1.3", "Private Link", "Snowflake KMS", "Account Usage Schema", "Dynamic Masking Policies"],
            "Status": ["✅ Enabled", "✅ Enabled", "✅ Enabled", "✅ Enabled", "✅ Enabled", "✅ Enabled", "✅ Enabled", "✅ Enabled"],
            "Compliance": ["SOC 2", "GDPR, SOC 2", "GDPR, SOC 2", "SOC 2", "SOC 2", "SOC 2", "SOC 2, GDPR", "GDPR, PCI-DSS"]
        })
        st.dataframe(security, use_container_width=True)
    
    # =================================================================
    # TAB 8: INTEGRATIONS
    # =================================================================
    with arch_tab8:
        st.subheader("🔌 External Integrations & APIs")
        
        # Integration diagram
        st.markdown("##### 📊 Integration Landscape")
        
        int_diagram = """
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            Snowflake [label="Snowflake\\nData Platform", shape=cylinder, fillcolor="#29b5e8", fontcolor=white];
            
            subgraph cluster_inbound {
                label="Inbound (Data Sources)";
                style=filled;
                color="#e8f5e9";
                
                SAP [label="SAP S/4HANA\\nOData API", fillcolor="#a5d6a7"];
                Salesforce [label="Salesforce\\nREST API", fillcolor="#a5d6a7"];
                Telit [label="Telit deviceWISE\\nMQTT/REST", fillcolor="#a5d6a7"];
                Weather [label="OpenWeather\\nREST API", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_outbound {
                label="Outbound (Consumers)";
                style=filled;
                color="#fce4ec";
                
                PowerBI [label="Power BI\\nDirect Query", fillcolor="#f48fb1"];
                Tableau [label="Tableau\\nSnowflake Connector", fillcolor="#f48fb1"];
                Python [label="Python Apps\\nSnowpark", fillcolor="#f48fb1"];
                Excel [label="Excel\\nODBC", fillcolor="#f48fb1"];
            }
            
            subgraph cluster_share {
                label="Data Sharing";
                style=filled;
                color="#e3f2fd";
                
                Partners [label="Partner Shares\\nSecure Sharing", fillcolor="#90caf9"];
                Marketplace [label="Marketplace\\nData Products", fillcolor="#90caf9"];
            }
            
            SAP -> Snowflake;
            Salesforce -> Snowflake;
            Telit -> Snowflake;
            Weather -> Snowflake;
            
            Snowflake -> PowerBI;
            Snowflake -> Tableau;
            Snowflake -> Python;
            Snowflake -> Excel;
            
            Snowflake -> Partners;
            Snowflake -> Marketplace;
        }
        """
        st.graphviz_chart(int_diagram, use_container_width=True)
        
        # API specifications
        st.markdown("---")
        st.markdown("##### 📋 API Specifications")
        
        apis = pd.DataFrame({
            "API": ["SAP OData", "Salesforce REST", "Telit deviceWISE", "OpenWeather", "DHL Tracking", "FedEx API", "PTCRB Cert", "GCF Portal", "Foxconn EDI", "Bloomberg Market"],
            "Type": ["REST/OData", "REST", "MQTT/REST", "REST", "REST", "REST", "REST", "REST/SOAP", "EDI/SFTP", "Snowflake Share"],
            "Auth": ["OAuth 2.0", "OAuth 2.0", "API Key", "API Key", "API Key", "OAuth 2.0", "API Key", "Certificate", "X.509 Cert", "Data Share"],
            "Rate Limit": ["1000/min", "15000/day", "Unlimited", "1000/day", "500/min", "500/min", "100/hr", "50/hr", "N/A", "N/A"],
            "Data Format": ["JSON/XML", "JSON", "JSON", "JSON", "JSON", "JSON", "JSON", "XML", "X12/CSV", "Parquet"],
            "Refresh": ["15 min", "30 min", "Real-time", "1 hour", "On-event", "On-event", "Daily", "Daily", "Hourly", "Daily"],
            "Owner": ["IT - ERP", "IT - CRM", "IoT Team", "Data Eng", "Logistics", "Logistics", "Quality", "Quality", "CM Mgmt", "Data Eng"]
        })
        st.dataframe(apis, use_container_width=True)
        
        # Data sharing
        st.markdown("---")
        st.markdown("##### 🤝 Secure Data Shares")
        
        shares = pd.DataFrame({
            "Share Name": ["TELIT_SUPPLIER_PORTAL", "TELIT_CUSTOMER_VISIBILITY", "TELIT_CM_PORTAL", "TELIT_CARRIER_CERTS", "TELIT_PARTNER_DATA", "TELIT_ANALYTICS_EXPORT"],
            "Direction": ["Outbound", "Outbound", "Bidirectional", "Outbound", "Bidirectional", "Outbound"],
            "Consumers": ["158 suppliers", "245 customers", "3 CMs", "15 carriers", "12 partners", "Internal teams"],
            "Databases": ["SUPPLIER_PORTAL", "CUSTOMER_HUB", "CM_EXCHANGE", "CARRIER_CERTS", "PARTNER_EXCHANGE", "ANALYTICS_EXPORT"],
            "Tables/Views": ["15", "12", "18", "8", "15", "35"],
            "Row-Level Security": ["Yes (by supplier)", "Yes (by customer)", "Yes (by CM)", "Yes (by carrier)", "Yes", "No"],
            "Refresh": ["Near real-time", "Hourly", "Hourly", "Daily", "Near real-time", "Daily"]
        })
        st.dataframe(shares, use_container_width=True)
    
    # =================================================================
    # TAB 9: CODE STRUCTURE
    # =================================================================
    with arch_tab9:
        st.subheader("📁 Application Code Structure")
        
        # App architecture
        st.markdown("##### 📊 Streamlit App Architecture")
        
        app_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            subgraph cluster_app {
                label="Streamlit Application";
                style=filled;
                color="#fce4ec";
                
                Main [label="streamlit_app.py\\n(Main Entry)", fillcolor="#f48fb1"];
                
                subgraph cluster_pages {
                    label="Pages/Dashboards";
                    style=filled;
                    color="#fff3e0";
                    
                    Home [label="Home", fillcolor="#ffcc80"];
                    Exec [label="Executive", fillcolor="#ffcc80"];
                    Digital [label="Digital Twin", fillcolor="#ffcc80"];
                    Inv [label="Inventory", fillcolor="#ffcc80"];
                    Other [label="... (17 total)", fillcolor="#ffcc80"];
                }
                
                subgraph cluster_comp {
                    label="Components";
                    style=filled;
                    color="#e3f2fd";
                    
                    Charts [label="charts.py\\nPlotly wrappers", fillcolor="#90caf9"];
                    Cards [label="cards.py\\nKPI cards", fillcolor="#90caf9"];
                    Tables [label="tables.py\\nDataframes", fillcolor="#90caf9"];
                    Styles [label="styles.py\\nCSS/Theming", fillcolor="#90caf9"];
                }
                
                subgraph cluster_data {
                    label="Data Layer";
                    style=filled;
                    color="#e8f5e9";
                    
                    Queries [label="queries.py\\nSQL queries", fillcolor="#a5d6a7"];
                    Cache [label="cache.py\\nst.cache_data", fillcolor="#a5d6a7"];
                    Models [label="models.py\\nPydantic models", fillcolor="#a5d6a7"];
                }
            }
            
            subgraph cluster_snowflake {
                label="Snowflake Backend";
                style=filled;
                color="#e3f2fd";
                
                SF [label="Snowflake\\nData Cloud", shape=cylinder, fillcolor="#29b5e8", fontcolor=white];
            }
            
            Main -> Home;
            Main -> Exec;
            Main -> Digital;
            Main -> Inv;
            Main -> Other;
            
            Home -> Charts;
            Home -> Cards;
            Home -> Tables;
            
            Charts -> Queries;
            Cards -> Queries;
            Tables -> Queries;
            
            Queries -> Cache;
            Cache -> SF;
            
            Main -> Styles;
        }
        """
        st.graphviz_chart(app_diagram, use_container_width=True)
        
        # File structure
        st.markdown("---")
        st.markdown("##### 📂 Repository Structure")
        
        repo_col1, repo_col2 = st.columns(2)
        
        with repo_col1:
            st.code("""
telit-supply-chain/
├── README.md
├── requirements.txt
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy-dev.yml
│       └── deploy-prod.yml
├── snowflake_app/
│   ├── streamlit_app.py      # Main app (13,000+ lines)
│   ├── components/
│   │   ├── __init__.py
│   │   ├── styles.py         # CSS theming
│   │   ├── charts.py         # Plotly wrappers
│   │   ├── cards.py          # KPI cards
│   │   ├── tables.py         # DataFrames
│   │   └── maps.py           # Geo visualizations
│   ├── data/
│   │   ├── __init__.py
│   │   ├── queries.py        # SQL queries
│   │   ├── cache.py          # st.cache_data
│   │   └── models.py         # Pydantic models
│   ├── ml/
│   │   ├── __init__.py
│   │   ├── forecasting.py    # Demand models
│   │   └── scoring.py        # UDF wrappers
│   └── utils/
│       └── formatters.py     # Formatting utils
├── dbt/
│   └── (125 models)
├── terraform/
│   └── (IaC configs)
└── tests/
    └── (unit + integration)
            """, language="text")
        
        with repo_col2:
            st.markdown("##### 📊 Code Metrics")
            code_metrics = pd.DataFrame({
                "Metric": ["Total Lines of Code", "Python Files", "SQL Files (dbt)", "Test Coverage", "Dashboards", "Tabs (total)", "Charts", "KPI Cards", "Data Tables"],
                "Value": ["~13,000", "22", "125", "74%", "17", "115+", "180+", "280+", "120+"]
            })
            st.dataframe(code_metrics, use_container_width=True)
            
            st.markdown("##### 📦 Key Dependencies")
            st.code("""
streamlit==1.31.0
pandas==2.1.4
plotly==5.18.0
snowflake-connector-python==3.6.0
snowflake-snowpark-python==1.11.1
graphviz==0.20.1
numpy==1.26.3
pydantic==2.5.3
            """, language="text")
        
        # Dashboard summary
        st.markdown("---")
        st.markdown("##### 📊 Dashboard Summary")
        
        dashboards = pd.DataFrame({
            "Dashboard": ["🏠 Home", "📊 Executive", "🏭 Digital Twin", "📦 Inventory & Shipments", "📈 Demand Forecast", "🤝 Suppliers", "✅ Quality", "🔗 Traceability", "📱 Certifications", "🔄 Product Lifecycle", "📋 Customer Orders", "🔁 Returns & RMA", "🏭 CM Portal", "💱 Financial & Costing", "🌱 Carbon ESG", "⚠️ Risk & Maintenance", "🏗️ Architecture"],
            "Tabs": ["1", "5", "11", "11", "13", "9", "9", "7", "6", "6", "6", "6", "6", "6", "7", "8", "10"],
            "Charts": ["15", "12", "25", "20", "18", "12", "15", "8", "10", "12", "10", "12", "14", "12", "12", "10", "10"],
            "KPI Cards": ["25", "20", "30", "25", "20", "15", "20", "12", "18", "15", "12", "14", "16", "15", "18", "16", "8"],
            "Tables": ["8", "5", "12", "15", "10", "8", "10", "8", "6", "8", "10", "8", "12", "10", "8", "6", "12"],
            "ML Models": ["—", "2", "3", "2", "3", "1", "1", "—", "—", "2", "1", "1", "2", "1", "1", "3", "—"],
            "Data Sources": ["All", "5", "4", "3", "4", "2", "2", "3", "2", "4", "3", "3", "4", "3", "3", "4", "—"]
        })
        st.dataframe(dashboards, use_container_width=True)
        
        # Implementation timeline
        st.markdown("---")
        st.markdown("##### 📅 Implementation Phases")
        
        phases = pd.DataFrame({
            "Phase": ["Phase 1: Foundation", "Phase 2: Core Dashboards", "Phase 3: Advanced Analytics", "Phase 4: AI/ML", "Phase 5: Extended"],
            "Duration": ["4 weeks", "6 weeks", "4 weeks", "4 weeks", "14 weeks"],
            "Deliverables": ["Data platform, ETL, base schemas", "Executive, Inventory, Suppliers, Quality", "Digital Twin, Demand Forecast, Traceability", "Cortex AI, Predictive Models, Insights", "Certifications, PLM, Orders, RMA, CM, Financial"],
            "Status": ["✅ Complete", "✅ Complete", "✅ Complete", "✅ Complete", "🔵 In Progress"],
            "Team": ["Data Eng (3)", "Data Eng (2) + BI (2)", "Data Eng (2) + DS (2)", "Data Science (3)", "Data Eng (2) + BI (2)"]
        })
        st.dataframe(phases, use_container_width=True)
    
    # =================================================================
    # TAB 10: GOVERNANCE & SECURITY
    # =================================================================
    with arch_tab10:
        st.subheader("🔐 Snowflake Governance & Security")
        
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #1a1a2e, #16213e); 
                    border-radius: 12px; padding: 20px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span style="font-size: 40px;">🛡️</span>
                <div>
                    <div style="font-size: 20px; font-weight: 700; color: white;">Enterprise Security & Governance</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 14px;">SOC 2 Type II • GDPR • ISO 27001 • FedRAMP compliant data platform</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Security KPIs
        sec_kpis = st.columns(6)
        for col, (label, value) in zip(sec_kpis, [
            ("Compliance", "SOC 2 Type II"),
            ("Encryption", "AES-256"),
            ("MFA Enabled", "100%"),
            ("Data Masking", "15 policies"),
            ("RBAC Roles", "24"),
            ("Audit Retention", "365 days")
        ]):
            col.metric(label, value)
        
        st.markdown("---")
        
        # Governance architecture diagram
        st.markdown("##### 🏛️ Governance Architecture")
        
        gov_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            subgraph cluster_identity {
                label="Identity & Access Management";
                style=filled;
                color="#e3f2fd";
                
                SSO [label="SSO (Okta)\\nSAML 2.0", fillcolor="#90caf9"];
                MFA [label="Multi-Factor\\nAuthentication", fillcolor="#90caf9"];
                SCIM [label="SCIM\\nUser Provisioning", fillcolor="#90caf9"];
            }
            
            subgraph cluster_access {
                label="Access Control";
                style=filled;
                color="#e8f5e9";
                
                RBAC [label="RBAC\\nRole-Based Access", fillcolor="#a5d6a7"];
                RLS [label="Row-Level Security\\nSecure Views", fillcolor="#a5d6a7"];
                CLS [label="Column-Level Security\\nDynamic Masking", fillcolor="#a5d6a7"];
                ObjPriv [label="Object Privileges\\nGRANT/REVOKE", fillcolor="#a5d6a7"];
            }
            
            subgraph cluster_data {
                label="Data Protection";
                style=filled;
                color="#fff3e0";
                
                EncRest [label="Encryption at Rest\\nAES-256", fillcolor="#ffcc80"];
                EncTransit [label="Encryption in Transit\\nTLS 1.3", fillcolor="#ffcc80"];
                KeyMgmt [label="Key Management\\nTri-Secret Secure", fillcolor="#ffcc80"];
                Masking [label="Dynamic Data Masking\\n15 Policies", fillcolor="#ffcc80"];
            }
            
            subgraph cluster_network {
                label="Network Security";
                style=filled;
                color="#fce4ec";
                
                PrivateLink [label="AWS PrivateLink\\nPrivate Connectivity", fillcolor="#f48fb1"];
                NetworkPolicy [label="Network Policies\\nIP Allowlisting", fillcolor="#f48fb1"];
                Firewall [label="Cloud Firewall\\nPerimeter Protection", fillcolor="#f48fb1"];
            }
            
            subgraph cluster_audit {
                label="Audit & Compliance";
                style=filled;
                color="#f3e5f5";
                
                AccessHist [label="ACCESS_HISTORY\\nQuery Logging", fillcolor="#ce93d8"];
                LoginHist [label="LOGIN_HISTORY\\nAuth Events", fillcolor="#ce93d8"];
                QueryHist [label="QUERY_HISTORY\\nPerformance", fillcolor="#ce93d8"];
                SIEM [label="SIEM Integration\\nSplunk/Datadog", fillcolor="#ce93d8"];
            }
            
            SSO -> RBAC;
            MFA -> SSO;
            SCIM -> SSO;
            
            RBAC -> RLS;
            RBAC -> CLS;
            RBAC -> ObjPriv;
            
            RLS -> EncRest;
            CLS -> Masking;
            
            PrivateLink -> EncTransit;
            NetworkPolicy -> PrivateLink;
            
            AccessHist -> SIEM;
            LoginHist -> SIEM;
            QueryHist -> SIEM;
        }
        """
        st.graphviz_chart(gov_diagram, use_container_width=True)
        
        # Role hierarchy
        st.markdown("---")
        st.markdown("##### 👥 Role Hierarchy (RBAC)")
        
        role_diagram = """
        digraph G {
            rankdir=TB;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            ACCOUNTADMIN [label="ACCOUNTADMIN\\n(2 users)", fillcolor="#ef5350", fontcolor=white];
            
            subgraph cluster_admin {
                label="Admin Roles";
                style=filled;
                color="#ffebee";
                
                SECURITYADMIN [label="SECURITYADMIN\\n(3 users)", fillcolor="#ff8a80"];
                SYSADMIN [label="SYSADMIN\\n(5 users)", fillcolor="#ff8a80"];
            }
            
            subgraph cluster_functional {
                label="Functional Roles";
                style=filled;
                color="#e3f2fd";
                
                DATA_ENGINEER [label="DATA_ENGINEER\\n(8 users)", fillcolor="#64b5f6"];
                DATA_SCIENTIST [label="DATA_SCIENTIST\\n(5 users)", fillcolor="#64b5f6"];
                BI_DEVELOPER [label="BI_DEVELOPER\\n(6 users)", fillcolor="#64b5f6"];
                APP_DEVELOPER [label="APP_DEVELOPER\\n(4 users)", fillcolor="#64b5f6"];
            }
            
            subgraph cluster_business {
                label="Business Roles";
                style=filled;
                color="#e8f5e9";
                
                ANALYST [label="ANALYST\\n(45 users)", fillcolor="#81c784"];
                VIEWER [label="VIEWER\\n(150 users)", fillcolor="#81c784"];
                EXECUTIVE [label="EXECUTIVE\\n(12 users)", fillcolor="#81c784"];
            }
            
            subgraph cluster_external {
                label="External Roles";
                style=filled;
                color="#fff3e0";
                
                SUPPLIER_PORTAL [label="SUPPLIER_PORTAL\\n(45 suppliers)", fillcolor="#ffb74d"];
                CUSTOMER_VIEW [label="CUSTOMER_VIEW\\n(125 customers)", fillcolor="#ffb74d"];
                PARTNER_ACCESS [label="PARTNER_ACCESS\\n(8 partners)", fillcolor="#ffb74d"];
            }
            
            ACCOUNTADMIN -> SECURITYADMIN;
            ACCOUNTADMIN -> SYSADMIN;
            
            SYSADMIN -> DATA_ENGINEER;
            SYSADMIN -> DATA_SCIENTIST;
            SYSADMIN -> BI_DEVELOPER;
            SYSADMIN -> APP_DEVELOPER;
            
            DATA_ENGINEER -> ANALYST;
            BI_DEVELOPER -> ANALYST;
            ANALYST -> VIEWER;
            ANALYST -> EXECUTIVE;
            
            SECURITYADMIN -> SUPPLIER_PORTAL;
            SECURITYADMIN -> CUSTOMER_VIEW;
            SECURITYADMIN -> PARTNER_ACCESS;
        }
        """
        st.graphviz_chart(role_diagram, use_container_width=True)
        
        # Role permissions matrix
        st.markdown("---")
        st.markdown("##### 📋 Role Permission Matrix")
        
        permissions = pd.DataFrame({
            "Role": ["ACCOUNTADMIN", "SECURITYADMIN", "SYSADMIN", "DATA_ENGINEER", "DATA_SCIENTIST", "BI_DEVELOPER", "ANALYST", "VIEWER", "EXECUTIVE", "CM_MANAGER", "QUALITY_LEAD", "FINANCE_ANALYST"],
            "Create Objects": ["✅", "❌", "✅", "✅", "✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Manage Users": ["✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Read RAW": ["✅", "❌", "✅", "✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Read CURATED": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "❌", "✅", "✅", "✅", "✅"],
            "Read ANALYTICS": ["✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅", "✅"],
            "Write Data": ["✅", "❌", "✅", "✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Run ML Models": ["✅", "❌", "✅", "✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌"],
            "Access Costs": ["✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "✅", "❌", "❌", "✅"],
            "Access PII": ["✅", "✅", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌", "❌"]
        })
        st.dataframe(permissions, use_container_width=True)
        
        # Data masking policies
        st.markdown("---")
        st.markdown("##### 🎭 Dynamic Data Masking Policies")
        
        masking_col1, masking_col2 = st.columns(2)
        
        with masking_col1:
            masking_policies = pd.DataFrame({
                "Policy Name": ["MASK_EMAIL", "MASK_PHONE", "MASK_SSN", "MASK_CREDIT_CARD", "MASK_SALARY", "MASK_ADDRESS", "MASK_DOB", "MASK_ACCOUNT_NUM"],
                "Data Type": ["VARCHAR", "VARCHAR", "VARCHAR", "VARCHAR", "NUMBER", "VARCHAR", "DATE", "VARCHAR"],
                "Masking Logic": ["****@domain.com", "***-***-1234", "***-**-1234", "****-****-****-1234", "NULL / Bucketed", "City, State only", "Year only", "****1234"],
                "Applied To": ["3 columns", "2 columns", "1 column", "2 columns", "4 columns", "5 columns", "2 columns", "3 columns"]
            })
            st.dataframe(masking_policies, use_container_width=True)
        
        with masking_col2:
            st.markdown("##### Example Masking Policy (SQL)")
            st.code("""
-- Email Masking Policy
CREATE OR REPLACE MASKING POLICY mask_email AS
(val STRING) RETURNS STRING ->
    CASE
        WHEN CURRENT_ROLE() IN ('ACCOUNTADMIN', 'SECURITYADMIN', 'DATA_ENGINEER')
        THEN val
        ELSE CONCAT('****@', SPLIT_PART(val, '@', 2))
    END;

-- Apply to column
ALTER TABLE customers MODIFY COLUMN email
    SET MASKING POLICY mask_email;
            """, language="sql")
        
        # Row-level security
        st.markdown("---")
        st.markdown("##### 🔒 Row-Level Security (Secure Views)")
        
        rls_col1, rls_col2 = st.columns(2)
        
        with rls_col1:
            rls_policies = pd.DataFrame({
                "Secure View": ["V_SUPPLIER_DATA", "V_CUSTOMER_ORDERS", "V_REGIONAL_INVENTORY", "V_TEAM_PRODUCTION"],
                "Filter Column": ["supplier_id", "customer_id", "region", "team_id"],
                "Mapping Table": ["supplier_user_mapping", "customer_user_mapping", "region_user_mapping", "team_user_mapping"],
                "Description": ["Suppliers see only their data", "Customers see only their orders", "Users see only their region", "Teams see only their production"]
            })
            st.dataframe(rls_policies, use_container_width=True)
        
        with rls_col2:
            st.markdown("##### Example Secure View (SQL)")
            st.code("""
-- Row-Level Security via Secure View
CREATE OR REPLACE SECURE VIEW v_supplier_data AS
SELECT s.*
FROM curated.supplier_data s
JOIN security.supplier_user_mapping m
    ON s.supplier_id = m.supplier_id
WHERE m.user_email = CURRENT_USER()
   OR CURRENT_ROLE() IN ('SYSADMIN', 'DATA_ENGINEER');
            """, language="sql")
        
        # Network security
        st.markdown("---")
        st.markdown("##### 🌐 Network Security Configuration")
        
        network_cols = st.columns(3)
        
        with network_cols[0]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_BLUE}15, {TELIT_BLUE}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_BLUE};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_BLUE};">🔗 AWS PrivateLink</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <strong>Status:</strong> ✅ Enabled<br>
                    <strong>Endpoint:</strong> vpce-0abc123...<br>
                    <strong>Region:</strong> us-east-1<br>
                    <strong>Benefit:</strong> No public internet exposure
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with network_cols[1]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_GREEN}15, {TELIT_GREEN}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_GREEN};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_GREEN};">📋 Network Policies</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <strong>Allowed IPs:</strong> 15 ranges<br>
                    <strong>Blocked Countries:</strong> 12<br>
                    <strong>VPN Required:</strong> Yes (external)<br>
                    <strong>IP Allowlist:</strong> Corporate + VPN
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with network_cols[2]:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_ORANGE}15, {TELIT_ORANGE}05);
                        border-radius: 10px; padding: 15px; border-top: 3px solid {TELIT_ORANGE};">
                <div style="font-size: 14px; font-weight: 700; color: {TELIT_ORANGE};">🔐 Encryption</div>
                <div style="font-size: 11px; margin-top: 10px;">
                    <strong>At Rest:</strong> AES-256<br>
                    <strong>In Transit:</strong> TLS 1.3<br>
                    <strong>Key Rotation:</strong> Annual<br>
                    <strong>Tri-Secret:</strong> Enabled
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Audit and compliance
        st.markdown("---")
        st.markdown("##### 📊 Audit & Monitoring")
        
        audit_diagram = """
        digraph G {
            rankdir=LR;
            node [shape=box, style="rounded,filled", fontname="Arial", fontsize=10];
            
            subgraph cluster_snowflake {
                label="Snowflake Account Usage";
                style=filled;
                color="#e3f2fd";
                
                AccessHist [label="ACCESS_HISTORY\\nData Access Logs", fillcolor="#90caf9"];
                LoginHist [label="LOGIN_HISTORY\\nAuthentication", fillcolor="#90caf9"];
                QueryHist [label="QUERY_HISTORY\\nAll Queries", fillcolor="#90caf9"];
                CopyHist [label="COPY_HISTORY\\nData Loading", fillcolor="#90caf9"];
                SessionHist [label="SESSIONS\\nActive Sessions", fillcolor="#90caf9"];
            }
            
            subgraph cluster_process {
                label="Processing";
                style=filled;
                color="#fff3e0";
                
                Tasks [label="Scheduled Tasks\\nHourly Aggregation", fillcolor="#ffcc80"];
                Alerts [label="Alert Conditions\\nAnomaly Detection", fillcolor="#ffcc80"];
            }
            
            subgraph cluster_output {
                label="Outputs";
                style=filled;
                color="#e8f5e9";
                
                Dashboard [label="Security Dashboard\\n(Streamlit)", fillcolor="#a5d6a7"];
                SIEM [label="SIEM\\n(Splunk)", fillcolor="#a5d6a7"];
                Slack [label="Slack Alerts\\n(PagerDuty)", fillcolor="#a5d6a7"];
                Reports [label="Compliance Reports\\n(PDF)", fillcolor="#a5d6a7"];
            }
            
            AccessHist -> Tasks;
            LoginHist -> Tasks;
            QueryHist -> Tasks;
            CopyHist -> Tasks;
            SessionHist -> Alerts;
            
            Tasks -> Dashboard;
            Tasks -> SIEM;
            Alerts -> Slack;
            Tasks -> Reports;
        }
        """
        st.graphviz_chart(audit_diagram, use_container_width=True)
        
        # Audit queries
        st.markdown("---")
        st.markdown("##### 📋 Key Audit Views")
        
        audit_views = pd.DataFrame({
            "View": ["LOGIN_HISTORY", "ACCESS_HISTORY", "QUERY_HISTORY", "DATA_TRANSFER_HISTORY", "WAREHOUSE_METERING_HISTORY", "COPY_HISTORY"],
            "Schema": ["ACCOUNT_USAGE", "ACCOUNT_USAGE", "ACCOUNT_USAGE", "ACCOUNT_USAGE", "ACCOUNT_USAGE", "ACCOUNT_USAGE"],
            "Purpose": ["Track all login attempts", "Track data access (columns/tables)", "All executed queries", "Data exports and sharing", "Compute usage and costs", "Data loading operations"],
            "Retention": ["365 days", "365 days", ["365 days"], "365 days", "365 days", "365 days"],
            "Latency": ["45 min", "3 hours", "45 min", "3 hours", "3 hours", "45 min"],
            "Key Columns": ["user_name, client_ip, error", "query_id, objects_accessed", "query_text, execution_time", "target_account, bytes", "warehouse, credits_used", "file_name, row_count"]
        })
        st.dataframe(audit_views, use_container_width=True)
        
        # Compliance certifications
        st.markdown("---")
        st.markdown("##### ✅ Compliance Certifications")
        
        cert_cols = st.columns(5)
        certifications = [
            ("SOC 2 Type II", "✅ Certified", "Annual", TELIT_GREEN),
            ("GDPR", "✅ Compliant", "Ongoing", TELIT_GREEN),
            ("ISO 27001", "✅ Certified", "Annual", TELIT_GREEN),
            ("HIPAA", "✅ BAA Available", "As needed", TELIT_BLUE),
            ("PCI DSS", "✅ Level 1", "Annual", TELIT_GREEN),
        ]
        for col, (cert, status, frequency, color) in zip(cert_cols, certifications):
            col.markdown(f"""
            <div style="background: linear-gradient(135deg, {color}15, {color}05);
                        border-radius: 10px; padding: 12px; text-align: center; border-top: 3px solid {color};">
                <div style="font-size: 12px; font-weight: 700;">{cert}</div>
                <div style="font-size: 14px; font-weight: 700; color: {color}; margin: 5px 0;">{status}</div>
                <div style="font-size: 10px; color: {TELIT_GRAY};">Audit: {frequency}</div>
            </div>
            """, unsafe_allow_html=True)
        
        # Data classification
        st.markdown("---")
        st.markdown("##### 🏷️ Data Classification Framework")
        
        class_col1, class_col2 = st.columns(2)
        
        with class_col1:
            classification = pd.DataFrame({
                "Level": ["🔴 Restricted", "🟠 Confidential", "🟡 Internal", "🟢 Public"],
                "Description": ["PII, financial data, credentials", "Business sensitive, contracts", "Internal operations data", "Marketing, public metrics"],
                "Access": ["Need-to-know only", "Authorized roles", "All employees", "Anyone"],
                "Encryption": ["AES-256 + additional", "AES-256", "AES-256", "AES-256"],
                "Masking": ["Always (external)", "Role-based", "None", "None"],
                "Examples": ["SSN, salaries, passwords", "Supplier costs, margins", "Inventory, production", "Product specs, locations"]
            })
            st.dataframe(classification, use_container_width=True)
        
        with class_col2:
            st.markdown("##### Object Tags (SQL)")
            st.code("""
-- Create classification tags
CREATE TAG data_classification
    ALLOWED_VALUES 'RESTRICTED', 'CONFIDENTIAL', 
                   'INTERNAL', 'PUBLIC';

-- Apply to sensitive table
ALTER TABLE hr.employee_salaries 
    SET TAG data_classification = 'RESTRICTED';

-- Apply to column
ALTER TABLE customers MODIFY COLUMN ssn 
    SET TAG data_classification = 'RESTRICTED';

-- Query tagged objects
SELECT * FROM snowflake.account_usage.tag_references
WHERE tag_name = 'DATA_CLASSIFICATION'
  AND tag_value = 'RESTRICTED';
            """, language="sql")
        
        # Security best practices
        st.markdown("---")
        st.markdown("##### 📋 Security Best Practices Checklist")
        
        practices_col1, practices_col2 = st.columns(2)
        
        with practices_col1:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);
                        border-radius: 10px; padding: 15px;">
                <div style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">✅ Authentication & Access</div>
                <div style="font-size: 11px; line-height: 1.8;">
                    ✅ SSO with Okta enabled<br>
                    ✅ MFA required for all users<br>
                    ✅ SCIM provisioning active<br>
                    ✅ Password policy (90-day rotation)<br>
                    ✅ Session timeout (4 hours)<br>
                    ✅ Failed login alerts configured
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);
                        border-radius: 10px; padding: 15px; margin-top: 10px;">
                <div style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">✅ Data Protection</div>
                <div style="font-size: 11px; line-height: 1.8;">
                    ✅ Encryption at rest (AES-256)<br>
                    ✅ Encryption in transit (TLS 1.3)<br>
                    ✅ Dynamic masking policies<br>
                    ✅ Row-level security views<br>
                    ✅ Object tagging enabled<br>
                    ✅ Time Travel (90 days)
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with practices_col2:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);
                        border-radius: 10px; padding: 15px;">
                <div style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">✅ Network & Infrastructure</div>
                <div style="font-size: 11px; line-height: 1.8;">
                    ✅ AWS PrivateLink enabled<br>
                    ✅ Network policies configured<br>
                    ✅ IP allowlisting active<br>
                    ✅ Geo-blocking enabled<br>
                    ✅ VPN required for external<br>
                    ✅ Separate dev/prod accounts
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #e2e8f0);
                        border-radius: 10px; padding: 15px; margin-top: 10px;">
                <div style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">✅ Monitoring & Audit</div>
                <div style="font-size: 11px; line-height: 1.8;">
                    ✅ ACCESS_HISTORY enabled<br>
                    ✅ SIEM integration (Splunk)<br>
                    ✅ Anomaly detection alerts<br>
                    ✅ Quarterly access reviews<br>
                    ✅ Annual penetration testing<br>
                    ✅ Compliance reports automated
                </div>
            </div>
            """, unsafe_allow_html=True)
