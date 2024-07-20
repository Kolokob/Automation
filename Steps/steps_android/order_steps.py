import sys
import string
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime, timedelta
from behave import given, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from tenacity import retry, wait_fixed, stop_after_attempt
import time

from Steps.steps_android.base_steps import Swiper, BaseFixture
base_fixture_attr = BaseFixture()
now = datetime.now().day

counter_file = '/Users/kolokob/PycharmProjects/Automation/Steps/steps_android/counter.txt'


with open(counter_file, 'r') as file:
    unique_number = int(file.read())

unique_number += 1

with open(counter_file, 'w') as file:
    file.write(str(unique_number))

def restart_app(context):
    context.driver = base_fixture_attr.setUp(context)

@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
def execute_scenario(context):
    try:
        context.execute_steps('''
            Given I click on "Get a Quote"
            Then I select "Last-mile delivery" service
            Then I add pick-up address as "S"
            Then I add location details as "Crater"
            Then I click Continue
            Then I add drop-off address as "Q"
            Then I add location details as "Sun"
            Then I click Continue
            Then I click Continue
            Then I click Continue
            Then I click Continue
            Then I click Continue
            Then I add name of the order as "Cockroaches"
            Then I add description to the order as "Describe your shipment"
            Then I make a "medium" "down" swipe
            Then I add sender full name as "Dart Wader"
            Then I add sender phone number as "5104029083"
            Then I make a "long" "down" swipe
            Then I make a "short" "down" swipe
            Then I make a "short" "down" swipe
            Then I add receiver full name as "John Marston"
            Then I add receiver phone number as "5104029083"
            Then I click Continue
            Then I click Continue
            Then I add credit card info as "{card_number}" for credit card number, "0429" for expiration date and "123" for CVV
            Then I add credentials for my new account as "Avram" for the first name, "Linkolnych" for the last name, and "5104029084" for the phone number
            Then I make a "long" "down" swipe
            Then I click Continue
        ''')
    except WebDriverException as e:
        print(f"Application crashed with error: {e}. Restarting the app and retrying...")
        restart_app(context)
        execute_scenario(context)


@given('I click on "Get a Quote"')
def step_login(context):
    counter = 0
    while counter < 5:
        try:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnInstantOrder'))).click()
            break
        except:
            time.sleep(1)
            counter += 1


@then('I add pick-up address as "{address}"')
def step_login(context, address):
    context.pick_up_address = address
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(address)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()


@then('I add "{pick_up_num}" pick-up\'s addresses and "{drop_off_num}" drop-off addresses')
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
    for i in range(max(pick_up_num, drop_off_num)):
        if i < pick_up_num:
            # Adding pick-up
            if i > 0:
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddPickup'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(addresses[i])
            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()

            # Add location details
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocationDetails'))).send_keys(details[i])

            # Click on 'Continue' button
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnContinue'))).click()

        if i < drop_off_num:
            # Adding drop-off
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddDropOff'))).click()
            try:
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(addresses[pick_up_num + i])
            except StaleElementReferenceException:
                time.sleep(2)
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(addresses[pick_up_num + i])
            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()

            # Add location details
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocationDetails'))).send_keys(details[pick_up_num + i])

            # Click on 'Continue' button
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnContinue'))).click()


# @then('I add "{pick_up_num}" pick-up\'s addresses and "{drop_off_num}" drop-off addresses')
# def step_login(context, pick_up_num, drop_off_num):
#     alphabet = list(string.ascii_lowercase)
#     vowels = 'aeiou'
#     consonants = ''.join([c for c in alphabet if c not in vowels])
#     combinations = [c + v for c in consonants for v in vowels]
#     addresses = alphabet + combinations
#     details = [''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 8))) for _ in range(20)]
#     for i in range(int(pick_up_num) + int(drop_off_num)-1):
#         # Adding pick-up
#         if i > 0:
#             context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddPickup'))).click()
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(addresses[i])
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()
#
#         # Add location details
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocationDetails'))).send_keys(details[i])
#
#         # CLick on 'Continue' button
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnContinue'))).click()
#
#         # Adding drop-off
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddDropOff'))).click()
#         try:
#             context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
#             context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(addresses[i+1])
#         except StaleElementReferenceException:
#             time.sleep(2)
#             context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(addresses[i+1])
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()
#
#         # Add location details
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocationDetails'))).send_keys(details[i+1])
#
#         # CLick on 'Continue' button
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnContinue'))).click()

