class Star_Cinema:
    __hall_list = []
    def entry_hall(self,hall):
        self.__hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        self.entry_hall(self)

    def entry_show(self,id, movie_name,time):
        for item in self.__show_list:
            if item[0] == id:
                print("Show with id : {id} is already running")
                return
        newShow = (id,movie_name,time)
        self.__show_list.append(newShow)
        seats = []
        for i in range(0,self.__rows):
            temp = []
            for j in range(0,self.__cols):
                temp.append(int(0))
            seats.append(temp)
        self.__seats[id] = seats

    def book_seats(self,id,seatList):
        flag = False
        for shows in self.__show_list:
            if shows[0] == id:
                flag = True
                break
        if flag == False:
            print(f"\nWrong show id {id}\n")
            return
        for seat in seatList:
            if seat[0]< int(0) or seat[0]>=self.__rows or seat[1]< int(0) or seat[1]>=self.__cols:
                print(f"\nSeat {seat} is not a valid seat\n")
            elif self.__seats[id][seat[0]][seat[1]] == 1:
                print(f"\nSeat {seat} is already booked\n")
            else:
                print(f"\nSeat {seat} booked successfully\n")
                self.__seats[id][seat[0]][seat[1]] = 1

    def view_show_list(self):
        print("\n-----------------")
        print("Available shows :\n")
        for shows in self.__show_list:
            print(f'show id : {shows[0]} , show name : {shows[1]} , show time : {shows[2]}')
        print("-----------------")

    def view_available_seats(self,id):
        if id in self.__seats:
            print(f"\nSeats for show id {id} :\n")
            for rows in self.__seats[id]:
                for cols in rows:
                    print(cols,end=' ')
                print()
                    
        else:
            print(f"{id} is an invalid show ID")


hall2 = Hall(5,5,2)
hall2.entry_show('1','Surongo','13 dec, 2024')
hall2.entry_show('2','Daagi','14 dec, 2024')

while True:
    print("\nOptions: \n")
    print("\t1 : View all shows")
    print("\t2 : View available seats")
    print("\t3 : Book tickets")
    print("\te : Exit")
    print()
    opt = input("Enter your option : ")
    if opt == "1":
        hall2.view_show_list()
    elif opt == "2":
        show_id = input("Enter Show ID : ")
        hall2.view_available_seats(show_id)
    elif opt == "3":
        show_id = input("Enter Show ID : ")
        count = int(input("Enter ticket count : "))
        seats = []
        for i in range(0,count):
            row,col = map(int,input(f"{i+1} : Enter row and column : ").split())
            seat = (row,col)
            seats.append(seat)
        hall2.book_seats(show_id,seats)
    elif opt == "e":
        break
    else:
        print("\n\tWrong Option Selected!")