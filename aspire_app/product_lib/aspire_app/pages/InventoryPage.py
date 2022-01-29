from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By
from product_lib.aspire_app import gui_constants as const

utility_obj = Utility()

class InventoryPage(object):

    def go_to_inventory_page(self, driver):
        utility_obj.click(driver, By.XPATH, const.inventory_xpath)