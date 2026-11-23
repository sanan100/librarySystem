class Book:
    def __init__(self,bookId,title,author,pagecount):
        self.bookId = bookId
        self.title = title
        self.author = author
        self.pagecount = pagecount
        self.isAviable = True

    def showInfo(self):
        print(f"""
        
        Id : {self.bookId}
        Title : {self.title}
        Author : {self.author}
        PegaCount : {self.pagecount}
        """)
        if self.isAviable:
            print("Status: Aviable")
        else:
            print("Status: Borrowed")
    
    
    def borrow(self):
        if self.isAviable:
            self.isAviable = False
            print(f"{self.title} borrowed")
        else:
            print("this book is already in the library")


    def returnBook(self):
        if not self.isAviable:
            self.isAviable = True
            print(f"{self.title} returned")
        else:
            print("this book is already in the library")


book1 = Book(1,"Clean code","robert Mardin",464)
book2 = Book(2,"Clean code","Messi Mardin",324)
book3 = Book(3,"Motherland","robert carlos",567)

