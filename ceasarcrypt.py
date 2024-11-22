import random

def encrypt(word):

    outText = []
    cryptText = []
    
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    integers = ['1','2','3','4','5','6','7','8','9','0']
    special = ['!', '@', '#', '$', '%', '^', '&', '*']

    step = random.randrange(1,9)

    for eachLetter in word:
        if eachLetter in uppercase:
            index = uppercase.index(eachLetter)

            crypting = (index + step) % 26
            cryptText.append(crypting)


            new_letter = uppercase[crypting]
            outText.append(new_letter)
    
        elif eachLetter in lowercase:
            index = lowercase.index(eachLetter)

            crypting = (index + step) % 26
            cryptText.append(crypting)


            new_letter = lowercase[crypting]
            outText.append(new_letter)
            
        elif eachLetter in integers:
            index = integers.index(eachLetter)

            crypting = (index + step) % 10

            cryptText.append(crypting)


            new_letter = integers[crypting]
            outText.append(new_letter)

        elif eachLetter in special:
            index = special.index(eachLetter)

            crypting = (index + step) % 8

            cryptText.append(crypting)


            new_letter = special[crypting]
            outText.append(new_letter)

    return "".join(outText)

def encryptlistofwords(str1):

    lst = str1.split()
    temp = []

    for word in lst:

        temp.append(encrypt(word))

    return " ".join(temp)
    

word = input(str("input: "))
print(encryptlistofwords(word))
