# ⚠️ Risk & Maintenance Dashboard

## Overview
Supply chain risk management and predictive maintenance dashboard. Covers geopolitical risk, supplier financial risk, equipment health monitoring, and AI-powered failure prediction. Enables proactive risk mitigation.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Risk Overview** | Enterprise risk summary |
| **🌍 Geopolitical** | Country and regional risks |
| **💰 Financial Risk** | Supplier financial health |
| **⚙️ Equipment Health** | Predictive maintenance |
| **🔮 Predictions** | AI-powered risk forecasts |
| **📋 Mitigation Actions** | Risk response tracking |
| **🛡️ Cyber Risk** | IT/OT security monitoring |
| **📈 Trends** | Risk evolution over time |

---

## 📊 KPIs & Metrics

### Risk Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Enterprise Risk Score** | Weighted overall risk | <50 | Risk Model |
| **High-Risk Suppliers** | Suppliers with score >70 | Minimize | Risk Assessment |
| **Open Risk Items** | Unmitigated risks | Tracking | Risk Register |
| **Risk Trend** | 30-day risk trajectory | Stable/Decreasing | Calculated |
| **Insurance Coverage** | % risks covered | >80% | Finance |

### Geopolitical Risk
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Country Risk Index** | Political/economic stability | World Bank/EIU |
| **Supplier Concentration** | % spend by country | SAP MM |
| **Trade Policy Risk** | Tariff/sanction exposure | External |
| **Natural Disaster Risk** | Earthquake, flood, typhoon | Risk models |
| **Infrastructure Risk** | Power, ports, logistics | External data |

### Financial Risk
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Supplier Credit Score** | D&B/Experian rating | >70 | D&B API |
| **Payment Behavior** | Days payable trend | Stable | D&B |
| **Revenue Concentration** | Customer dependency | <30% | Supplier financials |
| **Bankruptcy Probability** | 12-month probability | <5% | Risk model |
| **Financial Stress Score** | Altman Z-score proxy | >3.0 | Calculated |

### Equipment Health (Predictive Maintenance)
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Equipment Health Score** | Overall health index | >80 | IoT + ML |
| **Remaining Useful Life (RUL)** | Predicted days to failure | >30 days | ML Model |
| **Anomaly Detection** | Active anomalies | 0 | ML Model |
| **MTBF** | Mean Time Between Failures | Increasing | Historical |
| **MTTR** | Mean Time To Repair | <4 hours | CMMS |
| **Planned Maintenance %** | PM vs reactive | >80% | CMMS |

### Cyber Risk
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Vulnerability Score** | Open vulnerabilities | Low | Security tools |
| **Supplier Cyber Score** | 3rd party cyber risk | >70 | BitSight/SecurityScorecard |
| **Incident Count** | Security incidents | 0 | SIEM |
| **Patch Compliance** | Systems patched | >95% | IT Ops |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Risk Heatmap** | Impact × Likelihood matrix | Plotly Heatmap |
| **World Map** | Risk by country | Plotly Choropleth |
| **Gauge Charts** | Risk level indicators | Plotly Indicator |
| **Trend Lines** | Risk evolution | Plotly Line |
| **Equipment Health Cards** | Status by machine | Custom HTML |
| **Anomaly Timeline** | Sensor anomalies | Plotly Scatter |
| **Pareto Chart** | Top risk contributors | Plotly Bar |
| **Network Graph** | Risk interdependencies | Graphviz |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **D&B/Experian** | Supplier financial data | API | Weekly |
| **World Bank/EIU** | Country risk indices | API | Monthly |
| **IoT Sensors** | Equipment telemetry | Snowpipe | Real-time |
| **CMMS** | Maintenance records | API | Daily |
| **News/Social** | Event monitoring | API | Real-time |
| **SecurityScorecard** | Cyber risk ratings | API | Weekly |
| **Internal Risk Register** | Risk assessments | Integration | On-change |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Risk & Maintenance
CURATED.FACT_RISK_ASSESSMENTS        -- Risk evaluations
CURATED.FACT_EQUIPMENT_TELEMETRY     -- Sensor data
CURATED.FACT_MAINTENANCE_EVENTS      -- PM and repairs
CURATED.DIM_RISK_CATEGORY            -- Risk taxonomy
CURATED.DIM_EQUIPMENT                -- Equipment master
EXTERNAL.COUNTRY_RISK_INDEX          -- Geopolitical data
EXTERNAL.SUPPLIER_CREDIT_SCORES      -- Financial risk
ANALYTICS.V_RISK_DASHBOARD           -- Consolidated risk view
ML.PRED_EQUIPMENT_FAILURE            -- RUL predictions
ML.FEAT_EQUIPMENT_HEALTH             -- Health features
```

---

## 🤖 Predictive Maintenance Model

### Model Specifications
| Attribute | Value |
|-----------|-------|
| **Algorithm** | XGBoost |
| **Features** | 28 (sensor + operational) |
| **Target** | Days to failure |
| **Training Data** | 2 years historical |
| **Accuracy (AUC)** | 0.92 |
| **Prediction Horizon** | 30 days |

### Key Features
| Category | Features |
|----------|----------|
| **Sensor** | Vibration RMS, temperature, current, pressure |
| **Operational** | Run hours, cycles, load %, downtime |
| **Maintenance** | Days since last PM, PM compliance |
| **Temporal** | Day of week, shift, seasonal |
| **Derived** | Rolling averages, rate of change |

---

## ❓ Potential Questions & Objections

### Q: "How do you aggregate different risk types?"
**A:** Weighted composite score:
```
Enterprise Risk = (Geo × 0.25) + (Financial × 0.30) + 
                  (Operational × 0.25) + (Cyber × 0.20)
