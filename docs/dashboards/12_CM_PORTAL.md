# 🏭 CM Portal Dashboard

## Overview
Contract Manufacturer (CM) visibility dashboard providing real-time production status, capacity utilization, WIP tracking, and performance scorecards across all manufacturing partners (Foxconn, Flex, Benchmark, etc.).

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | CM summary and status |
| **🏭 Production Status** | Real-time output by CM |
| **📈 Capacity** | Utilization and planning |
| **📦 WIP Tracking** | Work-in-progress visibility |
| **🏆 Scorecards** | CM performance ratings |
| **📋 PO Status** | Purchase order tracking |

---

## 📊 KPIs & Metrics

### CM Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Active CMs** | Manufacturing partners | 3-5 | Master Data |
| **Total Capacity** | Units per month | Planned | CM Data |
| **Capacity Utilization** | Actual ÷ Available | 70-85% | CM Data |
| **WIP Value** | Work-in-progress $ | Managed | CM Data |
| **On-Time Ship %** | CM OTD performance | >95% | CM Data |

### Production Metrics by CM
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Daily Output** | Units produced today | CM MES |
| **MTD Production** | Month-to-date units | CM MES |
| **Yield Rate** | FPY at CM | CM MES |
| **Scrap Rate** | Units scrapped | CM MES |
| **Line Utilization** | Line running hours % | CM MES |

### Capacity Planning
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Available Capacity** | Open capacity hours | Visible | CM Planning |
| **Booked Capacity** | Committed production | Planned | PO Data |
| **Capacity Gap** | Demand vs Capacity | Balanced | Calculation |
| **Lead Time** | Order to ship days | Per product | CM Data |
| **Ramp Capability** | Max ramp-up rate | Defined | CM Agreement |

### WIP Tracking
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **WIP Units** | Units in production | CM MES |
| **WIP Aging** | Days in WIP | CM MES |
| **Stage Distribution** | WIP by stage | CM MES |
| **At-Risk WIP** | WIP with issues | CM Alerts |
| **Component WIP** | Subassemblies | CM MES |

