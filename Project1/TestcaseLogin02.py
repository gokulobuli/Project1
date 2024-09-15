from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


#from webdriver_manager.chrome import ChromeDriverManager


def test_invalid_login():
    # Set up the WebDriver (Chrome in this case)
    driver = webdriver.Chrome()

    try:

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # Replace with your actual OrangeHRM URL

        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("Admin")

        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("Invalid password")

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        error_message = driver.find_element(By.XPATH, "//span[@id='spanMessage']").text
        assert "Invalid credentials" in error_message

        print(f"Error message for invalid login: {error_message}")

    finally:

        driver.quit()


test_invalid_login()
