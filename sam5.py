class Reader:
    def read(self):
        print("Читатель читает книгу в библиотеке.")

class Student(Reader):
    def read(self):
        print("Студент читает учебник по программированию.")

class Scientist(Reader):
    def read(self):
        print("Учёный изучает научные статьи и монографии.")


readers = [Reader(), Student(), Scientist()]
for r in readers:
    r.read()
