def mukmmal_sonlarni_top(n):
    mukammal_sonlar = []
    for i in range(1, n + 1):
        divisor_sum = 0
        for j in range(1, i):
            if i % j == 0:
                divisor_sum += j
        if divisor_sum == i:
            mukammal_sonlar.append(i)
    return mukammal_sonlar

print(mukmmal_sonlarni_top(10))