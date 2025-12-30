# 📋 Customer Orders Dashboard

## Overview
End-to-end customer order management dashboard covering order intake, backlog, fulfillment status, and customer service levels. Provides visibility into order-to-cash process and customer satisfaction metrics.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Order summary and key metrics |
| **📈 Order Intake** | New orders and booking trends |
| **📋 Backlog** | Open orders and aging |
| **🚚 Fulfillment** | Shipment and delivery status |
| **👥 Customer View** | Orders by customer |
| **⚠️ Exceptions** | At-risk orders and escalations |

---

## 📊 KPIs & Metrics

### Order Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Orders Today** | Orders received today | Tracking | SAP SD |
| **Backlog Value** | Open order value | Managed | SAP SD (VBAK) |
| **Book-to-Bill Ratio** | Orders ÷ Shipments | >1.0 | SAP SD |
| **Avg Order Value** | $ per order | Tracking | SAP SD |
| **Order Fill Rate** | Orders filled complete | >95% | SAP SD |

### Order Intake Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Orders This Week** | Weekly order count | SAP SD |
| **Revenue Booked** | Order value this week | SAP SD |
| **YoY Order Growth** | Compared to prior year | SAP SD |
| **Orders by Region** | Geographic distribution | SAP SD |
| **Orders by Segment** | Industry segment mix | SAP SD + CRM |

### Backlog Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Backlog Units** | Units on open orders | Tracking | SAP SD |
| **Backlog Value** | $ value of backlog | Tracking | SAP SD |
| **Backlog Aging** | Orders by age bucket | <30 days avg | SAP SD |
| **Past Due Orders** | Orders beyond promised date | 0 | SAP SD |
| **Weeks of Backlog** | Backlog ÷ Weekly shipments | 4-6 weeks | Calculated |

### Fulfillment Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **On-Time Delivery (OTD)** | Shipped by promised date | >95% | SAP SD |
| **OTIF** | On-time and in-full | >93% | SAP SD |
| **Avg Days to Ship** | Order to shipment days | <3 days | SAP SD |
| **Partial Shipments** | Orders shipped partial | <5% | SAP SD |
| **Shipment Accuracy** | Correct product/qty | >99.5% | SAP SD |

### Customer Service Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Customer Requests** | Open inquiries | Trending down | CRM |
| **Avg Response Time** | Hours to first response | <4 hours | CRM |
| **Order Amendments** | Change requests | Tracking | SAP SD |
| **Escalations** | Critical customer issues | 0 | CRM |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Order Trend Line** | Daily/weekly order intake | Plotly Line |
| **Backlog Waterfall** | In vs Out vs Current | Plotly Waterfall |
| **Aging Histogram** | Order age distribution | Plotly Bar |
| **Customer Treemap** | Orders by customer | Plotly Treemap |
| **Regional Map** | Orders by geography | Plotly Choropleth |
| **Fulfillment Funnel** | Order to delivery stages | Plotly Funnel |
| **OTD Gauge** | On-time delivery indicator | Plotly Indicator |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **SAP SD** | Orders, deliveries, invoices | Fivetran | 15 min |
| **Customer Portal** | Online orders, inquiries | API | Real-time |
| **EDI** | EDI 850 orders | Snowpipe | Real-time |
| **CRM (Salesforce)** | Customer requests, escalations | Fivetran | 30 min |
| **WMS** | Pick/pack/ship status | Kafka | 5 min |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Customer Orders
CURATED.FACT_ORDERS                  -- Order header (VBAK)
CURATED.FACT_ORDER_ITEMS             -- Order lines (VBAP)
CURATED.FACT_DELIVERIES              -- Delivery docs (LIKP, LIPS)
CURATED.FACT_INVOICES                -- Billing (VBRK, VBRP)
CURATED.DIM_CUSTOMER                 -- Customer master
CURATED.DIM_PRODUCT                  -- Product master
ANALYTICS.AGG_ORDERS_DAILY           -- Daily order aggregation
ANALYTICS.V_ORDER_BACKLOG            -- Current backlog view
ANALYTICS.V_ORDER_FULFILLMENT        -- Fulfillment status
ML.PRED_ORDER_RISK                   -- At-risk order predictions
```

---

## 📋 Order Status Flow

```
Order Received → Order Confirmed → Allocated → Picked → Packed → Shipped → Delivered → Invoiced
     ↓               ↓                ↓          ↓        ↓          ↓           ↓
   [NEW]         [CONFIRMED]     [ALLOCATED] [PICKING] [PACKED]  [SHIPPED]  [COMPLETE]
                      ↓
                [CREDIT BLOCK] → [RELEASED]
                      ↓
                 [ON HOLD] → [RELEASED]
```

---

## ❓ Potential Questions & Objections

### Q: "How real-time is order visibility?"
**A:** Multiple tiers:
- EDI orders: Real-time via Snowpipe
- Portal orders: Real-time via API
- SAP order changes: 15-minute refresh
- Shipment status: 5-minute via WMS

### Q: "Can customers see their own orders?"
**A:** Yes, via Secure Data Sharing:
- Customer-specific portal view
- Row-level security by customer ID
- No data duplication
- Real-time visibility

### Q: "How do you calculate OTD?"
**A:** 
```
OTD = Orders shipped by confirmed date / Total orders shipped × 100%
```
- Confirmed date used (not requested date)
- Partial shipments count as on-time if first ship is on-time
- Customer-caused delays excluded

### Q: "What about order exceptions?**
**A:** Exception tracking includes:
- Credit holds
- Inventory allocation failures
- Shipping exceptions
- Customer-requested holds
- Past due with no ship date

### Q: "How do you prioritize orders?"
**A:** Allocation rules:
1. Strategic customer tier
2. Order date (FIFO)
3. Contract commitments
4. Revenue value
5. Geographic routing optimization

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~2 weeks |
| **Prerequisites** | SAP SD access, EDI setup |
| **Dependencies** | WMS for ship status, CRM for escalations |
| **Data Cleanup** | Low - Standard SAP extracts |
| **Stakeholders** | Customer Service, Sales, Logistics |

---

## 📊 Sample Order Query

```sql
-- Order Backlog Summary
SELECT 
    c.customer_name,
    c.customer_segment,
    COUNT(DISTINCT o.order_id) as open_orders,
    SUM(oi.order_qty - COALESCE(oi.shipped_qty, 0)) as backlog_units,
    SUM((oi.order_qty - COALESCE(oi.shipped_qty, 0)) * oi.unit_price) as backlog_value,
    MIN(o.confirmed_date) as oldest_order_date,
    SUM(CASE WHEN o.confirmed_date < CURRENT_DATE() THEN 1 ELSE 0 END) as past_due_orders
FROM curated.fact_orders o
JOIN curated.fact_order_items oi ON o.order_key = oi.order_key
JOIN curated.dim_customer c ON o.customer_key = c.customer_key
WHERE o.order_status NOT IN ('SHIPPED', 'CANCELLED', 'COMPLETE')
GROUP BY 1, 2
ORDER BY backlog_value DESC;

-- OTD Trend by Week
SELECT 
    DATE_TRUNC('week', shipped_date) as week,
    COUNT(*) as total_orders,
    SUM(CASE WHEN shipped_date <= confirmed_date THEN 1 ELSE 0 END) as on_time,
    ROUND(SUM(CASE WHEN shipped_date <= confirmed_date THEN 1 ELSE 0 END) * 100.0 
          / COUNT(*), 1) as otd_pct
FROM curated.fact_deliveries
WHERE shipped_date >= DATEADD('month', -6, CURRENT_DATE())
GROUP BY 1
ORDER BY 1;
```

