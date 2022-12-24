'''
sum of n number using for loop
'''
n=int(input("Enter N: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum: ",sum)

'''
asume the sum is zero
if the given number is 5.
loop will run 1 to 5.
so when i = 1 , sum=sum+i , sum=0+1 , sum = 1
   when i = 2 , sum=sum+i , sum=1+2 , sum = 3
   when i = 3 , sum=sum+i , sum=3+3 , sum = 6
   when i = 4 , sum=sum+i , sum=6+4 , sum = 10
   when i = 5 , sum=sum+i , sum=10+5 , sum = 15

if the given number is 5. output will be 15.
1+2+3+4+5=15

if the given number is 10. output will be 55.
1+2+3+4+5+6+7+8+9+10=55

'''
                
