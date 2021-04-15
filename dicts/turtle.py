# Группа биологов в институте биоинформатики завела себе черепашку.

# После дрессировки черепашка научилась понимать и запоминать указания биологов следующего вида:
# север 10
# запад 20
# юг 30
# восток 40
# где первое слово — это направление, в котором должна двигаться черепашка, 
# а число после слова — это положительное расстояние в сантиметрах, которое должна пройти черепашка.

# Но команды даются быстро, а черепашка ползёт медленно, и программисты догадались, 
# что можно написать программу, которая определит, куда в итоге биологи приведут черепашку. 
# Для этого программисты просят вас написать программу, которая выведет точку, 
# в которой окажется черепашка после всех команд. Для простоты они решили считать, 
# что движение начинается в точке (0, 0), и движение на восток увеличивает первую координату, а на север — вторую.

# Программе подаётся на вход число команд nn, которые нужно выполнить черепашке, 
# после чего nn строк с самими командами. 
# Вывести нужно два числа в одну строку: первую и вторую координату конечной точки черепашки. 
# Все координаты целочисленные.

# создаем словарь-помощник, который подсказывает нам какую координату меняем
# и в какую сторону (плюс или минус)
diсt = {
    'север': [1, '+'],
    'юг': [1, '-'],
    'восток': [0, '+'],
    'запад': [0, '-']
}

# узнаем сколько у нас будет строк
n = int(input())
res = [0, 0]

# создаем массив введенных координат
destinations = [(input().split()) for i in range(n)]

# вычисляем координаты для точки, в которой окажется черепаха
for x in destinations:
    res[diсt[x[0]][0]] += int(diсt[x[0]][1] + x[1])
    
print(*res)

# Sample Input:

# 4
# север 10
# запад 20
# юг 30
# восток 40


# Sample Output:

# 20 -20