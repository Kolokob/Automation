import os
import time

from appium.webdriver.common.touch_action import TouchAction
from behave import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from Steps.steps_android.base_steps import Swiper
from Steps.steps_ios.base_steps import BaseFixture
base_fixture_attr = BaseFixture()

now = datetime.now().day

counter_file = '/Users/kolokob/PycharmProjects/Automation/Steps/steps_android/counter.txt'

with open(counter_file, 'r') as file:
    unique_number = int(file.read())

unique_number += 1

with open(counter_file, 'w') as file:
    file.write(str(unique_number))

@given("I click on the latest available order ios")
def step_impl(context):
    context.driver.find_element(by=AppiumBy.XPATH, value=f"//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeOther").click()

@given('I search for the order ID "{order_id}" and click on it ios')
def step_impl(context, order_id):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@value="Search"]').send_keys(order_id)
    time.sleep(1)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeOther'))).click()


@then('I as driver ios app extract all data to json file ios')
def step_impl(context):
    import re

    extracted_data = {}
    vehicle_types = ['Car', 'Pickup Truck', 'SUV', '9ft Cargo Van', '9ft Ref Van', '10ft Box Truck', '15ft Box Truck', '17ft Box Truck']
    size_types = ['Small (1-25 Lbs)', 'Medium (26-50 Lbs)', 'Large (51-70 Lbs)', 'Heavy Load (71+ Lbs)']

    def is_address(text):
        address_pattern1 = r'^\d+\s[a-zA-Z0-9\s]+,?\s[a-zA-Z\s]+,?\s[A-Z]{2}\s\d{5,6}$'
        address_pattern2 = r'^[a-zA-Z\s]+,\s[A-Z]{2},\s[A-Z]{3}$'
        address_pattern3 = r'^\d+\s[a-zA-Z0-9\s]+,?\s[a-zA-Z\s]+$'
        address_pattern4 = r'^\d+\s[a-zA-Z0-9\s]+,\s[a-zA-Z\s]+,\s[A-Z]{2}\s\d{5,6},\s[A-Z]{3}$'

        return bool(re.match(address_pattern1, text) or re.match(address_pattern2, text) or re.match(address_pattern3, text) or re.match(address_pattern4, text))

    for i in range(1, 25):
        try:
            element_text = context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{i}]').text

            if '$' in element_text:
                if 'driver_salary' in extracted_data:
                    if not isinstance(extracted_data['driver_salary'], list):
                        extracted_data['driver_salary'] = [extracted_data['driver_salary']]
                    extracted_data['driver_salary'].append(element_text)
                else:
                    extracted_data['driver_salary'] = element_text
            elif re.search(r'\d{2}/\d{2}/\d{4} \d{2}:\d{2} (AM|PM)', element_text) or 'As soon as possible' in element_text:
                extracted_data['when'] = element_text
            elif element_text in vehicle_types:
                extracted_data['vehicle'] = element_text
            elif element_text in size_types:
                extracted_data['size'] = element_text
            elif 'miles' in element_text:
                extracted_data['distance'] = element_text
            elif 'Nationwide' in element_text or 'Last-mile delivery' in element_text:
                extracted_data['order_type'] = element_text
            elif '·' in element_text:
                extracted_data['time_and_miles'] = element_text
            elif 'Order name' in element_text:
                extracted_data['order_name'] = context.driver.find_element(by=AppiumBy.XPATH, value='(//XCUIElementTypeStaticText[@name])[4]').text

        except NoSuchElementException:
            continue

    extracted_data['order_id'] = context.driver.find_element(by=AppiumBy.XPATH, value='(//XCUIElementTypeStaticText[@name])[1]').text

    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Route"]').click()

    for i in range(1, 25):
        try:
            element_text = context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{i}]').text

            if re.search(r'\d+ routes', element_text):
                extracted_data['routes_amount'] = element_text
            elif '·' in element_text:
                extracted_data['time_and_miles'] = element_text
            elif is_address(element_text):
                if 'pick_up_address' not in extracted_data:
                    extracted_data['pick_up_address'] = element_text
                else:
                    extracted_data['drop_off_address'] = element_text

        except NoSuchElementException:
            continue
    try:
        extracted_data['apt_pick_up'] = context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[12]').text
        extracted_data['apt_drop_off'] = context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[17]').text
    except NoSuchElementException:
        pass

    if 'Nationwide' in extracted_data.get('order_type', '') and 'apt_drop_off' not in extracted_data:
        extracted_data['apt_drop_off'] = 'No drop-off apt since this is nationwide order'

    base_fixture_attr.extract_data_to_json_file(extracted_data['order_id'],
                                                extracted_data['order_name'],
                                                extracted_data['driver_salary'],
                                                extracted_data['when'],
                                                extracted_data['vehicle'],
                                                extracted_data['size'],
                                                extracted_data['distance'],
                                                extracted_data['order_type'],
                                                extracted_data['routes_amount'],
                                                extracted_data['time_and_miles'],
                                                extracted_data['apt_pick_up'],
                                                extracted_data['pick_up_address'],
                                                extracted_data['apt_drop_off'],
                                                extracted_data['drop_off_address'])


