per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
deposit = list(map(lambda x: int(money/100*x), per_cent.values()))
print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))

