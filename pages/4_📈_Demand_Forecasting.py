"""
Telit Supply Chain - Demand Forecasting Dashboard
AI/ML-powered demand predictions for IoT modules
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

from components.styles import (
    get_telit_css, render_header, render_section_header,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_GRAY
)
from components.fake_data import get_demand_forecast, TELIT_PRODUCTS
from components.charts import create_forecast_chart

# Page config
st.set_page_config(page_title="Forecasting - Telit Supply Chain", page_icon="📈", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>📈 Demand Forecasting</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">AI-Powered Predictions</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    forecast_horizon = st.slider("Forecast Horizon (months)", 3, 24, 12)
    confidence_level = st.selectbox("Confidence Level", ["90%", "95%", "99%"], index=1)
    selected_product = st.selectbox("Product", [p['name'] for p in TELIT_PRODUCTS[:6]])

# Header
st.markdown(render_header("Demand Forecasting", "ML-powered demand predictions with confidence intervals"), unsafe_allow_html=True)

# Get data
forecast_df = get_demand_forecast(forecast_horizon)

# =============================================================================
# KPI CARDS
# =============================================================================
total_forecast = forecast_df[forecast_df['is_forecast']]['demand'].sum()
avg_growth = 12.5
forecast_accuracy = 94.2
mape = 5.8

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Forecasted Demand</div>
            <div class="kpi-value">{total_forecast/1000:.0f}K</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">Next {forecast_horizon} months</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Growth Rate</div>
            <div class="kpi-value" style="color: {TELIT_GREEN};">+{avg_growth}%</div>
            <div class="kpi-change positive">↑ YoY</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Forecast Accuracy</div>
            <div class="kpi-value">{forecast_accuracy}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">Last 6 months</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">MAPE</div>
            <div class="kpi-value">{mape}%</div>
            <div style="font-size: 12px; color: {TELIT_GRAY};">Mean Absolute % Error</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["📊 Forecast View", "🔬 Model Insights", "📋 Planning Recommendations"])

with tab1:
    st.markdown(render_section_header(f"Demand Forecast: {selected_product}"), unsafe_allow_html=True)
    
    # Filter for selected product
    product_df = forecast_df[forecast_df['product'] == selected_product].copy()
    
    # Create forecast chart
    fig = go.Figure()
    
    # Historical
    hist_df = product_df[~product_df['is_forecast']]
    fig.add_trace(go.Scatter(
        x=hist_df['date'], y=hist_df['demand'],
        mode='lines+markers',
        name='Historical',
        line=dict(color=TELIT_BLUE, width=2),
        marker=dict(size=6)
    ))
    
    # Forecast
    fore_df = product_df[product_df['is_forecast']]
    fig.add_trace(go.Scatter(
        x=fore_df['date'], y=fore_df['demand'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color=TELIT_ORANGE, width=2, dash='dot'),
        marker=dict(size=6)
    ))
    
    # Confidence band
    fig.add_trace(go.Scatter(
        x=list(fore_df['date']) + list(fore_df['date'])[::-1],
        y=list(fore_df['upper_bound']) + list(fore_df['lower_bound'])[::-1],
        fill='toself',
        fillcolor='rgba(255,107,53,0.15)',
        line=dict(color='rgba(255,107,53,0)'),
        name=f'{confidence_level} Confidence'
    ))
    
    # Add vertical line at forecast start
    fig.add_vline(x=hist_df['date'].iloc[-1], line_dash="dash", line_color=TELIT_GRAY, opacity=0.5)
    fig.add_annotation(x=hist_df['date'].iloc[-1], y=hist_df['demand'].max(),
                       text="Forecast Start", showarrow=False, yshift=10)
    
    fig.update_layout(
        height=450,
        margin=dict(l=40, r=40, t=40, b=40),
        xaxis_title="",
        yaxis_title="Demand (units)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Multi-product comparison
    st.markdown(render_section_header("Multi-Product Forecast Comparison"), unsafe_allow_html=True)
    
    fig2 = go.Figure()
    colors = [TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN, '#9c27b0', '#795548', '#607d8b']
    
    for i, product in enumerate(forecast_df['product'].unique()[:4]):
        prod_df = forecast_df[forecast_df['product'] == product]
        fig2.add_trace(go.Scatter(
            x=prod_df['date'], y=prod_df['demand'],
            mode='lines',
            name=product,
            line=dict(color=colors[i], width=2)
        ))
    
    fig2.update_layout(
        height=350,
        margin=dict(l=40, r=40, t=40, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.markdown(render_section_header("Model Performance"), unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Model accuracy over time
        months = pd.date_range(end=datetime.now(), periods=12, freq='M')
        accuracy_data = pd.DataFrame({
            'month': months,
            'accuracy': [92, 93, 91, 94, 93, 95, 94, 93, 95, 94, 95, 94]
        })
        
        fig = px.line(accuracy_data, x='month', y='accuracy',
                     title="Forecast Accuracy Trend",
                     color_discrete_sequence=[TELIT_GREEN])
        fig.update_layout(height=300, yaxis_range=[85, 100])
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Feature importance
        features = pd.DataFrame({
            'feature': ['Seasonality', 'Historical Trend', 'Economic Index', 'Market Share', 'Lead Time'],
            'importance': [28, 24, 18, 16, 14]
        })
        
        fig = px.bar(features, x='importance', y='feature', orientation='h',
                    title="Feature Importance",
                    color_discrete_sequence=[TELIT_BLUE])
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    # Seasonality decomposition
    st.markdown(render_section_header("Seasonality Analysis"), unsafe_allow_html=True)
    
    # Generate fake seasonality data
    months_of_year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    seasonality = [0.85, 0.88, 0.95, 1.02, 1.08, 1.12, 1.05, 0.98, 1.15, 1.20, 1.10, 0.92]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months_of_year, y=seasonality,
        marker_color=[TELIT_BLUE if s >= 1 else TELIT_ORANGE for s in seasonality]
    ))
    fig.add_hline(y=1, line_dash="dash", line_color=TELIT_GRAY)
    fig.update_layout(
        height=300,
        yaxis_title="Seasonal Index",
        xaxis_title="Month"
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown(render_section_header("Planning Recommendations"), unsafe_allow_html=True)
    
    # Recommendations based on forecast
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
            <div style="background: rgba(0,196,140,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_GREEN};">
                <h4 style="margin: 0 0 12px 0; color: {TELIT_DARK};">📈 Growth Products</h4>
                <p style="color: {TELIT_GRAY}; font-size: 14px;">Products with >15% forecasted growth</p>
                <ul style="margin: 12px 0; padding-left: 20px;">
                    <li><strong>FN980 5G Sub-6</strong> - +28% growth expected</li>
                    <li><strong>ME310G1 LTE Cat-M1</strong> - +22% growth expected</li>
                    <li><strong>WE310F6 Wi-Fi 6</strong> - +18% growth expected</li>
                </ul>
                <p style="font-size: 13px; color: {TELIT_GREEN};">💡 Consider increasing safety stock levels</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: rgba(255,184,0,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_ORANGE};">
                <h4 style="margin: 0 0 12px 0; color: {TELIT_DARK};">⚠️ Demand Spikes</h4>
                <p style="color: {TELIT_GRAY}; font-size: 14px;">Expected demand peaks</p>
                <ul style="margin: 12px 0; padding-left: 20px;">
                    <li><strong>Q4 2024</strong> - Holiday season surge (+35%)</li>
                    <li><strong>Q2 2025</strong> - Automotive launch cycle (+25%)</li>
                </ul>
                <p style="font-size: 13px; color: {TELIT_ORANGE};">💡 Plan production capacity in advance</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style="background: rgba(0,167,225,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid {TELIT_BLUE};">
                <h4 style="margin: 0 0 12px 0; color: {TELIT_DARK};">🏭 Production Planning</h4>
                <p style="color: {TELIT_GRAY}; font-size: 14px;">Recommended actions</p>
                <ul style="margin: 12px 0; padding-left: 20px;">
                    <li>Increase SMT Line 2 capacity by 15%</li>
                    <li>Secure additional 5G modem supply</li>
                    <li>Schedule preventive maintenance in Q1</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: rgba(103,58,183,0.1); border-radius: 12px; padding: 20px; border-left: 4px solid #673ab7;">
                <h4 style="margin: 0 0 12px 0; color: {TELIT_DARK};">📊 Inventory Optimization</h4>
                <p style="color: {TELIT_GRAY}; font-size: 14px;">Based on forecast analysis</p>
                <ul style="margin: 12px 0; padding-left: 20px;">
                    <li>Optimal safety stock: 14 days supply</li>
                    <li>Reorder point adjustment: +8%</li>
                    <li>Estimated savings: $2.1M annually</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # Export forecast data
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(render_section_header("Export Forecast Data"), unsafe_allow_html=True)
    
    export_df = forecast_df[forecast_df['is_forecast']][['date', 'product', 'demand', 'lower_bound', 'upper_bound']]
    export_df.columns = ['Date', 'Product', 'Forecast', 'Lower Bound', 'Upper Bound']
    
    st.dataframe(export_df, hide_index=True, use_container_width=True)
    
    st.download_button(
        "📥 Download Forecast CSV",
        export_df.to_csv(index=False),
        "telit_demand_forecast.csv",
        "text/csv"
    )

