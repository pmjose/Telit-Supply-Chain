# 📦 Inventory & Shipments Dashboard

## Overview
Comprehensive view of global inventory positions, warehouse operations, inbound/outbound shipments, and logistics performance. Enables inventory optimization, stockout prevention, and shipment tracking across the supply chain.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Summary KPIs and status |
| **📦 Inventory Position** | Stock levels by location and product |
| **📈 Trends** | Historical inventory patterns |
| **🔄 ABC Analysis** | Pareto analysis of inventory value |
| **⚠️ Stockouts & Excess** | Critical inventory alerts |
| **🚚 Inbound** | Incoming shipments and PO status |
| **📤 Outbound** | Customer shipments and deliveries |
| **🗺️ Shipment Map** | Geographic shipment visualization |
| **📊 Carrier Performance** | Logistics provider metrics |
| **📋 Customer Hub Inventory** | VMI/Hub stock at customer sites |
| **⏱️ Lead Times** | Supplier and delivery lead times |

---

## 📊 KPIs & Metrics

### Inventory Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Total Inventory Value** | $ value of all stock | Optimal level | SAP MM (MBEW) |
| **Days of Supply (DOS)** | Inventory / Daily demand | 40-50 days | SAP MM + SD |
| **Inventory Turns** | COGS / Avg Inventory | >8x/year | SAP MM + CO |
| **Fill Rate** | Orders filled from stock | >98% | SAP SD |
| **Stockout SKUs** | Products with zero stock | 0 | SAP MM |

### Inventory by Category
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Raw Materials** | Component inventory value | SAP MM (MARD) |
| **WIP** | Work-in-progress value | MES + SAP PP |
| **Finished Goods** | Completed products | SAP MM |
| **In-Transit** | Goods in shipment | SAP MM (MSKA) |
| **Consignment** | Stock at customer sites | SAP MM (MKOL) |

### ABC Analysis
| Category | % of SKUs | % of Value | Counting Frequency |
|----------|-----------|------------|-------------------|
| **A Items** | 10-20% | 70-80% | Weekly/Daily |
| **B Items** | 20-30% | 15-20% | Monthly |
| **C Items** | 50-70% | 5-10% | Quarterly |

### Shipment Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **On-Time Delivery (OTD)** | Delivered by promised date | >95% | SAP SD (LIKP) |
| **In-Full Delivery (OTIF)** | Full quantity delivered on time | >93% | SAP SD |
| **Shipments in Transit** | Current active shipments | N/A | Carrier APIs |
| **Avg Transit Time** | Order to delivery days | <5 days (domestic) | SAP SD + Carrier |
| **Carrier On-Time %** | By carrier performance | >95% | Carrier APIs |

### Carrier Performance
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **DHL On-Time %** | DHL delivery performance | DHL API |
| **FedEx On-Time %** | FedEx delivery performance | FedEx API |
| **Cost per Shipment** | Avg freight cost | SAP MM (Freight) |
| **Damage Rate** | Damaged shipments % | Claims data |
| **Lead Time Variance** | Actual vs quoted days | Carrier APIs |

