import flet as ft

def go_back(page):
    """Handles going back to the previous view"""
    if len(page.views) > 1:
        page.views.pop()
    else:
        page.views.clear()
        page.go("/")
    page.update()
