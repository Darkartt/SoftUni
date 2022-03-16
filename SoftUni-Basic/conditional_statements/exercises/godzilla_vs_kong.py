movie_budget = float(input())
amount_of_statists = int(input())
price_for_clothes_for_one_statist = float(input())

decor = movie_budget * (10/100)
total_price_for_clothes = price_for_clothes_for_one_statist * amount_of_statists

if amount_of_statists > 150:
    total_price_for_clothes *= 0.90

total_movie_amount = total_price_for_clothes + decor

if total_price_for_clothes + decor > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_movie_amount - movie_budget:.2f} leva more.")

elif total_price_for_clothes + decor <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - total_movie_amount:.2f} leva left.")