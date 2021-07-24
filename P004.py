# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
for i in range(100,1000):
    for x in range(100,1000):
        n = str(i*x)
        if list(reversed(n)) == list(n):
            print(i,x,i*x)