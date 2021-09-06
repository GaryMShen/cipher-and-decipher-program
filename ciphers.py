vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]


def arrayToString(array): #https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    str = " "

    for ele in array:
        str += ele
    return str

def pigLatin(text):
    detectedVowels = []
    head= []
    tail = []
    vowelDetected = False
    startsWithVowel = False
    lengthText = len(text)
    for i in range(lengthText):
        head.append(text[i])
        for x in range(len(vowels)):
            if text[i] == vowels[x]:
                if i == 0:
                    startsWithVowel = True
                detectedVowels.append(text[i])
    i = 0
    if startsWithVowel == False:
        while vowelDetected == False:
            if head[i] != detectedVowels[0]:
                tail.append(head[i])
                head.pop(i)
            else:
                vowelDetected = True
                
        strHead = (arrayToString(head))
        strTail = (arrayToString(tail))
        text = strHead + strTail + "ay"
    
    elif startsWithVowel == True:
        text = text + "yay"
    

    return text

def caesar(text, shift):
    
    text = text.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    puncuation = [" ", ".", "!", ",", "'", "(", ")", "@", "#", "$", "%", "^", "&", "*", ":"]
    newAlpha = []
    textArray = []
    newText = []
    x = 0

    for i in range(len(alphabet)):
        num = shift + i
        
        if num < 26:
            newAlpha.append(alphabet[num])
        if num >= 26:
            newAlpha.append(alphabet[x])
            x = x + 1
    
    for i in range(len(text)):
        textArray.append(text[i])
    
    for i in range(len(textArray)):
        holder = " "
        for x in range(len(alphabet)
        ):
            if textArray[i] == alphabet[x]:
                holder = x
        if holder == " ":
            newText.append(textArray[i])
        else:
            newText.append(newAlpha[holder])
        
        text = arrayToString(newText)
    return text



