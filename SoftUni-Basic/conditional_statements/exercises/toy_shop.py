holiday_price = float(input())
puzzle = int(input())
talking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

discount = 0

total_pieces_ordered = puzzle + talking_dolls + bears + minions + trucks

price_of_puzzle = puzzle * 2.60
price_of_talking_dolls = talking_dolls * 3
price_of_bears = bears * 4.10
price_of_minions = minions * 8.20
price_of_truck = trucks * 2

total_price = price_of_puzzle + price_of_talking_dolls + price_of_bears + price_of_minions + price_of_truck

if total_pieces_ordered >= 50:
    discount = total_price * (25/100)

final_money = total_price - discount
mortgage = final_money * (10/100)
money_made = final_money - mortgage


if money_made >= holiday_price:
    print(f"Yes! {money_made - holiday_price:.2f} lv left.")
elif money_made < holiday_price:
    print(f"Not enough money! {holiday_price - money_made:.2f} lv needed.")