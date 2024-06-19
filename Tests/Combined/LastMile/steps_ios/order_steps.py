import os
import time
import re
from behave import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from Tests.Combined.LastMile.steps_ios.base_steps import Swiper, BaseFixture
base_fixture_attr = BaseFixture()

now = datetime.now().day

counter_file = '//Tests/Driver/LastMile/IOS/INPUTS/counter.txt'

@given("I click on the latest available order")
def step_impl(context):
    context.driver.find_element(by=AppiumBy.XPATH, value=f"//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeOther").click()

@given('I search for the order ID "{order_id}" and click on it')
def step_impl(context, order_id):
    context.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeTextField[@value="Search"]').send_keys(order_id)
    time.sleep(1)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeOther[1]/XCUIElementTypeOther'))).click()


@then('I as driver ios app extract all data to json file')
def step_impl(context):
    import re

    extracted_data = {}
    vehicle_types = ['Car', 'Pickup Truck', 'SUV', '9ft Cargo Van', '9ft Ref Van', '10ft Box Truck', '15ft Box Truck',
                     '17ft Box Truck']
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
