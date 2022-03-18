budget = float(input())
season = input()

destination = ""
place = ""
cost = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        budget = budget * 0.30
    elif season == "winter":
        place = "Hotel"
        budget = budget * 0.70
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        budget = budget * 0.40
    elif season == "winter":
        place = "Hotel"
        budget = budget * 0.80
if budget > 1000:
    destination = "Europe"
    if season == "summer" or season == "winter":
        place = "Hotel"
        budget = budget * 0.90



print(f"Somewhere in {destination}")
print(f"{place} - {budget:.2f}")