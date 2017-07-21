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
1. Number
2. 字符串
3. 布尔值
4. null和undefined
5. 数组
6. 对象

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

# 字符串

JavaScript的字符串就是用''或者"" 括起来的字符表示。

## 转义字符: `\`

## 多行字符串：
由于多行字符串用`\n`写起来比较费事，所以最新的ES6标准新增了一种多行字符串的表示方法，用**反引号** \`...` 表示：

## 模板字符串

要把多个字符串连接起来，可以用+号连接：

```
var name = '小明';
var age = 20;
var message = '你好, ' + name + ', 你今年' + age + '岁了!';
alert(message);
```

如果有很多变量需要连接，用+号就比较麻烦。ES6新增了一种模板字符串，表示方法和上面的多行字符串一样，但是它会自动替换字符串中的变量：

```
var name = '小明';
var age = 20;
var message = `你好, ${name}, 你今年${age}岁了!`;
alert(message);
```

# 操作字符串
s.length 字符串的长度

可以使用类似Array的下标操作，索引号从0开始。

由于字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是也没有任何效果。

JavaScript为字符串提供了一些常用方法，注意，调用这些方法本身不会改变原有字符串的内容，而是返回一个**新字符串**。

- toUpperCase() 把一个字符串全部变为大写
- toLowerCase() 把一个字符串全部变为小写
- indexOf() 会搜索指定字符串出现的位置
- substring() 返回指定索引区间的子串

# 数组

JavaScript的数组可以包含任意数据类型，并通过索引来访问每个元素。

使用length属性来获取数组的长度。

**注意**，直接给Array的length赋一个新的值会导致Array大小的变化。

Array可以通过索引把对应的元素修改为新的值，因此，对Array的索引进行赋值会直接修改这个Array。

**注意**,如果通过索引赋值时，索引超过了范围，同样会引起Array大小的变化。

大多数其他编程语言不允许直接改变数组的大小，越界访问索引会报错。然而，JavaScript的Array却不会有任何错误。在编写代码时，不建议直接修改Array的大小，访问索引时要确保索引不会越界。

**indexOf**,与String类似，Array也可以通过indexOf()来搜索一个指定的元素的位置。

**slice**，slice()就是对应String的substring()版本，它截取Array的部分元素，然后染回一个**新的Array**。

注意，slice()的起始参数包括开始索引，不包括结束索引。

如果不给slice()传递任何参数，它就会从头到尾截取所有元素。利用这一点，我们可以很容易地复制一个Array。

**push()**，push()向Array的末尾添加若干元素。

**pop()**，pop()把Array的最后一个元素删除掉。

**unshift**，unshift()往Array的头部添加若干元素。

**shift()**，把Array的第一个元素删除掉。

**sort()**，sort()可以对当天Array进行排序，它会直接修改当前Array的元素位置，直接调用时，按照默认顺序排序。

**reverse()**，reverse()把整个Array()的元素翻转。

**splice()**，splice()方法是修改Array的万能方法，它可以从**指定的索引**开始**删除**若干元素，然后再从该位置添加若干元素。

**concat()**，concat()方法把当前的Array和另一个Array连接起来，并返回一个新的Array。

注意，concat()方法并没有修改当前Array，而是返回了一个新的Array。

实际上，concat()方法可以接收任意个元素和Array，并且自动把Array拆开，然后全部添加到新的Array里。

**join()**，join()方法是一个非常实用的方法，它把当前Array的每个元素都用指定的字符串连接起来，然后返回**连接后的字符串**。如果Array的元素不是字符串，将自动转换为字符串后再连接。

```
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-');//"A-B-C-1-2-3"
//多维数组
var arr = [[1,2, 3], [400, 500, 600], '-'];
var x = arr[1][1]//500

//练习
var arr = ['小明', '小红', '大军', '阿黄'];
alert(`欢迎${arr.sort().slice(0, 3).join(',')}和${arr[3]}同学!`)
```

# 对象
JavaScript用一个`{...}`表示一个对象，键值对以`xxx: xxx`形式申明。

访问属性是通过`.`操作符完成的，但这要求属性名必须是一个有效的变量名。如果属性名包含特殊字符，就必须用`''`括起来：

```
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No. 1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};

xiaoming.name;//"小明"
xiaoming.birth;//1990
```
`xiaohong`的属性名`middle-school`不是一个有效的变量，就需要用`''`括起来。访问这个属性也无法使用.操作符，必须用`['xxx']`来访问：

```
var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};

xiaohong['middle-school'];//'No.1 Middle School'
xiaohong['name'];//'小红'
xiaohong.name;//'小红'
```
也可以用`xiaohong['name']`来访问`xiaohong`的`name`属性，不过`xiaohong.name`的写法**更简洁**。我们在编写JavaScript代码的时候，属性名尽量使用标准的变量名，这样就可以直接通过`object.prop`的形式访问一个属性了。

实际上JavaScript对象的所有属性都是**字符串**，不过**属性对应的值可以是任意数据类型**。

