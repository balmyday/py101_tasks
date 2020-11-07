"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное

def has_even(num_list):
    for n in num_list:
        if n % 2 == 0:
            print('has even number')
            return
    print('has no even numbers')    
    return   


# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
sell_alcohol()

def sell_alcohol():
    print("Выберите вашу водку")

def check_age(age):
    sell_alcohol() if age >= 21 else print("Мы не продаем алкоголь несовершеннолетним")


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()

import keyword 

def is_keyword(word):
    if keyword.iskeyword(word):
        print ('Is keyword in Phython')
    else:
        print ('Not a keyword')


# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(any_object):
    if isinstance(any_object, bool):
        print('Это булев тип')
    elif isinstance(any_object, float):
        print('Это число с точкой')
    elif isinstance(any_object, int):
        print('Это число')
    elif isinstance(any_object, list):
        print('Это список')
    elif isinstance(any_object, tuple):
        print('Это кортеж')
    elif isinstance(any_object, set):
        print('Это множество')
    elif isinstance(any_object, dict):
        print('Это словарь')
    elif isinstance(any_object, str):
        print('Это строка')
    elif any_object is None:
        print ('Это пустой тип')
    else:
        print('Неизвестная херня')

