"""
Telit Supply Chain Intelligence Platform
Homepage - Use Case Overview
"""

import streamlit as st
from components.styles import (
    get_telit_css, TELIT_LOGO_SVG,
    TELIT_BLUE, TELIT_DARK, TELIT_NAVY, TELIT_ORANGE, TELIT_GREEN, TELIT_GRAY
)

# Page configuration
st.set_page_config(
    page_title="Telit Supply Chain Intelligence",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Additional homepage styles
st.markdown("""
<style>
    .hero-section {
        background: linear-gradient(135deg, #1E3A5F 0%, #0D2137 50%, #1E3A5F 100%);
        padding: 60px 40px;
        border-radius: 24px;
        margin-bottom: 40px;
        position: relative;
        overflow: hidden;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -100px;
        right: -100px;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle, rgba(0,167,225,0.3) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        bottom: -150px;
        left: -100px;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(255,107,53,0.2) 0%, transparent 70%);
        border-radius: 50%;
    }
    
    .use-case-card {
        background: white;
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid #e9ecef;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .use-case-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 40px rgba(0,167,225,0.15);
        border-color: #00A7E1;
    }
    
    .use-case-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        margin-bottom: 16px;
    }
    
    .snowflake-benefit {
        background: linear-gradient(135deg, #29B5E8 0%, #00A3E0 100%);
        border-radius: 16px;
        padding: 24px;
        color: white;
    }
    
    .data-source-tag {
        display: inline-block;
        background: #f0f9ff;
        color: #0284c7;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11px;
        margin: 2px;
        font-weight: 500;
    }
    
    .architecture-box {
        background: #f8fafc;
        border: 2px dashed #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# SIDEBAR
# =============================================================================
with st.sidebar:
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
    
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px; margin-bottom: 20px;">
            <div style="color: white; font-size: 13px;">
                <strong>🏠 Home</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Use Case Overview</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Snowflake badge
    st.markdown("<br>" * 2, unsafe_allow_html=True)
    st.markdown("""
        <div style="background: linear-gradient(135deg, #29B5E8 0%, #00A3E0 100%); color: white; padding: 12px; border-radius: 12px; text-align: center;">
            <div style="font-size: 24px; margin-bottom: 4px;">❄️</div>
            <div style="font-size: 12px; font-weight: 600;">Powered by Snowflake</div>
            <div style="font-size: 10px; opacity: 0.8;">Data Cloud Platform</div>
        </div>
    """, unsafe_allow_html=True)

# =============================================================================
# HERO SECTION
# =============================================================================
st.markdown(f"""
    <div class="hero-section">
        <div style="position: relative; z-index: 1;">
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 24px;">
                <div style="font-size: 48px;">❄️</div>
                <div>
                    <h1 style="color: white; margin: 0; font-size: 2.5rem; font-weight: 700;">
                        Supply Chain Intelligence Platform
                    </h1>
                    <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0; font-size: 1.1rem;">
                        Powered by Snowflake Data Cloud | Built for Telit Cinterion
                    </p>
                </div>
            </div>
            
            <p style="color: rgba(255,255,255,0.9); font-size: 1rem; max-width: 800px; line-height: 1.6;">
                Transform your supply chain operations with real-time visibility, AI-powered insights, and unified data. 
                This platform demonstrates how Snowflake enables end-to-end supply chain intelligence for IoT manufacturing.
            </p>
            
            <div style="display: flex; gap: 16px; margin-top: 32px; flex-wrap: wrap;">
                <div style="background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); padding: 16px 24px; border-radius: 12px; text-align: center;">
                    <div style="color: white; font-size: 28px; font-weight: 700;">12</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px;">Use Cases</div>
                </div>
                <div style="background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); padding: 16px 24px; border-radius: 12px; text-align: center;">
                    <div style="color: white; font-size: 28px; font-weight: 700;">50+</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px;">Data Sources</div>
                </div>
                <div style="background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); padding: 16px 24px; border-radius: 12px; text-align: center;">
                    <div style="color: white; font-size: 28px; font-weight: 700;">Real-time</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px;">Analytics</div>
                </div>
                <div style="background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); padding: 16px 24px; border-radius: 12px; text-align: center;">
                    <div style="color: white; font-size: 28px; font-weight: 700;">AI/ML</div>
                    <div style="color: rgba(255,255,255,0.8); font-size: 12px;">Powered</div>
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# =============================================================================
# WHY SNOWFLAKE SECTION
# =============================================================================
st.markdown(f"""
    <h2 style="color: {TELIT_DARK}; margin-bottom: 24px; display: flex; align-items: center; gap: 12px;">
        <span style="font-size: 32px;">❄️</span> Why Snowflake for Supply Chain?
    </h2>
""", unsafe_allow_html=True)

benefit_col1, benefit_col2, benefit_col3, benefit_col4 = st.columns(4)

benefits = [
    {
        "icon": "🔗",
        "title": "Unified Data",
        "desc": "Single source of truth for all supply chain data - ERP, IoT, logistics, suppliers"
    },
    {
        "icon": "⚡",
        "title": "Real-time Analytics",
        "desc": "Stream processing with Snowpipe for live dashboards and instant insights"
    },
    {
        "icon": "🤖",
        "title": "AI/ML Ready",
        "desc": "Native Snowpark for Python ML models, demand forecasting, anomaly detection"
    },
    {
        "icon": "🔒",
        "title": "Secure Sharing",
        "desc": "Share data with suppliers and partners via Snowflake Data Sharing"
    }
]

for col, benefit in zip([benefit_col1, benefit_col2, benefit_col3, benefit_col4], benefits):
    with col:
        st.markdown(f"""
            <div class="snowflake-benefit">
                <div style="font-size: 32px; margin-bottom: 12px;">{benefit['icon']}</div>
                <h4 style="margin: 0 0 8px 0; font-size: 16px;">{benefit['title']}</h4>
                <p style="margin: 0; font-size: 13px; opacity: 0.9;">{benefit['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# USE CASES SECTION
# =============================================================================
st.markdown(f"""
    <h2 style="color: {TELIT_DARK}; margin: 40px 0 24px 0;">
        📊 Supply Chain Use Cases
    </h2>
    <p style="color: {TELIT_GRAY}; margin-bottom: 32px; font-size: 16px;">
        Click on the sidebar to explore each use case dashboard. Each dashboard demonstrates real-world applications of Snowflake for supply chain optimization.
    </p>
""", unsafe_allow_html=True)

# Use cases data
use_cases = [
    {
        "icon": "📊",
        "title": "Executive Dashboard",
        "color": TELIT_DARK,
        "page": "0_📊_Executive_Dashboard",
        "desc": "Real-time KPIs and global operations overview for C-level executives",
        "data_sources": ["SAP ERP", "Oracle", "IoT Sensors", "CRM", "Financial Systems"],
        "snowflake_value": "Unified view across all enterprise systems with sub-second query performance on petabytes of data"
    },
    {
        "icon": "🏭",
        "title": "Digital Twin",
        "color": "#9c27b0",
        "page": "1_🏭_Digital_Twin",
        "desc": "Interactive factory floor visualization with real-time equipment status and sensor data",
        "data_sources": ["IoT Sensors", "PLC/SCADA", "MES", "Equipment APIs", "Temperature/Humidity Sensors"],
        "snowflake_value": "Snowpipe streaming ingestion handles millions of sensor readings per second with real-time transformations"
    },
    {
        "icon": "📦",
        "title": "Inventory Management",
        "color": TELIT_ORANGE,
        "page": "2_📦_Inventory",
        "desc": "Real-time stock levels, warehouse distribution, and automated reorder alerts",
        "data_sources": ["WMS", "ERP Inventory", "Barcode/RFID", "Supplier Portals"],
        "snowflake_value": "Time Travel for inventory audits, zero-copy clones for what-if analysis"
    },
    {
        "icon": "🚚",
        "title": "Supply Chain Visibility",
        "color": TELIT_BLUE,
        "page": "3_🚚_Supply_Chain_Visibility",
        "desc": "End-to-end shipment tracking from suppliers to customers with live GPS data",
        "data_sources": ["GPS Trackers", "Carrier APIs", "Customs Data", "Port Systems", "Weather APIs"],
        "snowflake_value": "Geospatial functions for route optimization, external data marketplace for weather/traffic"
    },
    {
        "icon": "📈",
        "title": "Demand Forecasting",
        "color": TELIT_GREEN,
        "page": "4_📈_Demand_Forecasting",
        "desc": "AI/ML-powered demand predictions with confidence intervals and seasonality analysis",
        "data_sources": ["Historical Sales", "Market Data", "Economic Indicators", "Promotional Calendars"],
        "snowflake_value": "Snowpark ML for Python-based forecasting models running directly on Snowflake compute"
    },
    {
        "icon": "🤝",
        "title": "Supplier Performance",
        "color": "#795548",
        "page": "5_🤝_Supplier_Performance",
        "desc": "Supplier scorecards, quality metrics, and risk assessment dashboards",
        "data_sources": ["Supplier Portals", "Quality Systems", "AP/Procurement", "Third-party Risk Data"],
        "snowflake_value": "Secure Data Sharing with suppliers for collaborative performance improvement"
    },
    {
        "icon": "✅",
        "title": "Quality Control",
        "color": "#e91e63",
        "page": "6_✅_Quality_Control",
        "desc": "SPC control charts, defect analytics, and root cause analysis",
        "data_sources": ["QMS", "Inspection Systems", "AOI/Test Equipment", "Customer Returns"],
        "snowflake_value": "Statistical functions and ML-based anomaly detection for quality prediction"
    },
    {
        "icon": "🚛",
        "title": "Logistics & Fleet",
        "color": "#ff5722",
        "page": "7_🚛_Logistics",
        "desc": "Real-time fleet tracking, delivery performance, and route optimization",
        "data_sources": ["Fleet Telematics", "TMS", "Driver Apps", "Fuel Systems"],
        "snowflake_value": "Streaming data from vehicle IoT with geospatial analytics for route planning"
    },
    {
        "icon": "🔗",
        "title": "Component Traceability",
        "color": "#607d8b",
        "page": "8_🔗_Traceability",
        "desc": "Full genealogy from raw materials to finished products with recall simulation",
        "data_sources": ["MES", "Serialization Systems", "Supplier Lots", "Customer Shipments"],
        "snowflake_value": "Graph-like queries for lineage tracing, immutable audit trail with Time Travel"
    },
    {
        "icon": "🌱",
        "title": "Carbon & ESG",
        "color": TELIT_GREEN,
        "page": "9_🌱_Carbon_ESG",
        "desc": "Carbon footprint tracking, sustainability metrics, and ESG reporting",
        "data_sources": ["Energy Meters", "Emissions Calculators", "Waste Management", "Carbon APIs"],
        "snowflake_value": "Snowflake Marketplace for carbon factor databases, automated ESG reporting"
    },
    {
        "icon": "🔧",
        "title": "Predictive Maintenance",
        "color": "#ff9800",
        "page": "10_🔧_Predictive_Maintenance",
        "desc": "Equipment health monitoring, failure prediction, and maintenance optimization",
        "data_sources": ["Vibration Sensors", "Temperature Monitors", "CMMS", "Equipment Logs"],
        "snowflake_value": "Snowpark ML for failure prediction models, real-time streaming for sensor data"
    },
    {
        "icon": "⚠️",
        "title": "Risk Intelligence",
        "color": "#f44336",
        "page": "11_⚠️_Risk_Intelligence",
        "desc": "Global supply chain risk monitoring, scenario planning, and disruption alerts",
        "data_sources": ["News APIs", "Geopolitical Data", "Weather Services", "Financial Risk Scores"],
        "snowflake_value": "External data marketplace for risk feeds, ML-based risk scoring models"
    }
]

# Display use cases in a 3-column grid
for i in range(0, len(use_cases), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(use_cases):
            uc = use_cases[i + j]
            with col:
                # Data source tags
                data_tags = "".join([f'<span class="data-source-tag">{ds}</span>' for ds in uc['data_sources'][:4]])
                if len(uc['data_sources']) > 4:
                    data_tags += f'<span class="data-source-tag">+{len(uc["data_sources"])-4} more</span>'
                
                st.markdown(f"""
                    <div class="use-case-card">
                        <div class="use-case-icon" style="background: {uc['color']}20;">
                            <span>{uc['icon']}</span>
                        </div>
                        <h3 style="margin: 0 0 8px 0; color: {TELIT_DARK}; font-size: 18px;">{uc['title']}</h3>
                        <p style="color: {TELIT_GRAY}; font-size: 13px; margin-bottom: 16px; min-height: 40px;">{uc['desc']}</p>
                        
                        <div style="margin-bottom: 16px;">
                            <div style="font-size: 11px; color: {TELIT_DARK}; font-weight: 600; margin-bottom: 6px;">DATA SOURCES</div>
                            {data_tags}
                        </div>
                        
                        <div style="background: #f0f9ff; border-radius: 8px; padding: 12px; border-left: 3px solid #29B5E8;">
                            <div style="font-size: 11px; color: #0284c7; font-weight: 600; margin-bottom: 4px;">❄️ SNOWFLAKE VALUE</div>
                            <div style="font-size: 12px; color: {TELIT_DARK};">{uc['snowflake_value']}</div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# ARCHITECTURE SECTION
# =============================================================================
st.markdown(f"""
    <h2 style="color: {TELIT_DARK}; margin: 40px 0 24px 0;">
        🏗️ Solution Architecture
    </h2>
""", unsafe_allow_html=True)

st.markdown(f"""
    <div style="background: white; border-radius: 16px; padding: 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <div style="display: grid; grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr; gap: 16px; align-items: center; text-align: center;">
            
            <!-- Data Sources -->
            <div class="architecture-box">
                <div style="font-size: 24px; margin-bottom: 8px;">📥</div>
                <div style="font-weight: 600; color: {TELIT_DARK}; font-size: 14px;">Data Sources</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 8px;">
                    ERP • MES • IoT<br>
                    WMS • TMS • APIs
                </div>
            </div>
            
            <div style="font-size: 24px; color: {TELIT_BLUE};">→</div>
            
            <!-- Ingestion -->
            <div class="architecture-box" style="background: #e3f2fd; border-color: {TELIT_BLUE};">
                <div style="font-size: 24px; margin-bottom: 8px;">⚡</div>
                <div style="font-weight: 600; color: {TELIT_DARK}; font-size: 14px;">Ingestion</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 8px;">
                    Snowpipe<br>
                    Kafka Connector<br>
                    File Loading
                </div>
            </div>
            
            <div style="font-size: 24px; color: {TELIT_BLUE};">→</div>
            
            <!-- Snowflake -->
            <div style="background: linear-gradient(135deg, #29B5E8 0%, #00A3E0 100%); border-radius: 12px; padding: 20px; color: white;">
                <div style="font-size: 32px; margin-bottom: 8px;">❄️</div>
                <div style="font-weight: 700; font-size: 16px;">Snowflake</div>
                <div style="font-size: 11px; opacity: 0.9; margin-top: 8px;">
                    Data Warehouse<br>
                    Snowpark ML<br>
                    Data Sharing<br>
                    Marketplace
                </div>
            </div>
            
            <div style="font-size: 24px; color: {TELIT_BLUE};">→</div>
            
            <!-- Visualization -->
            <div class="architecture-box" style="background: #e8f5e9; border-color: {TELIT_GREEN};">
                <div style="font-size: 24px; margin-bottom: 8px;">📊</div>
                <div style="font-weight: 600; color: {TELIT_DARK}; font-size: 14px;">Visualization</div>
                <div style="font-size: 11px; color: {TELIT_GRAY}; margin-top: 8px;">
                    Streamlit<br>
                    Tableau / PowerBI<br>
                    Custom Apps
                </div>
            </div>
        </div>
        
        <div style="margin-top: 32px; text-align: center; padding-top: 24px; border-top: 1px solid #e9ecef;">
            <div style="font-size: 14px; color: {TELIT_DARK}; font-weight: 600; margin-bottom: 12px;">Key Snowflake Capabilities Used</div>
            <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;">
                <span style="background: #e3f2fd; color: #1565c0; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 500;">Snowpipe Streaming</span>
                <span style="background: #e8f5e9; color: #2e7d32; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 500;">Snowpark Python</span>
                <span style="background: #fff3e0; color: #ef6c00; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 500;">Time Travel</span>
                <span style="background: #f3e5f5; color: #7b1fa2; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 500;">Data Sharing</span>
                <span style="background: #fce4ec; color: #c2185b; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 500;">Geospatial</span>
                <span style="background: #e0f2f1; color: #00695c; padding: 6px 14px; border-radius: 20px; font-size: 12px; font-weight: 500;">Marketplace</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# =============================================================================
# CTA SECTION
# =============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_NAVY} 100%); border-radius: 20px; padding: 48px; text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: radial-gradient(circle, rgba(0,167,225,0.3) 0%, transparent 70%); border-radius: 50%;"></div>
        <div style="position: relative; z-index: 1;">
            <h2 style="color: white; margin: 0 0 16px 0; font-size: 2rem;">Ready to Explore?</h2>
            <p style="color: rgba(255,255,255,0.8); margin: 0 0 24px 0; font-size: 1.1rem;">
                Navigate to any dashboard using the sidebar to see detailed analytics and visualizations.
            </p>
            <div style="display: inline-flex; align-items: center; gap: 12px; background: {TELIT_BLUE}; color: white; padding: 14px 28px; border-radius: 12px; font-weight: 600;">
                <span>👈</span>
                <span>Start with the Executive Dashboard</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; padding: 24px; border-top: 1px solid #e9ecef; color: {TELIT_GRAY}; font-size: 12px;">
        <div style="display: flex; justify-content: center; align-items: center; gap: 24px; margin-bottom: 12px;">
            <span>Built with ❄️ Snowflake</span>
            <span>•</span>
            <span>Powered by 🎈 Streamlit</span>
            <span>•</span>
            <span>Designed for Telit Cinterion</span>
        </div>
        <div>© 2024 Telit Supply Chain Intelligence Platform | Demo Application</div>
    </div>
""", unsafe_allow_html=True)
