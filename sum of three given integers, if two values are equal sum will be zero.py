#Write a Python program to sum of three given integers.
#However, if two values are equal sum will be zero.
a=int(input("Enter A: "))
b=int(input("Enter B: "))
c=int(input("Enter C: "))
if a==b:
    print("(A=B)","Sum=0")
elif a==c:
    print("(A=C)","Sum=0")
elif b==c:
    print("(B=C)","Sum=0")
else:
    print("Sum =",a+b+c)


    
