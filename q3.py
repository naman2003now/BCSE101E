romanString = "IVXLCDMvxlcdm"

def getRoman(lengthOfNumber, positionOfNumber, number):
    global romanString
    subRoman = romanString[2*(lengthOfNumber - 1 - positionOfNumber):2*(lengthOfNumber - 1 - positionOfNumber)+3]
    if number == 0:
        return ""
    elif number < 4:
        return subRoman[0]*number
    elif number == 4:
        return subRoman[0] + subRoman[1]
    elif number == 5:
        return subRoman[1]
    elif number == 6:
        return subRoman[1] + subRoman[0]
    elif 9 > number > 6:
        return subRoman[1] + subRoman[0]*(number - 5)
    else:
        return subRoman[0] + subRoman[2]



DecimalNumber = int(input("Enter the number in decimal : "))

if DecimalNumber >= 4000 or DecimalNumber < 0:
    print("This is out of my range")

output = ""

for i in range(len(str(DecimalNumber))):
    output += getRoman(len(str(DecimalNumber)), i, int(str(DecimalNumber)[i]))
print(output)