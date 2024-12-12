import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides:int, filled: bool = True):
        if self.__is_valid_color(*color):
            self.__color = list(color)
        else:
            self.__color = [0, 0, 0]

        # self.__sides = list(sides)

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

        self.filled = filled


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        return (isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and
                0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print(f'Отсутствие выбранного цвета')

    def __is_valid_sides(self, *sides):
        # if len(sides) != len(self.__sides):
        #     return False
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return
        else:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple[int, int, int], *sides:int, filled: bool = True):
        if len(sides) == 1:
            self.__sides = [sides[0]]
        else:
            self.__radius = self.__sides[0] / (2 * math.pi)
            self.__sides = [1]
        super().__init__(color, *self.__sides, filled=filled)

    def get_square(self):
        area = math.pi * self.__radius ** 2
        return area


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides:int, filled: bool = True):
        if len(sides) == 3:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * 3
        super().__init__(color, *self.__sides, filled=filled)

    def get_square(self):
        p = sum(self.__sides) / 2
        return math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], *sides:int, filled: bool = True):
        if len(sides) == 1:
            self.__sides = [sides[0]] * 12
        elif len(sides) == 12:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * 12
        super().__init__(color, *self.__sides, filled=filled)

    def get_volume(self):
        a = self.__sides[0]
        return a ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
