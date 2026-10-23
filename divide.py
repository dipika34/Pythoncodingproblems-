def divide(n):
    try:
        temp=n/0
    except ZeroDivisionError:
        print("Can't be divided by zero")
divide(43)
