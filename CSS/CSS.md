# CSS

## CSS简介
CSS即层叠样式表(Cascading Style Sheet)它主要用于网页样式设计，比如：文字的大小，颜色，元素的定位等等。CSS的诞生将页面架构和页面显示进行了分离，各司其责。尤其在HTML5中废除了以往的font标签，big标签，strike标签，建议开发人员把外观的控制交给CSS负责。

## 1. CSS选择器

CSS 选择器用于选择需要设定样式的元素从而实现网页样式的设计，比如：文字的大小，颜色，元素的定位等等。

### 1.1 标签选择器

标签选择器，也常称为元素选择器；它用于设定指定标签的样式。(<font color=red>使用标签名</font>)

语法格式为：

```
标签名{
    property1 : value1;
    property2 : value2;
    property3 : value3;
    property4 : value4;
    ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标签选择器</title>
    <style type="text/css">
        p{
            font-size: 40px;
            color: white;
            width: 880px;
            height: 50px;
            background-color: pink;
        }
    </style>
</head>
<body>
    <p>本文作者：谷哥的小弟</p>
    <p>博客地址：http://blog.csdn.net/lfdfhl</p>
</body>
</html>
```

在该示例中，我们通过标签选择器为p标签统一设置宽度，高度，文字大小和背景颜色。

### 1.2 ID选择器

id选择器可依据id属性的值为标签指定样式，语法格式如下：（<font color=red>使用井号#</font>）

```
#idvalue {
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>id选择器</title>
    <style type="text/css">
        #names{
            background-color: pink;
        }
        #address{
            background-color: red;}
    </style>
</head>
<body>
    <p id="names">欧文</p>
    <h2 id="address">博客地址：http://yangshaoxiong.tech</h2>
</body>
</html>
```

在该示例中通过id选择器为id值为name的标签设置背景色为pink样式，为id值为address的标签设置背景色为red样式。

### 1.3 类选择器

类选择器可依据class属性的值为标签指定样式，语法格式如下：(<font color=red>使用点号.</font>）

```
.classvalue {
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>类选择器</title>
    <style type="text/css">
        .names{
            background-color: pink;
            color: white;
        }
        .address{
            background-color: red;
            color: white;
        }
    </style>
</head>
<body>
    <p class="names">欧文</p>
    <h2 class="address">博客地址：http://yangshaoxiong.tech</h2>
</body>
</html>
```

在该示例中，通过类选择器为class属性值为name和address的标签设置了样式。

### 1.4 通配符选择器

通配符选择器非常的简单，它会将页面中<font color=red>**所有的标签**</font>都设置成统一的样式，语法如下：（<font color=red>使用星号*</font>）

```
* {
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>通配符选择器</title>
    <style type="text/css">
    * {
        color: red;
    }
    </style>
</head>

<body>
    <strong>欢迎访问我的博客</strong>
    <em>谷哥的小弟</em>
    <p>http://blog.csdn.net/lfdfhl</p>
    <i>我们一起学习</i>
</body>

</html>
```

在此利用通配符选择器为所有元素设置了统一的样式；让每个标签中的文字都变成了红色。

**通配符选择器常见用途**

为了更好地兼容不同浏览器，我们可利用通配符选择器剔除浏览器默认的样式，代码如下：

```
* {
        margin: 0;
        padding: 0;
    }
```

通过该段代码将页面中的所有标签的margin值和padding值均设置为0。

### 以下这几个选择器都是上边几种选择器的组合
### 1.5 并集选择器

并集选择器由各个选择器通过<font color=red>**逗号**</font>连接而成的，它为不同的标签设置相同的CSS样式；语法格式如下：

```
selector1,selector2,selector3... {
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>类选择器</title>
    <style type="text/css">
        h2,#age,.names{
            background-color: pink;
            color: white;
        }
    </style>
</head>
<body>
    <h2>博客地址：http://yangshaoxiong.tech</h2>
    <p class="names">欧文</p>ss
    <i id="age">27</i>
</body>
</html>
```

在该示例中通过并集选择器统一为h2标签，id属性为age的标签，class属性为name的标签设置了样式。

### 1.6 标签指定式选择器

标签指定式选择器用于为指定的标签设置CSS样式；它表示并且的关系，即多个选择器的条件**都需要满足**。它最常见的用法是**标签名与类选择器**的结合或者**标签名与ID选择器**的结合，所以更加具体地来说标签指定式选择器有两种写法：

第一种：

```
标签名.类选择器名{
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

第二种：

```
标签名#ID选择器名{
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>类选择器</title>
    <style type="text/css">
        h2#age{
            background-color: pink;
            color: white;
        }
        h2.names{
            background-color: red;
            color: black;
        }
    </style>
