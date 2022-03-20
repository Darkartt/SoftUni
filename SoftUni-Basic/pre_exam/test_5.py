best_player = ''
best_player_goals = 0

while True:
    if best_player_goals >= 10:
        break
    player_name = input()
    if player_name == "END":
        break
    goals = int(input())
    if goals > best_player_goals:
        best_player = player_name
        best_player_goals = goals
    if goals == 10:
        break

print(f"{best_player} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")