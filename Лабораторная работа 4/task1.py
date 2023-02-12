import doctest

class Pets:
    """Базовый класс питомцев"""
    def __init__(self, type_of_pet: str, age: int):
        """Создание и подготовка объекта питомец
        :param type_of_pet: вид питомца
        :param age: возраст """
        self.type_of_pet = type_of_pet
        self.age = age

    def __str__(self):
        return f"Питомец {self.type_of_pet}. Возраст {self.age}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.type_of_pet!r}, age={self.age!r})"

class Cat(Pets):
    def __init__(self, type_of_pet: str, age: int, color: str):
        """Создание и подготовка объекта "кот".
        :param type_of_pet: вид питомца
        :param age: возраст кота
        :param color: цвет кота
        """
        super().__init__(type_of_pet, age)
        self.type_of_pet = type_of_pet
        self.age = age
        self.color = color

    def __str__(self):
        super.__str__(self)
        return f"Питомец {self.type_of_pet}. Возраст {self.age}"


if __name__ == "__main__":
    cat = Cat("Кот", 10, "Белый")
    doctest.testmod()
    pass
