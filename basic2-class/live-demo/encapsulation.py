class Cho:
    def __init__(self, name) -> None:
        self.name = name
        self._age = 3  # Protected attribute (by convention)
        self.__breed = "Pitbull"  # Private attribute (by convention)


dog = Cho("Gaugau")

print(dog.name)
print(dog._age)

dog._age = 10
print(dog._age)

print(dog._Cho__breed)

dog._Cho__breed = "German Shepherd"
print(dog._Cho__breed)


class Pitbull(Cho):
    def __init__(self, name) -> None:
        super().__init__(name)  # Goi method __init__ cua class Cho
        self._age = 7

    # def __str__(self) -> str:
    #     return f"Pitbull {self.name} {self._age}, woof, woof!"

    def print_super(self):
        print(super())


pit = Pitbull("Long")

print(pit.__str__())
pit.print_super()

print(pit)
