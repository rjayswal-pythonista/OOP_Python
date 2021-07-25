class Library:
    def __init__(self, availableBooks):
        self.availableBooks = availableBooks

    def displaybook(self):
        print('List of Available Books in Library are:')
        for books in self.availableBooks:
            print(books)

    def lendbook(self, requestedbook):
        if requestedbook in self.availableBooks:
            print()
            print(f"You have now borrowed book name {requestedbook} from Library")
            self.availableBooks.remove(requestedbook)
        else:
            print(f"Sorry, {requestedBook} is not available in Library now")

    def addbook(self, returnedbook):
        self.availableBooks.append(returnedbook)
        print()
        print(f"Thank you for returning book name {returnedbook} to Library")
        print()


class Customer:
    def requestbook(self):
        print('Enter the name of book which you want to borrow from Library: ')
        self.book = str(input())
        return self.book

    def returnbook(self):
        print('Enter the name of book which you want to return to Library: ')
        self.book = str(input())
        return self.book

if __name__ == "__main__":
    availableBooks = ['The Lord of the Rings', 'Harry Potter series', 'The Little Prince', 'Think and Grow Rich']
    library = Library(availableBooks)
    customer = Customer()
    print('##########################################################################################################')
    print("                                 Welcome to Roshan Jayswal Library                                        ")
    print('##########################################################################################################')
    print()
    print('Enter your choice: ')
    while True:
        print()
        print('Enter 1 to display available books in Library')
        print('Enter 2 to borrow book from Library')
        print('Enter 3 to return book to Library')
        print('Enter 4 to quit')
        userchoice = int(input())
        if userchoice == 1:
            library.displaybook()
        elif userchoice == 2:
            requestedBook = customer.requestbook()
            library.lendbook(requestedBook)
        elif userchoice == 3:
            returnedBook = customer.returnbook()
            library.addbook(returnedBook)
        elif userchoice == 4:
            print('#########################################################################################################')
            print('                     Thank you for visiting Roshan Jayswal Library. See you soon...                      ')
            print('#########################################################################################################')
            quit()
