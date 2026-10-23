temp = "night"
n = "10"
try:
    x = int(n)/int(temp)
except (ValueError,TypeError) as e:
    print("Error",e)
