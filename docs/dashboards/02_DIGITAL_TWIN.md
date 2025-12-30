# 🏭 Digital Twin Dashboard

## Overview
Real-time virtual representation of Telit's global manufacturing operations. Provides visibility into production lines, equipment health, environmental conditions, and facility status across all manufacturing sites and Contract Manufacturers (CMs).

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **🌍 Global View** | World map of all manufacturing sites |
| **🏭 Site Details** | Individual facility deep-dive |
| **📊 Production Lines** | Line-by-line status and output |
| **🔧 Equipment Health** | Equipment sensors and predictive maintenance |
| **📈 Live Metrics** | Real-time production gauges |
| **🌡️ Environment** | Temperature, humidity, air quality |
| **⚡ Energy** | Power consumption by facility |
| **🚨 Alerts** | Active alarms and warnings |
| **📉 OEE Tracking** | Overall Equipment Effectiveness |
| **🔮 Predictions** | ML-based failure and output predictions |
| **📋 Summary** | Executive summary for manufacturing |

---

## 📊 KPIs & Metrics

### Global Site Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Total Sites** | Active manufacturing locations | 5+ sites | Master Data |
| **Lines Running** | Production lines in operation | 90%+ | MES Real-time |
| **Units Today** | Total units produced today | Based on plan | MES Production |
| **Global OEE** | Average OEE across all sites | >85% | MES + IoT |

### Site-Level Metrics
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Site Status** | Running/Idle/Down | Running | MES + Alarms |
| **Production Rate** | Units per hour | Per line capacity | MES |
| **Headcount** | Operators on shift | Per schedule | HR/MES |
| **Yield Rate** | Good units / Total units | >98% | MES Quality |

### Equipment Health
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **MTBF** | Mean Time Between Failures | >500 hours | MES + CMMS |
| **MTTR** | Mean Time To Repair | <4 hours | CMMS |
| **Vibration (RMS)** | Equipment vibration level | <2.5 mm/s | IoT Sensors |
| **Temperature** | Equipment operating temp | Per spec | IoT Sensors |
| **Remaining Useful Life (RUL)** | Predicted days until failure | >30 days | ML Model |

### Production Line KPIs
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Cycle Time** | Time per unit | Per product spec | MES |
| **Throughput** | Units per shift | Per plan | MES |
| **Downtime Minutes** | Unplanned downtime | <30 min/shift | MES |
| **Changeover Time** | Time between products | <15 min | MES |

### OEE Components
| Metric | Formula | Target |
|--------|---------|--------|
| **Availability** | Run Time / Planned Time | >95% |
| **Performance** | (Ideal Cycle × Units) / Run Time | >95% |
| **Quality** | Good Units / Total Units | >99% |
| **OEE** | Availability × Performance × Quality | >85% |

### Environmental Monitoring
| Metric | Description | Limits | Data Source |
|--------|-------------|--------|-------------|
| **Temperature** | Ambient temp in production area | 20-25°C | IoT Sensors |
| **Humidity** | Relative humidity | 40-60% RH | IoT Sensors |
| **Air Quality (AQI)** | Particulate levels | <50 | IoT Sensors |
| **ESD Events** | Electrostatic discharge events | 0 | ESD Monitors |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Global Map** | Site locations with status markers | Plotly Scatter Geo |
| **3D Factory Layout** | Visual representation of lines | Custom SVG/HTML |
| **Gauge Charts** | Real-time metric gauges | Plotly Indicator |
| **Equipment Heatmap** | Sensor values by equipment | Plotly Heatmap |
| **OEE Waterfall** | OEE component breakdown | Plotly Waterfall |
| **Time Series** | Equipment sensor trends | Plotly Line |
| **Control Charts** | SPC for quality metrics | Plotly Scatter with limits |
| **Sankey Diagram** | Production flow | Plotly Sankey |
| **Failure Prediction** | RUL countdown | Plotly Indicator |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **MES (Camstar)** | Production counts, quality, WIP | Kafka Connect | Real-time |
| **SCADA** | Equipment sensors, PLCs | Snowpipe | 1 second |
| **IoT Sensors** | Temp, humidity, vibration | Snowpipe (MQTT) | Real-time |
| **CMMS** | Maintenance records, work orders | REST API | 5 min |
| **ERP (SAP PP)** | Production orders, BOMs | Fivetran | 15 min |
| **deviceWISE** | Telit IoT gateway data | REST API | Real-time |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Digital Twin
RAW.IOT_EQUIPMENT_TELEMETRY          -- Raw sensor readings
CURATED.FACT_PRODUCTION              -- Production transactions
CURATED.FACT_EQUIPMENT_STATUS        -- Equipment state changes
CURATED.DIM_EQUIPMENT                -- Equipment master
CURATED.DIM_PRODUCTION_LINE          -- Line configurations
ANALYTICS.AGG_OEE_HOURLY             -- Hourly OEE calculations
ML.PRED_EQUIPMENT_FAILURE            -- Failure predictions
ML.FEAT_EQUIPMENT_HEALTH             -- ML features
```

---

## ❓ Potential Questions & Objections

### Q: "How do you get data from our Contract Manufacturers?"
**A:** Three options:
1. **API Integration** - If CM has MES with API (Foxconn, Flex often do)
2. **File Feeds** - Daily/hourly SFTP files from CM
3. **Supplier Portal** - CM enters data in our portal (Snowflake-hosted)

### Q: "What IoT protocol do you support?"
**A:** Snowpipe ingests data via:
- MQTT (most common for IoT)
- REST/HTTP
- Kafka
- OPC-UA (via gateway)
- Telit's deviceWISE platform

### Q: "We don't have sensors on all equipment"
**A:** Start with critical equipment only. The dashboard works with partial data. We can also use MES data (cycle times, alarms) as proxy for equipment health.

### Q: "How accurate is the failure prediction?"
**A:** Our XGBoost model achieves:
- AUC: 0.92 (ability to distinguish failing vs healthy)
- Precision: 85% (when we predict failure, we're right 85% of time)
- Recall: 78% (we catch 78% of failures)
- Lead time: Average 14 days warning before failure

### Q: "What about data security with CMs?"
**A:** Snowflake Secure Data Sharing ensures:
- CMs only see their own data
- No data leaves Snowflake
- Row-level security by CM_ID
- All access is audited

### Q: "How much sensor data volume can you handle?"
**A:** Snowflake handles massive IoT volumes:
- 50M+ events/day typical
- Sub-second query on recent data
- Automatic clustering for time-series
- Cold storage for historical data

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~4 weeks |
| **Prerequisites** | MES connectivity, IoT sensor deployment |
| **Dependencies** | Network access to factory floor, CM agreements |
| **Data Cleanup** | Medium - Sensor calibration, master data alignment |
| **Stakeholders** | VP Manufacturing, Plant Managers, Maintenance |

---

## 🔌 CM Integration Patterns

### Foxconn Integration
```
Foxconn MES → SFTP (hourly CSV) → Snowpipe → RAW.CM_FOXCONN_*
```

### Flex Integration  
```
Flex API → REST Connector → Snowpipe → RAW.CM_FLEX_*
```

### Common Data Elements from CMs
- Production counts by SKU
- Defect counts by category
- WIP quantities
- Test results
- Shipping confirmations

