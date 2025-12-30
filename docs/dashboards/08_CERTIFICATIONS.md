# 📱 Certifications Dashboard

## Overview
Carrier and regulatory certification tracking dashboard for IoT modules. Manages certification status across global carriers (AT&T, Verizon, T-Mobile, Vodafone, etc.) and regional regulatory bodies (FCC, CE, PTCRB, GCF). Critical for go-to-market timing and compliance.

---

## 📑 Tabs Structure

| Tab | Purpose |
|-----|---------|
| **📊 Overview** | Certification summary and status |
| **📱 Carrier Certifications** | Status by carrier (AT&T, Verizon, etc.) |
| **🌍 Regional Certifications** | FCC, CE, IC, TELEC, etc. |
| **📅 Certification Calendar** | Timeline and deadlines |
| **⚠️ Expiring Soon** | Renewals and expirations |
| **📋 Test Status** | Certification test progress |

---

## 📊 KPIs & Metrics

### Certification Overview
| Metric | Description | Target | Data Source |
|--------|-------------|--------|-------------|
| **Active Certifications** | Valid certifications count | All products | Cert Database |
| **Pending Certifications** | In-progress certifications | Minimize | Cert Database |
| **Expiring in 90 Days** | Renewals needed | 0 surprises | Cert Database |
| **Certification Coverage** | % products certified | 100% by launch | Cert Database |
| **Avg Certification Time** | Days to certify | <45 days | Historical |

### Carrier Certification Status
| Carrier | Region | Certification Body | Typical Timeline |
|---------|--------|---------------------|------------------|
| **AT&T** | USA | AT&T IOT Lab | 6-8 weeks |
| **Verizon** | USA | Verizon Open Development | 8-10 weeks |
| **T-Mobile** | USA | T-Mobile Device Lab | 4-6 weeks |
| **Vodafone** | EMEA | Vodafone IoT Lab | 4-6 weeks |
| **Deutsche Telekom** | EMEA | DT Hub:raum | 4-6 weeks |
| **NTT DoCoMo** | Japan | DoCoMo Device Lab | 6-8 weeks |
| **China Mobile** | China | CMCC Lab | 8-12 weeks |

### Regional Regulatory Certifications
| Region | Certification | Authority | Validity |
|--------|---------------|-----------|----------|
| **USA** | FCC | Federal Communications Commission | Perpetual |
| **USA/Canada** | PTCRB | PTCRB | 2 years |
| **Europe** | CE Mark | EU | Perpetual (with DoC) |
| **Europe** | GCF | Global Certification Forum | Ongoing |
| **Canada** | IC | Innovation Canada | Perpetual |
| **Japan** | TELEC/JATE | MIC | Perpetual |
| **Australia** | RCM | ACMA | Perpetual |
| **China** | CCC/SRRC | MIIT | 5 years |
| **Korea** | KC | KCC | Perpetual |
| **Brazil** | ANATEL | ANATEL | 2 years |

### Test Status Metrics
| Metric | Description | Data Source |
|--------|-------------|-------------|
| **Tests Passed** | Certification tests passed | Test Labs |
| **Tests Failed** | Tests requiring rework | Test Labs |
| **Tests Pending** | Tests in queue | Test Labs |
| **First Time Pass Rate** | % passing first attempt | Test History |
| **Avg Retest Cycles** | Iterations to pass | Test History |

---

## 📈 Visualizations

| Chart Type | Purpose | Library |
|------------|---------|---------|
| **Status Matrix** | Carrier × Product status | Plotly Heatmap |
| **Timeline/Gantt** | Certification schedule | Plotly Timeline |
| **World Map** | Regional cert coverage | Plotly Choropleth |
| **Progress Bars** | Test completion % | Custom HTML |
| **Calendar Heatmap** | Expiration dates | Plotly Heatmap |
| **Funnel Chart** | Certification pipeline | Plotly Funnel |

---

## 🗄️ Data Sources

| Source System | Data Elements | Connection | Refresh |
|--------------|---------------|------------|---------|
| **PTCRB Portal** | PTCRB certification status | API | Daily |
| **GCF Portal** | GCF certification status | API/Manual | Daily |
| **Carrier Portals** | Individual carrier status | API/Manual | Daily |
| **Test Lab System** | Test results, reports | Integration | Real-time |
| **PLM (Teamcenter)** | Product configurations | REST API | Hourly |
| **Internal Cert DB** | Master certification records | Direct | Real-time |

---

## 🔧 Key Tables (Snowflake)

