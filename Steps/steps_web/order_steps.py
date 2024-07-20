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
from Steps.steps_android.order_steps import unique_number
from Steps.steps_web.base_steps import BaseFixture
base_fixture_attr = BaseFixture()

now = datetime.now().day

counter_file = '/Users/kolokob/PycharmProjects/Automation/Steps/steps_android/counter.txt'


@then('I wait for "{seconds}" seconds on web')
def step_impl(context, seconds):
    time.sleep(int(seconds))


@then('I click on "Place an order" on web')
def step_impl(context):
    for i in range(10):
        try:
            context.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Place an order')]"))).click()
            break
        except:
            time.sleep(1)

@then('I add "{pick_up_num}" pick-up\'s addresses and "{drop_off_num}" drop-off addresses on web')
def step_login(context, pick_up_num, drop_off_num):
    import random
    import string
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import StaleElementReferenceException
    from appium.webdriver.common.appiumby import AppiumBy

    pick_up_num = int(pick_up_num)
    drop_off_num = int(drop_off_num)

    alphabet = list(string.ascii_lowercase)
    vowels = 'aeiou'
    consonants = ''.join([c for c in alphabet if c not in vowels])
    combinations = [c + v for c in consonants for v in vowels]
    addresses = alphabet + combinations
    details = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 8))) for _ in range(40)]
    context.addresses_amount = max(pick_up_num, drop_off_num)
    counter = 1
    time.sleep(4)
    for i in range(max(pick_up_num, drop_off_num)):
        if i < pick_up_num:
            if i > 1:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'pick-up')]"))).click()
                time.sleep(1)
            time.sleep(1)
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//input[@placeholder='Enter address here'])[{counter}]"))).send_keys(addresses[i])
            time.sleep(1)
            context.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='pac-item-query'])[1]"))).click()
            time.sleep(1)
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//input[contains(@class, 'col-3') or contains(@class, 'or-input-suit') or contains(@class, 'fd-ol') or contains(@class, 'suite_number_pickup')])[{counter}]"))).send_keys(details[i])
            time.sleep(1)
            counter += 1
        if i < drop_off_num:
            if i > 1:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'drop-off')]"))).click()
                time.sleep(1)
            time.sleep(1)
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//input[@placeholder='Enter address here'])[{counter}]"))).send_keys(addresses[i+1])
            time.sleep(1)
            context.wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='pac-item-query'])[1]"))).click()
            time.sleep(1)
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//input[contains(@class, 'col-3') or contains(@class, 'or-input-suit') or contains(@class, 'fd-ol') or contains(@class, 'suite_number_pickup')])[{counter}]"))).send_keys(details[i+1])
            time.sleep(1)
            counter += 1

@then('I click Continue on web')
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Continue')]"))).click()

@then('I add declared value "{value}" on web')
def step_impl(context, value):
    for i in range(10):
        try:
            context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='number']"))).send_keys(value)
            break
        except:
            time.sleep(1)

@then('I add parcel size as "{parcel_size}" and "{vehicle_type}" on web')
def step_impl(context, parcel_size, vehicle_type):
    context.parsel_size = parcel_size
    if parcel_size == 'small':
        pass
    elif parcel_size == 'medium':
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Medium (26-50kg)')]"))).click()
    elif parcel_size == 'large':
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Large (51-70kg)')]"))).click()
        base_fixture_attr.choose_vehicle_type(context, vehicle_type)
    elif parcel_size == 'heavy_load':
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Heavy Load (71+ kg)')]"))).click()
        base_fixture_attr.choose_vehicle_type(context, vehicle_type)
    elif parcel_size == 'custom size':
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Custom size')]"))).click()
        base_fixture_attr.put_info_for_custom_size(context, [2, 2, 2, 2])
        base_fixture_attr.choose_vehicle_type(context, vehicle_type)


@then('I add pick-up time as "{pick_up_time}" with days "{days_or_date}" and time "{time}" for each and start date as "{start_date}" on web')
def step_login(context, pick_up_time, days_or_date, time, start_date):
    # 29/06/2024
    context.pick_up_time = pick_up_time
    days_or_date = days_or_date.split('/')
    if pick_up_time == 'urgent':
        pass

    elif pick_up_time == 'scheduled':
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Schedule a pick-up')]"))).click()
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Select a pick-up date and time')]"))).click()
        while True:
            if base_fixture_attr.check_year(context, days_or_date[2]):
                break
            else:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-icon-double-right']"))).click()

        while True:
            if base_fixture_attr.check_month(context, days_or_date[1]):
                break
            else:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-icon-right']"))).click()
        if not base_fixture_attr.check_day(context, days_or_date[0]):
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{days_or_date[0].removeprefix('0')}')]"))).click()

        # current_pm_am = context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//li[@class='mx-time-item active'])[2]"))).text
        # if current_pm_am.lower() not in ['am', 'pm']:
        #     current_pm_am = context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//li[@class='mx-time-item active'])[3]"))).text

        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{time[:2]}')]"))).click()
        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//div[@class='mx-scrollbar mx-time-column'])[2]//li[contains(text(),'{round(int(time[3:5])/10) * 10}')]"))).click()
        # if current_pm_am != time[-2:]:
        #     context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{time[-2:]}')]"))).click()

    elif pick_up_time == 'repeated':
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Repeated weekly')]"))).click()
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Repeated start date')]"))).click()
        while True:
            if base_fixture_attr.check_year(context, start_date.split('/')[2]):
                break
            else:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-icon-double-right']"))).click()

        while True:
            if base_fixture_attr.check_month(context, start_date.split('/')[1]):
                break
            else:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-icon-right']"))).click()

        if not base_fixture_attr.check_day(context, start_date.split('/')[0]):
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{start_date.split('/')[0].removeprefix('0')}')]"))).click()

        base_fixture_attr.select_days_for_repeated_order(context, days_or_date, time)


