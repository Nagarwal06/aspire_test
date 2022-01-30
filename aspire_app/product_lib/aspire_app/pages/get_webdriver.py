#!/usr/bin/python
"""
.. module:: get_webdriver

This return same webdriver instance for all testcases run as testsuites

"""
import sys
from os.path import abspath, dirname, join
from selenium import webdriver

def driver_chrome(driver_name):
    '''
    Create Selenium driver object and returns it
    Args: driver_name: Name of webdriver.

    '''
    global driver
    if driver_name.lower() == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    else:
        return "Invalid selected browser."
    return driver
