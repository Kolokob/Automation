import unittest
import pickle
import json
from pathlib import Path
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Убедитесь, что путь к chromedriver правильный
service = Service(executable_path='/opt/homebrew/bin/chromedriver')
options = Options()

user_data_dir = '/Users/kolokob/Library/Application Support/Google/Chrome/Default'
options.add_argument(f"--user-data-dir={user_data_dir}")

pages = {'login_page': 'https://v4-sandbox.senpex.com/customer/login',
         'register_page': 'https://v4-sandbox.senpex.com/customer/sign-up',
         'main_page': 'https://v4-sandbox.senpex.com/',}

class BaseFixture:
    def setUp(self, context, page):
        context.browser = webdriver.Chrome(service=service, options=options)
        context.browser.get(pages[page])

        context.wait = WebDriverWait(context.browser, 5)
        context.size = {'small': 1, 'medium': 2, 'large': 3, 'heavy_load': 5, 'custom_size': 6}
        context.timing = {'urgent': 1, "schedule_a_pick-up": 2, "repeated_weekly": 3}
        context.extra_services = {'Furniture Assembly and Disassembly': 1, 'Ladder': 2, 'Food Catering Setup': 3,
                               'Blankets': 4, 'White gloves service': 5, 'Waiting on the line': 6,
                               'Temperature Controlled Coolers': 7, 'Special Handling': 8, 'Personal Shopper': 9,
                               'Ratchet Straps': 10, 'Loading Ramps': 11, 'Hand Truck': 12, 'Applience Dolly': 13, 'Packing and Unpacking': 14}
        context.get_key = lambda d, value: next((k for k, v in d.items() if v == value), None)
        context.payment_methods = {'Credit Card': 1, 'Existing Credit Card': 2, 'Create a payment link': 3}
        context.months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def tearDown(self, context):
        context.browser.quit()

    def click_element_with_retry(self, context, xpath, wait_time=15, max_attempts=5):
        try:
            context.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            return True
        except:
            attempts = 0
            while attempts < max_attempts:
                try:
                    context.browser.find_element(By.XPATH, xpath).click()
                    return True
                except:
                    attempts += 1
        return False

    def choose_vehicle_type(self, context, vehicle_type:str):
        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//p[contains(text(), '{vehicle_type}')]"))).click()

    def put_info_for_custom_size(self, context, dimensions):
        for i in range(1, 5):
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//input[contains(@placeholder, 'Please enter')])[{i}]"))).send_keys(dimensions[i-1])

    def check_day(self, context, date_to_check):
        try:
            reference_day = context.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//td[@class='cell today']"))).text
        except:
            return
        date = date_to_check[0]
        return date == reference_day

    def check_month(self, context, date_to_check):
        month_abbr_to_num = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}

        ref_month_num = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-current-month']"))).text
        reference_month = month_abbr_to_num[ref_month_num]
        date = date_to_check.removeprefix('0')
        return int(date) == int(reference_month)

    def check_year(self, context, date_to_check):
        reference_year = context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'20')]"))).text
        return date_to_check == reference_year

    def put_all_info_for_repeated_order(self, context, days, time, date):
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Repeated weekly')]"))).click()
        context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@placeholder, 'Repeated start date')]"))).click()
        while True:
            if self.check_year(context, date.split()):
                break
            else:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-icon-double-right']"))).click()

        while True:
            if self.check_month(context, days[1]):
                break
            else:
                context.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='mx-btn mx-btn-text mx-btn-icon-right']"))).click()
        if not self.check_day(context, days[0]):
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{days[0].removeprefix('0')}')]"))).click()

        current_pm_am = context.wait.until(EC.element_to_be_clickable((By.XPATH, f"(//li[@class='mx-time-item active'])[2]"))).text

        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{time[:2]}')]"))).click()
        context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{round(int(time[3:5]) / 10) * 10}')]"))).click()
        if current_pm_am != time[-2:]:
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(),'{time[-2:]}')]"))).click()

        self.select_days_for_repeated_order(context, days[0], time)

    def select_days_for_repeated_order(self, context, days_or_date, time):
        time = time.split(', ')
        counter = 0
        for i in days_or_date[0].split(', '):
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{i}')]"))).click()
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='fd-select wk-hour'][not(@disabled='disabled')]/option[contains(text(), '{str(time[counter][:2]).removeprefix('0')}')]"))).click()
            context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='fd-select wk-minutes'][not(@disabled='disabled')]/option[contains(text(), '{time[counter][3:5]}')]"))).click()
            if 'pm' in time[counter][3:5]:
                current_pm_am = context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='fd-select wk-am-pm'][not(@disabled='disabled')]")))
                if current_pm_am.text != time[counter][-2:].lower():
                    current_pm_am.click()
                    context.wait.until(EC.element_to_be_clickable((By.XPATH, f"//select[@class='fd-select wk-am-pm'][not(@disabled='disabled')]/option[contains(text(), '{time[counter][-2:].lower()}')]"))).click()
            counter += 1


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
