# HTML

[教程地址](http://blog.csdn.net/column/details/17220.html)

## 1. HTML 常用标签

### 1.1 p标签

p标签在HTML中常用于表示**段落**，它是英文单词paragraph的缩写。

### 1.2 h标签

h标签用于表示**标题**，它是英文单词header的缩写。在HTML中h标签细分为h1~h6，请注意：h后的数字越大，那么标题所对应的字体越小。

```
<h1>这里是h1</h1>
<h2>这里是h2</h2>
```

### 1.3 hr标签

hr标签用于表示一条**水平横线**，它是英文中Horizontal Rule的缩写。

```
<h1>这里是h1</h1>
<hr>
<h2>这里是h2</h2>
```

### 1.4 br标签

br标签用于表示换行，它在英文所对应的单词是break。

```
<h1>这里<br>是h1</h1>
```

### 1.5 nobr标签

nobr标签表示不换行。

```
<p><nobr>凯里·欧文于2011年以选秀状元身份进入NBA，新秀赛季当选最佳新秀；2014年首次入选全明星正赛先发阵容，并当选最有价值球员；2014-15赛季入选最佳阵容第三阵容；2015-16赛季随骑士队获得NBA总冠军。</nobr></p>
```

### 1.6 center标签

center标签表示居中显示。

```
<h1><center>这里是h1</center></h1>
```

### 1.7 marquee标签

marquee标签用于表示跑马灯效果。

```
<marquee behavior="scroll" direction="left">
        <p>测试marquee标签</p>
</marquee>
```

在marquee标签中可以通过behavior和direction属性控制跑马灯的不同效果。

### 1.8 button标签

button标签用于表示按钮。onclick的值表示监听的函数。

```
<button type="button" onclick="onButtonClick()">This is a button</button>
    <script type="text/javascript">
        function onButtonClick(){
            alert('You click button');
        }
    </script>
```

### 1.9 a标签

a标签在THML中常用于表示锚点和超链接，它是英文中anchor的缩写。

```
<a href="http://blog.csdn.net/next_second" title="程序员学习笔记" target="_blank">请点击此处的超链</a>
```

在a标签中利用href属性指明**超链接的地址**，利用title表示当鼠标悬停在超链接时的**提示文字**，利用target属性表示**打开超链接的方式**。如果target的取值为_blank表示在新窗口中打开超链接；假若target的取值为_self表示在当前窗口中打开超链接。

### 1.10 img标签

img标签在HTML中常用于表示图像，它是英文中image的缩写。

```
<img src="bear.jpg" title="这是我的头像">

<img src="https://avatars2.githubusercontent.com/u/8236175?s=400&u=4ef8ad6e72966ea14cb197e986cff78fb4ca9e6e&v=4" title="头像2">
```

src表示图片文件地址，可以为本地文件地址，也可以为网络图片地址。

title表示鼠标在图片上的时候的提示语。