from ciphers import *
from deciphers import *

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break

def checkMode(text):
    while True:
        userInput = str((input(text)))
        if userInput == "cipher":
            return userInput
            break
        elif userInput == "decipher":
            return userInput
            break
        else:
            print("please enter cipher or decipher")
            continue

def checkCipher(text):
    while True:
        userInput = str((input(text)))
        if userInput == "Pig Latin":
            return userInput
            break
        if userInput == "caesar":
            return userInput
            break
        else:
            print("please enter a valid cipher")
            continue

def checkDeCipher(text):
    while True:
        userInput = str((input(text)))
        if userInput == "Pig Latin":
            return userInput
            break
        if userInput == "caesar":
            return userInput
            break
        if userInput == "no":
            return userInput
            break
        else:
            print("please enter a valid cipher or no if you don't know what cipher was used")
            continue

def cipher(text):
    cipherType = checkCipher("Enter the type of cipher: ")
    if cipherType == "Pig Latin":
        words = text.split()
        sentance = ""
        for i in range(len(words)):
            word = pigLatin(words[i])
            sentance = sentance + " " + word
    elif cipherType == "caesar":
        shift = inputNumber("enter the size of the shift: ")
        sentance = caesar(text, shift)


    return sentance

def decipher(text):
    deCipherType = checkDeCipher("Do you know the type of cipher?: ")
    if deCipherType == "Pig Latin":
            words = text.split()
            sentance = ""
            for i in range(len(words)):
                word = dePigLatin(words[i])
                sentance = sentance + " " + word
    if deCipherType == "caesar":
        sentance = ""
        for i in range(26):
            print(" ")
            print("shift of " + str(i + 1) + " : " + caesar(text, i + 1) )
    return sentance