a = (1,2,3,3)
b = 3,4,5,3
list = ["A", "B", 2]
c = tuple(list)
d = ()
e = (9)
print(f"a :{a} b : {b} c : {c} d : {d} e : {e} ")
#operations on tuple

s = c[0]
cnt = a.count(3)
print("cnt:",cnt)
idx = b.index(3)
print("index of 3 in b:",idx)
len(d)
#unpacked items
x, u, e = c
print(x,u,e)

print(f" index of 1 : { a.index(1)}")
print(f" count of 3s : {a.count(3)}")
"""
output:
a :(1, 2, 3, 3) b : (3, 4, 5, 3) c : ('A', 'B', 2) d : () e : 9 
cnt: 2
index of 3 in b: 0
A B 2
 index of 1 : 0
 count of 3s : 2
 """
