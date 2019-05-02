class DoubleLinkedListNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self.nxt = nxt
        self.prev = prev
        
    def __repr__(self):
        nval = self.nxt and self.nxt.value
        pval = self.prev and self.prev.value
        return f"[{self.value}:{repr(pval)}:{repr(nval)}]"

class DoubleLinkedList(object):
    def __init__(self):
        self.begin = None
        self.end = None

    def _invariant(self):
        '''
        1. Are there zero elements? Then self.begin and self.end need to be None.
        2. If there is one element, then self.begin and self.end have to be equal (point at same node).
        3. The first element must always have a prev that is None.
        4. The last element must always have a next that is None.
        '''
        if(self._isEmpty()):
            assert(self.begin is None)
            assert(self.end is None)
        elif(self._isSingleton()):
            assert(self.begin is self.end)
            assert(self.begin.prev is None)
            assert(self.end.nxt is None)
        else:
            assert(self.begin.prev is None)
            assert(self.end.nxt is None)

    def count(self) -> int:
        count = 0
        currentNode = self.begin
        while(currentNode is not None):
            count += 1
            currentNode = currentNode.nxt
        return count

    def dump(self):
        currentNode = self.begin
        while(currentNode is not None):
            print("%s:" % currentNode.value)
            currentNode = currentNode.nxt

    def _isEmpty(self) -> bool:
        return self.begin is None

    def _isSingleton(self) -> bool:
        return self.begin is not None and (self.begin is self.end)

    def push(self, obj):
        """Appends a new value on the end of the list"""
        if(self._isEmpty()):
            newNode = DoubleLinkedListNode(obj, None, None)
            self.begin = newNode
            self.end = newNode
        else:
            newNode = DoubleLinkedListNode(obj, None, self.end)
            self.end.nxt = newNode
            self.end = newNode

    def pop(self) -> object:
        """Removes the last item and returns it."""
        if(self._isEmpty()):
            return None
        if(self._isSingleton()):
            res = self.end.value
            self.end = None
            self.begin = None
            return res

        # Many elements
        res = self.end.value
        self.end = self.end.prev
        self.end.nxt = None
        return res

    def shift(self, obj):
        """ Adds an element to the front of the list """
        if(self._isEmpty()):
            newNode = DoubleLinkedListNode(obj, None, None)
            self.begin = newNode
            self.end = newNode
        else:
            newNode = DoubleLinkedListNode(obj, self.begin, None)
            self.begin.prev = newNode
            self.begin = newNode

    def unshift(self) -> object:
        """Removes the first item (from begin) and returns it."""
        if(self._isEmpty()):
            return None
        if(self._isSingleton()):
            res = self.begin.value
            self.begin = None
            self.end = None
            return res
        # Many elements
        res = self.begin.value
        self.begin = self.begin.nxt
        self.begin.prev = None
        return res

    def detatch_node(self, node):
        """You'll need to use this operation sometimes, but mostly
        inside remove().  It should take a node, and detach it from the
        list, whether the node is at the front, end, or in the middle."""
        if(self._isEmpty()):
            return 
        if(self._isSingleton() and node is self.begin):
            self.begin = None
            self.end = None
            return
        # Many elements 
        if(node is self.begin):
            self.begin = self.begin.nxt
            self.begin.prev = None
        elif(node is self.end):
            self.end = self.end.prev
            self.end.nxt = None
        else:
            # Node is a middle element
            prev = node.prev
            nxt = node.nxt

            prev.nxt = nxt
            nxt.prev = prev
        
    def remove(self, obj):
        """Finds a matching item and removes it from the list."""
        currentNode = self.begin
        count = 0
        while(currentNode is not None):
            if(currentNode.value == obj):
                self.detatch_node(currentNode)
                return count
            currentNode = currentNode.nxt
            count += 1
        return None
    
    def first(self) -> object:
        if(self._isEmpty()):
            return None
        else:
            return self.begin.value

    def last(self) -> object:
        if(self._isEmpty()):
            return None
        else:
            return self.end.value

    def get(self, index) -> object:
        """ Returns the object value at the supplied index """
        if(self._isEmpty()):
            return None

        currentNode = self.begin
        
        while(index > 0):
            currentNode = currentNode.nxt
            if(currentNode is None):
                return None
            index -= 1
            
        return currentNode.value

    def get_node(self, index) -> DoubleLinkedListNode:
        """
        Returns the DoubleLinkedListNode at the given index.
        Can be used to assign new values to the node member
        """
        if(self._isEmpty()):
            return None

        currentNode = self.begin
        
        while(index > 0):
            currentNode = currentNode.nxt
            if(currentNode is None):
                return None
            index -= 1
            
        return currentNode

    def set_value(self, index: int, value: object):
        node = self.get_node(index)
        node.value = value