</head>
<body>
    <h2>博客地址：http://yangshaoxiong.tech</h2>
    <p class="names">欧文</p>
    <i id="age">27</i>
    <h2 class="names">欧文</h2>
    <h2 id="age">27</h2>
</body>
</html>
```

### 1.7 后代选择器

后代选择器又称为包含选择器；与标签指定式选择器强调的”既….并且….”不同，后代选择器强调的是<font color=red>**"嵌套"**</font>，语法格式如下：（选择器之间用<font color=red>**空格**</font>隔开）

```
selector1 selector2 selector3... {
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>后代选择器</title>
    <style type="text/css">
    div .welcome {
        font-size: 23px;
        color: red;
    }
    </style>
</head>

<body>
    <div>
        <div>
            <section>
                 <p class="welcome">hello everyone</p>
            </section> 
        </div>
        <p class="welcome">欢迎访问我的博客</p>
        <p class="welcome">一起交流开发技术</p>
    </div>
    <p id="title">谷哥的小弟</p>
    <div>http://blog.csdn.net/lfdfhl</div>

</body>

</html>
```

在该实例中通过后代选择器为div标签里的所有class属性等于welcome的标签设置了样式。div标签中，不管是子元素，还是孙子元素只要其class属性等于welcome那么都会加上特定的样式。

### 1.8 子选择器

子选择器用于为指定标签的<font color=red>**第一代子元素**</font>设置样式，语法格式如下：(使用<font color=red>大于号></font>)

```
selector1 > selector2{
   property1 : value1;
   property2 : value2;
   property3 : value3;
   property4 : value4;
   ..................
}
```

eg.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>子选择器</title>
    <style type="text/css">
    div>.welcome {
        font-size: 23px;
        color: red;
    }
    </style>
</head>

<body>
    <div>
        <div>
            <section>
                 <p class="welcome">hello everyone</p>
            </section> 
        </div>
        <p class="welcome">欢迎访问我的博客</p>
        <p class="welcome">一起交流开发技术</p>
    </div>
    <p id="title">谷哥的小弟</p>
    <div>http://blog.csdn.net/lfdfhl</div>

</body>

</html>
```

通过子选择器为div标签里的class属性等于welcome的直接子标签设置了样式。

**请注意：后代选择器和子选择器的区别：**

子选择器仅作用于标签的直接后代(第一代后代)；而后代选择器作用于标签的所有子孙后代元素。

## 2. 伪类

在CSS中，伪类用于向某些选择器添加特殊的效果。

在此介绍与超链接标签a有关的伪类。请看如下示例：

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>伪类</title>
    <style type="text/css">

            a:link{
                 color: red;
                 text-decoration: none;  
            } 

            a:visited{
                color: pink;
            }

            a:hover{
                 color: green;
                 text-decoration: underline;   
            }

            a:active{
                 color: black;
            }

        </style>
</head>
<body>
    <a href="http://blog.csdn.net/lfdfhl" target="_blank">谷哥的小弟</a>
</body>
</html>
```

代码详解如下：

- 利用a:link{ }设置了**超链接的颜色**，它的作用等同于a{ }选择器；但是某些浏览器不支持a:link{ }的写法导致其设置失效

- 利用a:visited{ }设置**超链接访问过后**的样式

- 利用a:hover{ }设置**鼠标放到超链接上**时的样式

- 利用a:active{ }设置**超链接被点击瞬间**的样式

- 请按照先后顺序实现a:visited{ }和a:hover{ }以及a:active{ }从而确保浏览器显示预计的效果

请分别在IE浏览器和谷歌浏览器中运行本示例，注意伪类在不同浏览器中可能出现的细微差异。

## 3. 伪元素

在CSS中，伪元素用于将特殊的效果添加到某些选择器。在此介绍几个CSS中常用的伪元素。

- `:first-letter` 用于向文本中的**第一个字**设置特殊样式。
- `:first-line` 用于向文本的**首行**设置特殊样式。
- `:before` 用于在元素的内容**之前**插入新内容。
- `:after` 用于在元素的内容**之后**插入新内容。

## 4. 盒子模型
在网页设计中CSS的盒子模型是一个非常重要的概念。HTML中的每个元素占据一个矩形区域，这块区域就是该元素所占据的盒子。

盒子包括如下几个部分：border、content、padding、margin。

- border，即盒子的外边框
- content，即盒子中所容纳的内容
- padding，即内容与边框之间的填充
- margin，即盒子与外界(其它盒子)之间的间隔

### 4.1 边框(border)

border常见属性：

- 宽度:`border-width:5px;`
- 样式:`border-style:solid;`常见的样式：solid(实线)、dotted(点线)、dashed(虚线)
- 颜色:`border-color:red;`

eg.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>盒子模型</title>
    <style type="text/css">
        div{
            width: 370px;
            height: 100px;
            background-color: yellow;
            border-width: 2px;
            border-style: dashed;
            border-color: red;
        }
    </style>
</head>
<body>
    <div>
        <p>本文作者：谷哥的小弟</p>
        <p>博客地址：http://blog.csdn.net/lfdfhl</p>
    </div>
</body>
</html>
```

当然，也可以**单独设置**某条边框的样式，分别为top,right,bottom,left。例如：

```
border-top-width:1px;
border-top-style:solid;
border-top-color: green;
```

我们也可以进行属性的**连写**(顺序可以改变)。

```
border-left:1px dotted  pink;
border-right: 1px dashed black;
border-bottom: 1px solid red;
```

### 4.2 内容(content)

盒子中的内容各不相同，视具体的需求而定。比如：图片，文本，视频，音频等等。

### 4.3 填充(padding)

与Android类似，padding-top,padding-right,padding-bottom,padding-left(从top逆时针旋转)。也可以统一设置padding。

**关于填充(padding)的属性联写：**

- padding: 10px; 表示上，右，下，左的填充值为10px 
- padding: 10px 20px;表示上和下的填充值为10px；左和右的padding值为20px 
- padding: 10px 20px 30px;表示上的填充值为10px ；左和右的padding为20px；下的填充值为30px 
- padding: 10px 20px 30px 40px;表示上， 右 ， 下， 左的填充值

### 4.4 间隔(margin)

与Android类似，margin-top,margin-right,margin-bottom,margin-left。

### 4.5 overflow

overflow属性用于指定当内容**溢出元素时**的应对措施。

- `overflow: visible` visible为overflow属性的**默认值**。使用该值后，假若元素中内容过多，这些内容不会被修剪，会在元素之外显示。
- `overflow: hidden`使用该值后，假若元素中内容过多，**超出部分将被隐藏**。
- `overflow: auto`使用该值后，假若元素中内容过多，那么系统会为元素设置滚动条；假若内容不够多并没有超出元素，那么系统不会为元素设置滚动条。所以，在实际开发中多采用该属性。
- `overflow: scorll`使用该值后，不论元素中内容是否超出元素的大小，系统都会为元素设置滚动条。

eg.

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>overflow</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }

    div {
        margin: 50px;
        width: 350px;
        height: 100px;
        border: 1px solid red;
        overflow: auto;
    }
    </style>
