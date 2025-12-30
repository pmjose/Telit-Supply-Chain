# 🤝 Suppliers Dashboard

## Overview
Comprehensive supplier management dashboard covering supplier performance scorecards, risk assessment, spend analysis, and relationship management. Enables strategic sourcing decisions and supply risk mitigation.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Supplier landscape and key metrics |
| **🏆 Scorecards** | Individual supplier performance ratings |
| **⚠️ Risk Assessment** | Financial, geopolitical, operational risks |
| **💰 Spend Analysis** | Procurement spend by supplier/category |
| **📍 Geographic View** | Supplier locations and concentration |
| **🔧 Performance Trends** | Historical supplier metrics |
| **📋 Contracts** | Contract status and renewals |
| **🌱 ESG Compliance** | Supplier sustainability scores |
| **🔄 Alternatives** | Second-source and backup suppliers |

---

## 📊 KPIs & Metrics

### Supplier Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Total Suppliers** | Active supplier count | Optimized | SAP MM (LFA1) |
| **Avg Supplier Score** | Overall performance rating | >85% | Scorecard calculation |
| **Total Spend** | Annual procurement value | Budget | SAP MM (EKPO) |
| **On-Time Delivery** | Supplier OTD average | >95% | SAP MM (EKBE) |
| **Quality PPM** | Defects per million | <500 PPM | QMS |
| **Critical Suppliers** | Tier 1 strategic suppliers | Identified | Classification |

### Supplier Scorecard Components
| Dimension | Weight | Metrics |
|-----------|--------|---------|
| **Quality** | 30% | PPM, FPY, Incoming inspection pass rate |
| **Delivery** | 30% | OTD, Lead time adherence, Flexibility |
| **Cost** | 20% | Price competitiveness, Cost reduction YoY |
| **Service** | 10% | Responsiveness, Technical support |
| **Risk** | 10% | Financial stability, Geo risk, Compliance |

### Risk Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Financial Risk Score** | D&B/Experian rating | D&B API |
| **Geopolitical Risk** | Country risk index | External data |
| **Single-Source Exposure** | % spend with single source | SAP MM analysis |
| **Compliance Status** | Certification validity | Supplier portal |
| **ESG Score** | Sustainability rating | ESG assessments |

### Spend Analysis
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Spend by Category** | Material type breakdown | SAP MM (MARA) |
| **Spend by Region** | Geographic distribution | SAP MM (LFA1) |
| **Spend Concentration** | Top 10 supplier % | SAP MM |
| **Maverick Spend** | Off-contract purchases | SAP MM |
| **Cost Savings YTD** | Negotiated reductions | Procurement |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Scorecard Radar** | Multi-dimension supplier scores | Plotly Radar |
| **Risk Heatmap** | Supplier risk matrix | Plotly Heatmap |
| **Geo Map** | Supplier locations | Plotly Scatter Geo |
| **Spend Treemap** | Hierarchical spend view | Plotly Treemap |
| **Pareto Chart** | Spend concentration | Plotly Bar + Line |
| **Trend Lines** | Performance over time | Plotly Line |
| **Gauge Charts** | OTD, Quality scores | Plotly Indicator |
| **Sankey Diagram** | Spend flow by category | Plotly Sankey |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **SAP MM** | Suppliers, POs, receipts, prices | Fivetran | 15 min |
| **SAP QM** | Incoming inspection, NCRs | Fivetran | 15 min |
| **D&B / Experian** | Financial risk scores | API | Weekly |
| **Supplier Portal** | Certifications, compliance docs | Snowflake | On-upload |
| **ESG Ratings** | Sustainability scores | API | Monthly |
| **Contract System** | Contract terms, renewals | Integration | Daily |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Suppliers Dashboard
CURATED.DIM_SUPPLIER                 -- Supplier master
CURATED.FACT_PURCHASE_ORDERS         -- PO details (EKKO, EKPO)
CURATED.FACT_GOODS_RECEIPTS          -- Receipts (EKBE)
CURATED.FACT_SUPPLIER_QUALITY        -- Quality data from QM
ANALYTICS.AGG_SUPPLIER_SCORECARD     -- Calculated scorecards
ANALYTICS.V_SUPPLIER_RISK            -- Risk score view
EXTERNAL.SUPPLIER_FINANCIAL_RISK     -- D&B data
ML.PRED_SUPPLIER_RISK                -- Predicted risk scores
```

---

## 🏆 Scorecard Calculation

### Overall Score Formula
```
Overall Score = (Quality × 0.30) + (Delivery × 0.30) + (Cost × 0.20) 
              + (Service × 0.10) + (Risk × 0.10)
