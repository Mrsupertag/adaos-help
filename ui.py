import flet as ft
from navigation import navigate_to_category, go_back

def create_ui(page):
    # Top Bar
    top_bar = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(icon=ft.icons.SETTINGS, icon_color="white"),
                ft.Text("User Manual", size=22, weight="bold", color="white"),
                ft.IconButton(icon=ft.icons.SEARCH, on_click=lambda e: page.go("/search"), icon_color="white"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor="#1F1F1F",
        padding=10,
        border_radius=20,
        width=page.window_width * 0.85,
        height=60
    )

    # Main Heading
    heading = ft.Container(
        content=ft.Text("How to use AdaOS", size=36, weight="bold", color="white"),
        padding=40,
        alignment=ft.alignment.center
    )

    # Category Buttons
    categories = [
        "Linux Terminal",
        "File Management",
        "Software Installation",
        "System Settings",
        "Networking",
        "Security & Permissions",
        "User Management",
        "Disk Management",
        "Troubleshooting"
    ]

    category_buttons = ft.Column(
        controls=[
            ft.Row([
                ft.Container(
                    ft.ElevatedButton(
                        text=categories[i],
                        bgcolor="white",
                        color="black",
                        width=250,
                        height=60,
                        on_click=lambda e, c=categories[i]: navigate_to_category(e, c, page)
                    ),
                    padding=10
                ) for i in range(j, min(j + 3, len(categories)))
            ], alignment=ft.MainAxisAlignment.CENTER) for j in range(0, len(categories), 3)
        ]
    )

    # Add Components to Page
    page.add(
        ft.Row([top_bar], alignment=ft.MainAxisAlignment.CENTER),
        heading,
        category_buttons
    )
