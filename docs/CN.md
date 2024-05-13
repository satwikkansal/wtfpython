---
hide:
  - toc
---

<p align="center"><img src="../images/logo.png" alt=""></p>
<h1 align="center">What the f*ck Python! 🐍</h1>
<p align="center">一些有趣且鲜为人知的 Python 特性.</p>

翻译版本: [English](https://github.com/satwikkansal/wtfpython) | [Vietnamese Tiếng Việt](https://github.com/vuduclyunitn/wtfptyhon-vi) | [Spanish Español](https://web.archive.org/web/20220511161045/https://github.com/JoseDeFreitas/wtfpython-es) | [Korean 한국어](https://github.com/buttercrab/wtfpython-ko) | [Russian Русский](https://github.com/frontdevops/wtfpython) | [German Deutsch](https://github.com/BenSt099/wtfpython) | [Add translation](https://github.com/satwikkansal/wtfpython/issues/new?title=Add%20translation%20for%20[LANGUAGE]&body=Expected%20time%20to%20finish:%20[X]%20weeks.%20I%27ll%20start%20working%20on%20it%20from%20[Y].)


其他模式: [Interactive](https://mybinder.org/v2/gh/robertparley/wtfpython-cn/master?labpath=irrelevant%2Fwtf.ipynb) 

[![WTFPL 2.0][license-image]][license-url]   [![Commit id][commit-image]][commit-url] 


Python, 是一个设计优美的解释型高级语言, 它提供了很多能让程序员感到舒适的功能特性. 但有的时候, Python 的一些输出结果对于初学者来说似乎并不是那么一目了然.

这个有趣的项目意在收集 Python 中那些难以理解和反人类直觉的例子以及鲜为人知的功能特性, 并尝试讨论这些现象背后真正的原理!

虽然下面的有些例子并不一定会让你觉得 WTFs, 但它们依然有可能会告诉你一些你所不知道的 Python 有趣特性.  我觉得这是一种学习编程语言内部原理的好办法, 而且我相信你也会从中获得乐趣!

如果您是一位经验比较丰富的 Python 程序员, 你可以尝试挑战看是否能一次就找到例子的正确答案. 你可能对其中的一些例子已经比较熟悉了, 那这也许能唤起你当年踩这些坑时的甜蜜回忆 :sweat_smile:

PS: 如果你不是第一次读了, 你可以在[这里](https://github.com/satwikkansal/wtfpython/releases/)获取变动内容.

那么, 让我们开始吧...

# Table of Contents/目录
<!-- TOC -->

- [Table of Contents/目录](#table-of-contents目录)
- [Structure of the Examples/示例结构](#structure-of-the-examples示例结构)
- [Usage/用法](#usage用法)
- [👀 Examples/示例](#-examples示例)
    - [Section: Strain your brain!/大脑运动!](#section-strain-your-brain大脑运动)
        - [> First things first!/要事优先 *](#-First-things-first!/要事优先-*)
        - [> Strings can be tricky sometimes/微妙的字符串 *](#-strings-can-be-tricky-sometimes微妙的字符串-)
        - [> Be careful with chained operations/小心链式操作](#-be-careful-with-chained-operations小心链式操作)
        - [> How not to use `is` operator/为什么不使用 `is` 操作符](#-How-not-to-use-is-operator/为什么不使用-is-操作符-)
        - [> Hash brownies/是时候来点蛋糕了!](#-Hash-brownies是时候来点蛋糕了)
        - [> Deep down, we're all the same./本质上,我们都一样. *](#-deep-down-were-all-the-same本质上我们都一样-)
        - [> Disorder within order/有序中潜藏着无序 *](#-disorder-within-order/有序中潜藏着无序-*)
        - [> Keep trying.../不停的try *](#-Keep-trying不停的try-)
        - [> For what?/为什么?](#-for-what为什么)
        - [> Evaluation time discrepancy/执行时机差异](#-evaluation-time-discrepancy执行时机差异)
        - [> `is not ...` is not `is (not ...)` / `is not ...` 不是 `is (not ...)`](#-is-not--is-not-is-not-is-not--不是-is-not-)
        - [> A tic-tac-toe where X wins in the first attempt!/一蹴即至!](#-a-tic-tac-toe-where-x-wins-in-the-first-attempt一蹴即至)
        - [> Schrödinger's variable/薛定谔的变量 *](#-Schrödingers-variable薛定谔的变量-)
        - [> The chicken-egg problem/先有鸡还是先有蛋 *](#-the-chicken-egg-problem/先有鸡还是先有蛋-*)
        - [> Subclass relationships/子类关系 *](#-subclass-relationships子类关系-)
        - [> Methods equality and identity/方法的相等性和唯一性 *](#-Methods-equality-and-identity/方法的相等性和唯一性-)
        - [> All-true-ation/返回True的all函数 *](#-All-true-ation/返回True的all函数-)
        - [> The surprising comma/意外的逗号](#-the-surprising-comma意外的逗号)
        - [> Strings and the backslashes/字符串与反斜杠](#-strings-and-the-backslashes字符串与反斜杠)
        - [> not knot!/别纠结!](#-not-knot别纠结)
        - [> Half triple-quoted strings/三个引号](#-half-triple-quoted-strings三个引号)
        - [> What's wrong with booleans?/布尔你咋了?](#-whats-wrong-with-booleans布尔你咋了)
        - [> Class attributes and instance attributes/类属性和实例属性](#-class-attributes-and-instance-attributes类属性和实例属性)
        - [> yielding None/生成 None](#-yielding-none生成-none)
        - [> Yielding from... return!/生成器里的return *](#-Yielding-from-return/生成器里的return-)
        - [> Nan-reflexivity/Nan的自反性](#-Nan-reflexivityNan的自反性)
        - [> Mutating the immutable!/强人所难](#-mutating-the-immutable强人所难)
        - [> The disappearing variable from outer scope/消失的外部变量](#-the-disappearing-variable-from-outer-scope消失的外部变量)
        - [> The mysterious key type conversion/神秘的键型转换 *](#-the-mysterious-key-type-conversion神秘的键型转换-)
        - [> Let's see if you can guess this?/看看你能否猜到这一点?](#-lets-see-if-you-can-guess-this看看你能否猜到这一点)
        - [> Exceeds the limit for integer string conversion/整型转字符串越界](#-exceeds-the-limit-for-integer-string-conversion整型转字符串越界)
    - [Section: Slippery Slopes/滑坡谬误](#section-slippery-slopes滑坡谬误)
        - [> Modifying a dictionary while iterating over it/迭代字典时的修改](#-modifying-a-dictionary-while-iterating-over-it迭代字典时的修改)
        - [> Stubborn `del` operator/坚强的 `del` *](#-stubborn-del-operator坚强的-del-)
        - [> The out of scope variable/外部作用域变量](#-the-out-of-scope-variable外部作用域变量)
        - [> Deleting a list item while iterating/迭代列表时删除元素](#-deleting-a-list-item-while-iterating迭代列表时删除元素)
        - [> Lossy zip of iterators/丢三落四的zip *](#->-Lossy-zip-of-iterators/丢三落四的zip-)
        - [> Loop variables leaking out!/循环变量泄漏!](#-loop-variables-leaking-out循环变量泄漏)
        - [> Beware of default mutable arguments!/当心默认的可变参数!](#-beware-of-default-mutable-arguments当心默认的可变参数)
        - [> Catching the Exceptions/捕获异常](#-catching-the-exceptions捕获异常)
        - [> Same operands, different story!/同人不同命!](#-same-operands-different-story同人不同命)
        - [> Name resolution ignoring class scope/忽略类作用域的名称解析](#-name-resolution-ignoring-class-scope忽略类作用域的名称解析)
        - [> Rounding like a banker/像银行家一样舍入 *](#-rounding-like-a-banker/像银行家一样舍入-)
        - [> Needles in a Haystack/大海捞针](#-needles-in-a-haystack大海捞针)
        - [> Splitsies/分割函数](#-Splitsies分割函数-)
        - [> Wild imports/通配符导入方式 *](#-Wild-imports通配符导入方式-)
        - [> All sorted?/都排序了吗？ *](#-All-sorted都排序了吗-)
        - [> Midnight time doesn't exist?/不存在的午夜?](#-midnight-time-doesnt-exist不存在的午夜)
    - [Section: The Hidden treasures!/隐藏的宝藏!](#section-the-hidden-treasures隐藏的宝藏)
        - [> Okay Python, Can you make me fly?/Python, 可否带我飞? *](#-okay-python-can-you-make-me-flypython-可否带我飞-)
        - [> `goto`, but why?/`goto`, 但为什么? *](#-goto-but-whygoto-但为什么-)
        - [> Brace yourself!/做好思想准备 *](#-brace-yourself做好思想准备-)
        - [> Let's meet Friendly Language Uncle For Life/让生活更友好 *](#-lets-meet-friendly-language-uncle-for-life让生活更友好-)
        - [> Even Python understands that love is complicated/连Python也知道爱是难言的 *](#-even-python-understands-that-love-is-complicated连Python也知道爱是难言的-)
        - [> Yes, it exists!/是的, 它存在!](#-yes-it-exists是的-它存在)
        - [> Ellipsis/省略 *](#-Ellipsis省略-)
        - [> Inpinity/无限 *](#-inpinity无限-)
        - [> Let's mangle/修饰时间! *](#-Lets-mangle修饰时间-)
    - [Section: Appearances are deceptive!/外表是靠不住的!](#section-appearances-are-deceptive外表是靠不住的)
        - [> Skipping lines?/跳过一行?](#-skipping-lines跳过一行)
        - [> Teleportation/空间移动 *](#-teleportation空间移动-)
        - [> Well, something is fishy.../嗯, 有些可疑...](#-well-something-is-fishy嗯有些可疑)
    - [Section: Miscellaneous/杂项](#section-miscellaneous杂项)
        - [> `+=` is faster/更快的 `+=` ](#--is-faster更快的-)
        - [> Let's make a giant string!/来做个巨大的字符串吧!](#-lets-make-a-giant-string来做个巨大的字符串吧)
        - [> Slowing down `dict` lookups/让字典的查找慢下来 *](#-Slowing-down-dict-lookups让字典的查找慢下来-)
        - [> Bloating instance `dict`s/变臃肿的`dict`实例们 *](#-Bloating-instance-dicts/变臃肿的dict实例们-)
        - [> Minor Ones/小知识点](#-minor-ones小知识点)
- [Contributing/贡献](#contributing贡献)
- [Acknowledgements/致谢](#acknowledgements致谢)
- [🎓 License/许可](#-license许可)
    - [Help/帮助](#help帮助)
    - [Surprise your geeky pythonist friends?/想给你的极客朋友一个惊喜?](#surprise-your-geeky-pythonist-friends想给你的极客朋友一个惊喜)
    - [Need a pdf version?/需要来一份pdf版的?](#need-a-pdf-version需要来一份pdf版的)
    - [Follow Commit/追踪Commit](#follow-commit追踪Commit)
    - [996.icu](#996icu)

<!-- /TOC -->

# Structure of the Examples/示例结构

所有示例的结构都如下所示:

> ### > 一个精选的标题 *
> 标题末尾的星号表示该示例在第一版中不存在，是最近添加的.
>
> ```py
> # 准备代码.
> # 释放魔法...
> ```
>
> **Output (Python version):**
> ```py
> >>> 触发语句
> 出乎意料的输出结果
> ```
> (可选): 对意外输出结果的简短描述.
>
>
> #### 💡 说明:
>
> * 简要说明发生了什么以及为什么会发生.
>   ```py
>   如有必要, 举例说明
>   ```
>   **Output:**
>   ```py
>   >>> 触发语句 # 一些让魔法变得容易理解的例子
>   # 一些正常的输入
>   ```

**注意:** 所有的示例都在 Python 3.5.2 版本的交互解释器上测试过, 如果不特别说明应该适用于所有 Python 版本.

# Usage/用法

我个人建议, 最好依次阅读下面的示例, 并对每个示例:
- 仔细阅读设置例子最开始的代码.  如果您是一位经验丰富的 Python 程序员, 那么大多数时候您都能成功预期到后面的结果.
- 阅读输出结果,
  + 确认结果是否如你所料.
  + 确认你是否知道这背后的原理.
    - 如果不知道, 深呼吸然后阅读说明 (如果你还是看不明白, 别沉默! 可以在[这](https://github.com/satwikkansal/wtfPython)提个 issue).
    - 如果知道, 给自己点奖励, 然后去看下一个例子.

PS: 你也可以在命令行阅读 WTFpython. 我们有 pypi 包 和 npm 包(支持代码高亮).(译: 这两个都是英文版的)

安装 npm 包 [`wtfpython`](https://www.npmjs.com/package/wtfpython)
```sh
$ npm install -g wtfpython
```

或者, 安装 pypi 包 [`wtfpython`](https://pypi.python.org/pypi/wtfpython)
```sh
$ pip install wtfpython -U
```

现在, 在命令行中运行 `wtfpython`, 你就可以开始浏览了.

---

# 👀 Examples/示例


## Section: Strain your brain!/大脑运动!

### > First things first!/要事优先 *

<!-- Example ID: d3d73936-3cf1-4632-b5ab-817981338863 -->
<!-- read-only -->

众所周知，Python 3.8 推出"海象"运算符 (`:=`) 方便易用，让我们一起看看。

1\.

```py
# Python 版本 3.8+

>>> a = "wtf_walrus"
>>> a
'wtf_walrus'

>>> a := "wtf_walrus"
File "<stdin>", line 1
    a := "wtf_walrus"
      ^
SyntaxError: invalid syntax

>>> (a := "wtf_walrus") # 该语句有效
'wtf_walrus'
>>> a
'wtf_walrus'
```

2 \.

```py
# Python 版本 3.8+

>>> a = 6, 9
>>> a
(6, 9)

>>> (a := 6, 9)
(6, 9)
>>> a
6

>>> a, b = 6, 9 # 典型拆包操作
>>> a, b
(6, 9)
>>> (a, b = 16, 19) # 出错啦
  File "<stdin>", line 1
    (a, b = 16, 19)
          ^
SyntaxError: invalid syntax

>>> (a, b := 16, 19) # 这里的结果是一个奇怪的三元组
(6, 16, 19)

>>> a # a值仍然没变?
6

>>> b
16
```



#### 💡 说明

**“海象”运算符简介**

海象运算符 (`:=`) 在Python 3.8中被引入，用来在表达式中为变量赋值。

```py
def some_func():
        # 假设这儿有一些耗时的计算
        # time.sleep(1000)
        return 5

# 引入“海象”运算符前的例子
if some_func():
        print(some_func()) # 糟糕的案例——函数运算了两次

# 或者，加以改进：
a = some_func()
if a:
    print(a)

# 有了“海象”运算符，你可以写的更简洁：
if a := some_func():
        print(a)
```

**输出 (> Python 3.8):**

```py
5
5
5
```
这样既减少了一行代码，又避免了两次调用 `some_func` 函数。

- 在顶层的无括号赋值操作（使用“海象”运算符）被限制，因此例1中的 `a := "wtf_walrus"` 出现了 `SyntaxError` 。用括号括起来。它就能正常工作了。

- 一般的，包含 `=` 操作的表达式是不能用括号括起来的，因此 `(a, b = 6, 9)` 中出现了语法错误。

- “海象”运算符的语法形式为：`NAME:= expr`，`NAME` 是一个有效的标识符，而 `expr` 是一个有效的表达式。 因此，这意味着它不支持可迭代的打包和拆包。

  - `(a := 6, 9)` 等价于 `((a := 6), 9)` ，最终得到 `(a, 9) ` (其中 `a` 的值为6)

    ```py
    >>> (a := 6, 9) == ((a := 6), 9)
    True
    >>> x = (a := 696, 9)
    >>> x
    (696, 9)
    >>> x[0] is a # 两个变量指向同一内存空间
    True
    ```

  - 类似的， `(a, b := 16, 19)` 等价于 `(a, (b := 16), 19)` ，只是一个三元组。 


---

### > Strings can be tricky sometimes/微妙的字符串 *

1\.
```py
>>> a = "some_string"
>>> id(a)
140420665652016
>>> id("some" + "_" + "string") # 注意两个的id值是相同的.
140420665652016
```

2\.
```py
>>> a = "wtf"
>>> b = "wtf"
>>> a is b
True

>>> a = "wtf!"
>>> b = "wtf!"
>>> a is b
False

>>> a, b = "wtf!", "wtf!"
>>> a is b 
True # 3.7 版本返回结果为 False.
```

3\.
```py
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False # 3.7 版本返回结果为 True
```

很好理解, 对吧?

#### 💡 说明:
- 这些行为是由于 Cpython 在编译优化时, 某些情况下会尝试使用已经存在的不可变对象而不是每次都创建一个新对象. (这种行为被称作字符串的驻留[string interning])
- 发生驻留之后, 许多变量可能指向内存中的相同字符串对象. (从而节省内存)
- 在上面的代码中, 字符串是隐式驻留的. 何时发生隐式驻留则取决于具体的实现. 这里有一些方法可以用来猜测字符串是否会被驻留:
  - 所有长度为 0 和长度为 1 的字符串都被驻留.
  - 字符串在编译时被实现 (`'wtf'` 将被驻留, 但是 `''.join(['w', 't', 'f'])` 将不会被驻留)
  - 字符串中只包含字母，数字或下划线时将会驻留. 所以 `'wtf!'` 由于包含 `!` 而未被驻留. 可以在[这里](https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19)找到 CPython 对此规则的实现.

    <img src="../images/string-intern/string_intern.png" alt="">

- 当在同一行将 `a` 和 `b` 的值设置为 `"wtf!"` 的时候, Python 解释器会创建一个新对象, 然后同时引用第二个变量(译: 仅适用于3.7以下, 详细情况请看[这里](https://github.com/leisurelicht/wtfpython-cn/issues/13)). 如果你在不同的行上进行赋值操作, 它就不会“知道”已经有一个 `wtf！` 对象 (因为 `"wtf!"` 不是按照上面提到的方式被隐式驻留的). 它是一种编译器优化, 特别适用于交互式环境.
- 常量折叠(constant folding) 是 Python 中的一种 [窥孔优化(peephole optimization)](https://en.wikipedia.org/wiki/Peephole_optimization) 技术. 这意味着在编译时表达式 `'a'*20` 会被替换为 `'aaaaaaaaaaaaaaaaaaaa'` 以减少运行时的时钟周期. 只有长度小于 20 的字符串才会发生常量折叠. (为啥? 想象一下由于表达式 `'a'*10**10` 而生成的 `.pyc` 文件的大小). 相关的源码实现在[这里](https://github.com/python/cpython/blob/3.6/Python/peephole.c#L288).
- 如果你是使用 3.7 版本中运行上述示例代码, 会发现部分代码的运行结果与注释说明相同. 这是因为在 3.7 版本中, 常量折叠已经从窥孔优化器迁移至新的 AST 优化器, 后者可以以更高的一致性来执行优化. (由 Eugene Toder 和 INADA Naoki 在 [bpo-29469](https://bugs.python.org/issue29469) 和 [bpo-11549](https://bugs.python.org/issue11549) 中贡献.) 
- (译: 但是在最新的 3.8 版本中, 结果又变回去了. 虽然 3.8 版本和 3.7 版本一样, 都是使用 AST 优化器. 目前不确定官方对 3.8 版本的 AST 做了什么调整.)


---

### > Be careful with chained operations/小心链式操作

```py
>>> (False == False) in [False] # 可以理解
False
>>> False == (False in [False]) # 可以理解
False
>>> False == False in [False] # 为毛?
True

>>> True is False == False
False
>>> False is False is False
True

>>> 1 > 0 < 1
True
>>> (1 > 0) < 1
False
>>> 1 > (0 < 1)
False
```

#### 💡 说明:

根据 https://docs.python.org/3/reference/expressions.html#comparisons

> 形式上, 如果 a, b, c, ..., y, z 是表达式, 而 op1, op2, ..., opN 是比较运算符, 那么除了每个表达式最多只出现一次以外 a op1 b op2 c ... y opN z 就等于 a op1 b and b op2 c and ... y opN z.

虽然上面的例子似乎很愚蠢, 但是像 `a == b == c` 或 `0 <= x <= 100` 就很棒了.

* `False is False is False` 相当于 `(False is False) and (False is False)`
* `True is False == False` 相当于 `(True is False) and (False == False)`, 由于语句的第一部分 (`True is False`) 等于 `False`, 因此整个表达式的结果为 `False`.
* `1 > 0 < 1` 相当于 `(1 > 0) and (0 < 1)`, 所以最终结果为 `True`.
* 表达式 `(1 > 0) < 1` 相当于 `True < 1` 且
  ```py
  >>> int(True)
  1
  >>> True + 1 # 与这个例子无关，只是娱乐一下
  2
  ```
  所以, `1 < 1` 等于 `False`


---

### > How not to use `is` operator/为什么不使用 `is` 操作符
<!-- Example ID: 230fa2ac-ab36-4ad1-b675-5f5a1c1a6217 --->

下面是一个在互联网上非常有名的例子.

1\.

```py
>>> a = 256
>>> b = 256
>>> a is b
True

>>> a = 257
>>> b = 257
>>> a is b
False
```

2\.

```py
>>> a = []
>>> b = []
>>> a is b
False

>>> a = tuple()
>>> b = tuple()
>>> a is b
True
```

3\.
**Output**

```py
>>> a, b = 257, 257
>>> a is b
True
```

**Output (Python 3.7.x specifically)**

```py
>>> a, b = 257, 257
>>> a is b
False
```

#### 💡 说明:

**`is` 和 `==` 的区别**

* `is` 运算符检查两个运算对象是否引用自同一对象 (即, 它检查两个运算对象是否相同).
* `==` 运算符比较两个运算对象的值是否相等.
* 因此 `is` 代表引用相同, `==` 代表值相等. 下面的例子可以很好的说明这点,
  ```py
  >>> [] == []
  True
  >>> [] is [] # 这两个空列表位于不同的内存地址.
  False
  ```

**`256` 是一个已经存在的对象, 而 `257` 不是**

当你启动Python 的时候, 数值为 `-5` 到 `256` 的对象就已经被分配好了. 这些数字因为经常被使用, 所以会被提前准备好.

Python 通过这种创建小整数池的方式来避免小整数频繁的申请和销毁内存空间.

引用自 https://docs.python.org/3/c-api/long.html
> 当前的实现为-5到256之间的所有整数保留一个整数对象数组, 当你创建了一个该范围内的整数时, 你只需要返回现有对象的引用. 所以改变1的值是有可能的. 我怀疑这种行为在Python中是未定义行为. :-)

```py
>>> id(256)
10922528
>>> a = 256
>>> b = 256
>>> id(a)
10922528
>>> id(b)
10922528
>>> id(257)
140084850247312
>>> x = 257
>>> y = 257
>>> id(x)
140084850247440
>>> id(y)
140084850247344
```

这里解释器并没有智能到能在执行 `y = 257` 时意识到我们已经创建了一个整数 `257`, 所以它在内存中又新建了另一个对象.

类似的优化也适用于其他**不可变**对象，例如空元组。由于列表是可变的，这就是为什么 `[] is []` 将返回 `False` 而 `() is ()` 将返回 `True`。 这解释了我们的第二个代码段。而第三个呢：

**当 `a` 和 `b` 在同一行中使用相同的值初始化时，会指向同一个对象.**

```py
>>> a, b = 257, 257
>>> id(a)
140640774013296
>>> id(b)
140640774013296
>>> a = 257
>>> b = 257
>>> id(a)
140640774013392
>>> id(b)
140640774013488
```

* 当 a 和 b 在同一行中被设置为 `257` 时, Python 解释器会创建一个新对象, 然后同时引用第二个变量. 如果你在不同的行上进行, 它就不会 "知道" 已经存在一个 `257` 对象了.
* 这是一种特别为交互式环境做的编译器优化. 当你在实时解释器中输入两行的时候, 他们会单独编译, 因此也会单独进行优化. 如果你在 `.py` 文件中尝试这个例子, 则不会看到相同的行为, 因为文件是一次性编译的。这种优化不仅限于整数，它也适用于其他不可变数据类型，例如字符串（查看示例“微妙的字符串”）和浮点数，

  ```py
  >>> a, b = 257.0, 257.0
  >>> a is b
  True
  ```

* 为什么这不适用于 Python 3.7？ 大概是因为此类编译器优化是特定于实现的（即可能随版本、操作系统等而变化）。我仍在试图弄清楚导致问题的具体实现更改，您可以查看此 [问题](https://github.com/satwikkansal/wtfpython/issues/100) 以获取更新。


---

### > Hash brownies/是时候来点蛋糕了!
* hash brownie指一种含有大麻成分的蛋糕, 所以这里是句双关
* 这里保留原作者对于标题的翻译
<!-- Example ID: eb17db53-49fd-4b61-85d6-345c5ca213ff --->


1\.
```py
some_dict = {}
some_dict[5.5] = "JavaScript"
some_dict[5.0] = "Ruby"
some_dict[5] = "Python"
```

**Output:**

```py
>>> some_dict[5.5]
"JavaScript"
>>> some_dict[5.0] # "Python" 消除了 "Ruby" 的存在?
"Python"
>>> some_dict[5] 
"Python"

>>> complex_five = 5 + 0j
>>> type(complex_five)
complex
>>> some_dict[complex_five]
"Python"
```

为什么到处都是Python?


#### 💡 说明


* 这个 StackOverflow的 [回答](https://stackoverflow.com/a/32211042/4354153) 漂亮地解释了这背后的基本原理.

* Python 字典中键的唯一性是根据 *等价性*，而不是同一性。 因此，即使 `5`、`5.0` 和 `5 + 0j` 是不同类型的不同对象，由于它们是相等的，它们不能都在同一个 `dict`（或 `set`）中。 只要您插入其中任何一个，尝试查找任何不同但等价的键都将使用原始映射值成功（而不是因“KeyError”而失败）：

  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> 5 is not 5.0 is not 5 + 0j
  True
  >>> some_dict = {}
  >>> some_dict[5.0] = "Ruby"
  >>> 5.0 in some_dict
  True
  >>> (5 in some_dict) and (5 + 0j in some_dict)
  True
  ```

* 这在赋值的时候也会生效。因此，当您执行 `some_dict[5] = "Python"` 时，Python 会找到具有等价键值 `5.0 -> "Ruby"` 的现有项，覆盖其值，并保留原始键值。

  ```py
  >>> some_dict
  {5.0: 'Ruby'}
  >>> some_dict[5] = "Python"
  >>> some_dict
  {5.0: 'Python'}
  ```
* 那么我们如何将键值更新为`5`（而不是`5.0`）？ 我们实际上不能原地更新，但是我们可以先删除键（`del some_dict[5.0]`），然后重新赋值（`some_dict[5]`）得到整数`5` 作为键而不是浮点数 `5.0`，尽管这属于极少数情况。

* Python 是如何在包含 `5.0` 的字典中找到 `5` 的？ Python 只需要花费常数时间，而无需使用哈希函数遍历每一项。当 Python 在 dict 中查找键 `foo` 时，它首先计算 `hash(foo)`（以常数时间运行）。因为在 Python 中，要求相等的对象具有相同的哈希值（此处为[文档](https://docs.python.org/3/reference/datamodel.html#object.__hash__)），`5` 、`5.0` 和 `5 + 0j` 具有相同的哈希值。

  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> hash(5) == hash(5.0) == hash(5 + 0j)
  True
  ```

  **注意：** 反之不一定正确：具有相等哈希值的对象本身可能不相等。（这是[哈希冲突](https://en.wikipedia.org/wiki/Collision_(computer_science)）造成的，这也会降低哈希运算的性能。）


---

### > Deep down, we're all the same./本质上,我们都一样. *

```py
class WTF:
  pass
```

**Output:**
```py
>>> WTF() == WTF() # 两个不同的对象应该不相等
False
>>> WTF() is WTF() # 也不相同
False
>>> hash(WTF()) == hash(WTF()) # 哈希值也应该不同
True
>>> id(WTF()) == id(WTF())
True
```

#### 💡 说明:

* 当调用 `id` 函数时, Python 创建了一个 `WTF` 类的对象并传给 `id` 函数. 然后 `id` 函数获取其id值 (也就是内存地址), 然后丢弃该对象. 该对象就被销毁了.
* 当我们连续两次进行这个操作时, Python会将相同的内存地址分配给第二个对象. 因为 (在CPython中) `id` 函数使用对象的内存地址作为对象的id值, 所以两个对象的id值是相同的.
* 综上, 对象的id值仅仅在对象的生命周期内唯一. 在对象被销毁之后, 或被创建之前, 其他对象可以具有相同的id值.
* 那为什么 `is` 操作的结果为 `False` 呢? 让我们看看这段代码.
  ```py
  class WTF(object):
    def __init__(self): print("I")
    def __del__(self): print("D")
  ```

  **Output:**
  ```py
  >>> WTF() is WTF()
  I
  I
  D
  D
  False
  >>> id(WTF()) == id(WTF())
  I
  D
  I
  D
  True
  ```
  正如你所看到的, 对象销毁的顺序是造成所有不同之处的原因.


---

### > Disorder within order/有序中潜藏着无序 *
<!-- Example ID: 91bff1f8-541d-455a-9de4-6cd8ff00ea66 --->

```py
from collections import OrderedDict

dictionary = dict()
dictionary[1] = 'a'; dictionary[2] = 'b';

ordered_dict = OrderedDict()
ordered_dict[1] = 'a'; ordered_dict[2] = 'b';

another_ordered_dict = OrderedDict()
another_ordered_dict[2] = 'b'; another_ordered_dict[1] = 'a';

class DictWithHash(dict):
    """
    实现了 __hash__ 魔法方法的dict类
    """
    __hash__ = lambda self: 0

class OrderedDictWithHash(OrderedDict):
    """
    实现了 __hash__ 魔法方法的OrderedDict类
    """
    __hash__ = lambda self: 0
```

**Output**
```py
>>> dictionary == ordered_dict # 如果 a == b
True
>>> dictionary == another_ordered_dict # 且 b == c
True
>>> ordered_dict == another_ordered_dict # 那么为什么 c == a 不成立??
False

# 众所周知，set数据结构储存不重复元素，
# 让我们生成以上字典的 set 数据类型，看看会发生什么……

>>> len({dictionary, ordered_dict, another_ordered_dict})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

# dict类没有实现 __hash__ ，出错可以理解，接下来使用我们派生的类。

>>> dictionary = DictWithHash()
>>> dictionary[1] = 'a'; dictionary[2] = 'b';
>>> ordered_dict = OrderedDictWithHash()
>>> ordered_dict[1] = 'a'; ordered_dict[2] = 'b';
>>> another_ordered_dict = OrderedDictWithHash()
>>> another_ordered_dict[2] = 'b'; another_ordered_dict[1] = 'a';
>>> len({dictionary, ordered_dict, another_ordered_dict})
1
>>> len({ordered_dict, another_ordered_dict, dictionary}) # 交换顺序
2
```

到底发生了什么?

#### 💡 说明:

- 等号的传递性没有在 `dictionary`, `ordered_dict` 和 `another_ordered_dict` 之间生效是 `OrderedDict` 类中 `__eq__` 方法的实现方式造成的。根据[文档](https://docs.python.org/3/library/collections.html#ordereddict-objects)以下部分:
  
    > 对于 `OrderedDict` 类之间，相等性的判定是位置敏感的，实现类似于 `list(od1.items())==list(od2.items())`。对于 `OrderedDict` 类与其他 `Mapping` 对象（例如`dict` 类），相等性的判定是非位置敏感的。
- 这是为了任何使用常规 `dict` 类的地方能够直接使用 `OrderedDict` 对象代替。
- 好啦，那为什么改变顺序会影响 `set` 对象生成的长度呢? 答案就是上面说的缺乏等号的传递性。因为 `set` 类是唯一元素的无序集合，元素插入的顺序不应该有影响。但在此例中，确有不同。让我们进一步深入。

    ```py
    >>> some_set = set()
    >>> some_set.add(dictionary) # 涉及的变量是前序片段定义的 mapping 对象
    >>> ordered_dict in some_set
    True
    >>> some_set.add(ordered_dict)
    >>> len(some_set)
    1
    >>> another_ordered_dict in some_set
    True
    >>> some_set.add(another_ordered_dict)
    >>> len(some_set)
    1

    >>> another_set = set()
    >>> another_set.add(ordered_dict)
    >>> another_ordered_dict in another_set
    False
    >>> another_set.add(another_ordered_dict)
    >>> len(another_set)
    2
    >>> dictionary in another_set
    True
    >>> another_set.add(another_ordered_dict)
    >>> len(another_set)
    2
    ```
    因此，不一致性是由于 `another_ordered_dict in another_set` 结果为 `False`。 因为 `ordered_dict` 已经在 `another_set` 中，但如前所述， `ordered_dict == another_ordered_dict` 的结果为 `False`，会在后续再加入 `another_ordered_dict` 到 `another_set` 中。


---

### > Keep trying.../不停的try *
<!-- Example ID: b4349443-e89f-4d25-a109-8616be9d41a --->

```py
def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'

def another_func(): 
    for _ in range(3):
        try:
            continue
        finally:
            print("Finally!")

def one_more_func(): # A gotcha!
    try:
        for i in range(3):
            try:
                1 / i
            except ZeroDivisionError:
                # Let's throw it here and handle it outside for loop
                raise ZeroDivisionError("A trivial divide by zero error")
            finally:
                print("Iteration", i)
                break
    except ZeroDivisionError as e:
        print("Zero division error occurred", e)
```

**Output:**

```py
>>> some_func()
'from_finally'

>>> another_func()
Finally!
Finally!
Finally!

>>> 1 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> one_more_func()
Iteration 0

```

#### 💡 说明:

- 当在 "try...finally" 语句的 `try` 中执行 `return`, `break` 或 `continue` 后, `finally` 子句依然会执行.
- 函数的返回值由最后执行的 `return` 语句决定. 由于 `finally` 子句一定会执行, 所以 `finally` 子句中的 `return` 将始终是最后执行的语句.
- 这里需要注意的是，如果 finally 子句执行 `return` 或 `break` 语句，临时保存的异常将被丢弃。


---

### > For what?/为什么?

```py
some_string = "wtf"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    pass
```

**Output:**
```py
>>> some_dict # 创建了索引字典.
{0: 'w', 1: 't', 2: 'f'}
```

####  💡 说明:

* [Python 语法](https://docs.python.org/3/reference/grammar.html) 中对 `for` 的定义是:
  ```
  for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
  ```
  其中 `exprlist` 指分配目标. 这意味着对可迭代对象中的**每一项都会执行**类似 `{exprlist} = {next_value}` 的操作.

  一个有趣的例子说明了这一点:
  ```py
  for i in range(4):
      print(i)
      i = 10
  ```

  **Output:**
  ```
  0
  1
  2
  3
  ```

  你可曾觉得这个循环只会运行一次?

  **💡 说明:**

  - 由于循环在Python中工作方式, 赋值语句 `i = 10` 并不会影响迭代循环, 在每次迭代开始之前, 迭代器(这里指 `range(4)`) 生成的下一个元素就被解包并赋值给目标列表的变量(这里指 `i`)了.

* 在每一次的迭代中, `enumerate(some_string)` 函数就生成一个新值 `i` (计数器增加) 并从 `some_string` 中获取一个字符. 然后将字典 `some_dict` 键 `i` (刚刚分配的) 的值设为该字符. 本例中循环的展开可以简化为:
  ```py
  >>> i, some_dict[i] = (0, 'w')
  >>> i, some_dict[i] = (1, 't')
  >>> i, some_dict[i] = (2, 'f')
  >>> some_dict
  ```

---

### > Evaluation time discrepancy/执行时机差异

1\.
```py
array = [1, 8, 15]
# 一个典型的生成器表达式
g = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
```

**Output:**
```py
>>> print(list(g)) #其他的值去哪儿了？
[8]
```

2\.

```py
array_1 = [1,2,3,4]
g1 = (x for x in array_1)
array_1 = [1,2,3,4,5]

array_2 = [1,2,3,4]
g2 = (x for x in array_2)
array_2[:] = [1,2,3,4,5]
```

**Output:**
```py
>>> print(list(g1))
[1,2,3,4]

>>> print(list(g2))
[1,2,3,4,5]
```

3\.

```py
array_3 = [1, 2, 3]
array_4 = [10, 20, 30]
gen = (i + j for i in array_3 for j in array_4)

array_3 = [4, 5, 6]
array_4 = [400, 500, 600]
```

**Output:**
```py
>>> print(list(gen))
[401, 501, 601, 402, 502, 602, 403, 503, 603]
```

#### 💡 说明

- 在[生成器](https://wiki.python.org/moin/Generators)表达式中, `in` 子句在声明时执行, 而条件子句则是在运行时执行.
- 所以在运行前, `array` 已经被重新赋值为 `[2, 8, 22]`, 因此对于之前的 `1`, `8` 和 `15`, 只有 `count(8)` 的结果是大于 `0` 的, 所以生成器只会生成 `8`.
- 第二部分中 `g1` 和 `g2` 的输出差异则是由于变量 `array_1` 和 `array_2` 被重新赋值的方式导致的.
- 在第一种情况下, `array_1` 被绑定到新对象 `[1,2,3,4,5]`, 因为 `in` 子句是在声明时被执行的， 所以它仍然引用旧对象 `[1,2,3,4]`(并没有被销毁).
- 在第二种情况下, 对 `array_2` 的切片赋值将相同的旧对象 `[1,2,3,4]` 原地更新为 `[1,2,3,4,5]`. 因此 `g2` 和 `array_2` 仍然引用同一个对象(这个对象现在已经更新为 `[1,2,3,4,5]`).
- 好啦，按照目前讨论的逻辑，第三个代码段中的 `list(gen)` 的值不应该是 `[11, 21, 31, 12, 22, 32, 13, 23, 33]` 吗? （毕竟 `array_3` 和 `array_4` 的行为与 `array_1` 一样）。 [PEP-289](https://www.python.org/dev/peps/pep-0289/#the-details) 中解释了（只有）`array_4` 值更新的原因
     > 只有最外层的 for 表达式会立即计算，其他表达式会延迟到生成器运行。


---

### > `is not ...` is not `is (not ...)`/`is not ...` 不是 `is (not ...)`

```py
>>> 'something' is not None
True
>>> 'something' is (not None)
False
```

#### 💡 说明:

- `is not` 是个单独的二元运算符, 与分别使用 `is` 和 `not` 不同.
-  如果操作符两侧的变量指向同一个对象, 则 `is not` 的结果为 `False`, 否则结果为 `True`.


---

### > A tic-tac-toe where X wins in the first attempt!/一蹴即至!

```py
# 我们先初始化一个变量row
row = [""]*3 #row i['', '', '']
# 并创建一个变量board
board = [row]*3
```

**Output:**
```py
>>> board
[['', '', ''], ['', '', ''], ['', '', '']]
>>> board[0]
['', '', '']
>>> board[0][0]
''
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['X', '', ''], ['X', '', '']]
```

我们有没有赋值过3个 "X" 呢？

#### 💡 说明:

当我们初始化 `row` 变量时, 下面这张图展示了内存中的情况。

![image](../images/tic-tac-toe/after_row_initialized.png)

而当通过对 `row` 做乘法来初始化 `board` 时, 内存中的情况则如下图所示 (每个元素 `board[0]`, `board[1]` 和 `board[2]` 都和 `row` 一样引用了同一列表.)

![image](../images/tic-tac-toe/after_board_initialized.png)

我们可以通过不使用变量 `row` 生成 `board` 来避免这种情况. ([这个](https://github.com/satwikkansal/wtfpython/issues/68)issue提出了这个需求.)

```py
>>> board = [['']*3 for _ in range(3)]
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['', '', ''], ['', '', '']]
```

---

### > Schrödinger's variable/薛定谔的变量 *
<!-- Example ID: 4dc42f77-94cb-4eb5-a120-8203d3ed7604 --->

```py
funcs = []
results = []
for x in range(7):
    def some_func():
        return x
    funcs.append(some_func)
    results.append(some_func()) # 注意这里函数被执行了

funcs_results = [func() for func in funcs]
```

**Output:**
```py
>>> results
[0, 1, 2, 3, 4, 5, 6]
>>> funcs_results
[6, 6, 6, 6, 6, 6, 6]
```

即使每次在迭代中将 `some_func` 加入 `funcs` 前的 `x` 值都不相同, 所有的函数还是都返回6.

// 再换个例子

```py
>>> powers_of_x = [lambda x: x**i for i in range(10)]
>>> [f(2) for f in powers_of_x]
[512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
```

#### 💡 说明:

- 当在循环内部定义一个函数时, 如果该函数在其主体中使用了循环变量, 则闭包函数将与循环变量绑定, 而不是它的值. 因此, 所有的函数都是使用最后分配给变量的值来进行计算的.

- 可以通过将循环变量作为命名变量传递给函数来获得预期的结果. **为什么这样可行?** 因为这会在函数内再次定义一个局部变量。我们可以看到它使用了来自上下文的`x`（即*不是*局部变量）：
（译者注: inspect位于Python标准库中，该模块用于收集python对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等等，Python3.3+版本支持getclosurevars函数）
```py
>>> import inspect
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={'x': 6}, builtins={}, unbound=set())
```

由于 `x` 是一个全局值，我们可以通过更新 `x` 来更改 `funcs` 用来查找和返回的值：

```py
>>> x = 42
>>> [func() for func in funcs]
[42, 42, 42, 42, 42, 42, 42]
```

* 要获得想要的结果，您可以将循环变量作为命名变量传递给函数。 **为什么会这样？** 因为这会在函数的作用域内定义变量。 它将不再进入周围（全局）范围来查找变量值，而是会创建一个局部变量来存储该时间点的“x”值。

```py
funcs = []
for x in range(7):
    def some_func(x=x):
        return x
    funcs.append(some_func)
```

**Output:**
```py
>>> funcs_results = [func() for func in funcs]
>>> funcs_results
[0, 1, 2, 3, 4, 5, 6]
```

此时，不再使用全局变量 `x`：

```py
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={}, builtins={}, unbound=set())
```


---

### > The chicken-egg problem/先有鸡还是先有蛋 *
<!-- Example ID: 60730dc2-0d79-4416-8568-2a63323b3ce8 --->

1\.
```py
>>> isinstance(3, int)
True
>>> isinstance(type, object)
True
>>> isinstance(object, type)
True
```
那么到底谁是“最终”的基类呢？下边顺便列出更多的令人困惑的地方

2\. 

```py
>>> class A: pass
>>> isinstance(A, A)
False
>>> isinstance(type, type)
True
>>> isinstance(object, object)
True
```

3\.

```py
>>> issubclass(int, object)
True
>>> issubclass(type, object)
True
>>> issubclass(object, type)
False
```


#### 💡 说明

- `type` 是 Python 中的[元类](https://realpython.com/python-metaclasses/)。
- Python 中，**一切**皆对象，其中包括类及其对象（实例）。
- `type` 类型是`object`类的元类，每个类（包括`type`）都直接或间接地继承自`object`。
- 对象和类型之间没有真正的基类。上述片段中的令人困惑的地方之所以出现，是因为我们从 Python 类的角度考虑这些关系（issubclass 和 isinstance）。 `object`和`type`之间的关系不能在纯python中重现。 更准确地说，以下关系不能在纯 Python 中重现:
    + A类是B类的一个实例，B类是A类的一个实例。
    + A类是它自己的一个实例。
- `object`和`type`之间的关系（既是彼此的实例，也是它们自己的实例）存在于 Python 中，这是源于实现层级上的“作弊”行为。


---

### > Subclass relationships/子类关系 *

**Output:**
```py
>>> from collections.abc import Hashable
>>> issubclass(list, object)
True
>>> issubclass(object, Hashable)
True
>>> issubclass(list, Hashable)
False
```

子类关系应该是可传递的, 对吧? (即, 如果 `A` 是 `B` 的子类, `B` 是 `C` 的子类, 那么 `A` _应该_ 是 `C` 的子类.)

#### 💡 说明:

* Python 中的子类关系并不一定是传递的. 任何人都可以在元类中随意定义 `__subclasscheck__`.
* 当 `issubclass(cls, Hashable)` 被调用时, 它只是在 `cls` 中寻找 `__hash__` 方法或者从继承的父类中寻找 `__hash__` 方法.
* 由于 `object` is 可散列的(hashable), 但是 `list` 是不可散列的, 所以它打破了这种传递关系.
* 在[这里](https://www.naftaliharris.com/blog/python-subclass-intransitivity/)可以找到更详细的解释.

---

### > Methods equality and identity/方法的相等性和唯一性 *
<!-- Example ID: 94802911-48fe-4242-defa-728ae893fa32 --->

1.
```py
class SomeClass:
    def method(self):
        pass

    @classmethod
    def classm(cls):
        pass

    @staticmethod
    def staticm():
        pass
```

**Output:**
```py
>>> print(SomeClass.method is SomeClass.method)
True
>>> print(SomeClass.classm is SomeClass.classm)
False
>>> print(SomeClass.classm == SomeClass.classm)
True
>>> print(SomeClass.staticm is SomeClass.staticm)
True
```
访问 `classm` 两次，我们得到一个相等的对象，但不是*同一个*？ 让我们看看 `SomeClass` 的实例会发生什么：

2.
```py
o1 = SomeClass()
o2 = SomeClass()
```

**Output:**
```py
>>> print(o1.method == o2.method)
False
>>> print(o1.method == o1.method)
True
>>> print(o1.method is o1.method)
False
>>> print(o1.classm is o1.classm)
False
>>> print(o1.classm == o1.classm == o2.classm == SomeClass.classm)
True
>>> print(o1.staticm is o1.staticm is o2.staticm is SomeClass.staticm)
True
```

访问 ` classm` or `method` 两次, 为 `SomeClass` 的同一个实例创建了相等但是*不同*的对象。

#### 💡 说明
* 函数是[描述符](https://docs.python.org/3/howto/descriptor.html)。每当将函数作为属性访问时，就会调用描述符，创建一个方法对象，该对象将函数与拥有该属性的对象“绑定”。如果被调用，该方法调用函数，隐式传递绑定对象作为第一个参数（这就是我们如何将 self 作为第一个参数获取，尽管没有显式传递它）。

```py
>>> o1.method
<bound method SomeClass.method of <__main__.SomeClass object at ...>>
```

* 多次访问该属性，每次都会创建一个方法对象！ 因此，`o1.method is o1.method` 永远不会是真的。但是，将函数作为类属性（而不是实例）访问并不会创建方法对象，所以 `SomeClass.method is SomeClass.method` 是真的。

```py
>>> SomeClass.method
<function SomeClass.method at ...>
```

* `classmethod` 将函数转换为类方法。 类方法是描述符，当被访问时，它会创建一个绑定*类本身*的方法对象，而不是对象本身。

```py
>>> o1.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```

* 与函数不同，`classmethod` 在作为类属性访问时也会创建一个方法（在这种情况下，它们绑定类，而不是类的类型）。 所以 `SomeClass.classm is SomeClass.classm` 是假的。

```py
>>> SomeClass.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```

* 当两个函数相等并且绑定的对象相同时，方法对象比较相等。 所以`o1.method == o1.method` 为真，尽管它们在内存中是两个不同的对象。
* `staticmethod` 将函数转换为“无操作”描述符，它按原样返回函数。没有方法对象被创建，所以 `is` 的比较运算为真。

```py
>>> o1.staticm
<function SomeClass.staticm at ...>
>>> SomeClass.staticm
<function SomeClass.staticm at ...>
```

* 每次 Python 调用实例方法时都必须创建新的“方法”对象，并且每次都必须修改参数以插入 `self` 严重影响性能。CPython 3.7 [解决了这个问题](https://bugs.python.org/issue26110) 。通过引入新的操作码来处理调用方法而不创建临时方法对象。这仅在实际调用访问的函数时使用，因此这里的代码片段不受影响，仍然会生成方法:)


---

### > All-true-ation/返回True的all函数 *

<!-- Example ID: dfe6d845-e452-48fe-a2da-0ed3869a8042 -->

```py
>>> all([True, True, True])
True
>>> all([True, True, False])
False

>>> all([])
True
>>> all([[]])
False
>>> all([[[]]])
True
```

为什么会有这种True-False的变化？

#### 💡 说明

- `all` 函数的实现等价于：

- ```py
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

- `all([])` 返回 `True` 因为可迭代对象为空。 
- `all([[]])` 返回 `False` 因为传入的数组有一个元素 `[]`， 在Python中，空列表为假。
- `all([[[]]])` 和更高的递归变体总是`True`。 这是因为传递的数组的单个元素（`[[...]]`）不再是空的，而有值的列表为真。


---

### > The surprising comma/意外的逗号

**Output:**
```py
>>> def f(x, y,):
...     print(x, y)
...
>>> def g(x=4, y=5,):
...     print(x, y)
...
>>> def h(x, **kwargs,):
  File "<stdin>", line 1
    def h(x, **kwargs,):
                     ^
SyntaxError: invalid syntax
>>> def h(*args,):
  File "<stdin>", line 1
    def h(*args,):
                ^
SyntaxError: invalid syntax
```

#### 💡 说明:

- 在Python函数的形式参数列表中, 尾随逗号并不一定是合法的.
- 在Python中, 参数列表部分用前置逗号定义, 部分用尾随逗号定义. 这种冲突导致逗号被夹在中间, 没有规则定义它.(译:这一句看得我也很懵逼,只能强翻了.详细解释看下面的讨论帖会一目了然.)
- **注意:** 尾随逗号的问题已经在Python 3.6中被[修复](https://bugs.python.org/issue9232)了. 而这篇[帖子](https://bugs.python.org/issue9232#msg248399)中则简要讨论了Python中尾随逗号的不同用法.
---

### > Strings and the backslashes/字符串与反斜杠
<!-- Example ID: 6ae622c3-6d99-4041-9b33-507bd1a4407b --->

**Output:**
```py
>>> print("\"")
"

>>> print(r"\"")
\"

>>> print(r"\")
File "<stdin>", line 1
    print(r"\")
              ^
SyntaxError: EOL while scanning string literal

>>> r'\'' == "\\'"
True
```

#### 💡 说明:

- 在一般的python字符串中，反斜杠用于转义可能具有特殊含义的字符（如单引号、双引号和反斜杠本身）。

    ```py
    >>> "wt\"f"
    'wt"f'
    ```

- 在以 `r` 开头的原始字符串中, 反斜杠并没有特殊含义.
    ```py
    >>> r'wt\"f' == 'wt\\"f'
    True
    >>> print(repr(r'wt\"f')
    'wt\\"f'

    >>> print("\n")

    >>> print(r"\\n")
    '\\n'
    ```

- 这意味着当解析器在原始字符串中遇到反斜杠时，它期望后面有另一个字符。 在我们的例子中（`print(r"\")`），反斜杠转义了尾随引号，使解析器没有终止引号（因此产生了`SyntaxError`）。 这就是为什么反斜杠在原始字符串末尾不起作用的原因。


---

### > not knot!/别纠结!

```py
x = True
y = False
```

**Output:**
```py
>>> not x == y
True
>>> x == not y
  File "<input>", line 1
    x == not y
           ^
SyntaxError: invalid syntax
```

#### 💡 说明:

* 运算符的优先级会影响表达式的求值顺序, 而在 Python 中 `==` 运算符的优先级要高于 `not` 运算符.
* 所以 `not x == y` 相当于 `not (x == y)`, 同时等价于 `not (True == False)`, 最后的运算结果就是 `True`.
* 之所以 `x == not y` 会抛一个 `SyntaxError` 异常, 是因为它会被认为等价于 `(x == not) y`, 而不是你一开始期望的 `x == (not y)`.
* 解释器期望 `not` 标记是 `not in` 操作符的一部分 (因为 `==` 和 `not in` 操作符具有相同的优先级), 但是它在 `not` 标记后面找不到 `in` 标记, 所以会抛出 `SyntaxError` 异常.

---

### > Half triple-quoted strings/三个引号

**Output:**
```py
>>> print('wtfpython''')
wtfpython
>>> print("wtfpython""")
wtfpython
>>> # 下面的语句会抛出 `SyntaxError` 异常
>>> # print('''wtfpython')
>>> # print("""wtfpython")
```

#### 💡 说明:
+ Python 提供隐式的[字符串连接](https://docs.python.org/2/reference/lexical_analysis.html#string-literal-concatenation), 例如,
  ```
  >>> print("wtf" "python")
  wtfpython
  >>> print("wtf" "") # or "wtf"""
  wtf
  ```
+ `'''` 和 `"""` 在 Python中也是字符串定界符, Python 解释器在先遇到三个引号的的时候会尝试再寻找三个终止引号作为定界符, 如果不存在则会导致 `SyntaxError` 异常.


---

### > What's wrong with booleans?/布尔你咋了?

1\.
```py
# 一个简单的例子, 统计下面可迭代对象中的布尔型值的个数和整型值的个数
mixed_list = [False, 1.0, "some_string", 3, True, [], False]
integers_found_so_far = 0
booleans_found_so_far = 0

for item in mixed_list:
    if isinstance(item, int):
        integers_found_so_far += 1
    elif isinstance(item, bool):
        booleans_found_so_far += 1
```

**Output:**
```py
>>> integers_found_so_far
4
>>> booleans_found_so_far
0
```

2\.
```py
>>> some_bool = True
>>> "wtf" * some_bool
'wtf'
>>> some_bool = False
>>> "wtf" * some_bool
''
```

3\.
```py
def tell_truth():
    True = False
    if True == False:
        print("I have lost faith in truth!")
```

**Output (< 3.x):**

```py
>>> tell_truth()
I have lost faith in truth!
```


#### 💡 说明:

* 布尔值是 `int` 的子类
    ```py
    >>> issubclass(bool, int)
    True
    >>> issubclass(int, bool)
    False
    ```

* 因此，`True` 和 `False` 是 `int` 的实例
  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

*  `True` 的整数值是 `1`, 而 `False` 的整数值是 `0`

  ```py
  >>> int(True)
  1
  >>> int(False)
  0
  ```

* 关于其背后的原理, 请看这个 StackOverflow 的[回答](https://stackoverflow.com/a/8169049/4354153).

* 最初，Python 没有 `bool` 类型（人们使用 0 表示假，使用非零值，如 1 表示真）。`True`、`False` 和 `bool` 类型在 2.x 版本中被添加，但为了向后兼容，`True` 和 `False` 不能成为常量。它们只是内置变量，可以重新分配它们

* Python 3 向后不兼容，问题终于得到解决，因此最后一个代码段不适用于 Python 3.x！


---

### > Class attributes and instance attributes/类属性和实例属性

1\.
```py
class A:
    x = 1

class B(A):
    pass

class C(A):
    pass
```

**Output:**
```py
>>> A.x, B.x, C.x
(1, 1, 1)
>>> B.x = 2
>>> A.x, B.x, C.x
(1, 2, 1)
>>> A.x = 3
>>> A.x, B.x, C.x
(3, 2, 3)
>>> a = A()
>>> a.x, A.x
(3, 3)
>>> a.x += 1
>>> a.x, A.x
(4, 3)
```

2\.
```py
class SomeClass:
    some_var = 15
    some_list = [5]
    another_list = [5]
    def __init__(self, x):
        self.some_var = x + 1
        self.some_list = self.some_list + [x]
        self.another_list += [x]
```

**Output:**

```py
>>> some_obj = SomeClass(420)
>>> some_obj.some_list
[5, 420]
>>> some_obj.another_list
[5, 420]
>>> another_obj = SomeClass(111)
>>> another_obj.some_list
[5, 111]
>>> another_obj.another_list
[5, 420, 111]
>>> another_obj.another_list is SomeClass.another_list
True
>>> another_obj.another_list is some_obj.another_list
True
```

#### 💡 说明:

* 类变量和实例变量在内部是通过类对象的字典来处理(译: 就是 `__dict__` 属性). 如果在当前类的字典中找不到的话就去它的父类中寻找.
* `+=` 运算符会在原地修改可变对象, 而不是创建新对象. 因此, 在这种情况下, 修改一个实例的属性会影响其他实例和类属性.

---

### > yielding None/生成 None

```py
some_iterable = ('a', 'b')

def some_func(val):
    return "something"
```

**Output:**
```py
>>> [x for x in some_iterable]
['a', 'b']
>>> [(yield x) for x in some_iterable]
<generator object <listcomp> at 0x7f70b0a4ad58>
>>> list([(yield x) for x in some_iterable])
['a', 'b']
>>> list((yield x) for x in some_iterable)
['a', None, 'b', None]
>>> list(some_func((yield x)) for x in some_iterable)
['a', 'something', 'b', 'something']
```

#### 💡 说明:
- 来源和解释可以在这里找到: https://stackoverflow.com/questions/32139885/yield-in-list-comprehensions-and-generator-expressions
- 相关错误报告: http://bugs.python.org/issue10544
- 这个bug在3.7以后的版本中不被推荐使用, 并在3.8中被修复. 因此在3.8中尝试在推导式中使用 yield, 只会得到一个 SyntaxError. 详细内容可以看[3.7更新内容](https://docs.python.org/dev/whatsnew/3.7.html#deprecated-python-behavior), [3.8更新内容](https://docs.python.org/dev/whatsnew/3.8.html#changes-in-python-behavior).


---

### > Yielding from... return!/生成器里的return *
<!-- Example ID: 5626d8ef-8802-49c2-adbc-7cda5c550816 --->
1\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        yield from range(x)
```

**Output (> 3.3):**

```py
>>> list(some_func(3))
[]
```

`"wtf"` 去哪儿了？是因为`yield from`的一些特殊效果吗？让我们验证一下

2\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        for i in range(x):
          yield i
```

**Output:**

```py
>>> list(some_func(3))
[]
```

同样的结果，这里也不起作用。

#### 💡 说明

+ 从 Python 3.3 开始，可以在生成器中使用带有值的 `return` 语句（参见 [PEP380](https://www.python.org/dev/peps/pep-0380/)）。 [官方文档](https://www.python.org/dev/peps/pep-0380/#enhancements-to-stopiteration) 描述，

> "... 生成器中的 `return expr` 会导致在退出生成器时引发 `StopIteration(expr)`。"

+ 在 `some_func(3)` 例子中，`return` 语句在开始就引发了`StopIteration`。 `StopIteration` 异常会在`list(...)` 包装器和`for` 循环中自动捕获。 因此，以上两个片段都产生的是一个空列表。

+ 要从生成器 `some_func` 中获取 `["wtf"]`，我们需要捕获 `StopIteration` 异常，

    ```py
    try:
        next(some_func(3))
    except StopIteration as e:
        some_string = e.value
    ```

    ```py
    >>> some_string
    ["wtf"]
    ```


---

### > Nan-reflexivity/Nan的自反性
<!-- Example ID: 59bee91a-36e0-47a4-8c7d-aa89bf1d3976 --->

1\.
```py
a = float('inf')
b = float('nan')
c = float('-iNf')  # 这些字符串不区分大小写
d = float('nan')
```

**Output:**
```py
>>> a
inf
>>> b
nan
>>> c
-inf
>>> float('some_other_string')
ValueError: could not convert string to float: some_other_string
>>> a == -c #inf==inf
True
>>> None == None # None==None
True
>>> b == d #但是 nan!=nan
False
>>> 50/a
0.0
>>> a/a
nan
>>> 23 + b
nan
```

2\.

```py
>>> x = float('nan')
>>> y = x / x
>>> y is y # 同一性(identity)具备
True
>>> y == y # y不具备相等性(equality)
False
>>> [y] == [y] # 但包含y的列表验证相等性(equality)成功了
True
```

#### 💡 说明:

`'inf'` 和 `'nan'` 是特殊的字符串(不区分大小写), 当显示转换成 `float` 型时, 它们分别用于表示数学意义上的 "无穷大" 和 "非数字".
- 由于根据 IEEE 标准 `NaN != NaN`，遵守此规则打破了 Python 中集合元素的自反性假设，即如果 `x` 是 `list` 等集合的一部分，则比较等运算的实现基于假设`x == x`。由于这个假设，在比较两个元素时首先比较身份`identity`（因为它更快），并且仅在身份不匹配时才比较值。以下片段将更清楚地说明，

  ```py
  >>> x = float('nan')
  >>> x == x, [x] == [x]
  (False, True)
  >>> y = float('nan')
  >>> y == y, [y] == [y]
  (False, True)
  >>> x == y, [x] == [y]
  (False, False)
  ```

  由于 `x` 和 `y` 的身份`identity`不同，所以考虑的值也不同； 因此这次比较返回“False”。


- 感兴趣可以阅读 [Reflexivity, and other pillars of civilization](https://bertrandmeyer.com/2010/02/06/reflexivity-and-other-pillars-of-civilization/)


---

### > Mutating the immutable!/强人所难

```py
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
```

**Output:**
```py
>>> some_tuple[2] = "change this"
TypeError: 'tuple' object does not support item assignment
>>> another_tuple[2].append(1000) # 这里不出现错误
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000])
>>> another_tuple[2] += [99, 999]
TypeError: 'tuple' object does not support item assignment
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000, 99, 999])
```

我还以为元组是不可变的呢...

#### 💡 说明:

* 引用 https://docs.python.org/2/reference/datamodel.html

    > 不可变序列
        不可变序列的对象一旦创建就不能再改变. (如果对象包含对其他对象的引用，则这些其他对象可能是可变的并且可能会被修改; 但是，由不可变对象直接引用的对象集合不能更改.)

* `+=` 操作符在原地修改了列表. 元素赋值操作并不工作, 但是当异常抛出时, 元素已经在原地被修改了.

(译: 对于不可变对象, 这里指tuple, `+=` 并不是原子操作, 而是 `extend` 和 `=` 两个动作, 这里 `=` 操作虽然会抛出异常, 但 `extend` 操作已经修改成功了. 详细解释可以看[这里](https://segmentfault.com/a/1190000010767068))

---

### > The disappearing variable from outer scope/消失的外部变量

```py
e = 7
try:
    raise Exception()
except Exception as e:
    pass
```

**Output (Python 2.x):**
```py
>>> print(e)
# prints nothing
```

**Output (Python 3.x):**
```py
>>> print(e)
NameError: name 'e' is not defined
```

#### 💡 说明:

* 出处: https://docs.python.org/3/reference/compound_stmts.html#except

  当使用 `as` 为目标分配异常的时候, 将在except子句的末尾清除该异常.

  这就好像

  ```py
  except E as N:
      foo
  ```

  会被翻译成

  ```py
  except E as N:
      try:
          foo
      finally:
          del N
  ```

  这意味着异常必须在被赋值给其他变量才能在 `except` 子句之后引用它. 而异常之所以会被清除, 则是由于上面附加的回溯信息(trackback)会和栈帧(stack frame)形成循环引用, 使得该栈帧中的所有本地变量在下一次垃圾回收发生之前都处于活动状态.(译: 也就是说不会被回收)

* 子句在 Python 中并没有独立的作用域. 示例中的所有内容都处于同一作用域内, 所以变量 `e` 会由于执行了 `except` 子句而被删除. 而对于有独立的内部作用域的函数来说情况就不一样了. 下面的例子说明了这一点:

     ```py
     def f(x):
         del(x)
         print(x)

     x = 5
     y = [5, 4, 3]
     ```

     **Output:**
     ```py
     >>>f(x)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>>f(y)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>> x
     5
     >>> y
     [5, 4, 3]
     ```

* 在 Python 2.x 中, `Exception()` 实例被赋值给了变量 `e`, 所以当你尝试打印结果的时候, 它的输出为空.（译: 正常的Exception实例打印出来就是空）

    **Output (Python 2.x):**
    ```py
    >>> e
    Exception()
    >>> print e
    # 没有打印任何内容!
    ```


---

### > The mysterious key type conversion/神秘的键型转换 *

```py
class SomeClass(str):
    pass

some_dict = {'s':42}
```

**Output:**
```py
>>> type(list(some_dict.keys())[0])
str
>>> s = SomeClass('s')
>>> some_dict[s] = 40
>>> some_dict # 预期: 两个不同的键值对
{'s': 40}
>>> type(list(some_dict.keys())[0])
str
```

#### 💡 说明:

* 由于 `SomeClass` 会从 `str` 自动继承 `__hash__` 方法, 所以 `s` 对象和 `"s"` 字符串的哈希值是相同的.
* 而 `SomeClass("s") == "s"` 为 `True` 是因为 `SomeClass` 也继承了 `str` 类 `__eq__` 方法.
* 由于两者的哈希值相同且相等, 所以它们在字典中表示相同的键.
* 如果想要实现期望的功能, 我们可以重定义 `SomeClass` 的 `__eq__` 方法.
  ```py
  class SomeClass(str):
    def __eq__(self, other):
        return (
            type(self) is SomeClass
            and type(other) is SomeClass
            and super().__eq__(other)
        )

    # 当我们自定义 __eq__ 方法时, Python 不会再自动继承 __hash__ 方法
    # 所以我们也需要定义它
    __hash__ = str.__hash__

  some_dict = {'s':42}
  ```

  **Output:**
  ```py
  >>> s = SomeClass('s')
  >>> some_dict[s] = 40
  >>> some_dict
  {'s': 40, 's': 42}
  >>> keys = list(some_dict.keys())
  >>> type(keys[0]), type(keys[1])
  (__main__.SomeClass, str)
  ```

---

### > Let's see if you can guess this?/看看你能否猜到这一点?

```py
a, b = a[b] = {}, 5
```

**Output:**
```py
>>> a
{5: ({...}, 5)}
```

#### 💡 说明:

* 根据 [Python 语言参考](https://docs.python.org/2/reference/simple_stmts.html#assignment-statements), 赋值语句的形式如下
  ```
  (target_list "=")+ (expression_list | yield_expression)
  ```

  > 赋值语句计算表达式列表(expression list)(牢记 这可以是单个表达式或以逗号分隔的列表, 后者返回元组)并将单个结果对象从左到右分配给目标列表中的每一项.

*  `(target_list "=")+` 中的 `+` 意味着可以有**一个或多个**目标列表. 在这个例子中, 目标列表是 `a, b` 和 `a[b]` (注意表达式列表只能有一个, 在我们的例子中是 `{}, 5`).

* 表达式列表计算结束后, 将其值自动解包后**从左到右**分配给目标列表(target list). 因此, 在我们的例子中, 首先将 `{}, 5` 元组并赋值给 `a, b`, 然后我们就可以得到 `a = {}` 且 `b = 5`.

* `a` 被赋值的 `{}` 是可变对象.

* 第二个目标列表是 `a[b]` (你可能觉得这里会报错, 因为在之前的语句中 `a` 和 `b` 都还没有被定义. 但是别忘了, 我们刚刚将 `a` 赋值 `{}` 且将 `b` 赋值为 `5`).

* 现在, 我们将通过将字典中键 `5` 的值设置为元组 `({}, 5)` 来创建循环引用 (输出中的 `{...}` 指与 `a` 引用了相同的对象). 下面是一个更简单的循环引用的例子
  ```py
  >>> some_list = some_list[0] = [0]
  >>> some_list
  [[...]]
  >>> some_list[0]
  [[...]]
  >>> some_list is some_list[0]
  True
  >>> some_list[0][0][0][0][0][0] == some_list
  True
  ```
  我们的例子就是这种情况 (`a[b][0]` 与 `a` 是相同的对象)

* 总结一下, 你也可以把例子拆成
  ```py
  a, b = {}, 5
  a[b] = a, b
  ```
  并且可以通过 `a[b][0]` 与 `a` 是相同的对象来证明是循环引用
  ```py
  >>> a[b][0] is a
  True
  ```


---

### > Exceeds the limit for integer string conversion/整型转字符串越界
```py
>>> # Python 3.10.6
>>> int("2" * 5432)

>>> # Python 3.10.8
>>> int("2" * 5432)
```

**Output:**
```py
>>> # Python 3.10.6
222222222222222222222222222222222222222222222222222222222222222...

>>> # Python 3.10.8
Traceback (most recent call last):
   ...
ValueError: Exceeds the limit (4300) for integer string conversion:
   value has 5432 digits; use sys.set_int_max_str_digits()
   to increase the limit.
```

#### 💡 说明:

* 对`int()`的调用在Python 3.10.6中运行良好，但在Python 3.10.8中引发ValueError。请注意，Python仍然可以处理大整数。只有在整型和字符串之间转换时才会出现此错误。
* 幸运的是，当您希望操作超过允许的位数限制时，可以增加该限制的上限。为此，可以使用以下方法之一：
    - 使用 -X int_max_str_digits 的命令行参数（例如， python3 -X int_max_str_digits=640）
    - 使用来自sys模块的set_int_max_str_digits()函数
    - 设定 PYTHONINTMAXSTRDIGITS 环境变量

更多更改设置上限的操作细节查看[文档](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits)。

---

## Section: Slippery Slopes/滑坡谬误


### > Modifying a dictionary while iterating over it/迭代字典时的修改

```py
x = {0: None}

for i in x:
    del x[i]
    x[i+1] = None
    print(i)
```

**Output (Python 2.7- Python 3.5):**

```
0
1
2
3
4
5
6
7
```

是的, 它运行了**八次**然后才停下来.

#### 💡 说明:

* Python不支持对字典进行迭代的同时修改它.
* 它之所以运行8次, 是因为字典会自动扩容以容纳更多键值(我们有8次删除记录, 因此需要扩容). 这实际上是一个实现细节. (译: 应该是因为字典的初始最小值是8, 扩容会导致散列表地址发生变化而中断循环.)
* 在不同的Python实现中删除键的处理方式以及调整大小的时间可能会有所不同.(译: 就是说什么时候扩容在不同版本中可能是不同的, 在3.6及3.7的版本中到[5](https://github.com/python/cpython/blob/v3.6.1/Objects/dictobject.c#L103-L110)就会自动扩容了. 以后也有可能再次发生变化. 这是为了避免散列冲突. 顺带一提, 后面两次扩容会扩展为32和256. 即`8->32->256`.)
* 更多的信息, 你可以参考这个StackOverflow的[回答](https://stackoverflow.com/questions/44763802/bug-in-python-dict), 它详细的解释一个类似的例子.

---

### > Stubborn `del` operator/坚强的 `del` *

```py
class SomeClass:
    def __del__(self):
        print("Deleted!")
```

**Output:**
1\.
```py
>>> x = SomeClass()
>>> y = x
>>> del x # 这里应该会输出 "Deleted!"
>>> del y
Deleted!
```

唷, 终于删除了. 你可能已经猜到了在我们第一次尝试删除 `x` 时是什么让 `__del__` 免于被调用的. 那让我们给这个例子增加点难度.

2\.
```py
>>> x = SomeClass()
>>> y = x
>>> del x
>>> y # 检查一下y是否存在
<__main__.SomeClass instance at 0x7f98a1a67fc8>
>>> del y # 像之前一样, 这里应该会输出 "Deleted!"
>>> globals() # 好吧, 并没有. 让我们看一下所有的全局变量
Deleted!
{'__builtins__': <module '__builtin__' (built-in)>, 'SomeClass': <class __main__.SomeClass at 0x7f98a1a5f668>, '__package__': None, '__name__': '__main__', '__doc__': None}
```

好了，现在它被删除了 :confused:

#### 💡 说明:
+ `del x` 并不会立刻调用 `x.__del__()`.
+ 每当遇到 `del x`, Python 会将 `x` 的引用数减1, 当 `x` 的引用数减到0时就会调用 `x.__del__()`.
+ 在第二个例子中, `y.__del__()` 之所以未被调用, 是因为前一条语句 (`>>> y`) 对同一对象创建了另一个引用, 从而防止在执行 `del y` 后对象的引用数变为0.
+ 调用 `globals` 导致引用被销毁, 因此我们可以看到 "Deleted!" 终于被输出了.
+ (译: 这其实是 Python 交互解释器的特性, 它会自动让 `_` 保存上一个表达式输出的值, 详细可以看[这里](https://www.cnblogs.com/leisurelylicht/p/diao-pi-de-kong-zhi-tai.html).)


---

### > The out of scope variable/外部作用域变量
<!-- Example ID: 75c03015-7be9-4289-9e22-4f5fdda056f7 --->

1\.
```py
a = 1
def some_func():
    return a

def another_func():
    a += 1
    return a
```

2\.
```py
def some_closure_func():
    a = 1
    def some_inner_func():
        return a
    return some_inner_func()

def another_closure_func():
    a = 1
    def another_inner_func():
        a += 1
        return a
    return another_inner_func()
```

**Output:**
```py
>>> some_func()
1
>>> another_func()
UnboundLocalError: local variable 'a' referenced before assignment

>>> some_closure_func()
1
>>> another_closure_func()
UnboundLocalError: local variable 'a' referenced before assignment
```

#### 💡 说明:
* 当你在作用域中对变量进行赋值时, 变量会变成该作用域内的局部变量. 因此 `a` 会变成 `another_func` 函数作用域中的局部变量, 但它在函数作用域中并没有被初始化, 所以会引发错误.
* 想要在 `another_func` 中修改外部作用域变量 `a` 的话, 可以使用 `global` 关键字.
  ```py
  def another_func()
      global a
      a += 1
      return a
  ```

  **Output:**
  ```py
  >>> another_func()
  2
  ```

* 在 `another_closure_func` 函数中，`a` 会变成 `another_inner_func` 函数作用域中的局部变量, 但它在同一作用域中并没有被初始化, 所以会引发错误。
* 想要在 `another_inner_func` 中修改外部作用域变量 `a` 的话, 可以使用 `nonlocal` 关键字。nonlocal 表达式用于（除全局作用域外）最近一级的外部作用域。

  ```py
  def another_func():
      a = 1
      def another_inner_func():
          nonlocal a
          a += 1
          return a
      return another_inner_func()
  ```

  **Output:**
  ```py
  >>> another_func()
  2
  ```

*  `global` and `nonlocal` 关键字告诉 `Python` 解释器，不要声明新变量，而是在相应的外部作用域中查找变量。
* 可以阅读[这个](https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html)简短却很棒的指南, 了解更多关于 Python 中命名空间和作用域的工作原理。


---

### > Deleting a list item while iterating/迭代列表时删除元素

```py
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = [1, 2, 3, 4]
list_4 = [1, 2, 3, 4]

for idx, item in enumerate(list_1):
    del item

for idx, item in enumerate(list_2):
    list_2.remove(item)

for idx, item in enumerate(list_3[:]):
    list_3.remove(item)

for idx, item in enumerate(list_4):
    list_4.pop(idx)
```

**Output:**
```py
>>> list_1
[1, 2, 3, 4]
>>> list_2
[2, 4]
>>> list_3
[]
>>> list_4
[2, 4]
```

你能猜到为什么输出是 `[2, 4]` 吗?

#### 💡 说明:

* 在迭代时修改对象是一个很愚蠢的主意. 正确的做法是迭代对象的副本, `list_3[:]` 就是这么做的.

     ```py
     >>> some_list = [1, 2, 3, 4]
     >>> id(some_list)
     139798789457608
     >>> id(some_list[:]) # 注意python为切片列表创建了新对象.
     139798779601192
     ```

**`del`, `remove` 和 `pop` 的不同:**
* `del var_name` 只是从本地或全局命名空间中删除了 `var_name` (这就是为什么 `list_1` 没有受到影响).
* `remove` 会删除第一个匹配到的指定值, 而不是特定的索引, 如果找不到值则抛出 `ValueError` 异常.
* `pop` 则会删除指定索引处的元素并返回它, 如果指定了无效的索引则抛出 `IndexError` 异常.

**为什么输出是 `[2, 4]`?**
- 列表迭代是按索引进行的, 所以当我们从 `list_2` 或 `list_4` 中删除 `1` 时, 列表的内容就变成了 `[2, 3, 4]`. 剩余元素会依次位移, 也就是说, `2` 的索引会变为 0, `3` 会变为 1. 由于下一次迭代将获取索引为 1 的元素 (即 `3`), 因此 `2` 将被彻底的跳过. 类似的情况会交替发生在列表中的每个元素上.

* 参考这个StackOverflow的[回答](https://stackoverflow.com/questions/45946228/what-happens-when-you-try-to-delete-a-list-element-while-iterating-over-it)来解释这个例子
* 关于Python中字典的类似例子, 可以参考这个Stackoverflow的[回答](https://stackoverflow.com/questions/45877614/how-to-change-all-the-dictionary-keys-in-a-for-loop-with-d-items).


---

### > Lossy zip of iterators/丢三落四的zip *
<!-- Example ID: c28ed154-e59f-4070-8eb6-8967a4acac6d --->

```py
>>> numbers = list(range(7))
>>> numbers
[0, 1, 2, 3, 4, 5, 6]
>>> first_three, remaining = numbers[:3], numbers[3:]
>>> first_three, remaining
([0, 1, 2], [3, 4, 5, 6])
>>> numbers_iter = iter(numbers)
>>> list(zip(numbers_iter, first_three)) 
[(0, 0), (1, 1), (2, 2)]
# so far so good, let's zip the remaining
>>> list(zip(numbers_iter, remaining))
[(4, 3), (5, 4), (6, 5)]
```

`numbers` 列表中的元素 `3` 哪里去了？

#### 💡 说明

- 根据Python [文档](https://docs.python.org/3.3/library/functions.html#zip)， `zip` 函数的大概实现如下：

    ```py
    def zip(*iterables):
        sentinel = object()
        iterators = [iter(it) for it in iterables]
        while iterators:
            result = []
            for it in iterators:
                elem = next(it, sentinel)
                if elem is sentinel: return
                result.append(elem)
            yield tuple(result)
    ```

- 该函数接受任意数量的可迭代对象，通过调用 `next` 函数将它们的每个项目添加到 `result` 列表中，并在任一可迭代对象耗尽时停止。
- 这里需要注意的是，当任一可迭代对象用尽时，`result` 列表中的现有元素将被丢弃。这就是 `numbers_iter` 中的 `3` 所发生的情况。
- 使用 zip 执行上述操作的正确方法是:

    ```py
    >>> numbers = list(range(7))
    >>> numbers_iter = iter(numbers)
    >>> list(zip(first_three, numbers_iter))
    [(0, 0), (1, 1), (2, 2)]
    >>> list(zip(remaining, numbers_iter))
    [(3, 3), (4, 4), (5, 5), (6, 6)]
    ```

    `zip` 的第一个参数应当是有最少元素的那个。


---

### > Loop variables leaking out!/循环变量泄漏!

1\.
```py
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')
```

**Output:**
```py
6 : for x inside loop
6 : x in global
```

但是 `x` 从未在循环外被定义...

2\.
```py
# 这次我们先初始化x
x = -1
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')
```

**Output:**
```py
6 : for x inside loop
6 : x in global
```

3\.
```
x = 1
print([x for x in range(5)])
print(x, ': x in global')
```

**Output (on Python 2.x):**
```
[0, 1, 2, 3, 4]
(4, ': x in global')
```

**Output (on Python 3.x):**
```
[0, 1, 2, 3, 4]
1 : x in global
```

#### 💡 说明:

- 在 Python 中, for 循环使用所在作用域并在结束后保留定义的循环变量. 如果我们曾在全局命名空间中定义过循环变量. 在这种情况下, 它会重新绑定现有变量.

- Python 2.x 和 Python 3.x 解释器在列表推导式示例中的输出差异, 在文档 [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) 中可以找到相关的解释:

    > "列表推导不再支持句法形式 `[... for var in item1, item2, ...]`. 取而代之的是 `[... for var in (item1, item2, ...)]`. 另外, 注意列表推导具有不同的语义: 它们更接近于 `list()` 构造函数中生成器表达式的语法糖(译: 这一句我也不是很明白), 特别是循环控制变量不再泄漏到周围的作用域中."

---

### > Beware of default mutable arguments!/当心默认的可变参数!

```py
def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg
```

**Output:**
```py
>>> some_func()
['some_string']
>>> some_func()
['some_string', 'some_string']
>>> some_func([])
['some_string']
>>> some_func()
['some_string', 'some_string', 'some_string']
```

#### 💡 说明:

- Python中函数的默认可变参数并不是每次调用该函数时都会被初始化. 相反, 它们会使用最近分配的值作为默认值. 当我们明确的将 `[]` 作为参数传递给 `some_func` 的时候, 就不会使用 `default_arg` 的默认值, 所以函数会返回我们所期望的结果.

    ```py
    def some_func(default_arg=[]):
        default_arg.append("some_string")
        return default_arg
    ```

    **Output:**
    ```py
    >>> some_func.__defaults__ # 这里会显示函数的默认参数的值
    ([],)
    >>> some_func()
    >>> some_func.__defaults__
    (['some_string'],)
    >>> some_func()
    >>> some_func.__defaults__
    (['some_string', 'some_string'],)
    >>> some_func([])
    >>> some_func.__defaults__
    (['some_string', 'some_string'],)
    ```

- 避免可变参数导致的错误的常见做法是将 `None` 指定为参数的默认值, 然后检查是否有值传给对应的参数. 例:

    ```py
    def some_func(default_arg=None):
        if not default_arg:
            default_arg = []
        default_arg.append("some_string")
        return default_arg
    ```

---

### > Catching the Exceptions/捕获异常

```py
some_list = [1, 2, 3]
try:
    # 这里会抛出异常 ``IndexError``
    print(some_list[4])
except IndexError, ValueError:
    print("Caught!")

try:
    # 这里会抛出异常 ``ValueError``
    some_list.remove(4)
except IndexError, ValueError:
    print("Caught again!")
```

**Output (Python 2.x):**
```py
Caught!

ValueError: list.remove(x): x not in list
```

**Output (Python 3.x):**
```py
  File "<input>", line 3
    except IndexError, ValueError:
                     ^
SyntaxError: invalid syntax
```

#### 💡 说明:

* 如果你想要同时捕获多个不同类型的异常时, 你需要将它们用括号包成一个元组作为第一个参数传递. 第二个参数是可选名称, 如果你提供, 它将与被捕获的异常实例绑定. 例,
  ```py
  some_list = [1, 2, 3]
  try:
     # 这里会抛出异常 ``ValueError``
     some_list.remove(4)
  except (IndexError, ValueError), e:
     print("Caught again!")
     print(e)
  ```
  **Output (Python 2.x):**
  ```
  Caught again!
  list.remove(x): x not in list
  ```
  **Output (Python 3.x):**
  ```py
    File "<input>", line 4
      except (IndexError, ValueError), e:
                                       ^
  IndentationError: unindent does not match any outer indentation level
  ```

* 在 Python 3 中, 用逗号区分异常与可选名称是无效的; 正确的做法是使用 `as` 关键字. 例,
  ```py
  some_list = [1, 2, 3]
  try:
      some_list.remove(4)

  except (IndexError, ValueError) as e:
      print("Caught again!")
      print(e)
  ```
  **Output:**
  ```
  Caught again!
  list.remove(x): x not in list
  ```

---

### > Same operands, different story!/同人不同命!

1\.
```py
a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]
```

**Output:**
```py
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4]
```

2\.
```py
a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]
```

**Output:**
```py
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4, 5, 6, 7, 8]
```

#### 💡 说明:

*  `a += b` 并不总是与 `a = a + b` 表现相同. 类实现 *`op=`* 运算符的方式 *也许* 是不同的, 列表就是这样做的.

* 表达式 `a = a + [5,6,7,8]` 会生成一个新列表, 并让 `a` 引用这个新列表, 同时保持 `b` 不变.

* 表达式 `a += [5,6,7,8]` 实际上是使用的是 "extend" 函数, 所以 `a` 和 `b` 仍然指向已被修改的同一列表.


---

### > Name resolution ignoring class scope/忽略类作用域的名称解析

1\.
```py
x = 5
class SomeClass:
    x = 17
    y = (x for i in range(10))
```

**Output:**
```py
>>> list(SomeClass.y)[0]
5
```

2\.
```py
x = 5
class SomeClass:
    x = 17
    y = [x for i in range(10)]
```

**Output (Python 2.x):**
```py
>>> SomeClass.y[0]
17
```

**Output (Python 3.x):**
```py
>>> SomeClass.y[0]
5
```

#### 💡 说明:
- 类定义中嵌套的作用域会忽略类内的名称绑定.
- 生成器表达式有它自己的作用域.
- 从 Python 3.X 开始, 列表推导式也有自己的作用域.


---

### > Rounding like a banker/像银行家一样舍入 *

让我们实现一个简单的函数来获取列表的中间元素：

```py
def get_middle(some_list):
    mid_index = round(len(some_list) / 2)
    return some_list[mid_index - 1]
```

**Python 3.x:**
```py
>>> get_middle([1])  # looks good
1
>>> get_middle([1,2,3])  # looks good
2
>>> get_middle([1,2,3,4,5])  # huh?
2
>>> len([1,2,3,4,5]) / 2  # good
2.5
>>> round(len([1,2,3,4,5]) / 2)  # why?
2
```

似乎 Python 将 2.5 舍入到 2。

#### 💡 说明

- - 这不是浮点精度错误，实际上，这种行为是故意的。从 Python 3.0 开始，`round()` 使用[银行进位法](https://en.wikipedia.org/wiki/Rounding#Round_half_to_even)，其中 0.5 小数四舍五入到最接近的 **偶数** ：

```py
>>> round(0.5)
0
>>> round(1.5)
2
>>> round(2.5)
2
>>> import numpy  # numpy的结果也是一样
>>> numpy.round(0.5)
0.0
>>> numpy.round(1.5)
2.0
>>> numpy.round(2.5)
2.0
```

- 这是 [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754#Rounding_rules) 中描述的关于0.5分位舍入的推荐方法。然而，另一种方法（从零取整）大部分时间都是在学校教授的，所以银行进位法可能并不为人所知。此外，一些最流行的编程语言（例如：JavaScript、Java、C/C++、Ruby、Rust）也不使用银行进位法。因此，这对 Python 来说还是比较特殊的，在四舍五入时可能会导致混淆。
- 了解更多信息，请参阅文档 [round()](https://docs.python.org/3/library/functions.html#round) 或 [this stackoverflow thread](https://stackoverflow.com/questions/10825926/python -3-x-rounding-behavior) 
- 请注意，`get_middle([1])` 只返回1，因为它的索引是 `round(0.5) - 1 = 0 - 1 = -1`，返回列表中的最后一个元素。


---

### > Needles in a Haystack/大海捞针
<!-- Example ID: 52a199b1-989a-4b28-8910-dff562cebba9 --->

迄今为止，每一位Python开发者都会遇到类似以下的情况。

1\.
```py
x, y = (0, 1) if True else None, None
```

**Output:**
```
>>> x, y  # 期望的结果是 (0, 1)
((0, 1), None)
```

2\.
```py
t = ('one', 'two')
for i in t:
    print(i)

t = ('one')
for i in t:
    print(i)

t = ()
print(t)
```

**Output:**

```py
one
two
o
n
e
tuple()
```

3\.

```
ten_words_list = [
    "some",
    "very",
    "big",
    "list",
    "that"
    "consists",
    "of",
    "exactly",
    "ten",
    "words"
]
```

**Output**

```py
>>> len(ten_words_list)
9
```

4\. 不够健壮的断言机制

```py
a = "python"
b = "javascript"
```

**Output:**

```py
# 带有失败警告信息的assert表达式
>>> assert(a == b, "Both languages are different")
# 未引发 AssertionError 
```

5\.

```py
some_list = [1, 2, 3]
some_dict = {
  "key_1": 1,
  "key_2": 2,
  "key_3": 3
}

some_list = some_list.append(4) 
some_dict = some_dict.update({"key_4": 4})
```

**Output:**

```py
>>> print(some_list)
None
>>> print(some_dict)
None
```

6\.

```py
def some_recursive_func(a):
    if a[0] == 0:
        return
    a[0] -= 1
    some_recursive_func(a)
    return a

def similar_recursive_func(a):
    if a == 0:
        return a
    a -= 1
    similar_recursive_func(a)
    return a
```

**Output:**

```py
>>> some_recursive_func([5, 0])
[0, 0]
>>> similar_recursive_func(5)
4
```

#### 💡 说明:
* 对于 1, 正确的语句是 `x, y = (0, 1) if True else (None, None)`.
* 对于 2, 正确的语句是 `t = ('one',)` 或者 `t = 'one',` (缺少逗号) 否则解释器会认为 `t` 是一个字符串, 并逐个字符对其进行迭代.
* `()` 是一个特殊的标记，表示空元组.
* 对于 3，正如您可能已经弄清楚的那样，列表中的第5个元素（"that"）后面缺少一个逗号。因此，通过隐式字符串字面连接，

  ```py
  >>> ten_words_list
  ['some', 'very', 'big', 'list', 'thatconsists', 'of', 'exactly', 'ten', 'words']
  ```

* 在第4个代码段中没有引发"AssertionError"，因为我们不是断言单个表达式 `a == b`，而是断言整个元组。以下代码段将说明问题，

  ```py
  >>> a = "python"
  >>> b = "javascript"
  >>> assert a == b
  Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
  AssertionError
  
  >>> assert (a == b, "Values are not equal")
  <stdin>:1: SyntaxWarning: assertion is always true, perhaps remove parentheses?
  
  >>> assert a == b, "Values are not equal"
  Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
  AssertionError: Values are not equal
  ```
* 至于第五个片段，大多数修改序列/映射对象项的方法，如`list.append`、`dict.update`、`list.sort`等，都在原地修改对象并返回`None`。这背后的基本原理是通过原地操作，避免复制对象来提高性能(参考[这里](https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list))。
* 最后一个应该相当明显，可变对象（如`list`）可以在函数中更改，不可变对象（`a -= 1`）的重新赋值则不属于值的改变。
* 了解这些细节可以在程序长期运行中，为您节省数小时的调试工作。


---

### > Splitsies/分割函数 *
<!-- Example ID: ec3168ba-a81a-4482-afb0-691f1cc8d65a --->

```py
>>> 'a'.split()
['a']

# is same as
>>> 'a'.split(' ')
['a']

# but
>>> len(''.split())
0

# isn't the same as
>>> len(''.split(' '))
1
```

#### 💡 说明

- 起初人们可能会认为 split 的默认分隔符是单个空格 `' '`，但根据 [文档](https://docs.python.org/3/library/stdtypes.html#str.split)：
    >  如果 sep 未指定或为 `None`，则应用不同的拆分算法：连续的空格被视为单个分隔符，如果字符串有前导或尾随空格，则结果将在开头或结尾不包含空字符串。因此，使用 `None` 分隔符拆分空字符串或仅包含空格的字符串将返回 `[]`。
    > 如果给定 sep，连续的分隔符不会组合在一起，并被视为分隔空字符串（例如，`'1,,2'.split(',')` 返回 `['1', '', '2 ']`）。使用指定的分隔符拆分空字符串会返回 `['']`。
- Noticing how the leading and trailing whitespaces are handled in the following snippet will make things clear,
- 注意以下代码段中如何处理前导和尾随空格，促进更深入的理解：

    ```py
    >>> ' a '.split(' ')
    ['', 'a', '']
    >>> ' a '.split()
    ['a']
    >>> ''.split(' ')
    ['']
    ```


---

### > Wild imports/通配符导入方式 *
<!-- Example ID: 83deb561-bd55-4461-bb5e-77dd7f411e1c --->
<!-- read-only -->

```py
# File: module.py

def some_weird_name_func_():
    print("works!")

def _another_weird_name_func():
    print("works!")

```

**Output**

```py
>>> from module import *
>>> some_weird_name_func_()
"works!"
>>> _another_weird_name_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_another_weird_name_func' is not defined
```

#### 💡 说明

- 通常建议不要使用通配符导入。第一个明显的原因是，在通配符导入中，带有前导下划线的名称不会被导入。这可能会导致运行时出错。
- 如果我们使用 `from ... import a, b, c` 语法，上面的 `NameError` 就不会发生。

    ```py
    >>> from module import some_weird_name_func_, _another_weird_name_func
    >>> _another_weird_name_func()
    works!
    ```

- 如果你真的想使用通配符导入，那么你必须在你的模块中定义列表`__all__`，它包含一系列公共对象，当我们进行通配符导入时，列表中的这些对象将被导入。

    ```py
    __all__ = ['_another_weird_name_func']

    def some_weird_name_func_():
        print("works!")

    def _another_weird_name_func():
        print("works!")
    ```
    **Output**

    ```py
    >>> _another_weird_name_func()
    "works!"
    >>> some_weird_name_func_()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'some_weird_name_func_' is not defined
    ```


---

### > All sorted?/都排序了吗？ *

<!-- Example ID: e5ff1eaf-8823-4738-b4ce-b73f7c9d5511 -->

```py
>>> x = 7, 8, 9
>>> sorted(x) == x
False
>>> sorted(x) == sorted(x)
True

>>> y = reversed(x)
>>> sorted(y) == sorted(y)
False
```

#### 💡 说明

- `sorted` 方法一定返回列表类型, 比较列表与元组在Python中一定返回 `False`. 

- ```py
  >>> [] == tuple()
  False
  >>> x = 7, 8, 9
  >>> type(x), type(sorted(x))
  (tuple, list)
  ```

- 与 `sorted` 不同，`reversed` 方法返回一个迭代器。为什么？因为排序需要就地修改迭代器或使用额外的容器（列表），而反向可以简单地通过从最后一个索引迭代到第一个索引来工作。

- 所以在比较 `sorted(y) == sorted(y)` 时，第一次调用 `sorted()` 会消耗迭代器 `y`，下一次调用只会返回一个空列表。

  ```py
  >>> x = 7, 8, 9
  >>> y = reversed(x)
  >>> sorted(y), sorted(y)
  ([7, 8, 9], [])
  ```


---

### > Midnight time doesn't exist?/不存在的午夜?

```py
from datetime import datetime

midnight = datetime(2018, 1, 1, 0, 0)
midnight_time = midnight.time()

noon = datetime(2018, 1, 1, 12, 0)
noon_time = noon.time()

if midnight_time:
    print("Time at midnight is", midnight_time)

if noon_time:
    print("Time at noon is", noon_time)
```

**Output:**
```sh
('Time at noon is', datetime.time(12, 0))
```

midnight_time 并没有被输出.

#### 💡 说明:

在Python 3.5之前, 如果 `datetime.time` 对象存储的UTC的午夜时间(译: 就是 `00:00`), 那么它的布尔值会被认为是 `False`. 当使用 `if obj:` 语句来检查 `obj` 是否为 `null` 或者某些“空”值的时候, 很容易出错.


---

## Section: The Hidden treasures!/隐藏的宝藏!

本节包含了一些像我这样的大多数初学者都不知道的关于Python的鲜为人知的有趣的事情（好吧，现在不是了）。

### > Okay Python, Can you make me fly?/Python, 可否带我飞? *

好, 去吧.

```py
import antigravity
```

**Output:**
嘘.. 这是个超级秘密.

#### 💡 说明:
+ `antigravity` 模块是 Python 开发人员发布的少数复活节彩蛋之一.
+ `import antigravity` 会打开一个 Python 的[经典 XKCD 漫画](http://xkcd.com/353/)页面.
+ 不止如此. 这个**复活节彩蛋里还有一个复活节彩蛋**. 如果你看一下[代码](https://github.com/python/cpython/blob/master/Lib/antigravity.py#L7-L17), 就会发现还有一个函数实现了 [XKCD's geohashing 算法](https://xkcd.com/426/).

---

### > `goto`, but why?/`goto`, 但为什么? *

```py
from goto import goto, label
for i in range(9):
    for j in range(9):
        for k in range(9):
            print("I'm trapped, please rescue!")
            if k == 2:
                goto .breakout # 从多重循环中跳出
label .breakout
print("Freedom!")
```

**Output (Python 2.3):**
```py
I'm trapped, please rescue!
I'm trapped, please rescue!
Freedom!
```

#### 💡 说明:
- 2004年4月1日, Python [宣布](https://mail.python.org/pipermail/python-announce-list/2004-April/002982.html) 加入一个可用的 `goto` 作为愚人节礼物.
- 当前版本的 Python 并没有这个模块.
- 就算可以用, 也请不要使用它. 这里是为什么Python中没有 `goto` 的[原因](https://docs.python.org/3/faq/design.html#why-is-there-no-goto).

---

### > Brace yourself!/做好思想准备 *

如果你不喜欢在Python中使用空格来表示作用域, 你可以导入 C 风格的 {},

```py
from __future__ import braces
```

**Output:**
```py
  File "some_file.py", line 1
    from __future__ import braces
SyntaxError: not a chance
```

想用大括号 `braces`? 没门! 觉得不爽, 请去用java。那么，另一个令人惊讶的事情，找一找在 `__future__` 模块中，哪里引发了 `SyntaxError` [code](https://github.com/python/cpython/blob/master/Lib/__future__.py)?

#### 💡 说明:
+ 通常 `__future__` 会提供 Python 未来版本的功能. 然而，这里的 “未来” 是一个讽刺.
+ 这是一个表达社区对此类问题态度的复活节彩蛋.
+ 代码实际上在[`future.c` 文件]中 (https://github.com/python/cpython/blob/025eb98dc0c1dc27404df6c544fc2944e0fa9f3a/Python/future.c#L49).
+ 当 CPython 编译器遇到 [future表达式](https://docs.python.org/3.3/reference/simple_stmts.html#future-statements) 时，它首先在 `future.c` 中运行相应的代码，然后再对其进行处理作为正常的`import`表达式。


---

### > Let's meet Friendly Language Uncle For Life/让生活更友好 *
<!-- Example ID: 6427fae6-e959-462d-85da-ce4c94ce41be --->

**Output (Python 3.x)**
```py
>>> from __future__ import barry_as_FLUFL
>>> "Ruby" != "Python" # 这里没什么疑问
  File "some_file.py", line 1
    "Ruby" != "Python"
              ^
SyntaxError: invalid syntax

>>> "Ruby" <> "Python"
True
```

这就对了.

#### 💡 说明:
- 相关的 [PEP-401](https://www.python.org/dev/peps/pep-0401/) 发布于 2009年4月1日 (所以你现在知道这意味着什么了吧).
- 引用 PEP-401
  > 意识到 Python 3.0 里的 != 运算符是一个会引起手指疼痛的恐怖错误, FLUFL 将 <> 运算符恢复为唯一写法.
- Uncle Barry 在 PEP 中还分享了其他东西; 你可以在[这里](https://www.python.org/dev/peps/pep-0401/)获得他们.
- (译: 虽然文档中没写，但应该是只能在交互解释器中使用.)
- 它在交互式环境中正常运行，但是当您通过 python 文件运行时它会引发 `SyntaxError`（请参阅此 [问题](https://github.com/satwikkansal/wtfpython/issues/94)）。您可以将表达式作为`eval` 或 `compile` 参数中使用。

    ```py
    from __future__ import barry_as_FLUFL
    print(eval('"Ruby" <> "Python"'))
    ```


---

### > Even Python understands that love is complicated/连Python也知道爱是难言的 *

```py
import this
```

等等, **this** 是什么? `this` 是爱 :heart:

**Output:**
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
优美胜于丑陋（Python 以编写优美的代码为目标）
Explicit is better than implicit.
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
Simple is better than complex.
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
Complex is better than complicated.
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
Flat is better than nested.
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
Sparse is better than dense.
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
Readability counts.
可读性很重要（优美的代码一定是可读的）
Special cases aren't special enough to break the rules.
没有特例特殊到需要违背这些规则（这些规则至高无上）
Although practicality beats purity.
尽管我们更倾向于实用性
Errors should never pass silently.
不要安静的包容所有错误
Unless explicitly silenced.
除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）
In the face of ambiguity, refuse the temptation to guess.
拒绝诱惑你去猜测的暧昧事物
There should be one-- and preferably only one --obvious way to do it.
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
Although that way may not be obvious at first unless you're Dutch.
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）
Now is better than never.
现在行动好过永远不行动
Although never is often better than *right* now.
尽管不行动要好过鲁莽行动
If the implementation is hard to explain, it's a bad idea.
如果你无法向人描述你的方案，那肯定不是一个好方案；
If the implementation is easy to explain, it may be a good idea.
如果你能轻松向人描述你的方案，那也许会是一个好方案（方案测评标准）
Namespaces are one honking great idea -- let's do more of those!
命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）
```

这是 Python 之禅!

```py
>>> love = this
>>> this is love
True
>>> love is True
False
>>> love is False
False
>>> love is not True or False
True
>>> love is not True or False; love is love  # 爱是难言的
True
```

#### 💡 说明:

* `this` 模块是关于 Python 之禅的复活节彩蛋 ([PEP 20](https://www.python.org/dev/peps/pep-0020)).
* 如果你认为这已经够有趣的了, 可以看看 [this.py](https://hg.python.org/cpython/file/c3896275c0f6/Lib/this.py) 的实现. 有趣的是, Python 之禅的实现代码违反了他自己 (这可能是唯一会发生这种情况的地方).
*
至于 `love is not True or False; love is love`, 意外却又不言而喻.

---

### > Yes, it exists!/是的, 它存在!

**循环的 `else`.** 一个典型的例子:

```py
  def does_exists_num(l, to_find):
      for num in l:
          if num == to_find:
              print("Exists!")
              break
      else:
          print("Does not exist")
```

**Output:**
```py
>>> some_list = [1, 2, 3, 4, 5]
>>> does_exists_num(some_list, 4)
Exists!
>>> does_exists_num(some_list, -1)
Does not exist
```

**异常的 `else` .** 例,

```py
try:
    pass
except:
    print("Exception occurred!!!")
else:
    print("Try block executed successfully...")
```

**Output:**
```py
Try block executed successfully...
```

#### 💡 说明:
- 循环后的 `else` 子句只会在循环没有触发 `break` 语句, 正常结束的情况下才会执行.
- try 之后的 `else` 子句也被称为 "完成子句", 因为在 `try` 语句中到达 `else` 子句意味着try块实际上已成功完成.


---

### > Ellipsis/省略 *
<!-- Example ID: 969b7100-ab3d-4a7d-ad7d-a6be16181b2b --->

```py
def some_func():
    Ellipsis
```

**Output**
```py
>>> some_func()
# 没有输出，也没有报错

>>> SomeRandomString
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'SomeRandomString' is not defined

>>> Ellipsis
Ellipsis
```

#### 💡 说明
- 在 Python 中，`Ellipsis` 是一个全局可用的内置对象，相当于`...`。

    ```py
    >>> ...
    Ellipsis
    ```

- 省略号可用于多种用途，
    + 作为尚未编写的代码的占位符（就像`pass`语句）
    + 在切片语法中表示完整切片的其余维度

    ```py
    >>> import numpy as np
    >>> three_dimensional_array = np.arange(8).reshape(2, 2, 2)
    array([
        [
            [0, 1],
            [2, 3]
        ],

        [
            [4, 5],
            [6, 7]
        ]
    ])
    ```

    所以我们的 `three_dimensional_array` 是一个数组的数组的数组。假设我们要打印所有最内层数组的第二个元素（索引 `1`），我们可以使用 Ellipsis 绕过所有前面的维度

    ```py
    >>> three_dimensional_array[:,:,1]
    array([[1, 3],
       [5, 7]])
    >>> three_dimensional_array[..., 1] # 使用Ellipsis.
    array([[1, 3],
       [5, 7]])
    ```

    注意：这适用于任意数量的维度。您甚至可以在第一个和最后一个维度中选择切片并以这种方式忽略中间的切片(`n_dimensional_array[firs_dim_slice, ..., last_dim_slice]`)

     + 在 [类型提示](https://docs.python.org/3/library/typing.html)中仅表示类型的一部分（如 `(Callable[..., int]` 或 `Tuple[ str, ...]`))

     + 您也可以使用省略号作为默认函数参数（在您想要区分“无参数”和“传递None值”场景的情况下）。


---

### > Inpinity/无限 *

英文拼写是有意的, 请不要为此提交补丁.
(译: 这里是为了突出 Python 中无限的定义与[Pi](https://en.wikipedia.org/wiki/Pi)有关, 所以将两个单词拼接了.)

**Output (Python 3.x):**
```py
>>> infinity = float('infinity')
>>> hash(infinity)
314159
>>> hash(float('-inf'))
-314159
```

#### 💡 说明:
- infinity 的哈希值是 10⁵ x π.
- 有意思的是, `float('-inf')` 的哈希值在 Python 3 中是 "-10⁵ x π"  , 而在 Python 2 中是 "-10⁵ x e".

---

### > Let's mangle/修饰时间! *
<!-- Example ID: 37146d2d-9e67-43a9-8729-3c17934b910c --->

1\.
```py
class Yo(object):
    def __init__(self):
        self.__honey = True
        self.bro = True
```

**Output:**
```py
>>> Yo().bro
True
>>> Yo().__honey
AttributeError: 'Yo' object has no attribute '__honey'
>>> Yo()._Yo__honey
True
```

2\.
```py
class Yo(object):
    def __init__(self):
        # 这次试试对称形式
        self.__honey__ = True
        self.bro = True
```

**Output:**
```py
>>> Yo().bro
True

>>> Yo()._Yo__honey__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Yo' object has no attribute '_Yo__honey__'
```

为什么 `Yo()._Yo__honey` 能运行? 只有印度人理解.(译: 这个梗可能是指印度音乐人[Yo Yo Honey Singh](https://en.wikipedia.org/wiki/Yo_Yo_Honey_Singh))


3\.

```py
_A__variable = "Some value"

class A(object):
    def some_func(self):
        return __variable # 没在任何地方初始化
```

**Output:**
```py
>>> A().__variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__variable'

>>> A().some_func()
'Some value'
```


#### 💡 说明:

* [命名修饰](https://en.wikipedia.org/wiki/Name_mangling) 用于避免不同命名空间之间名称冲突.
* 在 Python 中, 解释器会通过给类中以 `__` (双下划线)开头且结尾最多只有一个下划线的类成员名称加上`_NameOfTheClass` 来修饰(mangles)名称.
* 所以, 要访问 `__honey` 对象,我们需要加上 `_Yo` 以防止与其他类中定义的相同名称的属性发生冲突.
* 但是为什么它在第二个片段中不起作用？ 因为命名修饰排除了以双下划线结尾的名称。
* 第三个片段也是命名修饰的结果。 `return __variable` 语句中的 `__variable` 名称被修改为 `_A__variable`，这也恰好是我们在外部作用域中声明的变量的名称。
* 此外，如果修饰后的变量名超过255个字符，则会进行截断。


---

## Section: Appearances are deceptive!/外表是靠不住的!

### > Skipping lines?/跳过一行?

**Output:**
```py
>>> value = 11
>>> valuе = 32
>>> value
11
```

什么鬼?

**注意:** 如果你想要重现的话最简单的方法是直接复制上面的代码片段到你的文件或命令行里.

#### 💡 说明:

一些非西方字符虽然看起来和英语字母相同, 但会被解释器识别为不同的字母.

```py
>>> ord('е') # 西里尔语的 'e' (Ye)
1077
>>> ord('e') # 拉丁语的 'e', 用于英文并使用标准键盘输入
101
>>> 'е' == 'e'
False

>>> value = 42 # 拉丁语 e
>>> valuе = 23 # 西里尔语 'e', Python 2.x 的解释器在这会抛出 `SyntaxError` 异常
>>> value
42
```

内置的 `ord()` 函数可以返回一个字符的 Unicode [代码点](https://en.wikipedia.org/wiki/Code_point), 这里西里尔语 'e' 和拉丁语 'e' 的代码点不同证实了上述例子.

---

### > Teleportation/空间移动 *

```py
import numpy as np

def energy_send(x):
    # 初始化一个 numpy 数组
    np.array([float(x)])

def energy_receive():
    # 返回一个空的 numpy 数组
    return np.empty((), dtype=np.float).tolist()
```

**Output:**
```py
>>> energy_send(123.456)
>>> energy_receive()
123.456
```

谁来给我发个诺贝尔奖?

#### 💡 说明:

* 注意在 `energy_send` 函数中创建的 numpy 数组并没有返回, 因此内存空间被释放并可以被重新分配.
* `numpy.empty()` 直接返回下一段空闲内存，而不重新初始化. 而这个内存点恰好就是刚刚释放的那个(通常情况下, 并不绝对).

---

### > Well, something is fishy.../嗯，有些可疑...

```py
def square(x):
    """
    一个通过加法计算平方的简单函数.
    """
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
  return sum_so_far
```

**Output (Python 2.x):**

```py
>>> square(10)
10
```

难道不应该是100吗?

**注意:** 如果你无法重现, 可以尝试运行这个文件[mixed_tabs_and_spaces.py](/mixed_tabs_and_spaces.py).

#### 💡 说明:

* **不要混用制表符(tab)和空格(space)!** 在上面的例子中, return 的前面是"1个制表符", 而其他部分的代码前面是 "4个空格".
* Python是这么处理制表符的:
  > 首先, 制表符会从左到右依次被替换成8个空格, 直到被替换后的字符总数是八的倍数 <...>
* 因此, `square` 函数最后一行的制表符会被替换成8个空格, 导致return语句进入循环语句里面.
* Python 3 很友好, 在这种情况下会自动抛出错误.

    **Output (Python 3.x):**
    ```py
    TabError: inconsistent use of tabs and spaces in indentation
    ```


---

## Section: Miscellaneous/杂项


### > `+=` is faster/更快的 `+=`

```py
# 用 "+" 连接三个字符串:
>>> timeit.timeit("s1 = s1 + s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.25748300552368164
# 用 "+=" 连接三个字符串:
>>> timeit.timeit("s1 += s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.012188911437988281
```

#### 💡 说明:
+ 连接两个以上的字符串时 `+=` 比 `+` 更快, 因为在计算过程中第一个字符串 (例如, `s1 += s2 + s3` 中的 `s1`) 不会被销毁.(译: 就是 `+=` 执行的是追加操作，少了一个销毁新建的动作.)

---

### > Let's make a giant string!/来做个巨大的字符串吧！

```py
def add_string_with_plus(iters):
    s = ""
    for i in range(iters):
        s += "xyz"
    assert len(s) == 3*iters

def add_bytes_with_plus(iters):
    s = b""
    for i in range(iters):
        s += b"xyz"
    assert len(s) == 3*iters

def add_string_with_format(iters):
    fs = "{}"*iters
    s = fs.format(*(["xyz"]*iters))
    assert len(s) == 3*iters

def add_string_with_join(iters):
    l = []
    for i in range(iters):
        l.append("xyz")
    s = "".join(l)
    assert len(s) == 3*iters

def convert_list_to_string(l, iters):
    s = "".join(l)
    assert len(s) == 3*iters
```

**Output:**
```py
>>> timeit(add_string_with_plus(10000))
1000 loops, best of 3: 972 µs per loop
>>> timeit(add_bytes_with_plus(10000))
1000 loops, best of 3: 815 µs per loop
>>> timeit(add_string_with_format(10000))
1000 loops, best of 3: 508 µs per loop
>>> timeit(add_string_with_join(10000))
1000 loops, best of 3: 878 µs per loop
>>> l = ["xyz"]*10000
>>> timeit(convert_list_to_string(l, 10000))
10000 loops, best of 3: 80 µs per loop
```

让我们将迭代次数增加10倍.

```py
>>> timeit(add_string_with_plus(100000)) # 执行时间线性增加
100 loops, best of 3: 9.75 ms per loop
>>> timeit(add_bytes_with_plus(100000)) # 二次增加
1000 loops, best of 3: 974 ms per loop
>>> timeit(add_string_with_format(100000)) # 线性增加
100 loops, best of 3: 5.25 ms per loop
>>> timeit(add_string_with_join(100000)) # 线性增加
100 loops, best of 3: 9.85 ms per loop
>>> l = ["xyz"]*100000
>>> timeit(convert_list_to_string(l, 100000)) # 线性增加
1000 loops, best of 3: 723 µs per loop
```

#### 💡 说明:
- 你可以在这获得更多 [timeit](https://docs.python.org/3/library/timeit.html) 的相关信息. 它通常用于衡量代码片段的执行时间.
- 不要用 `+` 去生成过长的字符串, 在 Python 中, `str` 是不可变的, 所以在每次连接中你都要把左右两个字符串复制到新的字符串中. 如果你连接四个长度为10的字符串, 你需要拷贝 (10+10) + ((10+10)+10) + (((10+10)+10)+10) = 90 个字符而不是 40 个字符. 随着字符串的数量和大小的增加, 情况会变得越发的糟糕 (就像`add_bytes_with_plus` 函数的执行时间一样)
- 因此, 更建议使用 `.format.` 或 `%` 语法 (但是, 对于短字符串, 它们比 `+` 稍慢一点).
- 又或者, 如果你所需的内容已经以可迭代对象的形式提供了, 使用 `''.join(可迭代对象)` 要快多了.
- `add_string_with_plus` 的执行时间没有像 `add_bytes_with_plus` 一样出现二次增加是因为解释器会如同上一个例子所讨论的一样优化 `+=`. 用 `s = s + "x" + "y" + "z"` 替代 `s += "xyz"` 的话, 执行时间就会二次增加了.
  ```py
  def add_string_with_plus(iters):
      s = ""
      for i in range(iters):
          s = s + "x" + "y" + "z"
      assert len(s) == 3*iters

  >>> timeit(add_string_with_plus(10000))
  100 loops, best of 3: 9.87 ms per loop
  >>> timeit(add_string_with_plus(100000)) # 执行时间二次增加
  1 loops, best of 3: 1.09 s per loop
  ```


---

### > Slowing down `dict` lookups/让字典的查找慢下来 *
<!-- Example ID: c9c26ce6-df0c-47f7-af0b-966b9386d4c3 --->

```py
some_dict = {str(i): 1 for i in range(1_000_000)}
another_dict = {str(i): 1 for i in range(1_000_000)}
```

**Output:**
```py
>>> %timeit some_dict['5']
28.6 ns ± 0.115 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> some_dict[1] = 1
>>> %timeit some_dict['5']
37.2 ns ± 0.265 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

>>> %timeit another_dict['5']
28.5 ns ± 0.142 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> another_dict[1]  # Trying to access a key that doesn't exist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> %timeit another_dict['5']
38.5 ns ± 0.0913 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```

为什么相同的查找会变得越来越慢？

#### 💡 说明
+ CPython 有一个通用的字典查找函数，可以处理所有类型的键（`str`、`int`、任何对象...），以及一个专门用于处理仅由 `str` 键组成的字典的常见情况。
+ 专用函数（在 CPython 的 [源](https://github.com/python/cpython/blob/522691c46e2ae51faaad5bbbce7d959dd61770df/Objects/dictobject.c#L841) 中名为 `lookdict_unicode`）知道所有现有的键（包括查找的 key) 是字符串，并使用更快和更简单的字符串比较来比较键，而不是调用 `__eq__` 方法。
+ 第一次使用非 `str` 键访问 `dict` 实例时，会对其进行修改，以便将来的查找使用通用函数。
+ 这个过程对于特定的 `dict` 实例是不可逆的，并且键甚至不必存在于字典中。 这就是为什么对不存在的键进行查找具有相同副作用的原因。


---

### > Bloating instance `dict`s/变臃肿的`dict`实例们 *
<!-- Example ID: fe706ab4-1615-c0ba-a078-76c98cbe3f48 --->

```py
import sys

class SomeClass:
    def __init__(self):
        self.some_attr1 = 1
        self.some_attr2 = 2
        self.some_attr3 = 3
        self.some_attr4 = 4


def dict_size(o):
    return sys.getsizeof(o.__dict__)

```

**Output:** (Python 3.8, 其他 Python 3 的版本也许稍有不同)
```py
>>> o1 = SomeClass()
>>> o2 = SomeClass()
>>> dict_size(o1)
104
>>> dict_size(o2)
104
>>> del o1.some_attr1
>>> o3 = SomeClass()
>>> dict_size(o3)
232
>>> dict_size(o1)
232
```

让我们在一个新的解释器中再试一次：

```py
>>> o1 = SomeClass()
>>> o2 = SomeClass()
>>> dict_size(o1)
104  # 意料之中
>>> o1.some_attr5 = 5
>>> o1.some_attr6 = 6
>>> dict_size(o1)
360
>>> dict_size(o2)
272
>>> o3 = SomeClass()
>>> dict_size(o3)
232
```

是什么让那些字典变得臃肿？ 为什么新创建的对象也会变臃肿？

#### 💡 说明
+ CPython 能够在多个字典中重用相同的“键”对象。 这添加在 [PEP 412](https://www.python.org/dev/peps/pep-0412/) 中，目的是减少内存使用，特别是在实例字典中 —— 键（实例属性）几乎在所有实例都通用。
+ 这种优化对于实例字典来说是十分自然的，但如果某些假设被打破，它就会被禁用。
+ 密钥共享字典不支持删除；如果删除了实例属性，则字典是“未共享的”，并且同一类的所有未来实例都禁用密钥共享。
+ 另外，如果字典键已被调整大小（因为插入了新键），它们保持共享*仅当*它们被一个完全单一的字典使用时（这允许在第一个创建的实例的 `__init__` 中添加许多属性，而不会导致“取消共享”）。如果发生调整大小时存在多个实例，则为同一类的所有未来实例禁用密钥共享：CPython 无法判断您的实例是否正在使用相同的属性集，并决定放弃尝试共享它们的键值。
+ 一个小提示，如果你的目标是降低程序的内存占用：不要删除实例属性，并确保在 `__init__` 中初始化所有的属性！


---

### > Minor Ones/小知识点

* `join()` 是一个字符串操作而不是列表操作. (第一次接触会觉得有点违反直觉)

  **💡 说明:**
  如果 `join()` 是字符串方法 那么它就可以处理任何可迭代的对象(列表，元组，迭代器). 如果它是列表方法, 则必须在每种类型中单独实现. 另外, 在 `list` 对象的通用API中实现一个专用于字符串的方法没有太大的意义.

* 看着奇怪但能正确运行的语句:
  + `[] = ()` 语句在语义上是正确的 (解包一个空的 `tuple` 并赋值给 `list`)
  + `'a'[0][0][0][0][0]` 在语义上也是正确的, 因为 Python 不像C语言及其派生语言那样，具有字符数据类型。因此，从字符串中选择单个字符将返回单个字符串。
  + `3 --0-- 5 == 8` 和 `--5 == 5` 在语义上都是正确的, 且结果等于 `True`.(译: 3减负0等于3，再减负5相当于加5等于8；负的负5等于5.)

* 鉴于 `a` 是一个数字, `++a` 和 `--a` 都是有效的 Python 语句, 但其效果与 C, C++ 或 Java 等不一样.
  ```py
  >>> a = 5
  >>> a
  5
  >>> ++a
  5
  >>> --a
  5
  ```

  **💡 说明:**
  + python 里没有 `++` 操作符. 这其实是两个 `+` 操作符.
  + `++a` 被解析为 `+(+a)` 最后等于 `a`. `--a` 同理.
  + 这个 StackOverflow [回答](https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python) 讨论了为什么 Python 中缺少增量和减量运算符.

* Python 使用 2个字节存储函数中的本地变量. 理论上, 这意味着函数中只能定义65536个变量. 但是，Python 内置了一个方便的解决方案，可用于存储超过2^16个变量名. 下面的代码演示了当定义了超过65536个局部变量时堆栈中发生的情况 (警告: 这段代码会打印大约2^18行文本, 请做好准备!):
     ```py
     import dis
     exec("""
     def f():
         """ + """
         """.join(["X"+str(x)+"=" + str(x) for x in range(65539)]))

     f()

     print(dis.dis(f))
     ```

* 你的 *Python 代码* 并不会多线程同时运行 (是的, 你没听错!). 虽然你觉得会产生多个线程并让它们同时执行你的代码, 但是, 由于 [全局解释锁](https://wiki.python.org/moin/GlobalInterpreterLock)的存在, 你所做的只是让你的线程依次在同一个核心上执行. Python 多线程适用于IO密集型的任务, 但如果想要并行处理CPU密集型的任务, 你应该会想使用 [multiprocessing](https://docs.python.org/2/library/multiprocessing.html) 模块.

* 列表切片超出索引边界而不引发任何错误
  ```py
  >>> some_list = [1, 2, 3, 4, 5]
  >>> some_list[111:]
  []
  ```

* `int('١٢٣٤٥٦٧٨٩')` 在 Python 3 中会返回 `123456789`. 在 Python 中, 十进制字符包括数字字符, 以及可用于形成十进制数字的所有字符, 例如: U+0660, ARABIC-INDIC DIGIT ZERO. 这有一个关于此的 [有趣故事](http://chris.improbable.org/2014/8/25/adventures-in-unicode-digits/).

* `'abc'.count('') == 4`. 这有一个 `count` 方法的相近实现, 能更好的说明问题
  ```py
  def count(s, sub):
      result = 0
      for i in range(len(s) + 1 - len(sub)):
          result += (s[i:i + len(sub)] == sub)
      return result
  ```
  这个行为是由于空子串(`''`)与原始字符串中长度为0的切片相匹配导致的.

---

# Contributing/贡献

欢迎各种补丁! 详情请看[CONTRIBUTING.md](https://github.com/satwikkansal/wtfpython/blob/master/CONTRIBUTING.md).(译: 这是给原库提贡献的要求模版)

你可以通过新建 [issue](https://github.com/satwikkansal/wtfpython/issues/new) 或者在上 [Gitter](https://gitter.im/wtfpython/Lobby) 与我们进行讨论.

(译: 如果你想对这个翻译项目提供帮助, 请看[这里](https://github.com/leisurelicht/wtfpython-cn/blob/master/CONTRIBUTING.md))

# Acknowledgements/致谢

这个系列最初的想法和设计灵感来自于 Denys Dovhan 的项目 [wtfjs](https://github.com/denysdovhan/wtfjs). 社区的强大支持让它成长为现在的模样.

#### Some nice Links!/一些不错的资源
* https://www.youtube.com/watch?v=sH4XF6pKKmk
* https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python
* https://sopython.com/wiki/Common_Gotchas_In_Python
* https://stackoverflow.com/questions/530530/python-2-x-gotchas-and-landmines
* https://stackoverflow.com/questions/1011431/common-pitfalls-in-python
* https://www.python.org/doc/humor/
* https://www.codementor.io/satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65

# 🎓 License/许可

[![CC 4.0][license-image]][license-url]

&copy; [Satwik Kansal](https://satwikkansal.xyz)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square

## Help/帮助

如果您有任何想法或建议，欢迎分享.

## Surprise your geeky pythonist friends?/想给你的极客朋友一个惊喜?

您可以使用这些快链向 Twitter 和 Linkedin 上的朋友推荐 wtfpython,

[Twitter](https://twitter.com/intent/tweet?url=https://github.com/satwikkansal/wtfpython&hastags=python,wtfpython)
 | [Linkedin](https://www.linkedin.com/shareArticle?url=https://github.com/satwikkansal&title=What%20the%20f*ck%20Python!&summary=An%20interesting%20collection%20of%20subtle%20and%20tricky%20Python%20snippets.)

## Need a pdf version?/需要来一份pdf版的?

你可以快速在[这](https://form.jotform.com/221593245656057)获得英文作者制作的版本.

## Follow Commit/追踪Commit

这是中文版 fork 时所处的原库 Commit, 当原库更新时我会跟随更新.

[![Commit id][commit-image]][commit-url]

[commit-url]: https://github.com/satwikkansal/wtfpython/commit/19d4b075152d93e5bc75c5d08279338a895cfa27
[commit-image]: https://img.shields.io/badge/Commit-19d4b0-yellow.svg

