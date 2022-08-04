import pytest

from tasks.stack import Stack


class TestStack:

    stack_1 = Stack()

    fixture = [
        ([], True),
        ([1, 2, 3], False),
        ([], True)
    ]

    @pytest.mark.parametrize("stack, result", fixture)
    def test_is_empty(self, stack, result):
        self.stack_1.stack = stack
        assert self.stack_1.is_empty() == result

    fixture = [
        (1, [1]),
        ("a", [1, "a"]),
        ("aSdgfaf", [1, "a", "aSdgfaf"])
    ]

    @pytest.mark.parametrize("element, result", fixture)
    def test_push(self, element, result):
        self.stack_1.push(element)
        assert self.stack_1.stack == result

    fixture = [
        ("aSdgfaf", [1, "a"]),
        ("a", [1]),
        (1, [])
    ]

    @pytest.mark.parametrize("result, stack", fixture)
    def test_pop(self, result, stack):
        assert self.stack_1.pop() == result
        assert self.stack_1.stack == stack

    fixture = [
        ([1, "a", "aSdgfaf"], "aSdgfaf"),
        ([1, "a"], "a"),
        ([1], 1)
    ]

    @pytest.mark.parametrize("stack, result", fixture)
    def test_peek(self, stack, result):
        self.stack_1.stack = stack
        assert self.stack_1.peek() == result

    fixture = [
        ([1, "a", "aSdgfaf"], 3),
        ([1, "a"], 2),
        ([1], 1)
    ]

    @pytest.mark.parametrize("stack, result", fixture)
    def test_size(self, stack, result):
        self.stack_1.stack = stack
        assert self.stack_1.size() == result
