# Fun with numbers
# Built in functions with numbers
# rounds a number
# be careful of round, it rounds to the nearest even number
# eg 4.5 rounds to 4
# but 5.5 rounds to 6
# so do not use it accuracy is essential - como redondar um numero
# Author: Gabrila 

number_to_round = float(input("Enter a float number: "))
rounded_number = round (number_to_round)

print ( '{} round is {}' .format (number_to_round, rounded_number))