@given('I click on "Get a Quote" ios')
def step_login(context):
    counter = 0
    while counter < 5:
        try:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "Get a Quote" AND label == "Get a Quote" AND value == "Get a Quote"'))).click()
            break
        except:
            time.sleep(1)
            counter += 1



@then('I click on "{service}" service ios')
def step_login(context, service):
    counter = 0
    while counter < 5:
        try:
            if 'Last' in service:
                try:
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "HomeLastMileServiceBg"'))).click()
                except TimeoutException:
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Last-mile delivery"'))).click()
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "HomeLastMileServiceBg"'))).click()
            elif 'Moving' in service:
                try:
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "HomeMovingServiceBg"'))).click()
                except TimeoutException:
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Moving"'))).click()
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "HomeMovingServiceBg"'))).click()
            elif 'Nationwide' in service:
                try:
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "NationwideMovingServiceBg"'))).click()
                except TimeoutException:
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Nationwide"'))).click()
                    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "NationwideMovingServiceBg"'))).click()
            break
        except TimeoutException:
            counter += 1

@then('I add "{pick_up_num}" pick-up\'s addresses and "{drop_off_num}" drop-off addresses ios')
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
    for i in range(max(pick_up_num, drop_off_num)):
        if i < pick_up_num:
            # Adding pick-up
            if i > 0:
                context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "Add pick-up"'))).click()

            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "PickupYellowLoc"'))).send_keys(addresses[i] if context.country == 'US' else f'Surrey {counter}')

            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther'))).click()
            if i < 1:
                context.wait.until(EC.visibility_of_all_elements_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name.length > 0`][2]')))
            else:
                context.wait.until(EC.visibility_of_all_elements_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name.length > 0`][6]')))
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "Confirm pick-up address"'))).click()

            # Add location details
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'value == "-"'))).send_keys(details[i])

            # Click on 'Continue' button
            if counter >= 2:
                context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//XCUIElementTypeStaticText[@name="Continue"])[2]'))).click()
            else:
                context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Continue"]'))).click()

            counter += 1

        if i < drop_off_num:
            # Add drop-off
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "Add drop-off"'))).send_keys(addresses[i] if context.country == 'US' else f'Vancouver {counter}')
            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther'))).click()
            context.wait.until(EC.visibility_of_all_elements_located((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name.length > 0`][6]')))
            time.sleep(2)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "Confirm drop-Off address"'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'value == "-"'))).send_keys(details[i])

            # Click on 'Continue' button
            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Continue"]'))).click()

@then('I click on "Get a quote" ios')
def step_login(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Get a Quote"]'))).click()


@then('I click on button "Continue" ios')
def step_login(context):
    for i in range(1):
        try:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Continue"`]'))).click()
            break
        except:
            pass

        try:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "Continue" AND label == "Continue" AND type == "XCUIElementTypeButton"'))).click()
            break
        except:
            pass

        try:
            context.wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Continue"]'))).click()
            break
        except:
            pass

        try:
            context.driver.execute_script('mobile: tap', {'x': 198, 'y': 604})
        except:
            raise(Exception("Unable to click on element"))

@then('I click on "Confirm shipment details" ios')
def step_login(context):
    try:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Confirm shipment details"]'))).click()
    except:
        context.driver.swipe(201, 420, 1, 228, 151)
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Confirm shipment details"]'))).click()

@then('I click on "Calculate Price" ios')
def step_price(context):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Calculate Price"]').click()

@then('I add order name as "{name}" ios')
def step_name(context, name):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Name your order"]').send_keys(f"AUTO TEST {name} {context.test_id}")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()

@then('I swipe "{direction}" "{length}" ios')
def step_direction(context, direction, length):
    directions = {
        'down': 'scroll_down',
        'up': 'scroll_up',
        'right': 'scroll_right',
        'left': 'scroll_left'
    }
    context.swipe_attr = Swiper(context.driver)

    if direction in directions:
        getattr(context.swipe_attr, directions[direction])(length)
    else:
        raise ValueError(f"Invalid direction: {direction}. Must be one of {', '.join(directions.keys())}")

@then('I add sender\'s name ios')
def step_name(context):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]').send_keys(f"John {context.test_id}")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()


@then('I add sender\'s phone number ios')
def step_name(context):
    context.driver.find_element(by=AppiumBy.XPATH, value='(//XCUIElementTypeTextField[@value="(000) 000-0000"])[1]').send_keys("5104024004")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()

@then('I add receiver\'s name ios')
def step_name(context):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[5]').send_keys(f"Hannah {context.test_id}")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()

@then('I add receiver\'s phone number ios')
def step_name(context):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@value="(000) 000-0000"]').send_keys("5104020440")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()

