meters_that_will_be_landscaped = float(input())

the_price_for_landsacping = meters_that_will_be_landscaped * 7.61
discount = the_price_for_landsacping * 0.18
total_price = the_price_for_landsacping - discount

print(f"the total price is {total_price}")
print(f"discount is {discount}")