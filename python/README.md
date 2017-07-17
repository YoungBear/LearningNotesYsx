# python learn
感谢[廖雪峰的Python教程](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)

## python3 
version 3.5.0

交互式环境 or 文本编辑器

直接运行.py文件，需要在文件开头添加python3的路径的注释：(不同机器可能路径不同，可以使用which python3来查看)

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
```

## 数据类型
- 整数
- 浮点数
- 字符串
- 布尔值 True False，运算：and or not
- 空值 None
- 变量 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量

Tips：

两种除法：

`/`除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数;

`//`地板除，两个整数的除法仍然是整数。

## 编码

`ord()`获取字符的整数表示

`chr()`函数把编码转换为对应的字符

Python对bytes类型的数据用带`b`前缀的单引号或双引号表示：

将bytes转换为字符串:`decode()`

`len()`:返回字符串的字符长度或者字节的长度。
当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
```

## 列表 list

list是一种有序的集合，可以随时添加和删除其中的元素。list里面的元素的数据类型**可以不同**。

`list = [e1,e2,e3]` 定义list。

`list.len()`返回list的元素的个数。

`list[i]`访问i位置的元素，如果为负数，则表示倒数第i个。

`list.append(e)`往list中追加元素到末尾。

`list.insert(index, e)`:插入元素到特定位置。

`list.pop()`:删除末尾的元素。

`list.pop(index)`:删除特定位置的元素。

## 元组 tuple

tuple和list非常类似，也是一种有序列表，但是tuple<font color=red>一旦初始化就不能修改</font>。

使用()来定义tuple:

`tuple = ('James', 'Smith', 'Love')`

只有1个元素的tuple定义时必须加一个逗号,，来消除歧义:

`t = (1,)`

## 条件判断
```
if
elif
else
```
注意，使用`:`然后下一行需要缩进。

if判断条件的简写：

```
if x:
    print(True)
```

只要`x`是非零数值、非空字符串、非空`list`等，就判断为`True`，否则为`False`。

## 循环

第一种：for in 循环：

```
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

`range()`函数，生成一个整数序列，可以再通过list转化成列表:`list(range(5))`

```
>>> list(range(5))
[0, 1, 2, 3, 4]
```

计算1+2+3+...+100：

```
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
```

第二种：while循环：可以使用break和continue:

```
sum = 0
i = 1
while i < 101:
    sum = sum + i
    i = i + 1
print(sum)
```

## 字典dic
dic,即dictionary,java中称为map,使用键-值（key-value）存储，具有极快的查找速度。

```
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']//如果key不存在，则会报错
```

可以使用`key in dic`来判断是dic中是否存在key。返回Ture或者False。

或者使用`dic.get(key)`或者`dic.get(key, default)`前者不存在key时，会返回None。

`dic.pop(key)`:删除key及对应的value。

### 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

1. 查找和插入的速度极快，不会随着key的增加而变慢；
2. 需要占用大量的内存，内存浪费多。

而list相反：

1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。

所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是<font color=red>dict的key必须是不可变对象</font>。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key。

## set 集合
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

```
>>> s = set([1,2,3])
>>> s
{1, 2, 3}
```
注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。

`set.add(key)`:添加一个元素。

`set.remove(key)`:删除一个元素。

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

```
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
{2, 3}
>>> s1 | s2
{1, 2, 3, 4}
```

`s1 & s2`: 求两个集合的交集。

`s1 | s2`: 求连个集合的并集。

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

