import customtkinter as ctk
from tkinter import Canvas
import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class GamerStatsApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gaming Analytics Dashboard")
        self.geometry("1280x750")
        self.minsize(900, 600)

        # Enhanced color scheme
        self.colors = {
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

        # Navigation history
        self.page_history = ["Dashboard"]
        self.current_page = "Dashboard"

        # Sample gaming data
        self.gaming_data = self.generate_sample_data()

        # Fade-in start
        self.attributes("-alpha", 0.0)

        self.create_layout()

        # Animations
        self.fade_in()
        self.slide_sidebar()

    # ---------------- SAMPLE DATA ----------------
    def generate_sample_data(self):
        return {
            "line_chart": {
                "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
                "world_players": [2800, 2850, 2900, 2950, 3000, 3050, 3080, 3100, 3150, 3180, 3190, 3200],
                "india_players": [480, 495, 510, 525, 535, 540, 545, 550, 555, 560, 565, 568],
                "revenue": [120, 125, 130, 135, 140, 142, 145, 148, 152, 155, 157, 159]
            },
            "bar_chart": {
                "platforms": ["Mobile", "PC", "Console", "VR", "Cloud"],
                "users": [1850, 980, 720, 85, 165],
                "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6"]
            },
            "pie_chart": {
                "regions": ["Asia", "North America", "Europe", "South America", "Africa", "Oceania"],
                "percentages": [45, 25, 18, 7, 3, 2],
                "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4"]
            },
            "genres": {
                "labels": ["Action", "RPG", "Sports", "Strategy", "Shooter", "Racing"],
                "values": [28, 22, 15, 12, 18, 5],
                "colors": ["#ef4444", "#f59e0b", "#10b981", "#3b82f6", "#8b5cf6", "#06b6d4"]
            },
            "map_view": {
                "regions": ["Asia", "North America", "Europe", "South America", "Middle East", "Africa", "Oceania"],
                "gamers_m": [1440, 800, 576, 224, 96, 96, 64],
                "growth_pct": [14.2, 8.5, 6.3, 11.7, 18.4, 22.1, 5.8],
                "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4", "#f472b6"]
            },
            "youtube_stats": {
                "channels": ["PewDiePie", "Markiplier", "Jacksepticeye", "VanossGaming", "Dream", "MrBeast Gaming", "Ninja", "Shroud"],
                "subscribers_m": [111, 35, 31, 25, 32, 40, 19, 10],
                "views_b": [29.5, 19.8, 13.4, 14.2, 4.3, 12.1, 3.2, 2.8],
                "monthly_views_m": [320, 210, 180, 150, 280, 380, 95, 60],
                "colors": ["#3b82f6", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6", "#06b6d4", "#f472b6", "#fb923c"]
            }
        }

    # ---------------- FADE-IN ----------------
    def fade_in(self, alpha=0.0):
        if alpha < 1.0:
            self.attributes("-alpha", alpha)
            self.after(20, self.fade_in, alpha + 0.05)

    # ---------------- LAYOUT ----------------
    def create_layout(self):
        # Container with gradient effect
        self.container = ctk.CTkFrame(self, fg_color=self.colors["dark_bg"])
        self.container.pack(fill="both", expand=True)

        # Enhanced Sidebar — packed on the left so it doesn't steal main area space
        self.sidebar = ctk.CTkFrame(
            self.container,
            width=220,
            corner_radius=0,
            fg_color=self.colors["card_bg"],
            border_width=1,
            border_color=self.colors["primary"]
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)   # keep fixed width

        # Logo section with styling
        self.logo_frame = ctk.CTkFrame(
            self.sidebar,
            fg_color=self.colors["primary"],
            height=65
        )
        self.logo_frame.pack(fill="x", pady=(0, 10))
        self.logo_frame.pack_propagate(False)

        self.logo = ctk.CTkLabel(
            self.logo_frame,
            text="🎮 GamerStats",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color="#ffffff"
        )
        self.logo.pack(expand=True)

        self.nav_buttons()

        # Footer in sidebar
        self.footer = ctk.CTkLabel(
            self.sidebar,
            text="© 2024 Analytics",
            font=ctk.CTkFont(size=10),
            text_color="#64748b"
        )
        self.footer.pack(side="bottom", pady=15)

        # Main area — takes all remaining space to the right of sidebar
        self.main_area = ctk.CTkFrame(
            self.container,
            fg_color=self.colors["dark_bg"]
        )
        self.main_area.pack(side="left", fill="both", expand=True)

        self.header()
        self.content()

    # ---------------- SIDEBAR SLIDE ----------------
    def slide_sidebar(self):
        # Sidebar animation is now handled by pack layout; no slide needed.
        pass

    # ---------------- NAV ----------------
    def nav_buttons(self):
        buttons = [
            ("📊 Dashboard", "Dashboard"),
            ("📈 Line Charts", "Line Charts"),
            ("📊 Bar Charts", "Bar Charts"),
            ("🥧 Pie Charts", "Pie Charts"),
            ("🎲 3D Charts", "3D Charts"),
            ("🗺️ Map View", "Map View"),
            ("▶️ YouTube Stats", "YouTube Stats")
        ]

        self.nav_btn_list = []

        for icon_name, name in buttons:
            btn = ctk.CTkButton(
                self.sidebar,
                text=icon_name,
                height=38,
                anchor="w",
                corner_radius=8,
                fg_color="transparent",
                hover_color=self.colors["hover"],
                border_width=0,
                font=ctk.CTkFont(size=13, weight="bold"),
                command=lambda n=name: self.load_page(n)
            )
            btn.pack(fill="x", padx=15, pady=3)
            self.nav_btn_list.append(btn)

            # Enhanced hover effects
            btn.bind("<Enter>", lambda e, b=btn: self.on_nav_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self.on_nav_hover(b, False))

    def on_nav_hover(self, button, is_enter):
        if is_enter:
            button.configure(
                fg_color=self.colors["hover"],
                border_width=2,
                border_color=self.colors["accent"]
            )
        else:
            button.configure(
                fg_color="transparent",
                border_width=0
            )

    # ---------------- HEADER ----------------
    def header(self):
        self.header_frame = ctk.CTkFrame(
            self.main_area,
            height=80,
            fg_color=self.colors["card_bg"],
            corner_radius=12,
            border_width=1,
            border_color=self.colors["primary"]
        )
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))

        # Back button
        self.back_btn = ctk.CTkButton(
            self.header_frame,
            text="← Back",
            width=90,
            height=35,
            corner_radius=8,
            fg_color=self.colors["card_bg"],
            hover_color=self.colors["hover"],
            border_width=2,
            border_color=self.colors["accent"],
            font=ctk.CTkFont(weight="bold"),
            command=self.go_back
        )
        self.back_btn.pack(side="left", padx=(20, 10))
        self.update_back_button()

        # Title with subtitle
        self.title_container = ctk.CTkFrame(
            self.header_frame,
            fg_color="transparent"
        )
        self.title_container.pack(side="left", padx=10)

        self.title_label = ctk.CTkLabel(
            self.title_container,
            text="Dashboard Overview",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#ffffff"
        )
        self.title_label.pack(anchor="w")

        self.subtitle_label = ctk.CTkLabel(
            self.title_container,
            text="Real-time gaming statistics and analytics",
            font=ctk.CTkFont(size=11),
            text_color="#94a3b8"
        )
        self.subtitle_label.pack(anchor="w")

        # Action buttons
        self.btn_container = ctk.CTkFrame(
            self.header_frame,
            fg_color="transparent"
        )
        self.btn_container.pack(side="right", padx=10)

        self.export_btn = ctk.CTkButton(
            self.btn_container,
            text="📥 Export",
            width=100,
            height=35,
            corner_radius=8,
            fg_color=self.colors["success"],
            hover_color="#059669",
            font=ctk.CTkFont(weight="bold")
        )
        self.export_btn.pack(side="left", padx=5)

        self.refresh_btn = ctk.CTkButton(
            self.btn_container,
            text="🔄 Refresh",
            width=100,
            height=35,
            corner_radius=8,
            fg_color=self.colors["secondary"],
            hover_color=self.colors["hover"],
            font=ctk.CTkFont(weight="bold"),
            command=self.refresh_data
        )
        self.refresh_btn.pack(side="left", padx=5)

    # ---------------- CONTENT ----------------
    def content(self):
        self.content_frame = ctk.CTkScrollableFrame(
            self.main_area,
            fg_color="transparent"
        )
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.dashboard_cards()

    # ---------------- DASHBOARD ----------------
    def dashboard_cards(self):
        # Main container for cards with grid layout
        cards_container = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        cards_container.pack(fill="both", expand=True, pady=10)
        
        # Configure grid to be responsive
        cards_container.grid_columnconfigure(0, weight=1)
        cards_container.grid_columnconfigure(1, weight=1)
        cards_container.grid_rowconfigure(0, weight=1)
        cards_container.grid_rowconfigure(1, weight=1)

        # Create cards in grid layout
        self.world = self.card(
            "🌍 World Gamers",
            cards_container,
            self.colors["secondary"],
            "+12.5%",
            row=0, column=0
        )
        self.india = self.card(
            "🇮🇳 India Gamers",
            cards_container,
            self.colors["success"],
            "+8.3%",
            row=0, column=1
        )
        self.platform = self.card(
            "📱 Top Platform",
            cards_container,
            self.colors["warning"],
            "Most Popular",
            text_only=True,
            row=1, column=0
        )
        self.revenue = self.card(
            "💰 Revenue",
            cards_container,
            self.colors["danger"],
            "+15.7%",
            row=1, column=1
        )

        # Animate counts
        self.count_up(self.world, 0, 3200, " M")
        self.count_up(self.india, 0, 568, " M")
        self.platform.configure(text="📱 Mobile")
        self.count_up(self.revenue, 0, 159, " B")

        # Add chart section
        self.add_chart_section()

    def card(self, title, parent, color, badge_text, text_only=False, row=0, column=0):
        # Enhanced card with gradient and shadow effect using grid
        frame = ctk.CTkFrame(
            parent,
            corner_radius=15,
            fg_color=self.colors["card_bg"],
            border_width=2,
            border_color=color
        )
        frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

        # Header with title and badge
        header = ctk.CTkFrame(frame, fg_color="transparent")
        header.pack(fill="x", padx=15, pady=(15, 5))

        ctk.CTkLabel(
            header,
            text=title,
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#cbd5e1"
        ).pack(side="left")

        badge = ctk.CTkLabel(
            header,
            text=badge_text,
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#ffffff",
            fg_color=color,
            corner_radius=10,
            padx=8,
            pady=2
        )
        badge.pack(side="right")

        # Value label
        label = ctk.CTkLabel(
            frame,
            text="0",
            font=ctk.CTkFont(size=26, weight="bold"),
            text_color="#ffffff"
        )
        label.pack(pady=(8, 4))

        # Trend indicator
        trend = ctk.CTkLabel(
            frame,
            text="↗ Trending Up",
            font=ctk.CTkFont(size=11),
            text_color=self.colors["success"]
        )
        trend.pack()

        # Hover effect
        frame.bind("<Enter>", lambda e: frame.configure(border_color="#ffffff"))
        frame.bind("<Leave>", lambda e: frame.configure(border_color=color))

        return label

    def add_chart_section(self):
        # Chart preview section
        chart_container = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=1,
            border_color=self.colors["primary"]
        )
        chart_container.pack(fill="both", expand=True, pady=20)

        # Chart header
        chart_header = ctk.CTkFrame(chart_container, fg_color="transparent")
        chart_header.pack(fill="x", padx=20, pady=15)

        ctk.CTkLabel(
            chart_header,
            text="📊 Gaming Trends Overview",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(side="left")

        # Mini line chart preview
        self.create_mini_chart(chart_container)

    def create_mini_chart(self, parent):
        fig = Figure(figsize=(self._fw(), 2.8), dpi=90, facecolor='#1e293b')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#0f172a')
        data = self.gaming_data["line_chart"]
        ax.plot(data["months"], data["world_players"],
                color='#3b82f6', linewidth=2, marker='o', markersize=4, label='World Gamers (M)')
        ax.plot(data["months"], data["india_players"],
                color='#10b981', linewidth=2, marker='s', markersize=4, label='India Gamers (M)')
        ax.set_title('Player Growth Trends 2024', color='white', fontsize=10, pad=6)
        ax.legend(loc='upper left', facecolor='#1e293b', edgecolor='#3b82f6', labelcolor='white', fontsize=8)
        ax.tick_params(colors='#94a3b8', labelsize=7)
        ax.grid(True, alpha=0.2, color='#475569')
        for sp in ax.spines.values():
            sp.set_color('#475569')
        fig.tight_layout(pad=1.0)
        self._embed(fig, parent, padx=15, pady=(0, 15))

    # ---------------- COUNT UP ----------------
    def count_up(self, label, current, target, suffix):
        if current <= target:
            label.configure(text=f"{current}{suffix}")
            label.after(15, self.count_up, label, current + 20, target, suffix)

    # ---------------- RESPONSIVE CHART HELPERS ----------------
    def _fw(self, fraction=1.0, dpi=90):
        """Return figure width in inches for a given fraction of the content area."""
        self.update_idletasks()
        sidebar_w = 220
        padding = 80  # scrollbar + padx margins
        available_px = max(self.winfo_width() - sidebar_w - padding, 380)
        return max(4.0, (available_px * fraction) / dpi)

    def _embed(self, fig, parent, padx=12, pady=10):
        """Embed a matplotlib figure into a tkinter parent, filling it fully."""
        canvas = FigureCanvasTkAgg(fig, parent)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True, padx=padx, pady=pady)
        return canvas

    # ---------------- REFRESH DATA ----------------
    def refresh_data(self):
        # Reload current page
        current = self.current_page
        self.load_page(current)

    # ---------------- PAGE SWITCH ----------------
    def load_page(self, page_name):
        # Add to history if it's a new page
        if page_name != self.current_page:
            self.page_history.append(page_name)
            self.current_page = page_name
        
        self.title_label.configure(text=page_name)
        self.subtitle_label.configure(text=f"Detailed view of {page_name.lower()}")
        self.update_back_button()

        for w in self.content_frame.winfo_children():
            w.destroy()

        # Load specific page content
        if page_name == "Dashboard":
            self.dashboard_cards()
        elif page_name == "Line Charts":
            self.show_line_charts()
        elif page_name == "Bar Charts":
            self.show_bar_charts()
        elif page_name == "Pie Charts":
            self.show_pie_charts()
        elif page_name == "3D Charts":
            self.show_3d_charts()
        elif page_name == "Map View":
            self.show_map_view()
        elif page_name == "YouTube Stats":
            self.show_youtube_stats()
        else:
            # Coming soon page
            self.show_coming_soon(page_name)

    # ---------------- LINE CHARTS PAGE ----------------
    def show_line_charts(self):
        # Header
        header = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            header,
            text="📈 Player Growth & Revenue Trends",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            header,
            text="Analyzing year-over-year gaming industry growth",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        ).pack(anchor="w")

        # Chart 1: Player Growth
        chart1_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=1,
            border_color=self.colors["primary"]
        )
        chart1_frame.pack(fill="x", expand=False, pady=8)

        fig1 = Figure(figsize=(self._fw(), 3.2), dpi=90, facecolor='#1e293b')
        ax1 = fig1.add_subplot(111)
        ax1.set_facecolor('#0f172a')
        data = self.gaming_data["line_chart"]
        ax1.plot(data["months"], data["world_players"],
                 color='#3b82f6', linewidth=2.5, marker='o', markersize=6, label='World Gamers (M)')
        ax1.plot(data["months"], data["india_players"],
                 color='#10b981', linewidth=2.5, marker='s', markersize=6, label='India Gamers (M)')
        ax1.set_title('Global & India Gaming Population 2024', color='white', fontsize=12, pad=8, weight='bold')
        ax1.set_xlabel('Month', color='#94a3b8', fontsize=9)
        ax1.set_ylabel('Players (Millions)', color='#94a3b8', fontsize=9)
        ax1.legend(loc='upper left', facecolor='#1e293b', edgecolor='#3b82f6', labelcolor='white', fontsize=8)
        ax1.tick_params(colors='#94a3b8', labelsize=8)
        ax1.grid(True, alpha=0.3, color='#475569', linestyle='--')
        for spine in ax1.spines.values():
            spine.set_color('#475569')
        fig1.tight_layout(pad=1.2)
        self._embed(fig1, chart1_frame)

        # Chart 2: Revenue Trend
        chart2_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=1,
            border_color=self.colors["primary"]
        )
        chart2_frame.pack(fill="x", expand=False, pady=8)

        fig2 = Figure(figsize=(self._fw(), 3.2), dpi=90, facecolor='#1e293b')
        ax2 = fig2.add_subplot(111)
        ax2.set_facecolor('#0f172a')
        ax2.plot(data["months"], data["revenue"],
                 color='#f59e0b', linewidth=2.5, marker='D', markersize=6, label='Revenue ($B)')
        ax2.fill_between(data["months"], data["revenue"], alpha=0.3, color='#f59e0b')
        ax2.set_title('Gaming Industry Revenue 2024', color='white', fontsize=12, pad=8, weight='bold')
        ax2.set_xlabel('Month', color='#94a3b8', fontsize=9)
        ax2.set_ylabel('Revenue (Billions $)', color='#94a3b8', fontsize=9)
        ax2.legend(loc='upper left', facecolor='#1e293b', edgecolor='#f59e0b', labelcolor='white', fontsize=8)
        ax2.tick_params(colors='#94a3b8', labelsize=8)
        ax2.grid(True, alpha=0.3, color='#475569', linestyle='--')
        for spine in ax2.spines.values():
            spine.set_color('#475569')
        fig2.tight_layout(pad=1.2)
        self._embed(fig2, chart2_frame)

    # ---------------- BAR CHARTS PAGE ----------------
    def show_bar_charts(self):
        # Header
        header = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            header,
            text="📊 Platform & Market Analysis",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            header,
            text="Comparing gaming platforms and market distribution",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        ).pack(anchor="w")

        # Chart: Platform Distribution
        chart_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=1,
            border_color=self.colors["primary"]
        )
        chart_frame.pack(fill="x", expand=False, pady=8)

        fig = Figure(figsize=(self._fw(), 3.5), dpi=90, facecolor='#1e293b')
        ax = fig.add_subplot(111)
        ax.set_facecolor('#0f172a')
        data = self.gaming_data["bar_chart"]
        bars = ax.bar(data["platforms"], data["users"], color=data["colors"],
                     edgecolor='white', linewidth=1.5, alpha=0.85)
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}M', ha='center', va='bottom', color='white', fontsize=9, weight='bold')
        ax.set_title('Gaming Platform User Distribution', color='white', fontsize=12, pad=8, weight='bold')
        ax.set_xlabel('Platform', color='#94a3b8', fontsize=9)
        ax.set_ylabel('Active Users (Millions)', color='#94a3b8', fontsize=9)
        ax.tick_params(colors='#94a3b8', labelsize=9)
        ax.grid(True, alpha=0.3, color='#475569', linestyle='--', axis='y')
        for spine in ax.spines.values():
            spine.set_color('#475569')
        fig.tight_layout(pad=1.2)
        self._embed(fig, chart_frame)

    # ---------------- PIE CHARTS PAGE ----------------
    def show_pie_charts(self):
        # Header
        header = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        
        ctk.CTkLabel(
            header,
            text="🥧 Market Share & Distribution",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        
        ctk.CTkLabel(
            header,
            text="Regional and genre distribution analysis",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        ).pack(anchor="w")

        # Container for two pie charts
        charts_container = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        charts_container.pack(fill="both", expand=True)
        
        charts_container.grid_columnconfigure(0, weight=1)
        charts_container.grid_columnconfigure(1, weight=1)

        # Chart 1: Regional Distribution
        chart1_frame = ctk.CTkFrame(
            charts_container,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=1,
            border_color=self.colors["primary"]
        )
        chart1_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        fig1 = Figure(figsize=(self._fw(0.47), 4.0), dpi=90, facecolor='#1e293b')
        ax1 = fig1.add_subplot(111)
        data1 = self.gaming_data["pie_chart"]
        wedges, texts, autotexts = ax1.pie(
            data1["percentages"],
            labels=data1["regions"],
            colors=data1["colors"],
            autopct='%1.1f%%',
            startangle=90,
            textprops={'color': 'white', 'fontsize': 8}
        )
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_weight('bold')
            autotext.set_fontsize(7)
        ax1.set_title('Regional Market Share', color='white', fontsize=11, pad=8, weight='bold')
        fig1.tight_layout(pad=0.8)
        self._embed(fig1, chart1_frame, padx=10, pady=10)

        # Chart 2: Genre Distribution
        chart2_frame = ctk.CTkFrame(
            charts_container,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=1,
            border_color=self.colors["primary"]
        )
        chart2_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        fig2 = Figure(figsize=(self._fw(0.47), 4.0), dpi=90, facecolor='#1e293b')
        ax2 = fig2.add_subplot(111)
        data2 = self.gaming_data["genres"]
        wedges2, texts2, autotexts2 = ax2.pie(
            data2["values"],
            labels=data2["labels"],
            colors=data2["colors"],
            autopct='%1.1f%%',
            startangle=45,
            explode=[0.05, 0, 0, 0, 0, 0],
            textprops={'color': 'white', 'fontsize': 8}
        )
        for autotext in autotexts2:
            autotext.set_color('white')
            autotext.set_weight('bold')
            autotext.set_fontsize(7)
        ax2.set_title('Popular Game Genres', color='white', fontsize=11, pad=8, weight='bold')
        fig2.tight_layout(pad=0.8)
        self._embed(fig2, chart2_frame, padx=10, pady=10)

    # ---------------- 3D CHARTS PAGE ----------------
    def show_3d_charts(self):
        header = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(
            header,
            text="🎲 3D Gaming Data Visualizations",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        ctk.CTkLabel(
            header,
            text="Interactive 3D charts for platform, genre and engagement analysis",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        ).pack(anchor="w")

        # ---- Row 1: 3D Bar + 3D Surface ----
        row1 = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        row1.pack(fill="both", expand=True, pady=5)
        row1.grid_columnconfigure(0, weight=1)
        row1.grid_columnconfigure(1, weight=1)

        # 3D Bar Chart — Platform Users
        bar3d_frame = ctk.CTkFrame(
            row1, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        bar3d_frame.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

        fig1 = Figure(figsize=(self._fw(0.47), 4.0), dpi=90, facecolor='#1e293b')
        ax1 = fig1.add_subplot(111, projection='3d')
        ax1.set_facecolor('#0f172a')
        fig1.patch.set_facecolor('#1e293b')
        platforms = self.gaming_data["bar_chart"]["platforms"]
        users = self.gaming_data["bar_chart"]["users"]
        colors_3d = self.gaming_data["bar_chart"]["colors"]
        xpos = list(range(len(platforms)))
        ypos = [0] * len(platforms)
        zpos = [0] * len(platforms)
        dx = dy = [0.6] * len(platforms)
        dz = users
        for i in range(len(xpos)):
            ax1.bar3d(xpos[i], ypos[i], zpos[i], dx[i], dy[i], dz[i],
                      color=colors_3d[i], alpha=0.85, shade=True)
        ax1.set_xticks(xpos)
        ax1.set_xticklabels(platforms, color='#94a3b8', fontsize=7)
        ax1.set_title('Platform Users (3D)', color='white', fontsize=10, weight='bold', pad=6)
        ax1.set_ylabel('', color='#94a3b8')
        ax1.set_zlabel('Users (M)', color='#94a3b8', fontsize=8)
        ax1.tick_params(colors='#94a3b8', labelsize=6)
        ax1.xaxis.pane.fill = False
        ax1.yaxis.pane.fill = False
        ax1.zaxis.pane.fill = False
        ax1.grid(True, alpha=0.15)
        fig1.tight_layout(pad=0.5)
        self._embed(fig1, bar3d_frame, padx=10, pady=10)

        # 3D Surface Chart — Genre Popularity Heatmap
        surf_frame = ctk.CTkFrame(
            row1, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        surf_frame.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")

        fig2 = Figure(figsize=(self._fw(0.47), 4.0), dpi=90, facecolor='#1e293b')
        ax2 = fig2.add_subplot(111, projection='3d')
        fig2.patch.set_facecolor('#1e293b')
        genres_short = ["Action", "RPG", "Sports", "Strategy", "Shooter", "Racing"]
        quarters = ["Q1", "Q2", "Q3", "Q4"]
        base = [28, 22, 15, 12, 18, 5]
        growth = [[1.00, 1.05, 1.10, 1.15],
                  [1.00, 1.08, 1.12, 1.18],
                  [1.00, 1.03, 1.07, 1.09],
                  [1.00, 1.06, 1.11, 1.14],
                  [1.00, 1.09, 1.13, 1.17],
                  [1.00, 1.02, 1.05, 1.07]]
        Z = np.array([[base[g] * growth[g][q] for q in range(4)] for g in range(6)])
        X, Y = np.meshgrid(range(4), range(6))
        surf = ax2.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.85, edgecolor='none')
        ax2.set_xticks(range(4))
        ax2.set_xticklabels(quarters, color='#94a3b8', fontsize=7)
        ax2.set_yticks(range(6))
        ax2.set_yticklabels(genres_short, color='#94a3b8', fontsize=6)
        ax2.set_title('Genre Popularity Surface', color='white', fontsize=10, weight='bold', pad=6)
        ax2.set_zlabel('Share %', color='#94a3b8', fontsize=8)
        ax2.tick_params(colors='#94a3b8', labelsize=6)
        ax2.xaxis.pane.fill = False
        ax2.yaxis.pane.fill = False
        ax2.zaxis.pane.fill = False
        fig2.colorbar(surf, ax=ax2, shrink=0.4, aspect=8, pad=0.08)
        fig2.tight_layout(pad=0.5)
        self._embed(fig2, surf_frame, padx=10, pady=10)

        # ---- Row 2: 3D Scatter ----
        scatter_frame = ctk.CTkFrame(
            self.content_frame, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        scatter_frame.pack(fill="both", expand=True, pady=8)

        fig3 = Figure(figsize=(self._fw(), 3.8), dpi=90, facecolor='#1e293b')
        ax3 = fig3.add_subplot(111, projection='3d')
        fig3.patch.set_facecolor('#1e293b')
        np.random.seed(42)
        n = 200
        age = np.random.randint(13, 45, n)
        hours_per_week = np.random.randint(1, 40, n)
        spending = np.random.exponential(scale=50, size=n).clip(0, 300)
        region_idx = np.random.randint(0, 7, n)
        scatter_colors = np.array(self.gaming_data["map_view"]["colors"])[region_idx]
        ax3.scatter(age, hours_per_week, spending, c=scatter_colors, s=25, alpha=0.7, edgecolors='none')
        ax3.set_xlabel('Age', color='#94a3b8', fontsize=8)
        ax3.set_ylabel('Hrs/Wk', color='#94a3b8', fontsize=8)
        ax3.set_zlabel('Spending ($)', color='#94a3b8', fontsize=8)
        ax3.set_title('Gamer Engagement: Age vs Hours vs Spending', color='white', fontsize=11, weight='bold', pad=8)
        ax3.tick_params(colors='#94a3b8', labelsize=6)
        ax3.xaxis.pane.fill = False
        ax3.yaxis.pane.fill = False
        ax3.zaxis.pane.fill = False
        ax3.grid(True, alpha=0.15)
        from matplotlib.lines import Line2D
        regions = self.gaming_data["map_view"]["regions"]
        rc = self.gaming_data["map_view"]["colors"]
        legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor=rc[i],
                                  markersize=5, label=regions[i]) for i in range(len(regions))]
        ax3.legend(handles=legend_elements, loc='upper left', facecolor='#1e293b',
                   edgecolor='#3b82f6', labelcolor='white', fontsize=7)
        fig3.tight_layout(pad=0.8)
        self._embed(fig3, scatter_frame, padx=15, pady=12)

    # ---------------- MAP VIEW PAGE ----------------
    def show_map_view(self):
        header = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(
            header,
            text="🗺️ Global Gamer Distribution",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        ctk.CTkLabel(
            header,
            text="Regional breakdown of gaming population and growth rates worldwide",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        ).pack(anchor="w")

        data = self.gaming_data["map_view"]

        # ---- Row 1: Horizontal Bar + Donut ----
        row1 = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        row1.pack(fill="both", expand=True, pady=5)
        row1.grid_columnconfigure(0, weight=3)
        row1.grid_columnconfigure(1, weight=2)

        # Horizontal bar chart - Gamers by region
        bar_frame = ctk.CTkFrame(
            row1, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        bar_frame.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

        fig1 = Figure(figsize=(self._fw(0.58), 3.8), dpi=90, facecolor='#1e293b')
        ax1 = fig1.add_subplot(111)
        ax1.set_facecolor('#0f172a')
        regions = data["regions"]
        gamers = data["gamers_m"]
        colors = data["colors"]
        sorted_idx = sorted(range(len(gamers)), key=lambda i: gamers[i])
        sorted_regions = [regions[i] for i in sorted_idx]
        sorted_gamers = [gamers[i] for i in sorted_idx]
        sorted_colors = [colors[i] for i in sorted_idx]
        bars = ax1.barh(sorted_regions, sorted_gamers, color=sorted_colors, alpha=0.85, edgecolor='none', height=0.6)
        for bar, val in zip(bars, sorted_gamers):
            ax1.text(val + 10, bar.get_y() + bar.get_height()/2,
                     f'{val}M', va='center', color='white', fontsize=8, weight='bold')
        ax1.set_title('Gamers by Region (Millions)', color='white', fontsize=11, weight='bold', pad=8)
        ax1.set_xlabel('Active Gamers (M)', color='#94a3b8', fontsize=8)
        ax1.tick_params(colors='#94a3b8', labelsize=8)
        ax1.grid(True, alpha=0.2, color='#475569', linestyle='--', axis='x')
        for spine in ax1.spines.values():
            spine.set_color('#475569')
        ax1.set_xlim(0, max(gamers) * 1.2)
        fig1.tight_layout(pad=1.0)
        self._embed(fig1, bar_frame, padx=10, pady=10)

        # Donut chart - share
        donut_frame = ctk.CTkFrame(
            row1, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        donut_frame.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")

        fig2 = Figure(figsize=(self._fw(0.37), 3.8), dpi=90, facecolor='#1e293b')
        ax2 = fig2.add_subplot(111)
        wedges, texts, autotexts = ax2.pie(
            gamers, labels=None, colors=colors,
            autopct='%1.0f%%', startangle=90,
            wedgeprops=dict(width=0.55),
            textprops={'color': 'white', 'fontsize': 7}
        )
        for at in autotexts:
            at.set_color('white')
            at.set_weight('bold')
            at.set_fontsize(7)
        ax2.legend(wedges, regions, loc='lower center', ncol=2,
                   bbox_to_anchor=(0.5, -0.22),
                   facecolor='#1e293b', edgecolor='#3b82f6',
                   labelcolor='white', fontsize=6)
        ax2.set_title('Regional Share', color='white', fontsize=11, weight='bold', pad=8)
        fig2.tight_layout(pad=0.5)
        self._embed(fig2, donut_frame, padx=10, pady=10)

        # ---- Row 2: Growth Rate bar ----
        growth_frame = ctk.CTkFrame(
            self.content_frame, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        growth_frame.pack(fill="both", expand=True, pady=8)

        fig3 = Figure(figsize=(self._fw(), 3.0), dpi=90, facecolor='#1e293b')
        ax3 = fig3.add_subplot(111)
        ax3.set_facecolor('#0f172a')
        growth = data["growth_pct"]
        bar3 = ax3.bar(regions, growth, color=colors, alpha=0.85, edgecolor='none', width=0.55)
        for b, v in zip(bar3, growth):
            ax3.text(b.get_x() + b.get_width()/2, v + 0.2,
                     f'{v}%', ha='center', color='white', fontsize=8, weight='bold')
        ax3.set_title('YoY Growth Rate by Region (%)', color='white', fontsize=11, weight='bold', pad=8)
        ax3.set_ylabel('Growth (%)', color='#94a3b8', fontsize=8)
        ax3.tick_params(colors='#94a3b8', labelsize=8)
        ax3.grid(True, alpha=0.2, color='#475569', linestyle='--', axis='y')
        for spine in ax3.spines.values():
            spine.set_color('#475569')
        ax3.set_ylim(0, max(growth) * 1.3)
        fig3.tight_layout(pad=1.0)
        self._embed(fig3, growth_frame, padx=15, pady=12)

    # ---------------- YOUTUBE STATS PAGE ----------------
    def show_youtube_stats(self):
        header = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(
            header,
            text="▶️ Gaming YouTube Statistics",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(anchor="w")
        ctk.CTkLabel(
            header,
            text="Top gaming YouTuber analytics: subscribers, views, and monthly performance",
            font=ctk.CTkFont(size=12),
            text_color="#94a3b8"
        ).pack(anchor="w")

        data = self.gaming_data["youtube_stats"]
        channels = data["channels"]
        subs = data["subscribers_m"]
        views = data["views_b"]
        monthly = data["monthly_views_m"]
        colors = data["colors"]

        # ---- Row 1: Subscribers bar + Views donut ----
        row1 = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        row1.pack(fill="both", expand=True, pady=5)
        row1.grid_columnconfigure(0, weight=3)
        row1.grid_columnconfigure(1, weight=2)

        # Bar chart - subscribers
        sub_frame = ctk.CTkFrame(
            row1, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        sub_frame.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

        fig1 = Figure(figsize=(self._fw(0.58), 3.8), dpi=90, facecolor='#1e293b')
        ax1 = fig1.add_subplot(111)
        ax1.set_facecolor('#0f172a')
        x = range(len(channels))
        bars = ax1.bar(x, subs, color=colors, alpha=0.85, edgecolor='none', width=0.65)
        for b, v in zip(bars, subs):
            ax1.text(b.get_x() + b.get_width()/2, v + 0.5,
                     f'{v}M', ha='center', color='white', fontsize=7, weight='bold')
        ax1.set_xticks(list(x))
        ax1.set_xticklabels(channels, rotation=25, ha='right', color='#94a3b8', fontsize=7)
        ax1.set_title('Gaming YouTubers — Subscribers (M)', color='white', fontsize=11, weight='bold', pad=8)
        ax1.set_ylabel('Subscribers (M)', color='#94a3b8', fontsize=8)
        ax1.tick_params(colors='#94a3b8', labelsize=7)
        ax1.grid(True, alpha=0.2, color='#475569', linestyle='--', axis='y')
        for spine in ax1.spines.values():
            spine.set_color('#475569')
        fig1.tight_layout(pad=1.0)
        self._embed(fig1, sub_frame, padx=10, pady=10)

        # Pie chart - total views share
        views_frame = ctk.CTkFrame(
            row1, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        views_frame.grid(row=0, column=1, padx=8, pady=8, sticky="nsew")

        fig2 = Figure(figsize=(self._fw(0.37), 3.8), dpi=90, facecolor='#1e293b')
        ax2 = fig2.add_subplot(111)
        wedges, texts, autotexts = ax2.pie(
            views, labels=None, colors=colors,
            autopct='%1.0f%%', startangle=90,
            explode=[0.05] + [0]*(len(channels)-1),
            textprops={'color': 'white', 'fontsize': 7}
        )
        for at in autotexts:
            at.set_color('white')
            at.set_weight('bold')
            at.set_fontsize(6)
        ax2.legend(wedges, [f'{c} ({v}B)' for c, v in zip(channels, views)],
                   loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.22),
                   facecolor='#1e293b', edgecolor='#3b82f6',
                   labelcolor='white', fontsize=5)
        ax2.set_title('Total Views Share (B)', color='white', fontsize=10, weight='bold', pad=8)
        fig2.tight_layout(pad=0.5)
        self._embed(fig2, views_frame, padx=10, pady=10)

        # ---- Row 2: Monthly views line chart ----
        monthly_frame = ctk.CTkFrame(
            self.content_frame, fg_color=self.colors["card_bg"],
            corner_radius=15, border_width=1, border_color=self.colors["primary"]
        )
        monthly_frame.pack(fill="both", expand=True, pady=8)

        fig3 = Figure(figsize=(self._fw(), 3.0), dpi=90, facecolor='#1e293b')
        ax3 = fig3.add_subplot(111)
        ax3.set_facecolor('#0f172a')
        months_yt = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan"]
        np.random.seed(7)
        for i in range(4):
            trend = [monthly[i] + np.random.randint(-15, 20) for _ in months_yt]
            trend[0] = monthly[i]
            ax3.plot(months_yt, trend, color=colors[i], linewidth=2,
                     marker='o', markersize=5, label=channels[i])
            ax3.fill_between(months_yt, trend, alpha=0.08, color=colors[i])
        ax3.set_title('Monthly Views Trend — Top 4 Channels (M)', color='white', fontsize=11, weight='bold', pad=8)
        ax3.set_xlabel('Month', color='#94a3b8', fontsize=8)
        ax3.set_ylabel('Monthly Views (M)', color='#94a3b8', fontsize=8)
        ax3.legend(loc='upper right', facecolor='#1e293b', edgecolor='#3b82f6',
                   labelcolor='white', fontsize=8)
        ax3.tick_params(colors='#94a3b8', labelsize=8)
        ax3.grid(True, alpha=0.2, color='#475569', linestyle='--')
        for spine in ax3.spines.values():
            spine.set_color('#475569')
        fig3.tight_layout(pad=1.0)
        self._embed(fig3, monthly_frame, padx=15, pady=12)

    # ---------------- COMING SOON ----------------
    def show_coming_soon(self, page_name):
        coming_soon = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.colors["card_bg"],
            corner_radius=15,
            border_width=2,
            border_color=self.colors["accent"]
        )
        coming_soon.pack(fill="both", expand=True, pady=40)

        ctk.CTkLabel(
            coming_soon,
            text=f"🚀 {page_name}",
            font=ctk.CTkFont(size=36, weight="bold")
        ).pack(pady=(60, 10))

        ctk.CTkLabel(
            coming_soon,
            text="This feature is under development",
            font=ctk.CTkFont(size=16),
            text_color="#94a3b8"
        ).pack(pady=10)

        ctk.CTkButton(
            coming_soon,
            text="← Back to Dashboard",
            command=lambda: self.load_page("Dashboard"),
            width=180,
            height=40,
            corner_radius=10,
            fg_color=self.colors["secondary"],
            hover_color=self.colors["hover"]
        ).pack(pady=20)

    # ---------------- BACK NAVIGATION ----------------
    def go_back(self):
        if len(self.page_history) > 1:
            # Remove current page
            self.page_history.pop()
            # Get previous page
            previous_page = self.page_history[-1]
            self.current_page = previous_page
            
            self.title_label.configure(text=previous_page)
            if previous_page == "Dashboard":
                self.subtitle_label.configure(text="Real-time gaming statistics and analytics")
            else:
                self.subtitle_label.configure(text=f"Detailed view of {previous_page.lower()}")
            
            self.update_back_button()

            for w in self.content_frame.winfo_children():
                w.destroy()

            # Load content based on page
            if previous_page == "Dashboard":
                self.dashboard_cards()
            elif previous_page == "Line Charts":
                self.show_line_charts()
            elif previous_page == "Bar Charts":
                self.show_bar_charts()
            elif previous_page == "Pie Charts":
                self.show_pie_charts()
            elif previous_page == "3D Charts":
                self.show_3d_charts()
            elif previous_page == "Map View":
                self.show_map_view()
            elif previous_page == "YouTube Stats":
                self.show_youtube_stats()
            else:
                self.show_coming_soon(previous_page)

    def update_back_button(self):
        # Enable/disable back button based on history
        if len(self.page_history) <= 1:
            self.back_btn.configure(state="disabled", fg_color="#1e293b")
        else:
            self.back_btn.configure(state="normal", fg_color=self.colors["card_bg"])


if __name__ == "__main__":
    GamerStatsApp().mainloop()