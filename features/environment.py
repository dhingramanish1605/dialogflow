from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import configReader as cr

print(cr.readConfig("URLs", "dialog_flow"))

def before_feature(context,driver):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    context.driver.get("https://dialogflow.cloud.google.com/#/getStarted")
    context.driver.maximize_window()
    context.driver.implicitly_wait(30)
    context.driver.find_element(by=By.XPATH, value=cr.readConfig("locators", "sign_in_button")).click()
    windows = context.driver.window_handles
    for window in windows:
        context.driver.switch_to.window(window)

    context.driver.find_element(by=By.ID,value=("identifierId")).send_keys(
        cr.readConfig("credentials", "username"), Keys.RETURN)
    context.driver.find_element(by=By.XPATH,value=(cr.readConfig("locators", "password_input"))).send_keys(
        cr.readConfig("credentials", "password"), Keys.RETURN)
    time.sleep(50)
    windows = context.driver.window_handles
    for window in windows:
        context.driver.switch_to.window(window)