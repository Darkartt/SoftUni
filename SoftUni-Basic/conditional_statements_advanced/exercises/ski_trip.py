days = int(input())
place = input()
rating = input()

days_staying = days - 1
room_for_one_person_price = days_staying * 18
apartment_price = days_staying * 25
president_apartment_price = days_staying * 35

if place == "apartment":
    if days_staying < 10:
        apartment_price *= 0.70
    elif 10 <= days_staying < 15:
        apartment_price *= 0.65
    elif days_staying > 15:
        apartment_price *= 0.50

elif place == "president apartment":
    if days_staying < 10:
        president_apartment_price *= 0.90
    elif 10 <= days_staying < 15:
        president_apartment_price *= 0.85
    elif days_staying > 15:
        president_apartment_price *= 0.80

if rating == "positive":
    apartment_price = apartment_price + (apartment_price * 0.25)
    president_apartment_price = president_apartment_price + (president_apartment_price * 0.25)
    room_for_one_person_price = room_for_one_person_price + (room_for_one_person_price * 0.25)
elif rating == "negative":
    apartment_price = apartment_price - (apartment_price * 0.10)
    president_apartment_price = president_apartment_price - (president_apartment_price * 0.10)
    room_for_one_person_price = room_for_one_person_price - (room_for_one_person_price * 0.10)

if place == "apartment":
    print(f"{apartment_price:.2f}")
elif place == "president apartment":
    print(f"{president_apartment_price:.2f}")
elif place == "room for one person":
    print(f"{room_for_one_person_price:.2f}")
