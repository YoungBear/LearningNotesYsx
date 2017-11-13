function printHello(){
    console.log( "Hello, World!");
}
// 两秒后执行以上函数
var t = setInterval(printHello, 2000);

clearInterval(t);
