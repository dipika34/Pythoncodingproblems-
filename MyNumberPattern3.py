n = int(input("How many numbers?"))
for  i in range(n+1):
    for j  in range(1,n-i+1):
        print(j,end="")
    print()
    
