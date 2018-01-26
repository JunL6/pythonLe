L = ("Michael", "Lebron", "Wade")
n = 0
#@break
#while n < 3:
#    print(L[n])
#    if L[n] == "Lebron":
#        break
#    n = n + 1
  
#@continue
#while n < 3:
#    if L[n] == "Lebron":
#        n = n + 1
#        continue
#    print(L[n])
#    n = n + 1

#@dict
#dict中的key能重复吗
names = {'Michael':95, 'Bob':75, 'Tracy':90, 'Michael':90, 'Tracy':80, "Michael": 92}
print(names['Michael'])
#不能重复，后面定义的会覆盖掉前面同名key的value

#@str不可变对象
a = "abc"
a = a.replace('a', 'A')
print(a)

#@dict
#默认返回none
d =  {'Michael':90, 'Bob':80, 'Tracy':95}
no = d.get('Adam')
print(no)
d.pop('Michael')
print(d)

#@set
s = set([1, 2, 3])
print(s)


#list.sort()
li = ['c', 'b', 'a']
li.sort();
print(li)

#str.replace()
st = 'abc'
print(st.replace('a', 'A'))
print(st)