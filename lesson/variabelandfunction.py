# Ask user for their name 
name = input ("what is your name? ")

#remove whitespace from str
name = name.strip()

# capitalize the first letter of the name
name = name.capitalize()

# capitalize the user name 
name = name.title()


first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")
 