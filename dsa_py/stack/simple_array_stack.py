"""
Simple Array Stack implementation

The following file implements all the functionalities
within Base Stack for Simple Array Stack.
"""
from typing import List

from dsa_py.stack.base_stack import BaseStack, LinkedlistNode


class SimpleArrayStack(BaseStack):
    
    def __init__(
        self,
        size: int
    ) -> None:
        """
        Initialize the base stack.

        Args:
            size (int): The expected maximum size of the stack
        """
        self.linkedlist_stack: LinkedlistNode | None = None
        self.array_stack: List = []
        self.size = size
    
    def get_size(
        self,
    ) -> int:
        """
        Gets the size of the stack.

        Returns:
            int: The current number of elements in the stack.
        """
        return len(self.array_stack)
    
    def is_full(
        self,
    ) -> bool:
        """
        Checks if the stack is full.

        Returns:
            bool: True if full else False
        """
        return self.get_size() >= self.size
    
    def is_empty(
        self,
    ) -> bool:
        """
        Checks if the stack is empty.

        Returns:
            bool: True if empty else False
        """
        return self.get_size() == 0
    
    def push(
        self,
        value: int
    ) -> None:
        """
        Pushes an element into the stack.

        Args:
            value (int): The value to be pushed to the stack
        """
        if self.is_full():
            return
        self.array_stack.append(value)
    
    def pop(
        self,
    ) -> int | None:
        """
        Removes the top element from the stack.

        Returns:
            int | None: The removed element and its value
        """
        if self.is_empty():
            return None
        value = self.array_stack[-1]
        self.array_stack = self.array_stack[:-1]
        return value
    
    def peek_top(
        self,
    ) -> int | None:
        """
        Retrieves the top element without popping it.

        Returns:
            int | None: The value of the last element
        """
        if self.is_empty():
            return None
        return self.array_stack[-1]
        
    def traverse(
        self,
    ) -> List[int] | None:
        """
        Traverses the complete stack.

        Returns:
            List[int] | None: The complete stack
        """
        return [self.array_stack[-idx-1] for idx, _ in enumerate(self.array_stack)]
