"""
Telit Supply Chain - Interactive Factory Floor Map
SVG-based digital twin visualization
"""

from components.styles import (
    TELIT_BLUE, TELIT_DARK, TELIT_NAVY, TELIT_ORANGE, 
    TELIT_GREEN, TELIT_RED, TELIT_YELLOW, TELIT_GRAY
)

def get_status_color(status: str) -> str:
    """Get color based on status"""
    colors = {
        "active": TELIT_GREEN,
        "running": TELIT_GREEN,
        "good": TELIT_GREEN,
        "warning": TELIT_YELLOW,
        "idle": TELIT_GRAY,
        "error": TELIT_RED,
        "critical": TELIT_RED,
        "maintenance": TELIT_BLUE,
    }
    return colors.get(status.lower(), TELIT_GRAY)


def render_factory_floor(zones: list, width: int = 700, height: int = 480) -> str:
    """Render interactive SVG factory floor map"""
    
    # Generate zone SVG elements
    zone_elements = ""
    for zone in zones:
        status_color = get_status_color(zone.get('status', 'idle'))
        fill_opacity = "0.15" if zone['status'] == 'idle' else "0.25"
        
        # Animated pulse for active/warning zones
        pulse_animation = ""
        if zone['status'] in ['active', 'warning', 'error']:
            pulse_animation = f"""
                <animate attributeName="opacity" values="0.25;0.4;0.25" dur="2s" repeatCount="indefinite"/>
            """
        
        zone_elements += f"""
        <g class="factory-zone" data-zone="{zone['id']}" style="cursor: pointer;">
            <!-- Zone background -->
            <rect 
                x="{zone['x']}" 
                y="{zone['y']}" 
                width="{zone['width']}" 
                height="{zone['height']}" 
                rx="8" 
                fill="{status_color}" 
                fill-opacity="{fill_opacity}"
                stroke="{status_color}"
                stroke-width="2"
            >
                {pulse_animation}
            </rect>
            
            <!-- Zone header -->
            <rect 
                x="{zone['x']}" 
                y="{zone['y']}" 
                width="{zone['width']}" 
                height="28" 
                rx="8" 
                fill="{status_color}"
                fill-opacity="0.9"
            />
            <rect 
                x="{zone['x']}" 
                y="{zone['y'] + 20}" 
                width="{zone['width']}" 
                height="8" 
                fill="{status_color}"
                fill-opacity="0.9"
            />
            
            <!-- Zone title -->
            <text 
                x="{zone['x'] + zone['width']//2}" 
                y="{zone['y'] + 18}" 
                text-anchor="middle" 
                fill="white" 
                font-family="Inter, sans-serif" 
                font-size="12" 
                font-weight="600"
            >{zone['name']}</text>
            
            <!-- Status indicator -->
            <circle 
                cx="{zone['x'] + 15}" 
                cy="{zone['y'] + 14}" 
                r="5" 
                fill="white"
            >
                <animate attributeName="opacity" values="1;0.5;1" dur="1.5s" repeatCount="indefinite"/>
            </circle>
            
            <!-- Zone metrics -->
            <text 
                x="{zone['x'] + zone['width']//2}" 
                y="{zone['y'] + 50}" 
                text-anchor="middle" 
                fill="{TELIT_DARK}" 
                font-family="Inter, sans-serif" 
                font-size="20" 
                font-weight="700"
            >{zone['utilization']}%</text>
            <text 
                x="{zone['x'] + zone['width']//2}" 
                y="{zone['y'] + 68}" 
                text-anchor="middle" 
                fill="{TELIT_GRAY}" 
                font-family="Inter, sans-serif" 
                font-size="10"
            >Utilization</text>
            
            <!-- Units today -->
            <text 
                x="{zone['x'] + zone['width']//2}" 
                y="{zone['y'] + zone['height'] - 25}" 
                text-anchor="middle" 
                fill="{TELIT_DARK}" 
                font-family="Inter, sans-serif" 
                font-size="14" 
                font-weight="600"
            >{zone['units_today']:,} units</text>
            
            <!-- Environment readings -->
            <text 
                x="{zone['x'] + zone['width']//2}" 
                y="{zone['y'] + zone['height'] - 10}" 
                text-anchor="middle" 
                fill="{TELIT_GRAY}" 
                font-family="Inter, sans-serif" 
                font-size="9"
            >{zone['temperature']}°C | {zone['humidity']}% RH | {zone['workers']} workers</text>
        </g>
        """
    
    # Flow arrows between zones
    arrows = """
        <!-- Receiving to Warehouse -->
        <path d="M 125 150 L 125 165" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
        
        <!-- Receiving to SMT Line 1 -->
        <path d="M 200 100 L 215 100" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
        
        <!-- SMT Line 1 to SMT Line 2 -->
        <path d="M 400 100 L 415 100" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
        
        <!-- SMT Lines to Testing/Packaging -->
        <path d="M 310 150 L 310 165" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
        <path d="M 510 150 L 510 165" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
        
        <!-- Testing to Quality Lab -->
        <path d="M 310 290 L 310 305" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
        
        <!-- Packaging to Shipping -->
        <path d="M 510 290 L 510 305" stroke="{blue}" stroke-width="2" marker-end="url(#arrowhead)"/>
    """.format(blue=TELIT_BLUE)
    
    svg = f"""
    <svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <!-- Gradient background -->
            <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#f8fafc;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#e2e8f0;stop-opacity:1" />
            </linearGradient>
            
            <!-- Arrow marker -->
            <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
                <polygon points="0 0, 10 3.5, 0 7" fill="{TELIT_BLUE}" />
            </marker>
            
            <!-- Drop shadow filter -->
            <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                <feDropShadow dx="0" dy="2" stdDeviation="4" flood-opacity="0.1"/>
            </filter>
        </defs>
        
        <!-- Background -->
        <rect width="{width}" height="{height}" fill="url(#bgGradient)" rx="12"/>
        
        <!-- Grid pattern -->
        <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.5"/>
        </pattern>
        <rect width="{width}" height="{height}" fill="url(#grid)" rx="12"/>
        
        <!-- Flow arrows -->
        {arrows}
        
        <!-- Factory zones -->
        {zone_elements}
        
        <!-- Legend -->
        <g transform="translate(20, {height - 35})">
            <rect x="0" y="0" width="15" height="15" rx="3" fill="{TELIT_GREEN}"/>
            <text x="20" y="12" font-family="Inter, sans-serif" font-size="10" fill="{TELIT_DARK}">Active</text>
            
            <rect x="70" y="0" width="15" height="15" rx="3" fill="{TELIT_YELLOW}"/>
            <text x="90" y="12" font-family="Inter, sans-serif" font-size="10" fill="{TELIT_DARK}">Warning</text>
            
            <rect x="150" y="0" width="15" height="15" rx="3" fill="{TELIT_RED}"/>
            <text x="170" y="12" font-family="Inter, sans-serif" font-size="10" fill="{TELIT_DARK}">Critical</text>
            
            <rect x="225" y="0" width="15" height="15" rx="3" fill="{TELIT_GRAY}"/>
            <text x="245" y="12" font-family="Inter, sans-serif" font-size="10" fill="{TELIT_DARK}">Idle</text>
            
            <rect x="290" y="0" width="15" height="15" rx="3" fill="{TELIT_BLUE}"/>
            <text x="310" y="12" font-family="Inter, sans-serif" font-size="10" fill="{TELIT_DARK}">Maintenance</text>
        </g>
    </svg>
    """
    
    return svg


