"""
GamerStatsApp — main application class.
Handles window setup, sidebar navigation, header, and page routing.
"""

import customtkinter as ctk

from config import (
    COLORS, WINDOW_TITLE, WINDOW_GEOMETRY, WINDOW_MIN_SIZE,
    SIDEBAR_WIDTH, NAV_ITEMS,
)
from data import generate_sample_data
from pages import PAGE_REGISTRY
from pages.coming_soon import show_coming_soon


class GamerStatsApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(WINDOW_GEOMETRY)
        self.minsize(*WINDOW_MIN_SIZE)

        # Navigation history
        self.page_history = ["Dashboard"]
        self.current_page = "Dashboard"

        # Sample gaming data
        self.gaming_data = generate_sample_data()

        # Fade-in start
        self.attributes("-alpha", 0.0)

        self._create_layout()

        # Animations
        self._fade_in()

    # ------------------------------------------------------------------ #
    #  Fade-in animation
    # ------------------------------------------------------------------ #
    def _fade_in(self, alpha=0.0):
        if alpha < 1.0:
            self.attributes("-alpha", alpha)
            self.after(20, self._fade_in, alpha + 0.05)

    # ------------------------------------------------------------------ #
    #  Layout
    # ------------------------------------------------------------------ #
    def _create_layout(self):
        # Root container
        self.container = ctk.CTkFrame(self, fg_color=COLORS["dark_bg"])
        self.container.pack(fill="both", expand=True)

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self.container,
            width=SIDEBAR_WIDTH,
            corner_radius=0,
            fg_color=COLORS["card_bg"],
            border_width=1,
            border_color=COLORS["primary"],
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo
        logo_frame = ctk.CTkFrame(
            self.sidebar, fg_color=COLORS["primary"], height=65,
        )
        logo_frame.pack(fill="x", pady=(0, 10))
        logo_frame.pack_propagate(False)

        ctk.CTkLabel(
            logo_frame,
            text="🎮 GamerStats",
            font=ctk.CTkFont(size=17, weight="bold"),
            text_color="#ffffff",
        ).pack(expand=True)

        self._create_nav_buttons()

        # Footer
        ctk.CTkLabel(
            self.sidebar,
            text="© 2024 Analytics",
            font=ctk.CTkFont(size=10),
            text_color="#64748b",
        ).pack(side="bottom", pady=15)

        # Main area
        self.main_area = ctk.CTkFrame(
            self.container, fg_color=COLORS["dark_bg"],
        )
        self.main_area.pack(side="left", fill="both", expand=True)

        self._create_header()
        self._create_content()

    # ------------------------------------------------------------------ #
    #  Navigation buttons
    # ------------------------------------------------------------------ #
    def _create_nav_buttons(self):
        self.nav_btn_list = []

        for icon_name, name in NAV_ITEMS:
            btn = ctk.CTkButton(
                self.sidebar,
                text=icon_name,
                height=38,
                anchor="w",
                corner_radius=8,
                fg_color="transparent",
                hover_color=COLORS["hover"],
                border_width=0,
                font=ctk.CTkFont(size=13, weight="bold"),
                command=lambda n=name: self.load_page(n),
            )
            btn.pack(fill="x", padx=15, pady=3)
            self.nav_btn_list.append(btn)

            btn.bind("<Enter>", lambda e, b=btn: self._on_nav_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self._on_nav_hover(b, False))

    def _on_nav_hover(self, button, is_enter):
        if is_enter:
            button.configure(
                fg_color=COLORS["hover"],
                border_width=2,
                border_color=COLORS["accent"],
            )
        else:
            button.configure(fg_color="transparent", border_width=0)

    # ------------------------------------------------------------------ #
    #  Header
    # ------------------------------------------------------------------ #
    def _create_header(self):
        self.header_frame = ctk.CTkFrame(
            self.main_area,
            height=80,
            fg_color=COLORS["card_bg"],
            corner_radius=12,
            border_width=1,
            border_color=COLORS["primary"],
        )
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))

        # Back button
        self.back_btn = ctk.CTkButton(
            self.header_frame,
            text="← Back",
            width=90,
            height=35,
            corner_radius=8,
            fg_color=COLORS["card_bg"],
            hover_color=COLORS["hover"],
            border_width=2,
            border_color=COLORS["accent"],
            font=ctk.CTkFont(weight="bold"),
            command=self._go_back,
        )
        self.back_btn.pack(side="left", padx=(20, 10))
        self._update_back_button()

        # Title with subtitle
        title_container = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        title_container.pack(side="left", padx=10)

        self.title_label = ctk.CTkLabel(
            title_container,
            text="Dashboard Overview",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#ffffff",
        )
        self.title_label.pack(anchor="w")

        self.subtitle_label = ctk.CTkLabel(
            title_container,
            text="Real-time gaming statistics and analytics",
            font=ctk.CTkFont(size=11),
            text_color="#94a3b8",
        )
        self.subtitle_label.pack(anchor="w")

        # Action buttons
        btn_container = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        btn_container.pack(side="right", padx=10)

        ctk.CTkButton(
            btn_container,
            text="📥 Export",
            width=100,
            height=35,
            corner_radius=8,
            fg_color=COLORS["success"],
            hover_color="#059669",
            font=ctk.CTkFont(weight="bold"),
        ).pack(side="left", padx=5)

        ctk.CTkButton(
            btn_container,
            text="🔄 Refresh",
            width=100,
            height=35,
            corner_radius=8,
            fg_color=COLORS["secondary"],
            hover_color=COLORS["hover"],
            font=ctk.CTkFont(weight="bold"),
            command=self._refresh_data,
        ).pack(side="left", padx=5)

    # ------------------------------------------------------------------ #
    #  Content area
    # ------------------------------------------------------------------ #
    def _create_content(self):
        self.content_frame = ctk.CTkScrollableFrame(
            self.main_area, fg_color="transparent",
        )
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Show default page
        self.load_page("Dashboard")

    # ------------------------------------------------------------------ #
    #  Page routing
    # ------------------------------------------------------------------ #
    def load_page(self, page_name):
        """Switch to the requested page."""
        if page_name != self.current_page:
            self.page_history.append(page_name)
            self.current_page = page_name

        self.title_label.configure(text=page_name)
        self.subtitle_label.configure(
            text=(
                "Real-time gaming statistics and analytics"
                if page_name == "Dashboard"
                else f"Detailed view of {page_name.lower()}"
            )
        )
        self._update_back_button()

        for w in self.content_frame.winfo_children():
            w.destroy()

        render_fn = PAGE_REGISTRY.get(page_name)
        if render_fn:
            render_fn(self, self.content_frame, self.gaming_data)
        else:
            show_coming_soon(self, self.content_frame, self.gaming_data,
                             page_name=page_name)

    # ------------------------------------------------------------------ #
    #  Refresh
    # ------------------------------------------------------------------ #
    def _refresh_data(self):
        self.load_page(self.current_page)

    # ------------------------------------------------------------------ #
    #  Back navigation
    # ------------------------------------------------------------------ #
    def _go_back(self):
        if len(self.page_history) > 1:
            self.page_history.pop()
            previous_page = self.page_history[-1]
            self.current_page = previous_page
            self.load_page(previous_page)

    def _update_back_button(self):
        if len(self.page_history) <= 1:
            self.back_btn.configure(state="disabled", fg_color="#1e293b")
        else:
            self.back_btn.configure(state="normal",
                                    fg_color=COLORS["card_bg"])
