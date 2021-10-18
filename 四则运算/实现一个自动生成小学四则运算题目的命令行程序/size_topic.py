import numpy as np
import random
import json
from fractions import Fraction
from List import  *
from File import *
filename1 = 'Exercise.txt'
filename2 = 'Answer.txt'

def one_size_topic(r,times):
    """单运算符号"""
    if r < 0:
        print("请输入自然数")
    elif r > 10:
        print("请输入小于零的自然数")
        """限定r范围，防止小学生不会计算"""
    q = 0#q为生成题目计数量，每生成一题q+1
    while q < times:
        Operation_symbol = ['+', '-', '*', '÷']
        t = random.randint(0, 3)#random.randint()方法，随机生成一定范围的整数
        n1 = random.randint(0, r)
        n2 = random.randint(0, r)
        result = 0
        first = Operation_symbol[t]
        if t == 0:  # 加法
            result = n1 + n2
            print(n1, first, n2, '=')
            q+=1
        elif t == 1:  # 减法
            n1, n2 = max(n1, n2), min(n1, n2)#防止结果出现负数,用max(),min()使n1>n2
            result = n1 - n2
            print(n1, first, n2, '=')
            q+=1
        elif t == 2:  # 乘法
            result = n1 * n2
            print(n1, first, n2, '=')
            q+=1
        elif t == 3:  # 除法
            if n2 != 0: #除数不能为零，否则出现异常
                result = n1 / n2
                print(n1, first, n2, '=')
                q+=1
                if result % 1 == 0:#若能整除1，则直接取整数部分
                    result = int(result)
                elif result < 1:
                    result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                else:
                    result = getTrueFractionBig(result)
        Exercises_writer(filename1, q,n1, first, n2)#调用File.py里的函数将题目保存为txt
        Answers_writer(filename2, q, n1, first, n2, result)#调用File.py里的函数将题目以及答案保存为txt
    return  r,times


def double_size_topic(r,times):
    """双运算符号"""
    q = 0
    if r < 0:
        print("请输入自然数")
    while q < times:
        Operation_symbol = ['+', '-', '*', '÷']
        t = []
        num = np.random.randint(4, size=2)
        t = list(num)#对数组升序排序
        t1 = getNonRepeatList1(t)
        n1 = random.randint(0, r)
        n2 = random.randint(0, r)
        n3 = random.randint(0, r)
        result = 0
        if len(t1) > 1:#将数组经筛选后长度大于1的再次筛选，保证生成题目数量为输入值
            first = Operation_symbol[t1[0]]
            second = Operation_symbol[t1[1]]
            if t == [0, 1]:  # 加减法组合
                n4 = n1 + n2
                n4, n3 = max(n4, n3), min(n4, n3)
                result = (n1 + n2) - n3
                print('(', n1, first, n2, ')', second, n3, '=')
                q+=1
            elif t == [0, 2]:  # 加乘法组合
                result = (n1 + n2) * n3
                print('(', n1, first, n2, ')', second, n3, '=')
                q+=1
            elif t == [0, 3]:  # 加除法组合
                if n3 != 0:
                    result = (n1 + n2) / n3
                    print('(', n1, first, n2, ')', second, n3, '=')
                    q+=1
                    if result % 1 == 0:#若能整除1，则直接取整数部分
                        result = int(result)
                    elif result < 1:
                        result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                    else:
                        result = getTrueFractionBig(result)#实现大于1的小数化成真分数
            elif t == [1, 2]:  # 减乘法组合
                n1, n2 = max(n1, n2), min(n1, n2)#防止结果出现负数,用max(),min()使n1>n2
                result = (n1 - n2) * n3
                print('(', n1, first, n2, ')', second, n3, '=')
                q+=1
            elif t == [1, 3]:  # 减除法组合
                if n3 != 0:  # 除数不能为零
                    n1, n2 = max(n1, n2), min(n1, n2)#防止结果出现负数,用max(),min()使n1>n2
                    result = (n1 - n2) / n3
                    print('(', n1, first, n2, ')', second, n3, '=')
                    q+=1
                    if result % 1 == 0:
                        result = int(result)
                    elif result < 1:
                        result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                    else:
                        result = getTrueFractionBig(result)

            elif t == [2, 3]:  # 乘除法组合
                if n3 != 0:  # 除数不能为零
                    result = (n1 * n2) / n3
                    print('(', n1, first, n2, ')', second, n3, '=')
                    q+=1
                    if result % 1 == 0:#若能整除1,则直接取整数部分
                        result = int(result)
                    elif result < 1:
                        result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                    else:
                        result = getTrueFractionBig(result)     #实现大于1的小数化成真分数
            Exercises_writer1(filename1,q,n1,first,n2,second,n3)#调用File.py里的函数保存题目
            Answers_writer1(filename2,q,n1,first,n2,second,n3,result)#调用File.py里的函数保存题目和答案
    return r,times