@then('I select "{service}" service')
def step_login(context, service):
    counter = 0
    while counter < 5:
        try:
            if service != 'Last-mile delivery':
                context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName" and @text="{service}"]'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Place order"]'))).click()
            break
        except TimeoutException:
            counter += 1
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/imgClose'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnInstantOrder'))).click()
@then('I add location details as "{details}"')
def step_login(context, details):
    context.details = details
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocationDetails'))).send_keys(details)

@then('I click Continue')
def step_login(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnContinue'))).click()

@then('I add drop-off address as "{address}"')
def step_login(context, address):
    context.drop_off_address = address
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddDropOff'))).click()
    try:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(address)
    except StaleElementReferenceException:
        time.sleep(2)
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).send_keys(address)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()


@then('I add parcel size as "{parsel_size}" and "{vehicle_type}"')
def step_login(context, parsel_size, vehicle_type):
    context.parsel_size = parsel_size
    if parsel_size == 'small':
        # context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').click()
        pass
    elif parsel_size == 'medium':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]'))).click()
        # context.driver.find_element(by=AppiumBy.XPATH, value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]').click()
    elif parsel_size == 'large':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]'))).click()
        base_fixture_attr.choose_vehicle_type(context, vehicle_type)
    elif parsel_size == 'heavy_load':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]'))).click()
        base_fixture_attr.choose_vehicle_type(context, vehicle_type)
    elif parsel_size == 'custom size':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]'))).click()
        base_fixture_attr.put_info_for_custom_size(context, [2, 2, 2, 2])
        base_fixture_attr.choose_vehicle_type(context, vehicle_type)
    # if isinstance(parsel_size, dict):
    #     parsel_key = list(parsel_size.keys())[0]
    #
    #     if parsel_key != "small":
    #         if parsel_key == 'custom size':
    #             for key, value in parsel_size.items():
    #                 if not isinstance(value, list):
    #                     raise TypeError("Check rules for creating parcel size")
    #
    #             context.put_info_for_custom_size(parsel_size)
    #             context.choose_vehicle_type(parsel_size)
    #
    #         elif parsel_key == 'medium':
    #             raise TypeError("For medium size, a vehicle type cannot be selected")
    #
    #         else:
    #             context.driver.find_element(by=AppiumBy.XPATH, value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_key]}]').click()
    #             context.choose_vehicle_type(parsel_size)
    #
    # elif parsel_size == 'custom size':
    #     context.put_info_for_custom_size(parsel_size)
    #     context.driver.find_element(by=AppiumBy.XPATH, value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[1]').click()

# @then('I add parcel size as "{parsel_size}"')
# def step_login(context, parsel_size):
#     context.parsel_size = parsel_size
#     if isinstance(parsel_size, dict) and list(parsel_size.keys())[0] != "small":
#         if isinstance(parsel_size, dict) and list(parsel_size.keys())[0] == 'custom size':
#             for key, value in parsel_size.items():
#                 if not isinstance(value, list):
#                     raise TypeError("Check rules for creating parsel size")
#
#             context.put_info_for_custom_size(parsel_size)
#             context.choose_vegicle_type(parsel_size)
#
#         elif list(parsel_size.keys())[0] == 'medium' and isinstance(parsel_size, dict):
#             raise TypeError("For medium size can not be selected vehicle type")
#
#         elif isinstance(parsel_size, dict):
#             context.driver.find_element(by=AppiumBy.XPATH, value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[list(parsel_size.keys())[0]]}]').click()
#             context.choose_vegicle_type(parsel_size)
#
#     elif parsel_size == 'custom size':
#         context.put_info_for_custom_size(parsel_size)
#         context.driver.find_element(by=AppiumBy.XPATH, value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[1]').click()
#     else:
#         if parsel_size == 'small':
#             context.driver.find_element(by=AppiumBy.XPATH, value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]').click()
#         elif parsel_size != 'small' or parsel_size != 'medium':
#             context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').click()

