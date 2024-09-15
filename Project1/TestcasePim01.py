from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#from webdriver_manager.chrome import ChromeDriverManager


def test_add_new_employee():
    driver = webdriver.Chrome()

    try:

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with your actual OrangeHRM URL

        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("Admin")  # Replace with your actual username

        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("admin123")  # Replace with your actual password

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='menu_pim_viewPimModule']"))).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='menu_pim_addEmployee']"))).click()

        first_name_field = driver.find_element(By.XPATH, "//input[@id='firstName']")
        first_name_field.send_keys("John")  # Replace with test data

        last_name_field = driver.find_element(By.XPATH, "//input[@id='lastName']")
        last_name_field.send_keys("Doe")  # Replace with test data

        save_button = driver.find_element(By.XPATH, "//input[@id='btnSave']")
        save_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='message success fadable']"))
        ).text

        assert "Successfully Added" in success_message  # Adjust based on the actual success message

        print(f"Success message: {success_message}")

    finally:

        driver.quit()


test_add_new_employee()