```

### Quality Score (30%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| PPM | 50% | 100 - (PPM / 100) |
| Incoming Inspection | 30% | Pass Rate % |
| NCR Response Time | 20% | Within SLA % |

### Delivery Score (30%)
| Metric | Weight | Calculation |
|--------|--------|-------------|
| On-Time Delivery | 60% | Deliveries on-time % |
| Lead Time Adherence | 25% | Within quoted LT % |
| Flexibility | 15% | Expedite acceptance rate |

---

## ❓ Potential Questions & Objections

### Q: "How do you get supplier financial data?"
**A:** Multiple sources:
- **D&B Connector** - Credit scores, payment history
- **Experian API** - Financial health indicators
- **Public Filings** - SEC data for public companies
- **Supplier Portal** - Self-reported financials

### Q: "What about proprietary supplier agreements?"
**A:** Sensitive data is protected:
- Contract values visible only to Procurement role
- Pricing data masked for non-authorized users
- Row-level security by commodity team

### Q: "How current is the risk data?"
**A:** 
- Financial scores: Updated weekly
- Geopolitical: Real-time news monitoring
- Compliance: Updated on document expiry
- ESG: Quarterly refresh

### Q: "Can we add our own scoring criteria?"
**A:** Yes - the scorecard is configurable:
- Weight adjustments per dimension
- Custom metrics addition
- Category-specific scorecards
- Business unit variations

### Q: "How do you identify single-source risk?"
**A:** Analysis at multiple levels:
- Component level (BOM analysis)
- Commodity level (category spend)
- Technology level (e.g., chipset supplier)
- Geographic level (country concentration)

### Q: "What about Tier 2/Tier 3 suppliers?"
**A:** For IoT modules, sub-tier visibility includes:
- Semiconductor suppliers (Qualcomm, MediaTek)
- Passive component suppliers
- PCB/substrate suppliers
- We can extend visibility with BOM explosion

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~3 weeks |
| **Prerequisites** | SAP vendor master, quality history |
| **Dependencies** | D&B/Experian subscription, Supplier portal |
| **Data Cleanup** | Medium - Vendor master cleanup, duplicate removal |
| **Stakeholders** | Procurement, Quality, Supply Chain Risk |

---

## ⚠️ Key Suppliers for Telit IoT Modules

### Semiconductor Suppliers (Tier 1)
| Supplier | Component | Risk Level |
|----------|-----------|------------|
| **Qualcomm** | 5G/LTE chipsets (SDX62, SDX55) | Medium - Allocation |
| **MediaTek** | LTE modems (T750, Helio) | Low |
| **NXP** | MCUs, Power management | Low |
| **Murata** | RF modules, filters | Low |
| **TDK** | Passives, inductors | Low |

### Contract Manufacturers
| CM | Location | Capacity Share |
|----|----------|----------------|
| **Foxconn** | Taiwan, China | 45% |
| **Flex** | Malaysia, China | 35% |
| **Benchmark** | USA, Europe | 20% |

---

## 📊 Sample Risk Query

```sql
-- Supplier Risk Assessment
SELECT 
    s.supplier_name,
    s.supplier_country,
    s.tier,
    ss.quality_score,
    ss.delivery_score,
    ss.overall_score,
    r.financial_risk_score,
    r.geo_risk_score,
    sp.annual_spend_usd,
    sp.spend_pct,
    CASE 
        WHEN r.financial_risk_score < 50 OR r.geo_risk_score > 70 THEN 'HIGH'
        WHEN r.financial_risk_score < 70 OR r.geo_risk_score > 50 THEN 'MEDIUM'
        ELSE 'LOW'
    END as risk_category
FROM curated.dim_supplier s
JOIN analytics.agg_supplier_scorecard ss ON s.supplier_key = ss.supplier_key
JOIN external.supplier_financial_risk r ON s.supplier_id = r.supplier_id
JOIN analytics.agg_supplier_spend sp ON s.supplier_key = sp.supplier_key
WHERE sp.year = YEAR(CURRENT_DATE())
ORDER BY sp.annual_spend_usd DESC;
```

