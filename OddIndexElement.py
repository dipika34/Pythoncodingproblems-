n = int(input())
#without using function
my_List = []
for i in range(n):
    i=int(input())
    my_List.append(i)
for i in range(len(my_List)):
    if(i%2!=0):
        print(my_List[i],end=" ")
