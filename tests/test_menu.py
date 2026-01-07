from playwright.sync_api import Page, expect
import re

def test_visit_menu_links(page:Page):
    print("Given the user opens W3Schools homepage")
    #Abrir la página principal de W3Schools
    page.goto("https://www.w3schools.com/")

    print("When the user accepts cookies")
    #Localizamos el elemento por texto
    page.get_by_text("Accept all").click()

    print("And clicks on HTML menu link")
    #Localizamos el elemento por rol (button, link, heading) y por texto exacto
    page.get_by_role("link", name="HTML", exact=True).click()
    print("Then the user should be on HTML tutorial page")
    #Comprobamos que la URL contiene "html"
    expect(page).to_have_url(re.compile("html"))
    #Comprueba que el título de la página contiene el texto exacto "HTML Tutorial"
    expect(page).to_have_title("HTML Tutorial")
    #Localizamos el elemnento con título heading (H1), que tenga el texto exacto "HTML Tutorial".
    expect(page.get_by_role("heading", name="HTML Tutorial", exact=True)).to_be_visible

    print("And clicks on CSS menu")
    page.get_by_role("link", name="CSS", exact=True).click()
    print("Then the user should be on CSS tutorial page")
    #Comprobamos que la URL contiene "css"
    expect(page).to_have_url(re.compile("css"))
    #Comprueba que el título de la página contiene el texto exacto "CSS Tutorial"
    expect(page).to_have_title("CSS Tutorial")
    #Localizamos el elemnento con título heading (H1), que tenga el texto exacto "CSS Tutorial".
    expect(page.get_by_role("heading", name="CSS Tutorial", exact=True)).to_be_visible

    print("And clicks on JAVASCRIPT menu")
    page.get_by_role("link", name="JAVASCRIPT", exact=True).click()
    print("Then the user should be on JavaScript tutorial page")
    #Comprobamos que la URL contiene "javascript"
    expect(page).to_have_url(re.compile("javascript"))
    #Comprueba que el título de la página contiene el texto exacto "JavaScript Tutorial"
    expect(page).to_have_title("JavaScript Tutorial")
    #Localizamos el elemnento con título heading (H1), que tenga el texto exacto "JavaScript Tutorial".
    expect(page.get_by_role("heading", name="JavaScript Tutorial", exact=True)).to_be_visible

    print("And clicks on SQL menu")
    page.get_by_role("link", name="SQL", exact=True).click()
    print("Then the user should be on SQL tutorial page")
    #Comprobamos que la URL contiene "sql"
    expect(page).to_have_url(re.compile("sql"))
    #Comprueba que el título de la página contiene el texto exacto "SQL Tutorial"
    expect(page).to_have_title("SQL Tutorial")
    #Localizamos el elemnento con título heading (H1), que tenga el texto exacto "SQL Tutorial".
    expect(page.get_by_role("heading", name="SQL Tutorial", exact=True)).to_be_visible

    print("And clicks on PYTHON menu")
    page.get_by_role("link", name="PYTHON", exact=True).click()
    print("Then the user should be on Python tutorial page")
    #Comprobamos que la URL contiene "python"
    expect(page).to_have_url(re.compile("python"))
    #Comprueba que el título de la página contiene el texto exacto "Python Tutorial"
    expect(page).to_have_title("Python Tutorial")
    #Localizamos el elemnento con título heading (H1), que tenga el texto exacto "Python Tutorial".
    expect(page.get_by_role("heading", name="Python Tutorial", exact=True)).to_be_visible

    print("And clicks on JAVA menu")
    page.get_by_role("link", name="JAVA", exact=True).click()
    print("Then the user should be on Java tutorial page")
    #Comprobamos que la URL contiene "java"
    expect(page).to_have_url(re.compile("java"))
    #Comprueba que el título de la página contiene el texto exacto "Java Tutorial"
    expect(page).to_have_title("Java Tutorial")
    #Localizamos el elemnento con título heading (H1), que tenga el texto exacto "Java Tutorial".
    expect(page.get_by_role("heading", name="Java Tutorial", exact=True)).to_be_visible 