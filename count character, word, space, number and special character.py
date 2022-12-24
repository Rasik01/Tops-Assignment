#count character, word, space, number and special character
str=input("Enter String: ")
ch=0
w=1
sp=0
n=0
spch=0
for i in str:
    if i.isalpha():
        ch=ch+1
    elif i.isspace():
        sp=sp+1
        w=w+1
    elif i.isnumeric():
        n=n+1
    else:
        spch=spch+1
print("Total Character:",ch)
print("Total Word:",w)
print("Total Space:",sp)
print("Total Numeric:",n)
print("Total Special Character:",spch)
        
    
    
    
