# 🌱 Carbon ESG Dashboard

## Overview
Environmental, Social, and Governance (ESG) dashboard tracking carbon footprint, emissions, renewable energy usage, and sustainability metrics across the supply chain. Supports CSRD/EU Taxonomy compliance and corporate sustainability goals.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | ESG summary and scores |
| **🏭 Carbon Footprint** | Scope 1, 2, 3 emissions |
| **⚡ Energy** | Energy consumption and renewables |
| **♻️ Circularity** | Waste, recycling, materials |
| **🤝 Social** | Workforce diversity, safety |
| **📋 Supplier ESG** | Supply chain sustainability |
| **📈 Trends & Goals** | Progress toward targets |

---

## 📊 KPIs & Metrics

### ESG Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **ESG Score** | Overall ESG rating | >75 | ESG Platform |
| **Carbon Intensity** | tCO2e per $M revenue | Decreasing | Calculated |
| **Renewable Energy %** | Renewable share of energy | >50% | Energy Data |
| **Waste Diversion Rate** | % waste recycled/reused | >80% | Waste Tracking |
| **Supplier ESG Coverage** | Suppliers with ESG data | >80% | Supplier Portal |

### Carbon Footprint (GHG Protocol)
| Scope | Description | Metric | Data Source |
|-------|-------------|--------|-------------|
| **Scope 1** | Direct emissions (facilities, fleet) | tCO2e | Facilities data |
| **Scope 2** | Indirect (purchased electricity) | tCO2e | Energy bills |
| **Scope 3 Cat 1** | Purchased goods & services | tCO2e | LCA data |
| **Scope 3 Cat 4** | Upstream transportation | tCO2e | Logistics data |
| **Scope 3 Cat 11** | Use of sold products | tCO2e | Product specs |
| **Scope 3 Cat 12** | End-of-life treatment | tCO2e | Estimated |

### Energy Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Total Energy** | MWh consumed | Decreasing | Energy tracking |
| **Renewable Energy** | MWh from renewables | Increasing | Energy tracking |
| **Energy Intensity** | MWh per unit produced | Decreasing | Calculated |
| **PPA Coverage** | Power purchase agreements | >30% | Contracts |
| **On-site Solar** | Self-generated renewable | MW capacity | Facilities |

### Circularity Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Waste Generated** | Total waste (tons) | Decreasing | Waste tracking |
| **Hazardous Waste** | Hazardous waste (kg) | Minimized | Waste tracking |
| **Recycling Rate** | % materials recycled | >75% | Waste tracking |
| **Recycled Content** | % recycled input materials | >25% | Material specs |
| **E-Waste Recovery** | Electronic waste recycled | >95% | Tracking |

### Social Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Workforce Diversity** | % diverse employees | Increasing | HR |
| **Gender Ratio** | Female leadership % | >30% | HR |
| **Safety Incidents** | TRIR | <1.0 | EHS |
| **Training Hours** | Hours per employee | >40/year | HR |
| **Community Investment** | $ donated | Budget | Finance |

