from product_lib.aspire_app import gui_constants as const
from product_lib.aspire_app.lib.utility import Utility
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

utility_obj = Utility()

class ManufacturingPage(object):

    def go_to_application_page(self, driver):
        # Click on Application Icon
        utility_obj.click(driver, By.CSS_SELECTOR, const.application_icon_css)

    def create_order(self, driver, product_name, order_qty):
        # Click on Manufacturing icon on home page
        utility_obj.click(driver, By.XPATH, const.manufacturing_xpath)

        # Click on Create Order button on Manufacturing Page
        utility_obj.click(driver, By.XPATH, const.create_button_xpath)

        # Enter Product Name
        utility_obj.enter_text(driver, By.XPATH, const.PRODUCT_NAME_DROPDOWN_XPATH, product_name)

        # Click on suggested product
        utility_obj.click(driver, By.XPATH, const.SUGGESTION_ITEM % product_name)

        # Click on add a new line button in product section
        utility_obj.click(driver, By.XPATH, const.ADD_COMPONENT_BTN_XPATH)

        # Count existing Suggestion dropdown active
        current_suggestion = driver.find_elements(By.XPATH, const.SUGGESTION_DROPDOWN)

        # Enter product name
        row_elements = utility_obj.wait_and_find_elements(driver, By.XPATH, const.COMPONENT_ROW)
        row_elements[0].find_element_by_xpath(const.product_xpath).send_keys(product_name)

        # Wait until Current product drop-down becomes active i.e when suggestion > old suggestions.
        while 1 == 1 :
            if len(driver.find_elements(By.XPATH, const.SUGGESTION_DROPDOWN)) > len(current_suggestion):
                break

        # Find Search Suggestion item list
        prod_ele_list = driver.find_elements(By.XPATH, const.SUGGESTION_ITEM % product_name)

        # Click on the second half of the product suggestions.
        prod_ele_list[int(len(prod_ele_list)/2)].click()

        # Clear the existing quantity value
        component_quality = driver.find_element_by_xpath(const.quantity_xpath)
        for i in range(len(component_quality.get_attribute('value'))):
            component_quality.send_keys(Keys.BACK_SPACE)

        # Enter any random quantity for the product.
        component_quality.send_keys(order_qty)

        # Click on Confirm button
        utility_obj.click(driver, By.XPATH, const.CONFIRM_BTN_XPATH)


    def mark_order_as_done(self, driver):

        # Click on Mark as Done button
        utility_obj.click(driver, By.XPATH, const.MARK_AS_DONE_BTN_XPATH)

        # Click on Apply button in dialog box.
        utility_obj.click(driver, By.XPATH, const.APPLY_BTN_XPATH)

        # Click on Dialog box to be invisible.
        utility_obj.wait_for_element_invisibility(driver, By.XPATH, const.MODAL_DIALOG_XPATH)

        # Fetch Text From Current Status
        return utility_obj.find_element_text(driver, By.XPATH, const.CURRENT_STATUS_XPATH)


    def verify_order(self, driver, exp_name, exp_qunatity, exp_consumed_quantity):

        product_name = utility_obj.find_element_text(driver, By.XPATH, const.VERIFY_PRODUCT_NAME_XPATH)
        product_to_consume = utility_obj.find_element_text(driver, By.XPATH, const.VERIFY_PRODUCT_TO_CONSUME_XPATH)
        product_consumed = utility_obj.find_element_text(driver, By.XPATH, const.VERIFY_PRODUCT_CONSUMED_XPATH)

        if exp_name == product_name and str(exp_consumed_quantity) + ".00" == product_consumed and str(exp_qunatity) + ".00" == product_to_consume:
            driver.quit()
            return True
        else:
            return False