# 🏗️ Architecture Dashboard

## Overview
Technical architecture documentation and implementation blueprint for the Telit Supply Chain Intelligence Platform. Provides complete visibility into data sources, data model, ETL pipelines, Snowflake configuration, ML models, infrastructure, integrations, code structure, and governance.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **🏛️ Overview** | High-level architecture diagram |
| **🗄️ Data Sources** | All integrated systems |
| **📐 Data Model** | ERD and schema design |
| **🔄 ETL/Pipelines** | Data pipeline inventory |
| **❄️ Snowflake** | Snowflake-specific configuration |
| **🤖 ML/Analytics** | Machine learning models |
| **🖥️ Infrastructure** | DevOps and deployment |
| **🔌 Integrations** | External APIs and shares |
| **📁 Code Structure** | Repository layout |
| **🔐 Governance** | Security and compliance |

---

## 📊 Platform Statistics

| Metric | Value |
|--------|-------|
| **Dashboards** | 17 |
| **Data Sources** | 18 |
| **Tables** | 85+ |
| **ML Models** | 12 |
| **Pipelines** | 24 |
| **APIs** | 10 |
| **Users** | 500+ |
| **Uptime SLA** | 99.9% |

---

## 🏛️ Architecture Layers

### 1. Data Sources Layer
| Category | Sources |
|----------|---------|
| **ERP** | SAP S/4HANA (SD, MM, PP, FI/CO) |
| **CRM** | Salesforce |
| **Manufacturing** | MES (Camstar), PLM (Teamcenter) |
| **IoT** | deviceWISE, SCADA, sensors |
| **Quality** | LIMS, QMS |
| **External** | Weather, D&B, Bloomberg |
| **CM** | Foxconn, Flex (SFTP/API) |
| **B2B** | EDI X12 (850/856/830) |

### 2. Ingestion Layer
| Method | Use Case | Volume |
|--------|----------|--------|
| **Fivetran** | SAP, Salesforce (batch) | ~5M rows/day |
| **Kafka + Snowpipe** | MES, IoT (streaming) | ~50M events/day |
| **Snowpipe REST** | APIs (real-time) | ~1M records/day |
| **Internal Stage** | Files (batch) | Variable |
| **Data Marketplace** | External data | ~1M records/day |

### 3. Storage Layer (Snowflake)
| Schema | Purpose | Retention |
|--------|---------|-----------|
| **RAW** | Landing zone | 7 days |
| **STAGING** | Cleansed data | 30 days |
| **CURATED** | Business-ready | 7 years |
| **ANALYTICS** | Aggregations | 3 years |
| **ML** | Features/predictions | 1 year |
| **APP** | Application views | N/A |

### 4. Transform Layer
| Tool | Purpose |
|------|---------|
| **dbt** | SQL transformations, testing |
| **Dynamic Tables** | Incremental materialization |
| **Snowpark** | Python transformations |
| **Tasks** | Orchestration |

### 5. Compute Layer
| Capability | Technology |
|------------|------------|
| **ML Training** | Snowpark ML |
| **LLM Functions** | Cortex AI |
| **Forecasting** | Cortex FORECAST |
| **Streaming** | Snowpipe |

### 6. Application Layer
| Component | Technology |
|-----------|------------|
| **Dashboards** | Streamlit |
| **Sharing** | Secure Data Sharing |
| **Marketplace** | Native Apps (future) |
| **API** | Snowflake REST API |

---

## 📐 Data Model Overview

### Dimension Tables
| Table | Description |
|-------|-------------|
| DIM_PRODUCT | Product master (families, SKUs) |
| DIM_CUSTOMER | Customer master (segments, regions) |
| DIM_SUPPLIER | Supplier master (tiers, risk) |
| DIM_LOCATION | Facilities and warehouses |
| DIM_DATE | Date dimension |
| DIM_EQUIPMENT | Equipment master |
| DIM_CARRIER | Carrier master |
| DIM_CM_SITE | Contract manufacturer sites |

### Fact Tables
| Table | Grain | Volume |
|-------|-------|--------|
| FACT_INVENTORY | Product × Location × Day | ~2M rows/day |
| FACT_ORDERS | Order line | ~50K rows/day |
| FACT_PRODUCTION | Production record | ~5M rows/day |
| FACT_QUALITY | Test result | ~200K rows/day |
| FACT_SHIPMENTS | Shipment | ~10K rows/day |
| FACT_CERTIFICATIONS | Certification record | ~5K rows |

---

## 🤖 ML Model Inventory

