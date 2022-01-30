#!/usr/bin/python
"""
.. module:: test_place_order_for_new_product

Login to web application and navigate to `Inventory` feature. then create a new product and update the quantity
Then create a manufacturing order and update the status of the order to Done.

"""
import sys
from os.path import abspath, dirname, join

sys.path.insert(0, abspath(join(dirname(__file__), '../../../')))

from product_lib.aspire_app.pages.get_webdriver import *
from product_lib.aspire_app.pages.login_page import LoginPage
from product_lib.aspire_app.pages.inventory_page import InventoryPage
from product_lib.aspire_app.pages.product_page import ProductPage
from product_lib.aspire_app.pages.manufacturing_page import ManufacturingPage
from product_lib.aspire_app import gui_constants as const
import pytest
import random
import datetime

'''Object variables'''
login_page_obj = LoginPage()
inventory_page_obj = InventoryPage()
product_page_obj = ProductPage()
manufacturing_page_obj = ManufacturingPage()


@pytest.fixture(scope="session")
def test_setup_application():
    '''
    Set-Up and Tear Down for the function.
    Note: Returned fixture value will be shared for all tests requesting it as scope is session.
    :return:
    '''

    global driver
    ''' Step 1 - Get the Driver '''
    driver = driver_chrome(const.browser_name)

    ''' Step 2 - Login page '''
    login_page_obj.login_to_app(driver, const.user, const.password)
    print("Login successfully to aspire app using {0} user and {1} password".format(const.user, const.password))

    yield
    ''' Tear Down - Closes Browser. '''
    driver.close()
    driver.quit()
    print("\n Test Completed")


def test_create_product(test_setup_application):
    '''
    Test creates product in the application.
    :param test_setup_application: Test SetUp Fixture.
    '''

    '''Step 1 - Navigate to `Inventory` feature.'''
    inventory_page_obj.go_to_inventory_page(driver)

    '''Step 2 - From the top-menu bar, select `Products -> Products` item'''
    product_page_obj.select_product_menu(driver)

    '''Step 3 - Create a new product'''
    global product_name
    product_name = const.product_name + "_" + str( int(round((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds())))
    product_page_obj.create_a_product(driver, product_name)
    print("New product {0} is created  ".format(product_name))

    '''Step 4 - Update Product Quantity greater than 10 '''
    update_quantity = random.randint(11, 100)
    product_page_obj.update_product_quantity(driver, update_quantity)


def test_create_new_product_and_manufacturing_order():
    '''
    Create Order for newly created Product and update status to Done
    '''

    '''Step 1 - From top-left page, click on `Application` icon'''
    manufacturing_page_obj.go_to_application_page(driver)

    ''' Step 2 - Navigate to `Manufacturing` feature and create new Manufacturing Order.'''
    global order_qty
    order_qty=random.randint(2, 10)
    manufacturing_page_obj.create_order(driver, product_name, order_qty)


def test_update_order_status_and_verify():
    '''
    Update new order status to Done and verify order attributes.
    '''

    ''' Step 1 - Update the status of new Order to “Done” '''
    status = manufacturing_page_obj.mark_order_as_done(driver)
    assert status == "DONE"
    print("New manufacturing Order is updated to status Done")

    ''' Step 2 - Verify Order Details '''
    order_verification_status = manufacturing_page_obj.verify_order(driver, product_name, order_qty, order_qty)
    assert order_verification_status == True
    print("Verification is completed")
