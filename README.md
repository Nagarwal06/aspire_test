# aspire_test
**Pre-Requisites:**
1. Download Python 3 (https://www.python.org/downloads/release/python-368/),
2. Install Python 3 from MSI in windows.
3. Download Chrome WebDriver (https://chromedriver.storage.googleapis.com/index.html?path=97.0.4692.36/)
4. Move Chrome Driver in directory (C:\Program Files\Python36).
5. Open command prompt/terminal in Administrator mode.
6. Install Selenium using command -> pip insatll selenium
7. Install Pytest using command -> pip insatll pytest

**Python Packages:**
Make sure to install these packages before use case execution.


**Objective:**
Main goal of Aspire_test is to create test automation suite for application to mitigate human error and dependency. 

**Architecture**
* product lib:
    * It consists different page specific classes which consists product features and business logic.

* POM (Page Object Model)
    * Each functionality has specific test cases, which uses indiviual page specific object.
    * Page specific objects → are the libraries having specific page functionalitites.

* testcases:
    * All test suite and test cases to be executed for different features.
  
**Project Structure:** 
   * aspire_app
       * product_lib
           * aspire_app
               * lib
                   *  utility.py
               *  pages
                  *  get_webdriver.py
                  *  invetory_page.py
                  *  login_page.py
                  *  manufacturing_page.py
                  *  product_page.py
               * gui_constants.py
      * test_cases
         *  aspire_app
            *  test
               *  test_place_order_for_new_product.py



**Step-by-step guide**
*	Make sure all necessary packages are installed.
*	Open cmd as in administrator mode.
*	Change the directory to project path i.e, aspire_app. -> **cd aspire_test\aspire_app**
*	Run the command **"pytest -v -s testcases\aspire_app\test\test_place_order_for_new_product.py"**
*	Wait for test to complete and see result in command prompt.
