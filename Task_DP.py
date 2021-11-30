class Purse:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

    def __str__(self):
        return f'Клиент: ({self.name}, Баланс: {self.cash})'


