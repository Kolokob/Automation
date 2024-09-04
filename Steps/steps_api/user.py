import requests


class Sender:

    def __init__(self, email, password, country):
        self.session_key = None
        self.email = email
        self.password = password
        self.country = country
        self.url = 'https://version4.senpex.com/senpex/restfull/v4'
        self.session = requests.Session()  # Создаем сессию
        self.name = 'Ben'
        self.surname = 'Stone'
        self.cell = '4085154474'
        self.address_actual = "123"
        self.customer_type = "2"
        self.pack_id = 0
        self.active_orders = None

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

        response = self.session.put(login_url, json=login_payload, headers=headers)  # Используем сессию
        if response.status_code == 200:
            json_data = response.json()
            self.session_key = json_data['data'][0]['log_session_key']
            print(f"{self.email} successfully logged in")
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

        response = self.session.get(token_url, headers=headers)  # Используем сессию
        if response.status_code == 200:
            json_data = response.json()
            self.token = json_data['data']['api_token']
            print(f"{self.email} obtained token")
        else:
            raise Exception(f"Failed to get token: {response.status_code} - {response.text}")

    def create_order(self):
        order_url = f"{self.url}/senderapp/orders/lastmile"

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

        payload = {
            "api_token": self.token,
            "send_name": "Last mile - urgent",
            "desc_text": "ok",
            "sender_name": "Sam",
            "sender_cell": "123",
            "ask_sign": "1",
            "pay_type": "5",
            "tip_pay_type": "1",
            "tip_amount": "11",
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

        response = requests.post(order_url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f'Order {response.json()['inserted_id']} has been created successfully')
            return response.json()['inserted_id']
        else:
            raise Exception(f"Failed to create order: {response.status_code} - {response.text}")

    def edit_order(self, order_id):
        edit_order_url = f"{self.url}/senderapp/orders/lastmile/{order_id}"

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

        payload = {
            "api_token": self.token,
            "send_name": "Repeating order",
            "desc_text": "ok",
            "tip_pay_type": 2,
            "tip_amount": 2,
            "sender_name": "Ben Stone",
            "sender_cell": "123",
            "ask_sign": "1",
            "card_last_4": "1243",
            "routes": [
                {
                    "rec_name": "Jack",
                    "rec_phone": "123",
                    "route_desc": "ok"
                },
                {
                    "rec_name": "Jim",
                    "rec_phone": "123",
                    "route_desc": "ok"
                },
                {
                    "rec_name": "Jill",
                    "rec_phone": "123",
                    "route_desc": "ok"
                }
            ]
        }

        response = requests.put(edit_order_url, json=payload, headers=headers)
        if response.status_code == 200:
            print(response.json())
        else:
            raise Exception(f"Failed to edit order: {response.status_code} - {response.text}")

    def get_active_orders(self):
        orders_url = f"{self.url}/senderapp/orders/all/active"

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

        response = self.session.get(orders_url, headers=headers)  # Используем сессию
        if response.status_code == 200:
            self.pack_id = [i['id'] for i in response.json()['data']]
            print(self.pack_id)
            return response.json()['data']

        else:
            raise Exception(f"Failed to get active orders: {response.status_code} - {response.text}")

    def get_chat_conversations(self):
        chat_conversations_url = f"{self.url}/senderapp/chat/conversations"  # Базовый URL без параметров

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

        response = []
        try:
            i = 0
            while True:
                params = {
                    "pack_id": self.pack_id[int(i)],
                    "count": 20,
                    "start": 0
                }
                response.append(self.session.get(chat_conversations_url, params=params, headers=headers).json())
                i += 1
        except IndexError:
            pass

        return response


if __name__ == "__main__":
    user = Sender('test_base@gmail.com', '123456', 'ca')
    user.login()
    user.get_token()
    user.get_active_orders()
    print(user.get_chat_conversations())

# import asyncio
# import aiohttp
# import time
#
# class LinkTester:
#
#     def __init__(self, urls):
#         self.urls = urls
#         self.successful_requests = 0
#         self.failed_requests = 0
#         self.fail_threshold = 10  # Лимит неудачных запросов перед остановкой теста
#
#     async def open_link(self, session, url, link_id):
#         print(f"[DEBUG] Attempting to open link {link_id}: {url}")
#         start_time = time.time()
#
#         try:
#             async with session.get(url) as response:
#                 elapsed_time = time.time() - start_time
#                 if response.status == 200:
#                     self.successful_requests += 1
#                     print(f"[DEBUG] Link {link_id} opened successfully in {elapsed_time:.2f} seconds")
#                 else:
#                     self.failed_requests += 1
#                     print(f"[ERROR] Failed to open link {link_id} in {elapsed_time:.2f} seconds: {response.status}")
#         except Exception as e:
#             elapsed_time = time.time() - start_time
#             self.failed_requests += 1
#             print(f"[ERROR] Exception while opening link {link_id} in {elapsed_time:.2f} seconds: {e}")
#
#         # Check if the number of failed requests exceeds the threshold
#         if self.failed_requests >= self.fail_threshold:
#             print(f"[ERROR] Stopping test after {self.failed_requests} failures.")
#             raise Exception("Too many failed requests.")
#
#     async def open_multiple_links(self, num_requests):
#         async with aiohttp.ClientSession() as session:
#             tasks = []
#             for i in range(num_requests):
#                 for url in self.urls:
#                     tasks.append(self.open_link(session, url, f"{i+1}-{url}"))
#
#             print("[DEBUG] Starting parallel requests")
#             try:
#                 await asyncio.gather(*tasks)
#             except Exception as e:
#                 print(f"[ERROR] Test stopped due to: {e}")
#             finally:
#                 print(f"[DEBUG] Finished processing all requests")
#                 print(f"[DEBUG] Total successful requests: {self.successful_requests}")
#                 print(f"[DEBUG] Total failed requests: {self.failed_requests}")
#
# async def main():
#     urls = [
#         "https://v4-sandbox.senpex.com/how-senpex-works",
#         "https://v4-sandbox.senpex.com/estimate",
#         "https://v4-sandbox.senpex.com/nationwide-delivery",
#         "https://v4-sandbox.senpex.com/moving-delivery-service",
#         "https://v4-sandbox.senpex.com/moving-delivery-service",
#         "https://v4-sandbox.senpex.com/moving-delivery-service",
#         "https://v4-sandbox.senpex.com/transportation-management-system",
#         "https://v4-sandbox.senpex.com/collection-service"
#     ]
#
#     tester = LinkTester(urls)
#
#     print("[DEBUG] Starting test for opening links 100 times simultaneously")
#     await tester.open_multiple_links(100)
#     print("[DEBUG] Test completed")
#
# if __name__ == "__main__":
#     asyncio.run(main())

#
# import aiohttp
# import asyncio
#
# import requests
#
# # Список всех ссылок, по которым нужно пройтись
# links = [
#     "https://v4-sandbox.senpex.com/",
#     "https://v4-sandbox.senpex.com/how-senpex-works",
#     "https://v4-sandbox.senpex.com/estimate/",
#     "https://v4-sandbox.senpex.com/nationwide-delivery",
#     "https://v4-sandbox.senpex.com/moving-delivery-service",
#     "https://v4-sandbox.senpex.com/freight-service",
#     "https://v4-sandbox.senpex.com/multi-route-service",
#     "https://v4-sandbox.senpex.com/transportation-management-system",
#     "https://v4-sandbox.senpex.com/collection-service",
#     "https://v4-sandbox.senpex.com/delivery-service-api",
#     "https://v4-sandbox.senpex.com/last-mile-logistics-consultant",
#     "https://v4-sandbox.senpex.com/retail-delivery-service",
#     "https://v4-sandbox.senpex.com/delivery-service-api",
#     "https://v4-sandbox.senpex.com/food-delivery-services",
#     "https://v4-sandbox.senpex.com/medical-courier-services",
#     "https://v4-sandbox.senpex.com/grocery-delivery-services",
#     "https://v4-sandbox.senpex.com/business-delivery-services",
#     "https://v4-sandbox.senpex.com/catering-delivery",
#     "https://v4-sandbox.senpex.com/contact-senpex",
#     "https://v4-sandbox.senpex.com/become-senpex-courier",
#     "https://v4-sandbox.senpex.com/customer/login",
#     "https://v4-sandbox.senpex.com/customer/sign-up",
#     "https://v4-sandbox.senpex.com/business-delivery-services",
#     "https://v4-sandbox.senpex.com/personal-courier-service",
#     "https://v4-sandbox.senpex.com/moving-delivery-service",
#     "https://v4-sandbox.senpex.com/incognito-delivery",
#     "https://v4-sandbox.senpex.com/food-delivery-services",
#     "https://v4-sandbox.senpex.com/electronics-hardware-delivery",
#     "https://v4-sandbox.senpex.com/legal-documents-delivery",
#     "https://v4-sandbox.senpex.com/airport-luggage-delivery",
#     "https://v4-sandbox.senpex.com/auto-parts-delivery",
#     "https://v4-sandbox.senpex.com/flowers-delivery",
#     "https://v4-sandbox.senpex.com/catering-delivery",
#     "https://v4-sandbox.senpex.com/medical-courier-services",
#     "https://v4-sandbox.senpex.com/healthcare-delivery-services",
#     "https://v4-sandbox.senpex.com/retail-delivery-service",
#     "https://v4-sandbox.senpex.com/furniture-delivery-service",
#     "https://v4-sandbox.senpex.com/grocery-delivery-services",
#     "https://v4-sandbox.senpex.com/delivery-service-api",
#     "https://v4-sandbox.senpex.com/collection-service",
#     "https://documenter.getpostman.com/view/9662282/TW73Fkyi",
#     "https://v4-sandbox.senpex.com/t2",
#     "https://v4-sandbox.senpex.com/multi-route-service",
#     "https://v4-sandbox.senpex.com/list-of-cities-delivered",
#     "https://v4-sandbox.senpex.com/list-of-universities-delivered",
#     "https://v4-sandbox.senpex.com/list-of-destinations",
#     "https://v4-sandbox.senpex.com/become-senpex-courier",
#     "https://v4-sandbox.senpex.com/careers",
#     "https://v4-sandbox.senpex.com/partners-local-b2b-courier-services",
#     "https://v4-sandbox.senpex.com/about-senpex",
#     "https://v4-sandbox.senpex.com/contact-senpex",
#     "https://v4-sandbox.senpex.com/blog",
#     "https://v4-sandbox.senpex.com/faq-senpex",
#     "https://v4-sandbox.senpex.com/files/COI-Senpex.pdf",
#     "https://v4-sandbox.senpex.com/privacy-policy",
#     "https://v4-sandbox.senpex.com/cookies-policy",
#     "https://v4-sandbox.senpex.com/terms-of-service",
#     "https://v4-sandbox.senpex.com/blog",
#     "https://v4-sandbox.senpex.com/business-delivery-services",
#     "https://v4-sandbox.senpex.com/personal-courier-service",
#     "https://v4-sandbox.senpex.com/moving-delivery-service",
#     "https://v4-sandbox.senpex.com/incognito-delivery",
#     "https://v4-sandbox.senpex.com/food-delivery-services",
#     "https://v4-sandbox.senpex.com/electronics-hardware-delivery",
#     "https://v4-sandbox.senpex.com/legal-documents-delivery",
#     "https://v4-sandbox.senpex.com/airport-luggage-delivery",
#     "https://v4-sandbox.senpex.com/auto-parts-delivery",
#     "https://v4-sandbox.senpex.com/flowers-delivery",
#     "https://v4-sandbox.senpex.com/catering-delivery",
#     "https://v4-sandbox.senpex.com/medical-courier-services",
#     "https://v4-sandbox.senpex.com/healthcare-delivery-services",
#     "https://v4-sandbox.senpex.com/retail-delivery-service",
#     "https://v4-sandbox.senpex.com/furniture-delivery-service",
#     "https://v4-sandbox.senpex.com/grocery-delivery-services",
#     "https://v4-sandbox.senpex.com/delivery-service-api",
#     "https://v4-sandbox.senpex.com/collection-service",
#     "https://documenter.getpostman.com/view/9662282/TW73Fkyi",
#     "https://v4-sandbox.senpex.com/t2",
#     "https://v4-sandbox.senpex.com/multi-route-service",
#     "https://v4-sandbox.senpex.com/list-of-cities-delivered",
#     "https://v4-sandbox.senpex.com/list-of-universities-delivered",
#     "https://v4-sandbox.senpex.com/list-of-destinations",
#     "https://v4-sandbox.senpex.com/become-senpex-courier",
#     "https://v4-sandbox.senpex.com/careers",
#     "https://v4-sandbox.senpex.com/partners-local-b2b-courier-services",
#     "https://v4-sandbox.senpex.com/about-senpex",
#     "https://v4-sandbox.senpex.com/contact-senpex",
#     "https://v4-sandbox.senpex.com/blog",
#     "https://v4-sandbox.senpex.com/faq-senpex",
#     "https://v4-sandbox.senpex.com/files/COI-Senpex.pdf",
#     "https://v4-sandbox.senpex.com/privacy-policy",
#     "https://v4-sandbox.senpex.com/cookies-policy",
#     "https://v4-sandbox.senpex.com/terms-of-service",
# ]
#
# # Счетчики успешных и заблокированных запросов
# success_count = 0
# blocked_count = 0
#
# async def fetch(session, url):
#     global success_count, blocked_count
#     try:
#         async with session.get(url, timeout=10) as response:  # Добавляем тайм-аут на запрос
#             status = response.status
#             if status == 200:
#                 print(f"Visited {url} - Status code: {status}")
#                 success_count += 1
#             else:
#                 print(f"Blocked at {url} - Status code: {status}")
#                 blocked_count += 1
#     except asyncio.TimeoutError:
#         print(f"Request to {url} timed out.")
#         blocked_count += 1
#     except Exception as e:
#         print(f"Error visiting {url}: {e}")
#         blocked_count += 1
#
# async def run():
#     timeout = aiohttp.ClientTimeout(total=60)  # Общий тайм-аут для всех запросов в клиенте
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         tasks = []
#
#         # Отправляем 60 запросов одновременно
#         for i in range(60):
#             url = links[i % len(links)]
#             tasks.append(fetch(session, url))
#
#         await asyncio.gather(*tasks)
#         print(f"After 60 requests: Successful: {success_count}, Blocked: {blocked_count}")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())
#
# # Финальная статистика
# print(f"Total successful requests: {success_count}")
# print(f"Total blocked requests: {blocked_count}")