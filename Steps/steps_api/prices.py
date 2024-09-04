import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed

class Sender:

    def __init__(self, email, password, country):
        self.session_key = None
        self.email = email
        self.password = password
        self.country = country
        self.url = 'https://version4.senpex.com/senpex/restfull/v4'
        self.token = None

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
            print(f"Token retrieved: {self.token}")
        else:
            raise Exception(f"Failed to get token: {response.status_code} - {response.text}")

    def process_price(self, row):
        getprice_url = f"{self.url}/senderapp/orders/lastmile/quote"

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

        row['min_distance'] = 1 if row['min_distance'] == 0 else row['min_distance']

        data = {
            "custom_weight": "26",
            "route_work_type": "2",
            "extra_services": [],
            "helper_count": "0",
            "promo_code": "",
            "schedule_date": "2023-11-16 04:32:39",
            "pack_from_apt": "342",
            "repeated": {
                "day4": {"hour": "00", "min": "00", "yes": "0"},
                "day2": {"hour": "00", "min": "00", "yes": "0"},
                "day6": {"hour": "00", "min": "00", "yes": "0"},
                "day5": {"hour": "00", "min": "00", "yes": "0"},
                "day1": {"hour": "00", "min": "00", "yes": "0"},
                "day7": {"hour": "00", "min": "00", "yes": "0"},
                "day3": {"hour": "00", "min": "00", "yes": "0"}
            },
            "pack_size_id": str(row['pack_size_id']),
            "pack_from_lat": 37.352671,
            "pack_from_lng": -122.024975,
            "driver_count": "1",
            "distance": row['min_distance'],
            "custom_length": "55",
            "pack_from_text": "668 Picasso Trl, Sunnyvale, CA 94087, USA",
            "distance_time": "300",
            "transport_id": str(row['transport_id']),
            "custom_height": "40",
            "repeated_start_date": "",
            "schedule_type": "1",
            "api_token": self.token,
            "routes": [
                {
                    "route_to_lat": 37.774929,
                    "route_distance_time": "300",
                    "route_to_text": "San Francisco, CA, USA",
                    "route_distance": row['max_distance'],
                    "route_to_apt": "344",
                    "route_to_lng": -122.419418,
                    "route_work_type": "0"
                }
            ],
            "pack_timezone": "240",
            "item_value": "0",
            "custom_width": "55"
        }

        response = requests.put(getprice_url, json=data, headers=headers)

        if response.status_code == 200:
            pack_price = response.json()['data']['payment_list']['pack_price']

            if row['min_distance'] >= 20:
                expected_price = row['customer_price'] + (row['customer_coof'] * row['min_distance'])
            else:
                expected_price = row['customer_price']

            if float(pack_price) == float(round(expected_price, 2)):
                print("Prices match!")
            else:
                print(f"Debug - customer_coof: {row['customer_coof']}, customer_price: {row['customer_price']}, distance: {row['min_distance']}")
                print(f"Size: {row['pack_size_id']}, Distance: {row['min_distance']} miles, Vehicle: {row['transport_id']}, API Price: {pack_price}, Expected Price: {round(expected_price, 2)}")
                print("Prices do not match!")
        else:
            print(f"Failed to get price for row: {response.status_code} - {response.text}")

    def get_price(self, df):
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(self.process_price, row) for index, row in df.iterrows()]
            for future in as_completed(futures):
                future.result()

sender = Sender('sonne@gmail.com', '123456', 'us')

sender.login()
sender.get_token()

file_path = '/Users/kolokob/Desktop/prices.xlsx'
df = pd.read_excel(file_path, sheet_name='expdata 1')

sender.get_price(df)
for i in range(1000):
    sender.get_price(df)



# file_path = '/Users/kolokob/Desktop/prices.xlsx'