from models import Room, Customer, Booking
from utils import calculate_total_price

def main():
    print("Welcome to the Hotel Booking System")
    while True:
        print("\n1. Add Room")
        print("2. Add Customer")
        print("3. Make Booking")
        print("4. View Bookings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            room_type = input("Enter room type: ")
            price_per_night = float(input("Enter price per night: "))
            Room.add_room(room_type, price_per_night)
            print("Room added successfully.")

        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            Customer.add_customer(first_name, last_name, email, phone_number)
            print("Customer added successfully.")

        elif choice == '3':
            customer_id = int(input("Enter customer ID: "))
            room_id = int(input("Enter room ID: "))
            check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
            check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
            total_price = calculate_total_price(room_id, check_in_date, check_out_date)
            booking_status = "Confirmed"
            Booking.add_booking(customer_id, room_id, check_in_date, check_out_date, total_price, booking_status)
            print("Booking added successfully.")

        elif choice == '4':
            # You can add a function to view all bookings here
            pass

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()