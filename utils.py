from datetime import datetime
from conection import connect_db

def calculate_total_price(room_id, check_in_date, check_out_date):
    conn = connect_db()
    cursor = conn.cursor()
    
    try:
        # Fetch the price per night for the given room ID
        cursor.execute("SELECT price_per_night FROM rooms WHERE room_id = %s", (room_id,))
        result = cursor.fetchone()
        
        if result is None:
            raise ValueError(f"No room found with room_id: {room_id}")
        
        price_per_night = result[0]
        
        # Calculate the number of nights
        check_in = datetime.strptime(check_in_date, '%Y-%m-%d')
        check_out = datetime.strptime(check_out_date, '%Y-%m-%d')
        number_of_nights = (check_out - check_in).days
        
        if number_of_nights <= 0:
            raise ValueError("Check-out date must be after check-in date.")
        
        total_price = price_per_night * number_of_nights
        return total_price
    
    except Exception as e:
        print(f"Error calculating total price: {e}")
        return None  # Return None if there's an error
    finally:
        cursor.close()
        conn.close()
