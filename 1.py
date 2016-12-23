# %cd D:\Dropbox\Programming\Python\Python35\Learn
class MyMat:

    def __init__(self):
        pass

    def cli(x, y):
        import matplotlib.pyplot as plt
        # x = [1, 2, 3, 4]
        # y = [5, 4, 3, 2]
        plt.figure()
        plt.subplot(231)
        plt.plot(x, y)
        plt.subplot(232)
        plt.bar(x, y)
        plt.subplot(233)
        plt.barh(x, y)
        plt.subplot(234)
        plt.bar(x, y)
        y1 = [7, 8, 5, 3]
        plt.bar(x, y1, bottom=y, color='r')
        plt.subplot(235)
        plt.boxplot(x)
        # 绘制盒图
        plt.subplot(236)
        plt.scatter(x, y)
        plt.show()

if __name__ == "__main__":
    newMyMat = MyMat()
    MyMat.cli([1, 22, 33, 22], [33, 22, 33, 22])


def func(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
func(*args)

dict = {'a': 1, 'b': 2, 'c': 3}
func(**dict)

S = 'abcdefghijk'
for i in range(0, len(S), 2):
    print(S[i])

S = 'abcdefghijklmn'
for (index, char) in enumerate(S):
    print(index)
    print(char)

ta = [1, 2, 3]
tb = [9, 8, 7]
tc = ['a', 'b', 'c]
for (a, b, c) in zip(ta, tb, tc):
    print(c, b, a)

ta = [1, 2, 3]
tb = [9, 8, 7]
zipped = zip(ta, tb)
print(zipped)
na, nb = zip(*zipped)
print(na, nb)

f = open('main.txt')
f.next()
f.next()
f.next()
f.next()


def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000

for i in gen():
    print(i)


def gen():
    for i in range(4):
        yield

G = (x for x in range(4))

L = []
for x in range(10):
    L.append(x ** 2)
L

L = [x ** 2 for x in range(10)]
L


def func(a, b):
    return(a + b)


def test(f, a, b):
    print('test')
    print(f(a, b))

test(func, 3, 5)

test((lambda x, y: x + y), 77, 33)

from pprint import pprint
remotion = map((lambda x, y: x + y + 111),
               [22, 22, 33, 44], [33, 22, 444, 444])
pprint(list(remotion))


def func(a):
    if a > 100:
        return True
    else:
        return False

print(list((filter(func, [111, 2, 33, 11, 3344, 111, 22]))))

from functools import reduce
print(reduce((lambda x, y: x + y), [22, 33, 22, 22, 11]))


def test__fucn


def test_func():
    try:
        m = 1 / 0
    except NameError:
        print('Catch NameError in the sub-function')

# test_func()

try:
    test_func()
except ZeroDivisionError:
    print('Catch error in the main program of ZeroDivisionError')

print('lalala')
raise StopIteration
print('ddddd')

a = 5
b = a
a = a + 2
a

L1 = [1, 2, 3]
L2 = L1
L1[0] = 10
print(L2)

'''
immutable object
'''


def f(x):
    x = 100
    print(x)

a = 1
f(a)
print(a)

'''
mutable object
'''


def f(x):
    x[0] = 100
    print(x)

a = [1, 2, 3]
f(a)
print(a)

x1 = [1, 3, 5]
y1 = [9, 12, 13]
L = [x ** 2 for (x, y) in zip(x1, y1) if y > 0]

print(L)
'''
[1,9,25]
'''

'''
Python deepin 1
'''
'abc' + 'xyz'
'abc'.__add__('xyz')

len([1, 2, 3])
[1, 2, 3].__len__()

li = [1, 2, 3, 4, 56, 7, 8, 9]
print(li[3])

li = [1, 2, 34, 5, 6, 6, 7, 7, 8]
print(li.__getitem__(3))

'''
function is object __call__ equavalent add
'''


class SampleMore(object):

    def __call__(self, a):
        return a + 555

add = SampleMore()
print(add(2))
map(add, [2, 3, 4, 5])

'''
上下文管理器，第二段代码
'''
f = open("new,txt", "w")
print(f.closed)
f.write('Hello World!')
f.close()
print(f.closed)

with open('new.txt', 'w') as f:
    print(f.closed)
    f.write("Hello World!")
print(f.closed)


class VOW:

    def __init__(self, text):
        self.text = text
    '''此处自定义上下文管理器'''

    def __enter__(self):
        self.text = 'I say: ' + self.text
        return self

    '''此处自定义上下文管理器'''

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + '!'

with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)

'''
第一行为bird类的属性，比如feather。第二行为chicken类的属性，比如fly和__init__方法。第三行为summer对象的属性，也就是age。有一些属性，比如__doc__，并不是由我们定义的，而是由Python自动生成。此外，bird类也有父类，是object类(正如我们的bird定义，class bird(object))。这个object类是Python中所有类的父类。

可以看到，Python中的属性是分层定义的，比如这里分为object/bird/chicken/summer这四层。当我们需要调用某个属性的时候，Python会一层层向上遍历，直到找到那个属性。(某个属性可能出现再不同的层被重复定义，Python向上的过程中，会选取先遇到的那一个，也就是比较低层的属性定义)。

当我们有一个summer对象的时候，分别查询summer对象、chicken类、bird类以及object类的属性，就可以知道summer对象所有的__dict__，就可以找到通过对象summer可以调用和修改的所有属性了
'''


class bird(object):
    feather = True


class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age

summer = chicken(2)

print(bird.__dict__)
print('\n')
print(chicken.__dict__)
print('\n')
print(summer.__dict__)
print('\n')

summer.__dict__['age'] = 3
print(summer.__dict__['age'])

summer.age = 5
print(summer.age)

'''
peoperty
'''


class bird(object):
    feather = True


class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age

    def getAdult(self):
        if self.age > 1.0:
            return True
        else:
            return False
    adult = property(getAdult)   # property is built-in

summer = chicken(2)

print(summer.adult)
summer.age = 0.5
print(summer.adult)
'''
property 2
'''


class num(object):

    def __init__(self, value):
        self.value = value

    def getNeg(self):
        return -self.value

    def setNeg(self, value):
        self.value = -value

    def delNeg(self):
        print('value also deleted')
        del self.value
    neg = property(getNeg, setNeg, delNeg, "I'm negative")

x = num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(num.neg.__doc__)
del x.neg

'''
使用特殊方法__getattr__

我们可以用__getattr__(self, name)来查询即时生成的属性。当我们查询一个属性时，如果通过__dict__方法无法找到该属性，那么Python会调用对象的__getattr__方法，来即时生成该属性。比如:
'''


class bird(object):
    feather = True


class chicken(bird):
    fly = False

    def __init__(self, age):
        self.age = age

    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)

