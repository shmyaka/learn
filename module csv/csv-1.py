# https://stepik.org/lesson/24473/step/2?unit=6777
#
# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.
#
# Одним из атрибутов преступления является его тип – Primary Type.
#
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

import csv
import re


# Функция для фильтрации строк по 2015 году
def foo(item):
    return True if int(''.join(re.split(r'\d{2}\/\d{2}\/(\d{4}).*', item[2]))) == 2015 else False


res = []
ans_dict = {}
# Записываем в массив все строки, из нашего файла, кроме первой (шапки таблицы)
with open('Crimes.csv') as t:
    rows = csv.reader(t)
    for i, row in enumerate(rows):
        if i:
            res.append(row)

# Оставляем в списке только строки с 2015-м годом
res = list(filter(foo, res))

# Подсчитываем количество преступлений того или иного вида
# и записываем результаты в словарь
for el in res:
    ans_dict[el[5]] = ans_dict[el[5]] + 1 if ans_dict.get(el[5]) else 1

# Создаем из наших пар "ключ-значение" список и сортируем его
# по количеству преступлений в обратном направлении
res = sorted(list(ans_dict.items()), key=lambda x: int(x[1]), reverse=True)

# Печатаем тип самого распространённого преступления
print(res[0][0])
