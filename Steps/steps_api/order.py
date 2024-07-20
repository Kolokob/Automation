import random
import re
import string
import requests
from behave import *
import requests
from Steps.steps_api.base_steps import *


def login_and_get_session_key(email, password, country):
    login_url = "https://version4.senpex.com/senpex/restfull/v4//senderapp/authentication/login"
    login_payload = {
        "email": email,
        "password": password
    }

    headers = {
        "Content-Type": "application/json",
        "log-device-type": "APPLE_PHONE",
        "log-device-id": "123",
        "log-user-argent": "123",
        "log-app-version": "Firefox",
        "log-timezone": "240",
        "country": country
    }

    response = requests.put(login_url, json=login_payload, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        return json_data['data'][0]['log_session_key']
    else:
        raise Exception(f"Failed to login: {response.text}")

def get_token(email, password, country):
    token_url = "https://version4.senpex.com/senpex/restfull/v4//senderapp/orders/lastmile/token"

    headers = {
        "Content-Type": "application/json",
        "Authorization": login_and_get_session_key(email, password, country),
        "log-device-type": "APPLE_PHONE",
        "log-device-id": "123",
        "log-user-argent": "123",
        "log-app-version": "Firefox",
        "log-timezone": "240",
        "country": country
    }

    response = requests.get(token_url, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        return json_data.get('data').get('api_token')
    else:
        raise Exception(f"Failed to get token: {response.status_code} - {response.text}")

@then('I login into account "{email}", "{password}" in "{country}" and create an order')
def create_order(context, email, password, country):
    url = "https://version4.senpex.com/senpex/restfull/v4//senderapp/orders/lastmile"

    api_token = get_token(email, password, country)
    auth = login_and_get_session_key(email, password, country)

    payload = {
        "api_token": api_token,
        "send_name": "Last mile",
        "desc_text": "ok",
        "sender_name": "Sam",
        "sender_cell": "123",
        "ask_sign": "1",
        "pay_type": "3",
        "tip_pay_type": "1",
        "tip_amount": "11",
        "card_last_4": 4242,
        "stripeToken": "tok_visa",
        "routes": [
            {
                "rec_name": "Abc",
                "rec_phone": "123",
                "route_desc": "ok"
            },
            {
                "rec_name": "Def",
                "rec_phone": "123",
                "route_desc": "ok"
            },
            {
                "rec_name": "Ghi",
                "rec_phone": "123",
                "route_desc": "ok"
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.40.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Authorization": auth,
        "log-device-type": "APPLE_PHONE",
        "log-device-id": "123",
        "log-user-argent": "123",
        "log-app-version": "Firefox",
        "log-timezone": "240",
        "country": 'ca'
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        json_data = response.json()
        if json_data.get('code') == '0':
            print(f"Order created successfully. Order number: {json_data.get('inserted_id')}")
        else:
            print(f"Failed to create order: {json_data}")
    else:
        print(f"HTTP error occurred: {response.status_code} - {response.text}")

@then('I add credit card as "{email}", "{password}" in "{country}"')
def add_credit_card(context, email, password, country):
    url = 'https://version4.senpex.com/senpex/restfull/v4//senderapp/profile/cards'

    headers = {
        "Content-Type": "application/json",
        "Authorization": login_and_get_session_key(email, password, country),
        "log-device-type": "APPLE_PHONE",
        "log-device-id": "123",
        "log-user-argent": "123",
        "log-app-version": "Firefox",
        "log-timezone": "240",
        "country": 'ca'
    }

    payload = {
        "stripeToken": "tok_1NG8PVDsDVygPhtytugvN2gc"
    }


    response = requests.get(url, headers=headers, json=payload)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        raise Exception(f"Failed to add credit card: {response.status_code} - {response.text}")


