"""
Risk Intelligence - Snowflake Version
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

st.set_page_config(page_title="Risk Intelligence", page_icon="⚠️", layout="wide")

st.markdown(f"""
    <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, #0D2137 100%); padding: 32px; border-radius: 16px; margin-bottom: 24px;">
        <h1 style="color: white; margin: 0;">⚠️ Risk Intelligence</h1>
        <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0 0;">Global supply chain risk monitoring</p>
    </div>
""", unsafe_allow_html=True)

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Risks Monitored", "6")
col2.metric("High Impact", "3", delta_color="inverse")
col3.metric("Avg Risk Score", "6.6/10")
col4.metric("Critical Alerts", "2", delta_color="inverse")

# Critical alerts
st.markdown(f"""
    <div style="background: {TELIT_RED}15; border-left: 4px solid {TELIT_RED}; padding: 12px; border-radius: 0 8px 8px 0; margin-bottom: 8px;">
        🚨 <strong>[Geopolitical]</strong> Taiwan strait tensions affecting semiconductor supply - Score: 8.5
    </div>
    <div style="background: {TELIT_RED}15; border-left: 4px solid {TELIT_RED}; padding: 12px; border-radius: 0 8px 8px 0; margin-bottom: 16px;">
        🚨 <strong>[Cyber]</strong> Ransomware threat to logistics partners - Score: 7.8
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Risk heatmap
st.subheader("🗺️ Global Risk Heatmap")

regions = pd.DataFrame({
    'Region': ['North America', 'South America', 'Western Europe', 'Eastern Europe', 'Middle East', 
               'Africa', 'South Asia', 'East Asia', 'Southeast Asia', 'Oceania'],
    'lat': [40, -15, 50, 50, 25, 0, 20, 35, 5, -25],
    'lon': [-100, -60, 10, 30, 45, 20, 78, 115, 110, 135],
    'Risk': [4.2, 5.5, 5.8, 6.5, 7.2, 6.0, 5.5, 7.1, 5.8, 3.5]
})

fig = px.scatter_mapbox(regions, lat='lat', lon='lon', size=[30]*10, color='Risk',
                        hover_name='Region', 
                        color_continuous_scale=[[0, TELIT_GREEN], [0.5, TELIT_ORANGE], [1, TELIT_RED]],
                        zoom=1, mapbox_style="carto-positron")
fig.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

# Risk by category
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Risk by Category")
    categories = pd.DataFrame({
        'Category': ['Geopolitical', 'Cyber', 'Supplier', 'Natural Disaster', 'Logistics', 'Regulatory'],
        'Score': [8.5, 7.8, 7.0, 6.2, 5.8, 4.5]
    })
    colors = [TELIT_RED if s > 7 else TELIT_ORANGE if s > 5 else TELIT_GREEN for s in categories['Score']]
    
    fig = go.Figure(go.Bar(y=categories['Category'], x=categories['Score'], orientation='h',
                           marker_color=colors, text=categories['Score'], textposition='outside'))
    fig.update_layout(height=350, xaxis_range=[0, 10], xaxis_title="Risk Score")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🎯 Risk Matrix")
    risks = pd.DataFrame({
        'Risk': ['Geopolitical', 'Cyber', 'Supplier', 'Natural', 'Logistics', 'Regulatory'],
        'Probability': [0.35, 0.25, 0.20, 0.45, 0.55, 0.80],
        'Impact': [3, 3, 3, 2, 2, 1],
        'Score': [8.5, 7.8, 7.0, 6.2, 5.8, 4.5]
    })
    
    fig = go.Figure()
    for _, r in risks.iterrows():
        color = TELIT_RED if r['Score'] > 7 else TELIT_ORANGE if r['Score'] > 5 else TELIT_GREEN
        fig.add_trace(go.Scatter(x=[r['Probability']], y=[r['Impact']], mode='markers+text',
                                 marker=dict(size=r['Score']*5, color=color),
                                 text=[r['Risk'][:8]], textposition='top center', showlegend=False))
    
    fig.update_layout(height=350, xaxis_title="Probability", xaxis_range=[0, 1],
                      yaxis=dict(ticktext=['Low', 'Medium', 'High'], tickvals=[1, 2, 3], title='Impact'))
    st.plotly_chart(fig, use_container_width=True)

# Risk register
st.subheader("📋 Risk Register")

risk_data = pd.DataFrame({
    'ID': ['RSK-001', 'RSK-002', 'RSK-003', 'RSK-004', 'RSK-005', 'RSK-006'],
    'Category': ['Geopolitical', 'Natural Disaster', 'Supplier', 'Logistics', 'Regulatory', 'Cyber'],
    'Description': ['Taiwan strait tensions', 'Typhoon season Japan', 'Key supplier instability', 
                    'Port congestion Rotterdam', 'EU sustainability rules', 'Ransomware threat'],
    'Impact': ['High', 'Medium', 'High', 'Medium', 'Low', 'High'],
    'Probability': ['35%', '45%', '20%', '55%', '80%', '25%'],
    'Score': [8.5, 6.2, 7.0, 5.8, 4.5, 7.8],
    'Region': ['APAC', 'APAC', 'Global', 'EMEA', 'EMEA', 'Global']
})

st.dataframe(risk_data, column_config={
    "Score": st.column_config.ProgressColumn("Score", min_value=0, max_value=10)
}, hide_index=True, use_container_width=True)

