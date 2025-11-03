class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Книга: «{self.title}», автор: {self.author}")


book1 = Book("Преступление и наказание", "Ф. М. Достоевский")
book1.show_info()
