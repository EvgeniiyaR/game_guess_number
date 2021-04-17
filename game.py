import random


def is_valid_right(r):
    if r.isdigit() and int(r) > 0:
        return True
    return False


def is_valid(s):
    if s.isdigit() and 1 <= int(s) <= int(right_n):
        return True
    return False


def right_num():
    print('Укажите правую границу числа:')
    global right_n
    while True:
        right_n = input()
        if is_valid_right(right_n):
            return int(right_n)
        else:
            print('Укажите положительное число от 1:')


def input_num():
    print('Введите число от 1 до ', right_n, ':', sep='')
    while True:
        predict_num = input()
        if is_valid(predict_num):
            return int(predict_num)
        else:
            print('А может быть все-таки введем целое число от 1 до ', right_n, '?', sep='')


def game(new_game=True):
    if new_game:
        print('Добро пожаловать в числовую угадайку')
    num = random.randint(1, right_num())
    try_predict = 0
    flag = False
    final_result = 0

    while True:
        if flag:
            break

        pr = input_num()
        try_predict += 1

        while pr > 0:
            if pr > num:
                print('Слишком много, попробуйте еще раз')
                pr = input_num()
                try_predict += 1
                continue

            elif pr < num:
                print('Слишком мало, попробуйте еще раз')
                pr = input_num()
                try_predict += 1
                continue

            else:
                if final_result == 0:
                    print('Вы угадали, поздравляем!')
                    print('Количество попыток:', try_predict)
                    final_result += 1
                again = input('Вы хотите сыграть еще? (Напишите "y" - да или "n" - нет): ')
                if again == 'y':
                    game(new_game=False)
                elif again == 'n':
                    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                    flag = True
                    break
                else:
                    print('Введите "y" - да или "n" - нет')


game()
