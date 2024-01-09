class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
class LinkedList():
  def __init__(self, length=0):
    self.head = None
    self.length = length

  def append(self, data):
    new_node = Node(data)
    curr_node = self.head
    if self.head is None:
      self.head = new_node
      self.length += 1
    else:
      while curr_node.next:
        curr_node = curr_node.next
      curr_node.next = new_node
      self.length += 1

  def printll(self):
    curr_node = self.head
    while curr_node:
      print(curr_node.data, self.length, end= '\t')
      curr_node = curr_node.next
  def deleteNode(self, node):
    temp = self.head
    while temp.next is not None and temp.next != node:
      temp = temp.next
    else:
      temp.next = node.next
      node.next = None


linkedlist = LinkedList()
linkedlist.append(5)
linkedlist.append(10)
linkedlist.append(15)
linkedlist.deleteNode(Node(5))
linkedlist.printll()
