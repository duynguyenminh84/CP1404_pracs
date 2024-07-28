class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.type = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.type == 'Dynamic'

    def __str__(self):
        return f"{self.name}, {self.type}, Reflection={self.reflection}, First appeared in {self.year}"





