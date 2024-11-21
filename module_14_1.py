import sqlite3


def create_db():
    # Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
    ...

def create_table():
    # Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
    # Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
    # id - целое число, первичный ключ
    # username - текст (не пустой)
    # email - текст (не пустой)
    # age - целое число
    # balance - целое число (не пустой)
    ...


def fill_table():
    # Заполните её 10 записями:
    # User1, example1@gmail.com, 10, 1000
    # User2, example2@gmail.com, 20, 1000
    # User3, example3@gmail.com, 30, 1000
    # ...
    # User10, example10@gmail.com, 100, 1000
    # Обновите balance у каждой 2ой записи начиная с 1ой на 500:
    # User1, example1@gmail.com, 10, 500
    # User2, example2@gmail.com, 20, 1000
    # User3, example3@gmail.com, 30, 500
    # ...
    # User10, example10@gmail.com, 100, 1000
    # Удалите каждую 3ую запись в таблице начиная с 1ой:
    # User2, example2@gmail.com, 20, 1000
    # User3, example3@gmail.com, 30, 500
    # User5, example5@gmail.com, 50, 500
    # ...
    # User9, example9@gmail.com, 90, 500
    ...


def fetch_records():
    # Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
    # Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
    return ''


def main():
    create_db()
    create_table()
    fill_table()
    result = fetch_records()
    print(result)
    """
    Вывод на консоль:
    Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
    Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
    Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
    Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
    Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
    """


if __name__ == '__main__':
    main()


"""
2024/01/29 00:00|Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."
Если вы решали старую версию задачи, проверка будет производиться по ней.
Ссылка на старую версию тут.
Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.

Задача "Первые пользователи":
Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
id - целое число, первичный ключ
username - текст (не пустой)
email - текст (не пустой)
age - целое число
balance - целое число (не пустой)
Заполните её 10 записями:
User1, example1@gmail.com, 10, 1000
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 1000
...
User10, example10@gmail.com, 100, 1000
Обновите balance у каждой 2ой записи начиная с 1ой на 500:
User1, example1@gmail.com, 10, 500
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
...
User10, example10@gmail.com, 100, 1000
Удалите каждую 3ую запись в таблице начиная с 1ой:
User2, example2@gmail.com, 20, 1000
User3, example3@gmail.com, 30, 500
User5, example5@gmail.com, 50, 500
...
User9, example9@gmail.com, 90, 500

Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

Пример результата выполнения программы:
Вывод на консоль:
Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
Содержание БД:


Файл module_14_1.py с кодом и базу данных not_telegram.db загрузите на ваш GitHub репозиторий. В решении пришлите ссылку на него.
"""