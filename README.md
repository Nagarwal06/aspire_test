# aspire_test
**Pre-Requisites:**
1. Python 3
2. Selenium 
3. Chrome WebDriver
4. PyTest

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
  
** Project Structure:**  
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
*	Go to testcases/aspire_app/test directory
*	Open cmd as an administrator
*	Change the directory to project path i.e, aspire_app. -> cd aspire_app.
*	Run the command **"pytest -v -s testcases\aspire_app\test\test_place_order_for_new_product.py"**
*	This will execute all the tests mentioned in "test_place_order_for_new_product.py" file under folder testcases/aspire_app/test/
