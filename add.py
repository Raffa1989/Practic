import redis
import json

red = redis.Redis(
    host='redis-14387.c265.us-east-1-2.ec2.cloud.redislabs.com',
    port=14387,
    password='Vt236XwJBAc5FJGtDbFiLySw2sqyOqIP'
)

dict1 = {'key1': 'value1', 'key2': 'value2'} # создаём словарь для записи
red.set('dict1', json.dumps(dict1)) # с помощью функции dumps() из модуля json превратим наш словарь в строчку
converted_dict = json.loads(red.get('dict1')) # с помощью знакомой нам функции превращаем
# данные полученные из кэша обратно в словарь

red.delete('dict1') # удаляются ключи с помощью метода .delete()
print(red.get('dict1'))

# print(type(converted_dict)) # убеждаемся, что получили действительно словарь
# print(converted_dict) # ну и выводим его содержание

# red.set('var1', 'value1') # записываем в кеш строку "value1"
# print(red.get('var1')) # считываем из кэша данные
# print(red.get('var1')) # считываем из кэша данные
