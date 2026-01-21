distance = 10
sum_dist = distance


for i in range (2,10+1):
    distance = distance + distance * 0.1
    print(f"день №{i} = {distance:.1f} км")

    if i <= 7:
        sum_dist = sum_dist + distance

print(f"За 7 дней суммарная дистанция = {sum_dist:.1f} km")