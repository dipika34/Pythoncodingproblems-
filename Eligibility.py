def Set(p):
    if p<90:
        raise ValueError("Need 75% attendance")
    print("Eligible for vote",p)
try:
    Set(30)
except ValueError as E:
    print(E)
