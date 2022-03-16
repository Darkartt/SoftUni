record_in_seconds = float(input())
distance_in_meters = float(input())
time_to_swim_1_meter = float(input())

time_to_swim_in_seconds = distance_in_meters * time_to_swim_1_meter
resistance = distance_in_meters // 15
resistance_seconds = resistance * 12.5
total_time = time_to_swim_in_seconds + resistance_seconds

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif total_time >= record_in_seconds:
    print(f"No, he failed! He was {abs(record_in_seconds - total_time):.2f} seconds slower.")