import math

x1 = int(input("Enter min value for range: "))
x2 = int(input("Enter max value for range: "))
val = 0
prime = []

for n in range(x1, x2 + 1):
    if n > 1:
        for x in range(2, n):
            if (n % x) == 0:
                break
        else:
            val += n
            prime.append(n)
    #if n == 2:
        #val += n
        #prime.append(n)

print(prime)
