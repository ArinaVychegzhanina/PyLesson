class Hotel:
    def __init__(self, num_rooms):
        self._rooms = [0 for _ in range(num_rooms)]  # информация о статусе номеров

    # метод для бронирования номера по уникальному значению в списке
    def occypy(self, room_id):
        if self._rooms[room_id] == 0:
            self._rooms[room_id] = 1  # бронируем номер
        else:
            raise RuntimeError("Номер занят")

    # метод для освобождения номера по уникальному значению в списке
    def free(self, room_id):
        self._rooms[room_id] = 0  # освобождаем номер

    # метод, который занимает все свободные номера в отеле
    def all_occypy(self):
        for i in range(len(self._rooms)):
            self._rooms[i] = 1

    #метод, который освобождает все занятые номера отеля
    def all_free(self):
        for i in range(len(self._rooms)):
            self._rooms[i] = 0

    # метод, который возвращает долю занятых номеров
    def share_occupied(self):
        s = sum(self._rooms)/len(self._rooms)
        return 'Доля занятых номеров: ' + str(s)

    #метод, который возвращает выручку
    def revenue(self):
        s = sum(self._rooms)*5
        return 'Выручка: ' + str(s) + ' тыс. у.е.'

    #метод __str__ для красивой печати списка номеров
    def __str__(self):
        a = ''
        for i in range(len(self._rooms)):
            if self._rooms[i] == 0:
                a += 'Номер ' + str(i + 1) + " свободен\n"
            else:
                a += 'Номер ' + str(i + 1) + " занят\n"
        return a


hotel = Hotel(5)  # в нашем отеле, например, 5 номеров
print(hotel._rooms)  # смотрим номера через атрибут self.rooms
hotel.occypy(3)
print(hotel._rooms)
print(hotel.share_occupied())
print(hotel.revenue())
print(hotel)
hotel.free(3)
print(hotel._rooms)
hotel.all_occypy()
print(hotel._rooms)
print(hotel.share_occupied())
print(hotel.revenue())
hotel.all_free()
print(hotel._rooms)
print(hotel)
