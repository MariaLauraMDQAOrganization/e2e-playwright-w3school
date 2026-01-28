from playwright.sync_api import Page, expect
import re

def test_search_empty(page:Page):
    print("Given the user opens W3Schools homepage")
    page.goto("http://www.w3schools.com/")

    try:
        print("When the user accepts cookies")
        #Localizamos el elemento por texto
        page.frame_locator("iframe[title=\"FastCMP\"]").get_by_role("button", name=re.compile("accept|aceptar", re.IGNORECASE)).click(timeout=3000)
    except:
        #Cuaquier excepción la ignoramos (no se muestra el banner)
        print("No cookie banner displayed")

    print("And the user leaves the search field empty")
    #Presionamos el campo de búsqueda y lo dejamos vacío
    page.get_by_role("textbox", name="Search our tutorials").click()

    print("Then the user should keep seeing search bar")
    expect(page.get_by_role("textbox", name="Search our tutorials")).to_be_visible()

def test_search_valid_value(page:Page):
    print("Given the user opens W3Schools homepage")
    page.goto("http://www.w3schools.com/")
    try:
        print("When the user accepts cookies")
        #Localizamos el elemento por texto
        page.frame_locator("iframe[title=\"FastCMP\"]").get_by_role("button", name=re.compile("accept|aceptar", re.IGNORECASE)).click(timeout=3000)
    except:
        #Cuaquier excepción la ignoramos (no se muestra el banner)
        print("No cookie banner displayed")

    print("And the user fills the search field with a valid value")
    page.get_by_role("textbox", name="Search our tutorials").click()
    page.get_by_role("textbox", name="Search our tutorials").fill("html")
    page.get_by_role("textbox", name="Search our tutorials").press("Enter")

