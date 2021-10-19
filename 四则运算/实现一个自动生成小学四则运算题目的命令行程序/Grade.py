from fractions import Fraction
import sys

def Check(filename1='Exercise.txt',filename2='Answer.txt',filename3='Grade.txt'):
    """filename1.txt与filename2.txt相比较，得出正确数"""
    num=0
    with open(filename1) as file01:
        for line in file01:
            num=num+1
# print(num)
# 计算一共有几行
    with open(filename1,'r') as x ,open(filename2,'r') as y:
        line1=[]
        line2=[]
        line1=x.readlines()
        line2=y.readlines()
        c = 0
        w = 0
        correct_topic =[]
        wrong_topic = []
        for i in range(num):#for循环遍历
            if line1[i]==line2[i]:
                c += 1
                correct_topic.append(str(i+1))
            else:
                w += 1
                var=str(i+1)
                wrong_topic.append(str(i+1))
        temp = sys.stdout #标准输出管道
        file = open(filename3,'w')#将标准输出管道连到打开的文件
        sys.stdout = file
        print("Correct: ", str(c), '(', end='')
        print(*correct_topic, sep=',', end='')
        print(')')
        print("Wrong: ", str(w), '(', end='')
        print(*wrong_topic, sep=',', end='')
        print(')')
        sys.stdout.close()#关闭管道，所以，使用print 输出的数据，本来是存放在管道中，close()之后，全部写入文件中
        sys.stdout = temp

    return filename1,filename2