### CM Scorecard Components
| Dimension | Weight | Metrics |
|-----------|--------|---------|
| **Quality** | 25% | FPY, Escapes, Process compliance |
| **Delivery** | 30% | OTD, Lead time adherence |
| **Cost** | 20% | Unit cost, Scrap cost |
| **Responsiveness** | 15% | Communication, Issue resolution |
| **Flexibility** | 10% | Ramp capability, ECO speed |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **CM Status Cards** | Health by CM | Custom HTML |
| **Production Gauge** | Daily output vs plan | Plotly Indicator |
| **Capacity Bar** | Utilization by CM | Plotly Bar |
| **WIP Waterfall** | In vs Out vs Current | Plotly Waterfall |
| **Scorecard Radar** | CM performance dimensions | Plotly Radar |
| **Map** | CM locations | Plotly Scatter Geo |
| **Timeline** | PO delivery schedule | Plotly Timeline |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **Foxconn Portal** | Production, WIP, capacity | SFTP + Snowpipe | Hourly |
| **Flex Portal** | Production, WIP, quality | SFTP + Snowpipe | Hourly |
| **Benchmark Portal** | Production data | API | Daily |
| **SAP MM** | POs, GR, invoices | Fivetran | 15 min |
| **CM EDI** | ASN, production confirmations | Snowpipe | Real-time |
| **Quality System** | CM quality data | Integration | Daily |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for CM Portal
CURATED.DIM_CM_SITE                  -- CM site master
CURATED.DIM_PRODUCTION_LINE          -- CM line definitions
CURATED.FACT_CM_PRODUCTION           -- Production transactions
CURATED.FACT_CM_WIP                  -- WIP snapshots
CURATED.FACT_CM_CAPACITY             -- Capacity data
CURATED.FACT_PURCHASE_ORDERS         -- POs to CMs
ANALYTICS.AGG_CM_SCORECARD           -- CM performance
ANALYTICS.V_CM_PRODUCTION_STATUS     -- Current status view
ML.PRED_CM_CAPACITY                  -- Capacity forecasts
```

---

## 🏭 Telit Contract Manufacturers

### CM Portfolio
| CM | Location | Capacity | Products | Share |
|----|----------|----------|----------|-------|
| **Foxconn** | Taiwan, China | 500K/mo | LE910, ME910, FN980 | 45% |
| **Flex** | Malaysia, China | 400K/mo | LE910, HE910 | 35% |
| **Benchmark** | USA, Europe | 150K/mo | Custom, High-mix | 20% |

### CM Integration Levels
| Level | Description | Data Available |
|-------|-------------|----------------|
| **Level 1** | Basic | Daily production totals |
| **Level 2** | Standard | WIP, yields, shipments |
| **Level 3** | Advanced | Real-time, line-level, test data |
| **Level 4** | Integrated | Full MES visibility, genealogy |

---

## ❓ Potential Questions & Objections

### Q: "How do you get data from CMs?"
**A:** Multiple integration patterns:
- **Foxconn**: Daily SFTP file drops + weekly calls
- **Flex**: Portal API + EDI transactions
- **Benchmark**: Email reports → parsed by Python
- Goal: Move all to API-first integration

### Q: "What about data confidentiality?
**A:** CM-specific data isolation:
- Each CM sees only their own data
- Secure Data Sharing with row-level security
- No cross-CM visibility
- Aggregated data for Telit benchmarking

### Q: "How do you handle dual-sourcing visibility?"
**A:** Product × CM matrix:
- Same product at multiple CMs
- Capacity allocation by CM
- Performance comparison (anonymized)
- Dynamic rebalancing capability

### Q: "What if CM data is delayed or missing?"
**A:** Data quality monitoring:
- Expected vs received data alerts
- Stale data flagging (>24 hours)
- Estimated data based on historical patterns
- CM data SLA tracking

### Q: "Can you predict CM capacity constraints?"
**A:** ML-based capacity forecasting:
- Historical production patterns
- Seasonal capacity variations
- Equipment maintenance schedules
- Workforce availability

### Q: "How do you handle expedites?**
**A:** Expedite tracking:
- Expedite request workflow
- Premium cost tracking
- Impact on other orders
- Historical expedite success rates

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~3 weeks |
| **Prerequisites** | CM data agreements, integration setup |
| **Dependencies** | SAP for PO data, Quality for CM metrics |
| **Data Cleanup** | Medium - Product mapping, data format standardization |
| **Stakeholders** | Operations, Supply Chain, Procurement |

---

## 📊 Sample CM Query

```sql
-- CM Production Summary
SELECT 
    cm.cm_name,
    cm.site_location,
    p.product_family,
    SUM(cp.units_produced) as units_produced,
    SUM(cp.units_shipped) as units_shipped,
    SUM(cp.units_in_wip) as current_wip,
    AVG(cp.yield_rate) as avg_yield,
    SUM(cp.scrap_qty) as total_scrap,
    SUM(cp.production_cost_usd) as total_cost
FROM curated.fact_cm_production cp
JOIN curated.dim_cm_site cm ON cp.cm_site_key = cm.cm_site_key
JOIN curated.dim_product p ON cp.product_key = p.product_key
WHERE cp.production_date >= DATE_TRUNC('month', CURRENT_DATE())
GROUP BY 1, 2, 3
ORDER BY units_produced DESC;

-- CM Scorecard Calculation
SELECT 
    cm.cm_name,
    -- Quality (25%)
    AVG(CASE WHEN metric_type = 'FPY' THEN metric_value END) * 0.25 as quality_score,
    -- Delivery (30%)
    AVG(CASE WHEN metric_type = 'OTD' THEN metric_value END) * 0.30 as delivery_score,
    -- Cost (20%)
    AVG(CASE WHEN metric_type = 'COST_INDEX' THEN metric_value END) * 0.20 as cost_score,
    -- Responsiveness (15%)
    AVG(CASE WHEN metric_type = 'RESPONSE_TIME' THEN metric_value END) * 0.15 as response_score,
    -- Flexibility (10%)
    AVG(CASE WHEN metric_type = 'FLEXIBILITY' THEN metric_value END) * 0.10 as flex_score,
    -- Overall
    SUM(metric_value * weight) / SUM(weight) as overall_score
FROM analytics.agg_cm_metrics m
JOIN curated.dim_cm_site cm ON m.cm_site_key = cm.cm_site_key
WHERE metric_period = DATE_TRUNC('month', CURRENT_DATE())
GROUP BY 1
ORDER BY overall_score DESC;
```

