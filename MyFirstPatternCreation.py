n=int(input())
for i in range(n+1):
  for j in range(1,n-i+1):
    print(n-i-j+1,end="")
  print()

#output
5
54321
4321
321
21
1
