students = ["Вася", "Маша", "Петя", "Дима", "Марина", "Люба", "Коля", "Ваня"]
grades = {"Вася" : 4, "Петя" : 9, "Марина" : 8, "Люба" : 4, "Коля" : 5, "Ваня": 10}
for item in students:
    if grades.get(item) == None:
        print(item, 'контрольную работу не писал(а)')
    else:
        print(item, grades[item])

good = []
bad = []
for item in grades:
    if grades[item] >= 8:
        print(item,'получил(а) отличную оценку')
        good.append(item)
    else:
        bad.append(item)
print(good)
print(bad)




marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
categories = {'отлично' : [8, 9, 10],
             'хорошо' : [6, 7],
             'удовлетворительно' : [4, 5],
             'неуд' : [0, 1, 2, 3]}

kurs = int(input())
k = len(marks)
s = sum({marks[i][kurs-1] for i in marks})
print('Курс', kurs, '-', round(s/k))
for i in categories:
    if round(s/k) in categories[i]:
        print('Курс', kurs, '-', i)


marks = {'Mary' : [5, 8, 9, 10, 3, 5, 6, 6],
        'John' : [3, 3, 6, 8, 2, 1, 8, 5],
        'Alex' : [4, 4, 7, 4, 7, 3, 2, 9],
        'Patricia' : [2, 1, 6, 8, 2, 3, 7, 4]}
num = int(input())
kol = 0
for i in marks:
    for j in marks[i]:
        if j >= num:
            kol += 1
print(kol)


results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
for j in results:
   results[j].setdefault('ROI', round(((results[j]['revenue'] / results[j]['cost'] - 1) * 100), 2))
print(results)