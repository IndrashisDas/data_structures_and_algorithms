"""
Single Linkedlist implementation

The following file implements all the functionalities
within Base Linkedlist for Single Linkedlist.
"""
from typing import List

from dsa_py.linkedlist.base_linkedlist import BaseLinkedlist, Node


class SingleLinkedlist(BaseLinkedlist):
    
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
        if idx < 0:
            return
        if idx > self.count_length():
            return
        
        if idx == 0:
            self.insert_start(value=value)
            return
        
        counter = 0
        current = self.head
        while current:
            counter += 1
            if counter == idx:
                break
            current = current.next
        node.next = current.next
        current.next = node
    
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
            if current.next.next is None:
                current.next = None
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
        if idx < 0:
            return
        if idx > self.count_length():
            return
        if self.is_empty():
            return
        
        if idx == 0:
            self.delete_start()
            return
        
        counter = 0
        current = self.head
        while current:
            if counter + 1 == idx:
                current.next = current.next.next
                break
            current = current.next
            counter += 1
    
    def delete_by_value(
        self,
        value: int,
        delete_all: bool = False,
    ) -> None:
        """
        Deletes a node by value. You can delete either only 
        the first occurence or all the occurences of the same
        value in the linkedlist.

        Args:
            value (int): Value is the value to be searched and deleted.
            delete_all (bool, optional): Decides if you delete the first occurence
                or all the occurences of the node. Defaults to False.
        """
        previous = None
        current = self.head
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                if not delete_all:
                    break

                current = current.next
                continue

            previous = current
            current = current.next
    
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
            current = current.next
        return counter
            
    def reverse(
        self,
    ) -> None:
        """
        Shows a linkedlist in a reverse order.
        """
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
