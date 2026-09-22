sentence = "Hello"
count1 = 0
count2 = 0
char =  "aeiou"
vowels = 0
consonant = 0

for i in sentence.lower():
    if i in char:
        count1+=1
        vowels = count1
    else:
        count2+=1
        consonant=count2
print("VOwels",vowels)
print("Consonant",consonant)
