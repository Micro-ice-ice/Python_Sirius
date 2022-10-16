from sys import argv
from math import sqrt

try:
    n = int(argv[1])
    prime_numbers = []

    for i in range(2, n + 1):
        if i > 10:
            if (i % 2 == 0) or (i % 10 == 5):
                continue
        for j in prime_numbers:
            if j > int((sqrt(n + 1))):
                prime_numbers.append(i)
                break
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

    sum_of_prime = 0

    for i in prime_numbers:
        sum_of_prime = sum_of_prime + i

    #  print(prime_numbers)
    print(sum_of_prime)

except:
    print("Error")



