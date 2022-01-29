from product_lib.aspire_app import gui_constants as const
from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By

utility_obj = Utility()

class LoginPage(object):

    def login_to_app(self, driver, user, password):
        driver.maximize_window()
        driver.get('https://aspireapp.odoo.com')
        utility_obj.enter_text(driver, By.CSS_SELECTOR, const.username_css, user)
        utility_obj.enter_text(driver, By.CSS_SELECTOR, const.password_css, password)
        utility_obj.click(driver, By.CSS_SELECTOR, const.loginbutton_css)