@then('I make a "{length}" "{direction}" swipe')
def step_login(context, length, direction):
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


@then('I add declared value "{value}"')
def step_login(context, value):
    if int(value) > 0:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtItemValue'))).send_keys(value)
        context.declared_value = value
    else:
        context.declared_value = 0

@then('I add pick-up time as "{pick_up_time}" with days "{days_or_date}" and time "{time}" for each and start date as "{start_date}"')
def step_login(context, pick_up_time, days_or_date, time, start_date):
    context.pick_up_time = pick_up_time
    if pick_up_time == 'urgent':
        pass

    elif pick_up_time == 'scheduled':
        # Select scheduled
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbScheduled'))).click()
        # Select the date on the calendar
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.CheckedTextView[@content-desc="{days_or_date.split('/')[1].removeprefix('0')}"])[2]'))).click()
        # Select time
        base_fixture_attr.select_pick_up_time(context, time)

        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnContinue'))).click()

    elif pick_up_time == 'repeated':
        # Select repeated
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbRepeated'))).click()
        counter = 0
        for i in days_or_date.split(', '):
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f"com.snpx.customer:id/chk{i}"))).click()
            base_fixture_attr.select_pick_up_time(context, time.split(', ')[counter])
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()
            counter += 1

        formatted_date = datetime.strptime(start_date, "%d/%m/%Y").strftime("%d %B %Y")
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtStartDate'))).click()
        current_year = context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/date_picker_header_year'))).text
        current_month = context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/date_picker_header_date'))).text
        current_year_month = current_year + ' ' + current_month

        formatted_month = datetime.strptime(formatted_date, "%d %B %Y").strftime("%B")
        current_month = datetime.strptime(current_year_month, "%Y %a, %b %d").strftime("%B")

        if formatted_month != current_month:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/next"))).click()

        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.view.View[@content-desc="{formatted_date}"]'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

@then('I add extra services "{extra_service}" and service "{service}"')
def step_login(context, extra_service, service):
    extra_service = extra_service.split(', ')
    service = service.split(', ')
    min_length = min(len(extra_service), len(service))
    extra_services = {extra_service[i]: ['Be careful', service[i]] for i in range(min_length)}

    context.extra_services = extra_services
    if type(extra_services) == dict:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtNeedExtraServices'))).click()
        counter = 1
        counter_for_services = 0
        while counter_for_services < len(extra_services):
            try:
                for i in extra_services.keys():
                    if context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName"])[{counter}]').text == i:
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.ImageView[@resource-id="com.snpx.customer:id/checkbox"])[{counter}]'))).click()
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f'com.snpx.customer:id/txtNote'))).send_keys(list(extra_services.values())[0][0])
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f'com.snpx.customer:id/txtDropDown'))).click()
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="android:id/text1" and @text="{extra_services[i][1]}"]'))).click()
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnSave'))).click()
                        counter_for_services += 1
                        break
                counter += 1
            except NoSuchElementException:
                context.driver.swipe(551, 1507, 551, 189)
                counter = 1

        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

@then('I add promo code as "{promo_code}"')
def step_login(context, promo_code):
    context.promo_code = promo_code
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPromo'))).send_keys(promo_code)

@then('I add tips as "{tips}"')
def step_login(context, tips):
    context.tips = tips
    if tips == 'None' or tips is None:
        pass
    elif tips in [10, 15, 20, 25]:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f'com.snpx.customer:id/rdb{tips}'))).click()
    else:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtTip'))).send_keys(tips)
        context.order_price = context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.snpx.customer:id/txtTotalAmount"]'))).text

