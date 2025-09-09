class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        return sum(self.marks)/len(self.marks)
    def add_mark(self,m):
        self.marks.append(m)
    def get_highest(self):
        return max(self.marks)
    def get_lowest(self):
        return min(self.marks)

s = Student("Goutham Reddy",[90,80,85])
print(s.name)
print(s.get_average())
print(s.get_highest())
print(s.get_lowest())
s.add_mark(98)
print(s.get_average())
print(s.get_highest())
print(s.get_lowest())