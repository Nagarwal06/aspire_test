#!/usr/bin/python3

from selenium import webdriver

def driver_chrome(driver_name):
    if driver_name.lower() == "chrome":
        driver = webdriver.Chrome()
    return driver
