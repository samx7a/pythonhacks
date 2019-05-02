from myqueue import *
def test_shift():
    colors = MyQueue()
    colors.shift("Pthalo Blue")
    assert colors.count() == 1
    colors.shift("Ultramarine Blue")
    colors._invariant()
    assert colors.count() == 2

def test_pop():
    colors = MyQueue()
    colors.shift("Magenta")
    colors.shift("Alizarin")
    colors._invariant()
    assert colors.unshift() == "Magenta"
    colors._invariant()
    assert colors.unshift() == "Alizarin"
    colors._invariant()
    assert colors.unshift() is None

test_shift()    
test_pop()