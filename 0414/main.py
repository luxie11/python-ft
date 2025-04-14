from modules import Library, Book
# dog = Dog("Maya")
# cat = Cat("Maya2")

def main():
    books_array = [
        Book("Testas", "testas", 12.22),
        Book("Testas", "testas", 12.22),
        Book("Testas", "testas", 12.22),
        Book("Testas", "testas", 12.22),
        Book("Testas", "testas", 12.22)
    ]
    libary = Library()
    book1 = Book("Testas", "testas", 12.22)
    # libary.add(book1)
    # print(libary.knygos)
    #
    # libary.add(Book("Testas", "testas", 12.22)) BLOGAS SPRENDIMAs

    for book in books_array:
        libary.add(book)

main()
