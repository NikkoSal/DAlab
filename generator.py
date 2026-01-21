import time
import random
from datetime import datetime

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
        "from": from_zone,
        "to": to_zone,
        "distance_km": distance_km,
        "price": price,
        "rating": rating
    }

    return ride


if __name__ == "__main__":
    while True:
        ride = generate_ride()
        print(ride)
        time.sleep(1)
