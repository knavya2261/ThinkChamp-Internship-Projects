print("Welcome to Library Management System")

while True:

    print("\n1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        book = input("Enter Book Name: ")

        file = open("books.txt", "a")
        file.write(book + "\n")
        file.close()

        print("Book Added Successfully!")

    elif choice == "2":

        file = open("books.txt", "r")

        print("\nAvailable Books:")

        for book in file:
            print(book.strip())

        file.close()

    elif choice == "3":

        name = input("Enter Book Name: ")

        file = open("books.txt", "r")

        found = False

        for book in file:

            if name.lower() in book.lower():
                print("Book Found:", book.strip())
                found = True

        if found == False:
            print("Book Not Found")

        file.close()

    elif choice == "4":

        name = input("Enter Book Name: ")

        file = open("books.txt", "r")
        books = file.readlines()
        file.close()

        file = open("books.txt", "w")

        found = False

        for book in books:

            if book.strip().lower() == name.lower():
                found = True
            else:
                file.write(book)

        file.close()

        if found:

            issue = open("issued_books.txt", "a")
            issue.write(name + "\n")
            issue.close()

            print("Book Issued Successfully!")

        else:
            print("Book Not Available")

    elif choice == "5":

        name = input("Enter Book Name: ")

        issue = open("issued_books.txt", "r")
        books = issue.readlines()
        issue.close()

        issue = open("issued_books.txt", "w")

        found = False

        for book in books:

            if book.strip().lower() == name.lower():
                found = True
            else:
                issue.write(book)

        issue.close()

        if found:

            file = open("books.txt", "a")
            file.write(name + "\n")
            file.close()

            print("Book Returned Successfully!")

        else:
            print("Book Not Found")

    elif choice == "6":

        print("Thank You")
        break

    else:

        print("Invalid Choice")