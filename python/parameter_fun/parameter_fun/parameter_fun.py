#####   位置参数

##example 1  
#def power(x):   #在这个函数当中，参数x就是一个位置参数
#    return x*x  #当调用这个函数的时候，必须传入有且仅有的一个参数X

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

####============================================================================================================================================================

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

#example 5     小学生入学注册的函数升级版
def enrolla(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enrolla('Ben','T')
enrolla('adam','M','Taibei')