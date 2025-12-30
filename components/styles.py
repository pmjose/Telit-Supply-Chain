"""
Telit Supply Chain - Styles and Theming
Custom CSS and styling components with Telit branding
"""

# Telit Brand Colors
TELIT_BLUE = "#00A7E1"
TELIT_DARK = "#1E3A5F"
TELIT_NAVY = "#0D2137"
TELIT_ORANGE = "#FF6B35"
TELIT_GREEN = "#00C48C"
TELIT_RED = "#FF4757"
TELIT_YELLOW = "#FFB800"
TELIT_GRAY = "#6B7C93"
TELIT_LIGHT = "#F5F7FA"

def get_telit_css():
    """Return the main Telit-branded CSS"""
    return f"""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Styles */
        .stApp {{
            font-family: 'Inter', sans-serif;
        }}
        
        /* Sidebar Styling - Light background for blue logo contrast */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #FFFFFF 0%, {TELIT_LIGHT} 100%);
        }}
        
        [data-testid="stSidebar"] .stMarkdown {{
            color: {TELIT_DARK};
        }}
        
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3 {{
            color: {TELIT_DARK} !important;
        }}
        
        [data-testid="stSidebar"] hr {{
            border-color: rgba(0, 167, 225, 0.2);
        }}
        
        /* Hide default Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        
        /* KPI Card Styles */
        .kpi-card {{
            background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.85) 100%);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
            border: 1px solid rgba(0, 167, 225, 0.1);
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .kpi-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 8px 32px rgba(0, 167, 225, 0.15);
        }}
        
        .kpi-value {{
            font-size: 2.5rem;
            font-weight: 700;
            color: {TELIT_DARK};
            margin: 8px 0;
        }}
        
        .kpi-label {{
            font-size: 0.875rem;
            font-weight: 500;
            color: {TELIT_GRAY};
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .kpi-change {{
            font-size: 0.875rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}
        
        .kpi-change.positive {{
            color: {TELIT_GREEN};
        }}
        
        .kpi-change.negative {{
            color: {TELIT_RED};
        }}
        
        /* Header Styles */
        .main-header {{
            background: linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_NAVY} 100%);
            color: white;
            padding: 32px;
            border-radius: 20px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
        }}
        
        .main-header::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(0,167,225,0.3) 0%, transparent 70%);
            border-radius: 50%;
        }}
        
        .main-header h1 {{
            margin: 0;
            font-size: 2rem;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }}
        
        .main-header p {{
            margin: 8px 0 0 0;
            opacity: 0.8;
            font-size: 1rem;
            position: relative;
            z-index: 1;
        }}
        
        /* Section Headers */
        .section-header {{
            font-size: 1.25rem;
            font-weight: 600;
            color: {TELIT_DARK};
            margin: 32px 0 16px 0;
            padding-bottom: 8px;
            border-bottom: 2px solid {TELIT_BLUE};
            display: inline-block;
        }}
        
        /* Alert Cards */
        .alert-card {{
            border-radius: 12px;
            padding: 16px;
            margin: 8px 0;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        
        .alert-card.critical {{
            background: linear-gradient(135deg, rgba(255,71,87,0.1) 0%, rgba(255,71,87,0.05) 100%);
            border-left: 4px solid {TELIT_RED};
        }}
        
        .alert-card.warning {{
            background: linear-gradient(135deg, rgba(255,184,0,0.1) 0%, rgba(255,184,0,0.05) 100%);
            border-left: 4px solid {TELIT_YELLOW};
        }}
        
        .alert-card.info {{
            background: linear-gradient(135deg, rgba(0,167,225,0.1) 0%, rgba(0,167,225,0.05) 100%);
            border-left: 4px solid {TELIT_BLUE};
        }}
        
        .alert-card.success {{
            background: linear-gradient(135deg, rgba(0,196,140,0.1) 0%, rgba(0,196,140,0.05) 100%);
            border-left: 4px solid {TELIT_GREEN};
        }}
        
        /* Metric Grid */
        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
            margin: 16px 0;
        }}
        
        /* Status Indicators */
        .status-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }}
        
        .status-dot.active {{
            background: {TELIT_GREEN};
            box-shadow: 0 0 8px {TELIT_GREEN};
            animation: pulse 2s infinite;
        }}
        
        .status-dot.warning {{
            background: {TELIT_YELLOW};
            box-shadow: 0 0 8px {TELIT_YELLOW};
        }}
        
        .status-dot.error {{
            background: {TELIT_RED};
            box-shadow: 0 0 8px {TELIT_RED};
            animation: pulse 1s infinite;
        }}
        
        .status-dot.idle {{
            background: {TELIT_GRAY};
        }}
        
        @keyframes pulse {{
            0% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
            100% {{ opacity: 1; }}
        }}
        
        /* Data Table Styling */
        .styled-table {{
            width: 100%;
            border-collapse: collapse;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
        }}
        
        .styled-table thead {{
            background: linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_NAVY} 100%);
            color: white;
        }}
        
        .styled-table th {{
            padding: 16px;
            text-align: left;
            font-weight: 600;
            font-size: 0.875rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        
        .styled-table td {{
            padding: 14px 16px;
            border-bottom: 1px solid #eee;
        }}
        
        .styled-table tbody tr:hover {{
            background: rgba(0, 167, 225, 0.05);
        }}
        
        /* Progress Bar */
        .progress-container {{
            background: #e9ecef;
            border-radius: 10px;
            overflow: hidden;
            height: 8px;
        }}
        
        .progress-bar {{
            height: 100%;
            border-radius: 10px;
            transition: width 0.5s ease;
        }}
        
        .progress-bar.blue {{
            background: linear-gradient(90deg, {TELIT_BLUE} 0%, #00D4FF 100%);
        }}
        
        .progress-bar.green {{
            background: linear-gradient(90deg, {TELIT_GREEN} 0%, #00E5A0 100%);
        }}
        
        .progress-bar.orange {{
            background: linear-gradient(90deg, {TELIT_ORANGE} 0%, #FF9F6B 100%);
        }}
        
        /* Gauge Container */
        .gauge-container {{
            background: white;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
            text-align: center;
        }}
        
        /* Tab Styling */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 8px;
            background: transparent;
        }}
        
        .stTabs [data-baseweb="tab"] {{
            background: white;
            border-radius: 8px 8px 0 0;
            padding: 12px 24px;
            border: 1px solid #e9ecef;
            border-bottom: none;
        }}
        
        .stTabs [aria-selected="true"] {{
            background: {TELIT_BLUE} !important;
            color: white !important;
        }}
        
        /* Sidebar Navigation */
        .nav-item {{
            padding: 12px 16px;
            border-radius: 8px;
            margin: 4px 0;
            cursor: pointer;
            transition: background 0.2s ease;
            color: rgba(255,255,255,0.8);
        }}
        
        .nav-item:hover {{
            background: rgba(255,255,255,0.1);
            color: white;
        }}
        
        .nav-item.active {{
            background: {TELIT_BLUE};
            color: white;
        }}
        
        /* Snowflake Badge */
        .snowflake-badge {{
            background: linear-gradient(135deg, #29B5E8 0%, #00A3E0 100%);
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}
        
        /* Card Grid */
        .card-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        
        /* Animated Background */
        .animated-bg {{
            background: linear-gradient(-45deg, {TELIT_NAVY}, {TELIT_DARK}, {TELIT_BLUE}, {TELIT_DARK});
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }}
        
        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
    </style>
    """


