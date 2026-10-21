
appointments = []

def book_appointment():
    print("\n--- Book Appointment ---")

    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date: ")
    time = input("Enter appointment time: ")

    appointment = {
        "Patient Name": patient_name,
        "Doctor Name": doctor_name,
        "Date": date,
        "Time": time
    }

    appointments.append(appointment)

    print("\nAppointment booked successfully!")

def view_appointments():
    print("\n--- View Appointments ---")

    if len(appointments) == 0:
        print("No appointments available.")
    else:
        for i, appointment in enumerate(appointments, start=1):
            print(f"\nAppointment {i}")
            print("Patient Name:", appointment["Patient Name"])
            print("Doctor Name:", appointment["Doctor Name"])
            print("Date:", appointment["Date"])
            print("Time:", appointment["Time"])

while True:
    print("\n===== Hospital Appointment Booking System =====")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_appointment()
    elif choice == "2":
        view_appointments()
    elif choice == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.")
