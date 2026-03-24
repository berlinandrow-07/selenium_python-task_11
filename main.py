import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def guvi_login():
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome()
        driver.get("https://www.guvi.in/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"(//button[@id='login-btn'])[1]").click()
        time.sleep(2)
        return driver
def user_input(driver):
        email=driver.find_element(By.XPATH,"//input[@type='email']")
        password=driver.find_element(By.XPATH,"//input[@type='password']")
        submit=driver.find_element(By.XPATH,"(//a[@id='login-btn'])[1]")
        return email,password,submit
def login_credential(email,password,username,passwords):
    email.send_keys(username)
    password.send_keys(passwords)
# AUTOMATION TESTING
driver=guvi_login()
email, password, submit = user_input(driver)
login_credential(email, password,"valid username","valid password")
submit.click()
time.sleep(2)
driver.quit()

# POSITIVE TSET CASES
def test_valid_login_url():
  driver=guvi_login()
  assert "https://www.guvi.in/sign-in/" in driver.current_url
  driver.quit()

def test_valid_user_field():
    driver = guvi_login()
    email,password,submit=user_input(driver)
    assert email.is_enabled()
    assert email.is_displayed()
    assert password.is_enabled()
    assert password.is_displayed()
    driver.quit()

def test_valid_submit():
    driver = guvi_login()
    email, password, submit = user_input(driver)
    login_credential(email, password,"valid username","valid password")
    submit.click()
    time.sleep(2)
    assert "https://www.guvi.in/" in driver.current_url
    driver.quit()

# NEGATIVE TSET CASES
def test_invalid_login_url():
  driver=guvi_login()
  assert "https://www.guvi.in/sign-ins/" in driver.current_url
  driver.quit()

def test_invalid_user_field():
    driver = guvi_login()
    email,password,submit=user_input(driver)
    assert email.is_enabled()==False
    assert email.is_displayed()==False
    assert password.is_enabled()==False
    assert password.is_displayed()==False
    driver.quit()

def test_invalid_submit():
    driver = guvi_login()
    email, password, submit = user_input(driver)
    login_credential(email, password,"valid username","valid password")
    submit.click()
    time.sleep(2)
    assert "https://www.guvi.ins/" in driver.current_url
    driver.quit()

