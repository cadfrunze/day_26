import pandas

# def formula(a, b, c):
#     return (a + b) ** c


#
# ecuatia = formula(a=2, b=3, c=2)
#
# print(ecuatia - 5)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# list_test = [item for item in weather_c.keys()]
# print(list_test)

# for (key, value) in weather_c.items():
#     print(key, value)


data_dict = {
    'useri': ['maryus', 'bianca', 'test_useri'],
    'scor': [1, 2, 'test_scor']
}

data_test = pandas.DataFrame(data_dict)
#
# for (cheia, valoare) in data_test.items():
#     print(valoare)

for (index, row) in data_test.iterrows():
    print(row.useri)




