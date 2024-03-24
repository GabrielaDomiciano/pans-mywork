def cube(number, power=3):
    print(number)
    return (number ** power) # elevado a 3
ans = cube(23)
print(f"We got {ans}")

num = 45

print(f"and {num} is {cube(num, 4)}")