import math
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143

def fat(x):
    for i in range(2,int(math.sqrt(x))):
        if x % i == 0:
            maxdivisor = i
            fat(x/i)
    print(x)
    exit()
    
fat(600851475143)
