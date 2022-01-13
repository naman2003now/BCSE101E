a = input().upper()*100
for x in range(5):
    y = x + 1
    print(*list(a[int((x*(x + 1))/2):int((y*(y + 1))/2)]))
    