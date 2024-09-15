from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from webdriver_manager.chrome import ChromeDriverManager


def test_successful_login():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    username_field = driver.find_element(By.XPATH, "//input[@name='username']")  # Adjust the ID as needed
    username_field.send_keys("Admin")


    password_field = driver.find_element(By.XPATH, "//input[@name='password']")  # Adjust the ID as needed
    password_field.send_keys("admin123")


    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")  # Adjust the ID as needed
    login_button.click()

    # Verify successful login
    assert "Dashboard" in driver.title  # Adjust based on your actual dashboard title

    driver.quit()


test_successful_login()
