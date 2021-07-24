'''The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?'''

import math 

i=1  
triangle = 1
numdivisors = 1
while numdivisors < 500:
    numdivisors = 0
    i+=1 # counting to create the next triangle number
    triangle += i # New Triangle Number
    for divisors in range(1,int(triangle**0.5+1)):
        if triangle % divisors == 0:
            numdivisors += 2 # Counting the divisors. counting the pair ex: triangle
                             # ex: triangle num = 28 and the pair is 4*7 so both 4 and 7 will be added to the divisors
                             # will only check to the the square root of that number
                             # and if the number is a perfect square we'll subtract one from the num of divisors
    if math.sqrt(triangle) == int(math.sqrt(triangle)):
        numdivisors -= 1
print(triangle)