## 函数
官网常用函数介绍：
[官网api](https://docs.python.org/3/library/functions.html)

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：

```
>>> a = abs
>>> a(-1)
1
```

### 定义函数
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

### 空函数
如果想定义一个什么事也不做的空函数，可以用pass语句：

```
def nop():
    pass
```

`isinstance()`:数据类型检查,eg.

`isinstance(x, (int, float))`:判断x是int值或者float值，是则返回True，否则返回false。

### 小结

定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。

### 默认参数

默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

默认参数必须指向不变对象。

### 可变参数

在参数前面添加一个*。

```
>>> def add(*num):
        sum = 0;
        for n in num:
            sum = sum + n
        return sum
```

```
>>> add(1,2)
3
>>> add(1,2,3)
6
```

可以将list或tuple参数传递进去，需要在其前边加*:

```
>>> s = [1,2,3]
>>> add(*s)
6
```

###关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

```
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

kw可以是一个dic。

```
>>> person('Michael', 30)
name: Michael age: 30 other: {}
>>> person('Michael', 30, city='Beijig')
name: Michael age: 30 other: {'city': 'Beijig'}
>>> d = {'city':'Beijing','Gender':'M'}
>>> person('Michael',30,**d)
name: Michael age: 30 other: {'city': 'Beijing', 'Gender': 'M'}
```

### 命令关键字参数

### 递归函数

汉诺塔的移动可以用递归函数非常简单地实现:

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def move(n, a, b,c):
    if n > 1:
        move(n-1, a, c, b)
        print("# " + a + " --> " + c)
        move(n-1, b, a, c)
    else:
        print("# " + a + " --> " + c)

move(3, 'A', 'B', 'C')
```

期待输出：

```
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
```

## 高阶函数

### 切片

`L[begin:end:step]`

reduce.py

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
```


prod.py

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce
def prod(L):
    def f(x,y):
        return x * y
    return reduce(f, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
```

### map
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

### reduce
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

```
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

### filter

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

### sorted
Python内置的sorted()函数就可以对list进行排序。

```
>>> sorted([36, 5, -12,9,-21])
[-21, -12, 5, 9, 36]
```

此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

```
>>> sorted([36,5,-12,9,-21], key=abs)
[5, 9, -12, -21, 36]
```

要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```
sorted

阅读: 201194
排序算法

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

Python内置的sorted()函数就可以对list进行排序：

```
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```
此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：

```
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```
key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过key=abs处理过的list：

```
list = [36, 5, -12, 9, -21]
keys = [36, 5,  12, 9,  21]
```

然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：

```
keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
```
我们再看一个字符串排序的例子：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```
默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

这样，我们给sorted传入key函数，即可实现忽略大小写的排序：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

小结

sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。

练习

假设我们用一组tuple表示学生名字和成绩：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

请用sorted()对上述列表分别按名字排序：

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def by_name(t):
    return t[0]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key = by_name)
print(L2)
```

再按成绩从高到低排序：

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def by_grade(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key = by_grade, reverse = True)
print(L2)
```

## 返回函数

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

## 匿名函数

```
>>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```
通过对比可以看出，匿名函数`lambda x: x * x`实际上就是：

```
def f(x):
    return x * x
```
关键字`lambda`表示匿名函数，冒号前面的`x`表示函数参数。

匿名函数有个**限制**，就是只能有一个表达式，不用写`return`，返回值就是该表达式的结果。

## 装饰器

## 偏函数

# 模块

# 面向对象编程

- `__`(两个下划线)代表**private**变量，只有内部可以访问，外部不能访问
- 在Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是**特殊变量**，特殊变量是可以直接访问的，不是private变量。
- 一个下划线开头的**实例变量名**，比如`_name`，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
- Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量：`bart._Student__name`, 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。
- `__init__`方法
- 可以给对象自由的绑定属性，也可以在`__init__`方法中绑定必要属性。

## 继承和多态

`isinstance(a, class)` 判断a是不是class的一个实例，相当于java中的`instanceof`方法

静态语言 vs 动态语言

## 获取对象信息

`type()` 判断对象类型，返回对应的Class类型。
`isinstance()` 判断是否是一个对应的实例
`dir()` 获得一个对象的所有属性和方法
`getattr()` 获取属性，相当于getter
`setattr()` 设置属性，相当于setter
`hasattr()` 判断是否有该属性
如果试图获取不存在的属性，会抛出AttributeError的错误。

可以传入一个default参数，如果属性不存在，就返回默认值。

## 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以**任意绑定属性**。

不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# 面向对象高级编程

多重继承、定制类、元类

## 使用`__slots__`
Python允许在定义class的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性。

使用`__slots__`要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。

除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`。

## 使用`@property`
`@property` 把一个getter方法变成属性，后边读属性的时候，实际上是使用了getter()方法。

`@score.setter` 设置属性名为score的setter()方法。

## 多重继承

python可以多重继承，eg:

```
class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print("Running...")

class Flyable(object):
    def fly(self):
        print("Flying...")

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass

```

### Mixln

在设计类的继承关系时，通常，主线都是**单一集成**下来的(类似java的继承)，例如`Ostrich`继承自`Bird`。但是，如果需要"混入"额外的功能，通过**多重继承**就可以实现(类似java的接口)，比如，让`Ostrich`除了继承自`Bird`外，再同时继承`Runnable`。这种设计通常称之为Mixln。

为了更好地看出继承关系，我们把`Runnable`和`Flyable`改为`RunnableMixIn`和`FlyableMixIn`。类似的，你还可以定义出肉食动物`CarnivorousMixIn`和值食动物`HerbivoresMixIn`，让某个动物同时拥有好几个MixIn:

```
class RunnableMixIn(object):
    def run(self):
        print("Running...")

class CarnivorousMixIn(object):
    def eatMeat(self):
        print("Eating meat...")


class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
```

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

## 定制类

**__str__** :  相当于java中的toString()。`__repr__()`

**__iter__** : 如果一个类想被用于`for ... in`循环，类似`list`或`tuple`那样，就必须实现一个`__iter__()`方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的`__next__()`方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

```
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a, b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出训话的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)
```

**__getitem** : Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行。要表现得像list那样按照下标取出元素，需要实现`__getitem__`方法：

```
def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[3])
```

**__getattr__** : 只有在没有找到属性的情况下，才调用`__getattr__`，已有的属性，不会在`__getattr__`中查找。

**__call__** : 调用无参数时调用的方法。使用`callable()`来判断一个变量是对象还是函数。

## 使用枚举类

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weakday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
```

`@unique`装饰器可以帮助我们检查保证没有重复值。

访问这些枚举类型可以有若干种方法：

```
day1 = Weekday.Mon
print(day1)
print(Weekday.Thu)
print(Weekday['Tue'])
print(Weekday.Tue.value)

print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)

