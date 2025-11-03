from sam2 import Book

class EBook(Book):
    def __init__(self, title, author, year, pages, file_size):
        super().__init__(title, author, year, pages)
        self.file_size = file_size  # дополнительный атрибут

    def download(self):
        print(f"Электронная книга «{self.title}» загружена ({self.file_size} МБ).")


ebook = EBook("Мастер и Маргарита", "М. А. Булгаков", 1967, 480, 2.3)
ebook.show_info()
ebook.download()