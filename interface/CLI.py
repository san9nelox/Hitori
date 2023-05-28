help_message = '/help - чтобы увидеть список команд\n' \
               '/start - сгенерировать головоломку\n' \
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


def exit_func():
    print('Пока-пока')
    exit()
