import flet as ft
from ui import create_ui

def main(page: ft.Page):
    page.title = "User Manual"
    page.bgcolor = "#2C2C2C"  # Dark Grey Background
    create_ui(page)  # Call the function to set up UI
    page.update()

ft.app(target=main)
