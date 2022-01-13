import numpy as np

fail=[]
def marks(lst):
    arr = np.array(lst, dtype =[("English","<i4"),("Maths","<i4"),("Physics","<i4"),("Chemistry","<i4"),("Commerce","<i4")])
    print(arr)
for i in range(0,5):
    marks(eval(input()))