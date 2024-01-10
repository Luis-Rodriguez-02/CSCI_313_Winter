class Node():
  def __init__(self, data):
    self.data = data
    self.next = None # test

class LinkedList():
  def __init__(self):
    self.head = None

  def append(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      temp = self.head
      while temp.next != None:
        temp = temp.next
      else:
        temp.next = Node(data)
  
  def printLL(self):
    temp = self.head
    while temp != None:
      print(temp.data)
      temp = temp.next

class ChainHashMap:
  def __init__(self):
    self.capacity = 101 # capacity of list that will hold values
    self.array = [] * self.capacity # empty list to hold values
    self.size = 0 # how many values in the list

  def put(self, key, value):
    self.pair.append((key,value))
    


test_ll = LinkedList()
test_ll.append(5)
test_ll.append(7)
test_ll.append(10)
test_ll.printLL()

test_hash = ChainHashMap()
print(test_hash.array)


test_dict = {
  '007': 'Agent Double O',
  '117': 'Agent Double 1',
  '227': 'Agent Double 2'
             }

