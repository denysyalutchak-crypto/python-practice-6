class Book:
    def __init__(self, name, author, count=1):
        self.name = name
        self.author = author
        self.count = count

    def __str__(self):
        return f"'{self.name}' by {self.author} (кількість: {self.count})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                book.count += 1
                return
        self.books.append(Book(name, author))

    def user_take_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                if book.count > 0:
                    book.count -= 1
                    print(f"Взяли книгу: {name}")
                    return
                else:
                    print("Книги немає в наявності")
                    return
        print("Такої книги не існує")

    def show_books(self):
        print("\nСписок книг:")
        for book in self.books:
            print(book)


# тест
lib = Library()

lib.add_book("1984", "Orwell")
lib.add_book("1984", "Orwell")
lib.add_book("It", "King")
lib.add_book("It", "Another Author")

lib.show_books()

lib.user_take_book("1984", "Orwell")
lib.user_take_book("1984", "Orwell")
lib.user_take_book("1984", "Orwell")  # перевірка

lib.user_take_book("Unknown", "Author")  # не існує

lib.show_books()