@then('I add promo code as "{promo_code}" on web')
def step_login(context, promo_code):
    context.promo_code = promo_code
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter promo code']"))).send_keys(promo_code)


@then('I add extra services "{extra_service}" and service "{details}" on web')
def step_login(context, extra_service, details):
    if extra_service is not None or extra_service != 'None':
        extra_service = extra_service.split(', ')
        service = details.split(', ')
        min_length = min(len(extra_service), len(service))
        extra_services = {extra_service[i]: ['Be careful', service[i]] for i in range(min_length)}
        counter = 0
        context.extra_services = extra_services
        if type(extra_services) == dict:
            context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Select Extra Service')]"))).click()
            for i in list(extra_services.keys()):
                context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//h6[contains(text(), '{i}')]/../..//i"))).click()
                context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='form-control custom-control']//option[contains(text(), '{list(extra_services.values())[counter][1]}')]"))).click()
                context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//textarea[@placeholder='Note']"))).send_keys(list(extra_services.values())[counter][0])
                context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='pop-btn pop-btn-primary']"))).click()

        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Save')]"))).click()


@then('I click on "Calculate Price" on web')
def step_price(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Calculate Price')]"))).click()

@then('I add tips as "{tips}" on web')
def step_login(context, tips):
    context.tips = tips
    if tips == 'None' or tips is None:
        pass
    elif tips in [10, 15, 20, 25]:
        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='v6-pack-tips']//span[contains(text(), '{tips}')]"))).click()
    else:
        context.wait.until(EC.element_to_be_clickable((By.ID, 'pc_tip'))).send_keys(tips)
        context.order_price = context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//span[@class='total-price']"))).text

@then('I add name of the order as "{name}" on web')
def step_login(context, name):

    with open(counter_file, 'r') as file:
        unique_numbers = int(file.read())

    unique_numbers += 1

    with open(counter_file, 'w') as file:
        file.write(str(unique_numbers))

    context.order_name = f"AUTO TEST №{unique_numbers}; Name: {name}"
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='send_name']"))).send_keys(f"AUTO TEST №{unique_numbers}; Name: {name}")


@then('I add signature "{decision}" on web')
def step_login(context, decision):
    if decision == "Yes":
        context.signature = True
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='v7-slider v7-round']"))).click()
    elif decision == "No":
        context.signature = False

@then('I add receiver\'s and sender\'s all info in all required fields on web')
def step_login(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter Sender First & Last name']"))).send_keys("John Marston")
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter phone number']"))).send_keys("5104020440")
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter name']"))).send_keys("Dart Wader")
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='xxx-xxx-xxxx']"))).send_keys("5104020440")
    time.sleep(1)


@then('I select saved credit card on web')
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Existing credit card')]"))).click()


@then('I add credit card info as "{credit_card_number}" for credit card number, "{expiration_date}" for expiration date and "{cvv}" for CVV on web')
def step_login(context, credit_card_number, expiration_date, cvv):
    context.credit_card_info = [credit_card_number, expiration_date, cvv]
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='__senpex']/div[@id='__layout']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/iframe[1]"))).send_keys(credit_card_number)
    time.sleep(0.5)
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='__senpex']/div[@id='__layout']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/iframe[1]"))).send_keys(expiration_date)
    time.sleep(0.5)
    context.wait.until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='__senpex']/div[@id='__layout']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/iframe[1]"))).send_keys(cvv)


@then('I click pay for the order on web')
def step_pay(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), 'Pay now {context.order_price} CAD')]"))).click()


@then('I click on "Schedule a delivery" on web')
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Schedule a delivery')]"))).click()


@given('I select country as "{country}" on web')
def step_impl(context, country):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[@class='user-name user-location']"))).click()
    if country == "US":
        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='user-dropdown-menu']/ul/li[1]"))).click()
    elif country == "CA":
        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@class='user-dropdown-menu']/ul/li[2]"))).click()



@then("I click Sign In")
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//a[contains(text(), 'Sign in')])[2]"))).click()