@then('I click "Confirm order" ios')
def step_conferm(context):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Confirm order"]').click()

@then('I click add card info as "{card_number}", "{expiration_date}", "{cvv}" ios')
def step_card_info(context, card_number, expiration_date, cvv):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@name="card number"]').send_keys(f"{card_number} {expiration_date}")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@name="CVC"]').send_keys(f"{cvv}")
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()

@then('I fill all info for sender and receiver ios')
def step_sender(context):
    i = 2
    for k in range(1, context.addresses_amount+5):
        try:
            context.driver.find_element(by=AppiumBy.XPATH, value=f'//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[{i}]').send_keys("Debora")
            # context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()

            try:
                context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeTextField[@value="(000) 000-0000"])[{k}]').send_keys("5104029082")
            except:
                try:
                    context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeTextField[@value="(000) 000-0000"])[{k-1}]').send_keys("5104029082")
                except:
                    context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeTextField[@value="(000) 000-0000"])[{k+1}]').send_keys("5104029082")
            # finally:
                # context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()
        except:
            raise Exception(print("Unable to fill all info for sender and receiver"))

        i += 3
    try:
        context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeButton[@name="Done"]').click()
        context.driver.swipe(120, 100, 120, 622, 100)
        for i in range(10):
            try:
                context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeTextField[@value="(000) 000-0000"])[{i}]').send_keys("5104029082")
            except:
                continue
    except:
        raise Exception(print("Unable to fill all info for sender and receiver"))

    context.driver.swipe(120, 622, 120, 100, 100)
    context.driver.swipe(120, 622, 120, 100, 100)

@then('I click pay for the order ios')
def step_pay(context):
    context.driver.find_element(by=AppiumBy.XPATH, value="(//XCUIElementTypeStaticText[contains(@name, 'Pay') or contains(@label, 'Pay')])[2]").click()


