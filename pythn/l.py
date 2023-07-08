age=20
if age>=18:
    print("You are old enough to vote!")
    not_teen= not age>=13 and age<=19
    print(not_teen)
while age<18:
    print("You are too young to vote!")
    age+=1
    print(age)
    not_teen= not age>=13 and age<=19
    print(not_teen)   