import flet as ft
from helpers import go_back  # Importing go_back to avoid circular import

def create_settings_page(page):
    """Generates the settings page UI with category-style buttons (3 per row)"""

    settings_options = [
        "Themes",
        "Fonts",
        "Accent Colours ",
        "Search Settings",
        "Customize Article Layout",
        "Default Settings",
        "Backup & Restore Preferences",
        "Change Language",
        "About This App",
        "View Changelog",
        "Report a Bug / Give Feedback"
    ]

    # Top bar with back button
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    on_click=lambda e: go_back(page),
                    icon_color="white"
                ),
                ft.Text("Settings", size=22, weight="bold", color="white"),
            ],
            alignment=ft.MainAxisAlignment.START
        ),
        bgcolor="#1F1F1F",
        padding=10,
        border_radius=20,
        width=page.window_width * 0.85,
        height=60
    )

    # Creating buttons just like category buttons (3 per row)
    settings_buttons = ft.Column(
        controls=[
            ft.Row([
                ft.Container(
                    ft.ElevatedButton(
                        text=settings_options[i],
                        bgcolor="white",
                        color="black",
                        width=250,  # Same width as home page category buttons
                        height=60,  # Same height as home page category buttons
                        on_click=lambda e, opt=settings_options[i]: handle_setting_click(page, opt)
                    ),
                    padding=10
                ) for i in range(j, min(j + 3, len(settings_options)))  # 3 buttons per row
            ], alignment=ft.MainAxisAlignment.CENTER) for j in range(0, len(settings_options), 3)
        ]
    )

    # Page Layout
    settings_page = ft.View(
        route="/settings",
        bgcolor="#2C2C2C",
        controls=[
            ft.Row([top_bar], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(
                content=settings_buttons,
                alignment=ft.alignment.center,
                expand=True
            )
        ]
    )

    return settings_page

def handle_setting_click(page, setting_name):
    """Handles what happens when a setting is clicked"""
    page.snack_bar = ft.SnackBar(
        ft.Text(f"Clicked: {setting_name}", color="white"),
        bgcolor="gray"
    )
    page.snack_bar.open = True
    page.update()