@given('I create an instant last-mile order ios')
def step_instant_last_mile(context):
    context.swipe_attr = Swiper(context.driver)

    # Get a quote
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Get a Quote"]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeImage[@name="HomeLastMileServiceBg"]'))).click()

    # Pick up address
    context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, 'name == "PickupYellowLoc"'))).send_keys("Q")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeButton[1]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Confirm pick-up address"]'))).click()

    # Continue
    try:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Continue"]'))).click()
    except TimeoutException:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Continue"])[2]'))).click()


    # Drop-off address
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Add drop-off"]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Pick-up address"]'))).send_keys("W")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeButton[1]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Confirm drop-Off address"]'))).click()

    # Continue
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="Continue"])[2]'))).click()

    # Continue
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Continue"]'))).click()

    # Shipment detail continue
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Confirm shipment details"]'))).click()

    # Calculate price
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Calculate Price"]'))).click()

    # Continue
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Continue"]'))).click()

    # Order name
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Name your order"]'))).send_keys(f"Test {context.test_id}")
    context.save_test_name(context.test_id)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()

    context.swipe_attr.scroll_down('long')

    # Sender's name
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]'))).send_keys(f"John {context.test_id}")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()

    # Sender's phone
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//XCUIElementTypeTextField[@value="(000) 000-0000"])[1]'))).send_keys("5104024004")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()

    context.swipe_attr.scroll_down('long')

    # Receiver's name
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[5]'))).send_keys(f"Hannah {context.test_id}")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()

    # Receiver's phone
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="(000) 000-0000"]'))).send_keys("5104020440")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()

    # Continue
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Continue"]'))).click()

    # Confirm order
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Confirm order"]'))).click()

    # Enter card number and card date
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="card number"]'))).send_keys("4242424242424242 0429")

    # Enter card CVC
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="CVC"]'))).send_keys("0429")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()

    # Sign up
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[1]'))).send_keys("Abracadabra")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]'))).send_keys("Abracadabrovich")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[3]'))).send_keys(f"abracadabra+{context.test_id}@gmail.com")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Done"]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeTextField[@value="(000) 000-0000"]'))).send_keys("5104022040")
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//XCUIElementTypeStaticText[contains(@name, "Pay") or contains(@label, "Pay")])[2]'))).send_keys("5104022040")

    time.sleep(10000)

# @then('I as driver ios app extract all data to json file')
# def step_impl(context):
#     last_mile_no_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': 10, 'when': 12, 'vehicle': 14, 'size': 16,
#                          'distance': 18, 'order_type': 20}
#     last_mile_with_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': [10, 11, 12], 'when': 14, 'vehicle': 16,
#                            'size': 18, 'distance': 20, 'order_type': 22}
#     nationwide_no_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': 11, 'when': 13, 'vehicle': 15, 'size': 17,
#                           'distance': 19, 'order_type': 21}
#     nationwide_with_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': [11, 12, 13], 'when': 14, 'vehicle': 16,
#                             'size': 18, 'distance': 20, 'order_type': 22}
#
#     order_types = []
#     for i in range(20, 24):
#         try:
#             order_types.append(
#                 context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{i}]').text)
#         except NoSuchElementException:
#             continue
#
#     allowed_services = ['Last-mile delivery', 'Nationwide']
#     order_type = [service for service in order_types if service in allowed_services]
#
#     if context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[11]').text == '+ ' or context.driver.find_element( by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[12]').text == '+ ':
#         order_type = f'{order_type[0]} + tips'
#     else:
#         order_type = order_type[0]
#
#     if order_type == 'Last-mile delivery':
#         fields = last_mile_no_tips
#     elif order_type == 'Last-mile delivery + tips':
#         fields = last_mile_with_tips
#     elif order_type == 'Nationwide':
#         fields = nationwide_no_tips
#     elif order_type == 'Nationwide + tips':
#         fields = nationwide_with_tips
#     else:
#         raise ValueError("Unknown order type")
#
#     extracted_data = {}
#
#     for key, value in fields.items():
#         if isinstance(value, list):
#             extracted_data[key] = [
#                 context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{v}]').text
#                 for v in value]
#         else:
#             extracted_data[key] = context.driver.find_element(by=AppiumBy.XPATH,
#                                                               value=f'(//XCUIElementTypeStaticText[@name])[{value}]').text
#
#     context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Route"]').click()
#
#     if order_type.startswith('Last-mile delivery'):
#         additional_fields = {
#             'routes_amount': 7,
#             'time_and_miles': 8,
#             'apt_pick_up': 10,
#             'pick_up_address': 11,
#             'apt_drop_off': 15,
#             'drop_off_address': 16
#         }
#     elif order_type.startswith('Nationwide'):
#         additional_fields = {
#             'routes_amount': 10,
#             'time_and_miles': 11,
#             'apt_pick_up': 13,
#             'pick_up_address': 14,
#             'apt_drop_off': 'No drop-off apt since this is nationwide order',
#             'drop_off_address': 18
#         }
#     else:
#         raise ValueError("Unknown order type")
#
#     for key, value in additional_fields.items():
#         if key == 'apt_drop_off' and value == 'No drop-off apt since this is nationwide order' and order_type.startswith(
#                 'Nationwide'):
#             extracted_data[key] = value
#         else:
#             extracted_data[key] = context.driver.find_element(by=AppiumBy.XPATH,
#                                                               value=f'(//XCUIElementTypeStaticText[@name])[{value}]').text
#
#     print(extracted_data)

