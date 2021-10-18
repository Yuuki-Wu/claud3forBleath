from fractions import Fraction
def getNonRepeatList1(data):
    """数组去重升序排序"""
    return list(set(data))
def getTrueFractionBig(num):
    """获取大于一的真分数"""
    t = 0
    while num > 0:
        if num > 1:
            num -= 1
            t += 1
        else:
            num = Fraction(num).limit_denominator(1000000000000000000000)#将小数化成分数
            break

    return str(t) + "'" + str(num)
def getTrueFractionSmall(num):
    """获取小于一的真分数"""
    while True:
        num = Fraction(num).limit_denominator(100000000)
        break
    return str(num)


