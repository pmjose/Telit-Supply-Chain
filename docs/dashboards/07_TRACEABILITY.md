# 🔗 Traceability Dashboard

## Overview
End-to-end product genealogy and traceability dashboard enabling complete visibility from raw materials through to final customer delivery. Critical for recall management, compliance, and quality investigations.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Traceability summary and lot status |
| **🔍 Lot Lookup** | Search by lot/serial number |
| **📋 BOM Explosion** | Bill of Materials breakdown |
| **🏭 Production Genealogy** | Manufacturing history |
| **🚚 Shipment History** | Customer delivery tracking |
| **🔄 Recall Simulation** | Impact analysis for recalls |
| **📦 Component Traceability** | Upstream supplier lots |

---

## 📊 KPIs & Metrics

### Traceability Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Traceability Coverage** | % of products with full trace | 100% | MES + SAP |
| **Avg Trace Depth** | Levels of BOM traced | 5+ levels | BOM + MES |
| **Trace Response Time** | Time to complete trace | <1 hour | SLA |
| **Lots in Field** | Active customer lots | Tracking | SAP SD |
| **Open Recalls** | Active recall actions | 0 | QMS |

### Lot-Level Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Production Date** | Manufacturing date | MES |
| **Production Line** | Line/cell used | MES |
| **Operator ID** | Production operator | MES |
| **Component Lots** | Incoming material lots | SAP MM |
| **Test Results** | All test data for lot | MES |
| **Ship-To Locations** | Customer destinations | SAP SD |

### Recall Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Affected Units** | Count of impacted units | Traceability query |
| **Customers Impacted** | # of customers affected | SAP SD |
| **Geographic Spread** | Regions with affected product | SAP SD |
| **Recovery Rate** | % recalled and returned | RMA system |
| **Cost Exposure** | Estimated recall cost | Finance |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Genealogy Tree** | Visual BOM/trace hierarchy | Graphviz |
| **Timeline** | Production-to-ship timeline | Plotly Timeline |
| **World Map** | Shipment locations | Plotly Scatter Geo |
| **Sankey Diagram** | Material flow | Plotly Sankey |
| **Network Graph** | Component relationships | Graphviz |
| **Data Tables** | Lot detail listings | Streamlit DataFrame |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **MES** | Production lots, test data, genealogy | Kafka | Real-time |
| **SAP MM** | Material lots, GR/GI | Fivetran | 15 min |
| **SAP SD** | Shipments, deliveries, customers | Fivetran | 15 min |
| **SAP PP** | Production orders, BOMs | Fivetran | 15 min |
| **WMS** | Warehouse movements | Kafka | 5 min |
| **Serialization** | Serial number assignments | MES | Real-time |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Traceability
CURATED.FACT_PRODUCTION_GENEALOGY    -- Parent-child lot relationships
CURATED.FACT_LOT_HISTORY             -- Lot lifecycle events
CURATED.BRIDGE_BOM                   -- Bill of Materials
CURATED.FACT_SHIPMENTS               -- Customer shipments
CURATED.FACT_GOODS_MOVEMENTS         -- Inventory movements
CURATED.DIM_PRODUCT                  -- Product master with BOM
CURATED.DIM_LOT                      -- Lot/batch master
ANALYTICS.V_TRACE_FORWARD            -- Forward trace (lot → customer)
ANALYTICS.V_TRACE_BACKWARD           -- Backward trace (customer → lots)
```

---

## 🔍 Trace Directions

### Forward Traceability (Lot → Customer)
Starting from a component lot, trace forward to:
1. Which finished goods used this component
2. Which production lots/work orders
3. Which shipments went to which customers
4. Final delivery locations and dates

### Backward Traceability (Customer → Lot)
Starting from a customer complaint, trace backward to:
1. Which lot was shipped to customer
2. When and where it was produced
3. Which component lots were used
4. Supplier lots and receiving dates

---

## ❓ Potential Questions & Objections

### Q: "How fast can you complete a trace?"
**A:** 
- Simple trace (1 lot to customers): <1 minute
- Full recall simulation (component → all affected): <5 minutes
- All data is pre-joined in Snowflake, no cross-system queries

### Q: "What about serial number level tracking?"
**A:** Supported for:
- IoT modules with unique IMEI/serial numbers
- High-value products with individual serialization
- Links to MES, SAP, and customer registration

### Q: "How deep does the BOM explosion go?"
**A:** Typically 5-7 levels:
- Level 0: Finished Good (IoT Module)
- Level 1: Sub-assemblies (PCB, antenna)
- Level 2: Components (ICs, passives)
- Level 3: Raw materials (wafers, substrates)
- Can extend to supplier sub-tier with data sharing

### Q: "Can you trace to our CM's production?"
**A:** Yes - CM data integration provides:
- Production lot linkage
- CM work order traceability
- CM test results
- Shipment to Telit/customer

### Q: "What about compliance requirements (IATF, FDA, etc.)?"
**A:** Dashboard supports:
- Lot-level test record retention (7+ years)
- Production parameter logging
- Electronic batch records
- Audit-ready reporting
- 21 CFR Part 11 compatible data handling

### Q: "How do you handle split lots?"
**A:** Full split/merge tracking:
- Parent lot to child lot relationships
- Quantity tracking through splits
- Merge genealogy for combined lots

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~3 weeks |
| **Prerequisites** | MES lot tracking, SAP batch management |
| **Dependencies** | BOM accuracy, material lot linkage |
| **Data Cleanup** | High - Lot linkage gaps, historical data cleanup |
| **Stakeholders** | Quality, Regulatory, Operations |

---

## 📊 Sample Trace Query

```sql
-- Forward Trace: Component Lot → Customers
WITH RECURSIVE lot_trace AS (
    -- Base: Start with the component lot
    SELECT 
        lot_id,
        product_key,
        parent_lot_id,
        lot_qty,
        1 as trace_level
    FROM curated.dim_lot
    WHERE lot_id = 'COMP-2024-001234'
    
    UNION ALL
    
    -- Recursive: Find child lots (assemblies using this component)
    SELECT 
        g.child_lot_id as lot_id,
        l.product_key,
        g.parent_lot_id,
        g.qty_used as lot_qty,
        t.trace_level + 1
    FROM lot_trace t
    JOIN curated.fact_production_genealogy g ON t.lot_id = g.parent_lot_id
    JOIN curated.dim_lot l ON g.child_lot_id = l.lot_id
    WHERE t.trace_level < 10
)
SELECT 
    t.lot_id,
    p.product_name,
    t.trace_level,
    s.shipment_date,
    c.customer_name,
    s.ship_to_country
FROM lot_trace t
JOIN curated.dim_product p ON t.product_key = p.product_key
LEFT JOIN curated.fact_shipments s ON t.lot_id = s.lot_id
LEFT JOIN curated.dim_customer c ON s.customer_key = c.customer_key
ORDER BY t.trace_level, s.shipment_date;

-- Recall Impact Simulation
SELECT 
    p.product_family,
    COUNT(DISTINCT s.shipment_id) as shipments_affected,
    COUNT(DISTINCT c.customer_id) as customers_affected,
    SUM(s.shipped_qty) as units_affected,
    COUNT(DISTINCT s.ship_to_country) as countries_affected
FROM analytics.v_trace_forward tf
JOIN curated.fact_shipments s ON tf.final_lot_id = s.lot_id
JOIN curated.dim_customer c ON s.customer_key = c.customer_key
JOIN curated.dim_product p ON s.product_key = p.product_key
WHERE tf.source_lot_id = 'COMP-2024-001234'  -- Affected component
GROUP BY p.product_family;
```

