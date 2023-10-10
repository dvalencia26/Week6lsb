def greet(name):
    return "Hello," + name + "!"


def add(a, b):
    Sum = a + b
    return Sum


def main():
    print("in utilities.py main function")


if __name__ == '__main__':
    x = greet("NCF")
    if x == "Hello,NCF!":
        print("Test passed")
