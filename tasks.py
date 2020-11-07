
### Function to check if list of numbers contains at least even number 

def has_even(num_list):
    for n in num_list:
        if n % 2 == 0:
            print('has even number')
            return
    print('has no even numbers')    
    return   

### Function to check if user is 21 or older

def sell_alcohol():
    print("Выберите вашу водку")

def check_age(age):
    sell_alcohol() if age >= 21 else print("Мы не продаем алкоголь несовершеннолетним")

### check_age(25)

 ### keyword 

import keyword 

#print(dir(keyword))

def is_keyword(word):
    if keyword.iskeyword(word):
        print ('Is keyword in Phython')
    else:
        print ('Not a keyword')

is_keyword('def')

### Function to return type of the input in Russian 

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
