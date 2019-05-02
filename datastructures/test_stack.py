from stack import Stack
def test_push():
    colors = Stack()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    assert colors.count() == 2
def test_pop():
    colors = Stack()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() is None

def test_top():
    colors = Stack()
    colors.push("Cadmium Red Light")
    assert colors._top() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors._top() == "Hansa Yellow"

test_push()
test_pop()
test_top()