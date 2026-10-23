lists=[1,2,3]
try:
    lists[3]=4
except IndexError:
    print("Index out of Error")
