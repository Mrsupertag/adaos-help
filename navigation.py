import flet as ft
from categories import get_category_content
from settings import create_settings_page
from helpers import go_back  # Import go_back from helpers.py to avoid circular import

def navigate_to_category(e, category, page):
    """Handles navigation to help categories and settings page"""
    
    # Special case: Open the settings page
    if category == "Settings":
        page.views.append(create_settings_page(page))  # Load settings page
    else:
        # Load the selected category's article
        article_content = get_category_content(category)
        
        page.views.append(ft.View(
            route=f"/{category.lower().replace(' ', '_')}",
            bgcolor="#2C2C2C",
            controls=[
                # Back Button (Top Bar)
                ft.Row(
                    [ft.Container(
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.icons.ARROW_BACK,
                                    on_click=lambda e: go_back(page),
                                    icon_color="white"
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            expand=True
                        ),
                        bgcolor="#1F1F1F",
                        padding=10,
                        border_radius=20,
                        width=page.window_width * 0.85,
                        height=60
                    )],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

                # Article Content (Scrollable)
                ft.Container(
                    content=ft.Column(
                        controls=article_content,
                        scroll=ft.ScrollMode.AUTO
                    ),
                    padding=40,
                    alignment=ft.alignment.center,
                    expand=True
                )
            ]
        ))

    page.update()
