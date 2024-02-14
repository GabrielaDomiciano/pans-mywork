# Program to subtract on number from another.
# iinput reads in a string so we need to convert it into an int
# so we can perform mathematical operations
#author Gabriela Domiciano

#Input returns a str,so we need to convert this to an int if we are going to do arithmetic on it


x = int (input ("Enter first number: "))
y = int (input ("Enter second number: "))

answer = x-y

print ("{} minus {} is {} " .format(x, y, answer))