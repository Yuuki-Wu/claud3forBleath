import unittest
from Generate_topic import *
import re

filename = "Exercise.txt"
class MyTestCase(unittest.TestCase):
    def test_something1(self):
        filename = "Exercise.txt"
        test1 = num_topic(10,10,3)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('10.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('10.','10.')  # 通过测试
            else:
                pass#反之不通过
    def test_something2(self):
        filename = "Exercise.txt"
        test1 = num_topic(9,5,1)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('9.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('9.','9.')  # 通过测试
            else:
                pass#反之不通过
    def test_something3(self):
        filename = "Exercise.txt"
        test1 = num_topic(4, 8, 3)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('4.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('4.','4.')  # 通过测试
            else:
                pass#反之不通过
    def test_something4(self):
        filename = "Exercise.txt"
        test1 = num_topic(7, 5, 2)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('7.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('7.','7.')  # 通过测试
            else:
                pass#反之不通过
    def test_something5(self):
        filename = "Exercise.txt"
        test1 = num_topic(8, 4, 2)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('8.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('8.','8.')  # 通过测试
            else:
                pass#反之不通过
    def test_something6(self):
        filename = "Exercise.txt"
        test1 = num_topic(9, 9, 1)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('9.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('9.','9.')  # 通过测试
            else:
                pass#反之不通过
    def test_something7(self):
        filename = "Exercise.txt"
        test1 = num_topic(5, 4, 3)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('5.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('5.','5.')  # 通过测试
            else:
                pass#反之不通过
    def test_something8(self):
        filename = "Exercise.txt"
        test1 = num_topic(7, 4, 1)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('7.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('7.','7.')  # 通过测试
            else:
                pass#反之不通过
    def test_something9(self):
        filename = "Exercise.txt"
        test1 = num_topic(8, 4, 3)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('8.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('8.','8.')  # 通过测试
            else:
                pass#反之不通过
    def test_somethin10(self):
        filename = "Exercise.txt"
        test1 = num_topic(3, 5, 2)
        with open(filename, 'r') as x:
            line1 = []
            line1 = x.readlines()
            line2 = []
            line2.append(re.match('3.', line1[-1]).span())#匹配正则表达式，看line[]数组最后一项是否等于生成题号
            if (0, 3) in line2:#若line[]数组最后一项是否等于生成题号
                self.assertEqual('3.','3.')  # 通过测试
            else:
                pass#反之不通过

if __name__ == '__main__':
    unittest.main()
