"""
Reusable UI components — cards, chart helpers, and animated counters.
"""

import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from config import COLORS, SIDEBAR_WIDTH


# ------------------------------------------------------------------ #
#  Stat Card
# ------------------------------------------------------------------ #
def create_card(title, parent, color, badge_text, row=0, column=0):
    """
    Build a styled stat card and return the *value label* so the caller
    can update it (e.g. with count_up).
    """
    frame = ctk.CTkFrame(
        parent,
        corner_radius=15,
        fg_color=COLORS["card_bg"],
        border_width=2,
        border_color=color,
    )
    frame.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")

    # Header with title and badge
    header = ctk.CTkFrame(frame, fg_color="transparent")
    header.pack(fill="x", padx=15, pady=(15, 5))

    ctk.CTkLabel(
        header,
        text=title,
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#cbd5e1",
    ).pack(side="left")

    badge = ctk.CTkLabel(
        header,
        text=badge_text,
        font=ctk.CTkFont(size=10, weight="bold"),
        text_color="#ffffff",
        fg_color=color,
        corner_radius=10,
        padx=8,
        pady=2,
    )
    badge.pack(side="right")

    # Value label
    label = ctk.CTkLabel(
        frame,
        text="0",
        font=ctk.CTkFont(size=26, weight="bold"),
        text_color="#ffffff",
    )
    label.pack(pady=(8, 4))

    # Trend indicator
    ctk.CTkLabel(
        frame,
        text="↗ Trending Up",
        font=ctk.CTkFont(size=11),
        text_color=COLORS["success"],
    ).pack()

    # Hover effect
    frame.bind("<Enter>", lambda e: frame.configure(border_color="#ffffff"))
    frame.bind("<Leave>", lambda e: frame.configure(border_color=color))

    return label


# ------------------------------------------------------------------ #
#  Count-up Animation
# ------------------------------------------------------------------ #
def count_up(label, current, target, suffix):
    """Animate a label from *current* to *target* appending *suffix*."""
    if current <= target:
        label.configure(text=f"{current}{suffix}")
        label.after(15, count_up, label, current + 20, target, suffix)


# ------------------------------------------------------------------ #
#  Chart Embedding Helpers
# ------------------------------------------------------------------ #
def figure_width(app, fraction=1.0, dpi=90):
    """
    Return figure width in inches for a given fraction of the content area.
    *app* must be the root Tk/CTk window so we can read winfo_width().
    """
    app.update_idletasks()
    padding = 80  # scrollbar + padx margins
    available_px = max(app.winfo_width() - SIDEBAR_WIDTH - padding, 380)
    return max(4.0, (available_px * fraction) / dpi)


def embed_figure(fig, parent, padx=12, pady=10):
    """Embed a matplotlib Figure into a tkinter parent widget."""
    canvas = FigureCanvasTkAgg(fig, parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True, padx=padx, pady=pady)
    return canvas
