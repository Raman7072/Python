def hello(name):
    print(f"Hello {name}!! Welcome to Module a")

def pattern(nrows):
    for row in range(1, nrows+1):
        print(" "*(nrows-row), "*"*row, sep='')