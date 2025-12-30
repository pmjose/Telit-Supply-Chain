# 💱 Financial & Costing Dashboard

## Overview
Product costing, margin analysis, and financial performance dashboard. Provides visibility into standard costs, variances, profitability by product/customer, and cost reduction initiatives.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Financial summary and margins |
| **💰 Product Costs** | Standard cost breakdown |
| **📈 Margin Analysis** | Profitability by product/customer |
| **📉 Variance Analysis** | Standard vs actual variances |
| **🔄 Cost Trends** | Historical cost evolution |
| **🎯 Cost Reduction** | Savings initiatives tracking |

---

## 📊 KPIs & Metrics

### Financial Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Gross Margin** | (Revenue - COGS) / Revenue | >38% | SAP CO |
| **Contribution Margin** | Revenue - Variable Costs | >45% | SAP CO |
| **Avg Product Cost** | Weighted average cost | Decreasing | SAP CO |
| **Cost Variance YTD** | Standard vs Actual | <2% | SAP CO |
| **Cost Reduction YTD** | Savings realized | $X target | Tracking |

### Product Cost Components
| Component | Description | % of Cost | Data Source |
|-----------|-------------|-----------|-------------|
| **Materials** | Component costs | 65-75% | SAP MM (MBEW) |
| **Labor** | Direct labor | 5-10% | SAP CO (CC) |
| **Overhead** | Allocated overhead | 10-15% | SAP CO (CC) |
| **Logistics** | Freight, duties | 5-10% | SAP MM |
| **Warranty** | Warranty reserve | 1-2% | Finance |

### Margin Analysis
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Margin by Product** | Profitability per SKU | SAP CO (Product Costing) |
| **Margin by Customer** | Profitability per customer | SAP SD + CO |
| **Margin by Region** | Geographic profitability | SAP SD + CO |
| **Margin by Segment** | Industry segment margins | SAP SD + CO |
| **Margin Trend** | Historical margin evolution | SAP CO |

### Variance Metrics
| Variance Type | Description | Threshold |
|---------------|-------------|-----------|
| **Material Price Variance** | Standard vs Actual price | ±3% |
| **Material Usage Variance** | Standard vs Actual qty | ±2% |
| **Labor Rate Variance** | Standard vs Actual rate | ±5% |
| **Labor Efficiency Variance** | Standard vs Actual hours | ±5% |
| **Overhead Variance** | Allocated vs Actual | ±10% |

