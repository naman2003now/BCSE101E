sideLengths = list(map(int, input().split()))

s = sum(sideLengths)/2

areaSquared = s
for element in sideLengths:
    areaSquared *= s - element

print(f"Area = {areaSquared**(1/2)}")