"""
Digital Twin - Smart Factory Dashboard (Snowflake Version)
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Digital Twin", page_icon="🏭", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🏭 Digital Twin - Smart Factory</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Real-time factory floor visualization</p>
    </div>
""", unsafe_allow_html=True)

# Factory KPIs
cols = st.columns(6)
kpis = [("OEE", "87.3%", TELIT_GREEN), ("Throughput", "12,450", TELIT_GREEN), 
        ("Quality", "98.7%", TELIT_GREEN), ("Availability", "92.1%", TELIT_ORANGE),
        ("Workers", "47/50", TELIT_GREEN), ("Energy", "1,247 kWh", TELIT_BLUE)]

for col, (label, value, color) in zip(cols, kpis):
    with col:
        st.markdown(f"""
            <div style="background: white; border-radius: 10px; padding: 12px; text-align: center; 
                        box-shadow: 0 2px 8px rgba(0,0,0,0.06); border-top: 3px solid {color};">
                <div style="font-size: 11px; color: {TELIT_GRAY}; text-transform: uppercase;">{label}</div>
                <div style="font-size: 20px; font-weight: 700; color: {TELIT_DARK};">{value}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Factory Floor SVG
st.subheader("🗺️ Factory Floor Layout")

factory_svg = f"""
<svg width="100%" height="400" viewBox="0 0 800 400" style="background: #f8fafc; border-radius: 12px;">
    <!-- Receiving -->
    <rect x="20" y="20" width="150" height="80" rx="8" fill="{TELIT_GREEN}20" stroke="{TELIT_GREEN}" stroke-width="2"/>
    <text x="95" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">RECEIVING</text>
    <text x="95" y="70" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">3 Docks Active</text>
    
    <!-- SMT Line 1 -->
    <rect x="200" y="20" width="180" height="80" rx="8" fill="{TELIT_GREEN}20" stroke="{TELIT_GREEN}" stroke-width="2"/>
    <text x="290" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">SMT LINE 1</text>
    <text x="290" y="70" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">847 units/hr | 98%</text>
    
    <!-- SMT Line 2 -->
    <rect x="410" y="20" width="180" height="80" rx="8" fill="{TELIT_ORANGE}20" stroke="{TELIT_ORANGE}" stroke-width="2"/>
    <text x="500" y="50" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">SMT LINE 2</text>
    <text x="500" y="70" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">792 units/hr | 94%</text>
    
    <!-- Warehouse -->
    <rect x="20" y="130" width="150" height="100" rx="8" fill="{TELIT_BLUE}20" stroke="{TELIT_BLUE}" stroke-width="2"/>
    <text x="95" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">WAREHOUSE</text>
    <text x="95" y="185" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">45,000 units</text>
    <text x="95" y="205" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">78% capacity</text>
    
    <!-- Testing -->
    <rect x="200" y="130" width="180" height="100" rx="8" fill="{TELIT_GREEN}20" stroke="{TELIT_GREEN}" stroke-width="2"/>
    <text x="290" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">TESTING</text>
    <text x="290" y="185" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">4 Stations Active</text>
    <text x="290" y="205" text-anchor="middle" font-size="10" fill="{TELIT_GREEN}">98.7% Pass Rate</text>
    
    <!-- Packaging -->
    <rect x="410" y="130" width="180" height="100" rx="8" fill="{TELIT_GREEN}20" stroke="{TELIT_GREEN}" stroke-width="2"/>
    <text x="500" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">PACKAGING</text>
    <text x="500" y="185" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">2 Lines Running</text>
    <text x="500" y="205" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">2,340 units/hr</text>
    
    <!-- Quality Lab -->
    <rect x="200" y="260" width="180" height="80" rx="8" fill="{TELIT_ORANGE}20" stroke="{TELIT_ORANGE}" stroke-width="2"/>
    <text x="290" y="290" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">QUALITY LAB</text>
    <text x="290" y="310" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">24 Samples Pending</text>
    
    <!-- Shipping -->
    <rect x="410" y="260" width="180" height="80" rx="8" fill="{TELIT_GREEN}20" stroke="{TELIT_GREEN}" stroke-width="2"/>
    <text x="500" y="290" text-anchor="middle" font-size="12" font-weight="bold" fill="{TELIT_DARK}">SHIPPING</text>
    <text x="500" y="310" text-anchor="middle" font-size="10" fill="{TELIT_GRAY}">2 Trucks Loading</text>
    
    <!-- Flow Arrows -->
    <defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
        <polygon points="0 0, 10 3.5, 0 7" fill="{TELIT_BLUE}"/></marker></defs>
    <line x1="170" y1="60" x2="195" y2="60" stroke="{TELIT_BLUE}" stroke-width="2" marker-end="url(#arrow)"/>
    <line x1="380" y1="60" x2="405" y2="60" stroke="{TELIT_BLUE}" stroke-width="2" marker-end="url(#arrow)"/>
    <line x1="290" y1="100" x2="290" y2="125" stroke="{TELIT_BLUE}" stroke-width="2" marker-end="url(#arrow)"/>
    <line x1="500" y1="100" x2="500" y2="125" stroke="{TELIT_BLUE}" stroke-width="2" marker-end="url(#arrow)"/>
    
    <!-- Legend -->
    <rect x="620" y="20" width="160" height="120" rx="8" fill="white" stroke="#e9ecef"/>
    <text x="700" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="{TELIT_DARK}">STATUS</text>
    <circle cx="640" cy="65" r="6" fill="{TELIT_GREEN}"/><text x="655" y="69" font-size="10" fill="{TELIT_DARK}">Running</text>
    <circle cx="640" cy="85" r="6" fill="{TELIT_ORANGE}"/><text x="655" y="89" font-size="10" fill="{TELIT_DARK}">Warning</text>
    <circle cx="640" cy="105" r="6" fill="{TELIT_RED}"/><text x="655" y="109" font-size="10" fill="{TELIT_DARK}">Critical</text>
    <circle cx="640" cy="125" r="6" fill="{TELIT_GRAY}"/><text x="655" y="129" font-size="10" fill="{TELIT_DARK}">Idle</text>
</svg>
"""
st.markdown(factory_svg, unsafe_allow_html=True)

# Equipment Health
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("⚙️ Equipment Health")

equipment = pd.DataFrame({
    'Equipment': ['SMT Line 1', 'SMT Line 2', 'Reflow Oven', 'AOI Station 1', 'AOI Station 2', 'Tester 1'],
    'Health': [92.5, 78.3, 95.1, 88.7, 65.2, 91.8],
    'Status': ['Good', 'Warning', 'Good', 'Good', 'Critical', 'Good']
})

for _, row in equipment.iterrows():
    color = TELIT_GREEN if row['Status'] == 'Good' else TELIT_ORANGE if row['Status'] == 'Warning' else TELIT_RED
    st.markdown(f"""
        <div style="display: flex; align-items: center; padding: 10px; background: white; border-radius: 8px; margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.05);">
            <div style="width: 200px; font-weight: 600;">{row['Equipment']}</div>
            <div style="flex: 1; background: #e9ecef; height: 8px; border-radius: 4px; margin: 0 16px;">
                <div style="width: {row['Health']}%; background: {color}; height: 100%; border-radius: 4px;"></div>
            </div>
            <div style="width: 60px; text-align: right; font-weight: 600; color: {color};">{row['Health']}%</div>
            <div style="width: 80px; text-align: right;"><span style="background: {color}20; color: {color}; padding: 2px 8px; border-radius: 10px; font-size: 11px;">{row['Status']}</span></div>
        </div>
    """, unsafe_allow_html=True)

