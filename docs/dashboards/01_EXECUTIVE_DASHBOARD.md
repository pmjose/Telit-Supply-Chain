# 📊 Executive Dashboard

## Overview
High-level business dashboard providing CIOs, VPs, and executives with a real-time unified view of critical supply chain KPIs. Enables rapid decision-making, identifies trends, and highlights areas requiring strategic intervention.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📈 Overview** | Executive summary with scorecards and top issues |
| **💰 Financial** | Revenue, margins, costs, profitability |
| **🏭 Operations** | Production, inventory, shipments status |
| **🎯 Customers & Market** | Design wins, customer revenue, market share |
| **⚠️ Alerts & AI** | AI-generated insights and recommendations |

---

## 📊 KPIs & Metrics

### Overview Tab
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Revenue YTD** | Year-to-date revenue | $500M+ | SAP FI (BKPF, BSEG) |
| **Gross Margin** | (Revenue - COGS) / Revenue | >38% | SAP CO (COEP) |
| **On-Time Delivery (OTD)** | Orders delivered by promised date | >95% | SAP SD (LIKP, LIPS) |
| **Quality FPY** | First Pass Yield | >98% | MES Quality Module |
| **Inventory Days** | Days of Supply on hand | 40-50 days | SAP MM (MARD, MBEW) |
| **Design Wins** | New customer/project wins YTD | >40/year | Salesforce Opportunities |

### Executive Scorecard
| Scorecard | Grade Scale | Components |
|-----------|-------------|------------|
| Financial Health | A/B/C/D/F | Revenue growth, margin trend, cash flow |
| Supply Chain | A/B/C/D/F | OTD, inventory turns, supplier performance |
| Risk Exposure | A/B/C/D/F | Geo risk, single-source, financial risk |
| Customer Satisfaction | A/B/C/D/F | NPS, quality escapes, response time |

### Financial Tab
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Operating Income** | EBIT | SAP FI/CO |
| **COGS** | Cost of Goods Sold | SAP CO (Product Costing) |
| **R&D Spend** | R&D as % of Revenue | SAP CO (Cost Centers) |
| **Revenue by Segment** | Industrial, Automotive, Enterprise | SAP SD + CRM |
| **Revenue by Region** | EMEA, Americas, APAC | SAP SD (Ship-to country) |

### Operations Tab
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Production Output** | Units produced per site | MES Production Records |
| **Inventory Value** | Total $ in inventory | SAP MM (MBEW) |
| **Open POs** | Open purchase orders count | SAP MM (EKKO, EKPO) |
| **Backlog Value** | Unfulfilled order value | SAP SD (VBAK, VBAP) |
| **Site Status** | Green/Yellow/Red by facility | MES + IoT Sensors |

### Customers & Market Tab
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Active Design Wins** | Projects in design phase | Salesforce Opportunities |
| **Customer Revenue Mix** | Top 10 customer revenue | SAP SD (VBRK) |
| **Market Segment Growth** | YoY by segment | SAP SD + Market Data |
| **Win Rate** | Won / (Won + Lost) | Salesforce |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **KPI Tiles** | At-a-glance metrics with delta | Streamlit metrics |
| **Scorecard Cards** | Letter grades with color coding | Custom HTML/CSS |
| **Revenue vs Target Bar** | Quarterly actuals vs plan | Plotly Bar + Scatter |
| **Revenue by Region Pie** | Regional revenue distribution | Plotly Pie (donut) |
| **Revenue Trend Area** | 12-month revenue trend | Plotly Area |
| **Cost Structure Bar** | Horizontal cost breakdown | Plotly Bar |
| **Segment Pie** | Revenue by business segment | Plotly Pie |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **SAP S/4HANA FI** | Revenue, costs, P&L | Fivetran SAP Connector | 15 min |
| **SAP S/4HANA SD** | Orders, deliveries, backlog | Fivetran SAP Connector | 15 min |
| **SAP S/4HANA MM** | Inventory, POs | Fivetran SAP Connector | 15 min |
| **SAP S/4HANA CO** | Cost centers, margins | Fivetran SAP Connector | 1 hour |
| **Salesforce CRM** | Design wins, pipeline | Fivetran Salesforce | 30 min |
| **MES (Camstar)** | Production output, quality | Kafka Connect | Real-time |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Executive Dashboard
ANALYTICS.AGG_REVENUE_DAILY          -- Daily revenue aggregations
ANALYTICS.AGG_MARGIN_BY_PRODUCT      -- Product-level margins
CURATED.FACT_ORDERS                  -- Order details
CURATED.FACT_INVENTORY               -- Inventory positions
CURATED.DIM_CUSTOMER                 -- Customer master
CURATED.DIM_PRODUCT                  -- Product master
ML.PRED_DEMAND_FORECAST              -- AI demand predictions
```

---

## ❓ Potential Questions & Objections

### Q: "How real-time is this data?"
**A:** SAP data refreshes every 15 minutes. MES production data is real-time via Kafka streaming. Financial close data updates hourly. All timestamps are visible in the dashboard header.

### Q: "We already have SAP reports - why do we need this?"
**A:** SAP reports are transactional and siloed. This dashboard combines SAP with MES, CRM, and external data into a single view. Plus, we add AI-powered insights that SAP doesn't provide.

### Q: "Can we drill down from these KPIs?"
**A:** Yes - each metric links to its detailed dashboard (e.g., clicking OTD goes to Inventory & Shipments). We also support click-through to source transactions.

### Q: "How do you calculate the scorecard grades?"
**A:** Each scorecard uses a weighted scoring model:
- Financial: Revenue growth (40%), Margin trend (30%), Cash flow (30%)
- Supply Chain: OTD (40%), Inventory turns (30%), Supplier score (30%)
- Grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)

### Q: "What if we use a different ERP than SAP?"
**A:** Snowflake connectors exist for Oracle, NetSuite, Dynamics 365, and most ERPs. The dashboard logic stays the same - only the data ingestion changes.

### Q: "Who has access to financial data?"
**A:** Role-based access control (RBAC) ensures only EXECUTIVE and FINANCE_ANALYST roles see cost and margin data. Others see operational metrics only.

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~2 weeks |
| **Prerequisites** | SAP access credentials, KPI definitions agreed |
| **Dependencies** | SAP SD, MM, FI/CO extracts, Salesforce connection |
| **Data Cleanup** | Low - Standard ERP extracts |
| **Stakeholders** | CFO, VP Operations, VP Sales |

