class StackNode(object):
    def __init__(self, value, nxt):
        self.value = value
        self.nxt = nxt
    
    def __repr__(self):
        nval = self.nxt.value
        return f"[{self.value}:{repr(nval)}]"

class Stack(object):
    def __init__(self):
        # Top is in fact the bottom of the stack
        self.top = None

    def __isEmpty__(self):
        return (self.top is None)

    def __isSingleton__(self):
        return (self.top.nxt is None)
    
    def push(self, obj):
        
        newNode = StackNode(obj,None)
        if(self.__isEmpty__()):
            self.top = newNode
            
        else:
            currentNode = self.top
            while(currentNode.nxt is not None):
                currentNode = currentNode.nxt
            # currentNode is now the last element of the stack
            currentNode.nxt = newNode

    def pop(self) -> object:
        """ Removes the last element of the list and returns its value """
        if(self.__isEmpty__()):
            return None
        elif(self.__isSingleton__()):
            res = self.top.value
            self.top = None
            return res
        else:
            # Long list
            currentNode = self.top
            prevNode = self.top
            while(currentNode.nxt is not None):
                prevNode = currentNode
                currentNode = currentNode.nxt

            # Invariant: currentNode is now the last Node, prevNode is the second to last.
            prevNode.nxt = None
            return currentNode.value

    def _top(self) -> object:
        """ Returns the value of the last element """
        if(self.__isEmpty__()):
            return None
        else:
            currentNode = self.top
            while(currentNode.nxt is not None):
                currentNode = currentNode.nxt
            # Invariant: the currentNode is now the last node.
            return currentNode.value

    def count(self) -> int:
        count = 0
        currentNode = self.top
        while(currentNode is not None):
            count += 1
            currentNode = currentNode.nxt
        
        return count

    def dump(self):
        currentNode = self.top
        while(currentNode is not None):
            print(f"{currentNode.value}:")
            currentNode = currentNode.nxt

colors = Stack()
colors.push("Hello")
colors.push("World")

colors.dump()