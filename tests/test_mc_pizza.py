import pytest

from pageobj.LoginPage import LoginPage
from pageobj.HomePage import HomePage
import config.config as confi


@pytest.mark.usefixtures("setup")
class TestMcPizza:

    def test_Order_veg_Pizza(self):

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.Login_start_Conversation(confi.first_name,confi.last_name,confi.email_id)
        home_page.order_veg_pizza()

    def test_order_non_veg_Pizza(self):
        home_page = HomePage(self.driver)
        home_page.order_Nonveg_pizza()

    def test_Adhoc_scenarios(self):
        home_page = HomePage(self.driver)
        home_page.adhoc_scenarios()