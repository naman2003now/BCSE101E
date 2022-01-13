import pandas as pd

def grade(marks):
    if marks >= 90:
        return "A"
    if marks >= 80:
        return "B"
    if marks >= 60:
        return "C"
    else: 
        return "F"

print(pd.DataFrame({
    "Marks-1":list(map(grade, eval(input()))), 
    "Marks-2":list(map(grade, eval(input())))
    }, 
["Maths", "Eng", "Cs", "Phy", "Che", "Bio"]))