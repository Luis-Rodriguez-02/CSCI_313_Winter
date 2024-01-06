'''Creating a simple class enrollment system (like CUNYFirst)'''

class College:
  def __init__(self, name):
    self.name = name
   
class QueensCollege(College):
    def __init__(self, name):
       super().__init__(name)

    def __str__(self):
      return f'{self.name}'

class CSDepartment(QueensCollege):
   def __init__(self, name):
      super().__init__(name)

   def __str__(self):
      return f'{self.name}'
   
class Subject(CSDepartment):
   def __init__(self, name):
      super().__init__(name)

   def __str__(self):
      return f'{self.name}'

class People():
   def __init__(self, name):
      self.name = name

class Student(People):
   def __init__(self, name, _college, _department, _class):
      super().__init__(name)
      self._college = _college
      self._department = _department
      self._class = _class

   def __str__(self) -> str:
      return f'{self.name}'


student1 = Student('Dan', QueensCollege("Queens College"), CSDepartment("CS Department"), Subject("CS313"))

print(student1.name)
print(student1._college)
print(student1._department)
print(student1._class)




