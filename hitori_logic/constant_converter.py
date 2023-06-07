import json


def to_tuple(some_str: str):
    trans_table = {ord(','): None, ord(')'): None, ord('('): None}
    return str_to_int(some_str.translate(trans_table).split())


def str_to_int(list_str):
    a = int(list_str[0])
    b = int(list_str[1])
    c = int(list_str[2])
    return (a, b, c)


# Цвета
with open('constants/CONST.json', 'r', encoding='UTF-8') as json_file:
    file = json.load(json_file)
    black = to_tuple(file["black"])
    white = to_tuple(file["white"])
    gray = to_tuple(file["gray"])


def return_color():
    return black, white, gray
