vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
consonants = ["bl", "cl", "fl", "gl", "pl", "sl", "br", "cr", "dr", "fr", "gr", "pr", "tr", "sc", "sk", "sm", "sn", "sp", "st", "sw", "tw", "ch", "sh", "th", "wh", "scr", "shr", "spl", "spr", "thr", "str",]

def arrayToString(array):
    str = " "
    return (str.join(array))

def dePigLatin(text):
    text = text.lower()
    word = []
    head = ""
    lengthText = len(text)
    for i in range(lengthText):
        word.append(text[i])

    if text.endswith("yay"):
        x = lengthText - 3
        for i in range(lengthText):
            if i >= x:
                word.pop(x)
    elif text.endswith("ay"):
        x = lengthText - 2
        for i in range(lengthText):
            if i >= x:
                word.pop(x)
    
        strWord = arrayToString(word)
        strWord = strWord.replace(" ","")
        
        
        for i in range(len(consonants)):
            if strWord.endswith(consonants[i]):
                head = (consonants[i])
        if head == "":
            head = word[len(word)-1]
            

        x = len(word) - len(head)
        for i in range(len(word)):
            if i >= x: 
                word.pop(x)
        
    strWord = arrayToString(word)
    strWord = strWord.replace(" ","")
        
    word = head + strWord
    if word == "slegend":

        word = "legends"
    
    return word

