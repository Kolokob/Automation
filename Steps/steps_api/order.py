import requests

class SenpexAPI:
    BASE_URL = "https://version4.senpex.com/senpex/restfull/v4//senderapp"
    CLIENT_ID = "c322dc7cb6a3abbe58f2182435cc9870"
    SECRET_ID = "299D35C9-6307-4CE1-8EFC-52130149692C2024081622360"
    GOOGLE_MAPS_API_KEY = "AIzaSyDK9PPCaZZu1UtrWciVDIRejHR0YW9AbkA"
    DEVICE_TYPE = "APPLE_PHONE"
    DEVICE_ID = "123"
    USER_AGENT = "Firefox"
    TIMEZONE = "240"

    def __init__(self, email, password, country):
        self.email = email
        self.password = password
        self.country = country
        self.session_key = self.login_and_get_session_key()
        self.api_token = self.get_token()

    def login_and_get_session_key(self):
        login_url = f"{self.BASE_URL}/authentication/login"
        login_payload = {
            "email": self.email,
            "password": self.password
        }
        headers = self._get_headers()

        response = requests.put(login_url, json=login_payload, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            return json_data['data'][0]['log_session_key']
        else:
            raise Exception(f"Failed to login: {response.text}")

    def get_token(self):
        token_url = f"{self.BASE_URL}/orders/lastmile/token"
        headers = self._get_headers(authorization=self.session_key)

        response = requests.get(token_url, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            return json_data.get('data').get('api_token')
        else:
            raise Exception(f"Failed to get token: {response.status_code} - {response.text}")

    def create_order(self):
        url = f"{self.BASE_URL}/orders/lastmile"
        payload = {
            "api_token": self.api_token,
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
                {"rec_name": "Abc", "rec_phone": "123", "route_desc": "ok"},
                {"rec_name": "Def", "rec_phone": "123", "route_desc": "ok"},
                {"rec_name": "Ghi", "rec_phone": "123", "route_desc": "ok"}
            ]
        }
        headers = self._get_headers(authorization=self.session_key)

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            if json_data.get('code') == '0':
                print(f"Order created successfully. Order number: {json_data.get('inserted_id')}")
            else:
                print(f"Failed to create order: {json_data}")
        else:
            print(f"HTTP error occurred: {response.status_code} - {response.text}")

    def add_credit_card(self):
        url = f"{self.BASE_URL}/profile/cards"
        payload = {"stripeToken": "tok_1NG8PVDsDVygPhtytugvN2gc"}
        headers = self._get_headers(authorization=self.session_key)

        response = requests.get(url, headers=headers, json=payload)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            raise Exception(f"Failed to add credit card: {response.status_code} - {response.text}")

    def _get_headers(self, authorization=None):
        headers = {
            "Content-Type": "application/json",
            "log-device-type": self.DEVICE_TYPE,
            "log-device-id": self.DEVICE_ID,
            "log-user-argent": "123",
            "log-app-version": self.USER_AGENT,
            "log-timezone": self.TIMEZONE,
            "country": self.country
        }
        if authorization:
            headers["Authorization"] = authorization
        return headers

    def get_dropoff_quote(self):
        url = f"{self.BASE_URL}/orders/dropoff/quote"
        headers = {
            "secretid": self.SECRET_ID,
            "clientid": self.CLIENT_ID,
            "Country": 'us'
        }
        payload = {
            "email": self.email,
            **self.order_details
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get dropoff quote: {response.status_code} - {response.text}")





# Example usage
email = "gordon.ramzy@gmail.com"
password = "123456Aa"
country = "us"

senpex_api = SenpexAPI(email, password, country)
# senpex_api.create_order()
print(senpex_api.add_credit_card())

# outA7D61816-C3C3-4882-A2B0-85017FE946022023101216540

# import scrapy
#
# class MySpider(scrapy.Spider):
#     name = 'myspider'
#     allowed_domains = ['v4-sandbox.senpex.com']
#
#     # Список ссылок
#     custom_links = [
#         "https://v4-sandbox.senpex.com/",
#         "https://v4-sandbox.senpex.com/how-senpex-works",
#         "https://v4-sandbox.senpex.com/estimate/",
#         "https://v4-sandbox.senpex.com/nationwide-delivery",
#         "https://v4-sandbox.senpex.com/moving-delivery-service",
#         "https://v4-sandbox.senpex.com/freight-service",
#         "https://v4-sandbox.senpex.com/multi-route-service",
#         "https://v4-sandbox.senpex.com/transportation-management-system",
#         "https://v4-sandbox.senpex.com/collection-service",
#         "https://v4-sandbox.senpex.com/delivery-service-api",
#         "https://v4-sandbox.senpex.com/last-mile-logistics-consultant",
#         "https://v4-sandbox.senpex.com/retail-delivery-service",
#         "https://v4-sandbox.senpex.com/delivery-service-api",
#         "https://v4-sandbox.senpex.com/food-delivery-services",
#         "https://v4-sandbox.senpex.com/medical-courier-services",
#         "https://v4-sandbox.senpex.com/grocery-delivery-services",
#         "https://v4-sandbox.senpex.com/business-delivery-services",
#         "https://v4-sandbox.senpex.com/catering-delivery",
#         "https://v4-sandbox.senpex.com/contact-senpex",
#         "https://v4-sandbox.senpex.com/become-senpex-courier",
#         "https://v4-sandbox.senpex.com/customer/login",
#         "https://v4-sandbox.senpex.com/customer/sign-up",
#         "https://v4-sandbox.senpex.com/business-delivery-services",
#         "https://v4-sandbox.senpex.com/personal-courier-service",
#         "https://v4-sandbox.senpex.com/moving-delivery-service",
#         "https://v4-sandbox.senpex.com/incognito-delivery",
#         "https://v4-sandbox.senpex.com/food-delivery-services",
#         "https://v4-sandbox.senpex.com/electronics-hardware-delivery",
#         "https://v4-sandbox.senpex.com/legal-documents-delivery",
#         "https://v4-sandbox.senpex.com/airport-luggage-delivery",
#         "https://v4-sandbox.senpex.com/auto-parts-delivery",
#         "https://v4-sandbox.senpex.com/flowers-delivery",
#         "https://v4-sandbox.senpex.com/catering-delivery",
#         "https://v4-sandbox.senpex.com/medical-courier-services",
#         "https://v4-sandbox.senpex.com/healthcare-delivery-services",
#         "https://v4-sandbox.senpex.com/retail-delivery-service",
#         "https://v4-sandbox.senpex.com/furniture-delivery-service",
#         "https://v4-sandbox.senpex.com/grocery-delivery-services",
#         "https://v4-sandbox.senpex.com/delivery-service-api",
#         "https://v4-sandbox.senpex.com/collection-service",
#         "https://documenter.getpostman.com/view/9662282/TW73Fkyi",
#         "https://v4-sandbox.senpex.com/t2",
#         "https://wordpress.org/plugins/senpex-on-demand-delivery/",
#         "https://v4-sandbox.senpex.com/multi-route-service",
#         "https://v4-sandbox.senpex.com/list-of-cities-delivered",
#         "https://v4-sandbox.senpex.com/list-of-universities-delivered",
#         "https://v4-sandbox.senpex.com/list-of-destinations",
#         "https://v4-sandbox.senpex.com/become-senpex-courier",
#         "https://v4-sandbox.senpex.com/careers",
#         "https://v4-sandbox.senpex.com/partners-local-b2b-courier-services",
#         "https://v4-sandbox.senpex.com/about-senpex",
#         "https://v4-sandbox.senpex.com/contact-senpex",
#         "https://v4-sandbox.senpex.com/blog",
#         "https://v4-sandbox.senpex.com/faq-senpex",
#         "https://v4-sandbox.senpex.com/files/COI-Senpex.pdf",
#         "https://v4-sandbox.senpex.com/privacy-policy",
#         "https://v4-sandbox.senpex.com/cookies-policy",
#         "https://v4-sandbox.senpex.com/terms-of-service",
#         "https://www.facebook.com/senpex.usa/",
#         "https://www.instagram.com/senpex.usa/",
#         "https://twitter.com/senpexusa",
#         "https://www.youtube.com/channel/UCRouVBuQSt2iZdOWziNJVoA",
#         "https://www.linkedin.com/company/senpex/",
#         "https://www.ezcater.com",
#         "https://www.harbor-electronics.com",
#         "https://tesla.com",
#         "https://rigetti.com",
#         "https://facebook.com",
#         "https://getmagic.com",
#         "https://iesupply.com",
#         "https://sweetgreen.com",
#         "https://xppower.com",
#         "https://covalentmetrology.com",
#         "https://samsungnext.com",
#         "https://twistbioscience.com",
#         "https://cfcsoakland.org",
#         "https://swopedesignsolutions.com",
#         "https://thehalalguys.com",
#         "https://apps.apple.com/us/app/senpex-client/id1276028389",
#         "https://play.google.com/store/apps/details?id=com.snpx.customer",
#         "https://v4-sandbox.senpex.com/blog",
#         "https://ceoweekly.com/the-biggest-delivery-problems-facing-businesses-and-how-shortcomings-can-be-addressed/",
#         "https://insidebigdata.com/2022/06/14/artificial-intelligence-data-analytics-in-the-last-mile-logistics/",
#         "https://www.forbes.com/sites/forbestechcouncil/2024/05/06/navigating-the-complexities-of-last-mile-logistics-challenges-and-solutions/?sh=c64b59142c99",
#         "https://nyweekly.com/tech/how-ai-powered-route-optimization-is-improving-delivery-times-for-couriers-and-delivery-drivers/",
#         "https://www.techtimes.com/articles/277691/20220706/changes-in-technology-are-moving-medicine-into-the-post-covid-era.htm",
#         "https://techbullion.com/senpex-sees-deliveries-for-businesses-through-the-last-mile/",
#         "https://v4-sandbox.senpex.com/business-delivery-services",
#         "https://v4-sandbox.senpex.com/personal-courier-service",
#         "https://v4-sandbox.senpex.com/moving-delivery-service",
#         "https://v4-sandbox.senpex.com/incognito-delivery",
#         "https://v4-sandbox.senpex.com/food-delivery-services",
#         "https://v4-sandbox.senpex.com/electronics-hardware-delivery",
#         "https://v4-sandbox.senpex.com/legal-documents-delivery",
#         "https://v4-sandbox.senpex.com/airport-luggage-delivery",
#         "https://v4-sandbox.senpex.com/auto-parts-delivery",
#         "https://v4-sandbox.senpex.com/flowers-delivery",
#         "https://v4-sandbox.senpex.com/catering-delivery",
#         "https://v4-sandbox.senpex.com/medical-courier-services",
#         "https://v4-sandbox.senpex.com/healthcare-delivery-services",
#         "https://v4-sandbox.senpex.com/retail-delivery-service",
#         "https://v4-sandbox.senpex.com/furniture-delivery-service",
#         "https://v4-sandbox.senpex.com/grocery-delivery-services",
#         "https://v4-sandbox.senpex.com/delivery-service-api",
#         "https://v4-sandbox.senpex.com/collection-service",
#         "https://documenter.getpostman.com/view/9662282/TW73Fkyi",
#         "https://v4-sandbox.senpex.com/t2",
#         "https://wordpress.org/plugins/senpex-on-demand-delivery/",
#         "https://v4-sandbox.senpex.com/multi-route-service",
#         "https://v4-sandbox.senpex.com/list-of-cities-delivered",
#         "https://v4-sandbox.senpex.com/list-of-universities-delivered",
#         "https://v4-sandbox.senpex.com/list-of-destinations",
#         "https://v4-sandbox.senpex.com/become-senpex-courier",
#         "https://v4-sandbox.senpex.com/careers",
#         "https://v4-sandbox.senpex.com/partners-local-b2b-courier-services",
#         "https://v4-sandbox.senpex.com/about-senpex",
#         "https://v4-sandbox.senpex.com/contact-senpex",
#         "https://v4-sandbox.senpex.com/blog",
#         "https://v4-sandbox.senpex.com/faq-senpex",
#         "https://v4-sandbox.senpex.com/files/COI-Senpex.pdf",
#         "https://v4-sandbox.senpex.com/privacy-policy",
#         "https://v4-sandbox.senpex.com/cookies-policy",
#         "https://v4-sandbox.senpex.com/terms-of-service",
#         "https://www.facebook.com/senpex.usa/",
#         "https://www.instagram.com/senpex.usa/",
#         "https://twitter.com/senpexusa",
#         "https://www.youtube.com/channel/UCRouVBuQSt2iZdOWziNJVoA",
#         "https://www.linkedin.com/company/senpex/"
#     ]
#
#     def start_requests(self):
#         # Цикл для повторного обхода ссылок 150 раз
#         for i in range(150):
#             for link in self.custom_links:
#                 yield scrapy.Request(url=link, callback=self.parse, dont_filter=True)
#
#     def parse(self, response):
#         self.log(f"Visited {response.url}")
#         # Здесь вы можете добавить обработку контента страницы, если необходимо
