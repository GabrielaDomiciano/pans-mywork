# Lab Topic 04-Flow control if elif and else
# Author Gabriela Domiciano

# This program reads in a students percentage and prints out the corresponding grade.

percentage = float(input("Enter the percentage: "))
#print (percentage)


if percentage < 0 or percentage > 100:
    print ("Please enter a number between 0 and 100 (inclusive)")

elif percentage < 40:
    print ("Fail")

elif percentage < 60:
    print ("Merit1")

elif percentage < 70:
    print ("Merit2")

else:
    print ("Distinction")