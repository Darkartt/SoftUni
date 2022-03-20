n = int(input())


for a in range(1, 9):
    for b in range(9, a, -1):
        for c in range(9):
            for d in range(9, c, -1):
                if a + b + c + d == a * b * c * d and str(n)[-1] == str(5):
                    print(f"{a}{b}{c}{d}")
                    exit()
                if (a * b * c * d) // (a + b + c + d) == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    exit()

print("Nothing found")