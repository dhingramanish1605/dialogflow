from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import time
import configReader as cr

from selenium.webdriver.support.wait import WebDriverWait

@given(u'Navigate to Create a intent')
def step_impl(context):
    context.driver.find_element(by=By.ID, value=cr.readConfig("locators", "create_intent")).click()


@when(u'Enter details "{intent_name}"')
def step_impl(context,intent_name):
    context.driver.find_element(by=By.XPATH,value=cr.readConfig("locators","intent_name_field")).send_keys(intent_name)
    context.driver.find_element_by_xpath(cr.readConfig("locators","save_button")).click()
    WebDriverWait(context.driver,20).until(
        ec.presence_of_element_located((By.XPATH,cr.readConfig("locators","toast_message"))))

@then(u'Validate message "{message}"')
def step_impl(context,message):
    actual_message = context.driver.find_element_by_xpath(cr.readConfig("locators","toast_message")).text
    context.driver.find_element_by_xpath(cr.readConfig("locators","toast_message_button")).click()
    if actual_message in message:
        assert True,"Pass, Expected:"+message+" Actual Message: "+actual_message
    else:
        assert False,"Failed, Expected:"+message+" Actual Message: "+actual_message
    time.sleep(5)