@then('I add name of the order as "{name}"')
def step_login(context, name):
    context.order_name = f"AUTO TEST №{unique_number}; Name: {name}"
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtSendingName'))).send_keys(f"AUTO TEST №{unique_number}; Name: {name}")

@then('I add description to the order as "{description}"')
def step_login(context, description):
    context.order_description = description
    counter = 0
    while counter < 5:
        try:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtDescription'))).send_keys(description)
            break
        except StaleElementReferenceException:
            counter += 1


@then('I add "{amount}" photos')
def step_login(context, amount):
    base_fixture_attr.check_photos_attached(amount)
    for i in range(1, amount):
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/addImages'))).click()
        time.sleep(7)
        if i < 2:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.ImageView[@content-desc="Image"])[{i}]'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/menu_done'))).click()

@then('I add signature "{decision}"')
def step_login(context, decision):
    if decision == "Yes":
        context.signature = True
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/chkSignature'))).click()
    elif decision == "No":
        context.signature = False

@then('I add sender full name as "{sender_full_name}"')
def step_login(context, sender_full_name):
    context.sender_full_name = sender_full_name
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtFullName'))).send_keys(sender_full_name)

@then('I add sender phone number as "{sender_phone_number}"')
def step_login(context, sender_phone_number):
    context.sender_phone_number = sender_phone_number
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPhone'))).send_keys(sender_phone_number)

@then('I add receiver full name as "{receiver_full_name}"')
def step_login(context, receiver_full_name):
    context.receiver_full_name = receiver_full_name
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtFullName'))).send_keys(receiver_full_name)

@then('I add receiver\'s and sender\'s all info in all required fields')
def step_login(context):
    context.swipe_attr = Swiper(context)
    context.sender_phone_number = "5104029082"
    context.receiver_phone_number = "5104029084"
    context.sender_full_name = "John Marston"
    context.receiver_full_name = "Arthur Morgan"
    counter = 1
    a = context.addresses_amount
    for i in range(context.addresses_amount + context.addresses_amount):
        if counter == 1:
            context.driver.swipe(300, 1380, 300, 330, 2000)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtFullName'))).send_keys(context.sender_full_name)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPhone'))).send_keys(context.sender_phone_number)
        context.driver.swipe(300, 1512, 300, 320, 2000)
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtFullName'))).send_keys(context.sender_full_name)
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPhone'))).send_keys(context.sender_phone_number)
        if counter == (context.addresses_amount + context.addresses_amount):
            last_elements = context.wait.until(EC.visibility_of_all_elements_located((AppiumBy.ID, 'com.snpx.customer:id/txtPhone')))
            last_elements[1].send_keys(context.sender_phone_number)
        counter += 1



@then('I add receiver phone number as "{receiver_phone_number}"')
def step_login(context, receiver_phone_number):
    context.receiver_phone_number = receiver_phone_number
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.snpx.customer:id/txtPhone" and @text="Receiver\'s phone number"]'))).send_keys(receiver_phone_number)

@then('I add credit card info as "{credit_card_number}" for credit card number, "{expiration_date}" for expiration date and "{cvv}" for CVV')
def step_login(context, credit_card_number, expiration_date, cvv):
    context.credit_card_info = [credit_card_number, expiration_date, cvv]
    counter = 0
    while counter < 10:
        try:
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys(credit_card_number)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys(expiration_date)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys(cvv)
        except:
            counter += 1
            context.driver.swipe(300, 1380, 300, 330, 1000)

@then('I pay with correct credit card')
def step_payment(context):
    context.credit_card_info = ['4242 4242 4242 4242', '0430', '123']
    try:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys('4242 4242 4242 4242')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys('0430')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys('123')
    except StaleElementReferenceException:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys('4242 4242 4242 4242')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys('0430')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys('123')

