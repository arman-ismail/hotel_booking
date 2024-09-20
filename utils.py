from connection import connect_db
from datetime import datetime

def calculate_total_price(room_id, check_in_date, check_out_date):
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT price_per_night FROM rooms WHERE room_id = %s", (room_id,))
    price_per_night = cursor.fetchone()[0]
    
    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
    check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
    num_nights = (check_out - check_in).days
    
    total_price = price_per_night * num_nights
    
    cursor.close()
    conn.close()
    
    return total_price
