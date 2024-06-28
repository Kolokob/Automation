# file: Tests/Client/LastMile/Android/steps_android/base_steps.py
import ast
import email
import imaplib
import inspect
import re
import time
from _pydatetime import timedelta
from email.header import decode_header

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

from selenium.common import NoSuchElementException, ElementClickInterceptedException

import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import subprocess
import datetime
from datetime import datetime
from datetime import timedelta
import os
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.snpx.customer',
    appActivity='com.snpx.customer.ui.SplashActivity',
    language='en',
    locale='US',
    newCommandTimeout=10000

)

appium_server_url = "http://localhost:4723"

class BaseFixture:

    def __init__(self):
        self.signature = None
        self.photos_attached = 0

    def setUp(self, context):
        context.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
        context.wait = WebDriverWait(context.driver, 10)

        file_path = '/Users/kolokob/PycharmProjects/Automation/Steps/steps_android/counter.txt'
        with open(file_path, 'r') as file:
            counter_value = int(file.read().strip())

        counter_value += 1

        with open(file_path, 'w') as file:
            file.write(str(counter_value))

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

    def check_photos_attached(self, photos_attached):
        if photos_attached > 0:
            self.photos_attached = photos_attached
        return 0

    def return_photos_attached(self):
        return self.photos_attached

    def choose_vehicle_type(self, context, vehicle_type:str):
        if vehicle_type != 'Car':
            while True:
                try:
                    if context.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').text == vehicle_type:
                        context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').click()
                        break
                    elif context.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[2]').text == vehicle_type:
                        context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[2]').click()
                        break
                    context.driver.swipe(900, 1676, 560, 1676, 300)
                except NoSuchElementException:
                    context.driver.swipe(900, 1676, 560, 1676, 300)
        elif vehicle_type == 'Car':
            context.driver.find_element(by=AppiumBy.XPATH, value=f'(//android.widget.TextView[@resource-id="com.snpx.customer:id/lblVehicleType"])[1]').click()

    def put_info_for_custom_size(self, context, parsel_size):
        context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtLength').send_keys(parsel_size[0])
        context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtWidth').send_keys(parsel_size[1])
        context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtHeight').send_keys(parsel_size[2])
        context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/txtWeight').send_keys(parsel_size[3])

        context.driver.find_element(by=AppiumBy.ID, value='com.snpx.customer:id/btnConfirm').click()

    def select_pick_up_time(self, context, time):

        def down(swipe_times, hmp):
            dic = {'hours': 300, 'minutes': 500, 'period': 1275}
            for _ in range(swipe_times):
                context.driver.swipe(dic[hmp], 1826, dic[hmp], 1640)

        def up(swipe_times, hmp):
            dic = {'hours': 300, 'minutes': 500, 'period': 1275}
            for _ in range(swipe_times):
                context.driver.swipe(dic[hmp], 1640, dic[hmp], 1826)

        def move_switch_back(direction):

            context.driver.swipe(1275, 1826, 1275, 1640) if direction == 'down' \
                else context.driver.swipe(1275, 1640, 1275, 1826)

        target_hour = int(time.split(':')[0])
        target_minute = int(time.split(':')[1][:2])
        target_period = time.split(' ')[1]


        current_hour = int(context.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="android:id/numberpicker_input"])[1]').text)
        current_minute = int(context.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="android:id/numberpicker_input"])[2]').text)
        current_period = context.driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.EditText[@resource-id="android:id/numberpicker_input"])[3]').text

        if target_hour != current_hour:
            if abs(target_hour - current_hour) == 6:
                down(int(abs(target_hour - current_hour)), 'hours')
            elif abs(target_hour - current_hour) < 6:
                if current_hour < target_hour:
                    down(int(abs(target_hour - current_hour)), 'hours')
                else:
                    up(int(abs(target_hour - current_hour)), 'hours')
            elif abs(target_hour - current_hour) > 6:
                if current_hour > target_hour:
                    down(int(abs(target_hour - current_hour)), 'hours')
                else:
                    up(int(abs(target_hour - current_hour)), 'hours')

        minute_diff = target_minute - current_minute
        if minute_diff != 0:
            if abs(minute_diff) < 30:
                if current_minute < target_minute:
                    down(abs(minute_diff), 'minutes')
                else:
                    up(abs(minute_diff), 'minutes')
            else:  # abs(minute_diff) >= 30
                if current_minute > target_minute:
                    down((60 - abs(minute_diff)), 'minutes')
                else:
                    up((60 - abs(minute_diff)), 'minutes')

        if target_period != current_period:
            move_switch_back('down' if current_period == 'AM' else 'up')

    def get_all_var_from_method(self, method, *args, **kwargs):
        sig = inspect.signature(method)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        return bound_args.arguments

    @staticmethod
    def extract_data_to_json_file(context, *args):
        extra_services = args[10]

        if isinstance(extra_services, str):
            try:
                extra_services = json.loads(extra_services.replace("'", '"'))
            except json.JSONDecodeError:
                pass

        formatted_extra_services = {}
        for key, value in extra_services.items():
            if isinstance(value, list) and len(value) == 2:
                formatted_extra_services[key] = {
                    "description": value[0],
                    "duration_or_quantity": value[1]
                }
            else:
                formatted_extra_services[key] = value

        data = {
            "order_id": args[0],
            "order_name": args[1],
            "order_price": args[2],
            "sender_full_name": args[3],
            "sender_phone_number": args[4],
            "receiver_full_name": args[5],
            "receiver_phone_number": args[6],
            "parcel_size": args[7],
            "declared_value": args[8],
            "pick_up_time": args[9],
            "extra_services": formatted_extra_services,
            "promo_code": args[11],
            "tips": args[12],
            "order_description": args[13],
            "photos_attached": args[14],
            "signature": args[15],
            "unique_number": args[16]
        }

        context.counter_file = '/Tests/Combined/LastMile/OUTPUTS/counter.txt'

        if not os.path.exists(context.counter_file):
            with open(context.counter_file, 'w') as file:
                file.write('0')

        with open(context.counter_file, 'r') as file:
            current_value = int(file.read())

        unique_number = current_value + 1

        data['unique_id'] = unique_number

        with open(context.counter_file, 'w') as file:
            file.write(str(unique_number))

        file_path = '/Tests/Combined/LastMile/OUTPUTS/outputs_android.json'
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                try:
                    existing_data = json.load(json_file)
                    if isinstance(existing_data, dict):
                        existing_data = [existing_data]
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        existing_data.append(data)

        with open(file_path, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

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

        # Получить только последние 5 писем
        status, messages = mail.search(None, '(FROM "noreply@senpex.com")')
        email_ids = messages[0].split()[-5:]  # Получаем последние 5 писем

        for email_id in reversed(email_ids):  # Проверяем последние письма сначала
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

                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                body = part.get_payload(decode=True).decode()
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

    def contains_repeated(self, pick_up_time):
        if isinstance(pick_up_time, str):
            return 'repeated' in pick_up_time
        elif isinstance(pick_up_time, list):
            return any(self.contains_repeated(item) for item in pick_up_time)
        elif isinstance(pick_up_time, dict):
            return any(self.contains_repeated(key) or self.contains_repeated(value) for key, value in pick_up_time.items())
        else:
            return False

    def compare_files(self):
        differences = []
        file1_path = '/Tests/Combined/LastMile/OUTPUTS/outputs_android.json'
        file2_path = '/Tests/Combined/LastMile/OUTPUTS/outputs_ios.json'

        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            file1_list = json.load(f1)
            file2_list = json.load(f2)

        file1 = file1_list[-1]
        file2 = file2_list[-1]

        if 'order_id' in file2:
            file2['order_id'] = str(file2['order_id'])

        logical_mapping = {
            "order_id": "order_id",
            "when": "pick_up_time",
            "size": "parcel_size",
            "pick_up_address": "pick_up_address",
            "drop_off_address": "drop_off_address",
            "apt_pick_up": "sender_full_name",
            "apt_drop_off": "receiver_full_name"
        }

        for key1, key2 in logical_mapping.items():
            value1 = file1.get(key1)
            value2 = file2.get(key2)

            if value1 != value2:
                differences.append({
                    'field_in_file1': key1,
                    'field_in_file2': key2,
                    'file1_value': value1,
                    'file2_value': value2
                })

        if differences:
            print("Differences found:")
            for diff in differences:
                print(f"Field in File 1: {diff['field_in_file1']}")
                print(f"Field in File 2: {diff['field_in_file2']}")
                print(f"Value in File 1: {diff['file1_value']}")
                print(f"Value in File 2: {diff['file2_value']}")
                print("-" * 40)
        else:
            print("No differences found. Test passed.")

    def get_link_from_email(self):
        username = "automation.senpex@outlook.com"
        password_for_email = "A27011975a"
        link = None
        max_wait_time = 600  # Максимальное время ожидания в секундах
        poll_interval = 30  # Интервал опроса в секундах

        mail = imaplib.IMAP4_SSL("outlook.office365.com", 993)
        try:
            mail.login(username, password_for_email)
            print("Login successful!")
        except imaplib.IMAP4.error as e:
            print(f"Failed to login: {e}")
            exit(1)

        while max_wait_time > 0:
            mail.select("inbox")

            status, messages = mail.search(None, '(FROM "noreply@senpex.com")')
            email_ids = messages[0].split()

            if email_ids:
                latest_email_id = email_ids[-1]

                res, msg = mail.fetch(latest_email_id, "(RFC822)")
                for response_part in msg:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        msg_date = email.utils.parsedate_to_datetime(msg['Date'])

                        # Преобразуем оба объекта datetime в наивные
                        msg_date_naive = msg_date.replace(tzinfo=None)
                        current_time_naive = datetime.now().replace(tzinfo=None)

                        # Check if the email was received within the last 2 minutes
                        if current_time_naive - msg_date_naive <= timedelta(minutes=2):
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
                                    if content_type == "text/plain" and "attachment" not in content_disposition:
                                        body = part.get_payload(decode=True).decode()
                                        match = re.search(
                                            r'Please use the link below to process payment\s*(https?://\S+)', body)
                                        if match:
                                            link = match.group(1)
                                            print(f"Extracted link: {link}")
                                            break
                            else:
                                body = msg.get_payload(decode=True).decode()
                                match = re.search(r'Please use the link below to process payment\s*(https?://\S+)',
                                                  body)
                                if match:
                                    link = match.group(1)
                                    print(f"Extracted link: {link}")
                                    break

                        if link:
                            break
                    if link:
                        break

            if link:
                break

            time.sleep(poll_interval)
            max_wait_time -= poll_interval
            print(f"Waiting for a new email. Time left: {max_wait_time} seconds")

        mail.close()
        mail.logout()

        return link

    def open_link_in_browser(self, link, card_number, date, cvv):
        desired_capabilities = {
            'platformName': 'Android',
            'automationName': 'uiautomator2',
            'deviceName': 'Android',
            'browserName': 'Chrome',
            'language': 'en',
            'locale': 'US',
            'chromedriver_autodownload': True
        }

        appium_server_url = "http://localhost:4723"

        driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_capabilities))

        try:
            driver.get(link)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.TAG_NAME, 'body')))
            print("Page loaded successfully")
            driver.wait = WebDriverWait(driver, 15)
            self.swipe_attr = Swiper(driver)
            for i in range(4):
                self.swipe_attr.scroll_down('long')
            driver.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//iframe[starts-with(@name, '__privateStripeFrame') and string-length(@name)=string-length('__privateStripeFrame')+4])[1]"))).send_keys(card_number)
            driver.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//iframe[starts-with(@name, '__privateStripeFrame') and string-length(@name)=string-length('__privateStripeFrame')+4])[2]"))).send_keys(date)
            driver.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "(//iframe[starts-with(@name, '__privateStripeFrame') and string-length(@name)=string-length('__privateStripeFrame')+4])[3]"))).send_keys(cvv)
            try:
                driver.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//section/div[1]/div/div[4]/button'))).click()
                time.sleep(1)
                driver.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//section/div[1]/div/div[4]/button/span'))).click()
            except:
                pass

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            driver.quit()

    def open_app(self, context, app_package, app_activity):
        desired_capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android',
            appPackage=app_package,
            appActivity=app_activity,
            language='en',
            locale='US'
        )

        context.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(desired_capabilities))
        context.wait = WebDriverWait(context.driver, 15)

    def start_screen_recording(self, context, save_path, filename="test_recording.mp4"):
        context.screen_recording_file = os.path.join(save_path, filename)
        command = f"adb shell screenrecord /sdcard/{filename}"
        context.screen_recording_process = subprocess.Popen(command, shell=True)
        print(f"Started screen recording: {filename}")

    def stop_screen_recording(self, context, save_path, filename="test_recording.mp4"):
        context.screen_recording_process.terminate()
        command = f"adb pull /sdcard/{filename} {context.screen_recording_file}"
        subprocess.run(command, shell=True)
        command = f"adb shell rm /sdcard/{filename}"
        subprocess.run(command, shell=True)
        print(f"Stopped screen recording and saved to: {context.screen_recording_file}")
        self.convert_video_to_standard_format(context.screen_recording_file)

    def convert_video_to_standard_format(self, filepath):
        output_file = filepath.replace(".mp4", "_converted.mp4")
        command = f"ffmpeg -i {filepath} -c:v libx264 -preset slow -crf 22 {output_file}"
        subprocess.run(command, shell=True)
        print(f"Converted video saved to: {output_file}")


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
        else:
            raise ValueError("Недопустимое значение для swipe_intensity. Используйте 'short', 'medium' или 'long'.")

    def scroll_down(self, swipe_intensity='medium'):
        size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        starty = size['height'] * start_factor
        endy = size['height'] * end_factor
        startx = size['width'] / 2
        self.context.swipe(startx, starty, startx, endy, 400)

    def scroll_right(self, context, swipe_intensity='medium'):
        size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        startx = self.size['width'] * (1 - start_factor)
        endx = self.size['width'] * start_factor
        starty = self.size['height'] / 2
        self.driver.swipe(startx, starty, endx, starty, 400)

    def scroll_left(self, context, swipe_intensity='medium'):
        self.size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        startx = self.size['width'] * start_factor
        endx = self.size['width'] * (1 - start_factor)
        starty = self.size['height'] / 2
        self.context.swipe(startx, starty, endx, starty, 400)

    def scroll_up(self, context, swipe_intensity='medium'):
        self.size = self.context.get_window_size()
        start_factor, end_factor = self.get_swipe_distance(swipe_intensity)
        starty = self.size['height'] * end_factor
        endy = self.size['height'] * start_factor
        startx = self.size['width'] / 2
        self.context.swipe(startx, starty, startx, endy, 400)
