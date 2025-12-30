"""
Telit Supply Chain - Supplier Performance Dashboard
Supplier scorecards and performance analytics
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from components.styles import (
    get_telit_css, render_header, render_section_header,
    TELIT_LOGO_SVG, TELIT_BLUE, TELIT_DARK, TELIT_ORANGE, TELIT_GREEN, TELIT_YELLOW, TELIT_RED, TELIT_GRAY
)
from components.fake_data import get_supplier_performance, SUPPLIERS
from components.charts import create_radar_chart, create_bar_chart

# Page config
st.set_page_config(page_title="Suppliers - Telit Supply Chain", page_icon="🤝", layout="wide")
st.markdown(get_telit_css(), unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown(f'<div style="padding: 20px 0; text-align: center; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 20px;">{TELIT_LOGO_SVG}</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(0,167,225,0.2); border-radius: 8px; padding: 12px;">
            <div style="color: white; font-size: 13px;">
                <strong>🤝 Supplier Performance</strong><br>
                <span style="opacity: 0.8; font-size: 11px;">Scorecards & Analytics</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    tier_filter = st.multiselect("Filter by Tier", [1, 2], default=[1, 2])
    category_filter = st.multiselect("Filter by Category", list(set([s['category'] for s in SUPPLIERS])))

# Header
st.markdown(render_header("Supplier Performance", "Comprehensive supplier scorecards and analytics"), unsafe_allow_html=True)

# Get data
supplier_df = get_supplier_performance()

# Apply filters
if tier_filter:
    supplier_df = supplier_df[supplier_df['tier'].isin(tier_filter)]
if category_filter:
    supplier_df = supplier_df[supplier_df['category'].isin(category_filter)]

# =============================================================================
# KPI CARDS
# =============================================================================
avg_otd = supplier_df['on_time_delivery'].mean()
avg_quality = supplier_df['quality_score'].mean()
avg_lead_time = supplier_df['lead_time_days'].mean()
total_spend = supplier_df['spend_ytd'].sum()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg On-Time Delivery</div>
            <div class="kpi-value">{avg_otd:.1f}%</div>
            <div class="kpi-change positive">↑ 2.3% vs target</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Quality Score</div>
            <div class="kpi-value">{avg_quality:.1f}%</div>
            <div class="kpi-change positive">↑ 1.1% YoY</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Avg Lead Time</div>
            <div class="kpi-value">{avg_lead_time:.0f} days</div>
            <div class="kpi-change positive">↓ 3 days vs last year</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Total Spend YTD</div>
            <div class="kpi-value">${total_spend/1000000:.1f}M</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =============================================================================
# TABS
# =============================================================================
tab1, tab2, tab3 = st.tabs(["📊 Scorecard Overview", "🏆 Supplier Rankings", "📈 Detailed Analysis"])

with tab1:
    st.markdown(render_section_header("Supplier Scorecards"), unsafe_allow_html=True)
    
    # Create scorecard grid
    cols = st.columns(2)
    
    for idx, (_, supplier) in enumerate(supplier_df.iterrows()):
        with cols[idx % 2]:
            # Calculate overall score
            overall = (supplier['on_time_delivery'] * 0.3 + 
                      supplier['quality_score'] * 0.3 + 
                      supplier['responsiveness'] * 0.2 +
                      (100 - supplier['risk_score'] * 100) * 0.2)
            
            score_color = TELIT_GREEN if overall >= 90 else TELIT_YELLOW if overall >= 80 else TELIT_RED
            tier_badge = f"Tier {int(supplier['tier'])}"
            
            st.markdown(f"""
                <div style="background: white; border-radius: 16px; padding: 20px; margin-bottom: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.06);">
                    <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 16px;">
                        <div>
                            <h3 style="margin: 0; color: {TELIT_DARK}; font-size: 18px;">{supplier['name']}</h3>
                            <span style="font-size: 12px; color: {TELIT_GRAY};">{supplier['category']} | {supplier['country']}</span>
                        </div>
                        <div style="text-align: right;">
                            <span style="background: {score_color}; color: white; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 18px;">{overall:.0f}</span>
                            <br><span style="background: {TELIT_DARK}; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; margin-top: 4px; display: inline-block;">{tier_badge}</span>
                        </div>
                    </div>
                    
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
                        <div>
                            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-bottom: 4px;">ON-TIME DELIVERY</div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <div style="flex: 1; background: #e9ecef; height: 6px; border-radius: 3px;">
                                    <div style="width: {supplier['on_time_delivery']}%; background: {TELIT_GREEN if supplier['on_time_delivery'] >= 95 else TELIT_YELLOW}; height: 100%; border-radius: 3px;"></div>
                                </div>
                                <span style="font-weight: 600; font-size: 13px;">{supplier['on_time_delivery']:.1f}%</span>
                            </div>
                        </div>
                        <div>
                            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-bottom: 4px;">QUALITY SCORE</div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <div style="flex: 1; background: #e9ecef; height: 6px; border-radius: 3px;">
                                    <div style="width: {supplier['quality_score']}%; background: {TELIT_GREEN if supplier['quality_score'] >= 95 else TELIT_YELLOW}; height: 100%; border-radius: 3px;"></div>
                                </div>
                                <span style="font-weight: 600; font-size: 13px;">{supplier['quality_score']:.1f}%</span>
                            </div>
                        </div>
                        <div>
                            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-bottom: 4px;">LEAD TIME</div>
                            <span style="font-weight: 600; font-size: 13px;">{supplier['lead_time_days']} days</span>
                        </div>
                        <div>
                            <div style="font-size: 11px; color: {TELIT_GRAY}; margin-bottom: 4px;">RISK LEVEL</div>
                            <span style="font-weight: 600; font-size: 13px; color: {TELIT_GREEN if supplier['risk_score'] < 0.2 else TELIT_YELLOW if supplier['risk_score'] < 0.3 else TELIT_RED};">
                                {'Low' if supplier['risk_score'] < 0.2 else 'Medium' if supplier['risk_score'] < 0.3 else 'High'}
                            </span>
                        </div>
                    </div>
                    
                    <div style="margin-top: 12px; padding-top: 12px; border-top: 1px solid #e9ecef; display: flex; justify-content: space-between;">
                        <span style="font-size: 12px; color: {TELIT_GRAY};">YTD Spend: <strong>${supplier['spend_ytd']/1000000:.1f}M</strong></span>
                        <span style="font-size: 12px; color: {TELIT_GRAY};">Orders: <strong>{supplier['orders_ytd']}</strong></span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown(render_section_header("Supplier Rankings"), unsafe_allow_html=True)
    
    # Calculate overall scores and rank
    supplier_df['overall_score'] = (
        supplier_df['on_time_delivery'] * 0.3 + 
        supplier_df['quality_score'] * 0.3 + 
        supplier_df['responsiveness'] * 0.2 +
        (100 - supplier_df['risk_score'] * 100) * 0.2
    )
    ranked_df = supplier_df.sort_values('overall_score', ascending=False)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig = go.Figure()
        
        colors = [TELIT_GREEN if s >= 90 else TELIT_YELLOW if s >= 80 else TELIT_RED 
                  for s in ranked_df['overall_score']]
        
        fig.add_trace(go.Bar(
            x=ranked_df['overall_score'],
            y=ranked_df['name'],
            orientation='h',
            marker_color=colors,
            text=ranked_df['overall_score'].round(1),
            textposition='outside'
        ))
        
        fig.update_layout(
            height=400,
            xaxis_title="Overall Score",
            yaxis_title="",
            xaxis_range=[0, 105],
            margin=dict(l=0, r=40, t=20, b=40)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_DARK}ee 100%); border-radius: 12px; padding: 20px; color: white;">
                <h4 style="margin: 0 0 16px 0;">🏆 Top Performers</h4>
        """, unsafe_allow_html=True)
        
        for i, (_, sup) in enumerate(ranked_df.head(3).iterrows()):
            medal = ["🥇", "🥈", "🥉"][i]
            st.markdown(f"""
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <span style="font-size: 24px;">{medal}</span>
                    <div>
                        <div style="font-weight: 600;">{sup['name']}</div>
                        <div style="font-size: 12px; opacity: 0.8;">Score: {sup['overall_score']:.1f}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown(render_section_header("Radar Analysis"), unsafe_allow_html=True)
    
    selected_suppliers = st.multiselect(
        "Select suppliers to compare",
        options=supplier_df['name'].tolist(),
        default=supplier_df['name'].tolist()[:2]
    )
    
    if selected_suppliers:
        col1, col2 = st.columns(2)
        
        for i, sup_name in enumerate(selected_suppliers[:2]):
            sup_data = supplier_df[supplier_df['name'] == sup_name].iloc[0]
            
            categories = ['On-Time\nDelivery', 'Quality', 'Responsiveness', 'Cost\nEfficiency', 'Risk\n(Inverse)']
            values = [
                sup_data['on_time_delivery'],
                sup_data['quality_score'],
                sup_data['responsiveness'],
                100 - abs(sup_data['cost_variance']) * 5,
                100 - sup_data['risk_score'] * 100
            ]
            
            with [col1, col2][i]:
                fig = create_radar_chart(categories, values, sup_name)
                st.plotly_chart(fig, use_container_width=True)
    
    # Performance trends
    st.markdown(render_section_header("Performance Trends"), unsafe_allow_html=True)
    
    import numpy as np
    from datetime import datetime, timedelta
    
    months = pd.date_range(end=datetime.now(), periods=12, freq='M')
    trend_data = []
    
    for sup in supplier_df['name'].tolist()[:4]:
        base_otd = supplier_df[supplier_df['name'] == sup]['on_time_delivery'].values[0]
        for m in months:
            trend_data.append({
                'month': m,
                'supplier': sup,
                'on_time_delivery': base_otd + np.random.normal(0, 2)
            })
    
    trend_df = pd.DataFrame(trend_data)
    
    fig = px.line(trend_df, x='month', y='on_time_delivery', color='supplier',
                  color_discrete_sequence=[TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN, '#9c27b0'])
    fig.update_layout(
        height=350,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        yaxis_title="On-Time Delivery %"
    )
    st.plotly_chart(fig, use_container_width=True)