@then('I pay with wrong credit card')
def step_payment(context):
    context.credit_card_info = ['1234 1234 1234 1234', '0430', '123']
    try:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys('1234 1234 1234 1234')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys('0430')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys('123')
    except StaleElementReferenceException:
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys('1234 1234 1234 1234')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys('0430')
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys('123')

@then('I pay with payment link')
def step_payment(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.snpx.customer:id/rltPaymentMethod"]/android.widget.ImageView[2]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbCreatePaymentLink'))).click()


# @then('I should see an error message')
# def step_see_error_message(context):
#     time.sleep(2)
#     specific_error_locator = (AppiumBy.ID, "com.snpx.customer:id/textinput_error")
#     generic_error_locators = [
#         (AppiumBy.ID, "android:id/message")
#     ]
#
#     expected_error_messages = ["Your card's number is invalid.", "Please try again later"]
#     error_message = None
#
#     try:
#         error_element = context.wait.until(EC.presence_of_element_located(specific_error_locator))
#         if error_element.is_displayed():
#             error_message = error_element.text
#             assert error_message in expected_error_messages, f"Unexpected error message: {error_message}"
#         else:
#             raise TimeoutException
#     except TimeoutException:
#         for locator in generic_error_locators:
#             try:
#                 error_element = context.wait.until(EC.presence_of_element_located(locator))
#                 if error_element.is_displayed():
#                     error_message = error_element.text
#                     if error_message in expected_error_messages:
#                         break
#             except TimeoutException:
#                 continue
#
#     assert error_message in expected_error_messages, f"Unexpected error message: {error_message}"
#
#     if error_message == "Your card's number is invalid.":
#         print(f'Card {context.credit_card_info[0]} was not accepted with error: {error_message}')
#     elif error_message == "Please try again later":
#         print(f'Card {context.credit_card_info[0]} was not accepted with a generic error: {error_message}')
#     else:
#         print(f'Card {context.credit_card_info[0]} was not accepted with an unexpected error: {error_message}')


@then('I should see an error message')
def step_login(context):
    time.sleep(2)
    specific_error_locator = (AppiumBy.ID, "com.snpx.customer:id/textinput_error")
    generic_error_locators = [(AppiumBy.ID, "android:id/message")]

    error_message = None

    try:
        error_element = context.wait.until(EC.presence_of_element_located(specific_error_locator))
        if error_element.is_displayed():
            error_message = error_element.text
            assert error_message == "Your card's number is invalid.", f"Error message: {error_message}"
        else:
            raise TimeoutException
    except TimeoutException or StaleElementReferenceException:
        for locator in generic_error_locators:
            try:
                error_element = context.wait.until(EC.presence_of_element_located(locator))
                if error_element.is_displayed():
                    error_message = error_element.text
                    if error_message != "Please try again later":
                        break
            except TimeoutException:
                continue

    if error_message == "Your card's number is invalid":
        print(f'Card {context.credit_card_info[0]} was not accepted with error: {error_message}')
    elif error_message == "Please try again later":
        print(f'Card {context.credit_card_info[0]} was not accepted with a generic error: {error_message}')
    else:
        print(f'Card {context.credit_card_info[0]} was not accepted with an expected error: {error_message}')


# There is no editing email, due to high complexity making it dynamic
@then('I add credentials for my new account as "{first_name}" for the first name, "{last_name}" for the last name, and "{phone_number}" for the phone number')
def step_login(context, first_name, last_name, phone_number):
    context.credentials_for_new_account = [first_name, last_name, phone_number]
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtFirstName'))).send_keys(first_name)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLastName'))).send_keys(last_name)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtEmail'))).send_keys(f'automation.senpex+{unique_number}@outlook.com')
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPhoneNumber'))).send_keys(phone_number)

    context.unique_number = unique_number

