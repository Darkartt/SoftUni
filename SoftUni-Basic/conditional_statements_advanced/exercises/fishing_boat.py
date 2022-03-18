budget = int(input())
season = input()
amount_of_fishermen = int(input())

boat_price = 0


if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if amount_of_fishermen <= 6:
    boat_price -= boat_price * 0.10
elif 7 <= amount_of_fishermen <= 11:
    boat_price -= boat_price * 0.15
elif amount_of_fishermen >= 12:
    boat_price -= boat_price * 0.25

if amount_of_fishermen % 2 == 0 and season != "Autumn":
    boat_price -= boat_price * 0.5

diff = abs(budget - boat_price)

if budget >= boat_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")