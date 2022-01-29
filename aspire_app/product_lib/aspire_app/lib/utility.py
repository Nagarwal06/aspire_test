from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from product_lib.aspire_app import gui_constants as const

class Utility():

    def wait_and_find_element(self, driver, selectorName, selectorVal):
        WebDriverWait(driver, const.refresh_tout).until(EC.visibility_of_element_located((selectorName, selectorVal)))
        return driver.find_element(selectorName, selectorVal)

    def wait_and_find_elements(self, driver, selectorName, selectorVal):
        WebDriverWait(driver, const.refresh_tout).until(EC.visibility_of_all_elements_located((selectorName, selectorVal)))
        return driver.find_elements(selectorName, selectorVal)

    def wait_for_element_invisibility(self, driver, selectorName, selectorVal):
        WebDriverWait(driver, const.refresh_tout).until(EC.invisibility_of_element_located((selectorName, selectorVal)))

    def click(self, driver, selectorName, selectorVal):
        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        element.click()

    def enter_text(self, driver, selectorName, selectorVal, text):
        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        element.send_keys(text)


    def find_element_text(self, driver, selectorName, selectorVal):
        element = self.wait_and_find_element(driver, selectorName, selectorVal)
        return element.text