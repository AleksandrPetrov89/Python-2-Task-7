from tasks.stack import Stack


def parenthesis_check(line: str) -> str:
    """
    Осуществляет проверку сбалансированности скобок.

    Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий
    ему закрывающий, и пары скобок правильно вложены друг в друга.

    :param line: строка со скобками
    :return: строка с ответом - "Сбалансированно" или "Несбалансированно"
    """
    stack_1 = Stack()
    comparison = {")": "(", "]": "[", "}": "{"}
    for symbol in line.strip():
        if symbol in "([{":
            stack_1.push(symbol)
        elif symbol in ")]}" and not stack_1.is_empty() and stack_1.peek() == comparison[symbol]:
            stack_1.pop()
        else:
            return "Несбалансированно"
    if stack_1.is_empty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"
