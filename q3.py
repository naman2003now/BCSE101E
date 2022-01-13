from timeit import timeit

def anaconda(n):
    print(*list(map(lambda x: "anaconda"[x[0]]*(not bool(int(x[1]))) + "ANACONDA"[x[0]]*bool(int(x[1])), enumerate("0"*(8 - len(bin(n)[2::])) + bin(n)[2::]))), sep="")


print(timeit(lambda: anaconda(10), number=10000))

