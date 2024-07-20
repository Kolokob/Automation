import os
import time
from behave import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from Steps.steps_android.base_steps import Swiper
from Steps.steps_ios.base_steps import BaseFixture
base_fixture_attr = BaseFixture()

@given('I login with credentials "{email}" and "{password}"')
def step_impl(context, email, password):
    time.sleep(1)
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))).send_keys(email)
    context.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).send_keys(password)
    try:
        context.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))).click()
    except:
        context.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Close')]"))).click()
        context.wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))).send_keys(email)
        context.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@type='button']"))).click()