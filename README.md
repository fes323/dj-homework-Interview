# n-homework-Interview

**Стек** - абстрактный тип данных, представляющий собой список элементов, организованных по принципу *LIFO (англ. last in — first out, «последним пришёл — первым вышел»)*. Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии(стрельба начнётся с патрона, заряженного последним).

1. Необходимо реализовать класс Stack со следующими методами:

- is_empty - проверка стека на пустоту. Метод возвращает True или False.
- push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
- pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
- peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
- size - возвращает количество элементов в стеке.

2. Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.

Пример сбалансированных последовательностей скобок:

- ```(((([{}]))))```
- ```[([])((([[[]]])))]{()}```
- ```{{[()]}}```

Несбалансированные последовательности:

- ```}{}```
- ```{{[(])]}}```
- ```[[{())}]```

Программа ожидает на вход строку со скобками. На выход сообщение: "Сбалансированно", если строка корректная, и "Несбалансированно", если строка составлена неверно.
