import json
from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None

    def borrow(self, user, days=14):
        if self.is_available:
            self.is_available = False
            self.borrowed_by = user
            self.due_date = datetime.now() + timedelta(days=days)
            return True
        return False

    def return_book(self):
        self.is_available = True
        self.borrowed_by = None
        self.due_date = None

    def __str__(self):
        status = "Доступна" if self.is_available else f"Занята (до {self.due_date.strftime('%Y-%m-%d')}, {self.borrowed_by})"
        return f"{self.title} | {self.author} | {self.year} | ISBN: {self.isbn} | {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена из библиотеки.")
                return
        print("Книга с указанным ISBN не найдена.")

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def list_available_books(self):
        return [book for book in self.books if book.is_available]

    def borrow_book(self, isbn, user):
        for book in self.books:
            if book.isbn == isbn:
                if book.borrow(user):
                    print(f"Книга '{book.title}' успешно взята пользователем {user}.")
                    return
                else:
                    print(f"Книга '{book.title}' уже занята.")
                    return
        print("Книга с указанным ISBN не найдена.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_available:
                    book.return_book()
                    print(f"Книга '{book.title}' успешно возвращена.")
                    return
                else:
                    print(f"Книга '{book.title}' уже доступна в библиотеке.")
                    return
        print("Книга с указанным ISBN не найдена.")

    def save_to_file(self, filename="library.json"):
        data = [
            {
                "title": book.title,
                "author": book.author,
                "year": book.year,
                "isbn": book.isbn,
                "is_available": book.is_available,
                "borrowed_by": book.borrowed_by,
                "due_date": book.due_date.strftime('%Y-%m-%d') if book.due_date else None
            }
            for book in self.books
        ]
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Состояние библиотеки сохранено.")

    def load_from_file(self, filename="library.json"):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.books = []
                for book_data in data:
                    book = Book(
                        book_data['title'],
                        book_data['author'],
                        book_data['year'],
                        book_data['isbn']
                    )
                    book.is_available = book_data['is_available']
                    book.borrowed_by = book_data['borrowed_by']
                    if book_data['due_date']:
                        book.due_date = datetime.strptime(book_data['due_date'], '%Y-%m-%d')
                    self.books.append(book)
                print("Состояние библиотеки загружено.")
        except FileNotFoundError:
            print("Файл с сохраненной библиотекой не найден.")


def main():
    library = Library()
    library.load_from_file()

    while True:
        print("\nДобро пожаловать в библиотеку!")
        print("1. Показать доступные книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книги по автору")
        print("5. Взять книгу")
        print("6. Вернуть книгу")
        print("7. Сохранить и выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            available_books = library.list_available_books()
            if available_books:
                print("\nДоступные книги:")
                for book in available_books:
                    print(book)
            else:
                print("Нет доступных книг.")

        elif choice == "2":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            isbn = input("Введите ISBN книги: ")
            new_book = Book(title, author, year, isbn)
            library.add_book(new_book)

        elif choice == "3":
            isbn = input("Введите ISBN книги для удаления: ")
            library.remove_book(isbn)

        elif choice == "4":
            author = input("Введите имя автора: ")
            books_by_author = library.find_books_by_author(author)
            if books_by_author:
                print("\nКниги автора:")
                for book in books_by_author:
                    print(book)
            else:
                print("Книги данного автора не найдены.")

        elif choice == "5":
            isbn = input("Введите ISBN книги для взятия: ")
            user = input("Введите ваше имя: ")
            library.borrow_book(isbn, user)

        elif choice == "6":
            isbn = input("Введите ISBN книги для возврата: ")
            library.return_book(isbn)

        elif choice == "7":
            library.save_to_file()
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
