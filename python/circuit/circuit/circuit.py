#example 1
names=['michael','bob','tracy\n']
for name in names:            #for...in....循环语句；in后面加上的是list或者tuple的名字。for后面加上的是你称呼list或者tuple里面元素的名称
    print(name)

names=['michael','bob','tracy']
for mingzi in names:                   #所以这一个与上面打印出来的东西是完全一样的e
    print(mingzi)

#example 2
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
    print(sum)

sum = 0
l=[1,2,3,4,5,6,7,8,9,10,11]
for x in l:                           #这两个例子是一样的
    sum = sum + x
    print(sum)


#example 3
y1=list(range(1001))  #这里面有两种函数 第一个是range()函数，range函数是能够生成一整个数列就像是在matlab中的（0：1：X）这个range函数是从0开始的，所以要注意一下。这个range（）函数就是生成 0到x-1的
print(y1)             #list()函数是把上面的range函数生成的数字序列转化成一个 list   。所以这是一个list函数  与我们普通定义的list不同
                     #就是函数都是用（） ，而list在定义时是使用  [ ]

y2=list(range(5))
print(y2)           #这个就是生成0 1 2 3 4

#example 4

sum1 = 0
for y in range(1001):
    sum1 = sum1 + y
    print(sum1)

                                #这两个的写法都可以的，只要in的后面跟着一个序列
sum2 = 0
for y in list(range(1001)):
    sum2 = sum2 + y
    print(sum2)
                                #这三个写法都是可以，把它变成一个tuple
sum3 = 0
for y in tuple(range(1001)):
    sum3 = sum3 + y
    print(sum3)

#example 5 
sum4 = 0
n = 100
while n>0:
    sum4 = sum4 +n
    n=n-1
    print(sum4)          #这个就是输出有1到100的所有整数相加之和

#练习
hah = ['bart','lisa','adam']
for yuansu in hah:
    print(yuansu)
    print('Hello,',yuansu)
    print('Hello,',yuansu,'!')
   ### #print('Hello,%s!',%yuansu)  #这个格式化输出存在着一定的问题，有待解决

mingzi=input('请输入您的名字：')
print('Hello,',mingzi,'!')

#example 5
n1=1
while n1<=100:
    print(n1)
    n1=n1+1
print('END')

   # 这个就是break语句
n2=1
while n2<=100:
    if n2==11:     #这里判断的时候，当n等于11时，就退出
        break     #这个break就是结束当前循环的
    print(n2)
    n2=n2+1
print('END')

   #这个就是continue语句
n3=0
while n3<10:
    n3=n3+1
    if n3%2 ==0:
        continue
    print(n3)
print('END')