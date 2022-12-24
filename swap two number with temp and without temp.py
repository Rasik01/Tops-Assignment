# swap two number with temp variable

a=int(input("Enter A: "))
b=int(input("Enter B: "))
temp=a
a=b
b=temp
print("A: ",a)
print("B: ",b)


#without temp variable
a=int(input("Enter A: "))
b=int(input("Enter B: "))

a,b=b,a
print("A: ",a)
print("B: ",b)
      
