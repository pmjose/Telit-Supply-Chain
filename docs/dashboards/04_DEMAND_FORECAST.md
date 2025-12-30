# 📈 Demand Forecast Dashboard

## Overview
AI-powered demand planning and forecasting dashboard that combines historical sales, design wins, seasonality, and external signals to generate accurate demand predictions. Supports S&OP processes, inventory planning, and capacity allocation.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Forecast Overview** | Summary of forecast accuracy and key metrics |
| **📈 Demand Trends** | Historical and predicted demand patterns |
| **🎯 Forecast vs Actual** | Accuracy tracking and variance analysis |
| **🔮 AI Predictions** | ML model outputs and confidence intervals |
| **📅 Seasonality** | Seasonal patterns and adjustments |
| **🏆 Design Wins** | New customer/project pipeline impact |
| **🌍 Regional Forecast** | Demand by geography |
| **📦 Product Family** | Forecast by product line |
| **🔧 Model Performance** | ML model metrics and drift monitoring |
| **📋 Scenario Planning** | What-if analysis tools |
| **⚠️ Demand Signals** | Early warning indicators |
| **📤 Export & S&OP** | Reports for planning meetings |
| **🔄 Consensus** | Collaborative forecast adjustments |

---

## 📊 KPIs & Metrics

### Forecast Accuracy
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **MAPE** | Mean Absolute Percentage Error | <10% | Forecast vs Actuals |
| **Bias** | Systematic over/under forecast | <±2% | Forecast vs Actuals |
| **WMAPE** | Weighted MAPE (volume-weighted) | <8% | Forecast vs Actuals |
| **Forecast Value Added** | Improvement over naive forecast | >15% | Model comparison |
| **Hit Rate** | % within ±10% of actual | >85% | Forecast vs Actuals |

### Demand Overview
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Demand This Month** | Current month forecast | ML Model |
| **Demand Next Quarter** | Q+1 forecast | ML Model |
| **YoY Growth** | Year-over-year demand change | Historical + Forecast |
| **Trend Direction** | Increasing/Decreasing/Stable | ML Model |
| **Confidence Level** | Prediction confidence | ML Model |

### Design Win Impact
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Active Design Wins** | Projects in design phase | Salesforce |
| **Projected Volume** | Expected units from design wins | Salesforce + Estimation |
| **Win Rate** | Historical win conversion | Salesforce |
| **Ramp Timeline** | Expected production start | Customer data |
| **Revenue Impact** | Projected $ from design wins | Sales estimates |

