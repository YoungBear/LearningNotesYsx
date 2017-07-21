'use strict';

var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-');//"A-B-C-1-2-3"

//多维数组
var arr = [[1,2, 3], [400, 500, 600], '-'];
var x = arr[1][1]//500

//练习
var arr = ['小明', '小红', '大军', '阿黄'];
alert(`欢迎${arr.sort().slice(0, 3).join(',')}和${arr[3]}同学!`)