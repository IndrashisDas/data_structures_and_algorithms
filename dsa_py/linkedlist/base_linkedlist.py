"""
Base Linkedlist

The following file contains the code for the base linkedlist 
which is inherited by different types of other linkedlists.
All the possible linkedlist implementations include:
    - Single Linkedlist
    - Double Linkedlist
    - Single Circular Linkedlist
    - Double Circular Linkedlist
"""
from dataclasses import dataclass
from typing import Any, Tuple


@dataclass(frozen=True)
class Node:
    value: int
    reference: Any
    
    
class BaseLinkedlist:
    
    def __init__(
        self,
    ) -> None:
        """
        Initializes the BaseLinkedlist
        """
        self.head: Node | None = None
    
    def is_empty(
        self,
    )-> bool:
        """
        Checks if the linkedlist is empty or not.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            idx (int): The index at which the node is to be inserted.
            value (int): The integer value to be held by the new node.
        """
        raise NotImplementedError
    
    def search_by_index(
        self,
        idx: int,
    ) -> int:
        """
        Search the value of the node by the index.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            idx (int): The search position.

        Returns:
            int: The value found at the specific index.
        """
        raise NotImplementedError
    
    def search_by_value(
        self,
        value: int,
    ) -> int:
        """
        Searches the linkedlist by value and return the index.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            value (int): The value to be searched within the linkelist.

        Returns:
            int: The position at which the value was found.
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            idx (int): The index at which the node's 
                value needs to be updated.
            value (int): The value that replaces the 
                existing node's value.
        """
        raise NotImplementedError
    
    def update_by_value(
        self,
        value: int,
        all: bool = False,
    ) -> None:
        """
        Updates a node by value. You can update either only 
        the first occurence or all the occurences of the same
        value in the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            value (int): Value is the value to be searched and updated.
            all (bool, optional): Decides if you update the first occurence
                or all the occurences of the node. Defaults to False.
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            idx (int): The node at this position is deleted.
        """
        raise NotImplementedError
    
    def delete_by_value(
        self,
        value: int,
        all: bool = False,
    ) -> None:
        """
        Deletes a node by value. You can delete either only 
        the first occurence or all the occurences of the same
        value in the linkedlist.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Args:
            value (int): Value is the value to be searched and deleted.
            all (bool, optional): Decides if you delete the first occurence
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
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------

        Returns:
            int: The number of elements in a linkedlist.
        """
        raise NotImplementedError
    
    def reverese(
        self,
    ) -> None:
        """
        Shows a linkedlist in a reverse order.
        
        --------------------------------------------------------------------
        |          Method            | Time Complexity | Memory Complexity |
        --------------------------------------------------------------------
        | Single Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Double Linkedlist          |                 |                   |
        --------------------------------------------------------------------
        | Single Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        | Double Circular Linkedlist |                 |                   |
        --------------------------------------------------------------------
        """
        raise NotImplementedError
