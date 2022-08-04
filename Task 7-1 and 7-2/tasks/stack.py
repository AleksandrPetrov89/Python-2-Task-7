class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        """
        Проверка стека на пустоту.

        :return: True - если стек пустой, False - если не пустой.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        """
        Добавляет новый элемент на вершину стека.

        :param element: элемент, который необходимо добавить.
        :return: Метод ничего не возвращает.
        """
        self.stack.append(element)

    def pop(self):
        """
        Удаляет верхний элемент стека. Стек изменяется.

        :return: Метод возвращает верхний элемент стека
        """
        return self.stack.pop()

    def peek(self):
        """
        Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.

        :return: Метод возвращает верхний элемент стека
        """
        return self.stack[-1]

    def size(self) -> int:
        """
        Возвращает количество элементов в стеке.

        :return: целое число, обозначающее количество элементов в стеке.
        """
        return len(self.stack)