# @then('I as driver ios app extract all data to json file')
# def step_impl(context):
#     last_mile_no_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': 10, 'when': 12, 'vehicle': 14, 'size': 16,
#                          'distance': 18, 'order_type': 20}
#     last_mile_with_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': [10, 11, 12], 'when': 14, 'vehicle': 16,
#                            'size': 18, 'distance': 20, 'order_type': 22}
#     nationwide_no_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': 11, 'when': 13, 'vehicle': 15, 'size': 17,
#                           'distance': 19, 'order_type': 21}
#     nationwide_with_tips = {'order_id': 1, 'order_name': 4, 'driver_salary': [11, 12, 13], 'when': 15, 'vehicle': 17,
#                             'size': 19, 'distance': 21, 'order_type': 23}
#     order_types = []
#     for i in range(20, 24):
#         try:
#             order_types.append(context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{i}]').text)
#         except NoSuchElementException:
#             pass
#
#     allowed_services = ['Last-mile delivery', 'Nationwide']
#     order_type = [service for service in order_types if service in allowed_services][0]
#
#     if context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{11}]').text == '+ ' or context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{12}]').text == '+ ':
#         order_type += ' + tips'
#
#
#
#     if order_type == 'Last-mile delivery':
#         fields = last_mile_no_tips
#     elif order_type == 'Last-mile delivery + tips':
#         fields = last_mile_with_tips
#     elif order_type == 'Nationwide':
#         fields = nationwide_no_tips
#     elif order_type == 'Nationwide + tips':
#         fields = nationwide_with_tips
#     else:
#         raise ValueError("Unknown order type")
#
#     extracted_data = {}
#     for key, value in fields.items():
#         if isinstance(value, list):
#             extracted_data[key] = [
#                 context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{v}]').text
#                 for v in value]
#         else:
#             extracted_data[key] = context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{value}]').text
#
#     context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeStaticText[@name="Route"]').click()
#
#     last_mile = {'routes_amount': 10, 'time_and_miles': 11, 'apt_pick_up': 13, 'pick_up_address': 14,
#                  'apt_drop_off': 'No drop-off apt since this is nationwide order', 'drop_off_address': 18}
#     nationwide = {'routes_amount': 7, 'time_and_miles': 8, 'apt_pick_up': 12, 'pick_up_address': 13, 'apt_drop_off': 17,
#                   'drop_off_address': 18}
#
#     if order_type.startswith('Last-mile delivery'):
#         additional_fields = last_mile
#     elif order_type.startswith('Nationwide'):
#         additional_fields = nationwide
#     else:
#         raise ValueError("Unknown order type")
#
#     for key, value in additional_fields.items():
#         if key == 'apt_drop_off' and value == 'No drop-off apt since this is nationwide order' and order_type.startswith(
#                 'Last-mile delivery'):
#             extracted_data[key] = value
#         else:
#             extracted_data[key] = context.driver.find_element(by=AppiumBy.XPATH, value=f'(//XCUIElementTypeStaticText[@name])[{value}]').text
#
#     print(extracted_data)

    # base_fixture_attr.extract_data_to_json_file(order_id, order_name, driver_salary, when, vehicle, size, distance, order_type,
    #                                routes_amount, time_and_miles, apt_pick_up, pick_up_address, apt_drop_off,
    #                                drop_off_address)