summer = chicken(2)
# True
print(summer.adult)
summer.age = 0.5
# False
print(summer.adult)
# AtrributeError(male)
print(summer.male)

'''
Try and Guess
'''

print((1.8).__mul__(2.0))
print(True.__or__(False))
print((-1).__abs__())
print((2.3).__int__())
print(li.__setitem__(3, 0))
print({'a': 1, 'b': 2}.__delitem__('a'))


def line_conf():
    def line(x):
        return 2 * x + 1
    print(line(5))
line_conf()
print(line(5))


def line_conf(a, b):
    def line(x):
        return a * x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(4))

'''装饰函数和方法'''


def square_sum(a, b):
    return a ** 2 + b ** 2


def square_diff(a, b):
    return a ** 2 - b ** 2

print(square_sum(3, 4))
print(square_diff(3, 22))


def square_sum(a, b):
    print("input: ", a, b)
    return a ** 2 + b ** 2


def square_diff(a, b):
    print("input ", a, b)
    return a ** 2 - b ** 2

print(square_sum(3, 22))
print(square_diff(33, 22))

'''
我们修改了函数的定义，为函数增加了功能。

现在，我们使用装饰器来实现上述修改：
'''


def decorator(F):
    def new_F(a, b):
        print("input: ", a, b)
        return F(a, b)
    return new_F


