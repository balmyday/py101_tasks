"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
import random

if __name__ == '__main__':
	min_v = 1
	max_v = 10000000
	num = random.randint(min_v, max_v)
	print(f'Hello! Guess a number from {min_v} to {max_v}.')
	while True:
	    user_input = input('Enter your guess: ')
	    if 'exit' in user_input or len(user_input) == 0:
	        print('looser')
	        break 
	    if not user_input.isdigit():
	        print('It\'s not a number,looser. Try again')
	        continue
	    user_number = int(user_input)
	    if user_number < min_v or user_number > max_v:
	        print('Your number is out of range. Try again') 
	        continue
	    if user_number > num:
	        print('Your number is greater than mine')
	    if user_number < num:    
	        print('Your number is less than mine')
	    if user_number == num: 
	        print('You won!')
	        break


