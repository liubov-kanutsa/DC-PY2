class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self.name

    @property
    def author(self):
        return self.author


    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.name = name
        self.author = author
        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError("Количество страниц в книге должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц в книге должно быть положительным числом")

    def __str__(self):
        super.__str__(self)
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.name = name
        self.author = author
        self.duration = duration
        if not isinstance(duration, float):
            raise TypeError("Продолжительность аудио книги должна быть типа float")
        if duration < 0:
            raise ValueError("Продолжительность аудио книги должна быть положительным числом")

    def __str__(self):
        super.__str__(self)
        return f"Книга {self.name}. Автор {self.author}"
