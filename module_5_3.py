class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # атрибут имени дома
        self.number_of_floors = number_of_floors  # атрибут количества этажей

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors  # количество этажей

    def __str__(self):
        return f"Название: {self.name}, Количество этажей: {self.number_of_floors}"  # информация о доме

    def assay_other(self, other):
        return isinstance(other, House)  # относится ли other к классу House

    def eq(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors == other
        return "Ошибка сравнения"

    def lt(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors < other
        return "Ошибка"

    def le(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors <= other
        return "Ошибка"

    def gt(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors > other
        return "Ошибка"

    def ge(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors >= other
        return "Ошибка"

    def ne(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, (int, float)):
            return self.number_of_floors != other
        return "Ошибка"

    def add(self, value):
        if isinstance(value, int):
            self.number_of_floors += value  # Увеличиваем количество этажей
            return self
        return "Ошибка при добавлении"

    def __radd__(self, value):
        return self.add(value)  # перегрузка оператора для a + b

    def __iadd__(self, value):
        return self.add(value)  # перегрузка оператора для a += b


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Эрендел', 30)

print(h1)
print(h2)
print(h3)

print('Сравнение')
print(h1 == h2)
print(h2 == h3)
print(h3 == h1)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)
print(h1 == h3)

h2 = 10 + h2
print(h2)

print(h1 > h3)
print(h1 >= h2)
print(h3 < h2)
print(h1 <= h2)
print(h1 != h2)
print(h1 != h3)
