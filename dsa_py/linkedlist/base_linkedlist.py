"""
Base Linkedlist implementation

The following file contains the code for the base linkedlist 
which is inherited by different types of other linkedlists.
All the possible linkedlist implementations include:
    - Single Linkedlist
    - Double Linkedlist
    - Single Circular Linkedlist
    - Double Circular Linkedlist
"""
from dataclasses import dataclass
from typing import Any, List


@dataclass
class Node:
    value: int
    next: Any | None = None
    prev: Any | None = None
    
    
class BaseLinkedlist:
    
    def __init__(
        self,
    ) -> None:
        """
        Initializes the BaseLinkedlist
        """
        self.head: Node | None = None
    
    def show_linkedlist(
        self,
    ) -> List[int]:
        """
        Prints the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(n)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(n)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(n)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(n)        |
        --------------------------------------------------------------------

        Returns:
            List[int]: The linkedlist node values
        """
        raise NotImplementedError
    
    def is_empty(
        self,
    )-> bool:
        """
        Checks if the linkedlist is empty or not.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(1)      |        O(1)       |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(1)      |        O(1)       |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(1)      |        O(1)       |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(1)      |        O(1)       |
        --------------------------------------------------------------------

        Returns:
            bool: True if empty, False if not empty.
        """
        raise NotImplementedError
    
    def insert(
        self,
        value: int,
    ) -> None:
        """
        Insert a node to the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            value (int): The integer value to be held by the new node.
        """
        raise NotImplementedError
    
    def insert_start(
        self,
        value: int,
    ) -> None:
        """
        Allows to insert a node at the beginning of the linekdlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(1)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(1)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            value (int): The integer value to be held by the new node.
        """
        raise NotImplementedError
    
    def insert_by_index(
        self,
        idx: int,
        value: int,
    ) -> None:
        """
        Allows to insert a node at a specific position in the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            idx (int): The index at which the node is to be inserted.
            value (int): The integer value to be held by the new node.
        """
        raise NotImplementedError
    
    def search_by_index(
        self,
        idx: int,
    ) -> int | None:
        """
        Search the value of the node by the index.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            idx (int): The search position.

        Returns:
            int | None: The value found at the specific index.
        """
        raise NotImplementedError
    
    def search_by_value(
        self,
        value: int,
    ) -> int | None:
        """
        Searches the linkedlist by value and return the index.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            value (int): The value to be searched within the linkelist.

        Returns:
            int | None: The position at which the value was found.
        """
        raise NotImplementedError
    
    def update_by_index(
        self,
        idx: int,
        value: int,
    ) -> None:
        """
        Updates the linkedlist at a specific index with 
        a value.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            idx (int): The index at which the node's 
                value needs to be updated.
            value (int): The value that replaces the 
                existing node's value.
        """
        raise NotImplementedError
    
    def delete_start(
        self,
    ) -> None:
        """
        Delete the first node in the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(1)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(1)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        """
        raise NotImplementedError
    
    def delete_end(
        self,
    ) -> None:
        """
        Delete the last node in the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        """
        raise NotImplementedError
    
    def delete_by_index(
        self,
        idx: int,
    ) -> None:
        """
        Deletes a node by the given index.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            idx (int): The node at this position is deleted.
        """
        raise NotImplementedError
    
    def delete_by_value(
        self,
        value: int,
        delete_all: bool = False,
    ) -> None:
        """
        Deletes a node by value. You can delete either only 
        the first occurence or all the occurences of the same
        value in the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Args:
            value (int): Value is the value to be searched and deleted.
            delete_all (bool, optional): Decides if you delete the first occurence
                or all the occurences of the node. Defaults to False.
        """
        raise NotImplementedError
    
    def count_length(
        self,
    ) -> int:
        """
        Counts the number of elements in a linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------

        Returns:
            int: The number of elements in a linkedlist.
        """
        raise NotImplementedError
    
    def reverse(
        self,
    ) -> None:
        """
        Shows a linkedlist in a reverse order.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Linkedlist          |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |       O(n)      |       O(1)        |
        --------------------------------------------------------------------
        """
        raise NotImplementedError
