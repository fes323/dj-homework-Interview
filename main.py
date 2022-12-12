from stack import Stack
from check_stack import list_to_str
import sys


if __name__ == '__main__':

    while True:
        command_list = ('\n\nКоманды:\n'
                        'is_empty - проверка стека (пустой или нет)\n'
                        'push - добавить элемент\n'
                        'pop - удалить последний элемент\n'
                        'peek -  получить последний элемент\n'
                        'size - получить количество элементов в стеке\n'
                        'check - проверить стек на сбалансированность\n'
                        'help - отобразить команды\n'
                        'exit - выйти.')
        print(command_list)

        user_command = str(input('\nВведите команду: '))

        if user_command == 'is_empty':
            Stack.is_empty(self=Stack)
        if user_command == 'push':
            Stack.push(self=Stack, new_element=str(input('Введите новый элемент: ')))
        if user_command == 'pop':
            Stack.pop(self=Stack)
        if user_command == 'peek':
            Stack.peek(self=Stack)
        if user_command == 'size':
            Stack.size(self=Stack)
        if user_command == 'check':
            list_to_str()
        if user_command == 'help':
            print(command_list)
        if user_command == 'exit':
            sys.exit()