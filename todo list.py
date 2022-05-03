import json

def p1():
 z = input('Сформулируйте задачу: ')
 k = input('Добавьте категорию к задаче: ')
 v = input('Добавьте время к задаче: ')
 data['task'].append({'category': k,
                       'name': z,
                      'time': v})
 with open('task.json', 'w') as outfile:
    json.dump(data['task'], outfile)

 return ("Команды: \n 1. Добавить задачу. \n 2. Вывести список задач. \n 3. Выход.")

def p2():
    with open("task.json", "r") as f_obj:
        f = json.load(f_obj)
        for item in f:
           print('Задача:', item["name"], 'Категория:', item["category"], 'Дата:', item["time"])
    return ("Команды: \n 1. Добавить задачу. \n 2. Вывести список задач. \n 3. Выход.")

data = {}
data['task'] = []
print("Текущие задачи из файла: \n", data['task'])
print("Команды: \n 1. Добавить задачу. \n 2. Вывести список задач. \n 3. Выход.")
comand = input('Укажите число ')
while comand != '3':
 if comand == '1':
  print(p1())
 elif comand == '2':
  print(p2())
 comand = input('Укажите число ')
print("Задачи сохранены в файл!")

# with open("task.json", "r") as f_obj:
#   list = json.load(f_obj)
# f_obj = {'category': k,
#           'name': z,
#          'time': v}
# f = json.dumps(f_obj)
# lst.append(f)
# print(lst)
# print(list, f)
# with open("task.json", "w") as file:
#   file.write(f)