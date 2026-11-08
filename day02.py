# Exercise 1: Greeting
name = " ".join(input("What's your name? ").split()).title()
print(f"Hello, {name}!")

# Exercise 2: Two numbers
x = float(input("Enter first number "))
y = float(input("Enter second number "))


print(f"Sum: {(x+y):.2f}")
print(f"Difference: {(x-y):.2f}")
print(f"Product: {(x*y):.2f}")
if y == 0:
    print("Cannot Divide by zero")
else:
    print(f"Division: {(x/y):.2f}")


# Exercise 3: Name Length
full_name = input("What's your full name? ").replace(" ", "")
full_name_length = len(full_name)
print(f"Full Name length is: {full_name_length}")


# Exercise 4: Initials
NAME = input("What's your name? ")
words = NAME.split()
for part in words: 
    print(f"{part[0].upper()}.", end="")

print()