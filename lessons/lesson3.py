n = 100
i = 0
sumdist = 0
distdodoma = 0


while i < n:
    i = i + 1
    
    current_dist = 1 / i
    sumdist = sumdist + current_dist

    if i % 2 != 0:
        distdodoma = distdodoma + current_dist
    else:
        distdodoma = distdodoma - current_dist

print(f"дистанция до дома {distdodoma:.2f} km")
        

print(f"суммарная дистанция равна {sumdist:.2f} km")





