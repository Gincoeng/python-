##print absolute value of an integer
a = 100
if a >= 0:
    print(a)
else:
        print(-a)

a=int(input('your age：'))        #这里的int（）函数，就是把 输入的数据 进行强制字符转换
if a >= 18 :                   #因为你输入的是一个字符串。所以一定要进行强制字符转换，这个很重要啊，
    print('you have the permission')
else:
    print('haha')


#直接使用print函数
print('n=123')
print('f=456.789')
print("s1='Hello, World'")
print("s2='Hello,\\'Adam\\''")#若是这样的话，是不能完全输出的，会缺失 \ \     ===>其实 \ 是转义字符。能够在单引号，双引号同时存在的情况下，使用转义字符输出。在要输出的符号前面加上 \ 即可

print("s3=r'Hello,", '"Bart" '"'") #利用在第一个练习 输入输出 中，采用 逗号 的方法 串连一个输出即可。 一个逗号就是一个空格，不加逗号就是没有加上空格。这一行我只加了一个逗号
print('s3=r\'Hello,\"Bart\"\'')
print("r'''Hello,")
print('Lisa!',"'''")


##另一种方法
n=123
f=456.789
s1="'Hello World'"
print('n=',n)
print('f=',f)
print('s1=',s1)

print('''huang
jian
chang
\n
\n''')     #使用 '''    ''' 这个符号就是可以把内容分成多行输出


print(r'''haung
jian
chang\n''')          #加上r之后就会 取消转义字符的

a ='ABC'
b=a
a='XYZ'
print(b)
print(a)