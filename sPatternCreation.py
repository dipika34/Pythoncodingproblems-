n = 5
for i in range(n):
  for j in range(1,i+1):
    print("*",end="")
  print()

for i in range(n):
  for j in range(1,n-i+1):
    print("*",end="")
  print()
  
