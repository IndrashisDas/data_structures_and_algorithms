"""
Single Linkedlist Stack implementation

The following file implements all the functionalities
within Base Stack for Single Linkedlist Stack.
"""
from typing import List

from dsa_py.stack.base_stack import BaseStack, LinkedlistNode


class LinkedlistStack(BaseStack):
    
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
        count = 0
        current = self.linkedlist_stack
        while current:
            current = current.next
            count += 1
        return count
    
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
        node = LinkedlistNode(value=value)
        if self.is_full():
            return
        if self.is_empty():
            self.linkedlist_stack = node
            return
        node.next = self.linkedlist_stack
        self.linkedlist_stack = node
    
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
        value = self.linkedlist_stack.value
        self.linkedlist_stack = self.linkedlist_stack.next
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
        return self.linkedlist_stack.value
        
    def traverse(
        self,
    ) -> List[int] | None:
        """
        Traverses the complete stack.

        Returns:
            List[int] | None: The complete stack
        """
        stack = []
        current = self.linkedlist_stack
        while current:
            stack.append(current.value)
            current = current.next
        return stack
