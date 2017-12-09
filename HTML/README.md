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

**汇总：**

| 序号     | 标签    | 说明    |
| :-----: | :----: | :----: |
| 1       |   p    | 段落 |
| 2       |   h    | 标题，从h1到h6，标题对应的字体越小 |
| 3       |   hr   | 水平横线 |
| 4       |   br   |   换行  |
| 5       |  nobr  | 不换行 |
| 6       | center | 居中显示|
| 7       |marquee | 跑马灯效果 |
| 8       | button |  按钮   |
| 9       |   a    | 超链接  |
| 10      | img    | 图片 |

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

**汇总：**

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

## 3. HTML语义标签

在讲这类标签之前，我们先来聊聊标签的语义化。 

HTML5标签语义化的目的：**让程序员(甚至是非IT人士)能够直观地认识到标签及其属性的用途和作用**。比如，当我们看到h1~h6时就知道：这个标签是用来显示标题的。当然，语义化还有其他非常重要的作用。通过语义化标签可以让爬虫，搜索引擎，SEO读懂我们的页面。比如，我们利用HTML5开发一款新闻朗读软件给盲人朋友用，如果我们把重点内容放入strong标签中，那么该内容会被重读从而突出重点。

### 3.1 blockquote 标签

blockquote用于表示<font color=red>**文本的引用**</font>。引用的文本会在**左、右两侧同时缩进**。

```
<blockquote cite="http://blog.csdn.net/next_second/article/details/78407931">GreenDAO是一个开源的Android端ORM(Object Relational Mapping 对象关系映射)框架，可以让用户使用Java方法来做增删改查等动作。。</blockquote>
```

### 3.2 cite标签

cite标签用于表示文本对某个参考文献的<font color=red>**引用**</font>，比如书籍或者杂志的标题。

```
这段话出自<cite>《java编程思想》</cite>
```

### 3.3 address标签

address标签用于表示<font color=red>**地址**</font>，显示效果通常为斜体。

```
<address>中国四川省成都市高新区</address>
```

### 3.4 code标签

code标签用于表示<font color=red>**计算机代码**</font>。

```
<code>system.out.println()</code>
```

### 3.5 var标签

var标签用于表示<font color=red>**变量**</font>。

```
<var>count</var>
```

### 3.6 dfn标签

dfn标签用于<font color=red>**定义专业术语**</font>，它源于短语defining instance。

```
<dfn>量子网络通信</dfn>
```

### 3.7 del标签

del标签用于表示<font color=red>**删除**</font>，在该标签中的文本会被画一条横线。

```
<del>该方法已经废弃</del>
```

### 3.8 pre标签

pre标签表示<font color=red>**预先的格式化**</font>，它源自于英语单词preformatted，该标签中的空格，回车等格式字符都会被保留。

```
<pre>
        <p>       第一行文字</p>


        <p>第二行文字</p>
</pre>
```

### 3.9 mark标签

mark标签用于<font color=red>**标记文本中的重点内容**</font>，默认采用荧光色标记。

```
<mark>排序算法是我们面试的重点</mark>
```

### 3.10 details和summary标签

details标签用于表示<font color=red>**详细信息**</font>；summary标签常用于表示<font color=red>**摘要信息**</font>；两者常结合起来使用。

```
<details>
    <summary>java编程思想</summary>
    这本书写得非常好，值得一看
</details>
```

**汇总：**

| 序号     | 标签       | 说明    |
| :-----: | :----:    | :----: |
| 1       | blockquote| 文本的引用 |
| 2       | cite      | 文本对某个参考文献的引用 |
| 3       | address   | 地址 |
| 4       |  code     | 计算机代码 |
| 5       |  var      | 变量 |
| 6       |  dfn      | 定义专业术语 defining instance|
| 7       |  del      |  删除 delete   |
| 8       |  pre      |  预先的格式化   |
| 9       | mark      | 标记文本中的重点内容 |
| 10      | details   | 详细信息 |
| 11      | summary   | 摘要信息 |

## 4. HTML 结构便签

我们在HTML页面中常用一些标签将页面划分为不同的区域用以表示页面结构。比如，可使用div标签将整个页面分为header，body，footer三部分。现在我们就来学习这些与页面结构有关的标签。

### 4.1 div标签

div标签在页面中非常常见，也常将其称为<font color=red>**标签容器**</font>。我们可以将一组功能相关的标签放到同一个div中，也可以对该标签内的元素作统一处理，比如设置对齐方式，背景颜色。

```
<div align="center" style="color:#0000FF">
      <p>这是div中一个p标签</p>
      <p>这是div中另外一个p标签</p>
</div>
```

但是，请注意：div标签本身没有任何语义，多用作布局以及样式化或脚本的钩子(hook)。正如，官方文档所言：


```
The div element has no special meaning at all
```

所以，在页面中大量使用div标签导致页面的语义性下降。因此HTML5中引入了新的结构标签article和section。

### 4.2 section标签

先来瞅瞅section标签的文档释义：

```
The section element represents a generic section of a document or application. A section , in this context, is a thematic grouping of content, typically with a heading
```

section不仅仅是一个标签容器，它带有明显的<font color=red>**语义**</font>。该标签常用于对网站或者应用程序中页面上的内容进行分块。比如，网站的主页可以分成简介、新闻和联系方式等几部分，那么每一部分都可以放到一个section里面；类似地，文章的章节、标签对话框中的标签页、或者论文中有编号的部分也可以放到一个section中。请注意：官方文档建议，在使用section时每个section标签中应带一个标题标签(h1-h6)，从而表达更清晰的语义。

### 4.3 article标签

```
The article element represents a self-contained composition in a document, page, application, or site and that is, in principle,independently distributable or reusable, e.g. in syndication.
```

article是一个特殊的section标签，它比section更具有明确的语义。也就是说：无论从结构上还是内容上来说，它代表一个独立的、完整的相关内容块。例如：博客中的一篇文章，论坛中的一个帖子或者一段浏览者的评论等。一般来说，article也有标题部分(通常包含在header内)，类似地它还有footer部分。

```
<article>
        <header><h2>有心课堂课程介绍</h2></header>
        <p>我们需要从每天的复制粘贴，盲目的debug中解放出来，找到解决问题的本质。在有心课堂，我们不仅仅是告诉你需求如何实现，还会教你如何分析，如何选择解决方案以及为什么要这样来实现。有心课堂，初衷是为了引导在职开发人员高效开发，养成良好的思维习惯，而不是简单的教你基础API调用。当然优质的教学体系还需要时下热门的市场需求来做辅助。所以我们在此基础上设计来三套阶梯式课程。</p>
        <section>
            <h3>Android架构设计方法、技巧与实践</h3>
            <p>这里是《Android架构设计方法、技巧与实践》的课程简介</p>
        </section>

        <section>
            <h3>三杆火枪干掉自定义View</h3>
            <p>这里是《三杆火枪干掉自定义View》的课程介绍。目前有1068位同学参加该课程</p>
        </section>

        <footer>课程内容版权均归上海有心网络科技有限公司所有</footer>
    </article>
```