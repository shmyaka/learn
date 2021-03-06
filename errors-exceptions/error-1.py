# https://stepik.org/lesson/24463/step/7?unit=6771

# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
#
# Или эквивалентно записи:
# class Error1(Error2, Error3 ... ErrorK):
#     pass
#
# Антон написал код, который выглядит следующим образом.
#
# try:
#    foo()
# except <имя 1>:
#    print("<имя 1>")
# except <имя 2>:
#    print("<имя 2>")
# ...
# Костя посмотрел на этот код и указал Антону на то,
# что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок.
# Но Антон не помнит какие исключения наследуются от каких.
# Помогите ему выйти из неловкого положения и напишите программу,
# которая будет определять обработку каких исключений можно удалить из кода.
#
# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы.
# Создавать классы исключений также не требуется
# Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить,
# потому что мы уже ранее где-то поймали их предка.
#
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.
#
# В следующих n строках содержится описание наследования классов.
# В i-й строке указано от каких классов наследуется i-й класс.
# Обратите внимание, что класс может ни от кого не наследоваться.
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.
#
# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения,
# обработку которого можно удалить из кода, не изменив при этом поведение программы.
# Имена следует выводить в том же порядке, в котором они идут во входных данных.
#
# Пример теста 1
# Рассмотрим код
#
# try:
#    foo()
# except ZeroDivision :
#    print("ZeroDivision")
# except OSError:
#    print("OSError")
# except ArithmeticError:
#    print("ArithmeticError")
# except FileNotFoundError:
#    print("FileNotFoundError")
#
#
# ...
#
#
# По условию этого теста, Костя посмотрел на этот код, и сказал Антону,
# что исключение FileNotFoundError можно не ловить,
# ведь мы уже ловим OSError -- предок FileNotFoundError

# Создаем класс, унаследованный от list,
# чтобы мы могли генерировать что-то вроде set
# только упорядоченного. По сути, нам это не сильно нужно
class MyList(list):
    def add(self, element):
        if element not in self:
            self.append(element)


# Создаем объект, в который будем собирать данные о наших классах и их родителях
# а также множество исключений, который были вызваны,
# и множество, в которое мы будем складывать исключения,
# которые можно было бы и не вызывать, так как они повторяются
# или вызваны после своих предков
res = {}
stack = MyList()
extra = MyList()


# Функция создает объект для хранения данных о новом классе исключения
# и помещает его в наш перечель объектов
def createExcep(new_name):
    if new_name not in res:
        res[new_name] = {
            'parents': MyList()
        }


# Функция вносит в объект нашего класса-исключения данные о предках
def setParents(child, *parents):
    createExcep(child)

    for p in parents:
        createExcep(p)
        res[child]['parents'].add(p)


# Рекурсивная функция, которая подсчитывает, является ли
# класс, переданный во втором аргументе прямым или непрямым предком искомого класса
def getParent(child, parent):
    result = 0

    if parent in res[child]['parents']:
        result = 1
    # если родителей у искомого класса больше нуля, то проходим по всем им
    elif len(res[child]['parents']):
        for k in res[child]['parents']:
            # проверяем является класс, переданный во втором аргументе родителем родителя искомого класса
            result += getParent(k, parent)

    return result


# Функция проверяет появляелся ли предок искомого класса уже в стеке
def checkParents(current_name):
    for k in stack:
        if bool(getParent(current_name, k)):
            return True

    return False


# Проверяет стэк вызовов
def checkStack(name):
    # если класс уже был вызыван в стэке,
    # добавляем его в список лишних
    if name in stack:
        extra.add(name)
    # если предок класса уже был вызыван в стэке,
    # добавляем его в список лишних
    elif checkParents(name):
        extra.add(name)
    # иначе добавляем его в стэк
    else:
        stack.add(name)

# Дальше идёт обработка данных введенных пользователем
n = int(input())

for x in range(n):
    s = input().split(' : ')
    name_ex = s[0]
    par = []

    if len(s) > 1:
        par = s[1].split()

    setParents(name_ex, *par)

q = int(input())

for i in range(q):
    s = input()
    checkStack(s)

for it in extra:
    print(it)

# Sample Input:
#
# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError


# Sample Output:
#
# FileNotFoundError
