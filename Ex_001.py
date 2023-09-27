# Задача 40: Работать с файлом california_housing_test.csv, 
# который находится в папке sample_data. Определить среднюю стоимость дома, 
# где кол-во людей от 0 до 500 (population).

import pandas as pd

data = pd.read_csv("sample_data/california_housing_test.csv")

filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

average_house_price = filtered_data['median_house_value'].mean()

print(f"Средняя стоимость дома, где кол-во людей от 0 до 500: ${average_house_price:.2f}")