from random import choice


def get_employees():
    surname = ['Собянин', 'Лавров', 'Песков']
    name_lastname = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'
    return (f"{choice(surname)} {choice(name_lastname)}.{choice(name_lastname)}.")