@then('I click on "Track Order"')
def step_login(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnTrackOrder'))).click()

@then('I click on button2 (I have no idea what it is, but it is necessary)')
def step_login(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/button2'))).click()

@then('I retrieve password from the email')
def step_login(context):
    context.new_password = BaseFixture.get_password_from_email(context)

@then('I navigate the latest order')
def step_login(context):
    time.sleep(3)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/navigation_orders'))).click()

    if base_fixture_attr.contains_repeated(context.pick_up_time):
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbRepeated'))).click()

    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerView"]/android.widget.FrameLayout[1]'))).click()
    context.order_id = context.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.snpx.customer:id/txtTitle"]'))).text[1:]


@then('I extract data to json file')
def step_login(context):
    base_fixture_attr.extract_data_to_json_file(context, context.order_id, context.order_name, context.order_price, context.sender_full_name, context.sender_phone_number,
                                      context.receiver_full_name, context.receiver_phone_number, context.parsel_size,
                                      context.declared_value, context.pick_up_time, context.extra_services,
                                      context.promo_code, context.tips, context.order_description, base_fixture_attr.return_photos_attached(),
                                      base_fixture_attr.signature, unique_number)

@then('I wait for "{seconds}" seconds')
def step_impl(context, seconds):
    time.sleep(int(seconds))

@then('I enjoy my work')
def step_impl(context):
    end_time = time.time() + 5
    while time.time() < end_time:
        for dots in range(4):
            sys.stdout.write(f"\r{'Enjoying my work'}{'.' * dots}   ")
            sys.stdout.flush()
            time.sleep(0.3)

@given('I compare two JSON files from client and driver')
def step_impl(context):
    base_fixture_attr.compare_files()

@then('I select payment type as payment link')
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.snpx.customer:id/rltPaymentMethod"]/android.widget.ImageView[2]'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbCreatePaymentLink'))).click()

@then('I add payer\'s phone number "{phone_number}" and email "{email}"')
def step_impl(context, phone_number, email=f'automation.senpex+{unique_number}@outlook.com'):
    if email == '<>':
        email = f'automation.senpex+{unique_number}@outlook.com'
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPayersEmail'))).send_keys(email)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPayersPhoneNumber'))).send_keys(phone_number)


@then('I open retrieved payment link and pay for it "{card_number}", "{date}", "{cvv}"')
def step_impl(context, card_number, date, cvv):
    payment_link = base_fixture_attr.get_link_from_email()
    base_fixture_attr.open_link_in_browser(payment_link, card_number, date, cvv)

@then('I open "{app}" app')
def step_impl(context, app):
    if app == "customer":
        app_package = 'com.snpx.customer'
        app_activity = 'com.snpx.customer.ui.SplashActivity'
    elif app == "chrome":
        app_package = 'com.android.chrome'
        app_activity = 'com.google.android.apps.chrome.Main'
    else:
        raise ValueError(f"Unknown app: {app}")

    base_fixture_attr.open_app(context, app_package, app_activity)


@then('I add credit card info as "{card_number}" for credit card number, "{date}" for expiration date and "{cvv}" for CVV for payment request')
def step_impl(context, card_number, date, cvv):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.webkit.WebView[@text="Payment request"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]'))).send_keys(card_number)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.webkit.WebView[@text="Payment request"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[4]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'))).send_keys(date)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.webkit.WebView[@text="Payment request"]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[6]/android.view.View/android.view.View/android.view.View'))).send_keys(cvv)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@text="Pay"]'))).click()

