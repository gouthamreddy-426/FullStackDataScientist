class Professor:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    def teach(self,cname):
        print(self.name,"is teaching",cname)
    def give_assignment(self,aname):
        print(self.name,"Assigned",aname)
class Student:
    def __init__(self,name):
        self.name = name
        self.courses = []
        self.ass = []
    def enroll(self,cname):
        self.courses.append(cname)
        print(self.name,"Enrolled in",cname)
    def submit_assignment(self,aname):
        self.ass.append(aname)
        print(self.name,"Submitted",aname)

p = Professor("Dr. Smith", "Computer Science")
s = Student("Alice")

p.teach("Python")
s.enroll("Python")
p.give_assignment("Project 1")
s.submit_assignment("Project 1")


        
        