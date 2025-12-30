# 🔁 Returns & RMA Dashboard

## Overview
Returns and RMA (Return Merchandise Authorization) management dashboard covering customer returns, failure analysis, warranty claims, and repair/refurbishment tracking. Supports quality improvement and customer satisfaction.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | RMA summary and key metrics |
| **📋 Open RMAs** | Active return cases |
| **🔍 Failure Analysis** | Root cause investigation |
| **💰 Warranty Claims** | Warranty cost tracking |
| **🔧 Repair Status** | Repair and refurbishment |
| **📈 Trends** | RMA patterns over time |

---

## 📊 KPIs & Metrics

### RMA Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Open RMAs** | Active RMA cases | Minimize | RMA System |
| **RMA Rate** | Returns ÷ Shipments | <0.5% | Calculated |
| **Avg Resolution Time** | Days to close RMA | <14 days | RMA System |
| **Warranty Cost** | Monthly warranty expense | <0.3% rev | Finance |
| **Repeat Failure Rate** | Same issue return rate | <5% | RMA System |

### Return Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Returns This Month** | RMAs opened this month | RMA System |
| **Units Returned** | Quantity returned | RMA System |
| **Return Value** | $ value of returns | RMA System |
| **Top Return Reasons** | Defect categories | RMA System |
| **Customer Distribution** | Returns by customer | RMA System |

### Failure Analysis Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **NFF Rate** | No Fault Found % | Failure Analysis |
| **Top Failure Modes** | Most common failures | Failure Analysis |
| **MTBF Field** | Field Mean Time Between Failures | Calculated |
| **DOA Rate** | Dead on Arrival % | RMA System |
| **Infant Mortality** | Failures <30 days | RMA System |

### Warranty Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **In-Warranty Claims** | Claims within warranty | Tracking | RMA System |
| **Out-of-Warranty Claims** | OOW claims | Billable | RMA System |
| **Warranty Reserve** | Accrued warranty liability | Adequate | Finance |
| **Avg Claim Cost** | Cost per warranty claim | Minimize | Finance |
| **Warranty Utilization** | Claims ÷ Coverage | <Expected | Analysis |

