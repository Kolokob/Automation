# import random
# from datetime import datetime, timedelta
#
# def random_date(start, end):
#     return start + timedelta(days=random.randint(0, (end - start).days))
#
#
# PARCEL_SIZES = ['small', 'medium', 'large', 'heavy_load', 'custom size']
# EXTRA_SERVICES = ['Ladder', 'Blankets', 'White gloves service', 'Food Catering Setup', 'None']
# VEHICLE_TYPES = {
#     'small': None,
#     'medium': None,
#     'large': ['Car', 'SUV', 'Pickup Truck'],
#     'heavy_load': ['Pickup Truck', '9ft Cargo Van', '9ft Ref Van', '10ft Box Truck', '15ft Box Truck'],
#     'custom size': ['Car', 'SUV', 'Pickup Truck', '9ft Cargo Van', '9ft Ref Van', '10ft Box Truck', '15ft Box Truck']
# }
# DATES = [random_date(datetime(2024, 7, 15), datetime(2024, 9, 30)).strftime('%d/%m/%Y') for _ in range(100)]
#
# test_cases = []
# for _ in range(300):
#     parcel_size = random.choice(PARCEL_SIZES)
#     vehicle_type = random.choice(VEHICLE_TYPES[parcel_size]) if VEHICLE_TYPES[parcel_size] else None
#     extra_service = random.choice(EXTRA_SERVICES)
#     extra_service_details = {
#         'Ladder': 5,
#         'Blankets': 5,
#         'White gloves service': '60 minutes',
#         'Food Catering Setup': '3 hours',
#         'None': ''
#     }[extra_service]
#     pick_up_time = random.choice(['urgent', 'scheduled', 'repeated'])
#
#     if pick_up_time == 'urgent':
#         days_or_date, time, start_date = None, None, None
#     elif pick_up_time == 'scheduled':
#         days_or_date, start_date = random.choice(DATES), None
#         time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"
#     else:
#         days_or_date = random.sample(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#                                      random.randint(1, 3))
#         time = [f"{random.randint(0, 23):02}:{random.randint(0, 59):02}" for _ in range(len(days_or_date))]
#         start_date = random.choice(DATES)
#
#     test_cases.append({
#         'pick_up_address_amount': 1,
#         'extra_service': extra_service,
#         'extra_service_details': extra_service_details,
#         'drop_off_address_amount': 1,
#         'parcel_size': parcel_size,
#         'vehicle_type': vehicle_type,
#         'declared_value': random.randint(0, 10000),
#         'pick_up_time': pick_up_time,
#         'days_or_date': ', '.join(days_or_date) if isinstance(days_or_date, list) else days_or_date,
#         'time': ', '.join(time) if isinstance(time, list) else time,
#         'start_date': start_date,
#         'tips': random.choice([0, 10, 20, 50, 100]),
#         'signature': random.choice([True, False])
#     })
#
# with open('test_cases.feature', 'w') as file:
#     file.write("Feature: Delivery Test Cases\n\n")
#     file.write("  Scenario Outline: Delivery scenario\n")
#     file.write("    Given pick up address amount is <pick_up_address_amount>\n")
#     file.write("    And extra service is <extra_service>\n")
#     file.write("    And extra service details are <extra_service_details>\n")
#     file.write("    And drop off address amount is <drop_off_address_amount>\n")
#     file.write("    And parcel size is <parcel_size>\n")
#     file.write("    And vehicle type is <vehicle_type>\n")
#     file.write("    And declared value is <declared_value>\n")
#     file.write("    And pick up time is <pick_up_time>\n")
#     file.write("    And days or date are <days_or_date>\n")
#     file.write("    And time is <time>\n")
#     file.write("    And start date is <start_date>\n")
#     file.write("    And tips are <tips>\n")
#     file.write("    And signature is <signature>\n\n")
#     file.write("  Examples:\n")
#     file.write(
#         "    | pick_up_address_amount | extra_service | extra_service_details | drop_off_address_amount | parcel_size | vehicle_type | declared_value | pick_up_time | days_or_date | time | start_date | tips | signature |\n")
#
#     for case in test_cases:
#         file.write("    | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n".format(
#             case['pick_up_address_amount'], case['extra_service'], case['extra_service_details'],
#             case['drop_off_address_amount'], case['parcel_size'], case['vehicle_type'],
#             case['declared_value'], case['pick_up_time'], case['days_or_date'],
#             case['time'], case['start_date'], case['tips'], case['signature']
#         ))
#
# print("Test cases generated and saved to test_cases.feature")
#
#

