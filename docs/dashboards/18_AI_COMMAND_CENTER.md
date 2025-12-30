# 🎛️ AI Command Center Dashboard

## Overview
The AI Command Center is the flagship dashboard showcasing Snowflake's advanced capabilities including Cortex AI, natural language processing, predictive analytics, and decision support tools. It serves as a central hub for executives and supply chain managers to get AI-powered insights and make data-driven decisions.

## Tab Structure

### Tab 1: 🤖 AI Insights (Snowflake Cortex)
Natural language query interface powered by Snowflake Cortex LLM.

### Tab 2: 🎚️ What-If Scenario Simulator
Interactive parameter adjustment to model supply chain disruptions.

### Tab 3: 🔔 Live Critical Alerts
Real-time monitoring of supply chain events requiring immediate attention.

### Tab 4: 🕸️ Interactive Network Graph
Visualization of supplier-component-product-customer relationships.

### Tab 5: ⏱️ Time Machine
Historical performance exploration and trend analysis.

### Tab 6: 💰 ROI Calculator
Investment analysis tool for supply chain intelligence implementation.

---

## Tab 1: AI Insights

### Features
| Feature | Description |
|---------|-------------|
| Natural Language Query | Text input for asking questions in plain English |
| Quick Question Buttons | Pre-built queries for common questions |
| AI-Generated Response | Structured response with findings and recommendations |
| Auto-Generated Insights | Daily insights cards (opportunities, warnings, risks) |
| Anomaly Detection Table | Real-time deviation monitoring |

### KPIs & Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| Query Response Time | Time for Cortex to generate response | < 3 seconds | Cortex API |
| Confidence Score | AI confidence in response accuracy | > 90% | Cortex Model |
| Data Freshness | Age of underlying data | < 5 minutes | ETL Pipeline |
| Anomaly Count | Number of detected deviations | Minimize | Statistical Models |

### Sample Cortex SQL
```sql
-- Natural Language Query using Cortex Complete
SELECT SNOWFLAKE.CORTEX.COMPLETE(
    'snowflake-arctic',
    CONCAT(
        'Based on this supply chain data: ', 
        (SELECT OBJECT_AGG(metric_name, metric_value) FROM supply_chain_metrics),
        ' Answer this question: ', :user_question
    )
) AS ai_response;

-- Anomaly Detection
SELECT 
    metric_name,
    current_value,
    expected_value,
    ABS(current_value - expected_value) / expected_value * 100 AS deviation_pct,
    CASE 
        WHEN deviation_pct > 10 THEN 'Anomaly'
        WHEN deviation_pct > 5 THEN 'Warning'
        ELSE 'Normal'
    END AS status
FROM daily_metrics
WHERE metric_date = CURRENT_DATE;
```

### Data Sources
- `SUPPLY_CHAIN_METRICS` - Aggregated KPIs
- `CORTEX_QUERY_LOG` - Query history and responses
- `ANOMALY_DETECTION_RESULTS` - Statistical analysis outputs

---

## Tab 2: What-If Scenario Simulator

### Scenario Types
| Scenario | Parameters | Impact Areas |
|----------|------------|--------------|
| Supply Disruption | Supplier, Severity %, Duration | Revenue, Production, Lead Time |
| Demand Surge | Product, Increase %, Region | Inventory, Production, Fulfillment |
| Cost Changes | Category, Change % | Margin, Pricing, Profitability |
| Geopolitical Event | Event Type, Probability | Risk Score, Alt Sourcing |
| Capacity Change | Site, Change % | Throughput, Allocation |

### Output Metrics
| Metric | Description | Calculation |
|--------|-------------|-------------|
| Revenue Impact | Projected revenue change | Sum of lost sales + recovery |
| Production Loss | Units not produced | Capacity × Disruption % × Duration |
| Lead Time Impact | Additional days | Base lead time × Impact factor |
| Recovery Time | Weeks to normalize | Based on mitigation actions |

### Sample SQL
```sql
-- Scenario Impact Calculation
WITH scenario_params AS (
    SELECT 
        :affected_supplier AS supplier,
        :disruption_severity / 100 AS severity,
        :duration_weeks AS duration
),
supplier_impact AS (
    SELECT 
        p.product_id,
        p.product_name,
        s.weekly_volume * sp.severity * sp.duration AS lost_units,
        s.weekly_volume * sp.severity * sp.duration * p.unit_price AS lost_revenue
    FROM supplier_products s
    JOIN products p ON s.product_id = p.product_id
    CROSS JOIN scenario_params sp
    WHERE s.supplier_name = sp.supplier
)
SELECT 
    SUM(lost_units) AS total_lost_units,
    SUM(lost_revenue) AS total_lost_revenue,
    COUNT(DISTINCT product_id) AS affected_products
FROM supplier_impact;
```

