# Program to subtract on number from another

# inputs reads in a string so we need to convertr it into an int
# so we can perform mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) 
# // gives the int division
remainder = x%y 
# % gives the remainder

print("{} divided by {} is {} with remainder {}".format( x, y,
answer, remainder))