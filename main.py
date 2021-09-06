from cipherToolFunctions import *

if __name__ == "__main__":  
    while True:  
        text = str(input("Enter text: "))
        mode = checkMode("Would you like to cipher or decipher this text?: ")
        if mode == "cipher":
            newText = cipher(text)
        elif mode == "decipher":
            newText = decipher(text)
        print(newText)
         