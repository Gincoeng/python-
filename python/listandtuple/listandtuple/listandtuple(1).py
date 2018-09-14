classmates=['Michael','Bob','Tracy']   #python内置的数据类型是列表，list是一种有序的集合，可以随时 添加 和 删除 其中的元素
print(classmates)                #变量classmates就是一个list，

a=len(classmates)        #使用len函数就可以获得list元素的个数
print('列表的长度为；',a)

print(classmates[0])   #使用索引就可以来访问list中的每一个位置的元素，⭐索引是从0开始的
print(classmates[1])   
print(classmates[2])   #如果要取最后一个元素，除了计算索引位置外，还可以用 -1 做索引，直接获取最后一个元素。。以此类推可以获取倒数第2，3，...个。

classmates.append('adam')
print(classmates)            #在list中追加元素的方法是  list名称 +   .append (' ')

classmates.insert(1,'jacky')
print(classmates)            #在list中插入到指定的位置，比如索引号为1的位置   list名称 +  .insert( 索引号，‘   ’)

classmates.pop()
print(classmates)       #要删除list末尾的元素的方法是   list名称 +   .pop（） 

classmates.pop(1)
print(classmates)       #要删除指定位置的元素的方法是    list名称 +  .pop(索引号)

classmates[1]='sarah'
print(classmates)       #要把某个元素替换成别的元素，就是直接给对应的索引位置赋值

L=['apple',123,True]     # list里面的元素的数据类型可以不同，可以同时存在字符串 整型 布尔
print(L)

S=['python','java','scheme',['asp','php']]   #在列表里面能够 嵌套另外一个list    但是这个数组只有4个元素
print(S)

H=[ ]
G=len(H)
print(G)  # 一个空的list，长度为0

#============================================================================================================
classmates=('Michael','Bob','Tracy')
print(classmates)   #这个就是元组tuple  跟list十分类似，但是tuple一旦初始化就不能修改

# tuple不能添加、插入、删除元素，只能访问tuple里面的各个元素   正正是因为tuple的不可变，所以代码更加安全，能用tuple就尽量不要用list
# tuple在定义的时候就要确定其中的元素，

t=( )
print(t)  #这就是定义一个空的tuple

y=(1)
print(y)  # 这种情况之下定义的不是tuple，而是1这个数，因为（）既可以表示tuple也可以表示公式中的小括号 要区别

yy=(1,)   # 这个就是定义的tuple       =====》就是只有一个元素的的tuple定义时，一定要加上一个逗号
print(yy)


#貌似可变的tuple，表明了 tuple的不变的tuple中的元素指向不变，假若指向一个list则这个list里面的元素就可以改变
w=('a','b',['A','B'])
print(w)
w[2][0]='x'
w[2][1]='Y'
print(w)

#练习题
U=[['Apple','Google','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
print(U[0][0])
print(U[1][1])
print(U[2][2])
print(U[1][1],U[1][1],U[2][2])