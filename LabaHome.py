documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def p():
 n = input('Введите номер документа: '); pc = 0
 for i in range(len(documents)):
  if documents[i]['number'] == n:
   print('Результат: \nВладелец документа:', end='')
   return documents[i]['name']
   pc += 1
 if pc == 0:
  return ('Результат: \nДокумент не найден в базе')

def s():
 n = input('Введите номер документа: '); sc = 0
 for i in range(len(directories)):
  for j in range(len(directories[str(i+1)])):
   if directories[str(i+1)][j] == n:
    print('Результат: \nДокумент хранится на полке:', end='')
    return i+1
    sc += 1
 if sc == 0:
  return ('Результат: \nДокумент не найден в базе')



def l():
 for i in range(len(documents)):
  for k in range(len(directories)):
   for j in range(len(directories[str(list(directories)[k])])):
    if directories[str(list(directories)[k])][j] == documents[i]['number']:
     documents[i]['lc'] = list(directories)[k]
  print('№', documents[i]['number'], ', тип:', documents[i]['type'], ', владелец:', documents[i]['name'], ', полка хранения:', documents[i]['lc'])
 return ""

def ads():
 ac = 0
 n = input('Введите номер полки: ')
 lst = list(directories)
 for i in range(len(lst)):
  if n == lst[i]:
   ac += 1
   print('Результат: \nТакая полка уже существует. Текущий перечень полок: ', end='')
   return ", ".join(lst)
 if ac == 0:
  directories.setdefault(n)
  directories[n]=[]
  lst = list(directories)
  print('Результат: \nПолка добавлена. Текущий перечень полок: ', end='')
  return ", ".join(lst)

def ds():
 n = input('Введите номер полки: ')
 if directories.get(n) == None:
  print('Результат: \nТакой полки не существует. Текущий перечень полок: ', end='')
  return ", ".join(list(directories))
 elif directories[n] != []:
  print('Результат: \nНа полке есть документа, удалите их перед удалением полки. Текущий перечень полок: ', end='')
  return ", ".join(list(directories))
 elif directories[n] == []:
  del directories[n]
  print('Результат: \nПолка удалена. Текущий перечень полок: ', end='')
  return ", ".join(list(directories))

def ad():
 lst = {}
 lst['number'] = input('Введите номер документа: ')
 lst['type'] = input('Введите тип документа: ')
 lst['name'] = input('Введите владельца документа: ')
 lst['ls'] = input('Введите полку для хранения: ')
 if lst['ls'] in list(directories):
  documents.append(lst)
  directories[lst['ls']].append(lst['number'])
  print('Документ добавлен. Текущий список документов:', end='')
 else:
  print('Такой полки не существует. Добавьте полку командой ads. \nТекущий список документов:', end='')
 return l()

def d():
 n = input('Введите номер документа: '); dc = 0
 for i in range(len(directories)):
  for j in range(len(directories[str(i + 1)])):
   if directories[str(i + 1)][j] == n:
    del directories[str(i + 1)][j]
 for i in range(len(documents)):
  if documents[i]['number'] == n:
   del documents[i]
   print('Документ удален. \nТекущий список документов:', end='')
   dc += 1
 if dc == 0:
  print('Документ не найден в базе. \nТекущий список документов:', end='')
 return l()

def m():
 n = input('Введите номер документа: '); mc = 0
 p = input('Введите номер полки: ')
 if directories.get(p) == None:
  print('Результат: \nТакой полки не существует. Текущий перечень полок: ', end='')
  return ", ".join(list(directories))
 for i in range(len(documents)):
  if documents[i]['number'] == n:
   mc += 1
 if mc == 0:
  print('Документ не найден в базе. \nТекущий список документов:', end='')
  return l()
 else:
  for i in range(len(directories)):
   for j in range(len(directories[str(i + 1)])):
    if directories[str(i + 1)][j] == n:
     del directories[str(i + 1)][j]
  directories[p].append(n)
  print('Документ перемещен. \nТекущий список документов:', end='')
  return l()

comand = input('Введите команду ')
while  comand!= 'q':
 if comand == 'p':
  print(p())
 elif comand == 's':
  print(s())
 elif comand == 'l':
  print(l())
 elif comand == 'ads':
  print(ads())
 elif comand == 'ds':
  print(ds())
 elif comand == 'ad':
  print(ad())
 elif comand == 'd':
  print(d())
 elif comand == 'm':
  print(m())
 comand = input('Введите команду ')



