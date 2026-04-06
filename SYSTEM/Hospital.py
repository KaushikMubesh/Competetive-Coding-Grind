from datetime import datetime

# -------- DOCTOR CLASS --------
class Doctor:
    def __init__(self, doc_id, name, specialization, fee):
        self.doc_id = doc_id
        self.name = name
        self.specialization = specialization
        self.fee = fee

    def display(self):
        print(f"ID: {self.doc_id} | Dr. {self.name} ({self.specialization}) | Fee: ₹{self.fee}")


# -------- PATIENT CLASS --------
class Patient:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def view_appointments(self):
        if not self.appointments:
            print("No appointments.")
        else:
            print("\n--- Your Appointments ---")
            for i, a in enumerate(self.appointments, 1):
                print(f"{i}. {a}")


# -------- APPOINTMENT CLASS --------
class Appointment:
    def __init__(self, patient_name, doctor, date):
        self.patient_name = patient_name
        self.doctor = doctor
        self.date = date
        self.status = "Booked"

    def __str__(self):
        return f"{self.date} | Dr.{self.doctor.name} ({self.doctor.specialization}) | Status: {self.status}"


# -------- HOSPITAL SYSTEM --------
class HospitalSystem:
    def __init__(self):
        self.doctors = {}
        self.patients = {}
        self.current_patient = None

        # Sample Doctors
        self.doctors["D1"] = Doctor("D1", "Ravi", "Cardiologist", 500)
        self.doctors["D2"] = Doctor("D2", "Meena", "Dermatologist", 300)

    # -------- ADMIN --------
    def add_doctor(self):
        doc_id = input("Enter Doctor ID: ")
        name = input("Enter Name: ")
        spec = input("Enter Specialization: ")
        fee = int(input("Enter Consultation Fee: "))

        self.doctors[doc_id] = Doctor(doc_id, name, spec, fee)
        print("✅ Doctor added successfully!")

    # -------- PATIENT --------
    def register(self):
        username = input("Enter username: ")
        if username in self.patients:
            print("User already exists.")
            return
        password = input("Enter password: ")
        age = int(input("Enter age: "))

        self.patients[username] = Patient(username, password, age)
        print("✅ Registered successfully!")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        patient = self.patients.get(username)
        if patient and patient.password == password:
            self.current_patient = patient
            print(f"✅ Welcome {username}")
            self.patient_menu()
        else:
            print("❌ Invalid credentials")

    # -------- DOCTOR VIEW --------
    def view_doctors(self):
        print("\n--- Available Doctors ---")
        for doc in self.doctors.values():
            doc.display()

    # -------- APPOINTMENT --------
    def book_appointment(self):
        self.view_doctors()
        doc_id = input("Enter Doctor ID: ")
        doctor = self.doctors.get(doc_id)

        if not doctor:
            print("❌ Doctor not found.")
            return

        date = input("Enter date (YYYY-MM-DD): ")

        appointment = Appointment(self.current_patient.username, doctor, date)
        self.current_patient.add_appointment(appointment)

        print("✅ Appointment booked!")
        print(f"💰 Fee to pay: ₹{doctor.fee}")

    def cancel_appointment(self):
        self.current_patient.view_appointments()
        index = int(input("Enter appointment number to cancel: ")) - 1

        if 0 <= index < len(self.current_patient.appointments):
            self.current_patient.appointments[index].status = "Cancelled"
            print("✅ Appointment cancelled")
        else:
            print("❌ Invalid choice")

    # -------- MENU --------
    def patient_menu(self):
        while True:
            print("\n===== PATIENT MENU =====")
            print("1. View Doctors")
            print("2. Book Appointment")
            print("3. View Appointments")
            print("4. Cancel Appointment")
            print("5. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_doctors()

            elif choice == "2":
                self.book_appointment()

            elif choice == "3":
                self.current_patient.view_appointments()

            elif choice == "4":
                self.cancel_appointment()

            elif choice == "5":
                print("Logged out.")
                break

            else:
                print("Invalid choice")


# -------- MAIN --------
system = HospitalSystem()

while True:
    print("\n====== HOSPITAL SYSTEM ======")
    print("1. Admin - Add Doctor")
    print("2. Patient Register")
    print("3. Patient Login")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_doctor()

    elif choice == "2":
        system.register()

    elif choice == "3":
        system.login()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")