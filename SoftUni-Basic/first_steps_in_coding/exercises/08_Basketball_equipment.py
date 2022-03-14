yearly_tax = int(input())

basketball_shoes = yearly_tax - (yearly_tax * (40 / 100))
basketball_clothes = basketball_shoes - (basketball_shoes * (20 / 100))
basketball_ball = basketball_clothes / 4
basketball_accessory = basketball_ball / 5

total_amount = basketball_shoes + basketball_clothes + basketball_ball + basketball_accessory + yearly_tax


print(total_amount)