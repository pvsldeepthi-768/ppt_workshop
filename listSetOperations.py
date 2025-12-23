list1=list(input("first list:").split(","))
list2=list(input("second list:").split(","))
print(list1)
print(list2)
common=list(set(list1) & set(list2))
print(common)
count={}
for x in common:
    count[x]=list2.count(x)
print(count)
union=list(set(list1)|set(list2))
print(union)
symmetric=list(set(union)-set(common))
print(symmetric)
"""
first list:1,2,3,4,5,6,7,8
second list:1,2,7,45,34,23,4,67
['1', '2', '3', '4', '5', '6', '7', '8']
['1', '2', '7', '45', '34', '23', '4', '67']
['1', '7', '4', '2']
{'1': 1, '7': 1, '4': 1, '2': 1}
['1', '34', '8', '5', '6', '4', '2', '23', '45', '3', '7', '67']
['34', '8', '5', '6', '23', '45', '3', '67']
"""
