class Book:
    total_books = 0
    def __init__(self,book_name):
        self.book_name = book_name

    @classmethod
    def increment_book_count(cls,addBook):
        cls.total_books += addBook
    
    def show_book(self):
        print(f"Total Book is {self.total_books} and book name is {self.book_name}")

b = Book("Physics")
b.increment_book_count(1)
b.show_book()
b1 = Book("Math")
b1.increment_book_count(1)
b1.show_book()