</head>

<body>
    <div>
        <p>本文作者:谷哥的小弟</p>
        <p>博客地址:http://blog.csdn.net/lfdfhl</p>
        <p>我们一起学习HTML</p>
        <p>我们一起学习CSS</p>
        <p>我们一起学习JS</p>
        <p>我们一起学习Android</p>
        <p>我们一起学习J2EE</p>
    </div>
</body>

</html>
```

### 4.6 元素居中

使用`margin: 0 auto;`可以使元素居中。

### 4.7 图文对齐

使用`vertical-align`属性实现图文对齐的功能，其取值及对应作用如下：

- `baseline` 元素放置在父元素的基线上，默认值。
- `sub` 垂直对齐文本的下标
- `super` 垂直对齐文本的上标
- `top` 把元素的顶端与行中最高元素的顶端对齐
- `text-top` 把元素的顶端与父元素字体的顶端对齐
- `middle` 把此元素放置在父元素的中部
- `bottom` 把元素的顶端与行中最低的元素的顶端对齐
- `text-bottom` 把元素的底端与父元素字体的底端对齐

### 需要注意的问题

**第一个问题：**

两个盒子**垂直**显示的时候，如果上方的盒子设置了margin-bottom: Mpx并且下方的盒子设置了 margin-top:Npx；那么两者的实际间距并不是M+N而是M、N两者的**最大值**。

**第二个问题：**

两个盒子**嵌套**显示的时候，若想通过给内部的盒子设置margin-top:Mpx;使其距离外部盒子顶部产生一定距离；此时发现无效，需要给外部盒子设置overflow: hidden;方可解决该问题。

## 5. display属性

### HTML标签的分类

按照标签显示方式的不同将HTML标签分为：块级标签(block)，行内标签(inline)，行内块标签(inline-block)；现对其分别介绍。

**1. 块级标签(block)**

典型的块级标签有：`<p></p>，<div></div>，<h1></h1>，<form></form>，<ul></ul>`

它们具有如下特点：

- 块级标签**独占一行**显示(不论其实际宽度是否有屏幕那么宽)
- 块级标签的高度、宽度、行高以及顶和底边距都可设置
- 当块级标签发生嵌套时候如果子标签未设置宽度，那么该子标签的宽度为其父标签的宽度

**2. 行内标签(inline)**

典型的行内标签有：`<span></span>，<strong></strong>，<label></label>，<a></a>，<br>`

它们具有如下特点：

- 行内标签**不会独占一行**显示，会和其他标签在同一行显示
- 不能直接设置行内标签的高度、宽度、行高以及顶和底边距
- 行内标签的宽度就是它包含的文字或图片的宽度

**3. 行内块标签(inline-block)**

典型的行内标签有：`<img>，<input>`

它们具有如下特点：

- 行内块标签在同一行显示
- 可以设置行内块标签的高度、宽度

### display属性

在某些需求下，我们可以利用display实现块级标签、行内标签、行内块标签的相互转换。

### 5.1 将行内标签转换为块级标签

`display: block;`可以将行内标签转换成块级标签。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>display属性</title>
    <style type="text/css">
    a {
        width: 300px;
        height: 100px;
        font-size: 30px;
        font-family: 宋体;
        text-decoration:none;
        color: red;
        background-color: yellow;
        display: block;
    }
    </style>
</head>

<body>
    <a href="http://blog.csdn.net/lfdfhl">原创作者</a>
    <br>
    <a href="http://blog.csdn.net/lfdfhl">谷哥的小弟</a>
</body>

</html>
```

