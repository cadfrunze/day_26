import pandas
data_brut = {
    "useri": ['Maryus', 'Bianca', 'Iulia', 'Sebi'],
    "scor:": [1, 2, 3, 4]
}

data_pd = pandas.DataFrame(data_brut)


for (cheia, valoarea) in data_pd.iterrows():
    print(valoarea)