@decorator
def square_sum(a, b):
    return a ** 2 + b ** 2


def square_diff(a, b):
    return a ** 2 - b ** 2

print(square_sum(222, 222))
print(square_diff(3343, 22))


def decorator(F):
    def new_F(a, b):
        print("input :", a, b)
        return F(a, b)
    return new_F


@decorator
def square_sum(a, b):
    return a ** 2 + b ** 2


@decorator
def square_diff(a, b):
    return a ** 2 - b ** 2

print(square_sum(22, 22))
print(square_diff(33, 22))
'''
装饰器可以用def的形式定义，如上面代码中的decorator。装饰器接收一个可调用对象作为输入参数，并返回一个新的可调用对象。装饰器新建了一个可调用对象，也就是上面的new_F。new_F中，我们增加了打印的功能，并通过调用F(a, b)来实现原有函数的功能。
就相当于：
square_sum = decorator(square_sum)
print(square_sum(3, 4))
'''


def decorator(pre=''):
    def subDecorator(F):
        def new_F(a, b):
            print(pre + " input :", a, b)
            return F(a, b)
        return new_F
    return subDecorator


@decorator('^_^')
def square_sum(a, b):
    return a ** 2 + b ** 2


@decorator('^_^')
def square_diff(a, b):
    return a ** 2 - b ** 2

print(square_sum(22, 22))
print(square_diff(33, 22))


def decorator(aClass):
    class newClass:

        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aClass(age)

        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()
    return newClass


@decorator
class Bird:

    def __init__(self, age):
        self.age = age

    def display(self):
        print("My age is ", self.age)

eagleLord = Bird(5)
for i in range(3):
    eagleLord.display()
'''
在decorator中，我们返回了一个新类newClass。在新类中，我们记录了原来类生成的对象（self.wrapped），并附加了新的属性total_display，用于记录调用display的次数。我们也同时更改了display方法。

通过修改，我们的Bird类可以显示调用display的次数了。

装饰器的核心作用是name binding。这种语法是Python多编程范式的又一个体现。大部分Python用户都不怎么需要定义装饰器，但有可能会使用装饰器。鉴于装饰器在Python项目中的广泛使用，了解这一语法是非常有益的。
'''

'''
1、通过闭包对一个数据 x 做“流水线操作”，至少三层闭包，每一层依次进行一项操作，（如先求绝对值，再开方，再求相反数）。
'''


def xiangfan(x):
    def kaifang(x):
        def juedui(x):
            return abs(x)
        return juedui(x) ** 0.5
    return -kaifang(x)

print(xiangfan(-4))

'''
装饰器实现
'''


def juedui(x):
    return abs(x)


def kaifang(F):
    def new_F(x):
        return F(x) ** 0.5
    return new_F


def xingfan(F):
    def new_F(x):
        return -F(x)
    return new_F

func = xingfan(kaifang(juedui))

print(func(-555))

