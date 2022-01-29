from product_lib.aspire_app.pages.getwebdriver import *
from product_lib.aspire_app.pages.LoginPage import LoginPage
from product_lib.aspire_app.pages.InventoryPage import InventoryPage
from product_lib.aspire_app.pages.ProductPage import ProductPage
from product_lib.aspire_app.pages.ManufacturingPage import ManufacturingPage
from product_lib.aspire_app import gui_constants as const
import random
import datetime

login_page_obj = LoginPage()
inventory_page_obj = InventoryPage()
product_page_obj = ProductPage()
manufacturing_page_obj = ManufacturingPage()

''' Step 1 - Get the Driver '''
driver = driver_chrome("chrome")

''' Step 2 - Login page '''
login_page_obj.login_to_app(driver, const.user, const.password)

''' Step 3 - Navigate to `Inventory` feature'''
inventory_page_obj.go_to_inventory_page(driver)

'''Step 4 - From the top-menu bar, select `Products -> Products` item'''
product_page_obj.select_product_menu(driver)

'''Step 5 - Create a new product'''
product_name = const.product_name + "_" + str(int(round((datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds())))
product_page_obj.create_a_product(driver, product_name)

'''Step 6 - Update Product Quantity'''
update_quantity = random.randint(11, 100)
product_page_obj.update_product_quantity(driver, update_quantity)

'''Step 7 - From top-left page, click on `Application` icon'''
manufacturing_page_obj.go_to_application_page(driver)

'''Step 8 - Navigate to `Manufacturing` feature, then create a new Manufacturing Order item'''
order_qty=random.randint(2, 10)
manufacturing_page_obj.create_order(driver, product_name, order_qty)

''' Step 9. Update the status of new Orders to “Done” '''
manufacturing_page_obj.mark_order_as_done(driver)

''' Step 10. Verify Order Details '''
manufacturing_page_obj.verify_order(driver, product_name, order_qty, order_qty)


