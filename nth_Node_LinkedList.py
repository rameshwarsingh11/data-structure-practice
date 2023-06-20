def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    for i in range(n - 1):
        if not right_pointer.nextnode:
            raise LookupError("Error: n is larger than n in the linked List")

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(15)
f = Node(6)
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


class TestNLast(object):
    def test(self, sol):
        assert (sol(3, a), c)
        print("Success")


t = TestNLast()
t.test(nth_to_last_node)