'''
Python补充

len(s)         返回： 序列中包含元素的个数
min(s)         返回： 序列中最小的元素
max(s)         返回： 序列中最大的元素
all(s)         返回： True, 如果所有元素都为True的话
any(s)         返回： True, 如果任一元素为True的话

sum(s)         返回：序列中所有元素的和
# x为元素值，i为下标(元素在序列中的位置)

s.count(x)     返回： x在s中出现的次数
s.index(x)     返回： x在s中第一次出现的下标

# l为一个表, l2为另一个表

l.extend(l2)        在表l的末尾添加表l2的所有元素
l.append(x)         在l的末尾附加x元素
l.sort()            对l中的元素排序
l.reverse()         将l中的元素逆序
l.pop()             返回：表l的最后一个元素，并在表l中删除该元素
del l[i]            删除该元素

#str为一个字符串，sub为str的一个子字符串。s为一个序列，它的元素都是字符串。width为一个整数，用于说明新生成字符串的宽度。

str.count(sub)       返回：sub在str中出现的次数
str.find(sub)        返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1

str.index(sub)       返回：从左开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误

str.rfind(sub)       返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，返回 -1

str.rindex(sub)      返回：从右开始，查找sub在str中第一次出现的位置。如果str中不包含sub，举出错误


str.isalnum()        返回：True， 如果所有的字符都是字母或数字
str.isalpha()        返回：True，如果所有的字符都是字母
str.isdigit()        返回：True，如果所有的字符都是数字
str.istitle()        返回：True，如果所有的词的首字母都是大写
str.isspace()        返回：True，如果所有的字符都是空格
str.islower()        返回：True，如果所有的字符都是小写字母
str.isupper()        返回：True，如果所有的字符都是大写字母

str.split([sep, [max]])    返回：从左开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.split(',')的方式使用逗号或者其它分割符

str.rsplit([sep, [max]])   返回：从右开始，以空格为分割符(separator)，将str分割为多个子字符串，总共分割max次。将所得的子字符串放在一个表中返回。可以str.rsplit(',')的方式使用逗号或者其它分割符

str.join(s)                返回：将s中的元素，以str为分割符，合并成为一个字符串。

str.strip([sub])           返回：去掉字符串开头和结尾的空格。也可以提供参数sub，去掉位于字符串开头和结尾的sub

str.replace(sub, new_sub)  返回：用一个新的字符串new_sub替换str中的sub
str.capitalize()           返回：将str第一个字母大写
str.lower()                返回：将str全部字母改为小写
str.upper()                返回：将str全部字母改为大写
str.swapcase()             返回：将str大写字母改为小写，小写改为大写
str.title()                返回：将str的每个词(以空格分隔)的首字母大写

str.center(width)          返回：长度为width的字符串，将原字符串放入该字符串中心，其它空余位置为空格。

str.ljust(width)           返回：长度为width的字符串，将原字符串左对齐放入该字符串，其它空余位置为空格。

str.rjust(width)           返回：长度为width的字符串，将原字符串右对齐放入该字符串，其它空余位置为空格。
'''

import sys
print(sys.path)


'''
三、Python内置函数清单

Python内置(built-in)函数随着python解释器的运行而创建。在Python的程序中，你可以随时调用这些函数，不需要定义。最常见的内置函数是:

print("Hello World!")
在Python教程中，我们已经提到下面一些内置函数:

type() dir() help() len() len() open() range() enumerate() zip() iter() map() filter() reduce()

下面我采取的都是实际的参数，你可以直接在命令行尝试效果。

1、数学运算

abs(-5)                          # 取绝对值，也就是5
round(2.6)                       # 四舍五入取整，也就是3.0
pow(2, 3)                        # 相当于2**3，如果是pow(2, 3, 5)，相当于2**3 % 5
cmp(2.3, 3.2)                    # 比较两个数的大小
divmod(9,2)                      # 返回除法结果和余数
max([1,5,2,9])                   # 求最大值
min([9,2,-4,2])                  # 求最小值
sum([2,-1,9,12])                 # 求和
2、类型转换

int("5")                         # 转换为整数 integer
float(2)                         # 转换为浮点数 float
long("23")                       # 转换为长整数 long integer
str(2.3)                         # 转换为字符串 string
complex(3, 9)                    # 返回复数 3 + 9i

ord("A")                         # "A"字符对应的数值
chr(65)                          # 数值65对应的字符
unichr(65)                       # 数值65对应的unicode字符

bool(0)                          # 转换为相应的真假值，在Python中，0相当于False .在Python中，下列对象都相当于False：** [], (), {}, 0, None, 0.0, '' **

bin(56)                          # 返回一个字符串，表示56的二进制数
hex(56)                          # 返回一个字符串，表示56的十六进制数
oct(56)                          # 返回一个字符串，表示56的八进制数

list((1,2,3))                    # 转换为表 list
tuple([2,3,4])                   # 转换为定值表 tuple
slice(5,2,-1)                    # 构建下标对象 slice
dict(a=1,b="hello",c=[1,2,3])    # 构建词典 dictionary
3、序列操作

all([True, 1, "hello!"])         # 是否所有的元素都相当于True值
any(["", 0, False, [], None])    # 是否有任意一个元素相当于True值

sorted([1,5,3])                  # 返回正序的序列，也就是[1,3,5]
reversed([1,5,3])                # 返回反序的序列，也就是[3,5,1]
4、类、对象、属性

# define class
class Me(object):
    def test(self):
        print "Hello!"

def new_test():
    print "New Hello!"

me = Me()
hasattr(me, "test")               # 检查me对象是否有test属性
getattr(me, "test")               # 返回test属性
setattr(me, "test", new_test)     # 将test属性设置为new_test
delattr(me, "test")               # 删除test属性
isinstance(me, Me)                # me对象是否为Me类生成的对象 (一个instance)
issubclass(Me, object)            # Me类是否为object类的子类
5、编译、执行

repr(me)                          # 返回对象的字符串表达
compile("print('Hello')",'test.py','exec')       # 编译字符串成为code对象
eval("1 + 1")                     # 解释字符串表达式。参数也可以是compile()返回的code对象
exec("print('Hello')")            # 解释并执行字符串，print('Hello')。参数也可以是compile()返回的code对象
6、其他

input("Please input:")            # 等待输入

globals()                         # 返回全局命名空间，比如全局变量名，全局函数名
locals()                          # 返回局部命名空间
'''
import re
m = re.search('[0-9]', 'abcddedf232ddf119')
print(m.group(0))

