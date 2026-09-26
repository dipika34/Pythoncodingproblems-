length = int(input())
nums = []
even = []
odd = []
for i in range(length):
  i = int(input())
  nums.append(i)
for i in range(len(nums)):
  if (nums[i] % 2 == 0):
    even.append(nums[i])
  if (nums[i] % 2!=0):
    odd.append(nums[i])
temp = even + odd
print(f"Segragated Lists:{temp}")
