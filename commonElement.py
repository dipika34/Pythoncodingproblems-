ar1 = [1,5,5]
ar2 = [3,4,5,5,10]
ar3 = [5,5,10,20]

ar1_set = set(ar1)
ar2_set = set(ar2)
ar3_set = set(ar3)

ar1_set.intersection_update(ar2_set,ar3_set)
ar1_list = list(ar1_set)
print(ar1_list)
