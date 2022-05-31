money_needed = float(input())
money_save = float(input())

days = 0
days_in_row = 0

while True:
    command = input()
    money = float(input())
    if money_save < 0:
        money_save = 0

    if command == 'spend':
        money_save -= money
        days += 1
        days_in_row += 1
        if days_in_row >= 5:
            break

    if command == 'save':
        money_save += money
        days += 1
        days_in_row = 0
        if money_save >= money_needed:
            break
if (money_needed > money_save) or days_in_row == 5:
    print("You can't save the money.")
    print(f"{days}")

else:
    print(f"You saved the money for {days} days.")