@then('I select payment type as "{payment_type}"')
def step_impl(context, payment_type):
    if payment_type == 'saved card':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtText"])[1]'))).click()
    elif payment_type == 'payment link':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RelativeLayout[@resource-id="com.snpx.customer:id/rltPaymentMethod"]/android.widget.ImageView[2]'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbCreatePaymentLink'))).click()
    elif payment_type == 'new credit card':
        counter = 0
        while counter < 3:
            try:
                context.credit_card_info = ['4242 4242 4242 4242', '0429', '123']

                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/imgCreditPlus'))).click()

                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys('4242 4242 4242 4242')

                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys('0429')
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys('123')
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddNewCard'))).click()
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
                context.driver.swipe(300, 330, 300, 1380, 500)
                context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtText"])[1]'))).click()
                break
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException,):
                if counter == 2:
                    raise Exception('Something went wrong with the list of cards')
                counter += 1
                context.driver.swipe(300, 1380, 300, 330, 1000)

    elif payment_type.split()[0] == 'new credit card':
        counter = 0
        credit_card_number = payment_type.split()[0]
        expiry = payment_type.split()[1]
        cvv = payment_type.split()[2]
        while counter < 3:
            try:
                context.credit_card_info = [credit_card_number, expiry, cvv]
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/imgCreditPlus'))).click()
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys(credit_card_number)
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys(expiry)
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys(cvv)
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddNewCard'))).click()
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
                context.driver.swipe(300, 330, 300, 1380, 500)
                context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtText"])[1]'))).click()
                break
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException,):
                if counter == 2:
                    raise Exception('Something went wrong with the list of cards')
                counter += 1
                context.driver.swipe(300, 330, 300, 1380, 1000)


@then('I select saved credit card')
def step_impl(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtText"])[1]'))).click()

@then('I select recently created credit card')
def step_impl(context):
    context.driver.swipe(300, 330, 300, 1380, 100)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtText"])[last()]'))).click()
    context.driver.swipe(300, 1380, 300, 330, 100)

@then('I add a new card as "{credit_card_number}" for credit card number, "{expiration_date}" for expiration date and "{cvv}" for CVV')
def step_login(context, credit_card_number, expiration_date, cvv):
    counter = 0
    while counter < 10:
        try:
            context.credit_card_info = [credit_card_number, expiration_date, cvv]

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/imgCreditPlus'))).click()

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys(credit_card_number)

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys(expiration_date)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys(cvv)
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddNewCard'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()
            break
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException,):
            if counter == 10:
                raise Exception('Something went wrong with the list of cards')
            counter += 1
            context.driver.swipe(300, 330, 300, 1380, 100)


@then('I select categories "{category}" with "{add_info}"')
def step_impl(context, category: str, add_info: str):
    i = 1
    while True:
        try:
            element = context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName"])[{i}]')))
            a = element.text
            if element.text == category:
                element.click()
                break
            else:
                i += 1
        except:
            context.driver.swipe(551, 1507, 551, 1000)
            i = 1

    k = 1
    while True:
        try:
            element = context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName"])[{k}]')))
            if element.text == add_info:
                element.click()
                break
            else:
                k += 1
        except:
            context.driver.swipe(551, 1507, 551, 1000)
            k = 1

# @then('I select categories "{category}" with "{add_info}"')
# def step_impl(context, category: str, add_info: str):
#     i = 1
#     k = 1
#     while i <= 11:
#         try:
#             element = context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName"])[{i}]')))
#             t = element.text
#             if element.text == category:
#                 element.click()
#                 break
#             i += 1
#         except:
#             context.driver.swipe(551, 1507, 551, 189)
#
#     while True:
#         try:
#             element2 = context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName"])[{k}]')))
#             if element2.text == add_info:
#                 element2.click()
#                 break
#             k += 1
#         except (IndexError, NoSuchElementException, StaleElementReferenceException):
#             context.driver.swipe(551, 1507, 551, 189)
#             k -= 1


#     context.extra_services = extra_services
#     if type(extra_services) == dict:
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtNeedExtraServices'))).click()
#         counter = 1
#         counter_for_services = 0
#         while counter_for_services < len(extra_services):
#             try:
#                 for i in extra_services.keys():
#                     if context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName"])[{counter}]').text == i:
#                         context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'(//android.widget.ImageView[@resource-id="com.snpx.customer:id/checkbox"])[{counter}]'))).click()
#                         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f'com.snpx.customer:id/txtNote'))).send_keys(list(extra_services.values())[0][0])
#                         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f'com.snpx.customer:id/txtDropDown'))).click()
#                         context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="android:id/text1" and @text="{list(extra_services.values())[counter_for_services][1]}"]'))).click()
#                         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnSave'))).click()
#                         counter_for_services += 1
#                         break
#                 counter += 1
#             except NoSuchElementException:
#                 context.driver.swipe(551, 1507, 551, 189)
#
#         context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

