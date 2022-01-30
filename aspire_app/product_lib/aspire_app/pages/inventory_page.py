#!/usr/bin/python
"""
.. module:: inventory_page

It contains Inventory Page functionalities.
"""

import sys
from os.path import abspath, dirname, join
from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By
from product_lib.aspire_app import gui_constants as const

utility_obj = Utility()


class InventoryPage(object):
    '''
    Class contains Inventory Page functionalities
    '''

    def go_to_inventory_page(self, driver):
        '''
        Navigate to Inventory Page.
        :param driver: webDriver reference variable.
        '''

        # Click on Inventory Element.
        utility_obj.click(driver, By.XPATH, const.inventory_xpath)