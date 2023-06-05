are_diagonal_neighbors_different = False


def switch():
    global are_diagonal_neighbors_different
    answer = input(f'Вы хотите переключить правило диагональных соседей?\n'
                   f'В настоящий момент значени {are_diagonal_neighbors_different}\n'
                   f'False - выключено, True - включено\n'
                   f'Введите y/n')
    match answer:
        case 'y':
            are_diagonal_neighbors_different = not are_diagonal_neighbors_different
        case 'n':
            pass
        case _:
            print('Неверный ввод')
