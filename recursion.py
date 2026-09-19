def sequence(n):
    if n==0:
        return
    print(n)
    sequence(n-1)
n = int(input())       
print(sequence(n))
