names = ['Maryus', 'Iulia', 'Bianca', 'Sebi']

new_names = [name.upper() for name in names if name != name.upper()]
print(new_names)

with open('work_log.txt', 'a') as file:
    file.writelines('\n19.02')