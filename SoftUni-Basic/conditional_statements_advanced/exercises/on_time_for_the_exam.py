exam_hour = int(input())
exam_minutes = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = hour_of_arrival * 60 + minutes_of_arrival
diff = abs(exam_time - arrival_time)

if exam_time == arrival_time:
    print("On time")

# early
if exam_time > arrival_time:
    if diff <= 30:
        print("On time")
        print(f"{abs(diff)} minutes before the start")
    elif diff <= 59:
        print("Early")
        print(f"{abs(diff)} minutes before the start")
    elif diff > 59:
        hours = diff // 60
        minutes = diff % 60
        print("Early")
        print(f"{hours}:{minutes:02d} hours before the start")
# late
elif exam_time < arrival_time:
    if diff <= 59:
        print("Late")
        print(f"{abs(diff)} minutes after the start")
    elif diff > 59:
        hours = diff // 60
        minutes = diff % 60
        print("Late")
        print(f"{hours}:{minutes:02d} hours after the start")