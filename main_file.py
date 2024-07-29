import string
import generator_password

string_chars = string.digits + string.punctuation + string.ascii_letters

input_for_exit = "exit"

input_1 = 'Введите количество генераций паролей (или "exit" для выхода):'

input_2 = 'Введите количество (число) знаков в пароле (или "exit" для выхода):'

error = 'Неверный формат вводимых данных! Попробуйте ещё раз...'

break_flag = False

# Основной файл генератора пароля представляет собой цикл из запросов на ввод данных с возможностью прерывания
# цикла в любой момент, с защитой от некоректно введенных данных - и дальнейшим вызовом функции генератора пароля.
# Вводимые данные: (1) количество генераций и (2) количество знаков в генерируемых строках
# для генерации пароля(ей).

i = 0
while i == 0:
    quantity = input(f"""
{input_1}
""")
    if quantity == input_for_exit:
        break
    else:
        while str.isdigit(quantity) != True:
            if quantity == input_for_exit:
                break_flag = True
                break
            else:
                print(error)
                quantity = input(f"""
{input_1}
""")
        if break_flag:
            break
        else:
            quantity = int(quantity)

        length = input(f"""
{input_2}
""")
        if length == input_for_exit:
            break
        else:
            while str.isdigit(length) != True:
                if length == input_for_exit:
                    break_flag = True
                    break
                else:
                    print(error)
                    length = input(f"""
{input_2}
""")
        if break_flag:
            break
        else:
            length = int(length)

        print(f"""
Количество паролей: {quantity}
Количество знаков в пароле(ях) {length}:

Результат:""")
        generator_password.generator(quantity, length)
