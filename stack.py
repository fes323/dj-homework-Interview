class Stack():

    data_stack = str(input('Введите стек: '))
    stack = list(data_stack)

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return print(True)
        else:
            return print(False)

    def push(self, new_element):
        self.stack.append(new_element)

    def pop(self):
        # -1 т.к. индексы с 0, а len считает с 1
        len_stack = len(self.stack) - 1
        self.stack.pop()
        # -1 т.к. последний элемент мы удалили
        return print(f'Последний элемент после удаления: {self.stack[len_stack - 1]}')

    def peek(self):
        len_stack = len(self.stack) - 1
        return print(f'Последний элемент стека: {self.stack[len_stack]}')

    def size(self):
        return print(f'Количество элементов в стеке: {len(self.stack)}')

    def return_stack(self):
        export_stack = self.stack
        return export_stack