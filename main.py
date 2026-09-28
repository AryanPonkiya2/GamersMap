"""
Entry point — launch the Gaming Analytics Dashboard.
"""

import customtkinter as ctk
from app import GamerStatsApp

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    GamerStatsApp().mainloop()
