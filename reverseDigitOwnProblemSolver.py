n = 1234
reverse = 0
while(n>0):
    temp = n % 10
    reverse = temp + reverse*10
    n = n // 10

print(reverse)
