class Student:
    def __init__(self,studentID,name):
        self.studentID = studentID
        self.name = name
        self.borrwedBooks = []


    
    def showInfo(self):
        print(f"""
        
        Id : {self.studentID}
        Name : {self.name}
        Borrowed books : {len(self.borrwedBooks)}
        """)

    def borrowBook(self,book):
        if book.isAviable:
            book.borrow()
            self.borrowedBooks.append(book)
        else:
            print("book is not aviable")
    def returnBook(self,book):
        if book in self.borrwedBooks:
           book.returnBook()
           self.borrwedBooks.remove(book)
        else:
            print("book is not aviable...")