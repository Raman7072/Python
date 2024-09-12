"""
    common programs listed here
    is_prime(num)
    fab(n)
    is_even(num)
"""
__author__ = "sachin"

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        for check in range(2, int(num**(1/2))+2):
            if num % check == 0:
                return False
    return True 

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def test():
    assert is_prime(121) == False, "Prime Function has Failed"
    assert is_prime(127) == True, "Prime Function has Failed"
    print("is_prime working fine")
    assert fib(5) == 3, "Fib Function Failed" # 0 1 1 2 3 5 8
    assert fib(7) == 8, "Fib function Failed"
    print("fib function working fine")
    assert is_even(12) == True, "Even Fuction Failed"
    assert is_even(11) == False, "Even Function Failed"
    print("is_even function working wine")


def pattern():
    print("--"*60)
    print('--'*60)
    print()
    print()
    print("__"*60)
    print("__"*60)

if __name__ == "__main__":
    try:
        test()
    except AssertionError as error:
        print("Test Failed!!", {error})
    else:
        print("All Test Case Passed Sucessfully!")
