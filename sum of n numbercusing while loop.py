#sum of n using while, loop run in incerment order of 1 to n
n=int(input("Enter Number: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum:= ",sum)


'''
we can also write code without creating i variable
loop run in decrement order of n to 1
sum=0
while n>0:
    sum=sum+n
    n=n-1
print("Sum:= ",sum)
'''
