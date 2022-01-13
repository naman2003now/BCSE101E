dic = {}
amounts = {"p1":5,"p2":10,"p3":10,"p4":10,"p5":5,"p6":10}
amount = 0
while(True):
    a = input()
    if(a=='A' or a=='U'):
        b = input()
        li = b.split(",")
        li2 = li[0].split("(")
        li3 = li[1].split(")")
        product = li2[1]
        qty = li3[0]
        dic.update({product: qty})



    elif(a=='R'):
        b = input()
        li = b.split("(")
        li2 = li[1].split(")")
        product = li2[0]
        qty = dic[product]
        dic.pop(product)
    else:
        break

for key,value in dic.items():
    amount += (amounts[key])*int(value)

print("Items in cart: ",end="")
for key in dic.keys():
    print(key,end=" ")
print()
print(amount)