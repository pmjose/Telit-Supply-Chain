# Deploying to Snowflake

This guide explains how to deploy the Telit Supply Chain Intelligence Platform to **Streamlit in Snowflake (SiS)**.

## Prerequisites

1. Snowflake account
2. Access to at least one database/schema where you can create objects
3. A warehouse for running the app

---

## ⚠️ Permission Issues?

If you get `Insufficient privileges` errors, use **Option A** below (use existing database).

---

## Option A: Use Your Existing Database (Recommended if no admin rights)

If you can't create databases, use a database/schema you already have access to:

```sql
-- Use your existing database (replace with your actual database name)
USE DATABASE YOUR_DATABASE;
USE SCHEMA YOUR_SCHEMA;

-- Or ask your admin which database you can use:
SHOW DATABASES;

-- Check what you have access to:
SHOW GRANTS TO USER CURRENT_USER();
```

Then skip to **Step 2** below, but use your existing database/schema names.

---

## Option B: Create New Database (Requires ACCOUNTADMIN or CREATE DATABASE privilege)

```sql
-- Only run this if you have admin privileges
USE ROLE ACCOUNTADMIN;  -- or a role with CREATE DATABASE

CREATE DATABASE IF NOT EXISTS TELIT_SUPPLY_CHAIN;
USE DATABASE TELIT_SUPPLY_CHAIN;
CREATE SCHEMA IF NOT EXISTS ANALYTICS;
USE SCHEMA ANALYTICS;
CREATE STAGE IF NOT EXISTS STREAMLIT_STAGE;
```

---

## Option 1: Deploy via Snowsight UI (Easiest - No Database Required!)

### Step 1: Create Streamlit App Directly in Snowsight

1. Go to **Snowsight** → Click **Streamlit** in the left sidebar
2. Click **+ Streamlit App** button
3. In the dialog:
   - **App name**: `TELIT_SUPPLY_CHAIN_APP`
   - **App location**: Select any database/schema you have access to
   - **Warehouse**: Select your warehouse
4. Click **Create**

### Step 2: Paste the Code

Copy the contents from `snowflake_app/streamlit_app.py` and paste into the editor.

**That's it!** The app will run with demo data (no tables needed for the demo).

### Step 2: Upload Files via Snowsight

1. Go to **Snowsight** → **Data** → **Databases**
2. Navigate to `TELIT_SUPPLY_CHAIN.ANALYTICS`
3. Click on **Stages** → `STREAMLIT_STAGE`
4. Click **+ Files** and upload:
   - `streamlit_app.py` (the main Snowflake-ready app)
   - `environment.yml`

### Step 3: Create the Streamlit App

```sql
CREATE OR REPLACE STREAMLIT TELIT_SUPPLY_CHAIN_APP
  ROOT_LOCATION = '@TELIT_SUPPLY_CHAIN.ANALYTICS.STREAMLIT_STAGE'
  MAIN_FILE = 'streamlit_app.py'
  QUERY_WAREHOUSE = 'COMPUTE_WH';  -- Replace with your warehouse
```

### Step 4: Open the App

1. Go to **Snowsight** → **Streamlit**
2. Click on `TELIT_SUPPLY_CHAIN_APP`
3. The app will open in a new tab!

---

## Option 2: Deploy via Snowflake CLI

### Step 1: Install Snowflake CLI

```bash
pip install snowflake-cli-labs
```

### Step 2: Configure Connection

```bash
snow connection add
# Follow prompts to add your Snowflake connection
```

### Step 3: Deploy

```bash
cd /path/to/Telit-Supply-Chain/snowflake_app

# Create the app
snow streamlit deploy --replace
```

---

## Option 3: Deploy via SQL Commands

### Step 1: Create Stage and Upload Files

```sql
-- Create stage
CREATE STAGE IF NOT EXISTS TELIT_SUPPLY_CHAIN.ANALYTICS.STREAMLIT_STAGE;

-- Upload files using PUT command (run from SnowSQL or worksheet)
PUT file:///path/to/snowflake_app/streamlit_app.py @TELIT_SUPPLY_CHAIN.ANALYTICS.STREAMLIT_STAGE OVERWRITE=TRUE AUTO_COMPRESS=FALSE;
PUT file:///path/to/snowflake_app/environment.yml @TELIT_SUPPLY_CHAIN.ANALYTICS.STREAMLIT_STAGE OVERWRITE=TRUE AUTO_COMPRESS=FALSE;
PUT file:///path/to/snowflake_app/pages/*.py @TELIT_SUPPLY_CHAIN.ANALYTICS.STREAMLIT_STAGE/pages/ OVERWRITE=TRUE AUTO_COMPRESS=FALSE;
```

### Step 2: Create Streamlit Object

```sql
CREATE OR REPLACE STREAMLIT TELIT_SUPPLY_CHAIN.ANALYTICS.TELIT_SUPPLY_CHAIN_APP
  ROOT_LOCATION = '@TELIT_SUPPLY_CHAIN.ANALYTICS.STREAMLIT_STAGE'
  MAIN_FILE = 'streamlit_app.py'
  QUERY_WAREHOUSE = 'COMPUTE_WH';
```

---

## Sharing the App

### Grant Access to Other Users

```sql
-- Grant access to a role
GRANT USAGE ON STREAMLIT TELIT_SUPPLY_CHAIN.ANALYTICS.TELIT_SUPPLY_CHAIN_APP TO ROLE analyst_role;

-- Grant underlying database access
GRANT USAGE ON DATABASE TELIT_SUPPLY_CHAIN TO ROLE analyst_role;
GRANT USAGE ON SCHEMA TELIT_SUPPLY_CHAIN.ANALYTICS TO ROLE analyst_role;
```

---

## Key Differences from Local Deployment

| Aspect | Local (Current) | Snowflake SiS |
|--------|----------------|---------------|
| Data Source | Fake data (Python) | Snowflake tables |
| Authentication | None | Snowflake SSO |
| Packages | Any pip package | Snowflake Anaconda only |
| Session | None | `snowflake.snowpark.context` |
| Hosting | Local machine | Snowflake infrastructure |

---

## Supported Packages in Snowflake

The following packages used in this app are available in Snowflake:
- ✅ streamlit
- ✅ pandas
- ✅ numpy
- ✅ plotly
- ⚠️ graphviz (may need alternative)
- ⚠️ faker (not needed - use real data)

Check available packages: [Snowflake Anaconda Channel](https://repo.anaconda.com/pkgs/snowflake/)

---

## Next Steps

1. Create Snowflake tables with your real supply chain data
2. Replace fake data generators with SQL queries
3. Use `st.connection("snowflake")` or Snowpark session for data access
4. Deploy and share with your team!

