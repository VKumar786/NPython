'''
    TODO: Exercise 6 - Library Management System in Python | Python Tutorial - Day #64 
'''
import json


class Library:
    Number_of_books = 0
    Books = []

    def __init__(self) -> None:
        with open(f"tut60/data.txt", "r") as f:
            self.Books = json.load(f)
            self.Number_of_books = len(self.Books)
            pass
        pass

    def checkLen(self) -> bool:
        return self.Number_of_books == len(self.Books)

    def AddBook(self, Book_Name, Quantity) -> None:
        self.Books.append({'Book Name': Book_Name, 'Quantity': Quantity})
        self.Number_of_books += 1
        with open(f"tut60/data.txt", "w") as f:
            json.dump(self.Books, f)
            pass

    def BookAvailable(self):
        for idx, el in enumerate(self.Books):
            print(f"{idx+1}. {el['Book Name']}")
        pass

    def CountBooks(self):
        return self.Number_of_books


obj = Library()

obj.AddBook("Harry Potter 1", 2)

obj.BookAvailable()

obj.CountBooks()

obj.checkLen()
