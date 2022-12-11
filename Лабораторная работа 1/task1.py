import doctest
from typing import Union

class Paper:
    """Документация на класс. Класс описывает параметры бумаги. """
    def __init__(self, height: Union[int, float], width: Union[int, float]):
        """ Создание и подготовка к работе объекта "бумага".
        :param height: высота листа бумаги
        :param width: ширина листа бумаги
        """
        if not isinstance(height, (int, float)):
            raise TypeError ("Высота листа бумаги должна быть типа int или float")
        if height < 0:
            raise ValueError ("Высота листа бумаги должна быть положительным числом")
        self.height = height

        if not isinstance(width, (int, float)):
            raise TypeError ("Ширина листа бумаги должна быть типа int или float")
        if width < 0:
            raise ValueError ("Ширина листа бумаги должна быть положительным числом")
        self.width = width

    def cutting_paper(self) -> None:
        """Разрезаем бумагу"""
        ...
    def gluing_paper(self) -> None:
        """Склеиваем бумагу"""
        ...


if __name__ == "__main__":
    paper = Paper(27, 13)
    doctest.testmod()
    pass

class Book:
   """Документация на класс. Класс описывает модель книги. """
   def __init__(self, author: str, pages: int):
       """Создание и подготовка объекта "книга".
       :param author: автор книги
       :param pages: количество страниц в книге
       """
       self.author = author
       self.pages = pages
       if not isinstance(pages, int):
           raise TypeError ("Количество страниц в книге должно быть типа int")
       if pages < 0:
           raise ValueError ("Количество страниц в книге должно быть положительным числом")

   def read_book(self) -> None:
        """Читаем книгу"""
        ...
   def close_book(self) -> None:
        """Закрываем книгу"""
        ...

if __name__ == "__main__":
    book = Book("Б. Стокер", 448)
    doctest.testmod()
    pass

class Cat:
    """Документация на класс. Класс описывает параметры кота."""
    def __init__(self, age: int, color: str):
        """Создание и подготовка объекта "кот".
        :param age: возраст кота
        :param color: цвет кота
        """
        if not isinstance(age, int):
            raise TypeError ("Возраст кота должен быть типа int")
        if age < 0:
            raise ValueError ("Возраст кота должен быть положительным числом")
        self.age = age
        self.color = color
    def feed_the_cat (self) -> None:
        """Кормим кота"""
        ...
    def call_the_cat (self) -> None:
        """Зовем кота"""
        ...
if __name__ == "__main__":
    cat = Cat(10, "Белый")
    doctest.testmod()
    pass