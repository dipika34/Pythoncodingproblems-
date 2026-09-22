def Cube(n):
    cube = 1
    for i in range(1,n+1):
        cube = i ** 3
        print(f"Current Number :{i} and the cube is {cube}")
n = int(input())
Cube(n)