print(Weekday(1))

print(day1 == Weekday(1))
```

## 使用元类

**type()** : `type()`函数可以查看一个类型或者变量的类型。

`type()`函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，

**metaclass** : `metaclass`，直译为**元类**，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：**先定义类，然后创建实例**。

但是如果我们想创建出类呢？那就必须根据`metaclass`创建出类，所以：**先定义metaclass，然后创建类**。

连接起来就是：**先定义metaclass，就可以创建类，最后创建实例**。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

(未掌握)

# IO编程

```
#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# 读文件
try:
    f = open('C:\\Users\\ysx\\github\\LearningNotesYsx\\python\\code\\test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 读文件，指定编码格式
try:
    f = open('C:\\Users\\ysx\\github\\LearningNotesYsx\\python\\code\\test_1.txt', 'r', encoding='gbk')
    print(f.read())
finally:
    if f:
        f.close()

# 写文件
try:
    f = open('C:\\Users\\ysx\\github\\LearningNotesYsx\\python\\code\\test_2.txt', 'w')
    f.write('Hello, world!')
finally:
    if f:
        f.close()
```







# 常用函数

`abs()` 绝对值

`str()` 转换为字符串

`s.upper()` 将字符串s转换为大写

`s.lower()` 将字符串s转化为小写

`s.capitalize()` 将字符串s的首字母大写，其余小写

`s.title()` 将字符串s的所有单词首字母大写，其余小写









