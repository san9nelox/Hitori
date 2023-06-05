help_message = '/help - чтобы увидеть список команд\n' \
               '/start - сгенерировать головоломку\n' \
               '/solve - узнать, можно ли решить головоломку с заданным полем\n' \
               '/switch - переключить диагональное правило\n' \
               '/exit - завершить работу\n'

wrong_case_message = 'Неизвестная команда\n'


def all_func():
    global help_message, wrong_case_message
    start_message = f'Привет! это игра Хитори. Ты в режиме разработчика\n' \
                    f'{help_message}'
    print(start_message)
    while True:
        user_message = input("Введите команду: ")
        match user_message:
            case "/help":
                help_func()
            case "/start":
                start_func()
            case "/solve":
                solve_func()
            case "/switch":
                switch_func()
            case "/exit":
                exit_func()
            case _:
                print(wrong_case_message)


def help_func():
    global help_message
    print(help_message)


def start_func():
    from hitori_logic.find_solution import hitori_solution
    hitori_solution()
    print()


def solve_func():
    from hitori_logic.find_solution import can_solve
    can_solve()
    print()


def switch_func():
    from settings.diagonal_neighbors import switch
    switch()
    print()


def exit_func():
    print('Пока-пока')
    exit()
