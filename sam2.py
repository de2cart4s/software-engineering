class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def show_info(self):
        print(f"«{self.title}» ({self.year}), автор: {self.author}, {self.pages} страниц")

    def is_long(self):
        if self.pages > 500:
            print("Это большая книга.")
        else:
            print("Это небольшая книга.")


book2 = Book("Война и мир", "Л. Н. Толстой", 1869, 1225)
book2.show_info()
book2.is_long()
