"""
Double Circular Linkedlist

The following file implements all the functionalities
within Base Linkedlist for Double Circular Linkedlist.
"""
from typing import List

from dsa_py.linkedlist.base_linkedlist import BaseLinkedlist, Node


class DoubleCircularLinkedlist(BaseLinkedlist):
    
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
            if current.next is self.head:
                break
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
            node.next = self.head
            node.prev = self.head
            return
        
        current = self.head
        while current.next is not self.head:
            current = current.next
        node.prev = current
        current.next = node
        node.next = self.head
        self.head.prev = node
    
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
            node.prev = self.head
            node.next = self.head
            return
        
        current = self.head
        while current:
            if current.next is self.head:
                break
            current = current.next
        node.next = self.head
        current.next = node
        node.prev = current
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
        node = Node(value=value)
        length = self.count_length()
        if idx < 0:
            return
        if idx > length:
            return
        
        if idx == 0:
            self.insert_start(value=value)
            return
        
        counter = 0
        current = self.head
        break_by_counter = False
        break_by_length = False
        while current:
            if current.next is self.head:
                break_by_length = True
                break
            counter += 1
            if counter == idx:
                break_by_counter = True
                break
            current = current.next
        if break_by_length:        
            current.next = node
            node.prev = current
            node.next = self.head
            self.head.prev = node
        if break_by_counter:
            node.next = current.next
            current.next.prev = node
            current.next = node
            node.prev = current
    
    def search_by_index(
        self,
        idx: int,
    ) -> int | None:
        """
        Search the value of the node by the index.
        
        Args:
            idx (int): The search position.

        Returns:
            int | None: The value found at the specific index.
        """
        if idx < 0:
            return None
        counter = 0
        found = None
        current = self.head
        while current:
            if counter == idx:
                found = current.value
            if current.next is self.head:
                break
            counter += 1
            current = current.next
        return found
    
    def search_by_value(
        self,
        value: int,
    ) -> int | None:
        """
        Searches the linkedlist by value and return the index.
        
        Args:
            value (int): The value to be searched within the linkelist.

        Returns:
            int | None: The position at which the value was found.
        """
        found = None
        counter = 0
        current = self.head
        while current:
            if current.value == value:
                found = counter
                break
            if current.next is self.head:
                break
            counter += 1
            current = current.next
        return found
    
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
        if idx < 0:
            return
        if idx > self.count_length():
            return
        
        counter = 0
        current = self.head
        while current:
            if counter == idx:
                current.value = value
            if current.next is self.head:
                break
            counter += 1
            current = current.next
    
    def delete_start(
        self,
    ) -> None:
        """
        Delete the first node in the linkedlist.
        """
        if self.is_empty():
            return None
        
        current = self.head
        while current:
            if current.next is self.head:
                self.head.next.prev = current
                current.next = self.head.next
                break
            current = current.next
            
        self.head = self.head.next
    
    def delete_end(
        self,
    ) -> None:
        """
        Delete the last node in the linkedlist.
        """
        if self.is_empty():
            return None
        
        current = self.head
        while current:
            if current.next.next is self.head:
                current.next.prev = None
                current.next.next = None
                current.next = self.head
                self.head.prev = current
                break
            current = current.next

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
        counter = 0
        current = self.head
        while current:
            counter += 1
            if current.next is self.head:
                break
            current = current.next
        return counter
    
    def reverese(
        self,
    ) -> None:
        """
        Shows a linkedlist in a reverse order.
        """
        pass
