# 🔄 Product Lifecycle Dashboard

## Overview
Product lifecycle management dashboard covering new product introduction (NPI), active products, end-of-life (EOL) management, and 4G/5G technology transitions. Critical for portfolio planning and customer communication.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Lifecycle summary and portfolio status |
| **🚀 NPI Pipeline** | New product introductions |
| **✅ Active Products** | Current production products |
| **⏳ EOL Planning** | End-of-life timeline |
| **📞 LTB (Last Time Buy)** | Last order opportunities |
| **🔄 4G→5G Transition** | Technology migration tracking |

---

## 📊 KPIs & Metrics

### Portfolio Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Total SKUs** | Active product count | Optimized | PLM |
| **NPI in Progress** | Products in development | Pipeline | PLM |
| **Products EOL This Year** | Planned EOLs | Managed | PLM |
| **5G Product %** | 5G as % of portfolio | Growing | PLM |
| **Avg Product Lifespan** | Years from launch to EOL | 5-7 years | Historical |

### Lifecycle Stage Distribution
| Stage | Description | Typical Duration |
|-------|-------------|------------------|
| **Concept** | Initial feasibility | 3-6 months |
| **Development** | Engineering development | 6-12 months |
| **Qualification** | Certification & testing | 3-6 months |
| **Pilot** | Limited production | 1-3 months |
| **Ramp** | Production ramp-up | 3-6 months |
| **Active** | Full production | 3-5 years |
| **Mature** | Declining demand | 1-3 years |
| **EOL Announced** | EOL communication sent | 6-12 months |
| **Last Time Buy** | Final order window | 3-6 months |
| **End of Production** | No new orders | - |
| **End of Support** | No support | 3-5 years after EOP |

### NPI Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Time to Market** | Concept to production | <18 months | PLM |
| **NPI On-Track** | Projects on schedule | >90% | Project Mgmt |
| **First Pass Qual** | Qualification pass rate | >80% | Test Data |
| **Design Wins at Launch** | Customers at launch | >5 | Salesforce |
| **Certification Ready** | Certs at launch | All major | Cert DB |

### EOL Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **EOL Revenue Impact** | Revenue at risk | SAP SD |
| **Customer Count** | Customers to migrate | SAP SD |
| **Replacement Product** | Successor product | PLM |
| **LTB Orders Received** | Last orders placed | SAP SD |
| **Migration Rate** | % moved to successor | Tracking |

