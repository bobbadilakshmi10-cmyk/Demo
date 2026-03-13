#Library Management System
'''1.Add Book
2.Search book
3.view book
4.issue book
5.return book
6.exit'''

class library():
    def __init__(self):
        self.books=[]
    def Add_book(self):
        book=input("enter the book name:")
        self.books.append(book)
        print("book added")

    def Search_book(self):
        book=input("book name to search:")
        if book in self.books:
            print("book funded")
        else:
            print("book not founded")
    def view_of_books(self):
        if len(self.books)==0:
            print("is empty")
        else:
            print("book in lib")
            for i in range(len(self.books)):
                print(i+1,self.books[i])
            print()
    def issue_book(self):
        book=input("enter the book name to search:")
        if book in self.books:
            self.books.remove(book)
            print("book is solved:")
        else:
            print("book not avaliabe")
    def return_book(self):
        book=input("enter the book name to return:")
        self.books.append(book)
        print("book returned")
obj1=library()
print("----Libraray Management System----")
while True:
    a=["1.Add Book","2.Search Book","3.View of books","4.Issue Book","5.Return Book","6.Exit"]
    for i in range(len(a)):
        print(a[i])
    choose=int(input("options(1-6):"))
    if choose==1:
        obj1.Add_book()
    elif choose==2:
        obj1.Search_book()
    elif choose==3:
        obj1.view_of_books()
    elif choose==4:
        obj1.issue_book()
    elif choose==5:
        obj1.return_book()
    elif choose==6:
        print("exit")
        break
    else:
        print("invalid option")
                    
