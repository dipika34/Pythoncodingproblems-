y = int(input())
list1 = []
new_list = []
current_sum = 0
for i in range(y):
  i = int(input())
  list1.append(i)
print(f"Original List:{list1}")

for i in range(y):
  current_sum+=list1[i]
  new_list.append(current_sum)
print(f"New List:{new_list}")

  

  
