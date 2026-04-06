class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def view_bookings(self):
        if not self.bookings:
            print("No bookings found.")
        else:
            print("\n--- Your Bookings ---")
            for b in self.bookings:
                print(b)


class TravelOption:
    def __init__(self, id, source, destination, price):
        self.id = id
        self.source = source
        self.destination = destination
        self.price = price

    def display(self):
        print(f"ID: {self.id} | {self.source} → {self.destination} | ₹{self.price}")


class Flight(TravelOption):
    def __init__(self, id, source, destination, price, airline):
        super().__init__(id, source, destination, price)
        self.airline = airline

    def display(self):
        print(f"[Flight] {self.airline} | ID: {self.id} | {self.source} → {self.destination} | ₹{self.price}")


class Train(TravelOption):
    def __init__(self, id, source, destination, price, train_name):
        super().__init__(id, source, destination, price)
        self.train_name = train_name

    def display(self):
        print(f"[Train] {self.train_name} | ID: {self.id} | {self.source} → {self.destination} | ₹{self.price}")


class Hotel:
    def __init__(self, id, name, city, price_per_night):
        self.id = id
        self.name = name
        self.city = city
        self.price = price_per_night

    def display(self):
        print(f"[Hotel] {self.name} | ID: {self.id} | City: {self.city} | ₹{self.price}/night")


class TravelBookingSystem:
    def __init__(self):
        self.users = {}
        self.current_user = None

        # Sample Data
        self.flights = [
            Flight("F1", "Chennai", "Delhi", 5000, "IndiGo"),
            Flight("F2", "Mumbai", "Bangalore", 4000, "Air India")
        ]

        self.trains = [
            Train("T1", "Chennai", "Madurai", 800, "Pandian Express"),
            Train("T2", "Coimbatore", "Chennai", 900, "Cheran Express")
        ]

        self.hotels = [
            Hotel("H1", "Taj Hotel", "Delhi", 3000),
            Hotel("H2", "Oberoi", "Mumbai", 3500)
        ]

    # -------- USER --------
    def register(self):
        username = input("Enter username: ")
        if username in self.users:
            print("User already exists.")
            return
        password = input("Enter password: ")
        self.users[username] = User(username, password)
        print("✅ Registered successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            print(f"✅ Welcome {username}")
            self.user_menu()
        else:
            print("❌ Invalid credentials")

    # -------- SEARCH --------
    def search_flights(self):
        print("\n--- Available Flights ---")
        for f in self.flights:
            f.display()

    def search_trains(self):
        print("\n--- Available Trains ---")
        for t in self.trains:
            t.display()

    def search_hotels(self):
        print("\n--- Available Hotels ---")
        for h in self.hotels:
            h.display()

    # -------- BOOK --------
    def book(self, category):
        id = input("Enter ID to book: ")

        items = []
        if category == "flight":
            items = self.flights
        elif category == "train":
            items = self.trains
        elif category == "hotel":
            items = self.hotels

        for item in items:
            if item.id == id:
                self.current_user.add_booking(str(item.__dict__))
                print("✅ Booking successful!")
                return

        print("❌ Invalid ID")

    # -------- CANCEL --------
    def cancel_booking(self):
        self.current_user.view_bookings()
        index = int(input("Enter booking number to cancel: ")) - 1

        if 0 <= index < len(self.current_user.bookings):
            self.current_user.bookings.pop(index)
            print("✅ Booking cancelled")
        else:
            print("❌ Invalid choice")

    # -------- MENU --------
    def user_menu(self):
        while True:
            print("\n===== USER MENU =====")
            print("1. Flights")
            print("2. Trains")
            print("3. Hotels")
            print("4. View Bookings")
            print("5. Cancel Booking")
            print("6. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.search_flights()
                self.book("flight")

            elif choice == "2":
                self.search_trains()
                self.book("train")

            elif choice == "3":
                self.search_hotels()
                self.book("hotel")

            elif choice == "4":
                self.current_user.view_bookings()

            elif choice == "5":
                self.cancel_booking()

            elif choice == "6":
                print("Logged out.")
                break

            else:
                print("Invalid choice")


# -------- MAIN --------
system = TravelBookingSystem()

while True:
    print("\n====== TRAVEL BOOKING SYSTEM ======")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.register()

    elif choice == "2":
        system.login()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice")