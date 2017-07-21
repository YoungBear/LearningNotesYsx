'use strict';

var m = new Map([['Michael', 95], ['Bob', 75], ['Tracy', 85]]);
m.get('Michael');//95

var m = new Map(); // 空Map
m.set('Adam', 67); // 添加新的key-value
m.set('Bob', 59);
m.has('Adam'); // 是否存在key 'Adam': true
m.get('Adam'); // 67
m.delete('Adam'); // 删除key 'Adam'
m.get('Adam'); // undefined

var m = new Map();
m.set('Adam', 67);
m.set('Adam', 88);
m.get('Adam');//88

//set learn
var s1 = new Set();//空Set
var s2 = new Set([1, 2, 3]);//含1,2,3

var s = new Set([1,2,3,3,'3']);
s; // Set(4) {1, 2, 3, "3"}

var s = new Set([1,2,3]);
s;//Set(3) {1, 2, 3}
s.add(4);
s;//Set(4) {1, 2, 3, 4}
s.add(4);
s;//Set(4) {1, 2, 3, 4}

var s = new Set([1,2,3]);
s;//Set(3) {1, 2, 3}
s.delete(3);
s;//s.delete(3);

var a = ['A', 'B', 'C'];
var s = new Set(['A', 'B', 'C']);
var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
for (var x of a) {//遍历Array
    alert(x);
}
for (var x of s) {// 遍历Set
    alert(x);
}
for (var x of m) { // 遍历Map
    alert(x[0] + '=' + x[1]);
}

// for in 与 for of的区别
var a = ['A','B','C'];
a.name = 'Hello';
for (var x in a) {
    alert(x);//'0','1','2','name'
}
a.length;//3

var a = ['A','B','C'];
a.name = 'Hello';
for (var x of a) {
    alert(x);//'A','B','C'
}

//iterable
var a = ['A','B','C'];
a.forEach(function (element, index, array) {
    // element: 指向当前元素的值
    // index: 指向当前索引
    // array: 指向Array对象本身
    alert(element);
});

var s = new Set(['A', 'B', 'C']);
s.forEach(function (element, sameElement, set) {
    alert(element);
});

var m = new Map([[1, 'x'], [2, 'y'], [3, 'z']]);
m.forEach(function (value, key, map) {
    alert(value);
});

var a = ['A', 'B', 'C'];
a.forEach(function (element) {
    alert(element);
});