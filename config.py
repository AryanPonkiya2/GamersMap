"""
Application configuration — color scheme, window settings, and navigation definitions.
"""

# Color palette used across the entire application
COLORS = {
    "primary": "#1e3a8a",
    "secondary": "#3b82f6",
    "accent": "#60a5fa",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "dark_bg": "#0f172a",
    "card_bg": "#1e293b",
    "hover": "#2563eb"
}

# Window settings
WINDOW_TITLE = "Gaming Analytics Dashboard"
WINDOW_GEOMETRY = "1280x750"
WINDOW_MIN_SIZE = (900, 600)
SIDEBAR_WIDTH = 220

# Navigation buttons: (display_text, page_name)
NAV_ITEMS = [
    ("📊 Dashboard", "Dashboard"),
    ("📈 Line Charts", "Line Charts"),
    ("📊 Bar Charts", "Bar Charts"),
    ("🥧 Pie Charts", "Pie Charts"),
    ("🎲 3D Charts", "3D Charts"),
    ("🗺️ Map View", "Map View"),
    ("▶️ YouTube Stats", "YouTube Stats"),
]