---

## Tab 3: Live Critical Alerts

### Alert Severity Levels
| Level | Color | Response Time | Escalation |
|-------|-------|---------------|------------|
| Critical | 🔴 Red | Immediate | VP + C-Suite |
| High | 🟠 Orange | < 4 hours | Director |
| Medium | 🟡 Yellow | < 24 hours | Manager |
| Low | 🟢 Green | < 1 week | Analyst |

### Alert Categories
- **Supply**: Supplier delays, shortages, quality issues
- **Production**: Equipment failures, yield drops, capacity issues
- **Logistics**: Shipping delays, port congestion, carrier issues
- **Quality**: Defect spikes, customer complaints, certification issues
- **Compliance**: Regulatory changes, certification expirations
- **Financial**: Cost overruns, currency fluctuations, credit risks

### KPIs
| Metric | Target | Current |
|--------|--------|---------|
| Critical Alert Count | 0-2 | 3 |
| Mean Time to Acknowledge | < 15 min | 12 min |
| Mean Time to Resolve | < 4 hours | 3.2 hours |
| Alert Accuracy | > 95% | 97% |

### Sample SQL
```sql
-- Active Critical Alerts
SELECT 
    alert_id,
    alert_title,
    severity,
    TIMESTAMPDIFF('minute', created_at, CURRENT_TIMESTAMP) AS age_minutes,
    impact_description,
    affected_products,
    assigned_owner,
    status
FROM supply_chain_alerts
WHERE severity IN ('CRITICAL', 'HIGH')
  AND status NOT IN ('RESOLVED', 'CLOSED')
ORDER BY 
    CASE severity WHEN 'CRITICAL' THEN 1 WHEN 'HIGH' THEN 2 END,
    created_at;
```

---

## Tab 4: Interactive Network Graph

### Node Types
| Type | Count | Attributes |
|------|-------|------------|
| Suppliers | 8 | Name, Location, Risk Score, Spend |
| Components | 8 | Part Number, Category, Lead Time |
| Products | 4 | SKU, Revenue, Volume |
| Customers | 6 | Name, Segment, Revenue |

### Edge Types
| Relationship | Description | Weight |
|--------------|-------------|--------|
| Supplier → Component | Supply relationship | Spend $ |
| Component → Product | BOM relationship | Quantity |
| Product → Customer | Sales relationship | Revenue |

### Network Metrics
| Metric | Description | Value |
|--------|-------------|-------|
| Total Nodes | All entities in network | 26 |
| Total Edges | All relationships | 42 |
| Single-Source Risk | Components with 1 supplier | 3 |
| Avg Path Length | Hops from supplier to customer | 3.2 |
| Network Resilience | Redundancy score | 72% |

### Sample SQL
```sql
-- Build Network Graph Data
-- Nodes
SELECT 'supplier' AS node_type, supplier_id AS node_id, supplier_name AS label
FROM dim_suppliers
UNION ALL
SELECT 'component', component_id, component_name FROM dim_components
UNION ALL
SELECT 'product', product_id, product_name FROM dim_products
UNION ALL
SELECT 'customer', customer_id, customer_name FROM dim_customers;

-- Edges
SELECT 
    'supply' AS edge_type,
    supplier_id AS source,
    component_id AS target,
    annual_spend AS weight
FROM supplier_components
UNION ALL
SELECT 'bom', component_id, product_id, quantity FROM bom_details
UNION ALL
SELECT 'sales', product_id, customer_id, revenue FROM customer_products;
```

---

## Tab 5: Time Machine

### Time Ranges
| Period | Granularity | Use Case |
|--------|-------------|----------|
| Last 7 days | Hourly | Operational issues |
| Last 30 days | Daily | Trend analysis |
| Last 12 months | Weekly/Monthly | Strategic planning |
| YTD vs PY | Monthly | Performance review |

### Historical Metrics Tracked
- Revenue by product/region
- OTD Rate
- Quality FPY
- Inventory Value & DOS
- Production Volume
- Supplier Performance

### Event Timeline
Significant events captured:
- Design wins
- Production starts
- Supply disruptions
- Quality incidents
- Certification milestones
- Contract signings

