items = {}
givenItems = input().split(",")
givenAmounts = input().split(",")
givenStock = input().split(",")
amount = {}
stock = {}
for i in range(len(givenItems)):
    amount[givenItems[i]] = int(givenAmounts[i])
    stock[givenItems[i]] = int(givenStock[i])
    
while True:
    operation = input()
    if operation == "X":
        break
    if operation == "A":
        itemName, quantity = tuple(input().replace("(", "").replace(")", "").replace(" ", "").split(","))
        items[itemName] = str(int(items.get(itemName, 0)) + int(quantity))
    elif operation == "U":
        itemName, quantity = tuple(input().replace("(", "").replace(")", "").replace(" ", "").split(","))
        items[itemName] = quantity
    elif operation == "R":
        itemName= input().replace("(", "").replace(")", "")
        items.pop(itemName)


salesAmount = 0
cart = []
print("Item in the Cart: ", end="")
for key, value in items.items():
    if stock[key] >= int(value): 
        salesAmount += int(value)*amount[key]
    else:
        salesAmount += stock[key]*amount[key]
    cart.append(key)
    
print(*sorted(cart), sep=", ")
print(f"Sales amount : {salesAmount}")