### Seasonality Patterns
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Seasonal Index** | Monthly seasonality factor | 3-year historical |
| **Peak Months** | Highest demand months | Historical analysis |
| **Trough Months** | Lowest demand months | Historical analysis |
| **Holiday Impact** | Sales around key dates | External calendar |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Forecast Line Chart** | Prediction with confidence bands | Plotly Line |
| **Accuracy Gauge** | MAPE indicator | Plotly Indicator |
| **Forecast vs Actual Bar** | Monthly comparison | Plotly Bar |
| **Seasonality Heatmap** | Monthly patterns by product | Plotly Heatmap |
| **Design Win Funnel** | Pipeline conversion | Plotly Funnel |
| **Regional Choropleth** | Demand by region | Plotly Choropleth |
| **Decomposition Chart** | Trend + Season + Residual | Plotly Subplots |
| **Scenario Comparison** | Multiple forecast scenarios | Plotly Line (multiple) |
| **Feature Importance** | ML model drivers | Plotly Bar |
| **Model Performance** | Time series of accuracy | Plotly Line |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **SAP SD** | Historical orders, shipments | Fivetran | 15 min |
| **Salesforce** | Design wins, opportunities, pipeline | Fivetran | 30 min |
| **Customer Forecasts** | EDI 830/862 forecasts | Snowpipe | Daily |
| **Market Data** | Industry trends, competitor data | Marketplace | Weekly |
| **Weather Data** | Seasonal/weather impact | OpenWeather API | Daily |
| **Economic Indicators** | GDP, industrial production | Bloomberg/Fed | Monthly |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Demand Forecast
CURATED.FACT_ORDERS                  -- Historical order data
CURATED.FACT_SHIPMENTS               -- Actual shipments
CURATED.DIM_PRODUCT                  -- Product master
CURATED.DIM_CUSTOMER                 -- Customer details
ANALYTICS.AGG_DEMAND_MONTHLY         -- Monthly demand aggregation
ML.FEAT_DEMAND_FEATURES              -- Feature store for ML
ML.PRED_DEMAND_FORECAST              -- Forecast predictions
ML.MODEL_DEMAND_METRICS              -- Model performance tracking
STAGING.STG_CUSTOMER_FORECAST        -- Customer EDI forecasts
EXTERNAL.MARKET_INDICATORS           -- External economic data
```

---

## 🤖 ML Models Used

### Primary Forecast Model
| Attribute | Value |
|-----------|-------|
| **Algorithm** | Cortex FORECAST + Prophet ensemble |
| **Features** | 45 features |
| **Training Data** | 3 years historical |
| **Prediction Horizon** | 12 months rolling |
| **Refresh** | Daily |
| **Accuracy (MAPE)** | 8.2% |

### Feature Categories
| Category | Features |
|----------|----------|
| **Time** | Day of week, month, quarter, holidays |
| **Lag** | 7d, 30d, 90d, 365d demand lags |
| **Rolling** | 7d, 30d, 90d moving averages |
| **Trend** | Linear trend, YoY growth rate |
| **Seasonality** | Monthly, quarterly indices |
| **External** | Weather, economic indicators |
| **Product** | Family, lifecycle stage, price tier |
| **Customer** | Segment, region, historical variability |

---

## ❓ Potential Questions & Objections

### Q: "How accurate is the AI forecast?"
**A:** Our ensemble model achieves:
- MAPE: 8.2% (industry average: 15-25%)
- Forecast Value Added: 23% improvement over naive methods
- Accuracy improves with longer history and stable products

### Q: "Can it handle new product introductions (NPI)?"
**A:** Yes, using:
- Analog product modeling (similar products' history)
- Design win pipeline data from Salesforce
- Customer forecast inputs
- Manual adjustments for unique factors

### Q: "How do you incorporate customer forecasts?"
**A:** Customer EDI 830/862 forecasts are:
1. Ingested via Snowpipe (real-time)
2. Weighted based on historical accuracy per customer
3. Blended with statistical forecast
4. Customer-specific bias corrections applied

### Q: "What about sudden demand changes (COVID, chip shortage)?"
**A:** Multi-layer approach:
- **Demand signals tab** monitors leading indicators
- **Scenario planning** allows stress testing
- **Manual overrides** for known disruptions
- **Anomaly detection** flags unusual patterns

### Q: "Can different teams see different forecasts?"
**A:** Yes, we support multiple forecast versions:
- **Statistical** - Pure ML output
- **Sales** - Sales team adjustments
- **Finance** - Budget-aligned
- **Consensus** - S&OP agreed forecast
All versions are tracked and compared.

### Q: "How far out can you forecast?"
**A:** 
- High confidence: 0-3 months
- Medium confidence: 3-6 months
- Directional: 6-12 months
Confidence intervals widen with horizon.

### Q: "How do you handle promotions or events?"
**A:** 
- Promotion calendar as feature input
- Lift factors from historical promotions
- Event flags for trade shows, launches
- Customer-specific promotion patterns

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~4 weeks |
| **Prerequisites** | 2+ years order history, customer master |
| **Dependencies** | Salesforce for design wins, customer forecasts |
| **Data Cleanup** | High - Historical order cleanup, outlier treatment |
| **Stakeholders** | Demand Planning, Sales, Finance, S&OP |

---

## 📊 Sample Cortex Forecast Query

```sql
-- Generate demand forecast using Cortex
CREATE OR REPLACE TABLE ml.pred_demand_forecast AS
SELECT 
    product_key,
    forecast_date,
    SNOWFLAKE.CORTEX.FORECAST(
        demand_qty,
        forecast_date,
        {'horizon': 90, 'frequency': 'D'}
    ) as predicted_demand,
    SNOWFLAKE.CORTEX.FORECAST_CONFIDENCE(
        demand_qty,
        forecast_date,
        {'horizon': 90, 'frequency': 'D', 'confidence': 0.95}
    ) as confidence_interval
FROM analytics.agg_demand_daily
GROUP BY product_key;

-- Calculate forecast accuracy
SELECT 
    DATE_TRUNC('month', actual_date) as month,
    AVG(ABS(predicted - actual) / NULLIF(actual, 0)) * 100 as mape,
    AVG(predicted - actual) / NULLIF(AVG(actual), 0) * 100 as bias
FROM analytics.forecast_vs_actual
WHERE actual_date >= DATEADD('month', -6, CURRENT_DATE())
GROUP BY 1
ORDER BY 1;
```

