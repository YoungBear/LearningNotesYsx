# Node.js 学习笔记

[教程地址](http://www.runoob.com/nodejs/nodejs-tutorial.html)

[官网-中文](https://nodejs.org/zh-cn/)

## [介绍](https://www.sitepoint.com/node-js-is-the-new-black/)
## [知乎上的讨论](https://www.zhihu.com/question/33578075)
## [外国人的介绍](http://www.codeceo.com/article/10-best-nodejs-tutorials-demo.html)
## [中文API](http://nodejs.cn/api/)

## 事件驱动程序

Node.js 使用事件驱动模型，当web server接收到请求，就把它关闭然后进行处理，然后去服务下一个web请求。

当这个请求完成，它被放回处理队列，当到达队列开头，这个结果被返回给用户。

这个模型非常高效可扩展性非常强，因为webserver一直接受请求而不等待任何读写操作。（这也被称之为**非阻塞式IO**或者**事件驱动IO**）

## EventEmitter

EventEmitter 的核心就是事件触发与事件监听器功能的封装。

EventEmitter 提供了多个属性，如 `on` 和 `emit`。`on` 函数用于**绑定**事件函数，`emit` 属性用于**触发**一个事件。

[具体参考](http://www.runoob.com/nodejs/nodejs-event.html)

## 缓冲区 Buffer

```
// 写入缓冲区，返回实际写入的大小
buf.write(string[, offset[, length]][, encoding])
// 从缓冲区读取数据， 返回：解码缓冲区数据并使用指定的编码返回字符串
buf.toString([encoding[, start[, end]]])
// 将 Buffer 转换为 JSON 对象， 返回 JSON 对象。
buf.toJSON()
// 缓冲区合并，返回一个多个成员合并的新 Buffer 对象。
Buffer.concat(list[, totalLength])
// 缓冲区比较，返回一个数字，表示 buf 在 otherBuffer 之前，之后或相同。
buf.compare(otherBuffer);
// 拷贝缓冲区， 没有返回值。
buf.copy(targetBuffer[, targetStart[, sourceStart[, sourceEnd]]])
// 缓冲区裁剪，返回一个新的缓冲区，它和旧缓冲区指向同一块内存，但是从索引 start 到 end 的位置剪切。
buf.slice([start[, end]])
// 缓冲区长度
buf.length;
```

## 流 Stream

Stream 有四种流类型：

- Readable - 可读操作。
- Writable - 可写操作。
- Duplex - 可读可写操作.
- Transform - 操作被写入数据，然后读出结果。

所有的 Stream 对象都是 EventEmitter 的实例。常用的事件有：

- data - 当有数据可读时触发。
- end - 没有更多的数据可读时触发。
- error - 在接收和写入过程中发生错误时触发。
- finish - 所有数据已被写入到底层系统时触发。

## 全局对象

JavaScript 中有一个特殊的对象，称为全局对象（Global Object），它及其所有属性都可以在程序的任何地方访问，即**全局变量**。
在浏览器 JavaScript 中，通常 window 是全局对象， 而 Node.js 中的全局对象是 global，所有全局变量（除了 global 本身以外）都是 global 对象的属性。
在 Node.js 我们可以直接访问到 global 的属性，而不需要在应用中包含它。

### 全局对象与全局变量

global 最根本的作用是作为全局变量的宿主。按照 ECMAScript 的定义，满足以下条 件的变量是全局变量：

- 在最外层定义的变量；
- 全局对象的属性；
- 隐式定义的变量（未定义直接赋值的变量）。

当你定义一个全局变量时，这个变量同时也会成为全局对象的属性，反之亦然。需要注意的是，在 Node.js 中你不可能在最外层定义变量，因为所有用户代码都是属于当前模块的， 而模块本身不是最外层上下文。

**注意**： 永远使用 var 定义变量以避免引入全局变量，因为全局变量会污染 命名空间，提高代码的耦合风险。

### 常用全局变量

- `__filename`  表示当前正在执行的脚本的文件名。它将输出文件所在位置的绝对路径，且和命令行参数所指定的文件名不一定相同。 如果在模块中，返回的值是模块文件的路径。
- `__dirname`  表示当前执行脚本所在的目录。
- `setTimeout(cb, ms)` 全局函数， 指定的毫秒(ms)数后执行指定函数(cb)。：setTimeout() 只执行一次指定函数。返回一个代表定时器的句柄值。
- `clearTimeout(t)` 全局函数， 用于停止一个之前通过 setTimeout() 创建的定时器。 参数 t 是通过 setTimeout() 函数创建的定时器。
- `setInterval(cb, ms)` 全局函数， 在指定的毫秒(ms)数后执行指定函数(cb)。返回一个代表定时器的句柄值。可以使用 clearInterval(t) 函数来清除定时器。setInterval() 方法会不停地调用函数，直到 clearInterval() 被调用或窗口被关闭。
- `clearInterval(t)` 全局函数， 用于停止一个之前通过 setInterval() 创建的定时器。
- `console` 控制台标准输出。
- `process` 用于描述当前Node.js 进程状态的对象，提供了一个与操作系统的简单接口。
