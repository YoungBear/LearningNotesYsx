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

## 2. HTML文本标签

### 2.1 b标签

b标签常用于文本加粗，它对应于英文中的bold。

`<b>b标签用于粗体显示文字</b>`

### 2.2 strong标签

strong标签的作用和用法与b标签基本相同，但是在HTML5中为strong标签增加了语义，用其表示重要的文本。

`<strong>strong标签用于粗体显示文本，表示重点内容</strong>`

### 2.3 small标签

small标签用于显示小号字体，比如：版权信息，法律信息，免责声明

`<small>National Basketball Association 2017</small>`

### 2.4 i标签

i标签用于将文本斜体显示，它源于英语单词italic；常用于显示专业词汇，术语，谚语。

`<i>service</i>`

### 2.5 em标签

em标签表示将文本斜体显示，它源于英语单词emphasize.

`<em>这里是考试的重点</em>`

**关于b标签与strong标签的区别，及i标签与em标签的区别：**


b标签和i标签仅仅表示”此处应该用粗体显示”或者”此处应该用斜体显示”，例如，要突出合同的价格那么可以用b标签粗体显示；要表达一句谚语，可以用i标签将其斜体显示。

strong标签和em标签是为了强调内容的重要意义而显示粗体或者斜体；对于搜索引擎，爬虫，SEO而言更受重视。例如，我们将”打倒法西斯！”这句话置于strong标签中；那么，语音阅读器时读到此strong标签就会重读。

概括地来说：b标签和i标签是<font color=red>**物理元素**</font> ；strong标签和em标签是**逻辑元素**。物理元素强调的是一种物理行为。比如说，把一段文字用b标签加粗，意思是告诉浏览器应该加粗显示，没有其他作用；而strong标签不但加粗了字体还起到了强调的作用。同理，i标签和em标签类似，故不再赘述。

### 2.6 u标签

u标签用于表示文本下划线，它源于英文单词underline；请看如下示例：

`<u>u标签标示文本的下划线</u>`

### 2.7 sup标签

sup标签用于表示文本的上标，它是英文单词superscript的缩写；请看如下示例：

`这里是上标<sup>1</sup>`

### 2.8 sub标签

sub标签用于表示文本的下标，它是英文单词subscript的缩写；请看如下示例：

`这里是下标<sub>2</sub>`

### 2.9 span标签

span用于组合文档中的行内元素；它常结合CSS为文本中的某些部分进行特殊处理。说到这里，大家是不是猛然想起来Android里也有类似的东西！比如，要把一部分文字改变颜色，还记得我们在Android里面怎么做的呢？是不是利用SpannableString就可以了？！你瞅瞅，它是不是也是个span呢？所以，这两者是互通的，知道了其中一个，另外一个自然也理解了。

`<span style="color:#FA0">大家好</span><span style="color:#F00">我是谷哥的小弟</span>`

### 2.10 font标签

font标签用于给文本设置文字大小和颜色等属性。示例如下：

`<font color="red" size="15">测试font</font>`

虽然font标签可以给文本设置样式，但是在HTML5中建议不再使用该标签，可采用CSS实现相同的功能。

汇总：

| 序号     | 标签    | 说明    |
| :-----: | :----: | :----: |
| 1       |   b    | 文本加粗 |
| 2       | strong | 文本加粗，强调 |
| 3       | small  | 小号字体 |
| 4       |   i    |   斜体  |
| 5       |   em   | 斜体，强调 |
| 6       |   u    | 文本下划线|
| 7       |  sup   |  上标   |
| 8       |  sub   |  下标   |
| 9       | span   | 文本处理 |
| 10      | font   | 字体处理 |