# file: Tests/Client/LastMile/Android/steps_android/login_steps.py

from behave import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from Tests.Combined.LastMile.steps_android.base_steps import BaseFixture
from Tests.Combined.LastMile.steps_android.order_steps import unique_number
base_fixture_attr = BaseFixture()

@given('I login as client with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtLogin').click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtEmail'))).send_keys(username)
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtPassword').send_keys(password)
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/btnSignIn').click()

@given('I login as new user with new credentials that were got from the email')
def step_login(context):
    context.new_password = base_fixture_attr.get_password_from_email()
    context.new_password = base_fixture_attr.get_password_from_email()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLogin'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtEmail'))).send_keys(f'automation.senpex+{unique_number}@outlook.com')
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtPassword').send_keys(context.new_password)
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/btnSignIn').click()