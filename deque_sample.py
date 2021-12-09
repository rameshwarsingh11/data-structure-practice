# Deque example
# Deque is a hybrid linear data structure that contains properties of both stack and a Queue. You can use this data structure to add and remove items both from the front and the rear end.
class Deque(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0, item)

  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)


d = Deque()

d.addFront('Hello')
d.addRear('Hola')
d.size()

print(d.removeFront() + ' ' + d.removeRear())
