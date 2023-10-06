class Book:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password
        self.borrowBook = []
        self.returnBook = []

class Library:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.books = []

    def addBook(self, id, name, quantity):
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f'{book.name} added successfully')
        return book
    
    def addUser(self, id, name, password):
        user = User(id, name, password)
        self.users.append(user)
        return user
    
    def borrowBook(self, useName, token):
        for book in self.books:
            if book.name == token:
                if book in user.borrowBook:
                    print('Book Allrady Borrowed ! \n')
                    return
                elif book.quantity == 0:
                    print('This book is not avalable ! \n')
                    return
                else:
                    user.borrowBook.append(book)
                    book.quantity -=1
                    print('Borrowed book successfuly')
                    return
        print(f'Not Found this {token} book ')
    
    def returnBook(self, useName, token):
        for book in self.books:
            if book.name == token:
                if book in user.borrowBook:
                    book.quantity +=1
                    user.returnBook.append(book)
                    user.borrowBook.remove(book)
                    print('Returend Book')
                elif book.quantity == 0:
                    print('This book is not avalable ! \n')
                    return
        print(f'Not Found this {token} book ')


bsk = Library('Vs Code')
admin = bsk.addUser(100, 'admin', 'admin')
ratin = bsk.addUser(17, 'ratin', 123)
cpBook =bsk.addBook(15, 'cp Book', 7)


currentUser = admin

while True:
    if currentUser == None:
        print('No Login Ueser\n')
        option = input("Login or Registar (L/R) :")

        if option == 'L':
            id = int(input('Enter Id :'))
            password = input('Enter Password :')

            for user in bsk.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break
                if match == False:
                    print('No User Found\n')

        elif option == 'R':
            id = int(input('Enter User Id :'))
            name = input('Enter User Name :')
            password = input('Enter User Paasword :')


            for user in bsk.users:
                if(user.id == id):
                    print('User alrady avaliavle')
            
            print(f'printing user{id}, {name}, {password}  ')
            user = bsk.addUser(id, name, password)
            currentUser  = user

    else:
        print(f'Welcome Back {currentUser.name} \n')

        if currentUser.name == 'admin':
            print('Options \n')
            print('1 - Add Book')
            print('2 - Add User')
            print('3 - Show All Books')
            print('4 - Logout')
            
            cmd = int(input('Enter Option :'))

            if cmd == 1:
                id = int(input('Enter Book Id :'))
                name = input('Enter Book Name :')
                quantity = int(input('Enter Quantity :'))
                bsk.addBook(id, name, quantity)
            elif cmd == 2:
                id = int(input('Enter User Id :'))
                name = input('Enter User Name :')
                password = input('Enter User Paasword :')
                bsk.addUser(id, name, password)
            elif cmd == 3:
                for book in bsk.books:
                    print(f'{book.id} \t {book.name} \t {book.quantity}')
                print('\n')
            elif cmd == 4:
                currentUser = None
        
        else:
            print('Options \n')
            print('1 - Borrow Book')
            print('2 - Return Book')
            print('3 - Show All Books')
            print('4 - Books History')
            print('5 - Logout')

            cmd = int(input('Enter Option :'))

            if cmd == 1:
                name = input('Enter User Name :')
                bsk.borrowBook(currentUser, name)
            elif cmd == 2:
                name = input('Enter User Name :')
                bsk.returnBook(currentUser, name)
            elif cmd == 3:
                print('\nBorrow Books\n')
                for book in currentUser.borrowBook:
                    print(f'{book.id} \t {book.name} \t {book.quantity}')
                print('\n')
            elif cmd == 4:
                print('\nHistory of Books\n')
                for book in currentUser.returnBook:
                    print(f'{book.id} \t {book.name} \t {book.quantity}')
                print('\n')
            elif cmd == 5:
                currentUser = None
