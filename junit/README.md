# JUnit 学习笔记

[教程网址](http://wiki.jikexueyuan.com/project/junit/)

JUnit 测试框架具有以下重要特性：

- 测试工具
- 测试套件
- 测试运行器
- 测试分类

## 重要的API

JUnit 中的最重要的程序包是 junit.framework 它包含了所有的核心类。一些重要的类列示如下：

|    序号    |    类名      |    描述    |
|   :----:   |  :----:      |   :----:   |
|     1      |   Assert     |assert 方法的集合|
|     2      |   TestCase   |一个定义了运行多重测试的固定装置|
|     3      | TestResult   |TestResult 集合了执行测试样例的所有结果|
|     4      |  TestSuite   |TestSuite 是测试的集合|

### Assert中的API

方法：

|    序号    |    方法名      |    描述    |
|   :----:   |  :----:      |   :----:   |
|     1      |   void assertEquals(boolean expected, boolean actual)     |检查两个变量或者等式是否平衡|
|     2      |   void assertTrue(boolean expected, boolean actual)   |检查条件为真|
|     3      | void assertFalse(boolean condition)   |检查条件为假|
|     4      |  void assertNotNull(Object object)   |检查对象不为空|
|     5      |  void assertNull(Object object)   |检查对象为空|
|     6      |  void assertSame(boolean condition)   |检查两个相关对象是否指向同一个对象|
|     7      |  void assertNotSame(boolean condition)   |检查两个相关对象是否不指向同一个对象|
|     8      |  void assertArrayEquals(expectedArray, resultArray)   |检查两个数组是否相等|

注解：
|    序号    |    注解名    |    描述    |
|   :----:   |  :----:      |   :----:   |
|     1      |   @Test     |这个注释说明依附在 JUnit 的 public void 方法可以作为一个测试案例。|
|     2      |   @Before     |有些测试在运行前需要创造几个相似的对象。在 public void 方法加该注释是因为该方法需要在 test 方法前运行。|
|     3      |   @After    |如果你将外部资源在 Before 方法中分配，那么你需要在测试运行后释放他们。在 public void 方法加该注释是因为该方法需要在 test 方法后运行。|
|     4      |   @BeforeClass     |在 public void 方法加该注释是因为该方法需要在类中所有方法前运行。|
|     5      |   @AfterClass     |它将会使方法在**所有测试结束**后执行。这个可以用来进行清理活动。|
|     6      |   @Ignore     |这个注释是用来忽略有关不需要执行的测试的。|

JUnit 执行过程：

- @BeforeClass 方法首先执行，并且只执行一次。
- @AfterClass() 方法最后执行，并且只执行一次。
- @Before() 方法针对每一个测试用例执行，但是是在执行测试用例之前。
- @After() 方法针对每一个测试用例执行，但是是在执行测试用例之后。
- 在 @Before() 方法和 @After() 方法之间，执行每一个测试用例。

**注意**：

**@BeforeClass** 和 **@AfterClass** 修饰的方法必须是<font color=red>**静态的**(static)</font>。否则就会报错：

```
java.lang.Exception: Method xxx should be static
```

## 执行测试

测试用例是使用 JUnitCore 类来执行的。JUnitCore 是运行测试的外观类。对于只有一次的测试运行，可以使用静态方法 runClasses(Class[])。

```
package com.example.ysx.asserttest;

import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;


public class TestRunner {
    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(JunitAnnotation.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        System.out.println(result.wasSuccessful());
    }
}
```

## 套件测试

测试套件意味着捆绑几个单元测试用例并且一起执行他们。在 JUnit 中，`@RunWith` 和 `@Suite` 注释用来运行套件测试。

```
package com.example.ysx.suite;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;

@RunWith(Suite.class)
@Suite.SuiteClasses({
   TestJunit1.class,
   TestJunit2.class
})
public class TestSuite {

}
```

TestSuite包含TestJunit1和TestJunit2两个单元测试。

## 忽略测试

```
    @Ignore
    @Test
    public void testPrintMessage2() {
        System.out.println("Inside testPrintMessage2()");
        assertEquals(message, messageUtil.printMessage());
    }
```

标记为@Ignore的测试用例不执行。

## 时间测试

如果一个测试用例比起指定的毫秒数花费了更多的时间，那么 Junit 将自动将它标记为失败。`timeout` 参数和 `@Test` 注释一起使用。

```
    @Test(timeout = 1000)
    public void testPrintMessage() {
        System.out.println("Inside testPrintMessage()");
        messageUtil.printMessage();
    }
```

如果该测试用例执行超过1000毫秒，则判定它为失败。

## 异常测试

Junit 用代码处理提供了一个追踪异常的选项。你可以测试代码是否它抛出了想要得到的异常。expected 参数和 @Test 注释一起使用。


```
    // MessageUtil.java
    public void printMessage() {
        System.out.println(message);
        int a = 0;
        int b = 1 / a;
    }
    
    // TestJunit.java
    @Test(expected = ArithmeticException.class)
    public void testPrintMessage() {
        System.out.println("Inside testPrintMessage()");
        messageUtil.printMessage();
    }
```

即`expected = ArithmeticException.class`表示期望该测试用例可以抛出ArithmeticException。如果实际没有抛出该异常，则判定该测试失败。

## 参数化测试

Junit 4 引入了一个新的功能参数化测试。参数化测试允许开发人员使用不同的值反复运行同一个测试。你将遵循 5 个步骤来创建参数化测试。

- 用 `@RunWith(Parameterized.class)` 来注释 test 类。
- 创建一个由 `@Parameters` 注释的公共的静态方法，它返回一个对象的集合(数组)来作为测试数据集合。
- 创建一个公共的构造函数，它接受和一行测试数据相等同的东西。
- 为每一列测试数据创建一个实例变量。
- 用实例变量作为测试数据的来源来创建你的测试用例。