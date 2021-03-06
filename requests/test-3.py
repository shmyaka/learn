# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".

# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/

# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests

is_last = False
answer = ''
url = 'https://stepic.org/media/attachments/course67/3.6.3/'
next_url = ''

# читаем файл и достаем из него ссылку для запроса
with open('dataset_3378_3.txt', 'r') as text:
    next_url = text.readline().strip()

# пока не дойдем до последнего файла, будем циклично посылать запросы
while not is_last:
    # посылаем запрос
    r = requests.get(next_url)
    # из содержимого файла создаем список сток
    rows = r.text.splitlines()
    # находим первое слово в содержимом файла
    first_word = rows[0].split()[0]
    # формируем ссылку для запроса на следующий файл (если это последний файл, то ссылка будет битой,
    # но нам уже это не важно)
    next_url = url + r.text

    # если первое слово то, которое мы ищем, значит файл - последний
    if first_word == 'We':
        # меняем флаг для прерывания цикла
        is_last = True
        # записываем в ответ искомый текст
        answer = r.text

print(answer)
