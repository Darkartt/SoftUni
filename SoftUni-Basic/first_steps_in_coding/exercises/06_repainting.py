amount_of_plastic = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
work_hours = int(input())


plastic_price = (amount_of_plastic + 2) * 1.50
paint_price = amount_of_paint * 14.50
thinner_price = amount_of_thinner * 5
plastic_bag = 0.40



paint_discount = paint_price * (10 / 100)
bonus_paint = paint_price + paint_discount


matirial_total_price = plastic_price + bonus_paint + thinner_price + plastic_bag
worker_price = matirial_total_price * (30 / 100) * work_hours

total_price = matirial_total_price + worker_price

print(total_price)