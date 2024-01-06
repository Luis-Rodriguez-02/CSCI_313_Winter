class ArrayList:
  def __init__(self, size=10) -> None:
    self.size = size
    self.count = 0;
    self.items = []
  
  def isEmpty(self):
    return self.count == 0

  def isFull(self):
    return self.count == self.size
  
  def get_size(self):
    return self.count
  
  def add(self, item):
    if self.isFull():
      raise Exception("ArrayList is full")
    else:
      self.items.append(item)
      self.count += 1
  
  def insert(self, index, item):
    if index < 0 or index >= self.size:
      raise Exception("Index out of range")
    else:
      self.items.insert(index, item)
      self.count += 1
  
  def toList(self):
    to_list = []
    for i in self.items:
      to_list.append(i)
    return to_list


test = ArrayList(10)
test.add(5)
test.add(4)
test.add(55)
print(test.get_size())
print(test.toList())
    