在此，在标签选择器a中利用了display: block将标签<a></a>从行内标签转换成了块级标签。所以，点击整个黄色区域都可以实现超链接。换句话说：原本的<a></a>标签是不能指定其宽高的，但是在此通过display: block就将其转换成了块级标签从而扩大了超链接的点击区域。

### 5.2 将行内标签转换为行内块标签

`display: inline-block;` 将行内标签转换成行内块标签。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>display属性</title>
    <style type="text/css">
    a {
        width: 300px;
        height: 300px;
        font-size: 30px;
        font-family: 宋体;
        color: red;
        background-color: pink;
        text-decoration: none;
        display: inline-block;
    }
    </style>
</head>

<body>
    <a href="http://blog.csdn.net/lfdfhl">原创作者</a>
    <a href="http://blog.csdn.net/lfdfhl">CSDN 谷哥的小弟</a>
</body>

</html>

```

其中，a本身是超链接标签，属于行内标签。转换为行内块标签后，可以设置宽高了，并且可以将它们放在同一行显示了。

### 5.3 将块级标签转换为行内标签

`display: inline;` 将块级标签转换成了行内标签。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>display属性</title>
    <style type="text/css">
    div {
        font-size: 30px;
        font-family: 宋体;
        color: red;
        background-color: pink;
        margin-left: 15px;
        display: inline;
    }
    </style>
</head>

<body>
    <div>谷哥的小弟 </div>
    <div>http://blog.csdn.net/lfdfhl</div>
</body>

</html>
```

