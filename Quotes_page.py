# pages/quotes_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuotesPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    LOGIN_LINK = (By.XPATH, "//a[text()='Login']")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Logout')]")
    CHANGE_TAG = (By.XPATH, "//a[normalize-space()='change']")
    DEEPTHOUGHT_TAG = (By.XPATH, "//a[normalize-space()='deep-thoughts']")
    THINKING_TAG = (By.XPATH, "//a[normalize-space()='thinking']")
    WORLD_TAG = (By.XPATH, "//a[normalize-space()='world']")
    NEXT_BUTTON = (By.XPATH, "//li[@class='next']/a")

    # Actions
    def click_login_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()

    def enter_username(self, username):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD))
        field.clear()
        field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_logout_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGOUT_BUTTON)).click()

    def click_change_tag(self):
        self.driver.find_element(*self.CHANGE_TAG).click()

    def click_deepthought_tag(self):
        self.driver.find_element(*self.DEEPTHOUGHT_TAG).click()

    def click_thinking_tag(self):
        self.driver.find_element(*self.THINKING_TAG).click()

    def click_world_tag(self):
        self.driver.find_element(*self.WORLD_TAG).click()

    def get_next_buttons(self):
        return self.driver.find_elements(*self.NEXT_BUTTON)