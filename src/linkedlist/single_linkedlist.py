"""
Implementation of Single Linkedlist.
"""
from typing import List
from .base_linkedlist import NodeSingle, BaseLinkedList


class SingleLinkedList(BaseLinkedList):
    
    def __init__(
        self,
    ) -> None:
        """
        Initialize the SingleLinkedList
        """
        self.head = None
        
    def is_empty(
        self,
    ) -> bool:
        """
        Checks if the linkedlist is empty
        
        Time complexity: O(1)

        Returns:
            bool: True if empty else False
        """
        return self.head is None  # None implies empty linkedlist
    
    def create_list(
        self,
        elements: List[int],
    ) -> None:
        """
        Creates a linkedlist and inserts all elements
        
        Time complexity: O(n^2)
        
        Args:
            elements (List[int]): The list of elements to be inserted into the linkedlist
        """
        # Create a linkedlist if it is empty else no
        if not self.is_empty():
            return
        
        for element in elements:
            node = NodeSingle(element)
            # Checks the base case if there is no element in the linkedlist
            if self.head is None:  
                self.head = node
            # Appends the new node after the last element of the linkedlist
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node
    
    def traverse_and_print(
        self,
    ) -> None:
        """
        Traverses the linkedlist and prints all its elements
        
        Time complexity - O(n)
        """
        if self.is_empty():
            print("SingleLinkedList is empty")
            return
        
        # Current tells us which node is being processed at the moment
        current = self.head
        while current is not None:
            if current.next is not None:
                print(current.data, end=" -> ")
            else:
                print(current.data, end=" -> None")
            current = current.next
    
    def clear_list(
        self,
    ) -> None:
        """
        Clears the complete linkedlist and deletes all existing nodes
        """
        if self.is_empty():
            return
        
        current = self.head
        while current is not None:
            # If you directly set current.next = None without next_node
            next_node = current.next
            current.next = None
            current = next_node
        self.head = None  # Best is to directly set self.head = None without doing anything else

    
    def insert_at_index(self,) -> None:
        raise NotImplementedError
    
    def insert_before_value(self,) -> None:
        raise NotImplementedError
    
    def insert_after_value(self,) -> None:
        raise NotImplementedError
    
    def delete_before_value(self,) -> None:
        raise NotImplementedError
    
    def delete_after_value(self,) -> None:
        raise NotImplementedError
    
    def delete_at_index(self,) -> None:
        raise NotImplementedError
    
    def delete_by_value(self,) -> None:
        raise NotImplementedError
    
    def update_node_by_value(self,) -> None:
        raise NotImplementedError
    
    def update_node_by_index(self,) -> None:
        raise NotImplementedError
    
    def search_element_by_value(self,) -> None:
        raise NotImplementedError
    
    def search_element_by_index(self,) -> None:
        raise NotImplementedError
    
    def count_length(self,) -> None:
        raise NotImplementedError
    
    def reverse_list(self,) -> None:
        raise NotImplementedError
    
    def merge_another_list(self,) -> None:
        raise NotImplementedError
    
    def split_list(self,) -> None:
        raise NotImplementedError
    
    def find_nth_node_from_end(self,) -> None:
        raise NotImplementedError

    def sort_linkedlist(self,) -> None:
        raise NotImplementedError
    
    def detect_duplicates(self,) -> None:
        raise NotImplementedError
    
    def detect_cycle(self,) -> None:
        raise NotImplementedError
    
    def remove_cycle(self,) -> None:
        raise NotImplementedError
    