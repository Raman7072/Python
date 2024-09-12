def hello():
    """
        It is a greeting function
    """
    print("Hello World")

def pattern(nrows):
    """
        it will print a left right angle triangle
    """
    for row in range(1, nrows+1):
        print("*"*row)

# python file
# python script / module

# __name__ will tell name of current name space in which you are executing code


print(f"Value of __name__ == {__name__}")

hello() 

pattern(10)

hello()