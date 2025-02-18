class Book:
    def __init__(books, title, year_published, author):
        books.title = title
        books.year_published = year_published
        books.author = author

    def define(books):
        print (f"Title:          {books.title}.")
        print (f"Year_Published: {books.year_published}.")
        print (f"Author:         {books.author}.\n")

book1 = Book("Alice Adventure in Wonderland", 2017, "Lewis Carroll")
book2 = Book("Pinocchio", 2012, "Carlo Collodi")
book3 = Book("Peter Pan", 1991, "J.M. Barrie")

book1.define()
book2.define()
book3.define()
