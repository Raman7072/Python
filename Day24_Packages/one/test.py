import common

for num in range(1, 101):
    if common.is_prime(num):
        print(num, end=', ')

common.pattern()

for i in range(1, 21):
    print(common.fib(i), end=', ')

common.pattern()

