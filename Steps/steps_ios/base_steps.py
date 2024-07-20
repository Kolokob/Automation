# file: Tests/Client/LastMile/Android/steps_android/base_steps.py
import email
import imaplib
import re
import sys
from email.header import decode_header
import json
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import subprocess
import datetime
import os
import time
from appium.options.android import UiAutomator2Options
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

appium_server_url = "http://localhost:4723"

capabilities = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "appium:deviceName": "iPhone",
    "appium:platformVersion": "16.2",
    "appium:language": "en",
    "appium:locale": "US",
    "appium:udid": "00008120-000849E214DB401E",
    "appium:xcodeSigningId": "iPhone Developer",
    "appium:updatedWDABundleId": "com.kolokob.WebDriverAgentRunner"
}

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class BaseFixture:

    def __init__(self):
        self.signature = None
        self.photos_attached = 0

    def setUp(self, context, bundle_id):
        capabilities["appium:bundleId"] = bundle_id
        options = UiAutomator2Options().load_capabilities(capabilities)
        context.driver = webdriver.Remote(appium_server_url, options=options)
        # context.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        context.wait = WebDriverWait(context.driver, 5)

        context.extra_services = {'Furniture Assembly and Disassembly': 1, 'Ladder': 2, 'Food Catering Setup': 3,
                               'Blankets': 4, 'White gloves service': 5, 'Waiting on the line': 6,
                               'Temperature Controlled Coolers': 7, 'Special Handling': 8, 'Personal Shopper': 9,
                               'Ratchet Straps': 10, 'Loading Ramps': 11, 'Hand Truck': 12, 'Applience Dolly': 13,
                               'Packing and Unpacking': 14}

        context.size = {'small': 1, 'medium': 2, 'large': 3, 'heavy_load': 4, 'custom size': 5}
        context.timing = {'urgent': 1, "schedule_a_pick-up": 2, "repeated_weekly": 3}
        context.days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 5: "Friday", 7: "Saturday"}
        context.days2 = {"Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 7}

        return context.driver, context.wait

    def tearDown(self, context):
        if context.driver:
            context.driver.quit()

    def extract_data_to_json_file(self, *args):
        filename = '/Tests/Combined/LastMile/OUTPUTS/outputs_ios.json'
        variable_names = [
            "order_id", "order_name", "driver_salary", "when", "vehicle", "size", "distance", "order_type",
            "routes_amount", "time_and_miles", "apt_pick_up", "pick_up_address", "apt_drop_off", "drop_off_address"
        ]

        new_data = {name: value for name, value in zip(variable_names, args)}

        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, 'r', encoding='utf-8') as f:
                try:
                    existing_data = json.load(f)
                except json.JSONDecodeError:
                    existing_data = []
            if isinstance(existing_data, list):
                existing_data.append(new_data)
            else:
                existing_data = [existing_data, new_data]
        else:
            existing_data = [new_data]

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=4)

    def get_password_from_email(self):
        username = "automation.senpex@outlook.com"
        password_for_email = "A27011975a"
        password = None

        mail = imaplib.IMAP4_SSL("outlook.office365.com", 993)
        try:
            mail.login(username, password_for_email)
            print("Login successful!")
        except imaplib.IMAP4.error as e:
            print(f"Failed to login: {e}")
            exit(1)

        mail.select("inbox")

        status, messages = mail.search(None, '(FROM "noreply@senpex.com")')
        email_ids = messages[0].split()

        if email_ids:
            email_date_pairs = []
            for email_id in email_ids:
                res, msg = mail.fetch(email_id, "(BODY[HEADER.FIELDS (DATE)])")
                for response_part in msg:
                    if isinstance(response_part, tuple):
                        msg_date = email.message_from_bytes(response_part[1])["Date"]
                        email_date_pairs.append((email_id, msg_date))

            email_date_pairs.sort(key=lambda x: email.utils.parsedate_to_datetime(x[1]), reverse=True)

            for email_id, _ in email_date_pairs:
                res, msg = mail.fetch(email_id, "(RFC822)")
                for response_part in msg:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject, encoding = decode_header(msg["Subject"])[0]
                        if isinstance(subject, bytes):
                            subject = subject.decode(encoding if encoding else "utf-8")
                        from_ = msg.get("From")

                        print("Subject:", subject)
                        print("From:", from_)
                        print("=" * 100)

                        if msg.is_multipart():
                            for part in msg.walk():
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))

                                try:
                                    body = part.get_payload(decode=True).decode()
                                except:
                                    pass

                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    print("Body:", body)
                                    match = re.search(r'Your password is (\d+)', body)
                                    if match:
                                        password = match.group(1)
                                        print(f"Extracted password: {password}")
                                        break
                        else:
                            body = msg.get_payload(decode=True).decode()
                            print("Body:", body)
                            match = re.search(r'Your password is (\d+)', body)
                            if match:
                                password = match.group(1)
                                print(f"Extracted password: {password}")
                                break
                if password:
                    break
        else:
            print("No emails found from noreply@senpex.com")

        mail.close()
        mail.logout()

        return password

    def choose_vehicle_type(self, context, vehicle_type: str):
        context.swipe_attr = Swiper(context.driver)
        success = False
        if vehicle_type != 'Car':
            while not success:
                try:
                    element = context.wait.until(EC.element_to_be_clickable((AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypeButton[`name == "{vehicle_type}"`]')))
                    element.click()
                    if not context.driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value=f'**/XCUIElementTypeButton[`name == "{vehicle_type}"`]'):
                        success = True
                    else:
                        context.driver.swipe(224, 560, 1, 560, 1000)
                except TimeoutException:
                    context.driver.swipe(224, 560, 1, 560, 1000)
                except Exception as e:
                    print(f"Error: {e}")
                    context.driver.swipe(224, 560, 1, 560, 1000)

        elif vehicle_type == 'Car':
            context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').click()
            success = True
        return success





class Swiper:

    def __init__(self, context):
        self.context = context

    def get_swipe_distance(self, swipe_intensity):
        if swipe_intensity == 'short':
            return 0.55, 0.45
        elif swipe_intensity == 'medium':
            return 0.60, 0.40
        elif swipe_intensity == 'long':
            return 0.65, 0.35
        elif swipe_intensity == 'deep':
            return 0.90, 0.10
        else:
            raise ValueError("Недопустимое значение для swipe_intensity. Используйте 'short', 'medium' или 'long'.")

    def scroll_down(self, swipe_intensity='medium'):
        size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        starty = size['height'] * start_factor
        endy = size['height'] * end_factor
        startx = size['width'] / 2
        if swipe_intensity == 'deep':
            self.context.swipe(startx, starty, startx, endy, 100)
        else:
            self.context.swipe(startx, starty, startx, endy, 400)


    def scroll_right(self, swipe_intensity='medium'):
        self.size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        startx = self.size['width'] * (1 - start_factor)
        endx = self.size['width'] * start_factor
        starty = self.size['height'] / 2
        if swipe_intensity == 'deep':
            self.context.swipe(startx, starty, startx, endx, 100)
        else:
            self.context.swipe(startx, starty, startx, endx, 400)

    def scroll_left(self, swipe_intensity='medium'):
        self.size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        startx = self.size['width'] * start_factor
        endx = self.size['width'] * (1 - start_factor)
        starty = self.size['height'] / 2
        if swipe_intensity == 'deep':
            self.context.swipe(startx, starty, startx, endx, 100)
        else:
            self.context.swipe(startx, starty, startx, endx, 400)

    def scroll_up(self, swipe_intensity='medium'):
        self.size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        starty = self.size['height'] * end_factor
        endy = self.size['height'] * start_factor
        startx = self.size['width'] / 2
        if swipe_intensity == 'deep':
            self.context.swipe(startx, starty, startx, endy, 100)
        else:
            self.context.swipe(startx, starty, startx, endy, 400)