@then('I choose vehicle type as "{vehicle_type}" in "{service}"')
def step_impl(context, vehicle_type: str, service: str):
    base_fixture_attr.choose_vehicle_type(context, vehicle_type, service)


@then('I select "{helpers_amount}" helpers')
def step_impl(context, helpers_amount:str):
    if helpers_amount == 'only driver':
        pass
    elif helpers_amount == '1':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RadioButton[@resource-id="com.snpx.customer:id/rbVehicleType" and @text="1"]'))).click()
    elif helpers_amount == '2':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RadioButton[@resource-id="com.snpx.customer:id/rbVehicleType" and @text="2"]'))).click()
    elif helpers_amount == '3':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.RadioButton[@resource-id="com.snpx.customer:id/rbVehicleType" and @text="3"]'))).click()


@then('I add pick-up address and drop-off address as "{pick_up_address}", "{drop_off_address}" for Nationwide')
def step_impl(context, pick_up_address, drop_off_address):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtPickupAddress'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtLocation'))).send_keys(pick_up_address)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtLocationDetails'))).send_keys('apt 1')
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/btnContinue'))).click()

    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtDropOffAddress'))).click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtLocation'))).send_keys(drop_off_address)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtLocationDetails'))).send_keys('apt 2')
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/btnContinue'))).click()


@then('I add pick-up full name as "{full_name}" for Nationwide')
def step_impl(context, full_name):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, 'com.snpx.customer:id/txtPickupFullName'))).send_keys(full_name)


@then('I should see order status as "{status}"')
def step_impl(context, status):
    element = context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtOrderStatus')))
    assert element.text == status


@then('I add a new card as "{card_number}" expecting it to fail')
def step_impl(context, card_number):
    counter = 0
    while counter < 10:
        try:
            context.credit_card_info = [card_number, '0429', '123']

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/imgCreditPlus'))).click()

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys(card_number)

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys('0429')
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys('123')
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnAddNewCard'))).click()
            break
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException,):
            if counter == 10:
                raise Exception('Something went wrong with the list of cards')
            counter += 1
            context.driver.swipe(300, 330, 300, 1380, 100)


@then('I add all sender\'s info "{send_full_name}", "{send_phone_number}", "{send_email}"')
def step_impl(context, send_full_name, send_phone_number, send_email):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPickupFullName'))).send_keys(send_full_name)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPickupPhone'))).send_keys(send_phone_number)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPickupEmail'))).send_keys(send_email)


@then('I add all recipient\'s info "{rec_full_name}", "{rec_phone_number}"')
def step_impl(context, rec_full_name, rec_phone_number):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtDropOffFullName'))).send_keys(rec_full_name)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtDropOffPhone'))).send_keys(rec_phone_number)


@then('I add custom dimensions as "{length}", "{width}", "{height}", "{parcel_weight}", "{packing}"')
def step_impl(context, length, width, height, parcel_weight, packing:str):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLength'))).send_keys(length)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtWidth'))).send_keys(width)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtHeight'))).send_keys(height)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtWeight'))).send_keys(parcel_weight)
    if packing == "No":
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPacking'))).click()
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f'//android.widget.CheckedTextView[@resource-id="android:id/text1" and contains(@text, "{packing.capitalize()}")]'))).click()


@then('I add additional indo as "{order_name}", "{declared_value}", "{special_notes}", "{schedule_time}"')
def step_impl(context, order_name, declared_value, special_notes, schedule_time):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtSendingName'))).send_keys(order_name)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtDeclaredValue'))).send_keys(declared_value)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtNote'))).send_keys(special_notes)
    if schedule_time != 'Ready for pick-up':
        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtScheduleTime'))).click()

