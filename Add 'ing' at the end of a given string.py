#Add 'ing' at the end of a given string
#If the given string already ends with 'ing' then add 'ly' instead.
#If the string length of the given string is less than 3, leave it unchanged
s=input("Enter String: ")

if len(s)>2:
    if s[-3:]=='ing':
        s=s+'ly'
    else:
        s=s+'ing'
print(s)        
        
    
