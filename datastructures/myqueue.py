class QueueNode(object):
    def __init__(self, value, nxt, prev):
        self.value = value
        self. nxt = nxt 
        self.prev = prev
    
    def __repr__(self):
        nval = self.nxt.value or None
        pval = self.prev.value or None
        return f"[{self.value}:{pval}:{nval}"

class MyQueue(object):
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
    def __init__(self):
        self.begin = None
        self.end = None
    
    def _isEmpty(self):
        return self.begin is None

    def _isSingleton(self):
        return self.begin is self.end

    def count(self) -> int:
        currentNode = self.begin
        count = 0
        while(currentNode is not None):
            currentNode = currentNode.nxt
            count += 1
        return count
    
    def shift(self,obj):
        """ Add item to the end of the queue """
        if(self._isEmpty()):
            newNode = QueueNode(obj, None, None)
            self.begin = newNode
            self.end = newNode
        else:
            newNode = QueueNode(obj, None, self.end)
            self.end.nxt = newNode
            self.end = newNode

    def unshift(self) -> object:
        """ Remove item from the front of the queue and return its value """
        if(self._isEmpty()):
            return None
        elif(self._isSingleton()):
            res = self.begin.value
            self.begin = None
            self.end = None
            return res
        else:
            # A big list
            res = self.begin.value
            snd = self.begin.nxt
            snd.prev = None 
            self.begin = snd
            return res





            
    
    
