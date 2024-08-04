class Project:

    def __init__(self, name, date, priority=0.0, cost=0.0, status=0):

        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.status = status

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, start: {self.date}, priority {self.priority}, cost estimated: ${self.cost}, completion: {self.status}%"

    def __lt__(self, other):
        return self.priority < other.priority










