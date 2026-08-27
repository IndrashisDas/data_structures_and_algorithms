"""
Double Linkedlist

The following file implements all the functionalities
within Base Linkedlist for Double Linkedlist.
"""
from typing import List

from dsa_py.linkedlist.base_linkedlist import BaseLinkedlist, Node


class DoubleLinkedlist(BaseLinkedlist):
    
    def __init__(
        self,
    ) -> None:
        super().__init__()
    
    def show_linkedlist(
        self,
    ) -> List[int]:
        """
        Prints the linkedlist.

        Returns:
            List[int]: The linkedlist node values
        """
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values
    
    def is_empty(
        self,
    )-> bool:
        """
        Checks if the linkedlist is empty or not.
        
        Returns:
            bool: True if empty, False if not empty.
        """
        return True if self.head is None else False
    
    def insert(
        self,
        value: int,
    ) -> None:
        """
        Insert a node to the linkedlist.
        
        Args:
            value (int): The integer value to be held by the new node.
        """
        node = Node(value=value)
        if self.is_empty():
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        node.prev = current
        current.next = node
    
    def insert_start(
        self,
        value: int,
    ) -> None:
        """
        Allows to insert a node at the beginning of the linekdlist.

        Args:
            value (int): The integer value to be held by the new node.
        """
        node = Node(value=value)
        if self.is_empty():
            self.head = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    
    def insert_by_index(
        self,
        idx: int,
        value: int,
    ) -> None:
        """
        Allows to insert a node at a specific position in the linkedlist.
        
        Args:
            idx (int): The index at which the node is to be inserted.
            value (int): The integer value to be held by the new node.
        """
        pass
    
    def search_by_index(
        self,
        idx: int,
    ) -> int:
        """
        Search the value of the node by the index.
        
        Args:
            idx (int): The search position.

        Returns:
            int: The value found at the specific index.
        """
        pass
    
    def search_by_value(
        self,
        value: int,
    ) -> int:
        """
        Searches the linkedlist by value and return the index.
        
        Args:
            value (int): The value to be searched within the linkelist.

        Returns:
            int: The position at which the value was found.
        """
        pass
    
    def update_by_index(
        self,
        idx: int,
        value: int,
    ) -> None:
        """
        Updates the linkedlist at a specific index with 
        a value.
        
        Args:
            idx (int): The index at which the node's 
                value needs to be updated.
            value (int): The value that replaces the 
                existing node's value.
        """
        pass
    
    def update_by_value(
        self,
        value: int,
        all: bool = False,
    ) -> None:
        """
        Updates a node by value. You can update either only 
        the first occurence or all the occurences of the same
        value in the linkedlist.

        Args:
            value (int): Value is the value to be searched and updated.
            all (bool, optional): Decides if you update the first occurence
                or all the occurences of the node. Defaults to False.
        """
        pass
    
    def delete_start(
        self,
    ) -> None:
        """
        Delete the first node in the linkedlist.
        """
        pass
    
    def delete_end(
        self,
    ) -> None:
        """
        Delete the last node in the linkedlist.
        """
        pass
    
    def delete_by_index(
        self,
        idx: int,
    ) -> None:
        """
        Deletes a node by the given index.
        
        Args:
            idx (int): The node at this position is deleted.
        """
        pass
    
    def delete_by_value(
        self,
        value: int,
        all: bool = False,
    ) -> None:
        """
        Deletes a node by value. You can delete either only 
        the first occurence or all the occurences of the same
        value in the linkedlist.

        Args:
            value (int): Value is the value to be searched and deleted.
            all (bool, optional): Decides if you delete the first occurence
                or all the occurences of the node. Defaults to False.
        """
        pass
    
    def count_length(
        self,
    ) -> int:
        """
        Counts the number of elements in a linkedlist.

        Returns:
            int: The number of elements in a linkedlist.
        """
        pass
    
    def reverese(
        self,
    ) -> None:
        """
        Shows a linkedlist in a reverse order.
        """
        pass
