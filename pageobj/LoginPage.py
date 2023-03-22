from pageobj.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):


    Pizza_BUTTON = (By.XPATH, "//img[@alt='Chat agent button']")
    get_started_button = (By.XPATH, "//a[text() ='Get Started']")
    FirstNAME_FIELD = (By.ID, "first_name")
    LastName_FIELD = (By.ID, "last_name")
    Email_id_field = (By.ID, "email")
    next_button =(By.XPATH,"//button[text()='Next']")


    def __init__(self, driver):
        super().__init__(driver)


    def Login_start_Conversation(self, firstname, lastname,email):
        self.click(self.Pizza_BUTTON)
        self.click(self.get_started_button)
        self.swith_to_frame("avaamoIframe")
        self.type(self.FirstNAME_FIELD,firstname)
        self.type(self.LastName_FIELD,lastname)
        self.type(self.Email_id_field,email)
        self.click(self.next_button)
        self.verify_page_should_contain("Welcome to McPizza Booking Journey")