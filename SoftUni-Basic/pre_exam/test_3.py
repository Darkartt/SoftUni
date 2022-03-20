amount_of_dancers = int(input())
amount_of_points = float(input())
season = input()
place = input()

money_left = 0
charity = 0
dancers_point_won = amount_of_dancers * amount_of_points
dancers_point_won_aboard = dancers_point_won + (dancers_point_won * 0.50)
money_per_dancer = 0

if place == "Bulgaria":
    if season == "summer":
        dancers_point_won = dancers_point_won - (dancers_point_won * 0.05)
        charity = dancers_point_won * 0.75
        money_left = dancers_point_won - charity
    elif season == "winter":
        dancers_point_won = dancers_point_won - (dancers_point_won * 0.08)
        charity = dancers_point_won * 0.75
        money_left = dancers_point_won - charity

if place == "Abroad":
    if season == "summer":
        dancers_point_won_aboard = dancers_point_won_aboard - (dancers_point_won_aboard * 0.10)
        charity = dancers_point_won_aboard * 0.75
        money_left = dancers_point_won_aboard - charity
    elif season == "winter":
        dancers_point_won_aboard = dancers_point_won_aboard - (dancers_point_won_aboard * 0.15)
        charity = dancers_point_won_aboard * 0.75
        money_left = dancers_point_won_aboard - charity

money_per_dancer = money_left / amount_of_dancers

print(f"Charity - {charity:.2f} ")
print(f"Money per dancer - {money_per_dancer:.2f}")