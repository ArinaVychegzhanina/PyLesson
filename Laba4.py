class Hotel:
    def __init__(self, SGL_rooms, DBL_rooms, JuniorSuite_rooms, Suite_rooms): # информация о статусе, стоимости и типе номеров
        self._rooms = {
            "SGL": [2000, [0 for _ in range(SGL_rooms)]],
            "DBL": [3500, [0 for _ in range(DBL_rooms)]],
            "Junior Suite": [27000, [0 for _ in range(JuniorSuite_rooms)]],
            "Suite": [18000, [0 for _ in range(Suite_rooms)]],
        }

    # метод для бронирования номера по уникальному значению в списке
    def occypy(self, room_type, room_id):
        if len(self._rooms[room_type][1]) > room_id:
            if self._rooms[room_type][1][room_id] == 0:
                self._rooms[room_type][1][room_id] = 1  # бронируем номер
            else:
                raise RuntimeError("Номер занят")
        else:
            raise RuntimeError("Такого номера нет")

    # метод для освобождения номера по типу и уникальному значению в списке
    def free(self, room_type, room_id):
        self._rooms[room_type][1][room_id] = 0

    # метод, который занимает все свободные номера какого-то типа в отеле
    def all_occypy(self, room_type):
        for i in range(len(self._rooms[room_type][1])):
            self._rooms[room_type][1][i] = 1

    #метод, который освобождает все занятые номера какого-то типа в отеле
    def all_free(self, room_type):
        for i in range(len(self._rooms[room_type][1])):
            self._rooms[room_type][1][i] = 0

    # метод, который возвращает долю занятых номеров каждого типа
    def share_occupied(self):
        s = ''
        for j in list(self._rooms):
            a = sum(self._rooms[j][1])/len(self._rooms[j][1])
            s += 'Доля занятых номеров типа ' + str(j) + ': ' + str(a) + "\n"
        return s

    #метод, который возвращает выручку со всех номеров
    def revenue(self):
         s = 0
         for j in list(self._rooms):
             s += sum(self._rooms[j][1]) * self._rooms[j][0]
         return 'Выручка: ' + str(s) + ' тыс. у.е.'

    #метод __str__ для красивой печати списка номеров
    def __str__(self):
         a = ''; lst = []; s = 0
         for j in list(self._rooms):
             s += len(self._rooms[j][1])
         for k in list(self._rooms):
             lst += self._rooms[k][1]
         for i in range(s):
             if lst[i] == 0:
                 a += 'Номер ' + str(i + 1) + " свободен\n"
             else:
                 a += 'Номер ' + str(i + 1) + " занят\n"
         return a



hotel = Hotel(5, 4, 1, 3)  # в нашем отеле, например, 5 номеров
print(hotel._rooms)  # смотрим номера через атрибут self.rooms
hotel.occypy("SGL", 3)
print(hotel._rooms)
print(hotel.revenue())
hotel.free("SGL", 3)
print(hotel._rooms)
hotel.all_occypy("DBL")
print(hotel._rooms)
print(hotel.share_occupied())
print(hotel.revenue())
print(hotel)
hotel.all_free("DBL")
print(hotel._rooms)
print(hotel)