from conection import connect_db

class Room:
    def __init__(self, room_type, price_per_night, is_available=True):
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available

    @staticmethod
    def add_room(room_type, price_per_night):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO rooms (room_type, price_per_night, is_available) VALUES (%s, %s, %s)",
            (room_type, price_per_night, True)
        )
        conn.commit()
        cursor.close()
        conn.close()

    # Add more methods like update_room, get_available_rooms, etc.


class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def add_customer(first_name, last_name, email, phone_number):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO customers (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, phone_number)
        )
        conn.commit()
        cursor.close()
        conn.close()


class Booking:
    def __init__(self, customer_id, room_id, check_in_date, check_out_date, total_price, booking_status):
        self.customer_id = customer_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_price = total_price
        self.booking_status = booking_status

    @staticmethod
    def add_booking(customer_id, room_id, check_in_date, check_out_date, total_price, booking_status):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booking (customer_id, room_id, check_in_date, check_out_date, total_price, booking_status) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (customer_id, room_id, check_in_date, check_out_date, total_price, booking_status)
        )
        conn.commit()
        cursor.close()
        conn.close()