import re
m = re.findall('[0-9]', 'adfadfdsf239237dfddf')
print(m)
import re
m = re.sub('[0-9]', 'd44', 'adfadfdsf239237dfddf')
print(m)

import re
m = re.split('[0-9]', 'adfadfdsf239237dfddf')
print(m)

import re
m = re.match('[0-9]', 'adfadfdsf239237dfddf')
print(m)

'''
time包
'''
import time
print(time.time())
print(time.clock())

import time
import time

import time
print('start')
time.sleep(10)
print('wake up')

st = time.gmtime()
print(st)
st = time.localtime()
print(st)
s = time.mktime(st)
print(s)

import datetime
t = datetime.datetime(2012, 9, 2, 21, 31)
print(t)

import datetime
t = datetime.datetime(2012, 9, 3, 21, 30)
t_next = datetime.datetime(2012, 9, 5, 23, 30)
delta1 = datetime.timedelta(seconds=600)
delta2 = datetime.timedelta(weeks=3)
print(t + delta1)
print(t + delta2)
print(t_next - t)

import datetime
t = datetime.datetime(2016, 8, 2, 12, 11)
delta1 = datetime.timedelta(seconds=600, weeks=4)
print(t + delta1)

print(t + delta1.strftime())

import os.path
path = '/hoame/vamei/doc/file.txt'

print(os.path.basename(path))
print(os.path.dirname(path))
info = os.path.split(path)
print(info)
path2 = os.path.join('/', 'home', 'vamei', 'doc', 'finel1.txt')
print(path2)

p_list = [path, path2]
'''查询多个路径的共同部分'''
print(os.path.commonprefix(p_list))

os.path.normpath(path)

import os.path
path = '/home/vamei/doc/file.txt'
print(os.path.exists(path))
print(os.path.getsize(path))
print(os.path.getatime(path))
print(os.path.getmtime(path))
print(os.path.isfile(path))
print(os.path.isdir(path))

import glob
print(glob.glob('/home/vamei/*'))

import os
os.mkdir('c:\ddd')
os.mkdir('c:\ddd\ddd')

import shutil
shutil.copy('4.jpg', '5.jpg')

from datetime import datetime
format = "output-%Y-%m-%d-%H%M%S.txt"
str = "output-1997-12-23-030000.txt"
t = datetime.strptime(str, format)
print(t)

from datetime import datetime
format = "output_%Y.%m.%d.%w.txt"
str = "output_1981.10.21.txt"
myWeek = t.strftime("%W")
# print(myWeek)
# print(str[:len(str)-4])
newT = str[:len(str) - 4] + '.' + myWeek + '.txt'
print(newT)

'''math包'''
import math
print(math.e)
print(math.pi)
print(math.ceil(123))
print(math.floor(123))
print(math.pow(123, 12))
print(math.log(123))
print(math.sqrt(123))

