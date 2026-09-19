def sequence(n):
    if n==0:
        return
    
    sequence(n-1)
    print(n)
n = int(input())       
print(sequence(n))