def render_kpi_card(label: str, value: str, change: float = None, prefix: str = "", suffix: str = ""):
    """Render a styled KPI card"""
    change_html = ""
    if change is not None:
        change_class = "positive" if change >= 0 else "negative"
        arrow = "↑" if change >= 0 else "↓"
        change_html = f'<div class="kpi-change {change_class}">{arrow} {abs(change):.1f}%</div>'
    
    return f"""
    <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{prefix}{value}{suffix}</div>
        {change_html}
    </div>
    """


def render_header(title: str, subtitle: str = ""):
    """Render a styled page header"""
    subtitle_html = f'<p>{subtitle}</p>' if subtitle else ''
    return f"""
    <div class="main-header">
        <h1>{title}</h1>
        {subtitle_html}
    </div>
    """


def render_section_header(title: str):
    """Render a section header"""
    return f'<div class="section-header">{title}</div>'


def render_alert_card(message: str, alert_type: str = "info", icon: str = "ℹ️"):
    """Render an alert card"""
    return f"""
    <div class="alert-card {alert_type}">
        <span style="font-size: 1.5rem;">{icon}</span>
        <span>{message}</span>
    </div>
    """


def render_status_indicator(status: str, label: str):
    """Render a status indicator with dot"""
    status_class = {
        "active": "active",
        "running": "active",
        "ok": "active",
        "warning": "warning",
        "idle": "idle",
        "error": "error",
        "critical": "error"
    }.get(status.lower(), "idle")
    
    return f'<span class="status-dot {status_class}"></span>{label}'


def render_progress_bar(value: float, max_value: float = 100, color: str = "blue"):
    """Render a progress bar"""
    percentage = min((value / max_value) * 100, 100)
    return f"""
    <div class="progress-container">
        <div class="progress-bar {color}" style="width: {percentage}%"></div>
    </div>
    """


def render_snowflake_badge():
    """Render Snowflake powered badge"""
    return """
    <div class="snowflake-badge">
        <span>❄️</span>
        <span>Powered by Snowflake</span>
    </div>
    """


def get_plotly_theme():
    """Return Plotly theme configuration"""
    return {
        'layout': {
            'font': {'family': 'Inter, sans-serif'},
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'colorway': [TELIT_BLUE, TELIT_ORANGE, TELIT_GREEN, TELIT_NAVY, TELIT_YELLOW, TELIT_RED],
            'title': {'font': {'color': TELIT_DARK, 'size': 18}},
            'xaxis': {'gridcolor': '#e9ecef', 'linecolor': '#e9ecef'},
            'yaxis': {'gridcolor': '#e9ecef', 'linecolor': '#e9ecef'},
        }
    }


# Telit Logo (using external image)
TELIT_LOGO_SVG = """
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telit_Cinterion_Logo.png/250px-Telit_Cinterion_Logo.png" 
     style="max-width: 180px; height: auto;" 
     alt="Telit Cinterion Logo">
"""

TELIT_LOGO_DARK_SVG = """
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Telit_Cinterion_Logo.png/250px-Telit_Cinterion_Logo.png" 
     style="max-width: 180px; height: auto;" 
     alt="Telit Cinterion Logo">
"""

