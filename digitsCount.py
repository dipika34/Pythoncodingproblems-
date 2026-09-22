n = int(input())
temp = 0
count = 0
digit_count = 0
while(n > 0):
    temp = n % 10
    count+=1
    n = n // 10
digit_count = count
print(digit_count)

