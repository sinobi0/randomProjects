x = 50 # угаданное число
cnt = 0 # счетчик

while True: #бесконечный цикл
    user_number = int(input('Я загадал число от 1 до 100, угайдай его :D')) # ввод пользователя
    cnt += 1 # прибавляем кол-во попыток
    if user_number == x: # если пользователь угадал
        print(f'Ты угадал число за {cnt} попыток')
        print('Спасибо за игру!')
        break # выход из цикла
    elif user_number > x: # если пользователь ввёл число меньше угаданного
        print('Наше число меньше того, которое ты ввел')
    else: # если ввёл больше угаданного 
        print('Наше число больше того, которое ты ввел')