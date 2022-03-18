town = input()
volume_sales = float(input())

bonus = 0

if town == "Sofia":
    if 0 <= volume_sales <= 500:
        bonus = 0.05
    elif 500 < volume_sales <= 1000:
        bonus = 0.07
    elif 1000 < volume_sales <= 10000:
        bonus = 0.08
    elif volume_sales > 10000:
        bonus = 0.12
    else:
        print("error")
        exit()

elif town == "Varna":
    if 0 <= volume_sales <= 500:
        bonus = 0.045
    elif 500 < volume_sales <= 1000:
        bonus = 0.075
    elif 1000 < volume_sales <= 10000:
        bonus = 0.1
    elif volume_sales > 10000:
        bonus = 0.13
    else:
        print("error")
        exit()

elif town == "Plovdiv":
    if 0 <= volume_sales <= 500:
        bonus = 0.055
    elif 500 < volume_sales <= 1000:
        bonus = 0.08
    elif 1000 < volume_sales <= 10000:
        bonus = 0.12
    elif volume_sales > 10000:
        bonus = 0.145
    else:
        print("error")
        exit()
else:
    print("error")
    exit()
commission = volume_sales * bonus

print(f"{commission:.2f}")