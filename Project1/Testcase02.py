from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from webdriver_manager.chrome import ChromeDriverManager


def test_successful_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_invalid_username():
        driver = webdriver.Chrome()
        driver.get("http://your-orangehrm-url")  # Replace with your OrangeHRM URL


        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        username_field.send_keys("InvalidUser")


        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys("admin123")


        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()


        error_message = driver.find_element(By.ID, "spanMessage").text  # Adjust the ID as needed
        assert "Invalid credentials" in error_message  # Adjust based on actual error message

        driver.quit()

    test_invalid_username()