'''random package'''
import random

random.seed(x)
random.choice([11, 22, 33, 33])
random.sample([111, 33, 22, 11], 3)
random.shaffle([11, 22, 33, 11])

import random
print(random.random())
print(random.random(11, 22))

'''
假设我们有一群人参加舞蹈比赛，为了公平起见，我们要随机排列他们的出场顺序。我们下面利用random包实现：
'''
import random
all_people = ['Tom', 'vivian', 'Paul', 'Liya', 'Manu', 'Deniel', 'Shawn']
random.shuffle(all_people)
for i, name in enumerate(all_people):
    print(i, ':' + name)

'''创建sqllite数据库'''
import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute('''CREATE TABLE category
(id int primary key,sort int,name text)''')
c.execute('''CREATE TABLE book
(id int primary key,
sort int,
name text,
price real,
category int,
FOREIGN KEY (category) REFERENCES category(id))''')

conn.commit()
conn.close()

'''插入sqlite数据库'''

import sqlite3

conn = sqlite3.connect("test.db")
c = conn.cursor()
books = [(1, 1, 'Cook Recipe', 3.12, 1),
         (2, 3, 'Python Intro', 17.5, 2),
         (3, 2, 'OS Intro', 13.6, 2),
         ]

c.execute("INSERT INTO category VALUES(1,1,'kitchen')")

c.executemany('INSERT INTO book VALUES(?,?,?,?,?)', books)

conn.commit()
conn.close()

'''查询sqlite数据库'''
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())
print(c.fetchone())

c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

for row in c.execute('SELECT name,price FROM book ORDER BY sort'):
    print(row)

'''删除sqlite数据库'''
import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('UPDATE book SET price=? WHERE id=?', (1000, 1))
c.execute('DELETE FROM book WHERE id=2')

conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()


c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())

c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

for raw in c.execute('SELECT name,price FROM book ORDER BY sort'):
    print(raw)

c.execute('DROP TABLE book')

'''relanch'''
import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())

c.execute('''CREATE TABLE book
(id int primary key,
sort int,
name text,
price real,
category int,
FOREIGN KEY (category) REFERENCES category(id))''')
conn.commit()

c.execute('SELECT * FROM book WHERE book.category=1')
print(c.fetchall())

for raw in c.execute('SELECT * FROM book'):
    print(raw)

import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()

c.execute('SELECT name FROM category ORDER BY sort')
print(c.fetchone())

# c.execute('''CREATE TABLE book
# (id int primary key,
# fort int,
# name text,
# price real,
# category int,
# FOREIGN KEY(category) REFERENCES category(id))'''
# )

for raw in c.execute('SELECT * FROM book'):
    print(raw)

'''TCP socket
在互联网上，我们可以让某台计算机作为服务器。服务器开放自己的端口，被动等待其他计算机连接。当其他计算机作为客户，主动使用socket连接到服务器的时候，服务器就开始为客户提供服务。

在Python中，我们使用标准库中的socket包来进行底层的socket编程。

首先是服务器端，我们使用bind()方法来赋予socket以固定的地址和端口，并使用listen()方法来被动的监听该端口。当有客户尝试用connect()方法连接的时候，服务器使用accept()接受连接，从而建立一个连接的socket：
'''
import socket

HOST = ''
PORT = 8000

reply = 'Hello World'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(3)

conn, addr = s.accept()

request = conn.recv(1024)

print('request is ', request)
print('Connected by ', addr)

conn.sendall(reply)
conn.close()

'''HTTP服务器端'''
import socket

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
text_content = '''HTTP/1.x 200 OK
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg', 'rb')
pic_content = '''
HTTP/1.x 200 OK
Content-Type: image/jpg

'''
pic_content = pic_content + f.read()
f.close()

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src = request.split(' ')[1]

    # deal with GET method
    if method == 'GET':
        # ULR
        if src == '/4.jpg':
            content = pic_content
        else:
            content = text_content

        print ('Connected by'), addr
        print ('Request is:'), request
        conn.sendall(content)
    # close connection
    conn.close()
