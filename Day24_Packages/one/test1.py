from common import pattern, is_prime, fib as fibnacci

# import common
# pattern = common.pattern
# is_prime = common.is_prime
# fib = common.fib
# fibnacci = fib = common.fib
# del fib
# del common


print('\n\n')

for num in range(1, 101):
    if is_prime(num):
        print(num, end=', ')

print('\n\n')
pattern()
print('\n\n')

for i in range(1, 21):
    print(fibnacci(i), end=', ')

print('\n\n')
pattern()
print('\n\n')
