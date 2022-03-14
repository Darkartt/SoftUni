length = int(input())
width = int(input())
height = int(input())
percent = float(input())

tank_volume = (length * width * height) / 1000
percent_price = percent / 100

needed_liters = tank_volume * (1 - percent_price)

print(needed_liters)