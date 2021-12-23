import requests  # импортируем наш знакомый модуль
import lxml.html
from lxml import etree
site = requests.get('https://www.python.org/')
# создадим объект ElementTree. Он возвращается функцией parse()
# print(site.text)
tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser()) # попытаемся спарсить наш файл с помощью HTML-парсера.
# Сам HTML — это то, что мы скачали и поместили в папку из браузера.

ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li') # помещаем в аргумент методу findall скопированный xpath.
# Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)

# создаём цикл, в котором будем выводить название каждого элемента из списка
for li in ul:
    a = li.find('a') # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>.
    # Т.е. гиперссылка, на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
    time = li.find('time') #показывает ещё и дату добавления новости
    print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием