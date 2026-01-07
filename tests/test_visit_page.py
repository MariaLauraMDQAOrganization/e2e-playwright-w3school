from playwright.sync_api import Page, expect

def test_visit(page: Page):
    print("Given user visit homepage")
    page.goto("https://w3schools.com")
    page.pause()

    #Comprobar imagen por ALT
    expect(page.get_by_alt_text("CodeGame")).to_be_visible()
    #Comprobar elemento por TITLE. Filtrar de todos cuando hya varios, el que tenga el texto Tutorial
    page.get_by_tittle("HTML Tutorial").filter(has_text="Tutorial").click()
    #Comprobar elemento por TITLE. De todos coger el primero; el último; o el de la posición 0,1,2
    page.get_by_title("HTML Tutorial").first
    page.get_by_title("HTML Tutorial").last
    page.get_by_title("HTML Tutorial").nth(2)
    #Localizar por id el menu
    page.locator("#subtonav")
    #Localizar por clase
    page.locator(".classic")
    #Localizar por elemento
    page.locator("h1")
    #Localizar por atributo
    page.locator("input[aria-label='Search our tutorials']")
    

