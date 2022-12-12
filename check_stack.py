from stack import Stack


def list_to_str():
    data_stack = Stack.return_stack(self=Stack)
    stack = ''.join(data_stack)
    check_stack(stack)


def check_stack(stack):

    data_list_stack = []

    for i in stack:
        if i == '(':
            data_list_stack.append(i)
        if i == ')':
            len_new_list = len(data_list_stack) - 1
            if data_list_stack[len_new_list] == '(':
                data_list_stack.pop()

        if i == '[':
            data_list_stack.append(i)
        if i == ']':
            len_new_list = len(data_list_stack) - 1
            if data_list_stack[len_new_list] == '[':
                data_list_stack.pop()

        if i == '{':
            data_list_stack.append(i)
        if i == '}':
            len_new_list = len(data_list_stack) - 1
            if data_list_stack[len_new_list] == '{':
                data_list_stack.pop()

    if len(data_list_stack) == 0:
        print('Сбалансированно')
    else:
        print('Несбалансированно')