```sql
-- Core tables for Certifications
CURATED.FACT_CERTIFICATIONS          -- Certification records
CURATED.FACT_CERTIFICATION_TESTS     -- Test results
CURATED.DIM_CARRIER                  -- Carrier master
CURATED.DIM_CERTIFICATION_TYPE       -- Cert type master
CURATED.DIM_PRODUCT                  -- Product master
CURATED.BRIDGE_PRODUCT_CARRIER       -- Product-carrier mapping
ANALYTICS.V_CERT_STATUS              -- Current cert status view
ANALYTICS.V_CERT_EXPIRING            -- Expiring certifications
ML.PRED_CERT_DELAY_RISK              -- Delay risk predictions
```

---

## 📱 IoT Module Certification Types

### Carrier Certifications
| Type | Purpose | Required For |
|------|---------|--------------|
| **PTCRB** | North America cellular | AT&T, T-Mobile, US Cellular |
| **Verizon OD** | Verizon network access | Verizon |
| **GCF** | Global interoperability | European/Asian carriers |
| **AT&T IOT** | AT&T IoT network | AT&T IoT plans |
| **Carrier Specific** | Network optimization | Premium support |

### Regulatory Certifications
| Type | Region | Requirements |
|------|--------|--------------|
| **FCC Part 15/22/24/27** | USA | RF emissions, SAR |
| **CE RED** | Europe | Radio Equipment Directive |
| **IC RSS** | Canada | Radio standards |
| **TELEC** | Japan | Radio law compliance |
| **SRRC** | China | Radio type approval |
| **RCM** | Australia/NZ | Regulatory compliance mark |

---

## ❓ Potential Questions & Objections

### Q: "How do you track certifications across 50+ carriers?"
**A:** Centralized database with:
- API feeds from PTCRB/GCF portals
- Manual updates from carrier portals
- Automated expiration alerting
- Product-carrier mapping matrix

### Q: "What happens when a cert expires?"
**A:** Multi-stage process:
1. 90-day advance warning
2. 60-day escalation to management
3. 30-day critical alert
4. Auto-generated renewal task
5. Tracking through recertification

### Q: "How do you handle firmware updates affecting certs?"
**A:** Change impact analysis:
- Firmware version linked to certifications
- Delta analysis for SW-only changes
- Re-certification trigger rules
- Carrier notification requirements

### Q: "Can you predict certification delays?"
**A:** ML model predicts:
- Based on product complexity
- Test lab capacity
- Historical carrier performance
- Seasonal patterns (holiday slowdowns)
- Accuracy: 88% within ±1 week

### Q: "How do you manage carrier-specific requirements?"
**A:** Carrier profile database:
- Unique test requirements per carrier
- Documentation requirements
- Contact information
- SLA expectations
- Historical performance

### Q: "What about China certifications (CCC, SRRC, NAL)?
**A:** Special handling for China:
- Longer timelines (8-12 weeks)
- Local representative required
- Annual inspection requirements
- Import license linkage
- Separate tracking workflow

---

## 📋 Implementation Notes

| Aspect | Detail |
|--------|--------|
| **Estimated Effort** | ~2 weeks |
| **Prerequisites** | Certification database, portal access |
| **Dependencies** | PLM for product configs, test lab integration |
| **Data Cleanup** | Medium - Historical cert record consolidation |
| **Stakeholders** | Regulatory, Product Management, Sales |

---

## 📊 Sample Certification Query

```sql
-- Certification Status Matrix by Product × Carrier
SELECT 
    p.product_name,
    p.product_family,
    c.carrier_name,
    cert.certification_type,
    cert.certification_status,
    cert.issue_date,
    cert.expiry_date,
    DATEDIFF('day', CURRENT_DATE(), cert.expiry_date) as days_to_expiry,
    CASE 
        WHEN DATEDIFF('day', CURRENT_DATE(), cert.expiry_date) < 30 THEN 'CRITICAL'
        WHEN DATEDIFF('day', CURRENT_DATE(), cert.expiry_date) < 90 THEN 'WARNING'
        ELSE 'OK'
    END as expiry_status
FROM curated.fact_certifications cert
JOIN curated.dim_product p ON cert.product_key = p.product_key
JOIN curated.dim_carrier c ON cert.carrier_key = c.carrier_key
WHERE cert.certification_status = 'ACTIVE'
ORDER BY days_to_expiry ASC;

-- Certification Pipeline by Status
SELECT 
    certification_status,
    COUNT(*) as cert_count,
    AVG(DATEDIFF('day', submission_date, 
        COALESCE(approval_date, CURRENT_DATE()))) as avg_days
FROM curated.fact_certifications
WHERE submission_date >= DATEADD('year', -1, CURRENT_DATE())
GROUP BY certification_status
ORDER BY 
    CASE certification_status 
        WHEN 'PENDING' THEN 1 
        WHEN 'IN_TESTING' THEN 2 
        WHEN 'APPROVED' THEN 3 
        WHEN 'REJECTED' THEN 4 
    END;
```