### Technology Transition (4G → 5G)
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **4G Products Active** | LTE/LTE-M products | PLM |
| **5G Products Active** | 5G/5G NR products | PLM |
| **5G Revenue %** | Revenue from 5G | SAP SD |
| **Transition Timeline** | By-product migration dates | Planning |
| **Customer 5G Adoption** | % customers on 5G | Salesforce |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Portfolio Pie/Donut** | Products by lifecycle stage | Plotly Pie |
| **Gantt Chart** | NPI and EOL timelines | Plotly Timeline |
| **Roadmap Timeline** | Product roadmap view | Custom/Plotly |
| **Technology Transition** | 4G to 5G migration | Plotly Area |
| **Revenue Impact Bar** | EOL revenue at risk | Plotly Bar |
| **NPI Funnel** | Development pipeline | Plotly Funnel |
| **Heatmap** | Product × Customer EOL impact | Plotly Heatmap |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **PLM (Teamcenter)** | Product master, lifecycle stage | REST API | Hourly |
| **SAP SD** | Revenue by product | Fivetran | 15 min |
| **Salesforce** | Design wins, opportunities | Fivetran | 30 min |
| **Project Management** | NPI milestones, status | API | Daily |
| **Certification DB** | Cert status by product | API | Daily |
| **Customer Portal** | EOL acknowledgments | Integration | Real-time |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Product Lifecycle
CURATED.DIM_PRODUCT                  -- Product master with lifecycle
CURATED.FACT_PRODUCT_LIFECYCLE       -- Lifecycle stage changes
CURATED.FACT_NPI_MILESTONES          -- NPI project milestones
CURATED.FACT_EOL_COMMUNICATIONS      -- EOL notices sent
CURATED.FACT_LTB_ORDERS              -- Last time buy orders
ANALYTICS.AGG_REVENUE_BY_PRODUCT     -- Product revenue trends
ANALYTICS.V_EOL_IMPACT               -- EOL customer impact view
ANALYTICS.V_TECHNOLOGY_MIX           -- 4G/5G revenue breakdown
ML.PRED_EOL_TIMING                   -- Predicted optimal EOL dates
```

---

## 📱 Telit Product Families

### Current Portfolio (Example)
| Family | Technology | Status | Successor |
|--------|------------|--------|-----------|
| **LE910Cx** | LTE Cat-1 | Active | LE910C4-NF |
| **ME910C1** | LTE-M/NB-IoT | Active | - |
| **FN980** | 5G Sub-6 | Active | FN990 |
| **FN990** | 5G mmWave | NPI | - |
| **LE910Bx** | LTE Cat-4 | EOL Announced | LE910Cx |
| **HE910** | 3G | End of Sale | LE910Cx |
| **GE910** | 2G | End of Support | ME310G1 |

### Technology Roadmap
| Year | Focus | Key Products |
|------|-------|--------------|
| 2024 | 5G expansion | FN990, FN920 |
| 2025 | 5G RedCap | New family |
| 2026 | 6G R&D | Research phase |

---

## ❓ Potential Questions & Objections

### Q: "How do you determine EOL timing?"
**A:** Multi-factor analysis:
- Revenue trend (declining >30% YoY)
- Component availability
- Technology obsolescence (2G/3G sunset)
- Customer migration readiness
- ML model for optimal timing

### Q: "How do you manage customer communication?"
**A:** Structured process:
1. EOL announcement (12+ months notice)
2. Last Time Buy notification (6 months)
3. Individual customer outreach (by revenue)
4. Migration support offering
5. End of support reminder

### Q: "What about 2G/3G sunset impact?"
**A:** Network sunset tracking:
- Carrier sunset dates by country
- Products affected by network type
- Customer impact by geography
- Proactive migration campaigns

### Q: "Can you predict which products need EOL?**
**A:** ML model considers:
- Revenue velocity and trend
- Customer concentration (risk if key customer leaves)
- Component lifecycle status
- Competitive positioning
- Carrier roadmaps

### Q: "How do you handle Last Time Buy?**
**A:** Structured LTB process:
- LTB window announcement (typically 90 days)
- Customer allocation based on history
- Buffer stock build recommendations
- Extended support offerings
- Clear communication of end dates

### Q: "What about cross-sell to successor products?"
**A:** Integrated with Salesforce:
- Automatic successor recommendations
- Migration path documentation
- Design support for transitions
- Incentive programs tracking

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~2 weeks |
| **Prerequisites** | PLM access, product master alignment |
| **Dependencies** | SAP for revenue data, Salesforce for customers |
| **Data Cleanup** | Medium - Lifecycle stage alignment, product hierarchy |
| **Stakeholders** | Product Management, Sales, Customer Success |

---

## 📊 Sample Lifecycle Query

```sql
-- EOL Impact Analysis
SELECT 
    p.product_name,
    p.product_family,
    p.lifecycle_stage,
    p.eol_announced_date,
    p.end_of_production_date,
    p.successor_product_id,
    COUNT(DISTINCT c.customer_id) as affected_customers,
    SUM(r.revenue_last_12m) as revenue_at_risk,
    STRING_AGG(DISTINCT c.customer_name, ', ') as top_customers
FROM curated.dim_product p
JOIN analytics.agg_revenue_by_product r ON p.product_key = r.product_key
JOIN curated.fact_orders o ON p.product_key = o.product_key
JOIN curated.dim_customer c ON o.customer_key = c.customer_key
WHERE p.lifecycle_stage IN ('EOL Announced', 'Last Time Buy')
  AND r.year = YEAR(CURRENT_DATE())
GROUP BY 1, 2, 3, 4, 5, 6
ORDER BY revenue_at_risk DESC;

-- 4G to 5G Technology Mix Trend
SELECT 
    DATE_TRUNC('month', order_date) as month,
    CASE 
        WHEN p.technology IN ('5G', '5G NR', '5G mmWave') THEN '5G'
        WHEN p.technology IN ('LTE', 'LTE-M', 'NB-IoT', 'Cat-1', 'Cat-4') THEN '4G'
        ELSE '2G/3G'
    END as technology_group,
    SUM(revenue_usd) as revenue,
    COUNT(DISTINCT customer_key) as customer_count
FROM curated.fact_orders o
JOIN curated.dim_product p ON o.product_key = p.product_key
WHERE order_date >= DATEADD('year', -2, CURRENT_DATE())
GROUP BY 1, 2
ORDER BY 1, 2;
```

