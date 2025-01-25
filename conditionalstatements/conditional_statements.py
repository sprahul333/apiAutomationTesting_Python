greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition is True")
else:
    print("Condition is False")

a=40-30+20

if a==30:
    print(a)
    print("Condition is True")

else:
    print("Condition is False")

#Nested If-Else

a=30

if a>20:
    print("a is greater than 20")
    if a>25:
        print("a is greater than 25")
    else:
        print("a is less than 25")
elif a>10 and a<20:
    print("a is less than 20")

else:
    print("a is less than 10")