from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then
from Page.Quotes_page import QuotesPage
import time


#Setup
@given("user opens quotes website")
def open_site(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("https://quotes.toscrape.com")
    context.quotes = QuotesPage(context.driver)

@then("user should see the homepage")
def see_homepage(context):
    assert "Quotes" in context.driver.title


#Login 
@when("user clicks on login button")
def click_login_link(context):
    context.quotes.click_login_link()
    time.sleep(2)

@when("user enters username")
def enter_username(context):
    context.quotes.enter_username("anish")

@when("user enters password")
def enter_password(context):
    context.quotes.enter_password("Ani123@@##")

@when("user clicks submit button")
def click_submit(context):
    context.quotes.click_login_button()
    time.sleep(1)

@then("user should be logged in successfully")
def verify_login(context):
    assert "Logout" in context.driver.page_source


#Logout
@when("user clicks logout button")
def click_logout(context):
    context.quotes.click_logout_button()
    time.sleep(1)

@then("user should be logged out successfully")
def verify_logout(context):
    assert "Login" in context.driver.page_source


#Tags
@when("user clicks on Change tag")
def click_change_tag(context):
    context.quotes.click_change_tag()
    time.sleep(1)

@then("user should see Change tag quotes")
def verify_change_tag(context):
    assert "change" in context.driver.current_url

@when("user clicks on Deepthought tag")
def click_deepthought_tag(context):
    context.quotes.click_deepthought_tag()
    time.sleep(1)



@when("user clicks on Thinking tag")
def click_thinking_tag(context):
    context.quotes.click_thinking_tag()
    time.sleep(1)

@then("user should see Thinking tag quotes")
def verify_thinking_tag(context):
    assert "thinking" in context.driver.current_url

@when("user clicks on World tag")
def click_world_tag(context):
    context.quotes.click_world_tag()
    time.sleep(1)

@then("user should see World tag quotes")
def verify_world_tag(context):
    assert "world" in context.driver.current_url


#Navigation until last page
@when("user clicks next button until last page")
def click_next_until_end(context):
    while True:
        next_buttons = context.quotes.get_next_buttons()
        if next_buttons:
            next_buttons[0].click()
            time.sleep(2)
        else:
            print("Reached last page")
            break

@then("user should reach the last page")
def verify_last_page(context):
    assert len(context.quotes.get_next_buttons()) == 0





