inputStringOne = input().replace(" ", "").split("+")
inputStringTwo = input().replace(" ", "").split("+")

intListOne = [0, 0]
intListTwo = [0, 0]

for element in inputStringOne:
    if element[-1] in ["j", "i"]:
        intListOne[1] += int(element[:-1])
    else:
        intListOne[0] += int(element)

for element in inputStringTwo:
    if element[-1] in ["j", "i"]:
        intListTwo[1] += int(element[:-1])
    else:
        intListTwo[0] += int(element)

print(f"Real part is {intListOne[0] + intListTwo[0]}")
print(f"Imaginary part is {intListOne[1] + intListTwo[1]}")