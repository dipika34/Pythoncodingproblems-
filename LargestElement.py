n = int(input())
arr = []
for i in range(n):
  el = int(input())
  arr.append(el)
print(arr)
max = arr[0]
for i in arr:
  if (i>max):
    max = i
print(max)
    