如果访问一个**不存在的属性**会返回什么呢？JavaScript规定，访问不存在的属性不报错，而是返回`undefined`：
```
var xiaoming = {
    name: '小明'
};
xiaoming.age;//undefined
```
由于JavaScript的对象是动态类型，你可以自由地给一个对象添加或删除属性：
```
var xiaoming = {
    name: '小明'
};
xiaoming.age;//undefined
xiaoming.age = 18;//新增一个age属性，value为18
xiaoming.age;//18
delete xiaoming.age;//删除age属性，返回true
xiaoming.age;//undefined
delete xiaoming['name'];//删除name属性，返回true
xiaoming.name;//undefined
delete xiaoming.school;//删除一个不存在的school属性也不会报错，返回true
```
如果我们要检测`xiaoming`是否拥有某一属性，可以用`in`操作符：
```
var xiaoming = {
    name: '小明',
    birth: 1990,
    school: 'No.1 Middle School',
    height: 1.70,
    weight: 65,
    score: null
};
'name' in xiaoming; // true
'grade' in xiaoming; // false
```
不过要小心，如果`in`判断一个属性存在，这个属性不一定是`xiaoming`的，它可能是`xiaoming`**继承**得到的：
```
'toString' in xiaoming; // true
```
因为`toString`定义在`object`对象中，而所有对象最终都会在原型链上指向`object`，所以`xiaoming`也拥有`toString`属性。

要判断一个属性是否是`xiaoming`**自身拥有**的，而不是继承得到的，可以用`hasOwnProperty()`方法：
```
var xiaoming = {
    name: '小明'
};
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false
```

# 条件判断
请注意，`for ... in`对`Array`的循环得到的是**String**而不是Number。

```
var a = ['A', 'B', 'C'];
for (var i in a) {
    alert(i);// '0', '1', '2'
    alert(a[i]);// 'A', 'B', 'C'
}
```
# Map和Set
JavaScript的默认对象表示方式{}可以视为其他语言中的Map或Dictionary的数据结构，即一组键值对。

## Map

`Map`是一组键值对的结构，具有**极快的查找速度**。(与Java中的Map类似)
初始化Map需要一个二维数组，或者使用set函数。
```
var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael');//95

var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined
```
- set(key,value) 添加(设置)键值对
- has(key) 判断是否有该key
- get(key) 获取该key的value
- delete(key) 删除该键值对

由于**一个key只能对应一个value**，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

## Set

Set和Map类似，也是一组**key**的集合，但不存储value。由于**key不能重复**，所以，在Set中，没有重复的key。(与Java中的Set类似)

要创建一个Set，需要提供一个Array作为输入，或者直接创建一个空Set：
```
var s1 = new Set();//空Set
var s2 = new Set([1, 2, 3]);//含1,2,3
```
**重复元素**在Set中**自动被过滤**：
```
var s = new Set([1,2,3,3,'3']);
s; // Set(4) {1, 2, 3, "3"}
```
通过`add(key)`方法可以添加元素到Set中，可以重复添加，但不会有效果：
```
var s = new Set([1,2,3]);
s;//Set(3) {1, 2, 3}
s.add(4);
s;//Set(4) {1, 2, 3, 4}
s.add(4);
s;//Set(4) {1, 2, 3, 4}
```
通过`delete(key)`方法可以删除元素：
```
var s = new Set([1,2,3]);
s;//Set(3) {1, 2, 3}
s.delete(3);
s;//s.delete(3);
```

Map和Set是ES6标准新增的数据类型，请根据浏览器的支持情况决定是否要使用。

# iterable
遍历`Array`可以采用下标循环，遍历`Map`和`Set`就无法使用下标。为了统一集合类型，ES6标准引入了新的iterable类型，Array、Map和Set都属于iterable类型。

具有iterable类型的集合可以通过新的`for ... of`循环来遍历。

`for ... of`循环是ES6引入的新的语法，请测试你的浏览器是否支持：

```
// for ... in 与 for ... of的区别
var a = ['A','B','C'];
a.name = 'Hello';
for (var x in a) {
    alert(x);//'0','1','2','name'
}
a.length;//3
```
`for ... in`循环将把name包括在内，但Array的length属性却不包括在内。

`for ... of`循环则完全修复了这些问题，它只循环集合本身的元素：

这就是为什么要引入新的`for ... of`循环。
```
var a = ['A','B','C'];
a.name = 'Hello';
for (var x of a) {
    alert(x);//'A','B','C'
}
```
然而，更好的方式是直接使用iterable内置的forEach方法，它接收一个函数，每次迭代就自动回调该函数。以Array为例：
```
var a = ['A','B','C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
});
```

Set与Array类似，但Set没有索引，因此回调函数的前两个参数都是元素本身：
```
var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    alert(element);
});
```
Map的回调函数参数依次为value、key和map本身：
```
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    alert(value);
});
```
如果对某些参数不感兴趣，由于JavaScript的函数调用不要求参数必须一致，因此可以忽略它们。例如，只需要获得Array的element：
```
var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    alert(element);
});
```






# 常用函数

## 字符串
- length 字符串的长度
- toUpperCase() 把一个字符串全部变为大写
- toLowerCase() 把一个字符串全部变为小写
- indexOf() 会搜索指定字符串出现的位置
- substring() 返回指定索引区间的子串

## 对象

- in 判断对象是否有该属性，如果有则返回true，否则范湖false
- hasOwnProperty() 判断一个属性是否是对象自身拥有的，而不是继承的，有则返回true


```
var s = 'Hello, world!';
s.length;//13
```

```
var xiaoming = {
    name: '小明'
};
'name' in xiaoming;//true
'toString' in xiaoming;//true
xiaoming.hasOwnProperty('name'); // true
xiaoming.hasOwnProperty('toString'); // false
```



















