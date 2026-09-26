num  = int(input())
lists = []
for i in range(num):
  i = int(input())
  lists.append(i)
print(lists)
temp = set(lists)
print(list(temp))
