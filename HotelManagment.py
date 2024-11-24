from datetime import date

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'std': [101, 102, 103], 'Delux': [201, 202, 203], 'Executive': [301, 302, 303], 'Suite': [401, 402, 403]}
        self.roomprice = {1: 2000, 2: 4000, 3: 5000, 4: 6000}

    def check_in(self, Name, Address, phone):
        roomtype = int(input('Room types:\n1.standard \n2.Deluxe\n3.Executive\n4.Suite\n Select a room type: '))
        if roomtype == 1:
            if self.available_rooms['std']:
                room_no = self.available_rooms['std'].pop(0)
            else:
                print('Sorry, standard room not available')
                return
        elif roomtype == 2:
            if self.available_rooms['Delux']:
                room_no = self.available_rooms['Delux'].pop(0)
            else:
                print('Sorry, Deluxe room not available')
                return
        elif roomtype == 3:
            if self.available_rooms['Executive']:
                room_no = self.available_rooms['Executive'].pop(0)
            else:
                print('Sorry, Executive room not available')
                return
        elif roomtype == 4:
            if self.available_rooms['Suite']:
                room_no = self.available_rooms['Suite'].pop(0)
            else:
                print('Sorry, Suite room not available')
                return
        else:
            print("Choose a valid room type")
            return

        d, m, y = map(int, input('Enter check-in-date in date, month, year: ').split())
        check_in = date(y, m, d)
        self.rooms[room_no] = {
            'name': Name,
            'address': Address,
            'phone': phone,
            'check_in_date': check_in,
            'room_type': roomtype,
            'roomservice': 0
        }
        print(f"Checked in {Name}, {Address} to room: {room_no} on {check_in}")

    def room_service(self, room_no):
        if room_no in self.rooms:
            print("****** GALAXY RESTURANT MENUE ******")
            print("1.Tea/coffee:Rs.20 2.Dessert:Rs.70 3.Breakfast:Rs.100 4.Lunch:Rs.150 5.Dinner:Rs.120 6.Exit")
            while 1:
                c=int(input("Select your choice:"))
                if c==1:
                    q=int(input("Enter the quantity:"))
                    self.rooms[room_no] ['roomservice'] +=20*q
                elif c==2:
                    q=int(input("Enter the quantity"))
                    self.rooms[room_no] ['roomservice'] +=70*q
                elif c==3:
                    q=int(input("Enter the quantity"))
                    self.rooms[room_no] ['roomservice'] +=100*q
                elif c==4:
                    q=int(input("Enter the quantity"))
                    self.rooms[room_no] ['roomservice'] +=150*q
                elif c==2:
                    q=int(input("Enter the quantity"))
                    self.rooms[room_no] ['roomservice'] +=120*q
                elif c==6:
                    break
                else:
                    print("Invalid option")
    
            print("Room service Rs:",self.rooms[room_no] ['roomservice'],"\n")
        else:
            print('Invalid room number')
        

                    

    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at the moment ")
        else:
            print("Occupied Rooms: ")
            print("-------------------")
            print('Room no.  Name  Phone')
            print("-------------------")
            for room_number, details in self.rooms.items():
                print(room_number,'\t',details['name'],'\t',details['phone'])


    def check_out(self, room_number):
        
     def start_app(self):
        while True:
            print("-----------------")
            print("Welcome To Galaxy Hotel")
            print("1. Check-in")
            print("2. Room service")
            print("3. Display occupied room")
            print("4. Check-out")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                Name = input("Enter Client Name: ")
                Address = input("Enter Address: ")
                phone = int(input("Enter Contact No. : "))
                self.check_in(Name, Address, phone)
            elif choice == '2':
                room_no = int(input("Enter room number: "))
                self.room_service(room_no)
            elif choice == '3':
                self.display_occupied()
            elif choice == '4':
                room_number = int(input("Enter room number: "))
                self.check_out(room_number)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again")

h = Hotel()
h.start_app()



