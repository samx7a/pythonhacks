from dllist import DoubleLinkedList
import sorting
from random import randint

def generateRandomList(length = 10) -> DoubleLinkedList:
    numbers = DoubleLinkedList()
    for _ in range(length):        
        numbers.shift(randint(0,101))
    return numbers

def is_sorted(list: DoubleLinkedList) -> bool:
    currentNode = list.begin
    while(currentNode.nxt is not None):
        if(currentNode.value > currentNode.nxt.value):
            return False
        currentNode = currentNode.nxt
    return True

def test_bubblesort():
    list = generateRandomList()
    sorting.bubblesort(list)
    assert(is_sorted(list))

def test_mergesort():
    list = generateRandomList()
    sorting.mergesort(list)
    assert(is_sorted(list))
def test_quicksort():
    test_list = generateRandomList()
    sorting.quicksort(test_list)
    assert(is_sorted(test_list))


test_bubblesort()
test_mergesort()
test_quicksort()