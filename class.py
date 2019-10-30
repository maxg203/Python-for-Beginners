#A simple program to under the concept of class and object in python3
class BookStore:
    noOfBooks = 0
 
    def __init__(self, title, author):
        self.title = title
        self.author = author
        BookStore.noOfBooks += 1
 
    def bookInfo(self):
        print("Book title:", self.title)
        print("Book author:", self.author,"\n")
 
# Create a virtual book store
b1 = BookStore("Great Expectations", "Charles Dickens")
b2 = BookStore("War and Peace", "Leo Tolstoy")
b3 = BookStore("Middlemarch", "George Eliot")
 
# call member functions for each object
b1.bookInfo()
b2.bookInfo()
b3.bookInfo()

print("BookStore.noOfBooks:", BookStore.noOfBooks)

##OUTPUT :
#Book title: Great Expectations
#Book author: Charles Dickens 

#Book title: War and Peace
#Book author: Leo Tolstoy 

#Book title: Middlemarch
#Book author: George Eliot 

#BookStore.noOfBooks: 3
