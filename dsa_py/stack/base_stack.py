"""
Base Stack implementation

The following file contains the code for the base stack 
which is inherited by different types of other stacks.
All the possible stack implementations include:
    - Simple Array Stack
    - Linkedlist Stack
"""
from dataclasses import dataclass
from typing import Any, List


@dataclass
class LinkedlistNode:
    value: int
    next: Any | None = None
    

class BaseStack:
    
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
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(n)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(n)       |        O(1)        |
        ----------------------------------------------------------------

        Returns:
            int: The current number of elements in the stack.
        """
        raise NotImplementedError
    
    def is_full(
        self,
    ) -> bool:
        """
        Checks if the stack is full.
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(n)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(n)       |        O(1)        |
        ----------------------------------------------------------------

        Returns:
            bool: True if full else False
        """
        raise NotImplementedError
    
    def is_empty(
        self,
    ) -> bool:
        """
        Checks if the stack is empty.
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(1)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(1)       |        O(1)        |
        ----------------------------------------------------------------

        Returns:
            bool: True if empty else False
        """
        raise NotImplementedError
    
    def push(
        self,
        value: int
    ) -> None:
        """
        Pushes an element into the stack.
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(1)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(1)       |        O(1)        |
        ----------------------------------------------------------------

        Args:
            value (int): The value to be pushed to the stack
        """
        raise NotImplementedError
    
    def pop(
        self,
    ) -> int | None:
        """
        Removes the top element from the stack.
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(1)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(1)       |        O(1)        |
        ----------------------------------------------------------------

        Returns:
            int | None: The removed element and its value
        """
        raise NotImplementedError
    
    def peek_top(
        self,
    ) -> int | None:
        """
        Retrieves the top element without popping it.
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(1)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(1)       |        O(1)        |
        ----------------------------------------------------------------

        Returns:
            int | None: The value of the last element
        """
        raise NotImplementedError
        
    def traverse(
        self,
    ) -> List[int] | None:
        """
        Traverses the complete stack.
        
        ----------------------------------------------------------------
        |        Method       |  Time Complexity  |  Memory Complexity |
        ----------------------------------------------------------------
        | Simple Array Stack  |        O(n)       |        O(1)        |
        ----------------------------------------------------------------
        | Linkedlist Stack    |        O(n)       |        O(1)        |
        ----------------------------------------------------------------

        Returns:
            List[int] | None: The complete stack
        """
        raise NotImplementedError
    