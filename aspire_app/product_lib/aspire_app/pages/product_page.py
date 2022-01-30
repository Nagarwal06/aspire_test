#!/usr/bin/python
"""
.. module:: product_page

It contains Product Page functionalities.
"""
from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from product_lib.aspire_app import gui_constants as const
import random

utility_obj = Utility()

class ProductPage(object):
    '''
    Class contains Product Page functionalities.
    '''

    def select_product_menu(self, driver):
        '''
        Navigate to Product page from top menu.
        :param driver: webDriver reference variable
        :return:
        '''
        # Wait for the Menu bar to display
        utility_obj.wait_and_find_element(driver, By.CSS_SELECTOR, const.top_meu_bar_css)

        # Click on the Product from Menu bar
        utility_obj.click(driver, By.XPATH, const.products_menu_xpath)

        # Click on the Products link from Product drop-down
        utility_obj.click(driver, By.XPATH, const.products_item_xpath)


    def create_a_product(self, driver, product_name):
        '''
        Create new product.
        :param driver: webDriver reference variable
        :param product_name: Name of the product to be created
        :return:
        '''

        # Click on the create button on product page
        utility_obj.click(driver, By.XPATH, const.create_btn_xpath)

        # Enter the product name
        utility_obj.enter_text(driver, By.XPATH, const.product_name_xpath, product_name)


    def update_product_quantity(self, driver, quantity):
        '''
        Update Quantity of created product.
        Pre-Requisite: User should be on Product page.

        :param driver: webDriver reference variable
        :param quantity: Quantity to be updated for the product.
        :return:
        '''

        # Click on Update Quantity Button
        utility_obj.click(driver, By.XPATH, const.update_btn_xpath)

        # Click on Create Button in qunatity page
        utility_obj.click(driver, By.XPATH, const.create_btn_xpath)

        # Select the row
        utility_obj.click(driver, By.XPATH, const.row_location)

        # Select Available location from drop-down
        items = utility_obj.wait_and_find_elements(driver, By.XPATH, const.available_location)
        random.choice(items).click()

        # Select quantity column
        columns_ele = utility_obj.wait_and_find_element(driver, By.XPATH, const.item_quality)

        # Remove initial default value i.e. 0.00 from input box.
        for i in range(len(columns_ele.get_attribute('value'))):
            columns_ele.send_keys(Keys.BACK_SPACE)
        columns_ele.send_keys(quantity)

        # Click on Save Button
        utility_obj.click(driver, By.XPATH, const.save_btn_xpath)