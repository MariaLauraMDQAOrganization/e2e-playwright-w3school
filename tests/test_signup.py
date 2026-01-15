from playwright.sync_api import Page, expect
import uuid
def generar_email_aleatorio():
    textounico = uuid.uuid4().hex
    random_email = textounico + "@test.com"
    return random_email

def test_signup_with_valid_email(page:Page):
    print("Given the user open W3Schools signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When the user fills email with a valid email")
    #Limpiamos el campo emial con .clear()
    page.get_by_placeholder("email").clear()
    #Introducimos un email aleatorio y rellenamos el campo con placeholder email con ese email aleatorio
    email = generar_email_aleatorio()
    #Introducimos un email válido
    page.get_by_placeholder("email").fill(email)

    print ("And the user fills password with valid password")
    password = "Test-1234"
    #Limpiamos el campo password con .clear()
    page.get_by_placeholder("password").clear()
    #Rellenamos el campo password con un password válido
    page.get_by_placeholder("password").fill(password)

    print("And the user fills first name and last name")
    #Limpiamos el campo firs name con .clear()
    page.get_by_placeholder("first name").clear()
    #Rellenamos el campo first name con un nombre válido
    page.get_by_placeholder("first name").fill("Test Name")

    print("And the user fills last name")
    #Limpiamos el campo last name con .clear()
    page.get_by_placeholder("last name").clear()
    #Rellenamos el campo last name con un apellido válido
    page.get_by_placeholder("last name").fill("Test Last Name")

    print("And the user clicks on Create account button")
    #Hacemos clic en el botón Create account
    page.get_by_role("button", name="Create account").click()


def test_signup_with_empty_email(page: Page):
    print("Given the user open W3Schools signup page")
    page.goto("https://profile.w3schools.com/signup")

    print("When user leaves the email field empty")
    #Dejamos vacío el campo email con clear
    page.get_by_placeholder("email").clear()

    print("And the user fills password")
    page.get_by_placeholder("password").clear()
    page.get_by_placeholder("password").fill("test1234")
    print("And the user fills first name and last name")
    page.get_by_placeholder("first name").clear()
    page.get_by_placeholder("first name").fill("María ")

    print("And the user fills last name")
    page.get_by_placeholder("last name").clear()
    page.get_by_placeholder("last name").fill("Monge")
   
    print("When the user clicks on Create account button")
    page.get_by_role("button", name="Create account").click()

    print("Then the user should see an error message indicating that email is required")
    expect(page.get_by_text("Please fill in all fields")).to_be_visible()



def test_signup_with_empty_password(page: Page):
    print("Given the user open W3Schools login page")
    page.goto("https://profile.w3schools.com/login")
    
    print("When user fills email")
    page.get_by_placeholder("email").fill("maria@gmail.com")
    
    print("And the user leaves the password field empty")
    page.get_by_placeholder("password").clear()

    print("When the user clicks on Sign in button")
    page.get_by_role("button", name="Sign in").click()

    print("Then the user should see an error message indicating that password is required")
    expect(page.get_by_text("Please enter your email and")).to_be_visible()

