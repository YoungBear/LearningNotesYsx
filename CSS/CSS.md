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