page_amount = int(input())
page_per_hour = int(input())
amount_of_days = int(input())

hours_to_read = page_amount / page_per_hour
hours_per_day = hours_to_read / amount_of_days

print(int(hours_per_day))