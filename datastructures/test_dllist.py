from dllist import *

def test_push():
    colors = DoubleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count() == 1
    colors.push("Ultramarine Blue")
    colors._invariant()
    assert colors.count() == 2

def test_pop():
    colors = DoubleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    colors._invariant()
    assert colors.pop() == "Alizarin"
    colors._invariant()
    assert colors.pop() == "Magenta"
    colors._invariant()
    assert colors.pop() is None

def test_shift():
    colors = DoubleLinkedList()
    colors.shift("Cadmium Orange")
    assert colors.count() == 1
    colors._invariant()
    colors.shift("Carbazole Violet")
    assert colors.count() == 2
    assert colors.pop() == "Cadmium Orange"
    colors._invariant()
    assert colors.count() == 1
    assert colors.pop() == "Carbazole Violet"
    colors._invariant()
    assert colors.count() == 0

def test_unshift():
    colors = DoubleLinkedList()
    colors.push("Viridian")
    colors._invariant()
    colors.push("Sap Green")
    colors.push("Van Dyke")
    colors._invariant()
    assert colors.unshift() == "Viridian"
    colors._invariant()
    assert colors.unshift() == "Sap Green"
    assert colors.unshift() == "Van Dyke"
    colors._invariant()
    assert colors.unshift() is None
    colors._invariant()

def test_detatch_node():
    colors = DoubleLinkedList()
    # Test empty case
    node = DoubleLinkedListNode("blah", None, None)
    colors.detatch_node(node)
    colors._invariant()

    # Test singleton
    colors.push("Green")
    colors.detatch_node(colors.begin)
    assert(colors._isEmpty())
    colors._invariant()

    # Test many elements
    colors.push("Green")
    colors.push("Purple")
    colors.push("Blue")

    #begin
    colors.detatch_node(colors.begin)
    assert(colors.count() == 2)
    assert(colors.begin.value == "Purple")
    assert(colors.end.value == "Blue")
    colors._invariant()
    #middle
    colors.push("Yellow")
    colors.detatch_node(colors.begin.nxt)
    assert(colors.count() == 2)
    assert(colors.begin.value == "Purple")
    assert(colors.end.value == "Yellow")
    colors._invariant()
    #end
    colors.detatch_node(colors.end)
    assert(colors.count() == 1)
    assert(colors.begin.value == "Purple")
    colors._invariant()
def test_remove():
    colors = DoubleLinkedList()
    colors.push("Cobalt")
    colors.push("Zinc White")
    colors.push("Nickle Yellow")
    colors.push("Perinone")
    colors._invariant()
    assert colors.remove("Cobalt") == 0
    colors._invariant()
    assert colors.remove("Perinone") == 2
    assert colors.remove("Nickle Yellow") ==1
    assert colors.remove("Zinc White") == 0
    colors._invariant()
def test_get():
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    colors._invariant()
    assert colors.get(0) == "Vermillion"
    colors.push("Sap Green")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get(0) == "Vermillion"
    assert colors.get(1) == "Sap Green"
    assert colors.get(2) == None
    colors.pop()
    assert colors.get(0) == "Vermillion"
    colors._invariant()
    colors.pop()
    assert colors.get(0) == None
def test_first():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.first() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.first() == "Cadmium Red Light"
    colors.shift("Pthalo Green")
    assert colors.first() == "Pthalo Green"

def test_last():
    colors = DoubleLinkedList()
    colors.push("Cadmium Red Light")
    assert colors.last() == "Cadmium Red Light"
    colors.push("Hansa Yellow")
    assert colors.last() == "Hansa Yellow"
    colors.shift("Pthalo Green")
    assert colors.last() == "Hansa Yellow"

def test_get_node():
    colors = DoubleLinkedList()
    colors.push("Vermillion")
    colors._invariant()
    assert colors.get_node(0).value == "Vermillion"
    colors.push("Sap Green")
    assert colors.get_node(0).value == "Vermillion"
    assert colors.get_node(1).value == "Sap Green"
    colors.push("Cadmium Yellow Light")
    assert colors.get_node(0).value == "Vermillion"
    assert colors.get_node(1).value == "Sap Green"
    assert colors.get_node(2).value == "Cadmium Yellow Light"
    assert colors.pop() == "Cadmium Yellow Light"
    assert colors.get_node(0).value == "Vermillion"
    assert colors.get_node(1).value == "Sap Green"
    assert colors.get_node(2) == None
    colors.pop()
    assert colors.get_node(0).value == "Vermillion"
    colors._invariant()
    colors.pop()
    assert colors.get(0) == None

def test_set_value():
    colors = DoubleLinkedList()
    colors.push("Red")
    colors.set_value(0,"Blue")
    assert colors.get(0) == "Blue"
    colors.push("Red")
    colors.push("Red")
    colors.push("Red")
    colors.pop()
    colors.set_value(2, "Blue")
    assert colors.pop() == "Blue"
    colors._invariant()


# Run Tests
test_push()
test_pop()
test_shift()
test_detatch_node()
test_remove()
test_get()
test_first()
test_last()
test_get_node()
test_set_value()
