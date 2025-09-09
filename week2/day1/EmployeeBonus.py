class Bonus:
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    def bonus(self):
        if self.role == "Manager":
            return (self.salary*20)//100
        elif self.role == "Developer":
            return (self.salary*10)//100
        elif self.role == "intern":
            return (self.salary*5)//100
        
e1 = Bonus("Goutham",25000,"Manager")
print(e1.bonus())
e2 = Bonus("Goutham",25000,"Developer")
print(e2.bonus())
e3 = Bonus("Goutham",25000,"intern")
print(e3.bonus())