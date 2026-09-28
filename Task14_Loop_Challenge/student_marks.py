marks = [78, 92, 45, 67, 88, 53, 99]

count_90_plus = 0
count_75_89 = 0
count_50_74 = 0
count_below_50 = 0

for m in marks:
    if m >= 90:
        count_90_plus += 1
    elif m >= 75:
        count_75_89 += 1
    elif m >= 50:
        count_50_74 += 1
    else:
        count_below_50 += 1

print("90+ :", count_90_plus)
print("75–89 :", count_75_89)
print("50–74 :", count_50_74)
print("Below 50 :", count_below_50)
