
#Dict
# Defined by x = {}
# x = {"var1":"value1","var2":123, "var3":[],"var4":{}}
# add/ access values with square brackets
# x["var1"]="newValue"
#print(x["var1"])
#can have any variable typeas value, so we can have dicts in dicts
# x["var4"]["someKey"] = aValue
#Use the get function if you are not sure
# that the key exists
#Use the update function if want
# to add key using the format{}

car = {
    "make" : "ford",
    "model" : "modeo",
    "year" : 2006,
    "owner" : {
        "name" : "andrew",
        "driver-number" : 1123
        }
}

print(car["year"])





#attr = "year"
#print (car[attr])

#make2 = "fiat"