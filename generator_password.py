import random
import string

string_chars = string.digits + string.punctuation + string.ascii_letters

# Основная функция генератора паролей реализована ввиде циклов с ипсользованием методов из различных
# встроенных библиотек ("random", "string")

def generator(quantity, length):
    for number in range(quantity):
        password = ''
        for number in range(length):
            password += random.choice(string_chars)
            result = password
        else:
            print (result)
