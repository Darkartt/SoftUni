teresa_money_per_day = float(input())
money_won_per_day = float(input())
money_spend_all = float(input())
gift_price = float(input())

days_left = 5

money_saved = days_left * teresa_money_per_day
money_won = days_left * money_won_per_day
total_money_saved = money_saved + money_won
cost = total_money_saved - money_spend_all

money_left = abs(cost - gift_price)

if cost >= gift_price:
    print(f"Profit: {cost:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {money_left:.2f} BGN.")