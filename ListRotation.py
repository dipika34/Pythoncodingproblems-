elements = int(input())
nums = []
newList1 = []
newList2 = []
for i in range(elements):
  i = int(input())
  nums.append(i)
k = 2
for i in range(k,len(nums)):
  newList1.append(nums[i])

for i in range(0,len(nums)-k-1):
  newList2.append(nums[i])
print("Rotated List:",newList1+newList2)
