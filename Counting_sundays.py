
d30 = (9,4,6,11)
count = 1
sunday = 0
for year in range(1901,2001):

    for i in range(1,13):
        if i in d30:
            month = 30
        else:
            month = 31
        if i == 2:
            if year % 4 != 0:
                month = 28
            else:
                month = 29

        for days in range(1,month+1):
            count+=1
            if count % 7 == 0 and days == 1:
                sunday += 1
    
print(sunday)
