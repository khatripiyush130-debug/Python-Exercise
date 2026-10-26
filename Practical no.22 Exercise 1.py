FILE = "library.txt"
def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    with open(FILE, "a") as f:
        f.write(f"{book_id}|{title}|{author}|Available\n")
    print("Book added successfully!")
def search_book():
    title = input("Enter title to search: ").lower()
    try:
        with open(FILE, "r") as f:
            found = False
            for line in f:
                if title in line.split("|")[1].lower():
                    print(line.strip())
                    found = True
            if not found:
                print("Book not found.")
    except FileNotFoundError:
        print("No books available.")
def display_books():
    try:
        with open(FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No books available.")
def main():
    while True:
        print("\n1. Add Book")
        print("2. Search Book")
        print("3. Display Books")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            display_books()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
main()