### Sample SQL
```sql
-- Historical KPI Trend
SELECT 
    DATE_TRUNC(:granularity, metric_date) AS period,
    AVG(otd_rate) AS avg_otd,
    AVG(fpy_rate) AS avg_fpy,
    SUM(revenue) AS total_revenue,
    AVG(inventory_dos) AS avg_dos
FROM daily_supply_chain_metrics
WHERE metric_date BETWEEN :start_date AND :end_date
GROUP BY 1
ORDER BY 1;

-- Significant Events
SELECT event_date, event_type, event_description, impact_type
FROM supply_chain_events
WHERE event_date BETWEEN :start_date AND :end_date
ORDER BY event_date DESC;
```

---

## Tab 6: ROI Calculator

### Input Parameters
| Category | Parameter | Default | Range |
|----------|-----------|---------|-------|
| Revenue | Annual Revenue ($M) | 500 | 10-10,000 |
| Volume | Annual Units (K) | 6,000 | 100-100,000 |
| Pricing | Avg Unit Price ($) | 85 | 1-1,000 |
| Performance | Current OTD (%) | 88 | 70-99 |
| Performance | Current FPY (%) | 96.5 | 90-99.9 |
| Inventory | Current DOS | 45 | 20-90 |
| Costs | COGS (% of Rev) | 62 | 40-80 |
| Costs | Logistics (% of Rev) | 6 | 2-15 |
| Costs | Expedite ($K/year) | 850 | 0-10,000 |
| Operations | Manual Hours/Week | 40 | 0-200 |
| Issues | Stockouts/Year | 12 | 0-100 |
| Issues | Quality Escapes/Year | 8 | 0-50 |

### Savings Calculations
| Category | Improvement | Calculation |
|----------|-------------|-------------|
| Expedite Reduction | 30% | Current × 0.30 |
| Inventory Carrying | 15% DOS reduction | Revenue × COGS% × (DOS reduction / 365) × 10% |
| Labor Efficiency | 70% automation | Hours × 52 × $75 × 0.70 |
| Quality Improvement | 50% fewer escapes | Escapes × $25K × 0.50 |
| Stockout Prevention | 60% reduction | Events × (Revenue/365/10) × 0.60 |

### ROI Outputs
| Metric | Formula |
|--------|---------|
| Annual Savings | Sum of all savings categories |
| Year 1 ROI | (Savings - Implementation - License) / (Implementation + License) |
| 3-Year ROI | (Savings×3 - Implementation - License×3) / (Implementation + License×3) |
| Payback Period | (Implementation + License) / (Savings / 12) |

### Cost Assumptions
- Implementation: $350,000 (one-time)
- Annual Snowflake License: $180,000

---

## Implementation Notes

### Snowflake Features Used
| Feature | Purpose |
|---------|---------|
| Cortex Complete | Natural language AI responses |
| Cortex Sentiment | Analyze supplier communications |
| Dynamic Tables | Real-time alert aggregation |
| Streams & Tasks | Alert trigger automation |
| Time Travel | Historical data exploration |
| Secure Views | ROI data sharing |

### Prerequisites
- Snowflake Enterprise Edition (for Cortex)
- Cortex functions enabled in account
- Real-time data feeds for alerts
- Historical data warehouse (2+ years)

### Security Considerations
- Row-level security on sensitive ROI data
- Audit logging for AI queries
- PII masking in Cortex prompts

---

## Q&A Preparation

### Likely Questions
1. **"How accurate is the Cortex AI?"**
   - Response: Cortex uses state-of-the-art LLMs trained on enterprise data patterns. Accuracy depends on data quality. We see 90%+ confidence scores on well-structured supply chain queries.

2. **"Can we customize the scenarios?"**
   - Response: Yes, the What-If simulator is fully configurable. We can add custom scenario types specific to your risk profile.

3. **"How quickly do alerts trigger?"**
   - Response: Alerts process every 5 minutes via Snowflake Streams. Critical alerts can be pushed to Slack/Teams within 30 seconds.

4. **"Is the ROI calculation realistic?"**
   - Response: The calculator uses industry benchmarks from supply chain transformations. Actual results vary but are typically within 20% of projections.

5. **"What data do we need for the Network Graph?"**
   - Response: We need supplier master, BOM data, customer master, and transaction history. Most companies have 80% of this in ERP systems.

### Objection Handling
| Objection | Response |
|-----------|----------|
| "AI sounds expensive" | Cortex is included in Enterprise license. ROI typically covers costs in 6-9 months. |
| "Our data isn't clean enough" | We include data profiling and cleansing in implementation. Cortex handles imperfect data well. |
| "We already have BI tools" | This isn't replacement—it's augmentation with AI capabilities your current tools don't have. |
| "Security concerns with AI" | All data stays in your Snowflake account. No data leaves to external AI services. |


