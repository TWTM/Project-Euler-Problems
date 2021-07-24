# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Check if the number is divisible by the numbers.
# Range is only 11 through 21 because all of the 
# numbers that are below that will be checked automatically
# Ex: 3 will be checked together with 12, 5 will be checked with 15
def divisible(x):
    for i in range(11,21):
        if x % i != 0:
            return False
    return True 
x = 20
divisible(x)

# If the number is divisible by all the 10 numbers then we'll print it, otherwise, we'll add 20 to it
while divisible(x) == False:
    x += 20
print(x)


