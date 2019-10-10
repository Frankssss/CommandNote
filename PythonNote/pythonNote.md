
# Python Note


+ 逻辑运算符and or 短路原则
	+ 当逻辑运算表达式含有False对象， 逻辑运算结果返回False类型本身
	+ print(True and 2)

+ 内存管理机制
	+ 存储方面
		+ 在python中一切皆对象
		+ 所有对象 都会在内存中开辟一块内存空间存储
			+ 根据不同的类型以及内容 开辟不同的空间大小进行存储
			+ 返回该空间的地址给其他对象引用 用于后续对这个对象的操作
		+ 对于整数和短小的字符， Python会进行缓存，不会创建多个相同对象
		+ 容器对像 存储的其他对象仅仅是其他对象的引用
	+ 垃圾回收方面
		+ 引用计数机制
			+ +1 对象被创建 对象被引用 对象作为参数 对象作为元素在其他容器对象中
			+ -1 对象的别名被显式销毁 对象的别名被赋予新的对象 一个对象离开他的作用域 对象所在的容器被销毁
		+ 垃圾回收机制 处理循环引用  
			+ 找到循环引用
				+ 通过双向链表存储所有容器对象
				+ 用一个变量gc_refs记录每个容器对象的引用计数
				+ 将容器对象内部引用的另一个容器对象的引用计数减1
				+ 最后如果容器对象的引用计数为0 这对象就是循环引用导致的
		+ 提升检测循环引用的性能
			+ 分代回收机制
				+ 默认一个对象被创建后属于0代
				+ 如果经历过一次垃圾回收后依然存活则划分到下一代
				+ 垃圾回收的周期顺序
					+ 0代垃圾回收一定次数，会触发0代和1代回收
					+ 1代垃圾回收一定次数，会触发0代，1代和2代回收 
		+ 垃圾回收触发机制
			+ 垃圾回收器新增的对象个数减去消亡的对象个数 达到一定的阈值才会触发垃圾检测  默认(700, 10, 10)
		+ 手动触发垃圾回收机制 gc.collect()
		+ 避免循环引用 
			+ 使用弱引用 weakref.ref()
			+ 手动破坏循环引用

+ for循环机制 
	+ 判断对象是否为可迭代对象，不是则抛出TypeError异常，否则调用__iter__ 返回一个迭代器
	+ 不断调用迭代器的__next__方法 每次返回一个值
	+ 没有元素则抛出stopIteration, Python语言内部回处理for循环和其他迭代上下文中的StopIteration

+ 同步是指代码调用IO操作时， 必须等待IO操作完成才返回的调用方式
+ 异步是指代码调用IO操作时， 不必等IO操作完成就返回的调用方式
+ 阻塞是指调用函数时候当前线程被挂起，
+ 非组塞是指调用函数时候当前线程不会被挂起， 而是立即返回

+ 一个字符串是一个字符序列
+ 编码：把码位转换成字节序列的过程是编码 encode
+ 解码: 把字节序列转换成码位的过程是解码 decode
	
# classonlymethod 修饰的方法只能被类调用
# classmethod 可以被一个实例或类调用

# 在密码学中，是指通过在密码任意固定位置插入特定的字符串，让散列后的结果和使用原始密码的散列结果不相符，这种过程称之为“加盐”。

# 装饰器实现单例
def singleton(cls):
    _instance = {}
    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner
