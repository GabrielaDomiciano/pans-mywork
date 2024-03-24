# num1 = int(input("enter a number"))
# num2 = int(input("and another"))
# answer = num1 * num2

# print(f"anwer is {answer}")



# num1 = False
# while (num1 == False):
#    try:
#       num1 = int(input("enter a number"))
#  except ValueError:
#        print ("that is not a number ", end= "")

#num2 = False
#while (num2 == False):
#    try:
#        num2 = int(input("enter a number"))
#   except ValueError:
#       print ("that is not a number ", end= "")

#answer = num1 * num2
#print(f"anwer is {answer}")



def readNum(message = "enter a number:"):
    num = False
    while (not num):
        try:
            num  = int(input(message))
        except ValueError:
            print ("that was not a number ", end="")
    return num    

num1 = readNum()
num2 = readNum("enter num2:")

answer = num1 * num2

print(f"answer is {answer}")
