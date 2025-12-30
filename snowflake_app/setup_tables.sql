-- ============================================================================
-- TELIT SUPPLY CHAIN - SNOWFLAKE TABLE SETUP
-- Run this script to create sample tables for the dashboard
-- ============================================================================

-- Create Database and Schema
CREATE DATABASE IF NOT EXISTS TELIT_SUPPLY_CHAIN;
USE DATABASE TELIT_SUPPLY_CHAIN;
CREATE SCHEMA IF NOT EXISTS ANALYTICS;
USE SCHEMA ANALYTICS;

-- ============================================================================
-- 1. EXECUTIVE KPIs TABLE
-- ============================================================================
CREATE OR REPLACE TABLE EXECUTIVE_KPIS (
    KPI_DATE DATE,
    TOTAL_REVENUE FLOAT,
    ORDERS_IN_TRANSIT INT,
    INVENTORY_VALUE FLOAT,
    ON_TIME_DELIVERY FLOAT,
    MANUFACTURING_OEE FLOAT,
    ACTIVE_SUPPLIERS INT,
    DEFECT_RATE FLOAT,
    CARBON_FOOTPRINT FLOAT,
    UPDATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- Insert sample data
INSERT INTO EXECUTIVE_KPIS VALUES
(CURRENT_DATE(), 247800000, 1247, 89400000, 94.7, 87.3, 48, 0.8, 12450, CURRENT_TIMESTAMP());

-- ============================================================================
-- 2. PRODUCTS TABLE
-- ============================================================================
CREATE OR REPLACE TABLE PRODUCTS (
    SKU VARCHAR(50) PRIMARY KEY,
    PRODUCT_NAME VARCHAR(200),
    CATEGORY VARCHAR(100),
    UNIT_PRICE FLOAT
);

INSERT INTO PRODUCTS VALUES
('ME310G1-W1', 'ME310G1 LTE Cat-M1', 'Cellular LPWA', 24.50),
('ME310G1-WW', 'ME310G1 Global', 'Cellular LPWA', 26.00),
('FN980-NA', 'FN980 5G Sub-6', 'Cellular 5G', 89.00),
('FN990-WW', 'FN990 5G mmWave', 'Cellular 5G', 125.00),
('LE910C4-NF', 'LE910C4 LTE Cat-4', 'Cellular LTE', 42.00),
('LE910C1-NA', 'LE910C1 LTE Cat-1', 'Cellular LTE', 32.00),
('SE868K3-A', 'SE868K3 GNSS', 'Positioning', 18.50),
('SE873Q5-A', 'SE873Q5 RTK', 'Positioning', 45.00),
('WE310F5', 'WE310F5 Wi-Fi 5', 'Wi-Fi & Bluetooth', 15.00),
('WE310F6', 'WE310F6 Wi-Fi 6', 'Wi-Fi & Bluetooth', 22.00),
('BlueMod+S50', 'BlueMod+S50 BLE', 'Wi-Fi & Bluetooth', 12.00),
('NE310H2-W1', 'NE310H2 NB-IoT', 'Cellular LPWA', 19.00);

-- ============================================================================
-- 3. WAREHOUSES TABLE
-- ============================================================================
CREATE OR REPLACE TABLE WAREHOUSES (
    WAREHOUSE_ID VARCHAR(20) PRIMARY KEY,
    WAREHOUSE_NAME VARCHAR(100),
    COUNTRY VARCHAR(50),
    REGION VARCHAR(20),
    LATITUDE FLOAT,
    LONGITUDE FLOAT,
    CAPACITY INT
);

INSERT INTO WAREHOUSES VALUES
('WH-US-CA', 'Los Angeles DC', 'USA', 'Americas', 34.0522, -118.2437, 50000),
('WH-US-TX', 'Dallas DC', 'USA', 'Americas', 32.7767, -96.7970, 35000),
('WH-DE-FR', 'Frankfurt Hub', 'Germany', 'EMEA', 50.1109, 8.6821, 45000),
('WH-UK-LO', 'London DC', 'UK', 'EMEA', 51.5074, -0.1278, 30000),
('WH-CN-SH', 'Shanghai DC', 'China', 'APAC', 31.2304, 121.4737, 60000),
('WH-SG-SG', 'Singapore Hub', 'Singapore', 'APAC', 1.3521, 103.8198, 40000),
('WH-JP-TK', 'Tokyo DC', 'Japan', 'APAC', 35.6762, 139.6503, 25000),
('WH-BR-SP', 'São Paulo DC', 'Brazil', 'Americas', -23.5505, -46.6333, 20000);

-- ============================================================================
-- 4. INVENTORY LEVELS TABLE
-- ============================================================================
CREATE OR REPLACE TABLE INVENTORY_LEVELS (
    INVENTORY_ID INT AUTOINCREMENT PRIMARY KEY,
    WAREHOUSE_ID VARCHAR(20),
    SKU VARCHAR(50),
    CURRENT_STOCK INT,
    REORDER_POINT INT,
    DAYS_OF_SUPPLY FLOAT,
    LAST_UPDATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (WAREHOUSE_ID) REFERENCES WAREHOUSES(WAREHOUSE_ID),
    FOREIGN KEY (SKU) REFERENCES PRODUCTS(SKU)
);

-- ============================================================================
-- 5. SUPPLIERS TABLE
-- ============================================================================
CREATE OR REPLACE TABLE SUPPLIERS (
    SUPPLIER_ID VARCHAR(20) PRIMARY KEY,
    SUPPLIER_NAME VARCHAR(200),
    COUNTRY VARCHAR(50),
    CATEGORY VARCHAR(100),
    TIER INT,
    ON_TIME_DELIVERY FLOAT,
    QUALITY_SCORE FLOAT,
    LEAD_TIME_DAYS INT,
    RISK_SCORE FLOAT
);

INSERT INTO SUPPLIERS VALUES
('SUP-001', 'Taiwan Semiconductor', 'Taiwan', 'Chipsets', 1, 96.5, 98.2, 28, 0.25),
('SUP-002', 'Samsung Electronics', 'South Korea', 'Memory', 1, 97.8, 99.1, 21, 0.18),
('SUP-003', 'Murata Manufacturing', 'Japan', 'Passives', 1, 98.2, 99.5, 18, 0.12),
('SUP-004', 'Qualcomm', 'USA', 'Modems', 1, 95.5, 97.8, 35, 0.28),
('SUP-005', 'Skyworks Solutions', 'USA', 'RF Components', 2, 94.2, 96.5, 24, 0.22),
('SUP-006', 'TDK Corporation', 'Japan', 'Inductors', 2, 97.1, 98.8, 20, 0.15),
('SUP-007', 'Yageo Corporation', 'Taiwan', 'Resistors', 2, 96.8, 97.5, 16, 0.20),
('SUP-008', 'Amphenol', 'USA', 'Connectors', 2, 95.9, 98.0, 22, 0.18);

-- ============================================================================
-- 6. SHIPMENTS TABLE
-- ============================================================================
CREATE OR REPLACE TABLE SHIPMENTS (
    SHIPMENT_ID VARCHAR(30) PRIMARY KEY,
    ORIGIN_WAREHOUSE VARCHAR(20),
    DESTINATION_WAREHOUSE VARCHAR(20),
    STATUS VARCHAR(50),
    CARRIER VARCHAR(100),
    ETA DATE,
    WEIGHT_KG FLOAT,
    VALUE FLOAT,
    PROGRESS INT,
    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- ============================================================================
-- 7. FACTORY SENSORS TABLE (for Digital Twin)
-- ============================================================================
CREATE OR REPLACE TABLE FACTORY_SENSORS (
    SENSOR_ID VARCHAR(30) PRIMARY KEY,
    ZONE_ID VARCHAR(30),
    ZONE_NAME VARCHAR(100),
    SENSOR_TYPE VARCHAR(50),
    CURRENT_VALUE FLOAT,
    UNIT VARCHAR(20),
    STATUS VARCHAR(20),
    LAST_READING TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- ============================================================================
-- 8. EQUIPMENT HEALTH TABLE (for Predictive Maintenance)
-- ============================================================================
CREATE OR REPLACE TABLE EQUIPMENT_HEALTH (
    EQUIPMENT_ID VARCHAR(30) PRIMARY KEY,
    EQUIPMENT_NAME VARCHAR(200),
    EQUIPMENT_TYPE VARCHAR(50),
    LOCATION VARCHAR(100),
    HEALTH_SCORE FLOAT,
    STATUS VARCHAR(20),
    TEMPERATURE FLOAT,
    VIBRATION FLOAT,
    RUNTIME_HOURS INT,
    NEXT_MAINTENANCE DATE,
    FAILURE_PROBABILITY FLOAT
);

INSERT INTO EQUIPMENT_HEALTH VALUES
('SMT-001', 'SMT Line 1 - Pick & Place', 'SMT', 'Production Floor A', 92.5, 'Good', 45.2, 0.3, 8500, DATEADD(day, 30, CURRENT_DATE()), 7.5),
('SMT-002', 'SMT Line 2 - Pick & Place', 'SMT', 'Production Floor A', 78.3, 'Warning', 52.8, 0.8, 12000, DATEADD(day, 7, CURRENT_DATE()), 21.7),
('SMT-003', 'Reflow Oven 1', 'Oven', 'Production Floor A', 95.1, 'Good', 68.5, 0.2, 6200, DATEADD(day, 45, CURRENT_DATE()), 4.9),
('AOI-001', 'AOI Station 1', 'Inspection', 'Quality Lab', 88.7, 'Good', 38.2, 0.4, 5800, DATEADD(day, 21, CURRENT_DATE()), 11.3),
('AOI-002', 'AOI Station 2', 'Inspection', 'Quality Lab', 65.2, 'Critical', 42.1, 1.2, 14500, DATEADD(day, 3, CURRENT_DATE()), 34.8),
('TEST-001', 'Functional Tester 1', 'Testing', 'Test Area', 91.8, 'Good', 35.5, 0.25, 7200, DATEADD(day, 35, CURRENT_DATE()), 8.2),
('TEST-002', 'Functional Tester 2', 'Testing', 'Test Area', 89.4, 'Good', 36.8, 0.35, 8100, DATEADD(day, 28, CURRENT_DATE()), 10.6),
('PKG-001', 'Packaging Line 1', 'Packaging', 'Shipping Area', 94.2, 'Good', 28.5, 0.15, 4500, DATEADD(day, 60, CURRENT_DATE()), 5.8);

-- ============================================================================
-- 9. QUALITY DATA TABLE
-- ============================================================================
CREATE OR REPLACE TABLE QUALITY_DATA (
    RECORD_ID INT AUTOINCREMENT PRIMARY KEY,
    RECORD_DATE DATE,
    PRODUCTION_LINE VARCHAR(50),
    FIRST_PASS_YIELD FLOAT,
    DEFECT_RATE FLOAT,
    SCRAP_RATE FLOAT,
    DEFECT_TYPE VARCHAR(100),
    DEFECT_COUNT INT
);

-- ============================================================================
-- 10. RISK SCORES TABLE
-- ============================================================================
CREATE OR REPLACE TABLE RISK_SCORES (
    RISK_ID VARCHAR(20) PRIMARY KEY,
    CATEGORY VARCHAR(50),
    DESCRIPTION VARCHAR(500),
    IMPACT VARCHAR(20),
    PROBABILITY FLOAT,
    SCORE FLOAT,
    REGION VARCHAR(50),
    LAST_UPDATED TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO RISK_SCORES VALUES
('RSK-001', 'Geopolitical', 'Taiwan strait tensions affecting semiconductor supply', 'High', 0.35, 8.5, 'APAC', CURRENT_TIMESTAMP()),
('RSK-002', 'Natural Disaster', 'Typhoon season risk for Japan suppliers', 'Medium', 0.45, 6.2, 'APAC', CURRENT_TIMESTAMP()),
('RSK-003', 'Supplier', 'Key supplier financial instability', 'High', 0.20, 7.0, 'Global', CURRENT_TIMESTAMP()),
('RSK-004', 'Logistics', 'Port congestion at Rotterdam', 'Medium', 0.55, 5.8, 'EMEA', CURRENT_TIMESTAMP()),
('RSK-005', 'Regulatory', 'New EU sustainability regulations', 'Low', 0.80, 4.5, 'EMEA', CURRENT_TIMESTAMP()),
('RSK-006', 'Cyber', 'Ransomware threat to logistics partners', 'High', 0.25, 7.8, 'Global', CURRENT_TIMESTAMP());

-- ============================================================================
-- 11. ESG METRICS TABLE
-- ============================================================================
CREATE OR REPLACE TABLE ESG_METRICS (
    RECORD_DATE DATE PRIMARY KEY,
    SCOPE1_EMISSIONS FLOAT,
    SCOPE2_EMISSIONS FLOAT,
    SCOPE3_EMISSIONS FLOAT,
    RENEWABLE_ENERGY_PCT FLOAT,
    WASTE_DIVERTED_PCT FLOAT,
    WATER_RECYCLED_PCT FLOAT
);

INSERT INTO ESG_METRICS VALUES
(CURRENT_DATE(), 3200, 7800, 1450, 62, 78, 45);

-- ============================================================================
-- 12. DEMAND FORECAST TABLE
-- ============================================================================
CREATE OR REPLACE TABLE DEMAND_FORECAST (
    FORECAST_ID INT AUTOINCREMENT PRIMARY KEY,
    FORECAST_DATE DATE,
    SKU VARCHAR(50),
    FORECASTED_DEMAND INT,
    LOWER_BOUND INT,
    UPPER_BOUND INT,
    CONFIDENCE_LEVEL FLOAT,
    IS_FORECAST BOOLEAN,
    CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

-- ============================================================================
-- CREATE VIEWS FOR DASHBOARDS
-- ============================================================================

-- Executive Summary View
CREATE OR REPLACE VIEW V_EXECUTIVE_SUMMARY AS
SELECT 
    k.KPI_DATE,
    k.TOTAL_REVENUE,
    k.ORDERS_IN_TRANSIT,
    k.INVENTORY_VALUE,
    k.ON_TIME_DELIVERY,
    k.MANUFACTURING_OEE,
    COUNT(DISTINCT s.SUPPLIER_ID) as ACTIVE_SUPPLIERS,
    k.DEFECT_RATE,
    k.CARBON_FOOTPRINT
FROM EXECUTIVE_KPIS k
CROSS JOIN SUPPLIERS s
WHERE k.KPI_DATE = CURRENT_DATE()
GROUP BY 1,2,3,4,5,6,8,9;

-- Inventory Summary View
CREATE OR REPLACE VIEW V_INVENTORY_SUMMARY AS
SELECT 
    w.REGION,
    w.WAREHOUSE_NAME,
    p.CATEGORY,
    SUM(i.CURRENT_STOCK) as TOTAL_STOCK,
    AVG(i.DAYS_OF_SUPPLY) as AVG_DAYS_OF_SUPPLY,
    SUM(CASE WHEN i.CURRENT_STOCK < i.REORDER_POINT THEN 1 ELSE 0 END) as LOW_STOCK_ITEMS
FROM INVENTORY_LEVELS i
JOIN WAREHOUSES w ON i.WAREHOUSE_ID = w.WAREHOUSE_ID
JOIN PRODUCTS p ON i.SKU = p.SKU
GROUP BY 1,2,3;

-- Supplier Scorecard View
CREATE OR REPLACE VIEW V_SUPPLIER_SCORECARD AS
SELECT 
    SUPPLIER_ID,
    SUPPLIER_NAME,
    COUNTRY,
    CATEGORY,
    TIER,
    ON_TIME_DELIVERY,
    QUALITY_SCORE,
    LEAD_TIME_DAYS,
    RISK_SCORE,
    (ON_TIME_DELIVERY * 0.3 + QUALITY_SCORE * 0.3 + (100 - RISK_SCORE * 100) * 0.2 + (100 - LEAD_TIME_DAYS) * 0.2) as OVERALL_SCORE
FROM SUPPLIERS
ORDER BY OVERALL_SCORE DESC;

-- ============================================================================
-- GRANT PERMISSIONS
-- ============================================================================
-- Uncomment and modify as needed:
-- GRANT SELECT ON ALL TABLES IN SCHEMA ANALYTICS TO ROLE analyst_role;
-- GRANT SELECT ON ALL VIEWS IN SCHEMA ANALYTICS TO ROLE analyst_role;

-- ============================================================================
-- DONE!
-- ============================================================================
SELECT 'Telit Supply Chain tables created successfully!' as STATUS;