### Customer Hub/VMI Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Hub Stock Value** | Inventory at customer hubs | SAP MM (MKOL) |
| **Hub Turns** | Customer consumption rate | SAP SD |
| **Replenishment Accuracy** | Right qty at right time | Customer EDI |
| **Min/Max Compliance** | Stock within agreed levels | VMI System |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **KPI Tiles** | Key metrics with trends | Streamlit metrics |
| **Inventory Treemap** | Stock by category/location | Plotly Treemap |
| **DOS Gauge** | Days of supply indicator | Plotly Indicator |
| **ABC Pareto Chart** | Cumulative value curve | Plotly Bar + Line |
| **Stock Trend Line** | Historical inventory levels | Plotly Line |
| **Shipment Map** | Geographic tracking | Plotly Scatter Geo |
| **Carrier Comparison Bar** | Performance by carrier | Plotly Bar |
| **Lead Time Histogram** | Distribution of lead times | Plotly Histogram |
| **Heatmap** | Stock levels by location/product | Plotly Heatmap |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **SAP MM** | Inventory quantities, values, movements | Fivetran | 15 min |
| **SAP SD** | Shipments, deliveries, orders | Fivetran | 15 min |
| **WMS** | Warehouse transactions, locations | Kafka Connect | 5 min |
| **DHL API** | Tracking, transit status | REST API | On-event |
| **FedEx API** | Tracking, POD | REST API | On-event |
| **Customer EDI** | VMI consumption, forecasts | Snowpipe (X12) | Real-time |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Inventory & Shipments
CURATED.FACT_INVENTORY               -- Daily inventory snapshots
CURATED.FACT_INVENTORY_MOVEMENTS     -- Stock transactions (MSEG)
CURATED.FACT_SHIPMENTS               -- Shipment header/detail
CURATED.DIM_PRODUCT                  -- Product master
CURATED.DIM_LOCATION                 -- Warehouse/plant locations
CURATED.DIM_CARRIER                  -- Carrier master
ANALYTICS.AGG_INVENTORY_DAILY        -- Daily aggregations
ANALYTICS.V_INVENTORY_POSITION       -- Current stock view
ANALYTICS.V_STOCKOUT_RISK            -- At-risk products
ML.PRED_INVENTORY_OPTIMIZATION       -- Optimal stock levels
```

---

## ❓ Potential Questions & Objections

### Q: "How do you value inventory?"
**A:** We pull valuation from SAP MBEW (Material Valuation):
- Standard Cost for planned items
- Moving Average for purchased items
- FIFO/LIFO as configured in SAP

### Q: "Can we see inventory at our CMs?"
**A:** Yes - CM inventory appears in the Customer Hub tab:
- Consignment stock (SAP MKOL)
- VMI stock (customer-reported)
- In-transit to CM (MSKA)

### Q: "How do you calculate Days of Supply?"
**A:** 
```
DOS = Current Stock Quantity / Average Daily Demand (90-day rolling)
```
We use a 90-day rolling average to smooth seasonality.

### Q: "What about safety stock recommendations?"
**A:** The Stockouts & Excess tab includes:
- Min/Max analysis
- Reorder Point alerts
- ML-based demand sensing for dynamic safety stock

### Q: "How do you get real-time carrier tracking?"
**A:** API integrations with major carriers:
- DHL: RESTful Tracking API
- FedEx: Web Services
- UPS: Quantum View
- Ocean: AIS vessel tracking

### Q: "Can you integrate with our 3PL?"
**A:** Yes - common 3PL integrations include:
- EDI 945/947 (Warehouse receipts/adjustments)
- API (most modern WMS have REST APIs)
- SFTP file feeds (legacy systems)

### Q: "What triggers stockout alerts?"
**A:** Multi-factor alerting:
1. Stock < Safety Stock threshold
2. DOS < minimum days
3. Open orders > Available stock
4. Lead time risk (supplier delay + transit)

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~3 weeks |
| **Prerequisites** | SAP MM/SD access, carrier API keys |
| **Dependencies** | WMS integration if separate from SAP |
| **Data Cleanup** | Medium - Material master alignment, location mapping |
| **Stakeholders** | VP Supply Chain, Logistics Manager, Warehouse Ops |

---

## 📊 Sample SQL Query

```sql
-- Current Inventory Position with DOS
SELECT 
    p.product_id,
    p.product_name,
    p.product_family,
    l.location_name,
    i.qty_on_hand,
    i.qty_in_transit,
    i.qty_reserved,
    i.qty_available,
    i.inventory_value_usd,
    d.avg_daily_demand,
    ROUND(i.qty_available / NULLIF(d.avg_daily_demand, 0), 1) as days_of_supply,
    CASE 
        WHEN i.qty_available / NULLIF(d.avg_daily_demand, 0) < 14 THEN 'CRITICAL'
        WHEN i.qty_available / NULLIF(d.avg_daily_demand, 0) < 30 THEN 'LOW'
        WHEN i.qty_available / NULLIF(d.avg_daily_demand, 0) > 90 THEN 'EXCESS'
        ELSE 'HEALTHY'
    END as stock_status
FROM curated.fact_inventory i
JOIN curated.dim_product p ON i.product_key = p.product_key
JOIN curated.dim_location l ON i.location_key = l.location_key
JOIN analytics.agg_demand_90d d ON i.product_key = d.product_key
WHERE i.snapshot_date = CURRENT_DATE();
```

