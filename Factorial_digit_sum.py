fat = 1
for i in range(1,101):
    fat = fat * i 

sum = 0
fat = str(fat)
for i in fat:
    sum += int(i)
print(sum) 
