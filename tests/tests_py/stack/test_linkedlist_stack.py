"""
Test Linkedlist Stack.

The following script contains tests for all the features of the linked-list
stack.
"""
import unittest

from dsa_py.stack.linkedlist_stack import LinkedlistStack


class TestLinkedlistStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = LinkedlistStack(size=4)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty(), True)

        self.stack.push(value=1)
        self.assertEqual(self.stack.is_empty(), False)

    def test_is_full(self):
        self.assertEqual(self.stack.is_full(), False)

        for value in [1, 2, 3, 4]:
            self.stack.push(value=value)

        self.assertEqual(self.stack.is_full(), True)

    def test_get_size(self):
        self.assertEqual(self.stack.get_size(), 0)

        for value in [1, 2, 3]:
            self.stack.push(value=value)

        self.assertEqual(self.stack.get_size(), 3)

    def test_push(self):
        for value in [1, 2, 3, 4]:
            self.stack.push(value=value)

        self.assertEqual(self.stack.traverse(), [4, 3, 2, 1])

        # A full stack must not accept another value.
        self.stack.push(value=5)
        self.assertEqual(self.stack.traverse(), [4, 3, 2, 1])

    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)

        for value in [1, 2, 3, 4]:
            self.stack.push(value=value)

        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.traverse(), [2, 1])

    def test_peek_top(self):
        self.assertEqual(self.stack.peek_top(), None)

        for value in [1, 2, 3]:
            self.stack.push(value=value)

        self.assertEqual(self.stack.peek_top(), 3)
        self.assertEqual(self.stack.get_size(), 3)

    def test_traverse(self):
        self.assertEqual(self.stack.traverse(), [])

        for value in [1, 2, 3, 4]:
            self.stack.push(value=value)

        self.assertEqual(self.stack.traverse(), [4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
