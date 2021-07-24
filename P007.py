import math
import time
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

## Check if the number presented is a prime number
def prime(x):
    ## Only need to check until the square root of the number to see if it is a prime number
    ## Starting from 3 since I disconsidered the even numbers
    for i in range(3,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True
# Starting from 3 since ill be checking only odd numbers
numchecked = 3
# 2 was already considered and is the only even prime number
primecount = 1

while primecount < 10001:
    if prime(numchecked) == True:
        primecount+=1
    numchecked +=2
print(numchecked)