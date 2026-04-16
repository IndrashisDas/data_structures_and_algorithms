"""
Base implementation of a Linkedlist.
"""
from abc import abstractmethod


class NodeSingle:
    
    def __init__(
        self,
        data: int,
    ) -> None:
        self.data = data
        self.next = None


class NodeDouble:
    
    def __init__(
        self,
        data: int,
    ) -> None:
        self.data = data
        self.next = None
        self.prev = None
    

class BaseLinkedList:
    
    def __init__(
        self,
    ) -> None:
        self.head = None
    
    @abstractmethod
    def is_empty(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def create_list(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def traverse_and_print(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def clear_list(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def insert_at_index(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def insert_before_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def insert_after_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_before_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_after_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_at_index(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete_by_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def update_node_by_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def update_node_by_index(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def search_element_by_value(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def search_element_by_index(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def count_length(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def reverse_list(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def merge_another_list(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def split_list(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def find_nth_node_from_end(self,) -> None:
        raise NotImplementedError

    @abstractmethod
    def sort_linkedlist(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def detect_duplicates(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def detect_cycle(self,) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def remove_cycle(self,) -> None:
        raise NotImplementedError