```
Weights adjustable by business priority.

### Q: "How current is geopolitical risk data?"
**A:** Multi-speed refresh:
- Country indices: Monthly
- Event monitoring: Real-time (news API)
- Supplier exposure: Weekly recalculation
- Sanctions lists: Daily

### Q: "How accurate is RUL prediction?"
**A:** Model performance:
- 78% of failures predicted with 14+ days notice
- False positive rate: 15% (conservative)
- Precision: 85%
- Deployed on 150+ critical equipment

### Q: "What about black swan events?**
**A:** Scenario planning capability:
- Stress testing for major disruptions
- "What if" analysis (Taiwan scenario)
- Business continuity triggers
- Historical disruption learning

### Q: "How do you handle supplier confidentiality?"
**A:** Data protection:
- Aggregated risk views for non-authorized users
- Supplier names anonymized in analytics
- Financial data visible only to Procurement/Risk
- Row-level security enforcement

### Q: "Can you integrate with our CMMS?"
**A:** Common integrations:
- SAP PM
- IBM Maximo
- Fiix
- UpKeep
- Maintenance Connection

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~4 weeks |
| **Prerequisites** | Equipment sensor data, risk register |
| **Dependencies** | D&B/external data subscriptions, CMMS |
| **Data Cleanup** | High - Sensor calibration, risk taxonomy |
| **Stakeholders** | Risk Management, Operations, IT Security |

---

## 📊 Sample Risk Queries

```sql
-- Supplier Risk Heat Map
SELECT 
    s.supplier_name,
    s.supplier_country,
    cr.geo_risk_score,
    fr.financial_risk_score,
    ROUND((cr.geo_risk_score * 0.4 + fr.financial_risk_score * 0.6), 1) as composite_risk,
    sp.annual_spend_usd,
    CASE 
        WHEN (cr.geo_risk_score > 70 OR fr.financial_risk_score > 70) THEN 'HIGH'
        WHEN (cr.geo_risk_score > 50 OR fr.financial_risk_score > 50) THEN 'MEDIUM'
        ELSE 'LOW'
    END as risk_category
FROM curated.dim_supplier s
JOIN external.country_risk_index cr ON s.supplier_country = cr.country_code
JOIN external.supplier_credit_scores fr ON s.supplier_id = fr.supplier_id
JOIN analytics.agg_supplier_spend sp ON s.supplier_key = sp.supplier_key
WHERE sp.year = YEAR(CURRENT_DATE())
ORDER BY composite_risk DESC;

-- Equipment Health and RUL
SELECT 
    e.equipment_name,
    e.equipment_type,
    e.location,
    h.health_score,
    p.predicted_rul_days,
    p.failure_probability,
    p.recommended_action,
    m.last_pm_date,
    DATEDIFF('day', m.last_pm_date, CURRENT_DATE()) as days_since_pm
FROM curated.dim_equipment e
JOIN ml.feat_equipment_health h ON e.equipment_key = h.equipment_key
JOIN ml.pred_equipment_failure p ON e.equipment_key = p.equipment_key
LEFT JOIN analytics.agg_maintenance_latest m ON e.equipment_key = m.equipment_key
WHERE p.failure_probability > 0.3 OR p.predicted_rul_days < 30
ORDER BY p.predicted_rul_days ASC;
```

