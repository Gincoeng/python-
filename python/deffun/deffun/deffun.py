#example 1  函数的def语句由===》   函数名 括号 括号中的参数  冒号   】这四个东西构成
#尝试自己定义一个 绝对值函数
def my_abs(x):       #首先第一项就是自己要构造的函数的 定义语句
    if x>=0:         #然后在定义语句的冒号后的缩进块中  填写函数的主体内容。
        return x     #函数的返回值用return语句返回
    else:
        return -x

print(my_abs(-9))
print(my_abs(-18))
print(my_abs(10))




#example 2 空函数          
def nop():
    pass        #这个就是空函数    这是一个什么都不做的空函数
                #空函数的作用： 实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码运行起来。





#example 3   参数检查  如果我们输入的参数类型不对，python解释器是没有办法自动检查出来的。  可以利用example 1的函数 与 python内置的
#                      abs函数分别进行试验。     my_abs('abc') 以及 abs('abc')   这两者的错误提示信息是不一样的。
# 可以利用python内置的isinstance()函数进行改进，改进之后

def my_abs(x):
    if not isinstance(x,(int,float)):            #就是通过这两行进行 参数检查
        raise TypeError ('bad operand type')     # 利用python内置的 isinstance函数实现目的
    if x>=0:
        return x
    else :
        return -x      #这个就是引进 参数检查 的改进型函数。当传入错误的参数类型，函数就会抛出对应的错误提示。







#example 4  在函数中实现返回多个值。  例子：在游戏当中要从一个点移动到另外一个点， 给出坐标，位移，角度就可以计算出新的坐标
import math          # import math语句表示导入math包，并允许后续代码引用math包里的sin，cos等函数。
def new_position(x,y,step,angle=0):       #我觉得这里angle=0 的初始化动作，应该时指定这个角度的起始边 为水平直线。
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=new_position(100,100,60,math.pi/6)
print(x,y)                    ##

print('x=',x)                 ##
print('y=',y)                 ##注意这三个print之间的比较 

print('x=',x,'y=',y)          ##

print('x=','y=',x,y)          #这种表达就是错的。不好的。得不到理想的效果


#与上面对比的，求证 为啥angle=0  而step却不用初始化
import math
def move(x,y,step=0,angle=0):        #事实证明step是否初始化，结果都是一样的  ⭐⭐⭐重点   angle一定要初始化，否则报错。
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)

##看清返回值中的假象，     但其实python函数返回的仍然是单一值
import math
def new_position(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
r=new_position(100,100,60,math.pi/6)
print(r)              #原来返回值是一个tuple！但是，在语法上，返回一个tuple是可以省略括号的，而多个变量可以同时接收一个tuple，按位置
                      #赋值给对应的值。    因此，python中的返回多个值，其实就是返回一个tuple，但是写起来更加方便。



#练习
import math
def quadratic(a,b,c):
    #if not isinstance(a,b,c,(int,float)):
    #    raise TypeError ('bad operand type')
    delta=b*b-4*a*c
    if delta>=0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return x1,x2
    else:
        print('Wrong Number! The Equation can not solve!!!')
        

a=int(input('请输入a:'))
b=int(input('请输入b:'))
c=int(input('请输入c:'))
print(quadratic(a,b,c))