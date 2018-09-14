print('I will now count my chickens:')#若要使每一行输出之后都空一行，那么就要在最后的地方加上 \n .如下例子
print('I will now count my chickens:\n')

print('Hens',25+30/6)#若要进行数据的计算可以直接在print中 逗号之后运行
print('Roosters',100-25*3%4)
print('What is 3+2 ? ',3+2)
print('What is 5-7 ? ',5-7)
print(4+5+8)#这样也可以直接进行计算
print(3+2+1-5+4%2-1/4+6,'\n')

print('%.7f' %(3+2+1-5+4%2-1/4+6))    #在精确的控制输出数位当中，是不用加 逗号 的
##print('%.1f' , %(3+2+1-5+4%2-1/4+6))    #这就是有语法错误，因此在控制输出数位中，是不需要加上 逗号的

print('%.1f' %(6.75))

print('\n ',100+200 )#若要对上一行进行空行，就在前面加上'\n';
print(5+6,'\n')#若要对下一行进行空行，就在后面加上'\n';
print('\n',5+9,'\n')#这样就可以上下两行都空行

print('Now I will count the eggs:')
print(' Is it true that 3+2<5-7 ? ')
print("that's why it's False .")
print('How about some more . ')

print(3+2 < 5-7)#这样就可以直接进行逻辑运算，结果就是输出真假


print('Is it greater ?',5 > -2)
print('Is it greater or equal ?',5 >= -2)
print('Is it less or equal ?',5 <= -2)   #在print语句中的逗号之后，不但可以进行数值的计算，还可以进行逻辑语句的运算




