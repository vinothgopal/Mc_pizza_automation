from pageobj.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import config.config as confi
import pyautogui
class HomePage(BasePage):

    type_message = (By.ID, "queryTextbox")
    send_button = (By.XPATH, "//button[@aria-label='Send']")
    click_veg_pizza= (By.XPATH,"//a[text()='veg']")
    click_nonveg_pizza = (By.XPATH, "//a[text()='non-veg']")
    cheese_checkbox = (By.XPATH,"//input[@value='cheese_id']")
    tomato_checkbox =(By.XPATH,"//input[@value='tomato_id']")
    submit_button = (By.XPATH,"//button[text()='Submit']")
    select_pizza =(By.XPATH,"//a[text()='Thick Crust']")
    pizza_size =(By.XPATH,"//a[text()='Medium']")
    yes_button =(By.XPATH,"//a[text()='Yes']")
    bacon_checkbox =(By.XPATH,"//input[@value='bacon_id']")

    def __init__(self, driver):
        super().__init__(driver)

    def order_veg_pizza(self):
        self.type(self.type_message,"I want to order pizza")
        self.click(self.send_button)
        self.click(self.click_veg_pizza)
        self.javascript_click(self.cheese_checkbox)
        self.javascript_click(self.submit_button)
        self.click(self.select_pizza)
        self.click(self.pizza_size)
        self.verify_page_should_contain("Would you like to confirm the order")
        self.click(self.yes_button)
        self.verify_page_should_contain("CONGRATS ! ORDER PLACED .")
        self.screenshot("order_veg_pizza")

    def order_Nonveg_pizza(self):
        self.type(self.type_message,"I want to order pizza")
        self.click(self.send_button)
        self.click(self.click_nonveg_pizza)
        self.javascript_click(self.bacon_checkbox)
        self.javascript_click(self.submit_button)
        self.click(self.select_pizza)
        self.click(self.pizza_size)
        self.verify_page_should_contain("Would you like to confirm the order")
        self.click(self.yes_button)
        self.verify_page_should_contain("CONGRATS ! ORDER PLACED .")
        self.screenshot("order_Nonveg_pizza")

    def adhoc_scenarios(self):
        self.send_message_and_verify_response("How old are you?","I don't know. My maker hasn't told me")
        self.send_message_and_verify_response("Where did you come from?","I was developed in Silicon Valley")
        self.send_message_and_verify_response("Where did you get your name?","I am sorry. I don't have an answer for that")
        self.send_message_and_verify_response("Are you a robot?","Yes I am! Did I have you fooled?")
        self.send_message_and_verify_response("where do you live?","I live in cyberspace, for now.")

    def send_message_and_verify_response(self,message,responce):
        self.type(self.type_message, message)
        self.click(self.send_button)
        self.verify_page_should_contain(responce)