在此，在标签选择器div中利用了display: inline将标签<div></div>从块级标签转换成了行内标签。既然是行内标签那么就可以将两个<div></div>放到同一行显示了；当然，此时为其设置的宽和高也就无效了。

## 6. float 浮动

**浮动的特点:**

1、使用了float的元素会脱离标准流不再占原来的位置
2、几个块级元素(比如div)同时使用float时它们将在同一行显示
3、float可将行内元素转化为行内块元素

**浮动(float)用途:**

1、利用浮动(float)实现图文环绕
2、利用浮动(float)制作导航栏
3、利用浮动(float)实现网页布局

## 7. position定位

### 简介

定位(position)允许用户较为精确地定义元素出现的相对位置，这个位置可以是相对于其本身出现的位置，也可以是相对于其上级元素的位置，也可以是相对于其他元素的位置，亦可为相对于浏览器视窗左上角的位置。

### 语法

- 定位(position)常用类型：static、absolute、relative、fixed
- 定位(position)通常与top、right、bottom、left属性联合使用
- 定位(position)的使用可能导致元素脱离标准流

### 7.1 static
position:static是CSS中默认的定位类型，在该类型下元素以标准流的显示方式，其位置不受top、bottom、left、right的影响。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>static定位</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }

    div {
        width: 510px;
        height: 200px;
        border: 1px solid red;
        background-color: greenyellow;
        position: static;
        left: 50px;
        top: 80px;
    }
    </style>
</head>

<body>
    <div>凯里欧文</div>
</body>

</html>
```

在该示例中，在标签选择器div里设置了position:static并且为left和top属性设置了具体的值，但是我们发现：<div></div>的位置没有发生改变。

### 7.2 absolute

`position:absolute`用于生成**绝对定位**的元素，即相对于static定位以外的第一个父元素进行定位。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>absolute定位</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }

    div {
        width: 510px;
        height: 200px;
        border: 1px solid red;
        background-color: #7FFF00;
        position: absolute;
        left: 50px;
        top: 80px;
    }
    </style>
</head>

<body>
    <div>
        <p>本文作者:谷哥的小弟</p>
        <p>博客地址:http://blog.csdn.net/lfdfhl</p>
    </div>
</body>

</html>
```

在该示例中，在标签选择器div里设置了position:absolute并且为left和top属性设置了具体的值，程序运行后发现<div></div>的位置像我们期待的那样发生了移动。

在此，小结position:absolute的特点：

