flowers = input()
amount_flowers = int(input())
budget = int(input())

final_price = 0

one_rose_price = 5
one_Dahlias_price = 3.80
one_Tulips_price = 2.80
one_Narcissus_price = 3
one_Gladiolus_price = 2.50

if flowers == "Roses":
    final_price = amount_flowers * one_rose_price
    if amount_flowers > 80:
        final_price = final_price - (final_price * 0.10)

if flowers == "Dahlias":
    final_price = amount_flowers * one_Dahlias_price
    if amount_flowers > 90:
        final_price = final_price - (final_price * 0.15)

if flowers == "Tulips":
    final_price = amount_flowers * one_Tulips_price
    if amount_flowers > 80:
        final_price = final_price - (final_price * 0.15)

if flowers == "Narcissus":
    final_price = amount_flowers * one_Narcissus_price
    if amount_flowers < 120:
        final_price = final_price + (final_price * 0.15)

if flowers == "Gladiolus":
    final_price = amount_flowers * one_Gladiolus_price
    if amount_flowers < 80:
        final_price = final_price + (final_price * 0.20)

if budget >= final_price:
    print(f"Hey, you have a great garden with {amount_flowers} {flowers} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")