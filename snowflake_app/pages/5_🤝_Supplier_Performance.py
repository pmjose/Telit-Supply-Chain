"""
Supplier Performance - Snowflake Version
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_GREEN = "#00C48C"
TELIT_ORANGE = "#FF6B35"
TELIT_RED = "#FF4757"
TELIT_GRAY = "#6B7C93"

st.set_page_config(page_title="Supplier Performance", page_icon="🤝", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">🤝 Supplier Performance</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Scorecards and analytics</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg On-Time", "95.8%", "↑ 2.3%")
col2.metric("Avg Quality", "97.2%", "↑ 1.1%")
col3.metric("Avg Lead Time", "24 days", "↓ 3 days")
col4.metric("Total Spend YTD", "$18.5M", "")

st.markdown("---")

# Supplier data
suppliers = pd.DataFrame({
    'Supplier': ['Taiwan Semi', 'Samsung', 'Murata', 'Qualcomm', 'Skyworks', 'TDK', 'Yageo', 'Amphenol'],
    'Category': ['Chipsets', 'Memory', 'Passives', 'Modems', 'RF', 'Inductors', 'Resistors', 'Connectors'],
    'OTD': [96.5, 97.8, 98.2, 95.5, 94.2, 97.1, 96.8, 95.9],
    'Quality': [98.2, 99.1, 99.5, 97.8, 96.5, 98.8, 97.5, 98.0],
    'LeadTime': [28, 21, 18, 35, 24, 20, 16, 22],
    'Risk': [0.25, 0.18, 0.12, 0.28, 0.22, 0.15, 0.20, 0.18],
    'Spend': [4.2, 3.8, 2.5, 3.5, 1.8, 1.2, 0.8, 0.7]
})

suppliers['Score'] = (suppliers['OTD'] * 0.3 + suppliers['Quality'] * 0.3 + 
                      (100 - suppliers['Risk'] * 100) * 0.2 + (50 - suppliers['LeadTime']) * 0.4)

# Rankings
st.subheader("🏆 Supplier Rankings")

fig = go.Figure()
colors = [TELIT_GREEN if s >= 90 else TELIT_ORANGE if s >= 80 else TELIT_RED for s in suppliers['Score']]

fig.add_trace(go.Bar(
    y=suppliers.sort_values('Score')['Supplier'],
    x=suppliers.sort_values('Score')['Score'],
    orientation='h',
    marker_color=colors,
    text=suppliers.sort_values('Score')['Score'].round(1),
    textposition='outside'
))

fig.update_layout(height=350, xaxis_range=[0, 105], xaxis_title="Overall Score")
st.plotly_chart(fig, use_container_width=True)

# Scorecards
st.subheader("📊 Supplier Scorecards")

cols = st.columns(2)
for i, (_, sup) in enumerate(suppliers.head(4).iterrows()):
    with cols[i % 2]:
        score_color = TELIT_GREEN if sup['Score'] >= 90 else TELIT_ORANGE
        st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 20px; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
                    <div>
                        <h3 style="margin: 0; color: {TELIT_DARK};">{sup['Supplier']}</h3>
                        <span style="color: {TELIT_GRAY}; font-size: 12px;">{sup['Category']}</span>
                    </div>
                    <div style="background: {score_color}; color: white; padding: 8px 16px; border-radius: 20px; font-weight: 700; font-size: 18px;">
                        {sup['Score']:.0f}
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 13px;">
                    <div>OTD: <strong>{sup['OTD']}%</strong></div>
                    <div>Quality: <strong>{sup['Quality']}%</strong></div>
                    <div>Lead Time: <strong>{sup['LeadTime']} days</strong></div>
                    <div>Risk: <strong>{'Low' if sup['Risk'] < 0.2 else 'Med'}</strong></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

# Radar chart for top supplier
st.subheader("🎯 Taiwan Semiconductor - Detailed Analysis")

categories = ['On-Time', 'Quality', 'Responsive', 'Cost', 'Risk (inv)']
values = [96.5, 98.2, 92, 88, 75]

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=values + [values[0]],
    theta=categories + [categories[0]],
    fill='toself',
    fillcolor=f'rgba(0,167,225,0.2)',
    line=dict(color=TELIT_BLUE, width=2)
))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
    showlegend=False,
    height=350
)
st.plotly_chart(fig, use_container_width=True)

