def factorial(n):
    n *= 10000
    number = 1
    while n > 1:
        number *= n
        n -= 1
