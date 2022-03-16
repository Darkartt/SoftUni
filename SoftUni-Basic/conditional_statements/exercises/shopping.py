petar_budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards * 250
one_processors_price = video_cards_price * 0.35
processors_price = processors * one_processors_price
one_ram_price = video_cards_price * 0.10
ram_price = one_ram_price * ram

total_price = video_cards_price + processors_price + ram_price
discount = total_price * 0.15

if video_cards > processors:
    total_price = total_price - discount

if petar_budget >= total_price:
    print(f"You have {petar_budget - total_price:.2f} leva left!")
elif total_price > petar_budget:
    print(f"Not enough money! You need {total_price - petar_budget:.2f} leva more!")