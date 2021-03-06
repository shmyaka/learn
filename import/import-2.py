# Алиса владеет интересной информацией, которую хочет заполучить Боб.
# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями,
# но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.
#
# Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
# Она представила информацию в виде строки, и затем записала в бинарный файл
# результат работы метода simplecrypt.encrypt.
#
# Вам необходимо установить библиотеку simple-crypt, и с помощью
# метода simplecrypt.decrypt узнать, какой из паролей служит
# ключом для расшифровки файла с интересной информацией.
#
# Ответом для данной задачи служит расшифрованная интересная информация Алисы

# Импортируем метод-дешифратор из модуля simplecrypt и объект исключения
# для неправильного пароля
from simplecrypt import decrypt, DecryptionException

# Считываем зашифрованную информацию из бинарного файла
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

# Считываем пароли из файла с паролями
with open("passwords.txt") as pas:
    passwords = pas.read()

# Проходим по циклу паролей, чтобы подобрать необходимый нам
for password in passwords.split():
    try:
        # Печатаем расшифровку
        print(decrypt(password.strip(), encrypted))
    # Тут ловим исключение на случай, если пароль не верный
    except DecryptionException:
        print('Bad password')


