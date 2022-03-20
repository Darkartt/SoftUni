amount_of_people = int(input())
amount_of_nights = int(input())
amount_of_cards_for_transport = int(input())
amount_of_tickets = int(input())

discount = 0.25

nights_price = amount_of_nights * 20
card_for_transport_price = amount_of_cards_for_transport * 1.60
ticket_price = amount_of_tickets * 6

price_for_one_person = nights_price + card_for_transport_price + ticket_price

total_price_for_all = price_for_one_person * amount_of_people

total_price = total_price_for_all + (total_price_for_all * discount)

print(f"{total_price:.2f}")