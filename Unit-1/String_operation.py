string1=input("Enter your String=>")
find=input("Enter your Charctor=>")
replace=input("Enter your Replace=>")
rev=""
count=0
vowel=0
new_str=""
for char in range(len(string1)-1,-1,-1):
    if string1[char]== "a" or string1[char]== "e" or string1[char]== "i" or string1[char]== "o" or string1[char]== "u" or string1[char]== "A" or string1[char]== "E" or string1[char]== "I" or string1[char]== "O" or string1[char]== "U":
        vowel+=1
    count+=1
    if(string1[char]==find):
        new_str+=replace
    else:
        new_str+=string1[char]
    
print("Vowel:",vowel)
print("count",count)  
print("Revesrse:",rev)
print("New String",new_str)
if(rev==string1):
    print("Palindrom")
else:
    print("Not Palindrom")


    

