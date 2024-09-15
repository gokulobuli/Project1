from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager
import time


def test_delete_employee():

    driver = webdriver.Chrome()

    try:
        # Open the OrangeHRM login page
        driver.get("http://your-orangehrm-url")  # Replace with your actual OrangeHRM URL


        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("Admin")  # Replace with your actual username

        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("admin123")  # Replace with your actual password

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()


        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='menu_pim_viewPimModule']"))).click()


        search_box = driver.find_element(By.XPATH, "//input[@id='empsearch_employee_name_empName']")
        search_box.send_keys("John Doe")  # Replace with the employee's name or other identifier

        search_button = driver.find_element(By.XPATH, "//input[@id='searchBtn']")
        search_button.click()


        employee_checkbox = driver.find_element(By.XPATH, "//input[@name='chkSelectRow[]']")  # Adjust if needed
        employee_checkbox.click()


        delete_button = driver.find_element(By.XPATH, "//input[@id='btnDelete']")
        delete_button.click()


        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='dialogDeleteBtn']")))
        confirm_button.click()


        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']"))
        ).text  # Adjust the XPath based on actual success message location

        assert "Successfully Deleted" in success_message  # Adjust based on the actual success message

        print(f"Success message for deleting employee: {success_message}")

    finally:

        driver.quit()



test_delete_employee()
