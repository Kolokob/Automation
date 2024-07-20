import asyncio
import random
import re
import string
import time

import requests
from behave import *
from Steps.steps_api.base_steps import *
from Steps.steps_api.order import *

class Sender:

    def __init__(self, email, password, country):
        self.session_key = None
        self.email = email
        self.password = password
        self.country = country
        self.url = 'https://version4.senpex.com/senpex/restfull/v4'
        self.name = 'Ben'
        self.surname = 'Stone'
        self.cell = '4085154474'
        self.address_actual =  "123"
        self.customer_type = "2"

    def create_sender(self):
        url = f"{self.url}/senderapp/profile"

        headers = {
            "Content-Type": "application/json",
            "log-device-type": "APPLE_PHONE",
            "log-device-id": "123",
            "log-user-argent": "123",
            "log-app-version": "Firefox",
            "log-timezone": "240",
            "country": self.country.lower()
        }

        payload = {
            "name": self.name,
            "surname": self.surname,
            "cell": self.cell,
            "address_actual": self.address_actual,
            "customer_type": self.customer_type,
            "company_name": 'Aradsasadsisaka',
            "email": self.email,
            "password": self.password
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            raise Exception(response.text)
        else:
            try:
                print(response.json()['msgtext'])
            except KeyError:
                print('Successfully created sender')

    def login(self):
        login_url = f"{self.url}/senderapp/authentication/login"

        login_payload = {"email": self.email, "password": self.password}

        headers = {
            "Content-Type": "application/json",
            "log-device-type": "APPLE_PHONE",
            "log-device-id": "123",
            "log-user-argent": "123",
            "log-app-version": "Firefox",
            "log-timezone": "240",
            "country": self.country
        }

        response = requests.put(login_url, json=login_payload, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            self.session_key = json_data['data'][0]['log_session_key']
            print(json_data)
            print('Successfully logged in')
            return self.session_key
        else:
            raise Exception(f"Failed to login: {response.text}")

    def get_token(self):
        token_url = f"{self.url}/senderapp/orders/lastmile/token"

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.session_key,
            "log-device-type": "APPLE_PHONE",
            "log-device-id": "123",
            "log-user-argent": "123",
            "log-app-version": "Firefox",
            "log-timezone": "240",
            "country": self.country
        }

        response = requests.get(token_url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            self.token = json_data['data']['api_token']
        else:
            raise Exception(f"Failed to get token: {response.status_code} - {response.text}")

    def logout(self):
        if not self.session_key:
            raise Exception("You are not logged in")

        url = f"{self.url}/senderapp/authentication/logout"

        delete_payload = {"email": self.email, "password": self.password}

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.session_key,
            "log-device-type": "APPLE_PHONE",
            "log-device-id": "123",
            "log-user-argent": "123",
            "log-app-version": "Firefox",
            "log-timezone": "240",
            "country": self.country
        }

        response = requests.delete(url, json=delete_payload, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            print('Successfully logged out')
        else:
            raise Exception(f"Failed to logout: {response.text}")

    def update_profile(self, name=None, surname=None, cell=None, address_actual=None):
        url = f"{self.url}/senderapp/profile"

        if not self.session_key:
            raise Exception("You are not logged in")

        update_payload = {
            "email": self.email,
            "password": self.password,
            "name": name if name else self.name,
            "surname": surname if surname else self.surname,
            "cell": cell if cell else self.cell,
            "address_actual": address_actual if address_actual else self.address_actual,
            "customer_type": '1'
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": self.session_key,
            "log-device-type": "APPLE_PHONE",
            "log-device-id": "123",
            "log-user-argent": "123",
            "log-app-version": "Firefox",
            "log-timezone": "240",
            "country": self.country
        }

        response = requests.put(url, json=update_payload, headers=headers)
        if response.status_code == 200:
            print('Profile was successfully updated')
        else:
            raise Exception(f"Failed to update profile: {response.text}")

sender = Sender('cybsasder@andrsoid.com', '123456', 'ca')

sender.create_sender()





