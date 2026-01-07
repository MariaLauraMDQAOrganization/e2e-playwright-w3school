from playwright.sync_api import Page, expect

def test_search_empty(page:Page):
    print("Given the user opens W3Schools homepage")
    page.goto("http://www.w3schools.com/")

    print("When the user accepts cookies")
    page.locator("iframe[title=\"FastCMP\"]").content_frame.get_by_role("button", name="Aceptar").click()

    print("And the user leaves the search field empty")
    #Presionamos el campo de búsqueda y lo dejamos vacío
    page.get_by_role("textbox", name="Search our tutorials").click()

    print("Then the user should keep seeing search bar")
    expect(page.get_by_role("textbox", name="Search our tutorials")).to_be_visible()

def test_search_valid_value(page:Page):
    print("Given the user opens W3Schools homepage")
    page.goto("http://www.w3schools.com/")

    print("When the user accepts cookies")
    page.locator("iframe[title=\"FastCMP\"]").content_frame.get_by_role("button", name="Aceptar").click()

    print("And the user fills the search field with a valid value")
    page.get_by_role("textbox", name="Search our tutorials").click()
    page.get_by_role("textbox", name="Search our tutorials").fill("html")
    page.get_by_role("textbox", name="Search our tutorials").press("Enter")

    print("Then the user should see relevant search results")
    page.locator("#listofsearchresults").get_by_role("link", name="HTML Tutorial").click()

