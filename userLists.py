n = int(input("Enter the numbers:"))
lists = []
for  i in range(n):
    nums = int(input())
    lists.append(nums)

index1 = int(input("Enter the index 1:"))
index2 = int(input("Enter the index 2:"))

temp = lists[index1]
lists[index1] = lists[index2]
lists[index2] = temp
print(lists)
