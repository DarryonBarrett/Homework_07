# Задача 42: Узнать какая максимальная households в 
# зоне минимального значения population.

import pandas as pd

data = pd.read_csv("sample_data/california_housing_test.csv")

min_population = data['population'].min()

min_population_zone = data[data['population'] == min_population]

max_households = min_population_zone['households'].max()

print(f"Максимальное количество households в зоне с минимальным значением population: {max_households}")