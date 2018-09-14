#example 1
d = {'michael':95,'bob':75,'tracy':85}
print(d['michael'])
print(d)

d['adam']=67
print(d['adam'])    #除了在初始化指定外，可以通过 这样的方式进行赋值,即还可以增加dict里面的元素
print(d)

d['adam']=100
print(d['adam'])   #一个key对应一个value，所以对一个key进行多次的放入value后，就会把前面的值覆盖。key会对应最新被放入的value
print(d)

####### d1['adam']=67
####### print(d1['adam'])   #进行这样的key放入value时，首要条件是这个dict是存在的， 若dict不存在，就不能进行这样的赋值


print('tomas' in d)   #这个语句能够检测该元素是否存在于一个dict中    存在就是true  不存在就是false

print(d.get('tomas'))  #这个语句同样是检测给元素是否存在于一个dict中    存在就会返回对应的值   不存在就会返回none
print(d.get('tomas',-1))    # 指定不存在时，返回的值为-1   不是none
print(d.get('adam'))


d1={'haha':77,'wawa':55,'kaka':99,'gaga':66}
print(d1)
d1.pop('wawa')   #要删除一个key，可以使用 dict的名字 + . + pop （‘要弹出的key的名字’）。那么对应的key包括对应的value就会在dict中被删除
print(d1)

#print(d1.pop('wawa'))  #这个指令是 输出要删除的key的对应的value  。不过执行完之后，对应的key和value都被删除了
#print(d1)



#example 2  set
s=set([1,2,3])   #在set中，传入的参数是一个list
print(s)

s1=set([1,1,2,2,3,3])    #在set中，重复的元素会自动地被过滤
print(s1)

s.add(4)   #往set中添加元素可以使用 set的名字 + . +（key）的方法。要注意的是：可以重复添加，但是不会有效果；每次只可以添加一个key。
print(s)
s1.add(5) #假如想一次添加多个key   像  s1.add（5，6，7，8，9）。这个时候就会报错
print(s1)

s.remove(2)   #若想删除 set 中的key，可以通过 set的名字 + . +（key）的方法。  这样就可以删除set中的key
print(s)
s1.remove(1)
print(s1)  


#example 3    set可以看成数学当中的无序和无重复元素的集合，因此，两个set可以做数学意义上的交，并集等操作
sa = set([1,2,3])
sb = set([2,3,4])
print(sa&sb)  #交运算
print(sa|sb)  #并运算


#举一反三  用str放入list再传入set

j = set(['haha','wawa','gaga','kaka'])
print(j)
j.add('lala')
print(j)
j.remove('gaga')
print(j)


#example 4 
a=['c','b','a']
print(a)
a.sort()  #sort函数  就是代表对 list进行原址排序。 对于tuple，不可用。因为tuple是不可变的
print(a)

#example 5     要明白 字符串 ，数字这些就是不变对象
a='abc'               #以下这两行，最好在jupyter上运行一次
a.replace('a','A')    #因为这一行，已经有改变。但是当你重新 print（a）时，又变回原形。。。  下面给出原因、


a='abc'
b=a.replace('a','A')
print(a)
print(b)
