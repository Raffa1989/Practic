class People:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def __str__(self):
        return f'({self.name}, {self.city}, {self.status})'