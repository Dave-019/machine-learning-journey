a = 35

if (a%5 == 0 and a%10 == 0):
    print("divisible by both")
elif(a%5 == 0 or a%10 == 0):
    if a%5==0:
        print("divisible by 5 only")
    else:
        print("divisible by 10")
else:
    print("not divisible ")