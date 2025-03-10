class Library:
    def __init__(self, name):
        self.name = name
        self.book = []

    def add_book(self, book_name):

        self.books.append(book_name)
        print(f'👍 "{book_name}" added to the library!')

    def show_books(self):

        if self.books:
            print(f"/n 😊 Books available in {self.name}:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("😒 No books in library")

    def borrow_book(self, book_name):

        if book_name in self.books:
            self.books.remove(book_name)
            print(f'✅ You borrowed "{book_name}". Enjoy reading!')
        else:
            print(f'❌ Sorry, "{book_name}" is not available!')

    my_library = Library("Kids' Library")

    my_library.add_book("Harry Potter")
    my_library.add_book("Alice in wonderland")
    my_library.add_book("Charlie and the chocolate factory")

    my_library.show_books()
    my_library.borrow_book("Alice in Wonderland")
    my_library.show_books()