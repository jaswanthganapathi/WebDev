class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = author
            print(f"{title} by {author} has been added to the library.")
        else:
            print(f"{title} is already in the library.")

    def display_books(self):
        if self.books:
            print("Books in the library:")
            for title, author in self.books.items():
                print(f"{title} by {author}")
        else:
            print("The library is empty.")

    def search_book(self, title):
        if title in self.books:
            print(f"{title} by {self.books[title]} is in the library.")
        else:
            print(f"{title} is not in the library.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"{title} has been removed from the library.")
        else:
            print(f"{title} is not in the library.")

def main():
    my_library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add a book")
        print("2. Display all books")
        print("3. Search for a book")
        print("4. Remove a book")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            my_library.add_book(title, author)
        elif choice == "2":
            my_library.display_books()
        elif choice == "3":
            title = input("Enter the title of the book you want to search for: ")
            my_library.search_book(title)
        elif choice == "4":
            title = input("Enter the title of the book you want to remove: ")
            my_library.remove_book(title)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
