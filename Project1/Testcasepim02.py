from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager


def test_edit_employee():

    driver = webdriver.Chrome()

    try:

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


        edit_button = driver.find_element(By.XPATH,
                                          "//a[text()='John Doe']")  # Adjust the XPath based on actual employee link
        edit_button.click()


        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='btnSave']")))  # Adjust if needed
        edit_button.click()


        middle_name_field = driver.find_element(By.XPATH, "//input[@id='middleName']")
        middle_name_field.clear()
        middle_name_field.send_keys("UpdatedMiddleName")  # Replace with new test data


        save_button = driver.find_element(By.XPATH, "//input[@id='btnSave']")
        save_button.click()


        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']"))
        ).text

        assert "Successfully Updated" in success_message  # Adjust based on the actual success message

        print(f"Success message for editing employee: {success_message}")

    finally:

        driver.quit()



test_edit_employee()
