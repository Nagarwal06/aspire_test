#!/usr/bin/python
"""
.. module:: manufacturing_page

It contains Manufacture Page functionalities.
"""

from product_lib.aspire_app import gui_constants as const
from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

utility_obj = Utility()


class ManufacturingPage(object):
    '''
    Class contains Manufacturing Page related functionalities.
    '''

    def go_to_application_page(self, driver):
        '''
        Navigate to Application page
        :param driver: webDriver reference variable
        :return: 
        '''

        # Click on Application Icon
        utility_obj.click(driver, By.CSS_SELECTOR, const.application_icon_css)


    def create_order(self, driver, product_name, order_qty):
        '''
        Creates Order for the product.
        Pre-Requisite: Product with passed product name should exist in system.

        :param driver: webDriver reference variable
        :param product_name: Name of the product for which order is to be created.
        :param order_qty: Quantity of the Product to be ordered.
        :return:
        '''

        # Click on Manufacturing icon on home page
        utility_obj.click(driver, By.XPATH, const.manufacturing_xpath)

        # Click on Create Order button on Manufacturing Page
        utility_obj.click(driver, By.XPATH, const.create_btn_xpath)

        # Enter Product Name
        utility_obj.enter_text(driver, By.XPATH, const.product_name_dropdown_xpath, product_name)

        # Click on suggested product
        utility_obj.click(driver, By.XPATH, const.suggestion_item % product_name)

        # Click on add a new line button in product section
        utility_obj.click(driver, By.XPATH, const.add_component_btn_xpath)

        # Count existing Suggestion dropdown active
        current_suggestion = driver.find_elements(By.XPATH, const.suggestion_dropdown)

        # Enter product name
        row_elements = utility_obj.wait_and_find_elements(driver, By.XPATH, const.row_component)
        row_elements[0].find_element(By.XPATH, const.product_xpath).send_keys(product_name)

        # Wait until Current product drop-down becomes active i.e when suggestion > old suggestions.
        while 1 == 1 :
            if len(driver.find_elements(By.XPATH, const.suggestion_dropdown)) > len(current_suggestion):
                break

        # Find Search Suggestion item list
        prod_ele_list = driver.find_elements(By.XPATH, const.suggestion_item % product_name)

        # Click on the second half of the product suggestions.
        prod_ele_list[int(len(prod_ele_list)/2)].click()

        # Clear the existing quantity value
        component_quality = driver.find_element(By.XPATH, const.quantity_xpath)
        for i in range(len(component_quality.get_attribute('value'))):
            component_quality.send_keys(Keys.BACK_SPACE)

        # Enter any random quantity for the product.
        component_quality.send_keys(order_qty)

        # Click on Confirm button
        utility_obj.click(driver, By.XPATH, const.confirm_btn_xpath)


    def mark_order_as_done(self, driver):
        '''
        Mark Order as done.
        Pre-Requisite: User should be on page for which order is to be marked as Done.

        :param driver: webDriver reference variable
        :return:
        '''

        # Click on Mark as Done button
        utility_obj.click(driver, By.XPATH, const.mark_as_done_btn_xpath)

        # Click on Apply button in dialog box.
        utility_obj.click(driver, By.XPATH, const.apply_btn_xpath)

        # Click on Dialog box to be invisible.
        utility_obj.wait_for_element_invisibility(driver, By.XPATH, const.modal_dialog_xpath)

        # Fetch Text From Current Status
        driver.refresh()
        return utility_obj.find_element_text(driver, By.XPATH, const.current_status_xpath)


    def verify_order(self, driver, exp_name, exp_qunatity, exp_consumed_quantity):
        '''
        Verify Order Details i.e. Product Name, Quantity

        :param driver: webDriver reference variable
        :param exp_name: expected product name
        :param exp_qunatity: expected quantity
        :param exp_consumed_quantity: expected consumed quantity
        :return: Boolen True or False.
        '''

        driver.refresh()

        product_name = utility_obj.find_element_text(driver, By.XPATH, const.verify_product_name_xpath)
        product_to_consume = utility_obj.find_element_text(driver, By.XPATH, const.verify_product_to_consume_xpath)
        product_consumed = utility_obj.find_element_text(driver, By.XPATH, const.verify_product_consumed_xpath)

        if exp_name == product_name and str(exp_consumed_quantity) + ".00" == product_consumed and str(exp_qunatity) + ".00" == product_to_consume:
            return True
        else:
            return False