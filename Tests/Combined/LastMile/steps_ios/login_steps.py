import os
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from behave import *
from Tests.Combined.LastMile.steps_ios.base_steps import BaseFixture

@given('I login as a driver with username "{username}" and password "{password}"')
def login_as_mykyta(context, username, password):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Sign in"]').click()

    # Enter email
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@value="Email address"]').send_keys(username)

    # Enter password
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeSecureTextField[@value="Password"]').send_keys(password)

    # Click Log In
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Log in"]').click()
