#count the occurrences of
#each word in a given sentence
str=input("Enter a sentence: ")

str=str.split()


dict={}

for i in str:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1       
for j in dict:        
    print(j," = ",dict[j])
    



        
