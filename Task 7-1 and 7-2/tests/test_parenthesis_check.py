import pytest

from tasks.parenthesis_check import parenthesis_check


fixture = [
    ("(((([{}]))))", "Сбалансированно"),
    ("[([])((([[[]]])))]{()}", "Сбалансированно"),
    ("{{[()]}}", "Сбалансированно"),
    ("}{}", "Несбалансированно"),
    ("{{[(])]}}", "Несбалансированно"),
    ("[[{())}]", "Несбалансированно")
]


@pytest.mark.parametrize("line, result", fixture)
def test_parenthesis_check(line, result):
    assert parenthesis_check(line) == result
