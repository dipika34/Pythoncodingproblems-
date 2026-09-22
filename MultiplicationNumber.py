def multiplication(n):
    product = 1
    print(f"Multiplication of a number {n} is")
    for i in range(1,10+1):
        product = i*n
        print(f"{n}*{i} = {product}")
n = int(input())
multiplication(n)
