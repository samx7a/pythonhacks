class SingleLinkedListNode(object):
    def __init__(self, value, nxt):
        self.value      = value
        self.nxt        = nxt

    def __repr__(self):
        nval = self.nxt or None 
        return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):
    def __init__(self):
        self.begin  = None
        self.end     = None
    def __repr__(self):
        return self.begin.__repr__()
                                                                                        
    def count(self) -> int:
        # Handle empty case
        if(self.begin is None):
            return 0
        count = 1
        currentNode = self.begin
        while(currentNode.nxt is not None):
            currentNode = currentNode.nxt
            count += 1
        return count

    def push(self, obj):
        """ Append the object to the end of the single linked list """
        # Instantiate new node to be added
        newNode = SingleLinkedListNode(obj, None)
        # Handle the case where we have an empty list.
        if(self.begin is None):
            self.begin = newNode
            self.end = newNode
            return
        
        # Handle the case where we have a singleton list
        if(self.begin.nxt is None):
            self.begin.nxt = newNode
            self.end = newNode
            return
        
        # Append to end of list.
        currentNode = self.begin
        while(currentNode.nxt is not None):
            currentNode = currentNode.nxt
        currentNode.nxt = newNode
        return

    def pop(self) -> object:
        """Removes the last item and returns it."""
        # Handle empty list case
        if(self.begin is None):
            return None

        # Handle singleton list case
        if(self.begin.nxt is None):
            result = self.begin.value
            self.begin = None
            self.end = None
            return result

        # Pop from end of long list
        previousNode = None
        currentNode = self.begin
        while(currentNode.nxt is not None):
            previousNode = currentNode
            currentNode = currentNode.nxt
        # currentNode holds the last node in the list
        previousNode.nxt = None
        self.end = previousNode
        return currentNode.value
    
    def shift(self, obj):
        """ Inserts item at the beginning of the list"""
        # Handle empty list case
        if(self.begin is None):
            newNode = SingleLinkedListNode(obj, None)
            self.begin = newNode
            self.end = newNode
        else:
            newNode = SingleLinkedListNode(obj, self.begin)
            self.begin = newNode
        return

    def unshift(self) -> object:
        """ Removes the first element of the list and returns it """
        # Handle empty case
        if(self.begin is None):
            return None
        
        # Handle singleton case
        if(self.begin.nxt is None):
            result = self.begin.value
            self.begin = None
            self.end = None
            return result

        # Handle long list case
        result = self.begin.value
        self.begin = self.begin.nxt
        return result

    def remove(self, obj) -> int:
        """ Takes an object value and removes the first element in the list that matches. Returns the matching index """
        # Handle empty case
        if(self.begin is None):
            return None
        
        # Handle long list case
        # if we are removing the first element of the list
        if(self.begin.value == obj):
            self.begin = self.begin.nxt
            return 0

        currentNode = self.begin.nxt
        previousNode = self.begin
        count = 1
        while(currentNode is not None):
            if(currentNode.value == obj):
                # Remove currentNode
                # Case where the currentNode is the last element of the list
                if(currentNode.nxt is None):
                    self.end = previousNode
                    previousNode.nxt = None
                else: 
                    previousNode.nxt = currentNode.nxt
                return count

            previousNode = currentNode
            currentNode = currentNode.nxt
            count += 1
        # Element not found in list
        return None

    def first(self) -> object:
        return self.begin.value

    def last(self) -> object:
        return self.end.value

    def get(self, index) -> object:
        """ Get the value at the index """
        # Handle empty case
        if(self.begin is None):
            return None
        currentNode = self.begin
        while(index > 0):
            currentNode = currentNode.nxt
            if(currentNode is None):
                return None
            index -= 1
        return currentNode.value


