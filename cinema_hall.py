class Star_Cinema:
    __hall_list = []

    def entry_hall(self, Hall):
        self.hall_list.append(Hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_on):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._col = cols
        self.__hall_no = hall_on

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self._show_list.append(show)
        site = [[0]*self._rows for _ in range(self._col)]
        self._seats[id] = site

    def view_show_list(self):
        for show in self._show_list:
            print(f'{show[1]}({show[0]}) {show[2]}')

    def book_ticket(self, id, row, col):
        flag = True
        for show in self._show_list:
            if show[0] == id:
                flag = False
                seat = self._seats[id]
                if seat[row][col]:
                    print(f'This Seat ({row} {col}) is already booked')
                    return 1
                else:
                    seat[row][col] = 1
                    self._seats[id] = seat
                    print(f'Disiare seat booked ({row+1} {col+1})')
                    return 0
                return
        if flag:
            print('Invalid ID')
            return 2

    def view_avaiable_seats(self, id):
        flag = True
        for show in self._show_list:
            if show[0] == id:
                flag = False
                seats = self._seats[id]
                for seat in seats:
                    for col in seat:
                        print(col, end=" ")
                    print()
                return 0
        if flag:
            print('Invalid ID')
            return 1


halls = Hall(5, 5, 200)
halls.entry_show(234, 'Dunki', '10/12/2023 10:00 AM')
halls.entry_show(334, 'Tiger 3', '31/12/2023 10:00 AM')
halls.entry_show(234, 'Jawan', '10/10/2023 s10:00 AM')

while True:
    print('1 - View all show today')
    print('2 - View avaliable seats')
    print('3 - Book Ticket')
    print('4 - Exit')

    cmd = int(input('\nEnter the options :'))
    if cmd == 1:
        halls.view_show_list()
    elif cmd == 2:
        show_id = int(input('Enter show id :'))
        id = halls.view_avaiable_seats(show_id)
        while id:
            show_id = int(input('Enter correct show id :'))
            id = halls.view_avaiable_seats(show_id)
    elif cmd == 3:
        ticketNum = int(input('Number of ticket : '))
        for i in range(ticketNum):
            show_id = int(input('Enter your show id : '))
            row = int(input('Enter seats row : '))
            col = int(input('Enter seats col : '))
            id = halls.book_ticket(show_id, row-1, col-1)
            while id:
                if id == 1:
                    row = int(input('Enter another row : '))
                    col = int(input('Enter another col : '))
                    id = halls.book_ticket(show_id, row-1, col -1)
                if id == 2:
                    show_id = int(input('Enter correct id : '))
                    id = halls.book_ticket(show_id, row-1, col -1)
    else:
        break

