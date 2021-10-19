def Exercises_writer(filename1,q,n1,first,n2):
    """实现x+y类似的式子，并输出式子为filename1.txt"""
    with open(filename1, 'a') as Exercises:
        Exercises.write(str(q) + '.' + str(n1) + str(first) + str(n2) + '=' + '\n')

def Answers_writer(filename2,q,n1,first,n2,result):
    """实现x+y类似的式子，并输出式子及答案为filename2.txt"""
    with open(filename2, 'a') as Answers:
        Answers.write(str(q) + '.' + str(n1) + str(first) + str(n2) + '=' + str(result) + '\n')

def Exercises_writer1(filename1,q,n1,first,n2,second,n3):
    """实现(x+y)*p类似的式子，并输出式子为filename1.txt"""
    with open(filename1, 'a') as Exercises:
        Exercises.write(str(q) + '.' + '(' + str(n1) + str(first) + str(n2) +')' + str(second) + str(n3) + '=' + '\n')

def Answers_writer1(filename2,q,n1,first,n2,second,n3,result):
    """实现(x+y)*p类似的式子，并输出式子及答案为filename2.txt"""
    with open(filename2, 'a') as Answers:
        Answers.write(str(q) + '.' + '(' + str(n1) + str(first) + str(n2) +')' + str(second) + str(n3) + '=' + str(result) + '\n')

def Exercises_writer2(filename1,q,n1,first,n2,second,n3,third,n4):
    """实现(x+y+z)*p类似的式子，并输出式子为filename1.txt"""
    with open(filename1, 'a') as Exercises:
        Exercises.write(str(q) + '.' + '(' + str(n1) + str(first) + str(n2) + str(second) + str(n3) + ')' + str(third) + str(n4) + '=' + '\n')

def Answers_writer2(filename2,q,n1,first,n2,second,n3,third,n4,result):
    """实现(x+y+z)*p类似的式子，并输出式子及答案为filename2.txt"""
    with open(filename2, 'a') as Answers:
        Answers.write(str(q) + '.' + '(' + str(n1) + str(first) + str(n2) + str(second) + str(n3) + ')' + str(third) + str(n4) + '=' + str(result) + '\n')

def Exercises_writer3(filename1,q,n1,first,n2,second,n3,third,n4):
    """实现(x+y)+z*p类似的式子，并输出式子为filename1.txt"""
    with open(filename1, 'a') as Exercises:
        Exercises.write(str(q) + '.' + '(' + str(n1) + str(first) + str(n2) + ')' + str(second) + str(n3) + str(third) + str(n4) + '=' + '\n')

def Answers_writer3(filename2,q,n1,first,n2,second,n3,third,n4,result):
    """实现(x+y)+z*p类似的式子，并输出式子及答案为filename2.txt"""
    with open(filename2, 'a') as Answers:
        Answers.write(str(q) + '.' + '(' + str(n1) + str(first) + str(n2) + ')' + str(second) + str(n3) + str(third) + str(n4) + '=' + str(result) + '\n')




