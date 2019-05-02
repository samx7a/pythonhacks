from dllist import *
from random import randint

def generateRandomList(length = 10) -> DoubleLinkedList:
    numbers = DoubleLinkedList()
    for _ in range(length):        
        numbers.shift(randint(0,101))
    return numbers

def swap(elem1: DoubleLinkedListNode, elem2: DoubleLinkedListNode):
    temp = elem1.value
    elem1.value = elem2.value
    elem2.value = temp

def bubblesort(list):
    is_sorted = False
    while(not is_sorted):
        is_sorted = True
        currentNode = list.begin
        while(currentNode.nxt is not None):
            if(currentNode.value > currentNode.nxt.value):
                #Swap the element values
                swap(currentNode, currentNode.nxt)
                is_sorted = False
            currentNode = currentNode.nxt

def mergesort(someList):
    res = _mergesort_helper(someList)
    someList.begin = res.begin

    currentNode = res.begin
    while(currentNode.nxt is not None):
        currentNode = currentNode.nxt
    # currentNode is now the last node of the res list
    someList.end = currentNode
    

def _mergesort_helper(list) -> DoubleLinkedList:
    if(list._isSingleton() or list._isEmpty()):
        return list

    n = list.count()
    midPoint = round(n/2)
    # We must split left and right with regards to the midpoint.
    left = DoubleLinkedList()
    right = DoubleLinkedList()
    # Scan to midpoint
    scanNode = list.begin
    for _ in range(midPoint - 1):
        scanNode = scanNode.nxt
    # (L ++ mid) ++ right
    right.begin = scanNode.nxt
    right.end = list.end
    left.begin = list.begin
    left.end = scanNode
    right.begin.prev = None
    left.end.nxt = None

    sorted_left = _mergesort_helper(left)
    sorted_right = _mergesort_helper(right)


    return merge(sorted_left, sorted_right)

def merge(left: DoubleLinkedList, right: DoubleLinkedList) -> DoubleLinkedList:
    res = DoubleLinkedList()
    while(not left._isEmpty() and not right._isEmpty()):
        lhead = left.first()
        rhead = right.first()
        if(lhead < rhead):
            res.push(left.unshift())
        else:
            res.push(right.unshift())

    # Add left over elements in either left or right
    while(not left._isEmpty()):
        res.push(left.unshift())
    while(not right._isEmpty()):
        res.push(right.unshift())
    
    return res

def quicksort(numbers: DoubleLinkedList) -> None:
    _quicksort_helper(numbers, 0, numbers.count() -1)
    return 
def _quicksort_helper(numbers: DoubleLinkedList,low, high) -> None:
    if(low >= high):
        return
    midpoint = low + round((high - low)/2)
    pivot_value = numbers.get(midpoint)
    i, j = low, high
    while(i <= j):
        while(numbers.get(i) < pivot_value):
            i += 1
        while(numbers.get(j) > pivot_value):
            j -= 1
        if(i <= j):
            temp = numbers.get(i)
            numbers.set_value(i, numbers.get(j))
            numbers.set_value(j, temp)
            i += 1
            j -= 1
        
    # Invariant: i and before are less than or equal to pivot value
    # Invariant: j and above are greater than or equal to pivot value
    
    # Left
    _quicksort_helper(numbers, low, j)
    # Right
    _quicksort_helper(numbers, i, high)