| Model | Algorithm | Accuracy | Use Case |
|-------|-----------|----------|----------|
| Demand Forecast | Prophet + Cortex | MAPE 8.2% | Demand planning |
| Equipment Failure | XGBoost | AUC 0.92 | Predictive maintenance |
| Quality Prediction | Random Forest | F1 0.89 | Quality risk |
| Supplier Risk | Ensemble | — | Risk scoring |
| RMA Root Cause | Cortex LLM + RF | F1 0.84 | Failure analysis |
| EOL Impact | Survival Analysis | C-Index 0.81 | Lifecycle planning |

---

## 🔐 Governance & Security

### Access Control
| Control | Implementation |
|---------|----------------|
| Authentication | SSO (Okta) + MFA |
| Authorization | RBAC (24 roles) |
| Row-Level Security | Secure Views |
| Column Masking | Dynamic Masking Policies |
| Network | AWS PrivateLink |

### Data Classification
| Level | Examples |
|-------|----------|
| **Restricted** | PII, salaries, passwords |
| **Confidential** | Costs, margins, contracts |
| **Internal** | Inventory, production |
| **Public** | Product specs |

### Compliance
| Standard | Status |
|----------|--------|
| SOC 2 Type II | ✅ Certified |
| GDPR | ✅ Compliant |
| ISO 27001 | ✅ Certified |
| PCI DSS Level 1 | ✅ Certified |

---

## 📊 Visualizations in Architecture Dashboard

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Architecture Diagram** | System overview | Graphviz |
| **Data Flow Diagram** | Source to dashboard | Graphviz |
| **ERD** | Data model | Graphviz |
| **Role Hierarchy** | RBAC structure | Graphviz |
| **Pipeline Diagram** | ETL flow | Graphviz |
| **Data Tables** | Configurations | Streamlit DataFrame |

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| **Data Platform** | Snowflake Enterprise |
| **Ingestion** | Fivetran, Snowpipe, Kafka |
| **Transformation** | dbt, Dynamic Tables |
| **ML/AI** | Snowpark ML, Cortex AI |
| **Visualization** | Streamlit, Plotly |
| **DevOps** | GitHub Actions, Terraform |
| **Monitoring** | Query History, Datadog |

---

## ❓ Potential Questions & Objections

### Q: "Why Snowflake vs other platforms?"
**A:** Snowflake advantages:
- Native Streamlit hosting
- Cortex AI (built-in LLM/ML)
- Secure Data Sharing (no data copies)
- Consumption-based pricing
- Near-zero administration

### Q: "How do you handle data freshness?"
**A:** Multi-tier latency:
- Real-time: Snowpipe (<1 minute)
- Near real-time: Dynamic Tables (1-5 minutes)
- Batch: dbt (hourly)
- All latencies visible in dashboards

### Q: "What about disaster recovery?"
**A:** Snowflake DR features:
- Time Travel (90 days)
- Fail-safe (7 days additional)
- Cross-region replication (optional)
- Zero-copy clones for testing

### Q: "How scalable is this architecture?"
**A:** Snowflake scalability:
- Separate storage and compute
- Multi-cluster warehouses (auto-scale)
- 50M+ events/day proven
- Petabyte-scale capable

### Q: "What about data lineage?"
**A:** Lineage tracked via:
- dbt documentation
- Snowflake ACCESS_HISTORY
- Column-level lineage in Enterprise+
- Audit logging for compliance

### Q: "How do you handle schema changes?"
**A:** Change management:
- Schemachange for migrations
- Blue/green deployments
- CI/CD with GitHub Actions
- Automated testing

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Platform** | Snowflake Enterprise Edition |
| **Region** | AWS us-east-1 (primary) |
| **Environments** | DEV, QA, PROD |
| **Monthly Compute** | ~$5,000 estimated |
| **Monthly Storage** | ~$500 estimated |
| **Support Level** | Premier |

---

## 📁 Repository Structure

```
telit-supply-chain/
├── snowflake_app/
│   ├── streamlit_app.py      # Main application
│   ├── components/           # UI components
│   ├── data/                 # Query layer
│   └── ml/                   # ML utilities
├── dbt/
│   ├── models/              # 125 SQL models
│   ├── tests/               # 380 tests
│   └── macros/              # Reusable SQL
├── terraform/
│   └── snowflake/           # IaC for Snowflake
├── .github/
│   └── workflows/           # CI/CD pipelines
├── docs/
│   └── dashboards/          # This documentation
└── tests/
    └── unit/                # Python tests
```

