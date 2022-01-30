# aspire_test
**Pre-Requisites:**
1. Python 3
2. Selenium 
3. Chrome WebDriver

**Python Packages:**
Make sure to install these packages before use case execution.
Selenium
Pytest

Main goal of Aspire_test is to simplify the task of managing & running multiple tests with different combination of runtime parameters.

Architecture
•	POM (Page Object Model)
        o On the top you have the test cases, which call the page specific object.
        o Page specific objects → are the libraries which are calling, for example, the LoginPage of Aspire_app

•	Product lib:
        o	covers the Libraries over the product features and business logic around the verification and validation

•	testcases:
        o	all test suite and test case


**Step-by-step guide**
Following are the steps
•	Make sure all the necessary packages are installed
•	Go to testcases/aspire_app/test directory
•	Open cmd as an administrator
•	Run the command python Place_Order_For_New_Product_Test.py
•	This will execute all the tests mentioned in .py file under folder testcases/aspire_app/test/





