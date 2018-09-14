##example 1
#print('=====这是一个把输入的数字转换为其绝对值的程序=====')
#absolute=int(input('请输入你想转换的实数:'))
#print(abs(absolute))                  # abs函数，是返回所输入的值的绝对值

#################################更多的python函数，可以查看已经收藏在 Chrome浏览器中的书签。

##wxample 2
#a=max(1,2,3,4,5,6,7,8,9,99,88,-7,-3)  # max函数，可以接收多个参数并返回其中的最大值
#print(a)

##example 3
#q=int('123')
#print(q)

#w=int(12.34)
#print(w)

#e=float('12.34')
#print(e)

#r=str(1.23)
#print(r)
#print(1.23==r)     #这一行以及下面那一行都是用来验证的。因为输出的时候，即使转化成了str类型，但是没有加上单引号，所以看上去很难区分
#print(1.23==1.23)  #所以就用这个判断的方法来验证，通过这个验证过可知， r已经不是1.23了，已经变成字符串类型

#t=str(100)
#print(t)
#print('\n')   #这是空行

#y=bool(1)
#print(y)
#i=bool(99)
#print(i)

#u=bool('')
#print(u)
#o=bool(0)
#print(o)

##example 4 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个别名
#g=abs  #变量g指向abs函数
#cc=g(-9)
#print(cc)
#print(g(-7))

#practice 1
print('=====这是一个将数字转化成对应的十六进制的程序=====')
a=100     #控制循环的次数
while a>0:
    shuru=int(input('请输入你想转换的数字：'))
    print(hex(shuru))
    a=a-1
print('END')

