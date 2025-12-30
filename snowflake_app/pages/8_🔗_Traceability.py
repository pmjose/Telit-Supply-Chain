"""
Component Traceability - Snowflake Version
"""
import streamlit as st
import pandas as pd

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Traceability", page_icon="🔗", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🔗 Component Traceability</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Track components from raw materials to delivery</p>
    </div>
""", unsafe_allow_html=True)

# Batch info
col1, col2, col3, col4 = st.columns(4)
col1.metric("Batch ID", "BATCH-2024-001")
col2.metric("Product", "ME310G1-W1")
col3.metric("Quantity", "5,000 units")
col4.metric("Test Yield", "99.74%", "↑ 0.2%")

st.markdown("---")

# Genealogy Tree SVG
st.subheader("🌳 Component Genealogy")

genealogy_svg = f"""
<svg width="100%" height="500" viewBox="0 0 900 500" style="background: #f8fafc; border-radius: 12px;">
    <!-- Raw Materials -->
    <text x="100" y="30" font-size="14" font-weight="bold" fill="{TELIT_DARK}">RAW MATERIALS</text>
    <rect x="20" y="50" width="160" height="50" rx="8" fill="{TELIT_ORANGE}20" stroke="{TELIT_ORANGE}" stroke-width="2"/>
    <text x="100" y="80" text-anchor="middle" font-size="11" fill="{TELIT_DARK}">Silicon Wafers</text>
    
    <rect x="20" y="110" width="160" height="50" rx="8" fill="{TELIT_ORANGE}20" stroke="{TELIT_ORANGE}" stroke-width="2"/>
    <text x="100" y="140" text-anchor="middle" font-size="11" fill="{TELIT_DARK}">Copper/Gold</text>
    
    <!-- Components -->
    <text x="350" y="30" font-size="14" font-weight="bold" fill="{TELIT_DARK}">COMPONENTS</text>
    <rect x="270" y="50" width="160" height="60" rx="8" fill="{TELIT_BLUE}20" stroke="{TELIT_BLUE}" stroke-width="2"/>
    <text x="350" y="75" text-anchor="middle" font-size="11" font-weight="bold" fill="{TELIT_DARK}">Qualcomm MDM9206</text>
    <text x="350" y="95" text-anchor="middle" font-size="9" fill="{TELIT_GRAY}">Lot: QC-2024-8847</text>
    
    <rect x="270" y="120" width="160" height="60" rx="8" fill="{TELIT_BLUE}20" stroke="{TELIT_BLUE}" stroke-width="2"/>
    <text x="350" y="145" text-anchor="middle" font-size="11" font-weight="bold" fill="{TELIT_DARK}">Samsung K4B4G16</text>
    <text x="350" y="165" text-anchor="middle" font-size="9" fill="{TELIT_GRAY}">Lot: SS-2024-1122</text>
    
    <rect x="270" y="190" width="160" height="60" rx="8" fill="{TELIT_BLUE}20" stroke="{TELIT_BLUE}" stroke-width="2"/>
    <text x="350" y="215" text-anchor="middle" font-size="11" font-weight="bold" fill="{TELIT_DARK}">Murata Inductors</text>
    <text x="350" y="235" text-anchor="middle" font-size="9" fill="{TELIT_GRAY}">Lot: MU-2024-3344</text>
    
    <!-- Finished Product -->
    <text x="600" y="30" font-size="14" font-weight="bold" fill="{TELIT_DARK}">FINISHED PRODUCT</text>
    <rect x="520" y="100" width="180" height="80" rx="8" fill="{TELIT_GREEN}20" stroke="{TELIT_GREEN}" stroke-width="2"/>
    <text x="610" y="130" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">ME310G1-W1</text>
    <text x="610" y="150" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">BATCH-2024-001</text>
    <text x="610" y="168" text-anchor="middle" font-size="10" fill="{TELIT_GREEN}">5,000 units</text>
    
    <!-- Customers -->
    <text x="800" y="30" font-size="14" font-weight="bold" fill="{TELIT_DARK}">CUSTOMERS</text>
    <rect x="730" y="60" width="150" height="50" rx="8" fill="#9c27b020" stroke="#9c27b0" stroke-width="2"/>
    <text x="805" y="90" text-anchor="middle" font-size="10" fill="{TELIT_DARK}">Automotive OEM Alpha</text>
    
    <rect x="730" y="120" width="150" height="50" rx="8" fill="#9c27b020" stroke="#9c27b0" stroke-width="2"/>
    <text x="805" y="150" text-anchor="middle" font-size="10" fill="{TELIT_DARK}">Fleet Management Inc</text>
    
    <!-- Arrows -->
    <line x1="180" y1="75" x2="265" y2="80" stroke="{TELIT_GRAY}" stroke-width="2" marker-end="url(#arrow)"/>
    <line x1="180" y1="135" x2="265" y2="150" stroke="{TELIT_GRAY}" stroke-width="2"/>
    <line x1="430" y1="80" x2="515" y2="130" stroke="{TELIT_GRAY}" stroke-width="2"/>
    <line x1="430" y1="150" x2="515" y2="140" stroke="{TELIT_GRAY}" stroke-width="2"/>
    <line x1="430" y1="220" x2="515" y2="150" stroke="{TELIT_GRAY}" stroke-width="2"/>
    <line x1="700" y1="130" x2="725" y2="85" stroke="{TELIT_GRAY}" stroke-width="2"/>
    <line x1="700" y1="150" x2="725" y2="145" stroke="{TELIT_GRAY}" stroke-width="2"/>
</svg>
"""
st.markdown(genealogy_svg, unsafe_allow_html=True)

# Timeline
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📅 Production Timeline")

timeline = [
    ("2024-12-10", "Raw Materials", "Components received from suppliers", TELIT_ORANGE),
    ("2024-12-12", "Incoming QC", "Quality inspection - 100% pass", TELIT_GREEN),
    ("2024-12-15", "Production", "Batch manufactured", TELIT_BLUE),
    ("2024-12-16", "Testing", "99.74% yield achieved", TELIT_GREEN),
    ("2024-12-18", "Shipment", "Shipped to 2 customers", TELIT_DARK),
]

for date, stage, desc, color in timeline:
    st.markdown(f"""
        <div style="display: flex; align-items: center; margin-bottom: 12px;">
            <div style="width: 100px; font-size: 12px; color: {TELIT_GRAY};">{date}</div>
            <div style="width: 16px; height: 16px; border-radius: 50%; background: {color}; margin-right: 16px;"></div>
            <div style="flex: 1; background: white; padding: 12px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
                <strong>{stage}</strong> - {desc}
            </div>
        </div>
    """, unsafe_allow_html=True)

# Component BOM
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📋 Bill of Materials")

bom = pd.DataFrame({
    'Component': ['Qualcomm MDM9206', 'Samsung K4B4G16', 'Murata LQH32CN', 'TDK MLZ2012'],
    'Supplier': ['Qualcomm', 'Samsung', 'Murata', 'TDK'],
    'Lot Number': ['QC-2024-8847', 'SS-2024-1122', 'MU-2024-3344', 'TDK-2024-5566'],
    'Quantity': [5000, 5000, 25000, 15000],
    'Status': ['Verified', 'Verified', 'Verified', 'Verified']
})

st.dataframe(bom, hide_index=True, use_container_width=True)

