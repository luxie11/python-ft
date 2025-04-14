class Library:
    knygos = []
    def __init__(self):
        self.knygos = []

    def add(self, book):
        self.knygos.append(book)

    def remove(self, book):
        self.knygos.remove(book)

    def edit(self, book, index):
        self.knygos[index] = book

    def take_book(self, book, index):
        self.knygos[index].is_taken = True