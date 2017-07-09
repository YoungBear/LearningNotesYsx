# JavaScript 学习笔记

感谢[廖雪峰的JavaScript教程](http://www.liaoxuefeng.com/wiki/001434446689867b27157e896e74d51a89c25cc8b43bdb3000)

为什么学习JavaScript:

在Web世界里，只有JavaScript能跨平台、跨浏览器驱动网页，与用户交互。

```
http://localhost/~youngbear/learn/JavaScript/code/

http://localhost/~youngbear/learn/JavaScript/code/hello.js

```

[测试路径](http://localhost/~youngbear/learn/JavaScript/code/hello.js)

# 数据类型

## Number
    JavaScript不区分整数和浮点数，统一用Number表示。

```
123;//整数123
0.456;//浮点数0.456
1.2345e3;//科学计数法1.2345x1000，等同于1234.5
-99;//负数
NaN;//NaN表示Not a Number，当无法计算结果时用NaN表示
Infinity;//Infinity表示无限大，当数值超过了JavaScript的Number所能表示的最大值，就表示为Infinity

```

## 字符串
字符串是以单引号'或者双引号"括起来的任意文本。

## 布尔值
true和false

运算符：

```
&&是逻辑与运算
||是逻辑或运算
!是逻辑非运算
比较运算符：
>
>=
==
```
JavaScript允许对任意数据类型做比较：
```
false == 0;//true
false === 0;//false
```
JavaScript有两种比较符：

`==`会自动转换数据类型再比较，很多时候，会得到非常诡异的结果；

`===`不会自动转换数据类型，如果数据类型不一致，返回`false`，如果一致，再比较。

所以，由于JavaScript这个设计缺陷，**不要**使用`==`比较，始终坚持使用`===`比较。

**另一个例外**：`NaN`这个特殊的Number与所有其他值都不相等，包括它自己：
```
NaN === NaN;//false
```

**最后**，要注意浮点数的比较，因为计算机存储浮点数有误差，所以不要用`===`来比较两个浮点数，用一个误差来表示。

### null和undefined
`null`表示空值。

`undefined`表示值未定义。

大多数情况下，我们都应该使用`null`。`undefined`仅仅在**判断函数参数是否传递**的情况下有用。

## 数组

数组是一组按顺序排列的集合，集合的每个值称为元素。JavaScript的数组可以包括**任意数据类型**。eg.

```
[1, 2, 3.14, 'Hello', null, true];
```
上述数组包含6个元素。数组用`[]`表示，元素之间用`,`分隔。

另一种穿件数组的方法是通过`Array()`函数实现：

```
new Array(1, 2, 3);//创建了数组[1, 2, 3]
```
然而，处于代码的可读性考虑，强烈建议直接使用`[]`。

数组的元素可以通过索引来访问，索引从0开始。

## 对象
JavaScript的对象时一组由`键-值`组成的无序集合。eg.
```
var person = {
	name: 'Bob',
	age: 20,
	tags: ['js', 'web', 'mobile'],
	city: 'Beijing',
	hasCar: true,
	zipCode: null
};
```

JavaScript对象的**键都是字符串类型**，**值可以是任意数据类型**。每个键又称为对象的属性。

要获取一个对象的属性，我们用`对象名称.属性名`的方式：

```
person.name;//'Bob'
person.zipCode;//null
```

## 变量

变量名是大小写**英文**、**数字**、**$**(美元符号)和**_**(下划线)的组合，且不能用数字开头。变量名也不能是JavaScript的关键字，如`if`、`while`等。声明一个变量用'var'语句，比如：

```
var a;// 申明了变量a，此时a的值为undefined
var $b = 1;// 申明了变量$b，同时给$b赋值，此时$b的值为1
var s_007 = '007';// s_007是一个字符串
var Answer = true;// Answer是一个布尔值true
var t = null;// t的值是null
```

使用`=`对变量进行赋值。可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，但是要注意只能用`var`声明一次。

这种变量**本身类型不固定**的语言称之为**动态语言**，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。

## strict模式

JavaScript在设计之初，为了方便初学者学习，并不强制要求用`var`声明变量。这个设计错误带来了严重的后果：如果一个变量没有通过`var`声明就被使用，那么该变量就自动被声明为**全局变量**：

```
i = 10; // i现在是全局变量
```

在**同一个页面**的不同的JavaScript文件中，如果都不用`var`声明，恰好都使用了变量i，将造成变量i互相影响，产生难以调试的错误结果。

使用`var`声明的变量则不是全局变量，它的范围被限制在该变量被声明的**函数体**内（函数的概念将稍后讲解），同名变量在不同的函数体内互不冲突。

为了修补JavaScript这一严重设计缺陷，ECMA在后续规范中推出了strict模式，在strict模式下运行的JavaScript代码，强制通过var申明变量，未使用var申明变量就使用的，将导致运行错误。

启用strict模式的方法是在JavaScript代码的第一行写上：

```
'use strict';
```
这是一个字符串，不支持strict模式的浏览器会把它当做一个字符串语句执行，支持strict模式的浏览器将开启strict模式运行JavaScript。





















