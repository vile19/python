def main():
    name = input("what should i call you? ").title()
    hello(name + (", pleasure to meet you!"))


def hello(to="Sir"):
    print("Hello,", to)


main()