# @given('I search for the order ID "{order_id}" and click on it')
# def step_impl(context, order_id):
#     swiper_attr = Swiper(context.driver)
#     counter_for_order = 1
#     while True:
#         try:
#             element = context.driver.find_element(by=AppiumBy.XPATH, value=f"//XCUIElementTypeTable/XCUIElementTypeCell[{counter_for_order}]//XCUIElementTypeStaticText[contains(@label, 'ID:')]")
#             if element.text[4:] == order_id:
#                 elem_to_click = element
#                 element.click()
#                 elem_to_click.click()
#                 print("Oh, here it is")
#                 break
#             else:
#                 print(f'Found order {element.text}, god damn it, I need another one')
#                 counter_for_order += 1
#         except NoSuchElementException:
#             swiper_attr.scroll_down('deep')
@then('I click on "Optimize route" "{decision}" ios')
def step_impl(context, decision: bool):
    if decision:
        context.driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN,value='**/XCUIElementTypeSwitch[`value == "0"`][2]').click()


@then('I add parcel size as "{parsel_size}" and "{vehicle_type}" ios')
def step_login(context, parsel_size, vehicle_type):
    context.parsel_size = parsel_size
    if context.country == 'US':
        if parsel_size == 'small':
            pass
        elif parsel_size == 'medium':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Medium (26-50 Lbs)"'))).click()
        elif parsel_size == 'large':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Large (51-70 Lbs)"'))).click()
            base_fixture_attr.choose_vehicle_type(context, vehicle_type)
        elif parsel_size == 'heavy_load':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Heavy Load (71+ Lbs)"'))).click()
            base_fixture_attr.choose_vehicle_type(context, vehicle_type)
        elif parsel_size == 'custom size':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Custom size"'))).click()
            base_fixture_attr.put_info_for_custom_size(context, [2, 2, 2, 2])
            base_fixture_attr.choose_vehicle_type(context, vehicle_type)
    elif context.country == 'CA':
        if parsel_size == 'small':
            pass
        elif parsel_size == 'medium':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Medium (26-50kg)"'))).click()
        elif parsel_size == 'large':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Large (51-70kg)"'))).click()
            base_fixture_attr.choose_vehicle_type(context, vehicle_type)
        elif parsel_size == 'heavy_load':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Heavy Load (71+ kg)"'))).click()
            base_fixture_attr.choose_vehicle_type(context, vehicle_type)
        elif parsel_size == 'custom size':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_PREDICATE, f'name == "Custom size"'))).click()
            base_fixture_attr.put_info_for_custom_size(context, [2, 2, 2, 2])
            base_fixture_attr.choose_vehicle_type(context, vehicle_type)


@given('I select country as "{country}" ios')
def step_impl(context, country):
    with open(counter_file, 'r') as file:
        a = int(file.read())
        context.test_id = a

    country_dict = {'United States':'US', 'Canada':'CA'}
    time.sleep(2)

    try:
        actual_text = context.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="US"]'))).text
    except:
        actual_text = context.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="CA"]'))).text

    context.country = actual_text

    if actual_text != country_dict[country]:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeImage[@name="DownArrowGray"]'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{country}"]'))).click()

@then('I add credit card info as "{card_number}" for credit card number, "{expiration_date}" for expiration date and "{cvv}" for CVV ios')
def step_impl(context, card_number, expiration_date, cvv):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeTextField[@name="card number"]'))).send_keys(card_number)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeTextField[@name="expiration date"]'))).send_keys(expiration_date)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeTextField[@name="CVC"]'))).send_keys(cvv)
    context.driver.swipe(120, 100, 120, 622, 100)


@then('I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number ios')
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[1]'))).send_keys('Avram')
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[2]'))).send_keys('Linkolnych')
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeTextField[3]'))).send_keys(f'automation.senpex+{unique_number}@outlook.com')
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//XCUIElementTypeTextField[@value="(000) 000-0000"]'))).send_keys('5104029084')

