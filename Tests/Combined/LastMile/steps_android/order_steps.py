import os
import time

from behave import *
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from Tests.Combined.LastMile.steps_android.base_steps import Swiper, BaseFixture
base_fixture_attr = BaseFixture()
now = datetime.now().day

counter_file = '/Users/kolokob/PycharmProjects/Automation/Tests/Combined/LastMile/steps_android/counter.txt'

with open(counter_file, 'r') as file:
    unique_number = int(file.read())

@given('I click on "Get a Quote"')
def step_login(context):
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnInstantOrder'))).click()

@then('I add pick-up address as "{address}"')
def step_login(context, address):
    context.pick_up_address = address
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtLocation'))).click()
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtLocation').send_keys(address)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()

@then('I select "{service}" service')
def step_login(context, service):
    if service != 'Last-mile delivery':
        context.driver.find_element(by=AppiumBy.ID, value=f'//android.widget.TextView[@resource-id="com.snpx.customer:id/txtName" and @text="{service}"]').click()
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@text="Place order"]'))).click()

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
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtLocation').click()
    context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtLocation').send_keys(address)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.view.ViewGroup[@resource-id="com.snpx.customer:id/place_item_view"])[1]'))).click()


@then('I add parcel size as "{parsel_size}"')
def step_login(context, parsel_size):
    context.parsel_size = parsel_size

    if isinstance(parsel_size, dict):
        parsel_key = list(parsel_size.keys())[0]

        if parsel_key != "small":
            if parsel_key == 'custom size':
                for key, value in parsel_size.items():
                    if not isinstance(value, list):
                        raise TypeError("Check rules for creating parcel size")

                context.put_info_for_custom_size(parsel_size)
                context.choose_vehicle_type(parsel_size)

            elif parsel_key == 'medium':
                raise TypeError("For medium size, a vehicle type cannot be selected")

            else:
                context.driver.find_element(by=AppiumBy.XPATH,
                                            value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_key]}]').click()
                context.choose_vehicle_type(parsel_size)

    elif parsel_size == 'custom size':
        context.put_info_for_custom_size(parsel_size)
        context.driver.find_element(by=AppiumBy.XPATH,
                                    value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[1]').click()

    else:
        if parsel_size == 'small':
            context.driver.find_element(by=AppiumBy.XPATH,
                                        value=f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.snpx.customer:id/recyclerViewSize"]/android.widget.RelativeLayout[{context.size[parsel_size]}]').click()
        elif parsel_size != 'medium':
            context.driver.find_element(by=AppiumBy.XPATH,
                                        value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').click()
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
    context.declared_value = value
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtItemValue'))).send_keys(value)

@then('I add pick-up time as "{pick_up_time}"')
def step_login(context, pick_up_time):
    context.pick_up_time = pick_up_time
    if type(pick_up_time) != str:
        date = datetime(year=datetime.now().year, month=datetime.now().month, day=list(pick_up_time.values())[0][-1])
        context.formatted_date = date.strftime("%d %B %Y")

        # Enter pick-up time
        if pick_up_time == 'urgent':
            pass

        elif pick_up_time == 'scheduled' or list(pick_up_time)[0] == 'scheduled':
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbScheduled'))).click()
            if isinstance(pick_up_time, str):
                context.wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ID, f'//android.widget.CheckedTextView[@content-desc="{now + 7}"]'))).click()
            elif isinstance(pick_up_time, dict):
                time.sleep(2)
                context.date = context.driver.find_elements(by=AppiumBy.XPATH, value=f'//android.widget.CheckedTextView[@content-desc="{list(pick_up_time.values())[0][0]}"]')
                if int(context.date[0].text) == int(list(pick_up_time.values())[0][0]):
                    context.date[0].click()
            context.select_pick_up_time(list(pick_up_time.values())[0][1])
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

        elif isinstance(pick_up_time, dict):
            if list(pick_up_time.keys())[0] == 'repeated':
                context.wait.until(
                    EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/rdbRepeated'))).click()
                for i in pick_up_time['repeated']:
                    if isinstance(i, dict):
                        for key, value in i.items():
                            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, f"com.snpx.customer:id/chk{key}"))).click()
                            context.select_pick_up_time(value)
                            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtStartDate'))).click()
                context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.view.View[@content-desc="{context.formatted_date}"]'))).click()
                context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'android:id/button1'))).click()

            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

        elif isinstance(pick_up_time, str):
            context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]"))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()
            context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

@then('I add extra services: "{extra_services}"')
def step_login(context, extra_services):
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
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, f'//android.widget.TextView[@resource-id="android:id/text1" and @text="{list(extra_services.values())[counter_for_services][1]}"]'))).click()
                        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnSave'))).click()
                        counter_for_services += 1
                        break
                counter += 1
            except NoSuchElementException:
                context.driver.swipe(551, 1507, 551, 189)

        context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/btnConfirm'))).click()

@then('I add promo code as "{promo_code}"')
def step_login(context, promo_code):
    context.promo_code = promo_code
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtPromo'))).send_keys(promo_code)

@then('I add tips as "{tips}"')
def step_login(context, tips):
    context.tips = tips
    if tips in [10, 15, 20, 25]:
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
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/txtDescription'))).send_keys(description)

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

@then('I add signature as required')
def step_login(context):
    context.signature = True
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/chkSignature'))).click()

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

@then('I add receiver phone number as "{receiver_phone_number}"')
def step_login(context, receiver_phone_number):
    context.receiver_phone_number = receiver_phone_number
    context.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.snpx.customer:id/txtPhone" and @text="Receiver\'s phone number"]'))).send_keys(receiver_phone_number)

@then('I add credit card info as "{credit_card_number}" for credit card number, "{expiration_date}" for expiration date and "{cvv}" for CVV')
def step_login(context, credit_card_number, expiration_date, cvv):
    context.credit_card_info = [credit_card_number, expiration_date, cvv]
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_card_number'))).send_keys(credit_card_number)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_expiry'))).send_keys(expiration_date)
    context.wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.snpx.customer:id/et_cvc'))).send_keys(cvv)

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

@then('I navigate to orders')
def step_login(context):
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
    print("Test passed")

@given('I compare two JSON files from client and driver')
def step_impl(context):
    base_fixture_attr.compare_files()
