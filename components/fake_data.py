"""
Telit Supply Chain - Fake Data Generators
Generates realistic fake data for all dashboards
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Seed for reproducibility
np.random.seed(42)
random.seed(42)

# =============================================================================
# TELIT PRODUCT DATA
# =============================================================================

TELIT_PRODUCTS = [
    # Cellular LPWA - LTE-M & NB-IoT (for Smart Meters, Asset Trackers)
    {"sku": "ME310G1-W1", "name": "ME310G1 LTE-M/NB-IoT", "category": "Cellular LPWA", "price": 24.50},
    {"sku": "ME310G1-WW", "name": "ME310G1 Global LPWA", "category": "Cellular LPWA", "price": 26.00},
    {"sku": "NE310H2-W1", "name": "NE310H2 NB-IoT", "category": "Cellular LPWA", "price": 19.00},
    # Cellular 5G - Sub-6 & mmWave (for V2X, Industrial IoT)
    {"sku": "FN990A28-WW", "name": "FN990A 5G Sub-6", "category": "Cellular 5G", "price": 125.00},
    {"sku": "FN990A40-WW", "name": "FN990A 5G mmWave", "category": "Cellular 5G", "price": 165.00},
    {"sku": "FN980-NA", "name": "FN980 5G RedCap", "category": "Cellular 5G", "price": 89.00},
    # Cellular LTE - Cat 1/4/6/12 (for Telematics, Fleet Management)
    {"sku": "LE910C4-NF", "name": "LE910C4 LTE Cat-4", "category": "Cellular LTE", "price": 42.00},
    {"sku": "LE910C1-NA", "name": "LE910C1 LTE Cat-1", "category": "Cellular LTE", "price": 32.00},
    {"sku": "LM960A18", "name": "LM960 LTE Cat-12", "category": "Cellular LTE", "price": 58.00},
    # Positioning/GNSS (for Fleet Tracking, Agriculture)
    {"sku": "SE868K3-A", "name": "SE868K3 GNSS L1", "category": "Positioning", "price": 18.50},
    {"sku": "SE873Q5-A", "name": "SE873Q5 RTK L1+L5", "category": "Positioning", "price": 45.00},
    {"sku": "SE869K5-DR", "name": "SE869K5-DR Dead Reckoning", "category": "Positioning", "price": 52.00},
    # Wi-Fi & Bluetooth (for Smart Buildings, Retail)
    {"sku": "WE310F5", "name": "WE310F5 Wi-Fi 5", "category": "Wi-Fi & Bluetooth", "price": 15.00},
    {"sku": "WE310F6", "name": "WE310F6 Wi-Fi 6", "category": "Wi-Fi & Bluetooth", "price": 22.00},
    {"sku": "BlueMod+S50", "name": "BlueMod+S50 BLE 5.0", "category": "Wi-Fi & Bluetooth", "price": 12.00},
    # Smart Modules (for EV Charging, Smart City)
    {"sku": "SE920A9", "name": "SE920 Android Smart Module", "category": "Smart Modules", "price": 85.00},
]

WAREHOUSES = [
    # Telit Cinterion Global Locations
    {"id": "WH-IT-TS", "name": "Trieste HQ", "country": "Italy", "region": "EMEA", "lat": 45.6495, "lon": 13.7768, "capacity": 75000},
    {"id": "WH-US-CA", "name": "Irvine (Americas)", "country": "USA", "region": "Americas", "lat": 33.6846, "lon": -117.8265, "capacity": 50000},
    {"id": "WH-DE-MU", "name": "Munich Hub", "country": "Germany", "region": "EMEA", "lat": 48.1351, "lon": 11.5820, "capacity": 45000},
    {"id": "WH-CN-SH", "name": "Shanghai DC", "country": "China", "region": "APAC", "lat": 31.2304, "lon": 121.4737, "capacity": 60000},
    {"id": "WH-SG-SG", "name": "Singapore Hub", "country": "Singapore", "region": "APAC", "lat": 1.3521, "lon": 103.8198, "capacity": 40000},
    {"id": "WH-IL-TLV", "name": "Tel Aviv R&D", "country": "Israel", "region": "EMEA", "lat": 32.0853, "lon": 34.7818, "capacity": 20000},
    {"id": "WH-JP-TK", "name": "Tokyo DC", "country": "Japan", "region": "APAC", "lat": 35.6762, "lon": 139.6503, "capacity": 25000},
    {"id": "WH-BR-SP", "name": "São Paulo DC", "country": "Brazil", "region": "Americas", "lat": -23.5505, "lon": -46.6333, "capacity": 20000},
]

SUPPLIERS = [
    {"id": "SUP-001", "name": "Taiwan Semiconductor", "country": "Taiwan", "category": "Chipsets", "tier": 1},
    {"id": "SUP-002", "name": "Samsung Electronics", "country": "South Korea", "category": "Memory", "tier": 1},
    {"id": "SUP-003", "name": "Murata Manufacturing", "country": "Japan", "category": "Passives", "tier": 1},
    {"id": "SUP-004", "name": "Qualcomm", "country": "USA", "category": "Modems", "tier": 1},
    {"id": "SUP-005", "name": "Skyworks Solutions", "country": "USA", "category": "RF Components", "tier": 2},
    {"id": "SUP-006", "name": "TDK Corporation", "country": "Japan", "category": "Inductors", "tier": 2},
    {"id": "SUP-007", "name": "Yageo Corporation", "country": "Taiwan", "category": "Resistors", "tier": 2},
    {"id": "SUP-008", "name": "Amphenol", "country": "USA", "category": "Connectors", "tier": 2},
]

# Telit Cinterion Key Customers by Industry Vertical
CUSTOMERS = [
    # Smart Energy & Utilities (Smart Meters)
    "Landis+Gyr", "Itron Inc", "Honeywell Elster",
    # Telematics & Transport (Fleet Management)
    "Continental AG", "Geotab", "CalAmp",
    # Automotive (V2X, Connected Cars)
    "BMW Group", "Stellantis", "Volvo Trucks",
    # Healthcare (Medical IoT)
    "Medtronic", "Philips Healthcare",
    # EV Charging Infrastructure
    "ChargePoint", "ABB E-mobility",
    # Agriculture & Precision Farming
    "John Deere", "AGCO Corporation",
    # Retail & Payment (POS, Vending)
    "Ingenico", "NCR Corporation",
    # Smart Buildings & Security
    "Johnson Controls", "Honeywell Building Tech"
]

# =============================================================================
# EXECUTIVE DASHBOARD DATA
# =============================================================================

def get_executive_kpis():
    """Generate executive-level KPIs"""
    return {
        "revenue": {"value": 247.8, "change": 12.3, "unit": "M"},
        "orders_in_transit": {"value": 1247, "change": 8.2, "unit": ""},
        "inventory_value": {"value": 89.4, "change": -2.1, "unit": "M"},
        "on_time_delivery": {"value": 94.7, "change": 1.8, "unit": "%"},
        "active_suppliers": {"value": 48, "change": 4.2, "unit": ""},
        "manufacturing_oee": {"value": 87.3, "change": 2.1, "unit": "%"},
        "defect_rate": {"value": 0.8, "change": -15.2, "unit": "%"},
        "carbon_footprint": {"value": 12450, "change": -8.5, "unit": "tons"},
    }

def get_revenue_by_region():
    """Generate revenue by region data"""
    return pd.DataFrame([
        {"region": "Americas", "revenue": 98.5, "growth": 14.2},
        {"region": "EMEA", "revenue": 82.3, "growth": 11.5},
        {"region": "APAC", "revenue": 67.0, "growth": 18.7},
    ])

def get_revenue_trend(days=30):
    """Generate daily revenue trend"""
    dates = [datetime.now() - timedelta(days=x) for x in range(days, 0, -1)]
    base = 8.0
    revenue = [base + np.sin(i/5) * 1.5 + np.random.normal(0, 0.3) + i*0.02 for i in range(days)]
    return pd.DataFrame({"date": dates, "revenue": revenue})

def get_top_products():
    """Generate top products by sales"""
    products = TELIT_PRODUCTS.copy()
    for p in products:
        p["units_sold"] = random.randint(5000, 50000)
        p["revenue"] = p["units_sold"] * p["price"]
    return sorted(products, key=lambda x: x["revenue"], reverse=True)[:8]

def get_active_alerts():
    """Generate active alerts"""
    return [
        {"type": "critical", "message": "Low stock alert: FN990A 5G module below reorder point at Shanghai DC", "time": "2 min ago"},
        {"type": "warning", "message": "Supplier delay: Qualcomm SDX62 chipset shipment delayed by 3 days", "time": "1 hour ago"},
        {"type": "warning", "message": "Quality alert: RF calibration drift detected on SMT Line 2 (FN990A)", "time": "3 hours ago"},
        {"type": "info", "message": "New order received: 50,000 units ME310G1 LTE-M from Landis+Gyr for smart meters", "time": "4 hours ago"},
        {"type": "success", "message": "Shipment delivered: Order #ORD-2024-8847 to Continental AG (fleet telematics)", "time": "5 hours ago"},
    ]

# =============================================================================
# INVENTORY DATA
# =============================================================================

def get_inventory_levels():
    """Generate inventory levels by warehouse and product"""
    data = []
    for wh in WAREHOUSES:
        for prod in TELIT_PRODUCTS:
            stock = random.randint(100, 5000)
            reorder_point = random.randint(200, 800)
            data.append({
                "warehouse_id": wh["id"],
                "warehouse_name": wh["name"],
                "region": wh["region"],
                "sku": prod["sku"],
                "product_name": prod["name"],
                "category": prod["category"],
                "current_stock": stock,
                "reorder_point": reorder_point,
                "status": "Low Stock" if stock < reorder_point else "OK",
                "days_of_supply": round(stock / random.randint(20, 100), 1),
            })
    return pd.DataFrame(data)

def get_warehouse_summary():
    """Generate warehouse summary data"""
    data = []
    for wh in WAREHOUSES:
        utilization = random.uniform(0.45, 0.95)
        data.append({
            **wh,
            "current_units": int(wh["capacity"] * utilization),
            "utilization": utilization * 100,
            "inbound_shipments": random.randint(5, 25),
            "outbound_shipments": random.randint(10, 40),
        })
    return pd.DataFrame(data)

# =============================================================================
# SUPPLY CHAIN VISIBILITY DATA
# =============================================================================

def get_active_shipments():
    """Generate active shipment data"""
    statuses = ["In Transit", "Customs Clearance", "At Hub", "Out for Delivery", "Delivered"]
    carriers = ["DHL Express", "FedEx", "UPS", "Maersk", "Kuehne+Nagel"]
    
    data = []
    for i in range(50):
        origin = random.choice(WAREHOUSES)
        dest = random.choice([w for w in WAREHOUSES if w["id"] != origin["id"]])
        status = random.choice(statuses)
        
        data.append({
            "shipment_id": f"SHP-2024-{10000+i}",
            "origin": origin["name"],
            "origin_lat": origin["lat"],
            "origin_lon": origin["lon"],
            "destination": dest["name"],
            "dest_lat": dest["lat"],
            "dest_lon": dest["lon"],
            "status": status,
            "carrier": random.choice(carriers),
            "eta": (datetime.now() + timedelta(days=random.randint(1, 14))).strftime("%Y-%m-%d"),
            "weight_kg": random.randint(50, 500),
            "value": random.randint(10000, 250000),
            "progress": random.randint(10, 100) if status != "Delivered" else 100,
        })
    return pd.DataFrame(data)

# =============================================================================
# DEMAND FORECASTING DATA
# =============================================================================

def get_demand_forecast(months=12):
    """Generate demand forecast with predictions"""
    dates = [datetime.now() + timedelta(days=30*x) for x in range(-6, months)]
    data = []
    
    for prod in TELIT_PRODUCTS[:6]:
        base_demand = random.randint(3000, 15000)
        for i, date in enumerate(dates):
            is_forecast = i >= 6
            seasonality = np.sin(i * np.pi / 6) * base_demand * 0.2
            trend = i * base_demand * 0.01
            noise = np.random.normal(0, base_demand * 0.05) if not is_forecast else 0
            
            demand = max(0, base_demand + seasonality + trend + noise)
            
            data.append({
                "date": date,
                "product": prod["name"],
                "sku": prod["sku"],
                "demand": int(demand),
                "lower_bound": int(demand * 0.85) if is_forecast else None,
                "upper_bound": int(demand * 1.15) if is_forecast else None,
                "is_forecast": is_forecast,
            })
    
    return pd.DataFrame(data)

# =============================================================================
# SUPPLIER PERFORMANCE DATA
# =============================================================================

def get_supplier_performance():
    """Generate supplier performance metrics"""
    data = []
    for sup in SUPPLIERS:
        data.append({
            **sup,
            "on_time_delivery": round(random.uniform(0.85, 0.99), 3) * 100,
            "quality_score": round(random.uniform(0.90, 0.995), 3) * 100,
            "lead_time_days": random.randint(14, 45),
            "cost_variance": round(random.uniform(-5, 8), 1),
            "responsiveness": round(random.uniform(0.80, 0.98), 2) * 100,
            "risk_score": round(random.uniform(0.1, 0.4), 2),
            "spend_ytd": random.randint(500000, 5000000),
            "orders_ytd": random.randint(50, 200),
        })
    return pd.DataFrame(data)

# =============================================================================
# QUALITY CONTROL DATA
# =============================================================================

def get_quality_metrics():
    """Generate quality control metrics"""
    return {
        "first_pass_yield": 98.7,
        "defect_rate": 0.8,
        "scrap_rate": 0.3,
        "rework_rate": 0.5,
        "customer_returns": 0.12,
        "quality_cost": 145000,
    }

def get_defect_data():
    """Generate defect pareto data"""
    defect_types = [
        "Solder Bridge", "Missing Component", "Misalignment", "Cold Solder",
        "Tombstone", "Component Damage", "Wrong Component", "PCB Defect"
    ]
    data = []
    total = 0
    for i, defect in enumerate(defect_types):
        count = int(1000 * (0.5 ** (i * 0.7)))
        total += count
        data.append({"defect_type": defect, "count": count})
    
    cumulative = 0
    for d in data:
        cumulative += d["count"]
        d["cumulative_pct"] = cumulative / total * 100
    
    return pd.DataFrame(data)

def get_control_chart_data(days=30):
    """Generate SPC control chart data"""
    dates = [datetime.now() - timedelta(days=x) for x in range(days, 0, -1)]
    mean = 2.5
    ucl = 3.5
    lcl = 1.5
    
    values = [mean + np.random.normal(0, 0.3) for _ in range(days)]
    # Add some out-of-control points
    values[10] = 3.8
    values[22] = 1.2
    
    return pd.DataFrame({
        "date": dates,
        "value": values,
        "mean": [mean] * days,
        "ucl": [ucl] * days,
        "lcl": [lcl] * days,
    })

# =============================================================================
# LOGISTICS DATA
# =============================================================================

def get_fleet_data():
    """Generate fleet tracking data"""
    vehicles = []
    for i in range(20):
        lat = random.uniform(25, 50)
        lon = random.uniform(-120, -70)
        vehicles.append({
            "vehicle_id": f"TRK-{1000+i}",
            "driver": f"Driver {i+1}",
            "status": random.choice(["En Route", "Delivering", "Returning", "Idle"]),
            "lat": lat,
            "lon": lon,
            "speed_mph": random.randint(0, 65),
            "fuel_level": random.randint(20, 100),
            "eta": (datetime.now() + timedelta(hours=random.randint(1, 24))).strftime("%H:%M"),
            "deliveries_today": random.randint(0, 12),
        })
    return pd.DataFrame(vehicles)

def get_delivery_kpis():
    """Generate delivery KPIs"""
    return {
        "on_time_rate": 94.7,
        "avg_delivery_time": 2.3,
        "deliveries_today": 847,
        "active_vehicles": 18,
        "fuel_efficiency": 8.2,
        "customer_satisfaction": 4.7,
    }

# =============================================================================
# COMPONENT TRACEABILITY DATA
# =============================================================================

def get_component_genealogy(batch_id="BATCH-2024-001"):
    """Generate component genealogy tree data"""
    return {
        "batch_id": batch_id,
        "product": "ME310G1-W1",
        "production_date": "2024-12-15",
        "quantity": 5000,
        "components": [
            {
                "name": "Qualcomm MDM9206",
                "supplier": "Qualcomm",
                "lot": "QC-2024-8847",
                "quantity": 5000,
            },
            {
                "name": "Samsung K4B4G16",
                "supplier": "Samsung Electronics",
                "lot": "SS-2024-1122",
                "quantity": 5000,
            },
            {
                "name": "Murata LQH32CN",
                "supplier": "Murata Manufacturing",
                "lot": "MU-2024-3344",
                "quantity": 25000,
            },
            {
                "name": "TDK MLZ2012",
                "supplier": "TDK Corporation",
                "lot": "TDK-2024-5566",
                "quantity": 15000,
            },
        ],
        "test_results": {
            "passed": 4987,
            "failed": 13,
            "yield": 99.74,
        },
        "shipped_to": ["Automotive OEM Alpha", "Fleet Management Inc"],
    }

# =============================================================================
# CARBON / ESG DATA
# =============================================================================

def get_carbon_metrics():
    """Generate carbon footprint and ESG metrics"""
    return {
        "scope1_emissions": 3200,
        "scope2_emissions": 7800,
        "scope3_emissions": 1450,
        "total_emissions": 12450,
        "yoy_reduction": 8.5,
        "renewable_energy_pct": 62,
        "waste_diverted_pct": 78,
        "water_recycled_pct": 45,
        "carbon_target": 10000,
        "carbon_progress": 75,
    }

def get_emissions_trend(months=12):
    """Generate emissions trend data"""
    dates = [datetime.now() - timedelta(days=30*x) for x in range(months, 0, -1)]
    base = 1200
    emissions = [base - (i * 15) + np.random.normal(0, 50) for i in range(months)]
    return pd.DataFrame({"date": dates, "emissions": emissions})

# =============================================================================
# PREDICTIVE MAINTENANCE DATA
# =============================================================================

def get_equipment_health():
    """Generate equipment health data"""
    equipment = [
        {"id": "SMT-001", "name": "SMT Line 1 - Pick & Place", "type": "SMT", "location": "Production Floor A"},
        {"id": "SMT-002", "name": "SMT Line 2 - Pick & Place", "type": "SMT", "location": "Production Floor A"},
        {"id": "SMT-003", "name": "Reflow Oven 1", "type": "Oven", "location": "Production Floor A"},
        {"id": "AOI-001", "name": "AOI Station 1", "type": "Inspection", "location": "Quality Lab"},
        {"id": "AOI-002", "name": "AOI Station 2", "type": "Inspection", "location": "Quality Lab"},
        {"id": "TEST-001", "name": "Functional Tester 1", "type": "Testing", "location": "Test Area"},
        {"id": "TEST-002", "name": "Functional Tester 2", "type": "Testing", "location": "Test Area"},
        {"id": "PKG-001", "name": "Packaging Line 1", "type": "Packaging", "location": "Shipping Area"},
    ]
    
    for eq in equipment:
        health = random.uniform(0.65, 0.99)
        eq["health_score"] = round(health * 100, 1)
        eq["status"] = "Critical" if health < 0.7 else "Warning" if health < 0.85 else "Good"
        eq["temperature"] = round(random.uniform(35, 75), 1)
        eq["vibration"] = round(random.uniform(0.1, 2.5), 2)
        eq["runtime_hours"] = random.randint(1000, 15000)
        eq["next_maintenance"] = (datetime.now() + timedelta(days=random.randint(1, 60))).strftime("%Y-%m-%d")
        eq["failure_probability"] = round((1 - health) * 100, 1)
    
    return pd.DataFrame(equipment)

def get_sensor_readings(equipment_id="SMT-001", hours=24):
    """Generate sensor readings for equipment"""
    timestamps = [datetime.now() - timedelta(hours=x) for x in range(hours, 0, -1)]
    return pd.DataFrame({
        "timestamp": timestamps,
        "temperature": [45 + np.sin(i/4) * 5 + np.random.normal(0, 1) for i in range(hours)],
        "vibration": [0.5 + np.random.exponential(0.1) for _ in range(hours)],
        "power_consumption": [2.5 + np.random.normal(0, 0.2) for _ in range(hours)],
        "cycle_time": [12 + np.random.normal(0, 0.5) for _ in range(hours)],
    })

# =============================================================================
# RISK INTELLIGENCE DATA
# =============================================================================

def get_risk_data():
    """Generate supply chain risk data"""
    risks = [
        {"id": "RSK-001", "category": "Geopolitical", "description": "Taiwan strait tensions affecting semiconductor supply", "impact": "High", "probability": 0.35, "score": 8.5, "region": "APAC"},
        {"id": "RSK-002", "category": "Natural Disaster", "description": "Typhoon season risk for Japan suppliers", "impact": "Medium", "probability": 0.45, "score": 6.2, "region": "APAC"},
        {"id": "RSK-003", "category": "Supplier", "description": "Key supplier financial instability", "impact": "High", "probability": 0.20, "score": 7.0, "region": "Global"},
        {"id": "RSK-004", "category": "Logistics", "description": "Port congestion at Rotterdam", "impact": "Medium", "probability": 0.55, "score": 5.8, "region": "EMEA"},
        {"id": "RSK-005", "category": "Regulatory", "description": "New EU sustainability regulations", "impact": "Low", "probability": 0.80, "score": 4.5, "region": "EMEA"},
        {"id": "RSK-006", "category": "Cyber", "description": "Ransomware threat to logistics partners", "impact": "High", "probability": 0.25, "score": 7.8, "region": "Global"},
    ]
    return pd.DataFrame(risks)

def get_risk_by_region():
    """Generate risk scores by region"""
    return pd.DataFrame([
        {"region": "Americas", "risk_score": 4.2, "trend": "stable"},
        {"region": "EMEA", "risk_score": 5.8, "trend": "increasing"},
        {"region": "APAC", "risk_score": 7.1, "trend": "increasing"},
    ])

# =============================================================================
# DIGITAL TWIN / FACTORY DATA
# =============================================================================

def get_factory_zones():
    """Generate factory zone data for digital twin"""
    zones = [
        {"id": "receiving", "name": "Receiving", "x": 50, "y": 50, "width": 150, "height": 100},
        {"id": "warehouse", "name": "Warehouse", "x": 50, "y": 170, "width": 150, "height": 120},
        {"id": "smt1", "name": "SMT Line 1", "x": 220, "y": 50, "width": 180, "height": 100},
        {"id": "smt2", "name": "SMT Line 2", "x": 420, "y": 50, "width": 180, "height": 100},
        {"id": "testing", "name": "Testing", "x": 220, "y": 170, "width": 180, "height": 120},
        {"id": "packaging", "name": "Packaging", "x": 420, "y": 170, "width": 180, "height": 120},
        {"id": "quality", "name": "Quality Lab", "x": 220, "y": 310, "width": 180, "height": 100},
        {"id": "shipping", "name": "Shipping", "x": 420, "y": 310, "width": 180, "height": 100},
    ]
    
    for zone in zones:
        zone["status"] = random.choice(["active", "active", "active", "warning", "idle"])
        zone["utilization"] = random.randint(45, 98)
        zone["workers"] = random.randint(2, 12)
        zone["units_today"] = random.randint(500, 5000)
        zone["temperature"] = round(random.uniform(20, 28), 1)
        zone["humidity"] = random.randint(35, 55)
    
    return zones

def get_production_flow():
    """Generate production flow data"""
    return {
        "total_input": 15000,
        "in_progress": 3200,
        "completed": 11450,
        "scrapped": 350,
        "throughput_rate": 847,  # units per hour
        "cycle_time": 42,  # seconds
        "oee": 87.3,
    }

def get_factory_kpis():
    """Generate real-time factory KPIs"""
    return {
        "oee": {"value": 87.3, "target": 85, "status": "good"},
        "throughput": {"value": 12450, "target": 12000, "status": "good"},
        "quality_rate": {"value": 98.7, "target": 98, "status": "good"},
        "availability": {"value": 92.1, "target": 95, "status": "warning"},
        "performance": {"value": 95.8, "target": 92, "status": "good"},
        "active_workers": {"value": 47, "target": 50, "status": "good"},
        "active_machines": {"value": 18, "target": 20, "status": "warning"},
        "energy_kwh": {"value": 1247, "target": 1500, "status": "good"},
    }