def render_factory_kpi_panel(kpis: dict) -> str:
    """Render KPI panel for factory dashboard"""
    
    def get_status_badge(status: str) -> str:
        colors = {
            "good": (TELIT_GREEN, "✓"),
            "warning": (TELIT_YELLOW, "!"),
            "critical": (TELIT_RED, "✗"),
        }
        color, icon = colors.get(status, (TELIT_GRAY, "?"))
        return f'<span style="background:{color};color:white;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600;">{icon}</span>'
    
    kpi_cards = ""
    for key, data in kpis.items():
        label = key.replace("_", " ").title()
        badge = get_status_badge(data.get('status', 'good'))
        target_text = f"Target: {data['target']}" if 'target' in data else ""
        
        kpi_cards += f"""
        <div style="
            background: white;
            border-radius: 12px;
            padding: 16px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            border: 1px solid #e9ecef;
        ">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
                <span style="font-size:12px;color:{TELIT_GRAY};text-transform:uppercase;letter-spacing:0.5px;">{label}</span>
                {badge}
            </div>
            <div style="font-size:28px;font-weight:700;color:{TELIT_DARK};">{data['value']}</div>
            <div style="font-size:11px;color:{TELIT_GRAY};">{target_text}</div>
        </div>
        """
    
    return f"""
    <div style="
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
        gap: 12px;
        margin: 16px 0;
    ">
        {kpi_cards}
    </div>
    """


