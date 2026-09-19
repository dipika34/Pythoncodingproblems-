ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

ar1_set = set(ar1)
ar2_set = set(ar2)
ar3_set = set(ar3)

ar1_set.intersection_update(ar2_set,ar3_set)
ar1_list = list(ar1_set)
print(ar1_list)
