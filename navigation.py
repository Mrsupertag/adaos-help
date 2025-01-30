import flet as ft
from categories import get_category_content

def navigate_to_category(e, category, page):
    article_content = get_category_content(category)  # Get content from categories.py

    page.views.append(ft.View(
        route=f"/{category.lower().replace(' ', '_')}",
        bgcolor="#2C2C2C",
        controls=[
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
            ft.Container(
                content=ft.Column(
                    controls=article_content,
                    scroll=ft.ScrollMode.AUTO
                ),
                padding=40,
                alignment=ft.alignment.center,
                expand=True  # Enable scrolling
            )
        ]
    ))
    page.update()

def go_back(page):
    if len(page.views) > 1:
        page.views.pop()
    else:
        page.views.clear()
        page.go("/")
    page.update()
