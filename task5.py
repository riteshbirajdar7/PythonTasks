a=int(input("Enter a number="))
b=int(input("Enter a number="))
c=int(input("Enter a number="))
print(a,b,c)
#following code checks whether all numbers are different or not
if (a==b) or (a==c) or( b==c):
    print("All numbers are not different")
    if(a==b):print("a and b are equal")
    if(c==b):print("c and b are equal")
    if(a==c):print("a and c are equal")
else:
    print("Some numbers are not same ")
#following code checks whether the first number is the largest or not
if (a>b) and (a>c):
    print(f"Yes, {a} is the largest")
else:
    print(f"{a} is not the largest")
#following code checks whether the numbers are strictly increasing or not 
if (a<b)and (b<c):
    print("Yes, the numbers are striclty increasing ")
else:
    print("The numbers are not strictly increasing")