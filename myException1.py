temp1= "20"
temp2="_20"
try:
    y = int(temp1)+temp2
except (ValueError,TypeError) as E:
    print("Error",E)
