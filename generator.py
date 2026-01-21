import time
import random
from datetime import datetime
import mysql.connector

cities = ["Москва", "Санкт-Петербург", "Владивосток", "Волгоград"]
zones = ["Центр", "Спальный район", "Аэропорт", "Вокзал", "Бизнес-квартал"]

def generate_ride():
    city = random.choice(cities)
    from_zone = random.choice(zones)
    to_zone = random.choice(zones)
    distance_km = round(random.uniform(1.0, 25.0), 2)
    price = round(distance_km * random.uniform(35, 55), 2)
    rating = random.randint(3, 5)

    ride = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "city": city,
        "from_zone": from_zone,
        "to_zone": to_zone,
        "distance_km": distance_km,
        "price": price,
        "rating": rating
    }

    return ride

def main():
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1111',
        database='taxi'
    )
    cursor = connection.cursor()

    try:
        while True:
            ride = generate_ride()
            query = """
                INSERT INTO rides (timestamp, city, from_zone, to_zone, distance_km, price, rating)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                ride["timestamp"],
                ride["city"],
                ride["from_zone"],
                ride["to_zone"],
                ride["distance_km"],
                ride["price"],
                ride["rating"]
            ))
            connection.commit()
            print(ride)
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
