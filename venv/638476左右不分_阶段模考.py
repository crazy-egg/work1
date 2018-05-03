# 阶段模拟考核（开卷考试）
# 考试目的：
# 巩固及熟悉之前所学知识，注意知识面拓展，重点在查漏补缺。提前接触面试题目。
# 考试时间：
# 2
# 小时内
# 答案提交：
# 在码云上提交，提交格式为
# qq昵称_阶段模考.py
# 注意是py文件
# 最迟上交时间：
# 5
# 月3日
#
# 一、简答题
# 1.
# 列表list_1 = [[1, 2, 3, 4, 5], [{“name”:”张三”, ”age”:28}, {“name”:”James”:”age: 30}]], 获取James的年龄


# list_1=[[1,2,3,4,5],[{"name":"张三","age":28},{"name":"james","age":30}]]
# print("james年龄是：",list_1[1][1]["age"])


# 2.
# 名词解释: 可迭代对象、迭代器、生成器、装饰器
'''
可迭代对象：
       1、list列表、dict字典、tuple元组、set集合、这些都是可以迭代对象
          整数，浮点数，复数都不是可迭代对象
       2、举例
       from collections import Iterable
       print(isinstance([],Iterable))
       返回 True

       from collections import Iterable
       print(isinstance({},Iterable))
       返回 True

       from collections import Iterable
       print(isinstance({"":""},Iterable))
       返回True

       from collections import Iterable
       print(isinstance((),Iterable))
       返回True

       from collections import Iterable
       print(isinstance(1,Iterable))
       返回Flase

迭代器：
       1、元组，列表，字典，数字，集合，都不是迭代器
          x for in range(10)这种类型是迭代器
       2、举例
       from collections import Iterator
       print(isinstance(1,Iterator))
       返回 False

       from collections import Iterator
       print(isinstance([],Iterable))
       返回 False

       from collections import Iterator
       print(isinstance({},Iterable))
       返回 False

       from collections import Iterator
       print(isinstance({"":""},Iterable))
       返回False

       from collections import Iterator
       print(isinstance((),Iterable))
       返回False

生成器：
       g=(x*x for x in range(10))
       for n in g:
            print(n)

装饰器：我们把动态函数叫装饰函数，通过变量调用函数，给对象在运行期间增加的函数
       某个功能，这个就是装饰器的作用

'''






#
# 3.
# 名词解释：面向对象编程中“类”中有几种方法？分别解释各种方法的用途。
'''
具有相同或相似性质的对象的抽象就是类。
类具有属性，它是对象的状态的抽象，用数据结构来描述类的属性。
类具有操作，它是对象的行为的抽象，用操作名和实现该操作的方法来描述。
类的特性：
1、封装：封装是面向对象的特征之一，是对象和类概念的主要特性
2、继承：面向对象编程（OOP）的一个主要功能就是继承。继承是指这样一种能力：
可以使用现有类的所有功能，并在无需重新编写原来类的情况下对这些功能进行扩展。
3、多态：多态性是允许将父对象设置成和一个或更多的子对象相等的技术，赋值之后
父对象就可以根据当前的赋值给它的子对象的特性以不同的方式运作。简单地说，
就是一句话：允许将子类类型运行的指针赋值给父类类型的指针。
'''



# 4.
# 输出以下代码运行结果，解释变量作用域LEGB.
x=2     #全局变量  G
z=3     #全局变量  G
def func_outer():
    y=9    #局部变量   L
    x=0    #局部变量   L
    global z   #申明z为全局变量  G
    def func_inner():
        nonlocal x  #局部变量  L
        x+=5        #局部变量  L
        z=6         #局部变量  L
        print("func_inner",max(x,z),max(x,y))
    z+=3   #函数定义变量
    x+=2   #函数定义变量
    print(x,y,z)
    return  func_inner
func_outer()()
# 5.
# 解释什么是GIL(全局解释器锁)

'''
在python的原始解释器CPython中存在着GIL（Global Interpreter Lock，全局解释器锁），
因此在解释执行python代码时，会产生互斥锁来限制线程对共享资源的访问，
直到解释器遇到I/O操作或者操作次数达到一定数目时才会释放GIL。
所以，虽然CPython的线程库直接封装了系统的原生线程，但CPython整体作为一个进程，
同一时间只会有一个获得GIL的线程在跑，其他线程则处于等待状态。这就造成了即使在多核CPU中，
多线程也只是做着分时切换而已。
不过muiltprocessing的出现，已经可以让多进程的python代码编写简化到了类似多线程的程度了。

'''
# 6.
# 什么是线程、协程、进程
'''
线程，有时被称为轻量级进程(Lightweight Process，LWP），是程序执行流的最小单元。一个标准的线程由线程ID，当前指令指针(PC），
寄存器集合和堆栈组成。另外，线程是进程中的一个实体，是被系统独立调度和分派的基本单位，
线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个进程的
其它线程共享进程所拥有的全部资源。一个线程可以创建和撤消另一个线程，同一进程中的
多个线程之间可以并发执行。由于线程之间的相互制约，致使线程在运行中呈现出间断性。
线程也有就绪、阻塞和运行三种基本状态。就绪状态是指线程具备运行的所有条件，逻辑上可以运行，在等待处理机；
运行状态是指线程占有处理机正在运行；阻塞状态是指线程在等待一个事件（如某个信号量），
逻辑上不可执行。每一个程序都至少有一个线程，若程序只有一个线程，那就是程序本身。
线程是程序中一个单一的顺序控制流程。进程内有一个相对独立的、可调度的执行单元，
是系统独立调度和分派CPU的基本单位指令运行时的程序的调度单位。在单个程序中同时运行多个线程完成不同的工作，称为多线程。
要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，
调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）
复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，
一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，
而子进程只需要调用getppid()就可以拿到父进程的ID。
Python的os模块封装了常见的系统调用，其中就包括fork
'''

# 7.
# 什么时候该用多线程、什么情况该用多进程
'''
一般运行一个程序称为一个进程。
进程可以创建线程，也可以创建进程。
多线程和多进程的区别：线程是由进程管理的，线程之间、
线程和父进程(创建线程的进程)之间可以共享内存变量(需要使用策略的)。
进程之间一般不可以直接共享内存变量，需要使用一些进程间的控制共享内存变量。
如果你使用并行计算，建议使用线程。

'''
# 8.
# 多个进程间如何通信？（注意多进程知识点回顾！！！）
'''
multiprocessing 是一个使用方法类似threading模块的进程模块。
允许程序员做并行开发。并且可以在UNIX和Windows下运行。
通过创建一个Process 类型并且通过调用call()方法spawn一个进程。

'''