### Disposition Tracking
| Disposition | Description |
|-------------|-------------|
| **Repair & Return** | Fixed and returned to customer |
| **Replace** | New unit provided |
| **Credit** | Customer credited |
| **Refurbish** | Repaired for resale |
| **Scrap** | Non-repairable, disposed |
| **NFF-Return** | No fault found, returned |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **RMA Trend Line** | Monthly RMA count | Plotly Line |
| **Failure Pareto** | Top failure modes | Plotly Bar |
| **Disposition Pie** | Outcome distribution | Plotly Pie |
| **Resolution Time Box** | Time distribution | Plotly Box |
| **Customer Heatmap** | RMAs by customer/product | Plotly Heatmap |
| **Warranty Cost Bar** | Monthly warranty expense | Plotly Bar |
| **Failure Timeline** | Product age at failure | Plotly Histogram |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **RMA System** | RMA tickets, status | REST API | Real-time |
| **Failure Analysis** | FA reports, root cause | Integration | Daily |
| **SAP SD** | Original shipment data | Fivetran | 15 min |
| **SAP QM** | Quality notifications | Fivetran | 15 min |
| **Repair Shop** | Repair status, parts used | Integration | Daily |
| **Finance** | Warranty accruals, costs | Fivetran | Daily |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Returns & RMA
CURATED.FACT_RMA_TICKETS             -- RMA header details
CURATED.FACT_RMA_LINES               -- RMA line items
CURATED.FACT_FAILURE_ANALYSIS        -- FA reports
CURATED.FACT_REPAIR_HISTORY          -- Repair transactions
CURATED.DIM_FAILURE_MODE             -- Failure classification
CURATED.DIM_DISPOSITION              -- Disposition types
CURATED.DIM_WARRANTY                 -- Warranty terms
ANALYTICS.AGG_RMA_BY_PRODUCT         -- RMA by product
ANALYTICS.V_WARRANTY_EXPOSURE        -- Warranty liability
ML.PRED_RMA_ROOT_CAUSE               -- AI root cause prediction
```

---

## 🔍 Failure Mode Categories

### Common IoT Module Failure Modes
| Category | Failure Mode | Typical Cause |
|----------|--------------|---------------|
| **Hardware** | No power | Power circuit failure |
| **Hardware** | No network | RF component failure |
| **Hardware** | Overheating | Thermal design issue |
| **Hardware** | Physical damage | Handling/ESD |
| **Firmware** | Boot failure | Firmware corruption |
| **Firmware** | Network attach fail | Configuration issue |
| **Firmware** | Feature not working | Software bug |
| **Application** | Customer SW issue | Integration problem |
| **NFF** | No fault found | Intermittent/customer error |

---

## ❓ Potential Questions & Objections

### Q: "How do you track warranty coverage?"
**A:** Warranty tracking includes:
- Serial number to shipment date linkage
- Warranty terms by product/customer
- Automatic in/out of warranty flagging
- Extended warranty contracts
- Customer-specific terms

### Q: "What's your NFF (No Fault Found) rate?"
**A:** Industry typical 15-30%. We track:
- NFF root cause (customer configuration, intermittent)
- Repeated NFF by customer (training need)
- Product-specific NFF patterns
- Cost of NFF processing

### Q: "How do you use AI in failure analysis?"
**A:** Cortex LLM + ML model:
- Analyze RMA notes for symptom extraction
- Match to known failure patterns
- Suggest root cause categories
- Predict disposition outcome
- F1 Score: 0.84

### Q: "Can you predict returns before they happen?"
**A:** Leading indicators:
- Production lot quality data
- Environmental conditions during use
- Customer complaint patterns
- Similar product RMA history

### Q: "How do you handle out-of-warranty repairs?"
**A:** OOW process:
- Quote generation for repair
- Customer approval workflow
- Flat-rate vs time/materials
- Refurbished unit exchange option

### Q: "What about international returns logistics?"
**A:** Global RMA logistics:
- Regional return centers
- Cross-border documentation
- Customs handling for repairs
- Loaner/swap programs

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~2 weeks |
| **Prerequisites** | RMA system access, FA database |
| **Dependencies** | SAP for shipment history, Finance for costs |
| **Data Cleanup** | Medium - Failure code standardization |
| **Stakeholders** | Customer Service, Quality, Finance |

---

## 📊 Sample RMA Query

```sql
-- RMA Summary by Product and Failure Mode
SELECT 
    p.product_family,
    p.product_name,
    fm.failure_category,
    fm.failure_mode,
    COUNT(*) as rma_count,
    AVG(r.resolution_days) as avg_resolution_days,
    SUM(r.warranty_cost_usd) as total_warranty_cost,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (PARTITION BY p.product_family), 1) as pct_of_family
FROM curated.fact_rma_tickets r
JOIN curated.dim_product p ON r.product_key = p.product_key
JOIN curated.dim_failure_mode fm ON r.failure_mode_key = fm.failure_mode_key
WHERE r.rma_created_date >= DATEADD('month', -12, CURRENT_DATE())
GROUP BY 1, 2, 3, 4
ORDER BY rma_count DESC;

-- RMA Rate Trend
SELECT 
    DATE_TRUNC('month', r.rma_created_date) as month,
    COUNT(DISTINCT r.rma_id) as rma_count,
    SUM(s.shipped_qty) as units_shipped,
    ROUND(COUNT(DISTINCT r.rma_id) * 100.0 / NULLIF(SUM(s.shipped_qty), 0), 3) as rma_rate_pct
FROM curated.fact_rma_tickets r
FULL OUTER JOIN curated.fact_shipments s 
    ON DATE_TRUNC('month', r.rma_created_date) = DATE_TRUNC('month', DATEADD('month', -3, s.ship_date))
WHERE COALESCE(r.rma_created_date, s.ship_date) >= DATEADD('year', -1, CURRENT_DATE())
GROUP BY 1
ORDER BY 1;
```

