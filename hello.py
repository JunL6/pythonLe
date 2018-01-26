classmates = ["Michael", "Bob", "Tracy"]
#print(classmates[-1])
#print(classmates)
classmates.insert(6, "Jack")
#print(classmates)
#print(classmates[3])
classmates[2] = "NOT_Tracy"
print(classmates)
print("\n")
classmates.append("Jeff")
#print()

tupl = ('Lebron', 'Wade', 'Jordan')
#tupl.pop()
#tuple 没有 pop()方法
#print(tupl)
z, q, j = tupl
print(z)
print(q)


ll = list(range(2,5))
#for x in ll:
#    print(x)
a, b, c = ll
print(a, b, c)

ss = set(['a','b', 'c'])
aa, bb, cc = ss
print(bb)
print(cc)
print(aa)

#@dict 用dict依次赋值 是否可行?
#可行，但是只会赋key值
dc = {'Michael':100, 'Sarah':90, 'James': 93}
ma, mb, mc = dc
print(ma)
print(mb)
print(dc[mc])

