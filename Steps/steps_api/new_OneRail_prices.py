import requests
import json


# Функция для вычисления объема
def calculate_volume(length, width, height, custom_quantity):
    return length * width * height * custom_quantity


# Функция для нахождения подходящей транспортной категории с коэффициентами
def find_transport_category(length, width, height, weight, volume):
    transport_categories = [
        {"Transport": "Car",            "Length": 20, "Width": 12, "Height": 8, "Weight": 394, "Volume": 1000.00, "Cub coof": 0.000360, "Weight coof": 0.378900, "Driver profit %": 60.0, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "10ft Box Truck", "Length": 24, "Width": 16, "Height": 12, "Weight": 591, "Volume": 6000.00, "Cub coof": 0.000270, "Weight coof": 0.454680, "Driver profit %": 50.00, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "SUV",            "Length": 35, "Width": 24, "Height": 16, "Weight": 787, "Volume": 2000.00, "Cub coof": 0.000180, "Weight coof": 0.585000, "Driver profit %": 60.00, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "9ft Ref Van",    "Length": 45, "Width": 26, "Height": 21, "Weight": 1575, "Volume": 4000.00, "Cub coof": 0.000090, "Weight coof": 0.636552, "Driver profit %": 50.00, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "15ft Box Truck", "Length": 43, "Width": 30, "Height": 28, "Weight": 1181, "Volume": 7000.00, "Cub coof": 0.000036, "Weight coof": 1.212480, "Driver profit %": 50.00, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "17ft Box Truck", "Length": 47, "Width": 28, "Height": 24, "Weight": 1575, "Volume": 8000.00, "Cub coof": 0.000045, "Weight coof": 0.727488, "Driver profit %": 50.00, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "Pickup Truck",   "Length": 71, "Width": 37, "Height": 34, "Weight": 2559, "Volume": 3000.00, "Cub coof": 0.000023, "Weight coof": 0.947250, "Driver profit %": 50.00, "Base Price": 20.00, "Customer Coof": 0.50},
        {"Transport": "9ft Cargo Van",  "Length": 80, "Width": 37, "Height": 34, "Weight": 2756, "Volume": 115000.00, "Cub coof": 0.000023, "Weight coof": 1.041975, "Driver profit %": 50.00, "Base Price": 20.00, "Customer Coof": 0.50}
    ]
    for category in transport_categories:
        if (length <= category["Length"] and
                width <= category["Width"] and
                height <= category["Height"] and
                weight * 5 <= category["Weight"] and
                volume <= category["Volume"]):
            return category
    return None


# Функция для расчета пользовательских значений
def calculate_custom_values(items):
    custom_weight = sum(item["weight"] * item["quantity"] for item in items)
    custom_length = max(item["length"] for item in items)
    custom_width = max(item["width"] for item in items)
    custom_height = max(item["height"] for item in items)
    custom_quantity = max(item["quantity"] for item in items)

    return custom_weight, custom_length, custom_width, custom_height, custom_quantity


# Функция для расчета конечной стоимости
def calculate_total_price(length, width, height, weight, distance_miles, quantity):
    # Вычисляем объем
    volume = calculate_volume(length, width, height, custom_quantity)

    # Ищем подходящую транспортную категорию
    category = find_transport_category(length, width, height, weight, volume)

    if category:
        # Извлекаем коэффициенты и базовую цену
        cub_coof = category["Cub coof"]
        weight_coof = category["Weight coof"]
        base_price = category["Base Price"]
        customer_coof = category["Customer Coof"]

        # Рассчитываем цену
        volume_cost = cub_coof * volume
        weight_cost = weight_coof * (weight * quantity)
        customer_price = base_price + (distance_miles * customer_coof)

        # Конечная цена
        total_price = volume_cost + weight_cost + customer_price
        return total_price, category["Transport"]
    else:
        return None, "No suitable transport found"


# Пример элементов (из ваших данных)
items = [
    {
        "description": "Laptop",
        "quantity": 5,
        "length": 20.02,
        "width": 11.06,
        "height": 16.54,
        "weight": 30.06
    }
]

# Вычисляем пользовательские значения
custom_weight, custom_length, custom_width, custom_height, custom_quantity = calculate_custom_values(items)

# Вычисляем объем
custom_volume = calculate_volume(custom_length, custom_width, custom_height, custom_quantity)

# Ищем подходящую транспортную категорию
distance_miles = 36.05  # Пример расстояния из ответа API
total_price, transport_category = calculate_total_price(custom_length, custom_width, custom_height, custom_weight,
                                                        distance_miles, quantity=5)

print(f"Calculated Weight: {custom_weight}")
print(f"Calculated Length: {custom_length}")
print(f"Calculated Width: {custom_width}")
print(f"Calculated Height: {custom_height}")
print(f"Calculated Volume: {custom_volume}")
print(f"Suitable Transport Category: {transport_category}")
print(f"Calculated Total Price: {total_price:.8f}")

# Отправка данных в API
payload = {
    "order_name": "Delivery Order",
    "taken_asap": 1,
    "transport_id": 1,  # Здесь можно заменить на ID подходящей категории
    "item_value": 1000,
    "pack_size_id": 1,
    "promo_code": "v4",
    "pack_from_text": "1001 Brannan St, San Francisco, CA 94103, United States",
    "client_id": "67e9deb369a750737cd8acb7876ac720",  # Пример client_id
    "secret_id": "05B9D2E4-6741-426A-9F33-105AAB278D182024091323550",  # Пример secret_id
    "use_optimization": 1,
    "items": items,
    "routes": [
        {
            "route_to_text": "350 Newpark Mall Rd, Newark, CA 94560",
            "rec_name": "John",
            "rec_phone": "1002003000"
        }
    ]
}

url = "https://api.sandbox.senpex.com/api/rest/v2/get_price"
headers = {
    "Content-Type": "application/json",
    "Postman-Token": "<calculated when request is sent>",
    "User-Agent": "PostmanRuntime/7.42.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Country": "us"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    response_data = response.json()

    api_details = response_data.get('details', [{}])[0]

    api_total_price = float(api_details.get('order_price', 0))

    if api_total_price is not None:
        print(f"API Total Price: {api_total_price:.8f}")

        # Сравнение рассчитанной цены с данными API
        if abs(api_total_price - total_price) < 0.01:
            print("Total price matches the calculated value.")