- 当为元素设置了position:absolute，那么该元素会脱离标准流(脱标)，这一点和浮动很类似
- 当为一个单独的元素设置position:absolute，该元素会以浏览器左上角(<body></body>左上角)为基准设置定位
- 当元素发生嵌套时，如果父元素没有设置除了static之外的其他定位；子元素设置position:absolute；在该情况下：子元素的定位以浏览器左上角(<body></body>左上角)为基准设置定位。
- 当元素发生嵌套时，如果父元素设置除了static之外的其他定位；子元素设置position:absolute；在该情况下：子元素的定位以父元素的左上角为基准。
- 为行内元素(比如<span></span>)设置position:absolute后该行内元素会转化为行内块元素

### 7.3 relative

`position:relative`用于微调元素位置，即相对于元素本身原来的位置进行调整。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>relative定位</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }

    .firstBox {
        width: 510px;
        height: 200px;
        border: 1px solid red;
        background-color: #7FFF00;
        position: relative;
        top: 40px;
        left: 90px;
    }

    .secondBox {
        width: 510px;
        height: 200px;
        border: 1px solid red;
        background-color: #00FFFF;
    }
    </style>
</head>

<body>
    <div class="firstBox">        
        <p>本文作者:谷哥的小弟</p>
        <p>博客地址:http://blog.csdn.net/lfdfhl</p>
    </div>
    <div class="secondBox">
        <p>有心课堂</p>
        <p>http://www.stay4it.com/</p>
    </div>
</body>

</html>
```

在该示例中，在类选择器firstBox中设置了position:relative和left、top属性。从效果图中可以看到：使用了类选择器firstBox的<div></div>的位置发生了改变。

在此，小结position:relative的特点：

- 元素设置position:relative后会根据top、right、bottom、left的值并以其原始位置为参照进行移动。
- 元素设置position:relative后该元素不会脱离标准流。
- 元素设置position:relative后不能进行元素的模式转换，比如：不能将行内元素<span></span>转换为行内块元素。
- position:relative一种常见的用法：子绝父相，即子元素设置绝对定位position:absolute而父元素设置相对定位position:relative。

### 7.4 fixed

`position:fixed`表示固定定位，即相对浏览器窗口定位。采用该定位后，不论页面如何滚动，该盒子显示的位置不变。

```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>fixed定位</title>
    <style type="text/css">
    * {
        margin: 0;
        padding: 0;
    }

    img {
        position: fixed;
    }

    p {
        width: 500px;
        background-color: #7FFF00;
    }
    </style>
</head>

<body>
    <img src="bear.jpg" width="100px" height="110px">
    <p>
       凯里·欧文于2011年以选秀状元身份进入NBA，新秀赛季当选最佳新秀；2014年首次入选全明星正赛先发阵容，并当选最有价值球员；2014-15赛季入选最佳阵容第三阵容；2015-16赛季随骑士队获得NBA总冠军。
    </p>
</body>

</html>
```

在该示例中，在标签选择器img中设置了position:fixed;属性。从效果图中可以看到：图片一直固定在某个位置，当我们拖动滚动条时它的位置仍然保持不变。

在此，小结position:fixed的特点：

- 设置position:fixed后元素会固定定位且不占位置并脱离标准流。
- 设置position:fixed后会将行内元素转化为行内块元素。
- 设置position:fixed后可通过z-index进行层次分级。

### 规避脱标流

有时使用float和position来实现某种效果，但是这很可能导致某些元素脱离标准流(脱标)；所以，应尽可能地避免脱标，可遵守以下原则：

- 网页布局过程中尽量使用标准流布局
- 标准流不能解决的问题优先考虑使用浮动
- 浮动不能解决的问题再考虑使用定位
- 在子元素中使用margin-left:auto 将其置于父元素的最右边
- 在子元素中使用margin-right:auto将其置于父元素的最左边
- 在子元素中使用margin 0 auto;使其在父元素内水平居中显示