import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

PARCEL_SIZES = ['custom size']  # Оставляем только 'custom size'
EXTRA_SERVICES = ['Ladder', 'Blankets', 'White gloves service', 'Food Catering Setup', 'None']
VEHICLE_TYPES = {'custom size': ['Car', 'SUV', 'Pickup Truck', '9ft Cargo Van', '9ft Ref Van', '10ft Box Truck', '15ft Box Truck']}
DATES = [random_date(datetime(2024, 7, 15), datetime(2024, 9, 30)).strftime('%d/%m/%Y') for _ in range(100)]

test_cases = []
for _ in range(300):
    parcel_size = 'custom size'
    vehicle_type = random.choice(VEHICLE_TYPES[parcel_size])
    extra_service = random.choice(EXTRA_SERVICES)
    extra_service_details = {
        'Ladder': 5,
        'Blankets': 5,
        'White gloves service': '60 minutes',
        'Food Catering Setup': '3 hours',
        'None': ''}[extra_service]
    pick_up_time = random.choice(['urgent', 'scheduled', 'repeated'])

    custom_dimensions = {
        'length': random.randint(1, 300),
        'width': random.randint(1, 300),
        'height': random.randint(1, 300)
    }

    if pick_up_time == 'urgent':
        days_or_date, time, start_date = None, None, None
    elif pick_up_time == 'scheduled':
        days_or_date, start_date = random.choice(DATES), None
        time = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}"
    else:
        days_or_date = random.sample(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
                                     random.randint(1, 3))
        time = [f"{random.randint(0, 23):02}:{random.randint(0, 59):02}" for _ in range(len(days_or_date))]
        start_date = random.choice(DATES)

    test_cases.append({
        'pick_up_address_amount': 1,
        'extra_service': extra_service,
        'extra_service_details': extra_service_details,
        'drop_off_address_amount': 1,
        'parcel_size': parcel_size,
        'vehicle_type': vehicle_type,
        'declared_value': random.randint(0, 10000),
        'pick_up_time': pick_up_time,
        'days_or_date': ', '.join(days_or_date) if isinstance(days_or_date, list) else days_or_date,
        'time': ', '.join(time) if isinstance(time, list) else time,
        'start_date': start_date,
        'custom_dimensions': custom_dimensions,
        'tips': random.choice([0, 10, 20, 50, 100]),
        'signature': random.choice([True, False])
    })

with open('test_cases.feature', 'w') as file:
    file.write("Feature: Delivery Test Cases with Custom Dimensions\n\n")
    file.write("  Scenario Outline: Delivery scenario\n")
    file.write("    Given pick up address amount is <pick_up_address_amount>\n")
    file.write("    And extra service is <extra_service>\n")
    file.write("    And extra service details are <extra_service_details>\n")
    file.write("    And drop off address amount is <drop_off_address_amount>\n")
    file.write("    And parcel size is <parcel_size>\n")
    file.write("    And vehicle type is <vehicle_type>\n")
    file.write("    And declared value is <declared_value>\n")
    file.write("    And pick up time is <pick_up_time>\n")
    file.write("    And days or date are <days_or_date>\n")
    file.write("    And time is <time>\n")
    file.write("    And start date is <start_date>\n")
    file.write("    And custom dimensions are <custom_dimensions>\n")
    file.write("    And tips are <tips>\n")
    file.write("    And signature is <signature>\n\n")
    file.write("  Examples:\n")
    file.write(
        "    | pick_up_address_amount | extra_service | extra_service_details | drop_off_address_amount | parcel_size | vehicle_type | declared_value | pick_up_time | days_or_date | time | start_date | custom_dimensions | tips | signature |\n")

    for case in test_cases:
        file.write("    | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |\n".format(
            case['pick_up_address_amount'], case['extra_service'], case['extra_service_details'],
            case['drop_off_address_amount'], case['parcel_size'], case['vehicle_type'],
            case['declared_value'], case['pick_up_time'], case['days_or_date'],
            case['time'], case['start_date'], case['custom_dimensions'], case['tips'], case['signature']
        ))

print("Test cases with custom dimensions generated and saved to test_cases.feature")
