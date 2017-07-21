'use strict';

var a = ['A', 'B', 'C'];
for (var i in a) {
    alert(i);// '0', '1', '2'
    alert(a[i]);// 'A', 'B', 'C'
}