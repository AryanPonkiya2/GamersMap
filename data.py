"""
Sample gaming data used throughout the application.
"""


def generate_sample_data():
    """Return the full sample-data dictionary used by every page."""
    return {
        "line_chart": {
            "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
            "world_players": [2800, 2850, 2900, 2950, 3000, 3050,
                              3080, 3100, 3150, 3180, 3190, 3200],
            "india_players": [480, 495, 510, 525, 535, 540,
                              545, 550, 555, 560, 565, 568],
            "revenue": [120, 125, 130, 135, 140, 142,
                        145, 148, 152, 155, 157, 159]
        },
        "bar_chart": {
            "platforms": ["Mobile", "PC", "Console", "VR", "Cloud"],
            "users": [1850, 980, 720, 85, 165],
            "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6"]
        },
        "pie_chart": {
            "regions": ["Asia", "North America", "Europe",
                        "South America", "Africa", "Oceania"],
            "percentages": [45, 25, 18, 7, 3, 2],
            "colors": ["#3b82f6", "#10b981", "#f59e0b",
                        "#ef4444", "#8b5cf6", "#06b6d4"]
        },
        "genres": {
            "labels": ["Action", "RPG", "Sports", "Strategy", "Shooter", "Racing"],
            "values": [28, 22, 15, 12, 18, 5],
            "colors": ["#ef4444", "#f59e0b", "#10b981",
                        "#3b82f6", "#8b5cf6", "#06b6d4"]
        },
        "map_view": {
            "regions": ["Asia", "North America", "Europe", "South America",
                        "Middle East", "Africa", "Oceania"],
            "gamers_m": [1440, 800, 576, 224, 96, 96, 64],
            "growth_pct": [14.2, 8.5, 6.3, 11.7, 18.4, 22.1, 5.8],
            "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444",
                        "#8b5cf6", "#06b6d4", "#f472b6"]
        },
        "youtube_stats": {
            "channels": ["PewDiePie", "Markiplier", "Jacksepticeye",
                         "VanossGaming", "Dream", "MrBeast Gaming",
                         "Ninja", "Shroud"],
            "subscribers_m": [111, 35, 31, 25, 32, 40, 19, 10],
            "views_b": [29.5, 19.8, 13.4, 14.2, 4.3, 12.1, 3.2, 2.8],
            "monthly_views_m": [320, 210, 180, 150, 280, 380, 95, 60],
            "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444",
                        "#8b5cf6", "#06b6d4", "#f472b6", "#fb923c"]
        }
    }