### Supplier ESG
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Supplier ESG Assessed** | % with ESG rating | >80% | Supplier Portal |
| **High-Risk Suppliers** | ESG score <50 | 0 | ESG Assessment |
| **Conflict Mineral Free** | % verified conflict-free | 100% | CMRT |
| **Supplier Carbon Data** | Suppliers reporting emissions | >50% | Supplier Portal |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Emissions Waterfall** | Scope 1, 2, 3 breakdown | Plotly Waterfall |
| **Energy Mix Pie** | Renewable vs fossil | Plotly Pie |
| **Trend Lines** | YoY progress | Plotly Line |
| **Goal Gauge** | Progress to 2030 targets | Plotly Indicator |
| **Supplier Heatmap** | ESG scores by supplier | Plotly Heatmap |
| **World Map** | Emissions by facility | Plotly Choropleth |
| **Sankey** | Material flow (circular) | Plotly Sankey |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **Facilities** | Utility bills, fuel usage | Integration | Monthly |
| **ESG Platform** | Carbon calculations | API | Monthly |
| **Supplier Portal** | Supplier ESG surveys | Integration | Quarterly |
| **Waste Mgmt** | Waste manifests | Integration | Monthly |
| **HR System** | Diversity, safety data | Fivetran | Monthly |
| **LCA Database** | Emission factors | Static | Annually |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Carbon ESG
CURATED.FACT_CARBON_EMISSIONS        -- Emissions by scope/site
CURATED.FACT_ENERGY_CONSUMPTION      -- Energy usage
CURATED.FACT_WASTE_TRACKING          -- Waste generation/disposal
CURATED.DIM_EMISSION_SCOPE           -- GHG scope definitions
CURATED.DIM_FACILITY                 -- Facility master
CURATED.DIM_SUSTAINABILITY_GOAL      -- Targets and goals
ANALYTICS.AGG_CARBON_BY_SITE         -- Site-level aggregation
ANALYTICS.AGG_SUPPLIER_ESG           -- Supplier ESG scores
ANALYTICS.V_ESG_SCORECARD            -- ESG dashboard view
EXTERNAL.EMISSION_FACTORS            -- Standard factors
```

---

## 🌍 Scope 3 Calculation Methods

### Category 1: Purchased Goods & Services
```
Emissions = ∑(Material Qty × Emission Factor by Material Type)
```
- LCA data for semiconductor components
- Supplier-specific data where available
- Industry averages for gaps

### Category 4: Upstream Transportation
```
Emissions = ∑(Weight × Distance × Mode Emission Factor)
```
- Air freight: 0.5-1.5 kg CO2e/ton-km
- Ocean freight: 0.01-0.03 kg CO2e/ton-km
- Truck: 0.05-0.15 kg CO2e/ton-km

---

## ❓ Potential Questions & Objections

### Q: "How do you calculate Scope 3?"
**A:** Multiple methods:
- **Spend-based**: $ spend × emission factor
- **Activity-based**: Physical data (weight, distance)
- **Supplier-specific**: Direct from suppliers
- We use hybrid approach, prioritizing accuracy

### Q: "What about CSRD compliance?"
**A:** Dashboard supports CSRD:
- Double materiality assessment data
- EU Taxonomy alignment metrics
- ESRS-aligned disclosures
- Audit-ready data lineage

### Q: "How accurate is carbon data?"
**A:** Data quality levels:
- Scope 1: High (direct measurement)
- Scope 2: High (utility bills)
- Scope 3: Medium (estimates + actuals)
- We track data quality by metric

### Q: "Can you set Science-Based Targets?**
**A:** SBTi alignment:
- Baseline year tracking
- 1.5°C pathway modeling
- Absolute vs intensity targets
- Progress monitoring

### Q: "How do you get supplier ESG data?"
**A:** Multi-channel:
- CDP supply chain program
- EcoVadis/Sedex scores
- Custom ESG surveys
- Self-reported via portal
- Third-party assessments

### Q: "What about product carbon footprint?"
**A:** Product LCA includes:
- Materials (BOM-based)
- Manufacturing (CM energy)
- Logistics (transportation)
- Use phase (power consumption)
- End-of-life (disposal)

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~3 weeks |
| **Prerequisites** | Utility data access, emission factors |
| **Dependencies** | Supplier ESG program, LCA database |
| **Data Cleanup** | High - Baseline setting, factor selection |
| **Stakeholders** | Sustainability, Facilities, Procurement |

---

## 📊 Sample ESG Query

```sql
-- Carbon Footprint by Scope
SELECT 
    e.reporting_year,
    s.scope_name,
    s.scope_category,
    SUM(e.emissions_tco2e) as total_emissions,
    ROUND(SUM(e.emissions_tco2e) * 100.0 / 
          SUM(SUM(e.emissions_tco2e)) OVER (PARTITION BY e.reporting_year), 1) as pct_of_total
FROM curated.fact_carbon_emissions e
JOIN curated.dim_emission_scope s ON e.scope_key = s.scope_key
GROUP BY 1, 2, 3
ORDER BY reporting_year, scope_name;

-- Supplier ESG Risk Assessment
SELECT 
    s.supplier_name,
    s.supplier_country,
    es.esg_overall_score,
    es.environmental_score,
    es.social_score,
    es.governance_score,
    sp.annual_spend_usd,
    CASE 
        WHEN es.esg_overall_score < 50 THEN 'HIGH RISK'
        WHEN es.esg_overall_score < 70 THEN 'MEDIUM RISK'
        ELSE 'LOW RISK'
    END as risk_category
FROM curated.dim_supplier s
LEFT JOIN analytics.agg_supplier_esg es ON s.supplier_key = es.supplier_key
JOIN analytics.agg_supplier_spend sp ON s.supplier_key = sp.supplier_key
WHERE sp.year = YEAR(CURRENT_DATE())
ORDER BY sp.annual_spend_usd DESC;
```

