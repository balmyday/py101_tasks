"""
Программа оценивает сложность пароля.

Пользователь вводит пароль, в ответ получает оценку "сложный"/"простой"
Сложным считается пароль, состоящий как минимум из 8-ми символов,
включая цифры и алфавитные символы
"""
def has_alpha_and_digit(pswd):
    return any(c.isalpha() for c in pswd) and any(c.isdigit() for c in pswd)

if __name__ == '__main__':
  
	password = input()
	if len(password) < 8:
	    print("Password is too easy")
	elif not has_alpha_and_digit(password):
	    print("Password is too easy")
	else:
	    print("ok")