import random
def generate_test_list() -> list:
    res = []
    for _ in range (0,11):
        res.append(random.randint(0,100))
    return res
"""
    Quicksort implementation
    O(log(n)) space complexity.
    Modifies list in place,
    Space is only allocated for stack frames (or number of recursions)
    which is log(n) for this divide & conquer algorithm
"""
def quicksort(numbers):
    _quicksort_helper(numbers, 0, len(numbers)-1)

def _quicksort_helper(numbers, low, high):
    if(low >= high):
        return
    midpoint = low + round((high-low)/2)
    pivot_value = numbers[midpoint]
    i = low
    j = high
    while(i <= j):
        while(numbers[i] < pivot_value):
            i += 1
        while(numbers[j] > pivot_value):
            j -= 1
        if(i <= j):
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp
            i += 1
            j -= 1
        # Invariant: all elements at i or after are greater than or equal to the pivot value
        # Invariant: all elements at j or before are less than or equal to the pivot value
    # Left
    _quicksort_helper(numbers, low, j)
    # Right
    _quicksort_helper(numbers, i, high)
    
    
test_list = generate_test_list()
quicksort(test_list)
print(test_list)
