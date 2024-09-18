import pandas as pd

# Укажите путь к вашему Excel файлу
file_path = '/Users/kolokob/Desktop/excel (2).xlsx'

# Чтение Excel файла
df = pd.read_excel(file_path, engine='openpyxl')

# Вывод названий столбцов
print("Columns in the DataFrame:", df.columns)

# Пример соответствия транспорта и его идентификатора
transport_mapping = {
    'Car': 1,
    'SUV': 2,
    '9ft Ref Van': 3,
    '17ft Box Truck': 4,
    'Pickup Truck': 5
}

# Пример функции для выбора строки на основе расстояния
def select_row_based_on_distance(df, transport_type, distance):
    # Получаем транспортный идентификатор для данного типа транспорта
    transport_id = transport_mapping.get(transport_type)

    if transport_id is None:
        print(f"No transport id found for transport type: {transport_type}")
        return None

    # Фильтруем строки для данного transport_id
    filtered_df = df[df['Transport id'] == transport_id]

    # Выбираем строку, где расстояние попадает в нужный диапазон
    selected_row = filtered_df[(filtered_df['Minimum distance'] <= distance) & (filtered_df['Maximum distance'] >= distance)]

    if not selected_row.empty:
        return selected_row
    else:
        return None

# Пример данных для расстояния
distance = 50  # Пример расстояния в милях

# Пример выбранного транспорта (на основе предыдущей логики)
selected_transport = 'SUV'

# Выбор строки на основе выбранного транспорта и расстояния
selected_row = select_row_based_on_distance(df, selected_transport, distance)

if selected_row is not None:
    print("Selected row:")
    print(selected_row)
else:
    print("No matching row found.")
