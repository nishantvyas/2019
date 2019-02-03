"""
fun with list
"""

#define the empty list
define_list = []
print(type(define_list))
other_way_define_list = list()
print(type(other_way_define_list))

for x in range(20):
    if x % 2 == 0:
        define_list.append(x)

print(define_list)

other_way_define_list = [x for x in range(20) if x % 2 == 0]

print(other_way_define_list)

alist = [1,2,3]
print(alist)
blist = alist
clist = alist[:]
alist.append(5)
print(alist)
print(blist)
print(clist)
