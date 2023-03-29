---
layout: post
title: new-skill-link!
tags: ["干货"]
description: 不断的学习，越努力越幸福。
---

##预备知识

1. hasattr()&getattr()
    * hasattr(object, name):判断一个对象是否有'name'属性或者'name'方法
    *getattr(object, name[,default]):获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。(如果获得的是方法,则返回的是方法的内存地址,有需要运行则需要加'()')

2. classmethod & staticmethod
    * 待完善

3. future模块&yeild
    * future:Python提供了__future__模块，把下一个新版本的特性导入到当前版本
    * yeild: yield的英文单词意思是生产,若某个函数包含yield，这意味着这个函数已经是一个Generator[深入理解yield](http://www.pythontab.com/html/2015/pythonhexinbiancheng_0415/946.html)

4. python concurrent 模块
    * 因python GIL全局锁的机制,产生了[concurrent](http://www.bubuko.com/infodetail-167068.html)一个实现并发的模块

5. NotImplementedError()异常处理机制
    * NotImplemented 是一个非异常对象，NotImplementedError 是一个异常对象.[参考链接](http://www.tuicool.com/articles/JRb6Zr)
    *[tornado 预定义接口返回异常的好处](https://segmentfault.com/q/1010000005012781) 
    *[tornado Configureable类](https://blog.zorro.im/tornado-configurable/)

6. Synchronous(同步)&Asynchronous(异步)
    *理解概念[链接](http://www.cnblogs.com/anny0404/p/5691379.html)

7. fileno()文件描述符
    *件描述符（File descriptor）是计算机科学中的一个术语，是一个用于表述指向文件的引用的抽象化概念。

    * 文件描述符在形式上是一个非负整数。实际上，它是一个索引值，指向内核为每一个进程所维护的该进程打开文件的记录表。当程序打开一个现有文件或者创建一个新文件时，内核向进程返回一个文件描述符。在程序设计中，一些涉及底层的程序编写往往会围绕着文件描述符展开。但是文件描述符这一概念往往只适用于UNIX、Linux这样的操作系统

8. double ckeck问题
    ```
    if not hasattr(IOLoop, "_instance"):
    with IOLoop._instance_lock:
        if not hasattr(IOLoop, "_instance"):
            # New instance after double check
            IOLoop._instance = IOLoop()
    ```

    * [torndao中单例模式的应用](http://www.jb51.net/article/80363.htm)

9. select、poll、epoll
    * [Linux IO模式及 select、poll、epoll详解](Linux IO模式及 select、poll、epoll详解)