def triple_size_topic(r,times):
    """三运算符号"""
    q=0
    if r < 0:
        print("请输入自然数")
    while q < times:
        Operation_symbol = ['+', '-', '*', '÷']
        t = []
        num = np.random.randint(4, size=3)
        t = list(num)#对列表升序排序，并去重
        t1 = getNonRepeatList1(t)
        n1 = random.randint(0, r)
        n2 = random.randint(0, r)
        n3 = random.randint(0, r)
        n4 = random.randint(0, r)
        result = 0
        if len(t1) > 2:#将去重排序后长度数组大于2的筛选出来，保证题目数与输入数一致
            first = Operation_symbol[t1[0]]
            second = Operation_symbol[t1[1]]
            third = Operation_symbol[t1[2]]
            n5 = n1 + n2
            n5, n3 = max(n5, n3), min(n5, n3) #防止结果出现负数,用max(),min()使n1+n2>n3
            if t1 == [0, 1, 2]:  # 加减乘组合
                result = (n5 - n3) * n4
                print('(', n5, first, n2, second, n3, ')', third, n4, '=')
                q += 1
                if result % 1 == 0:#若能整除1,则直接取整数部分
                    result = int(result)
                elif result < 1:
                    result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                else:
                    result = getTrueFractionBig(result)     #实现大于1的小数化成真分数
                Exercises_writer2(filename1, q, n1, first, n2, second, n3, third, n4)
                Answers_writer2(filename2, q, n1, first, n2, second, n3, third, n4, result)
            elif t1 == [0, 1, 3] :  # 加减除组合
                if n4 != 0:#除数不能为零，防止异常出现
                    result = (n5 - n3) / n4
                    print('(', n1, first, n2, second, n3, ')', third, n4, '=')
                    q += 1
                    if result % 1 == 0:#若能整除1，则直接取整数部分
                        result = int(result)
                    elif result < 1:
                        result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                    else:
                        result = getTrueFractionBig(result)     #实现大于1的小数化成真分数
                    Exercises_writer2(filename1, q, n1, first, n2, second, n3, third, n4)
                    Answers_writer2(filename2, q, n1, first, n2, second, n3, third, n4, result)


            elif t1 == [0, 2, 3] :#加乘除组合
                if n4 != 0:#除数不能为零,防止出现异常
                    result = (n1 + n2) * n3 / n4
                    print('(', n1, first, n2, ')', second, n3, third, n4, '=')
                    q += 1
                    if result % 1 == 0:#若能整除1,则取整数部分
                        result = int(result)
                    elif result < 1:
                        result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                    else:
                        result = getTrueFractionBig(result)  # 实现大于1的小数化成真分数
                    Exercises_writer3(filename1, q, n1, first, n2, second, n3, third, n4)
                    Answers_writer3(filename2, q, n1, first, n2, second, n3, third, n4, result)

            elif t1 == [1, 2, 3] :  # 减乘除组合
                if n4 != 0:#除数不能为零，防止出现异常
                    n1, n2 = max(n1, n2), min(n1, n2)
                    result = (n1 - n2) * n3 / n4
                    print('(', n1, first, n2, ')', second, n3, third, n4, '=')
                    q += 1
                    if result % 1 == 0:#若能整除1,则取整数部分
                        result = int(result)
                    elif result < 1:
                        result = getTrueFractionSmall(result)  # 实现小于1的小数化成真分数
                    else:
                        result = getTrueFractionBig(result)     #实现大于1的小数化成真分数
                    Exercises_writer3(filename1, q, n1, first, n2, second, n3, third, n4)
                    Answers_writer3(filename2, q, n1, first, n2, second, n3, third, n4, result)

    return r,times