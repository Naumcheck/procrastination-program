people_data = {'FIO': 'f f', 'Age': 12, 'Gender': 'Ж', 'Tasks':
    {'Task1': {'Error': 3, 'Time': 3.05, 'Question': 0},
     'Task2': {'Error': 4, 'Time': 5.23, 'Question': 0},
     'Task3': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task4': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task5': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task6': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task7': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task8': {'Error': 3, 'Time': 2.02, 'Question': 0}}}

import csv
fields = ['FIO', 'Age', 'Gender']
task_fields = ['Task', 'Error', 'Time', 'Question']
rows = []

# Добавление данных о задачах
for task, details in people_data['Tasks'].items():
    row = [people_data['FIO'], people_data['Age'], people_data['Gender'], task, details['Error'], details['Time'], details['Question']]
    rows.append(row)

# Имена заголовков для CSV файла
header = fields + task_fields

# Запись в файл
with open('people_data.csv', 'w', newline='',encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

import json

# Данные для записи
people_data = {
    'FIO': 'f f', 'Age': 12, 'Gender': 'Ж', 'Tasks':
    {'Task1': {'Error': 3, 'Time': 3.05, 'Question': 0},
     'Task2': {'Error': 4, 'Time': 5.23, 'Question': 0},
     'Task3': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task4': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task5': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task6': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task7': {'Error': 3, 'Time': 2.02, 'Question': 0},
     'Task8': {'Error': 3, 'Time': 2.02, 'Question': 0}}
}

# Запись в файл JSON
with open('people_data.json', 'w', encoding='utf-8') as file:
    json.dump(people_data, file, ensure_ascii=False, indent=4)

print("Данные успешно записаны в файл 'people_data.json'.")

