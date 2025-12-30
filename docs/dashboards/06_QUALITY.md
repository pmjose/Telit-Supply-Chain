# ✅ Quality Dashboard

## Overview
Comprehensive quality management dashboard covering First Pass Yield (FPY), defect tracking, Statistical Process Control (SPC), incoming inspection, and customer complaints. Supports continuous improvement and compliance requirements.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Quality KPIs and summary |
| **📈 FPY Trends** | First Pass Yield analysis |
| **🔍 Defect Pareto** | Top defect categories |
| **📉 SPC Charts** | Statistical Process Control |
| **📦 Incoming Inspection** | Supplier quality at receipt |
| **🚨 NCR/CAPA** | Non-conformance and corrective actions |
| **📋 Audit Status** | Internal/external audit tracking |
| **🔧 Process Capability** | Cp, Cpk analysis |
| **⚠️ Customer Complaints** | Field quality issues |

---

## 📊 KPIs & Metrics

### Quality Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **First Pass Yield (FPY)** | Units passing first test | >98% | MES Test Data |
| **DPMO** | Defects per million opportunities | <500 | MES Quality |
| **PPM** | Parts per million defective | <100 | QMS |
| **Cost of Poor Quality (COPQ)** | Scrap + rework + warranty | <1% of revenue | SAP CO |
| **Sigma Level** | Process capability | >4σ | Calculated |

### Manufacturing Quality
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Yield by Line** | FPY per production line | >98% | MES |
| **Yield by Product** | FPY per SKU | >98% | MES |
| **Rework Rate** | % requiring rework | <2% | MES |
| **Scrap Rate** | % scrapped | <0.5% | MES |
| **Test Coverage** | % of specs tested | 100% | Test Engineering |

### Incoming Quality
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Incoming Inspection Pass Rate** | Lots accepted | >99% | SAP QM |
| **Supplier PPM** | Defects by supplier | <500 | SAP QM |
| **Skip Lot Rate** | % on reduced inspection | >70% | SAP QM |
| **Incoming Cycle Time** | Receipt to release (hours) | <24 hrs | SAP QM |

### Field Quality
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Customer Complaints** | Monthly complaint count | Decreasing | CRM/QMS |
| **RMA Rate** | Return rate % | <0.5% | SAP SD |
| **Warranty Claims** | Claims $ value | <0.3% rev | SAP |
| **DOA Rate** | Dead on Arrival % | <0.1% | RMA Data |
| **MTBF** | Mean Time Between Failures | Per spec | Field data |

