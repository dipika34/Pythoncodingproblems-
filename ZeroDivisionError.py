a="0"
try:
    x = int(a)
    t = 10/x
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print(x)
