n = "10"
try:
    temp = n/0
except ValueError as v:
    print("Error",v)
except:
    print("Error found")
