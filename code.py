def translator_RegistrationNumber(n):
    if not 0 <= n <= 255:
        print("Number should be <=255")
        return
    binaryNumber = str(bin(n))[2::]
    binaryNumber = "0"*(8 - len(binaryNumber)) + binaryNumber
    
    for i in range(8):
        if binaryNumber[i] == "1":
            print("anaconda"[i].upper(), end="")
        else:
            print("anaconda"[i].lower(), end="")
            
inputValue = input()
try:       
    translator_RegistrationNumber(int(inputValue))
except:
    for letter in inputValue:
        translator_RegistrationNumber(int(ord(letter)))
        print("", end=" ")