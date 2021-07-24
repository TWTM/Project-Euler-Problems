# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
sum = 2
# Skipping even numbers
for i in range(3,2000000,2):
    # Prime will be initially set to True until proved otherwise
    prime = True
    # Checking to see if the number is prime
    for x in range(3,int(i**0.5)+1,2):
        if i % x == 0: 
            prime = False
            break
    if prime == True:
        # add the prime number to the sum
        sum += i
print(sum)

