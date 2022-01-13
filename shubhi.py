from timeit import timeit

def anaconda(n):
    print(*list(map(lambda x: "anaconda"[x["index"]]*(not x["number"]) + "ANACONDA"[x["index"]]*x["number"], [{"number": bool(int(x)), "index":i} for i, x in enumerate("0"*(8 - len(bin(n)[2::])) + bin(n)[2::])])), sep="")


print(timeit(lambda: anaconda(10), number=10000))