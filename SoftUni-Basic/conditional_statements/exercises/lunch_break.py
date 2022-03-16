import math

name_of_tv_show = input()
length_of_episode = int(input())
break_time = int(input())

lunch_time = break_time * 0.125
rest_time = break_time * 0.25
brake = lunch_time + rest_time
time_left = break_time - brake
free_time = time_left - length_of_episode

if time_left >= length_of_episode:
    print(f"You have enough time to watch {name_of_tv_show} and left with {math.ceil(free_time)} minutes free time.")
elif time_left < length_of_episode:
    print(f"You don't have enough time to watch {name_of_tv_show}, you need {math.ceil(abs(length_of_episode - time_left))} more minutes.")