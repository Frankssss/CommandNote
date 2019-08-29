Java 开发环境搭建 
1.安装JDK
2.配置环境变量
	JAVA_HOME 配置JDK安装路径         path
	PATH 配置JDK命令文件的位置  bin   path
	CLASSPATH 配置类库文件的位置 lib  .;path

java文件  -> 使用javac命令编译器compiler 得到字节码文件  -> 使用解释器interpreter使用java命令 

IDE 集成开发环境 将程序开发环境和程序调试环境集合在一起提升开发效率

变量命名要见名知意

自动类型转换 
1.目标类型要与源类型兼容 如double型能兼容int型 但是char不能兼容int型
2.目标类型大于源类型 如double类型长度为8字节 int类型为4字节，因此double可以存放int类型 反之不行

强制类型转换 double a=1.1; int b=(int) a;  但强制类型转换会造成数据的丢失

常量，它的值被设定后，在程序运行过程中不允许改变

注释  
/**
这里是文档注释
*/
/*
这里是多行注释 
*/
// 这里单行注释 

运算符 
算术运算符 + - * / % ++ --
赋值运算符 = += -= *= /= %= 
比较运算符 < > >= <= == !=
逻辑运算符 && || ! ^
条件运算符 ?:


TBD

Java中泛型的本质
Java中静态变量的使用场景
Java类加载原理及类加载器
Java中对Clone的理解
Java中HashMap的实现
Java中Collections和Collection的区别
Java数组解析
Java代码优化编程
Java事件处理机制与恋爱关系
Java中的JNDI（Java命名与目录接口）
Java中Comparable和Comparator的区别
Java中Heap和Stack的区别
Java中的反射机制 
Java中的synchronized使用
