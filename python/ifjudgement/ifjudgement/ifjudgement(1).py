#example 1
age=20
if age>=18:
    print('your age is', age,'you\'re an adult\n')  #学会使用之前的 转义字符\ 这样就不需要单双引号之间来回切换，
#    print('adult')

#example 2
age=3
if age >= 18:
    print('your age is :',age)
    print('you\'re an adult\n')
else:
        print('your age is :',age)
        print('you\'re a teenager\n')

#enhancement
age = int(input('what\'s your age:'))  #这里要 强制加上 字符转换，因为input是字符型，要加上int（）。才能把输入的类型转换为整型数据
if age >= 18:                          #因为age是字符串 不能够 直接与整型数据比较   要进行强制转换,,所以这里就不需要给18加上引号了
    print('your age is :',age)                                                                           
    print('you\'re an adult\n')
else:
        print('your age is :',age)
        print('you\'re a teenager\n')

#对比
age = int(input( ))             #这里要 强制加上 字符转换，因为input是字符型，要加上int（）。才能把输入的类型转换为整型数据
if age >= 18:                      #因为age是字符串 不能够 直接与整型数据比较   要进行强制转换,,所以这里就不需要给18加上引号了
    print('your age is :',age)
    print('you\'re an adult\n')
else:
        print('your age is :',age)
        print('you\'re a teenager\n')

#example 3
age = 3
if age >= 18:
    print('adult')
elif age >= 6:          #elif这就是 else if的缩写  ，在python中能够直接用 elif 代替
    print('teenager')
else:
    print('kid')


# example 4 
s=input('birth year:')
birth=int(s)
if birth<2000:
    print('00前')
else:
    print('00后')


#练习
tall=float(input('请输入您的身高：'))  #这里输入就不能用int（）函数了，因为输入的是浮点数，所以要改写成为float（）。才可以
weight=float(input('请出入您的体重：'))
BMI=(weight/(tall*tall))
print('your BMI is :',BMI)
if BMI<18.5:
    print('过轻')
elif 18.5<BMI<25:
    print('正常')
elif 25<BMI<32:
    print('肥胖')
else :                                 #最后的判断不需要加上这个 BMI>32   因为剩下的就是最后一种情况了，所以else后面什么条件都不用加，只需要加上 ：即可
    print('严重肥胖')


