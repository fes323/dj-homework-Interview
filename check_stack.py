from stack import Stack


def list_to_str():
    data_stack = Stack.return_stack(self=Stack)
    stack = ''.join(data_stack)
    check_stack(stack)


def check_stack(stack):
    square_bracket = 0 # Квадратная скобка
    round_backet = 0 # Круглая скобка
    figurate_backet = 0 # Фигурная скобка

    for i in stack:
        if i == '[':
            square_bracket += 1
        if i == ']':
            square_bracket -= 1

        if i == '(':
            round_backet += 1
        if i == ')':
            round_backet -= 1

        if i == '{':
            figurate_backet += 1
        if i == '}':
            figurate_backet -= 1

    if square_bracket + round_backet + figurate_backet == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно')