### Cost Reduction Tracking
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Savings Target** | Annual cost reduction goal | Finance |
| **Savings Achieved** | Realized savings YTD | Tracking |
| **Projects in Progress** | Active cost reduction projects | Project Mgmt |
| **Projected Savings** | Expected future savings | Forecasts |
| **VA/VE Savings** | Value engineering benefits | Engineering |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Cost Waterfall** | Cost component breakdown | Plotly Waterfall |
| **Margin Treemap** | Profitability hierarchy | Plotly Treemap |
| **Variance Bar** | Standard vs Actual | Plotly Bar |
| **Trend Line** | Cost/margin over time | Plotly Line |
| **Scatter** | Volume vs Margin | Plotly Scatter |
| **Sunburst** | Cost allocation hierarchy | Plotly Sunburst |
| **Gauge** | Margin indicators | Plotly Indicator |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **SAP CO** | Standard costs, variances | Fivetran | Daily |
| **SAP FI** | Actuals, P&L | Fivetran | Daily |
| **SAP MM** | Material prices, PO costs | Fivetran | 15 min |
| **SAP SD** | Revenue, customer data | Fivetran | 15 min |
| **SAP PP** | Production costs | Fivetran | Daily |
| **Budget System** | Targets, forecasts | Integration | Monthly |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Financial & Costing
CURATED.FACT_PRODUCT_COSTS           -- Standard costs by product
CURATED.FACT_COST_ACTUALS            -- Actual costs incurred
CURATED.FACT_COST_VARIANCES          -- Variance analysis
CURATED.DIM_COST_CENTER              -- Cost center master
CURATED.DIM_COST_ELEMENT             -- Cost element master
CURATED.DIM_PRODUCT                  -- Product master
ANALYTICS.AGG_MARGIN_BY_PRODUCT      -- Product profitability
ANALYTICS.AGG_MARGIN_BY_CUSTOMER     -- Customer profitability
ANALYTICS.V_COST_BREAKDOWN           -- Cost component view
ML.PRED_COST_VARIANCE                -- Predicted variances
```

---

## 💰 Cost Structure Example

### IoT Module Cost Breakdown
| Component | % of Cost | Example ($) |
|-----------|-----------|-------------|
| **Chipset (Qualcomm/MTK)** | 35-40% | $12.00 |
| **Memory/Flash** | 10-12% | $3.50 |
| **RF Components** | 8-10% | $3.00 |
| **Passives** | 5-7% | $2.00 |
| **PCB/Substrate** | 5-6% | $1.80 |
| **Antenna** | 3-4% | $1.20 |
| **CM Labor** | 6-8% | $2.50 |
| **CM Overhead** | 4-5% | $1.50 |
| **Test** | 3-4% | $1.20 |
| **Packaging** | 2-3% | $0.80 |
| **Freight** | 3-5% | $1.50 |
| **Total** | 100% | ~$31.00 |

---

## ❓ Potential Questions & Objections

### Q: "How do you handle standard cost updates?"
**A:** Standard cost roll process:
- Annual standard cost setting
- Quarterly variance analysis
- Mid-year re-costing if needed
- Component cost updates monthly

### Q: "How do you calculate customer profitability?"
**A:** Full P&L by customer:
- Revenue (net of discounts)
- Product COGS (standard + variances)
- Freight/logistics allocated
- SG&A allocated (by revenue %)
- Customer-specific costs

### Q: "What about transfer pricing?
**A:** Intercompany handled via:
- Standard transfer prices by entity
- Arm's length documentation
- Regional cost variations captured
- Currency effects isolated

### Q: "How granular is the cost data?**
**A:** Multiple levels:
- Product family level
- SKU level
- Customer level
- BOM component level
- Cost element level

### Q: "Can you predict cost variances?**
**A:** ML model identifies:
- Components with price volatility
- Suppliers with delivery issues (premium freight)
- Products with yield problems
- Seasonal patterns
- R²: 0.82 on variance prediction

### Q: "How do you track cost reduction initiatives?**
**A:** VA/VE tracking:
- Project registration and target
- Milestone tracking
- Savings validation (before/after)
- Sustainability of savings
- Multi-year impact

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~2 weeks |
| **Prerequisites** | SAP CO access, standard costs defined |
| **Dependencies** | SAP SD for revenue, MM for material costs |
| **Data Cleanup** | Medium - Cost element mapping, allocation rules |
| **Stakeholders** | Finance, Product Management, Procurement |

---

## 🔒 Access Control

| Role | Access Level |
|------|--------------|
| **FINANCE_ANALYST** | Full cost detail |
| **EXECUTIVE** | Summary margins, no component costs |
| **PROCUREMENT** | Material costs only |
| **PRODUCT_MANAGER** | Product margins, no customer detail |
| **GENERAL** | No access (cost data masked) |

---

## 📊 Sample Cost Query

```sql
-- Product Cost Breakdown
SELECT 
    p.product_family,
    p.product_name,
    c.cost_element_type,
    SUM(c.standard_cost) as std_cost,
    SUM(c.actual_cost) as act_cost,
    SUM(c.actual_cost - c.standard_cost) as variance,
    ROUND((SUM(c.actual_cost) - SUM(c.standard_cost)) / 
          NULLIF(SUM(c.standard_cost), 0) * 100, 2) as variance_pct
FROM curated.fact_product_costs c
JOIN curated.dim_product p ON c.product_key = p.product_key
WHERE c.cost_period = DATE_TRUNC('month', CURRENT_DATE())
GROUP BY 1, 2, 3
ORDER BY variance DESC;

-- Customer Profitability
SELECT 
    c.customer_name,
    c.customer_segment,
    SUM(m.revenue_usd) as revenue,
    SUM(m.cogs_usd) as cogs,
    SUM(m.gross_margin_usd) as gross_margin,
    ROUND(SUM(m.gross_margin_usd) / NULLIF(SUM(m.revenue_usd), 0) * 100, 1) as gm_pct,
    SUM(m.allocated_sga_usd) as sga,
    SUM(m.gross_margin_usd - m.allocated_sga_usd) as contribution
FROM analytics.agg_margin_by_customer m
JOIN curated.dim_customer c ON m.customer_key = c.customer_key
WHERE m.year = YEAR(CURRENT_DATE())
GROUP BY 1, 2
ORDER BY revenue DESC;
```

