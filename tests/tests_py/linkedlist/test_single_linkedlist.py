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
        # Insert multiple nodes into the linkedlist
        self.linkedlist.insert(value=3)
        self.linkedlist.insert(value=2)
        self.linkedlist.insert(value=1)
        self.linkedlist.insert(value=0)
        self.linkedlist.insert(value=-1)
        self.linkedlist.insert(value=-2)
        self.linkedlist.insert(value=-3)

    def test_insert_start(self):
        pass
    
    def test_insert_by_index(self):
        pass
    
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