num = int(input("The number: "))
i = 1
factorial = 1

while i<=num:
    factorial *=i
    i+=1
print("factorial of",num, "=",factorial)