### SPC Metrics
| Metric | Description | Target |
|--------|-------------|--------|
| **Cp** | Process Capability | >1.33 |
| **Cpk** | Process Capability Index | >1.33 |
| **Pp** | Process Performance | >1.33 |
| **Ppk** | Process Performance Index | >1.33 |
| **Out of Control Points** | Points outside limits | 0 |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **FPY Trend Line** | Yield over time | Plotly Line |
| **Defect Pareto** | Top defect types | Plotly Bar + Line |
| **Control Charts (X-bar, R)** | SPC monitoring | Plotly Scatter with limits |
| **Histogram** | Distribution analysis | Plotly Histogram |
| **Box Plots** | Variation by category | Plotly Box |
| **Heatmap** | Defects by line/product | Plotly Heatmap |
| **Gauge Charts** | FPY, Cpk indicators | Plotly Indicator |
| **Fishbone Diagram** | Root cause visualization | Custom/Graphviz |
| **CAPA Funnel** | Corrective action status | Plotly Funnel |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **MES** | Test results, yields, defects | Kafka | Real-time |
| **SAP QM** | Inspection lots, NCRs | Fivetran | 15 min |
| **LIMS** | Lab test results | Kafka | Real-time |
| **CRM/QMS** | Customer complaints | API | Daily |
| **RMA System** | Returns data | REST API | Real-time |
| **Test Equipment** | Raw measurement data | Snowpipe | Per test |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Quality Dashboard
CURATED.FACT_QUALITY_TESTS           -- Individual test results
CURATED.FACT_DEFECTS                 -- Defect records
CURATED.FACT_INCOMING_INSPECTION     -- SAP QM inspection lots
CURATED.FACT_NCR                     -- Non-conformance reports
CURATED.FACT_CAPA                    -- Corrective actions
CURATED.DIM_DEFECT_TYPE              -- Defect classification
CURATED.DIM_TEST_STATION             -- Test equipment master
ANALYTICS.AGG_FPY_DAILY              -- Daily FPY aggregation
ANALYTICS.AGG_SPC_DATA               -- SPC calculations
ML.PRED_QUALITY_RISK                 -- Predicted quality issues
```

---

## 📉 SPC Chart Types

### Control Chart Types Used
| Chart | Application | Formula |
|-------|-------------|---------|
| **X-bar R** | Variable data, subgroups | UCL = X̄ + A₂R̄ |
| **X-bar S** | Variable data, larger subgroups | UCL = X̄ + A₃S̄ |
| **Individual-MR** | Single measurements | UCL = X̄ + 2.66MR̄ |
| **P Chart** | Proportion defective | UCL = p̄ + 3√(p̄(1-p̄)/n) |
| **C Chart** | Defect count | UCL = c̄ + 3√c̄ |
| **U Chart** | Defects per unit | UCL = ū + 3√(ū/n) |

### Control Chart Rules (Western Electric)
| Rule | Description |
|------|-------------|
| Rule 1 | 1 point beyond 3σ |
| Rule 2 | 9 points in a row on same side of center |
| Rule 3 | 6 points in a row, increasing or decreasing |
| Rule 4 | 14 points in a row, alternating up/down |
| Rule 5 | 2 of 3 points beyond 2σ on same side |
| Rule 6 | 4 of 5 points beyond 1σ on same side |

---

## ❓ Potential Questions & Objections

### Q: "How do you calculate FPY?"
**A:** 
```
FPY = Units passing all tests first time / Total units tested × 100%
```
- Includes all test stations in sequence
- Reworked units that pass are NOT counted as first pass
- Each test step is tracked separately

### Q: "Can you do real-time SPC?"
**A:** Yes - for critical parameters:
- Test data streams via Kafka to Snowflake
- Dynamic Tables calculate control limits
- Alerts fire when points go out of control
- Typically <1 minute latency

### Q: "What about automotive quality requirements (IATF 16949)?"
**A:** Dashboard supports:
- PPAP documentation tracking
- MSA (Gage R&R) data
- Control plans per product
- 8D problem solving workflow
- Customer-specific requirements

### Q: "How do you link quality to supplier?"
**A:** Full traceability:
- Incoming inspection by supplier lot
- Defects traced to component supplier via BOM
- Supplier scorecard integration
- SCAR (Supplier Corrective Action) tracking

### Q: "What triggers a quality alert?"
**A:** Multi-level alerting:
1. SPC out-of-control condition
2. FPY below threshold (e.g., <95%)
3. New defect type appears
4. Customer complaint received
5. Pattern detected (e.g., shift effect)

### Q: "Can we integrate with our QMS (Windchill, ETQ, etc.)?"
**A:** Yes - common integrations:
- ETQ: REST API for NCR/CAPA
- Windchill Quality: PLM connector
- SAP QM: Standard Fivetran connector
- Custom QMS: SFTP or API

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~3 weeks |
| **Prerequisites** | MES quality module, test data access |
| **Dependencies** | SAP QM if used, QMS integration |
| **Data Cleanup** | Medium - Test station mapping, defect code alignment |
| **Stakeholders** | Quality Manager, Process Engineering, Plant Manager |

---

## 📊 Sample Quality Query

```sql
-- Daily FPY by Product and Line
SELECT 
    DATE_TRUNC('day', test_timestamp) as test_date,
    p.product_family,
    l.line_name,
    COUNT(*) as total_units,
    SUM(CASE WHEN first_pass_result = 'PASS' THEN 1 ELSE 0 END) as passed_first,
    ROUND(SUM(CASE WHEN first_pass_result = 'PASS' THEN 1 ELSE 0 END) * 100.0 
          / COUNT(*), 2) as fpy_pct,
    SUM(CASE WHEN final_result = 'FAIL' THEN 1 ELSE 0 END) as scrapped
FROM curated.fact_quality_tests t
JOIN curated.dim_product p ON t.product_key = p.product_key
JOIN curated.dim_production_line l ON t.line_key = l.line_key
WHERE test_timestamp >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY 1, 2, 3
ORDER BY 1 DESC, fpy_pct ASC;

-- Defect Pareto Analysis
SELECT 
    d.defect_category,
    d.defect_code,
    d.defect_description,
    COUNT(*) as defect_count,
    SUM(COUNT(*)) OVER (ORDER BY COUNT(*) DESC) as running_total,
    ROUND(SUM(COUNT(*)) OVER (ORDER BY COUNT(*) DESC) * 100.0 
          / SUM(COUNT(*)) OVER (), 2) as cumulative_pct
FROM curated.fact_defects f
JOIN curated.dim_defect_type d ON f.defect_key = d.defect_key
WHERE f.defect_date >= DATEADD('day', -30, CURRENT_DATE())
GROUP BY 1, 2, 3
ORDER BY defect_count DESC;
```

