class Library:
    def __init__(self,d):
        self.d = d 
    def borrow(self,title):
        if (title not in self.d) or self.d[title] == 0:
            return "Not Available"
        else:
            self.d[title] -= 1
            return "You Borrowed",title
    def return_book(self,title):
        if title not in self.d:
            return title,"not belongs to this library"
        self.d[title] += 1
        return "You Returned",title
    def show_books(self):
        print(self.d)

lib = Library({"Python 101": 3, "Data Science": 2})
print(lib.borrow("Python 101"))
print(lib.return_book("Python 102"))
lib.show_books()