def render_production_flow_diagram() -> str:
    """Render a Graphviz-style production flow diagram"""
    
    return """
    digraph production_flow {
        rankdir=LR;
        node [shape=box, style="rounded,filled", fontname="Inter", fontsize=10];
        edge [fontname="Inter", fontsize=9];
        
        // Nodes
        receiving [label="Receiving\\n▣ 3 Docks", fillcolor="#E3F2FD", color="#00A7E1"];
        warehouse [label="Warehouse\\n▣ 45,000 units", fillcolor="#E3F2FD", color="#00A7E1"];
        smt1 [label="SMT Line 1\\n⚡ 847 units/hr", fillcolor="#E8F5E9", color="#00C48C"];
        smt2 [label="SMT Line 2\\n⚡ 792 units/hr", fillcolor="#E8F5E9", color="#00C48C"];
        testing [label="Testing\\n✓ 98.7% pass", fillcolor="#E8F5E9", color="#00C48C"];
        quality [label="Quality Lab\\n◉ 24 samples", fillcolor="#FFF3E0", color="#FF6B35"];
        packaging [label="Packaging\\n📦 2,340/hr", fillcolor="#E8F5E9", color="#00C48C"];
        shipping [label="Shipping\\n🚛 Ready", fillcolor="#E3F2FD", color="#00A7E1"];
        
        // Edges
        receiving -> warehouse [label="Inbound"];
        receiving -> smt1 [label="Direct"];
        warehouse -> smt1;
        warehouse -> smt2;
        smt1 -> testing;
        smt2 -> testing;
        testing -> quality [label="Samples", style=dashed];
        testing -> packaging;
        packaging -> shipping;
    }
    """


def render_equipment_list(equipment: list) -> str:
    """Render equipment status list"""
    
    rows = ""
    for eq in equipment:
        status_color = get_status_color(eq['status'])
        health_bar_color = TELIT_GREEN if eq['health_score'] >= 85 else TELIT_YELLOW if eq['health_score'] >= 70 else TELIT_RED
        
        rows += f"""
        <tr style="border-bottom: 1px solid #e9ecef;">
            <td style="padding: 12px;">
                <div style="display:flex;align-items:center;gap:8px;">
                    <span style="width:8px;height:8px;border-radius:50%;background:{status_color};display:inline-block;"></span>
                    <span style="font-weight:600;color:{TELIT_DARK};">{eq['name']}</span>
                </div>
                <div style="font-size:11px;color:{TELIT_GRAY};margin-top:2px;">{eq['location']}</div>
            </td>
            <td style="padding: 12px;">
                <div style="font-weight:600;color:{TELIT_DARK};">{eq['health_score']}%</div>
                <div style="width:60px;height:4px;background:#e9ecef;border-radius:2px;margin-top:4px;">
                    <div style="width:{eq['health_score']}%;height:100%;background:{health_bar_color};border-radius:2px;"></div>
                </div>
            </td>
            <td style="padding: 12px;text-align:center;">
                <span style="font-size:12px;color:{TELIT_DARK};">{eq['temperature']}°C</span>
            </td>
            <td style="padding: 12px;text-align:center;">
                <span style="font-size:12px;color:{TELIT_DARK};">{eq['vibration']} mm/s</span>
            </td>
            <td style="padding: 12px;text-align:right;">
                <span style="
                    background: {'rgba(255,71,87,0.1)' if eq['failure_probability'] > 20 else 'rgba(0,196,140,0.1)'};
                    color: {TELIT_RED if eq['failure_probability'] > 20 else TELIT_GREEN};
                    padding: 4px 10px;
                    border-radius: 12px;
                    font-size: 11px;
                    font-weight: 600;
                ">{eq['failure_probability']}% risk</span>
            </td>
        </tr>
        """
    
    return f"""
    <table style="width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.06);">
        <thead>
            <tr style="background:linear-gradient(135deg, {TELIT_DARK} 0%, {TELIT_NAVY} 100%);">
                <th style="padding:14px;text-align:left;color:white;font-size:12px;text-transform:uppercase;letter-spacing:0.5px;">Equipment</th>
                <th style="padding:14px;text-align:left;color:white;font-size:12px;text-transform:uppercase;letter-spacing:0.5px;">Health</th>
                <th style="padding:14px;text-align:center;color:white;font-size:12px;text-transform:uppercase;letter-spacing:0.5px;">Temp</th>
                <th style="padding:14px;text-align:center;color:white;font-size:12px;text-transform:uppercase;letter-spacing:0.5px;">Vibration</th>
                <th style="padding:14px;text-align:right;color:white;font-size:12px;text-transform:uppercase;letter-spacing:0.5px;">Risk</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """

