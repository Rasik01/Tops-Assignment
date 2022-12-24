#Factorial number of given number
n=int(input("Enter A Number: "))
fact=1
for i in range(1,n+1):

    fact=fact*i
print("Factorial number of given number is: ",fact)    
