# Implementing custom HashTable class in Python
class HashTable(object):
  def __init__(self, size):

    self.size = size
    self.slots = [None]*self.size
    self.data = [None]*self.size

  def put(self, key, data):

    hashvalue = self.hashfunction(key, len(self.slots))

    # Check if there is no value already present at the slot
    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data

    else:
      if self.slots[hashvalue] == key:  # Means the key is already in the slot
          self.data[hashvalue] = data

      else:
        nextslot = self.rehash(hashvalue, len(self.slots))

        while self.slots[nextslot] != None and self.slots[nextslots] != key:
          nextslot = self.rehash(nextslot, len(self.slots))

        if self.slots[nextslot] == None:
          self.slots[nextslot] = key
          self.data[nextslot] = data

        else:
          self.data[nextslot] = data

  def hashfunction(self, key, size):
    # It is the actual hash function
    return key % size

  # Rehash method to find the next svailable slot in collision case.
  def rehash(self, oldhashvalue, size):
    return (oldhash+1) % size

  def get(self, key):
    startslot = self.hashfunction(key, len(self.slots))
    data = None
    stop = False
    found = False
    position = startslot

    while self.slots[position] != None and not found and not stop:
      if self.slots[position] == key:
        found = True
        data = self.data[position]

      else:
          position = self.rehash(position, len(self.slots))
          if position == startslot:
            stop = True

    return data

  def __getitem__(self, key):
      return self.get(key)

  def __setitem__self(self, key, data):
      self.put(key, data)


h = HashTable(10)
h.put(1, 1)
h.put(20, 2)
print(h.get(20))
