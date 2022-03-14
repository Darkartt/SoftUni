packs_of_pens_needed = int(input())
packs_of_markers_needed = int(input())
liters_of_dashboard_cleaner = int(input())
discount = int(input())


packs_of_pens = packs_of_pens_needed * 5.80
packs_of_markers = packs_of_markers_needed * 7.20
dashboard_cleaner = liters_of_dashboard_cleaner * 1.20

total_amount = packs_of_pens + packs_of_markers + dashboard_cleaner
percent_to_float = discount / 100

final_result = total_amount - (total_amount * percent_to_float)

print(final_result)