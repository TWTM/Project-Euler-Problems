import math

def divisors(x):
    x_divisors = [1] # começa no um porque 1 é sempre um divisor
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            if i != x/i:
                x_divisors.extend([i,x/i])
            else:
                x_divisors.append(i)
    return sum(x_divisors)

print(divisors(10))

amicable = []

for i in range(1,10000):

    x = (divisors(i))
    if x != i:
        if divisors(x) == i:
            amicable.append(i)
            print("amicable", i , x)
            print(sum(amicable))
    