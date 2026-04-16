"""
Implementation of Circular Single Linkedlist.
"""
from .base_linkedlist import NodeSingle, BaseLinkedList


class CircularSingleLinkedList(BaseLinkedList):
    
    def __init__(
        self,
    ) -> None:
        """
        Initialize the SingleLinkedList
        """
        self.head = None
        
    def is_empty(self,) -> None:
        raise NotImplementedError
    
    def create_list(self,) -> None:
        raise NotImplementedError
    
    def traverse_and_print(self,) -> None:
        raise NotImplementedError
    
    def clear_list(self,) -> None:
        raise NotImplementedError
    
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
    