month = input()
days_sleeping = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = days_sleeping * 50
    price_apartment = days_sleeping * 65
    if days_sleeping > 14:
        price_studio *= 0.70
    elif days_sleeping > 7:
        price_studio *= 0.95

if month == "June" or month == "September":
    price_studio = days_sleeping * 75.20
    price_apartment = days_sleeping * 68.70
    if days_sleeping > 14:
        price_studio *= 0.80

if month == "July" or month == "August":
    price_studio = days_sleeping * 76
    price_apartment = days_sleeping * 77

if days_sleeping > 14:
    price_apartment *= 0.90


print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

if diff < 59:
    print("Early")
    print(f"{diff} before the start")
elif diff > 59:
    hours = diff // 60
    minutes = diff = 60
    print("Early")
    print(f"{hours}:{minutes:.2d} hours before the start")