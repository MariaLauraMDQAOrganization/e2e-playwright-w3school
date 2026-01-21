from playwright.sync_api import Page, expect
import re

def is_mobile(page:Page):
    escritorio = 1024
    is_mobile = False
    
    #Si el ancho de la ventana es menor que 1024px, es móvil
    if(page.viewport_size["width"] < escritorio):
        is_mobile = True

    return is_mobile