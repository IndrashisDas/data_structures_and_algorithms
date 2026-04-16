from src.linkedlist.single_linkedlist import SingleLinkedList


def test_single_linkedlist_empty() -> None:
    
    sll = SingleLinkedList()
    print(f"Is SingleLinkedList empty? - {sll.is_empty()}")


def test_single_linkedlist_creation_and_traversal() -> None:
    
    sll_1 = SingleLinkedList()
    sll_1.create_list([1, 2, 3, 4])
    sll_1.traverse_and_print()
    print("\n")
    
    sll_2 = SingleLinkedList()
    sll_2.create_list([100, -100, 500, -500])
    sll_2.traverse_and_print()
    print("\n")


def test_clear_linkedlist() -> None:
    sll_3 = SingleLinkedList()
    sll_3.create_list([1, 2, 3, 4])
    sll_3.traverse_and_print()
    print("\n")
    sll_3.clear_list()
    test_single_linkedlist_empty()


if __name__ == "__main__":
    print("===============================================================")
    print("Test empty SingleLinkedList")
    test_single_linkedlist_empty()
    print("===============================================================")
    print("Test creation and traversal of SingleLinkedList")
    test_single_linkedlist_creation_and_traversal()
    print("===============================================================")
    print("Test clearing of SingleLinkedList")
    test_clear_linkedlist()
    print("===============================================================")
