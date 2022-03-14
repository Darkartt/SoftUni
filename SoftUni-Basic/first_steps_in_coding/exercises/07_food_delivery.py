chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegetarian_price = vegetarian_menu * 8.15

price = chicken_price + fish_price +vegetarian_price
desert = price * (20 / 100)
delivery = 2.50

total_price = price + desert + delivery

print(total_price)