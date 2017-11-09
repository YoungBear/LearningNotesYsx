# Maven 学习笔记

[教程网址](http://wiki.jikexueyuan.com/project/maven/)

## 基本命令

创建工程

```
mvn archetype:generate
```

构建工程

```
mvn clean package
mvn clean compile
```

外部依赖

pom.xml

```
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>3.8.1</version>
      <scope>test</scope>
    </dependency>

    <dependency>
        <groupId>ldapsdk</groupId>
        <artifactId>ldapsdk</artifactId>
        <version>4.1</version>
    </dependency>

  </dependencies>
```

生成工程文档

```
mvn site
```

## 快照

快照是一个特殊的版本，它表示当前开发的一个副本。与常规版本不同，Maven 为每一次构建从远程仓库中检出一份新的快照版本。

**快照 vs 版本**

对于版本，Maven 一旦下载了指定的版本（例如 data-service:1.0），它将不会尝试从仓库里再次下载一个新的 1.0 版本。想要下载新的代码，数据服务版本需要被升级到 1.1。

对于快照，每次用户接口团队构建他们的项目时，Maven 将自动获取最新的快照（data-service:1.0-SNAPSHOT）。

虽然，对于快照，Maven 每次自动获取最新的快照，但你可以在任何 maven 命令中使用 -U 参数强制 maven 下载最新的快照。

```
mvn clean package -U
```

