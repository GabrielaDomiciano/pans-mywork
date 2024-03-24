print (1,2,3, end="\t", sep="")
print("hi")


#unnamed arguments
def fun1(*args):
    print(type(args))
    for val in args:
        print(val)

fun1("a", "b", "c")

#keyword arguments
def fun2(**kwargs):
     print(type(kwargs))
     print (kwargs)
    #for val in args
       # print(val)
#fun2(name="Joe", age=21, gender="M")

#sample code
def ave(*values):
    number_of_values = len(values)
    sum= 0
    for value in values:
        sum+= value

    average = sum / number_of_values
    return average

print(ave(1,2,3,4,4,5,6))