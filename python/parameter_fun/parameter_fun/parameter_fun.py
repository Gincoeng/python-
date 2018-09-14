#####   位置参数

##example 1  
#def power(x):   #在这个函数当中，参数x就是一个位置参数
#    return x*x  #当调用这个函数的时候，必须传入有且仅有的一个参数x

#print(power(15))    #这个就是简单地调用这个函数

##example 2  举一反三
#def high_power( ):#这个函数就是可以在自己执行之后，再输入所想输入的数字。不用像第一种方法那样直接在程序中赋值，而不能在调试的时候再赋值
#    a=int(input('请输入你想平方的数值：'))
#    print(power(a))

#high_power( )   #这行代码就是调用所定义的这个函数


##example 2   当我们想求x的3，4，5，6，.....次方的时候，我们难道要定义无穷多个用来求次方的函数吗？ 我们能不能输入参数的时候多输入一个 参数呢？
#def power1(x,n):
#    s=1
#    while n>0:
#        n=n-1
#        s=s*x
#    return s
#print(power1(5,3))

#####============================================================================================================================================================

####   默认参数

##example 3   当我们在计算次方的时候，经常计算的是平方，其他次方用得少，但又不是不用。  所以这个时候就要用到 默认参数
#def power2(x,n=2):   #这里就是设置默认参数为2，就是当我们不输入指数的时候，默认计算 该输入数目的平方；
#    s=1              #
#    while n>0:       #
#        n=n-1        #函数的主体不发生改变，只是在定义函数的时候，加入默认参数
#        s=s*x        #
#    return s         #
#print(power2(3)) #所以在调用这个函数的时候，只输入一个参数，就是默认计算该数的平方
#print(power2(3,7)) #调用这个函数，同时输入该数字，以及其指数的时候，就会计算相对应的数值。

##example 4    小学生入学注册的函数
#def enroll(name,gender):
#    print('name:',name)
#    print('gender:',gender)

#enroll('sarah','F') 

##example 5     小学生入学注册的函数升级版
#def enrolla(name,gender,age=6,city='Beijing'):
#    print('name:',name)
#    print('gender:',gender)
#    print('age:',age)
#    print('city:',city)

#enrolla('Ben','T')
#enrolla('adam','M',city='Taibei')  #像这里中间跳了一项的话，不能直接写城市的名字，要在参数的前面加上参数名称；不然的话，就会按顺序来，地方名变了年龄的参数。

#example 6    使用默认参数不当就会掉进自己挖的坑。
def add_end(L=[ ]):
    L.append('END')
    return(L)

print(add_end([1,2,3]))   #正常调用参数时，没有出错
print(add_end(['x','y','z']))  #正常调用的时候都不会出错的

print(add_end( ))         #第一次调用 默认参数的时候  
print(add_end( ))         #第二次调用的时候就应该开始出错  ，出现了上一次调用默认参数时候的结果。第二次调用的时候结果就变成了两次调用的叠加
print(add_end( ))         #第三次也是一样的，会叠加第二次出现的结果，再输出
##################
#  原因就是：python函数在定义的时候，默认参数L的值就被计算出来了，即[ ]，因为默认参数L也是一个变量，它指向对象[ ]，每次调用该函数的时候，如果改变了L的内容
#            则下次调用的时候，默认参数的内容就变了。不再是函数定义时的[ ]了。
##################

#example 7     如何防止掉入自己默认参数使用不当的这个大坑     其实主要是当出现默认参数是  空  的时候，这个坑。
def add_end(L=None):
    if L==None:
        L = [ ]
    L.append('END')
    return L

print(add_end( ))   #
print(add_end( ))   # 在编写函数的时候，如果默认参数是空；  最好是要加上一行改进的。就是检测到是空的时候，强制令其等于空。 这样在之后几次的空的时候调用
print(add_end( ))   # 才不会叠加空参数的调用结果。
print(add_end( ))   #