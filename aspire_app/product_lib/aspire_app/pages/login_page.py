#!/usr/bin/python
"""
.. module:: login_page

It contains Login Page functionalities.
"""

import sys
from os.path import abspath, dirname, join
from product_lib.aspire_app import gui_constants as const
from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By

utility_obj = Utility()

class LoginPage(object):
    '''
    Class contains Login Page functionalities
    '''

    '''  '''
    def login_to_app(self, driver, user, password):
        '''
        Login to application using entered credentials.

        :param driver: webDriver reference variable
        :param user: username to login the application
        :param password: password
        :return:
        '''

        # Navigate to Login Page
        driver.get(const.web_url)

        # Enter User name and password.
        utility_obj.enter_text(driver, By.CSS_SELECTOR, const.username_css, user)
        utility_obj.enter_text(driver, By.CSS_SELECTOR, const.password_css, password)

        # Click on Login button.
        utility_obj.click(driver, By.CSS_SELECTOR, const.login_btn_css)