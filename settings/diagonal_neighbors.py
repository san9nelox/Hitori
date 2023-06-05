are_horiz_neigh_diff = False


def switch():
    global are_horiz_neigh_diff
    answer = input(f'Вы хотите переключить правило диагональных соседей?\n'
                   f'В настоящий момент значени {are_horiz_neigh_diff}\n'
                   f'False - выключено, True - включено\n'
                   f'Введите y/n: ')
    match answer:
        case 'y':
            are_horiz_neigh_diff = not are_horiz_neigh_diff
        case 'n':
            pass
        case _:
            print('Неверный ввод')
