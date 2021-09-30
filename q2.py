l = 0
ml = 0

for i in range(int(input("number of cases"))):
    volume = list(map(int, input("the volume : ").split()))
    l += volume[0]
    ml += volume[1]

l += ml//1000
print(f"{l} l and {ml%1000} ml")

