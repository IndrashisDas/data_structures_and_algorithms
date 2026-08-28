"""
Test Single Linkedlist

The following script contains all the code to test
all the features from Single Linkedlists.
"""
import unittest

from dsa_py.linkedlist.single_linkedlist import SingleLinkedlist


class TestSingleLinkedlist(unittest.TestCase):
    
    # setUp() is called once before every test. 
    # Need not worr< about initializing the linkedlist again.
    def setUp(self) -> None:
        self.linkedlist = SingleLinkedlist()

    def test_is_empty(self):
        # Test if linkedlist is empty
        is_empty = self.linkedlist.is_empty()
        self.assertEqual(is_empty, True)
        
        # Test if linkedlist is not empty
        self.linkedlist.insert(value=1)
        is_empty = self.linkedlist.is_empty()
        self.assertEqual(is_empty, False)

    def test_insert(self):
        # Insert single node
        values = [1]
        for value in values:
            self.linkedlist.insert(value=value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual(values, node_values)
        
        # Insert multiple nodes into the linkedlist
        new_values = [3, 2, 1, 0, -1, -2, -3]
        for value in new_values:
            self.linkedlist.insert(value=value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual(values + new_values, node_values)

    def test_insert_start(self):
        # Insert multiple nodes into the linkedlist
        values = [3, 2, 1, 0, -1, -2, -3]
        for value in values:
            self.linkedlist.insert(value=value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual(values, node_values)
        
        # Insert a node at the start of the linkedlist
        start_value = 4
        self.linkedlist.insert_start(value=start_value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual([start_value] + values, node_values)
    
    def test_insert_by_index(self):
        # Insert multiple nodes into the linkedlist
        values = [3, 2, 1, 0, -1, -2, -3]
        for value in values:
            self.linkedlist.insert(value=value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual(values, node_values)
        
        # Insert a node at idx = 0
        idx = 0
        idx_value = 4
        self.linkedlist.insert_by_index(idx=idx, value=idx_value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual([idx_value] + values, node_values)
        
        # Insert a node at idx = 2
        idx = 2
        idx_value = 9
        self.linkedlist.insert_by_index(idx=idx, value=idx_value)
        node_values = self.linkedlist.show_linkedlist()
        self.assertEqual([4, 3, 9, 2, 1, 0, -1, -2, -3], node_values)
    
    def test_search_by_index(self):
        pass
    
    def test_search_by_value(self):
        pass
    
    def test_update_by_index(self):
        pass
    
    def test_update_by_value(self):
        pass
    
    def test_delete_start(self):
        pass
    
    def test_delete_end(self):
        pass
    
    def test_delete_by_index(self):
        pass
    
    def test_delete_by_value(self):
        pass
    
    def test_count_length(self):
        pass
    
    def test_reverese(self):
        pass 