name = input("what is your name? ")

match name:
    case "harry" | "hermione" | "ron":
        print("griffindor")
    case "draco":
        print("slytherin")
    case _:
        print("who? ")
