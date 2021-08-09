<p align="center"><img src="/images/logo.png" alt=""></p>
<h1 align="center">What the f*ck Python! 😱</h1>
<p align="center">Exploring and understanding Python through surprising snippets.</p>

Translations: [Chinese 中文](https://github.com/leisurelicht/wtfpython-cn) | [Vietnamese Tiếng Việt](https://github.com/vuduclyunitn/wtfptyhon-vi) | [Spanish Español](https://github.com/JoseDeFreitas/wtfpython-es) | [Korean 한국어](https://github.com/buttercrab/wtfpython-ko) | [Add translation](https://github.com/satwikkansal/wtfpython/issues/new?title=Add%20translation%20for%20[LANGUAGE]&body=Expected%20time%20to%20finish:%20[X]%20weeks.%20I%27ll%20start%20working%20on%20it%20from%20[Y].)

Other modes: [Interactive](https://colab.research.google.com/github/satwikkansal/wtfpython/blob/master/irrelevant/wtf.ipynb) | [CLI](https://pypi.python.org/pypi/wtfpython)

Python, being a beautifully designed high-level and interpreter-based programming language, provides us with many features for the programmer's comfort. But sometimes, the outcomes of a Python snippet may not seem obvious at first sight.

Here's a fun project attempting to explain what exactly is happening under the hood for some counter-intuitive snippets and lesser-known features in Python.

While some of the examples you see below may not be WTFs in the truest sense, but they'll reveal some of the interesting parts of Python that you might be unaware of. I find it a nice way to learn the internals of a programming language, and I believe that you'll find it interesting too!

If you're an experienced Python programmer, you can take it as a challenge to get most of them right in the first attempt. You may have already experienced some of them before, and I might be able to revive sweet old memories of yours! :sweat_smile:

PS: If you're a returning reader, you can learn about the new modifications [here](https://github.com/satwikkansal/wtfpython/releases/) (the examples marked with asterisk are the ones added in the latest major revision). 

So, here we go...

# Table of Contents

<!-- Generated using "markdown-toc -i README.md --maxdepth 3"-->

<!-- toc -->

- [Structure of the Examples](#structure-of-the-examples)
    + [▶ Some fancy Title](#-some-fancy-title)
- [Usage](#usage)
- [👀 Examples](#-examples)
  * [Section: Strain your brain!](#section-strain-your-brain)
    + [▶ First things first! *](#-first-things-first-)
    + [▶ Strings can be tricky sometimes](#-strings-can-be-tricky-sometimes)
    + [▶ Be careful with chained operations](#-be-careful-with-chained-operations)
    + [▶ How not to use `is` operator](#-how-not-to-use-is-operator)
    + [▶ Hash brownies](#-hash-brownies)
    + [▶ Deep down, we're all the same.](#-deep-down-were-all-the-same)
    + [▶ Disorder within order *](#-disorder-within-order-)
    + [▶ Keep trying... *](#-keep-trying-)
    + [▶ For what?](#-for-what)
    + [▶ Evaluation time discrepancy](#-evaluation-time-discrepancy)
    + [▶ `is not ...` is not `is (not ...)`](#-is-not--is-not-is-not-)
    + [▶ A tic-tac-toe where X wins in the first attempt!](#-a-tic-tac-toe-where-x-wins-in-the-first-attempt)
    + [▶ Schrödinger's variable](#-schrödingers-variable-)
    + [▶ The chicken-egg problem *](#-the-chicken-egg-problem-)
    + [▶ Subclass relationships](#-subclass-relationships)
    + [▶ Methods equality and identity](#-methods-equality-and-identity)
    + [▶ All-true-ation *](#-all-true-ation-)
    + [▶ The surprising comma](#-the-surprising-comma)
    + [▶ Strings and the backslashes](#-strings-and-the-backslashes)
    + [▶ not knot!](#-not-knot)
    + [▶ Half triple-quoted strings](#-half-triple-quoted-strings)
    + [▶ What's wrong with booleans?](#-whats-wrong-with-booleans)
    + [▶ Class attributes and instance attributes](#-class-attributes-and-instance-attributes)
    + [▶ yielding None](#-yielding-none)
    + [▶ Yielding from... return! *](#-yielding-from-return-)
    + [▶ Nan-reflexivity *](#-nan-reflexivity-)
    + [▶ Mutating the immutable!](#-mutating-the-immutable)
    + [▶ The disappearing variable from outer scope](#-the-disappearing-variable-from-outer-scope)
    + [▶ The mysterious key type conversion](#-the-mysterious-key-type-conversion)
    + [▶ Let's see if you can guess this?](#-lets-see-if-you-can-guess-this)
  * [Section: Slippery Slopes](#section-slippery-slopes)
    + [▶ Modifying a dictionary while iterating over it](#-modifying-a-dictionary-while-iterating-over-it)
    + [▶ Stubborn `del` operation](#-stubborn-del-operation)
    + [▶ The out of scope variable](#-the-out-of-scope-variable)
    + [▶ Deleting a list item while iterating](#-deleting-a-list-item-while-iterating)
    + [▶ Lossy zip of iterators *](#-lossy-zip-of-iterators-)
    + [▶ Loop variables leaking out!](#-loop-variables-leaking-out)
    + [▶ Beware of default mutable arguments!](#-beware-of-default-mutable-arguments)
    + [▶ Catching the Exceptions](#-catching-the-exceptions)
    + [▶ Same operands, different story!](#-same-operands-different-story)
    + [▶ Name resolution ignoring class scope](#-name-resolution-ignoring-class-scope)
    + [▶ Rounding like a banker *](#-rounding-like-a-banker-)
    + [▶ Needles in a Haystack *](#-needles-in-a-haystack-)
    + [▶ Splitsies *](#-splitsies-)
    + [▶ Wild imports *](#-wild-imports-)
    + [▶ All sorted? *](#-all-sorted-)
    + [▶ Midnight time doesn't exist?](#-midnight-time-doesnt-exist)
  * [Section: The Hidden treasures!](#section-the-hidden-treasures)
    + [▶ Okay Python, Can you make me fly?](#-okay-python-can-you-make-me-fly)
    + [▶ `goto`, but why?](#-goto-but-why)
    + [▶ Brace yourself!](#-brace-yourself)
    + [▶ Let's meet Friendly Language Uncle For Life](#-lets-meet-friendly-language-uncle-for-life)
    + [▶ Even Python understands that love is complicated](#-even-python-understands-that-love-is-complicated)
    + [▶ Yes, it exists!](#-yes-it-exists)
    + [▶ Ellipsis *](#-ellipsis-)
    + [▶ Inpinity](#-inpinity)
    + [▶ Let's mangle](#-lets-mangle)
  * [Section: Appearances are deceptive!](#section-appearances-are-deceptive)
    + [▶ Skipping lines?](#-skipping-lines)
    + [▶ Teleportation](#-teleportation)
    + [▶ Well, something is fishy...](#-well-something-is-fishy)
  * [Section: Miscellaneous](#section-miscellaneous)
    + [▶ `+=` is faster](#--is-faster)
    + [▶ Let's make a giant string!](#-lets-make-a-giant-string)
    + [▶ Slowing down `dict` lookups *](#-slowing-down-dict-lookups-)
    + [▶ Bloating instance `dict`s *](#-bloating-instance-dicts-)
    + [▶ Minor Ones *](#-minor-ones-)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [🎓 License](#-license)
  * [Surprise your friends as well!](#surprise-your-friends-as-well)
  * [More content like this?](#more-content-like-this)

<!-- tocstop -->

# Structure of the Examples

All the examples are structured like below:

> ### ▶ Some fancy Title
>
> ```py
> # Set up the code.
> # Preparation for the magic...
> ```
>
> **Output (Python version(s)):**
>
> ```py
> >>> triggering_statement
> Some unexpected output
> ```
> (Optional): One line describing the unexpected output.
>
>
> #### 💡 Explanation:
>
> * Brief explanation of what's happening and why is it happening.
> ```py
> # Set up code
> # More examples for further clarification (if necessary)
> ```
> **Output (Python version(s)):**
>
> ```py
> >>> trigger # some example that makes it easy to unveil the magic
> # some justified output
> ```

**Note:** All the examples are tested on Python 3.5.2 interactive interpreter, and they should work for all the Python versions unless explicitly specified before the output.

# Usage

A nice way to get the most out of these examples, in my opinion, is to read them chronologically, and for every example:
- Carefully read the initial code for setting up the example. If you're an experienced Python programmer, you'll successfully anticipate what's going to happen next most of the time.
- Read the output snippets and,
  + Check if the outputs are the same as you'd expect.
  + Make sure if you know the exact reason behind the output being the way it is.
    - If the answer is no (which is perfectly okay), take a deep breath, and read the explanation (and if you still don't understand, shout out! and create an issue [here](https://github.com/satwikkansal/wtfpython/issues/new)).
    - If yes, give a gentle pat on your back, and you may skip to the next example.

PS: You can also read WTFPython at the command line using the [pypi package](https://pypi.python.org/pypi/wtfpython),
```sh
$ pip install wtfpython -U
$ wtfpython
```
---

# 👀 Examples

## Section: Strain your brain!

### ▶ First things first! *

<!-- Example ID: d3d73936-3cf1-4632-b5ab-817981338863 -->
<!-- read-only -->

For some reason, the Python 3.8's "Walrus" operator (`:=`) has become quite popular. Let's check it out,

1\.

```py
# Python version 3.8+

>>> a = "wtf_walrus"
>>> a
'wtf_walrus'

>>> a := "wtf_walrus"
File "<stdin>", line 1
    a := "wtf_walrus"
      ^
SyntaxError: invalid syntax

>>> (a := "wtf_walrus") # This works though
'wtf_walrus'
>>> a
'wtf_walrus'
```

2 \.

```py
# Python version 3.8+

>>> a = 6, 9
>>> a
(6, 9)

>>> (a := 6, 9)
(6, 9)
>>> a
6

>>> a, b = 6, 9 # Typical unpacking
>>> a, b
(6, 9)
>>> (a, b = 16, 19) # Oops
  File "<stdin>", line 1
    (a, b = 16, 19)
          ^
SyntaxError: invalid syntax

>>> (a, b := 16, 19) # This prints out a weird 3-tuple
(6, 16, 19)

>>> a # a is still unchanged?
6

>>> b
16
```



#### 💡 Explanation

**Quick walrus operator refresher**

The Walrus operator (`:=`) was introduced in Python 3.8, it can be useful in situations where you'd want to assign values to variables within an expression.

```py
def some_func():
        # Assume some expensive computation here
        # time.sleep(1000)
        return 5

# So instead of,
if some_func():
        print(some_func()) # Which is bad practice since computation is happening twice

# or
a = some_func()
if a:
    print(a)

# Now you can concisely write
if a := some_func():
        print(a)
```

**Output (> 3.8):**

```py
5
5
5
```

This saved one line of code, and implicitly prevented invoking `some_func` twice.

- Unparenthesized "assignment expression" (use of walrus operator), is restricted at the top level, hence the `SyntaxError` in the `a := "wtf_walrus"` statement of the first snippet. Parenthesizing it worked as expected and assigned `a`.  

- As usual, parenthesizing of an expression containing `=` operator is not allowed. Hence the syntax error in `(a, b = 6, 9)`. 

- The syntax of the Walrus operator is of the form `NAME:= expr`, where `NAME` is a valid identifier, and `expr` is a valid expression. Hence, iterable packing and unpacking are not supported which means, 

  - `(a := 6, 9)` is equivalent to `((a := 6), 9)` and ultimately `(a, 9) ` (where `a`'s value is 6')

    ```py
    >>> (a := 6, 9) == ((a := 6), 9)
    True
    >>> x = (a := 696, 9)
    >>> x
    (696, 9)
    >>> x[0] is a # Both reference same memory location
    True
    ```

  - Similarly, `(a, b := 16, 19)` is equivalent to `(a, (b := 16), 19)` which is nothing but a 3-tuple. 

---

### ▶ Strings can be tricky sometimes

<!-- Example ID: 30f1d3fc-e267-4b30-84ef-4d9e7091ac1a --->
1\.

```py
>>> a = "some_string"
>>> id(a)
140420665652016
>>> id("some" + "_" + "string") # Notice that both the ids are same.
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

```

3\.

```py
>>> a, b = "wtf!", "wtf!"
>>> a is b # All versions except 3.7.x
True

>>> a = "wtf!"; b = "wtf!"
>>> a is b # This will print True or False depending on where you're invoking it (python shell / ipython / as a script)
False
```

```py
# This time in file some_file.py
a = "wtf!"
b = "wtf!"
print(a is b)

# prints True when the module is invoked!
```

4\.

**Output (< Python3.7 )**

```py
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
```

Makes sense, right?

#### 💡 Explanation:
+ The behavior in first and second snippets is due to a CPython optimization (called string interning) that tries to use existing immutable objects in some cases rather than creating a new object every time.
+ After being "interned," many variables may reference the same string object in memory (saving memory thereby).
+ In the snippets above, strings are implicitly interned. The decision of when to implicitly intern a string is implementation-dependent. There are some rules that can be used to guess if a string will be interned or not:
  * All length 0 and length 1 strings are interned.
  * Strings are interned at compile time (`'wtf'` will be interned but `''.join(['w', 't', 'f'])` will not be interned)
  * Strings that are not composed of ASCII letters, digits or underscores, are not interned. This explains why `'wtf!'` was not interned due to `!`. CPython implementation of this rule can be found [here](https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19)
  ![image](/images/string-intern/string_intern.png)
+ When `a` and `b` are set to `"wtf!"` in the same line, the Python interpreter creates a new object, then references the second variable at the same time. If you do it on separate lines, it doesn't "know" that there's already `"wtf!"` as an object (because `"wtf!"` is not implicitly interned as per the facts mentioned above). It's a compile-time optimization. This optimization doesn't apply to 3.7.x versions of CPython (check this [issue](https://github.com/satwikkansal/wtfpython/issues/100) for more discussion).
+ A compile unit in an interactive environment like IPython consists of a single statement, whereas it consists of the entire module in case of modules. `a, b = "wtf!", "wtf!"` is single statement, whereas `a = "wtf!"; b = "wtf!"` are two statements in a single line. This explains why the identities are different in `a = "wtf!"; b = "wtf!"`, and also explain why they are same when invoked in `some_file.py`
+ The abrupt change in the output of the fourth snippet is due to a [peephole optimization](https://en.wikipedia.org/wiki/Peephole_optimization) technique known as Constant folding. This means the expression `'a'*20` is replaced by `'aaaaaaaaaaaaaaaaaaaa'` during compilation to save a  few clock cycles during runtime. Constant folding only occurs for strings having a length of less than 21. (Why? Imagine the size of `.pyc` file generated as a result of the expression `'a'*10**10`). [Here's](https://github.com/python/cpython/blob/3.6/Python/peephole.c#L288) the implementation source for the same.
+ Note: In Python 3.7, Constant folding was moved out from peephole optimizer to the new AST optimizer with some change in logic as well, so the fourth snippet doesn't work for Python 3.7. You can read more about the change [here](https://bugs.python.org/issue11549). 

---


### ▶ Be careful with chained operations
<!-- Example ID: 07974979-9c86-4720-80bd-467aa19470d9 --->
```py
>>> (False == False) in [False] # makes sense
False
>>> False == (False in [False]) # makes sense
False
>>> False == False in [False] # now what?
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

#### 💡 Explanation:

As per https://docs.python.org/3/reference/expressions.html#membership-test-operations

> Formally, if a, b, c, ..., y, z are expressions and op1, op2, ..., opN are comparison operators, then a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z, except that each expression is evaluated at most once.

While such behavior might seem silly to you in the above examples, it's fantastic with stuff like `a == b == c` and `0 <= x <= 100`.

* `False is False is False` is equivalent to `(False is False) and (False is False)`
* `True is False == False` is equivalent to `True is False and False == False` and since the first part of the statement (`True is False`) evaluates to `False`, the overall expression evaluates to `False`.
* `1 > 0 < 1` is equivalent to `1 > 0 and 0 < 1` which evaluates to `True`.
* The expression `(1 > 0) < 1` is equivalent to `True < 1` and
  ```py
  >>> int(True)
  1
  >>> True + 1 #not relevant for this example, but just for fun
  2
  ```
  So, `1 < 1` evaluates to `False`

---

### ▶ How not to use `is` operator
<!-- Example ID: 230fa2ac-ab36-4ad1-b675-5f5a1c1a6217 --->
The following is a very famous example present all over the internet.

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
>> a is b
False
```

#### 💡 Explanation:

**The difference between `is` and `==`**

* `is` operator checks if both the operands refer to the same object (i.e., it checks if the identity of the operands matches or not).
* `==` operator compares the values of both the operands and checks if they are the same.
* So `is` is for reference equality and `==` is for value equality. An example to clear things up,
  ```py
  >>> class A: pass
  >>> A() is A() # These are two empty objects at two different memory locations.
  False
  ```

**`256` is an existing object but `257` isn't**

When you start up python the numbers from `-5` to `256` will be allocated. These numbers are used a lot, so it makes sense just to have them ready.

Quoting from https://docs.python.org/3/c-api/long.html
> The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behavior of Python, in this case, is undefined. :-)

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

Here the interpreter isn't smart enough while executing `y = 257` to recognize that we've already created an integer of the value `257,` and so it goes on to create another object in the memory.

Similar optimization applies to other **immutable** objects like empty tuples as well. Since lists are mutable, that's why `[] is []` will return `False` and `() is ()` will return `True`. This explains our second snippet. Let's move on to the third one, 

**Both `a` and `b` refer to the same object when initialized with same value in the same line.**

**Output**

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

* When a and b are set to `257` in the same line, the Python interpreter creates a new object, then references the second variable at the same time. If you do it on separate lines, it doesn't "know" that there's already `257` as an object.

* It's a compiler optimization and specifically applies to the interactive environment. When you enter two lines in a live interpreter, they're compiled separately, therefore optimized separately. If you were to try this example in a `.py` file, you would not see the same behavior, because the file is compiled all at once. This optimization is not limited to integers, it works for other immutable data types like strings (check the "Strings are tricky example") and floats as well,

  ```py
  >>> a, b = 257.0, 257.0
  >>> a is b
  True
  ```

* Why didn't this work for Python 3.7? The abstract reason is because such compiler optimizations are implementation specific (i.e. may change with version, OS, etc). I'm still figuring out what exact implementation change cause the issue, you can check out this [issue](https://github.com/satwikkansal/wtfpython/issues/100) for updates.

---


### ▶ Hash brownies
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
>>> some_dict[5.0] # "Python" destroyed the existence of "Ruby"?
"Python"
>>> some_dict[5] 
"Python"

>>> complex_five = 5 + 0j
>>> type(complex_five)
complex
>>> some_dict[complex_five]
"Python"
```

So, why is Python all over the place?


#### 💡 Explanation

* Uniqueness of keys in a Python dictionary is by *equivalence*, not identity. So even though `5`, `5.0`, and `5 + 0j` are distinct objects of different types, since they're equal, they can't both be in the same `dict` (or `set`). As soon as you insert any one of them, attempting to look up any distinct but equivalent key will succeed with the original mapped value (rather than failing with a `KeyError`):
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
* This applies when setting an item as well. So when you do `some_dict[5] = "Python"`, Python finds the existing item with equivalent key `5.0 -> "Ruby"`, overwrites its value in place, and leaves the original key alone.
  ```py
  >>> some_dict
  {5.0: 'Ruby'}
  >>> some_dict[5] = "Python"
  >>> some_dict
  {5.0: 'Python'}
  ```
* So how can we update the key to `5` (instead of `5.0`)? We can't actually do this update in place, but what we can do is first delete the key (`del some_dict[5.0]`), and then set it (`some_dict[5]`) to get the integer `5` as the key instead of floating `5.0`, though this should be needed in rare cases.

* How did Python find `5` in a dictionary containing `5.0`? Python does this in constant time without having to scan through every item by using hash functions. When Python looks up a key `foo` in a dict, it first computes `hash(foo)` (which runs in constant-time). Since in Python it is required that objects that compare equal also have the same hash value ([docs](https://docs.python.org/3/reference/datamodel.html#object.__hash__) here), `5`, `5.0`, and `5 + 0j` have the same hash value.
  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> hash(5) == hash(5.0) == hash(5 + 0j)
  True
  ```
  **Note:** The inverse is not necessarily true: Objects with equal hash values may themselves be unequal. (This causes what's known as a [hash collision](https://en.wikipedia.org/wiki/Collision_(computer_science)), and degrades the constant-time performance that hashing usually provides.)

---

### ▶ Deep down, we're all the same.
<!-- Example ID: 8f99a35f-1736-43e2-920d-3b78ec35da9b --->
```py
class WTF:
  pass
```

**Output:**
```py
>>> WTF() == WTF() # two different instances can't be equal
False
>>> WTF() is WTF() # identities are also different
False
>>> hash(WTF()) == hash(WTF()) # hashes _should_ be different as well
True
>>> id(WTF()) == id(WTF())
True
```

#### 💡 Explanation:

* When `id` was called, Python created a `WTF` class object and passed it to the `id` function. The `id` function takes its `id` (its memory location), and throws away the object. The object is destroyed.
* When we do this twice in succession, Python allocates the same memory location to this second object as well. Since (in CPython) `id` uses the memory location as the object id, the id of the two objects is the same.
* So, the object's id is unique only for the lifetime of the object. After the object is destroyed, or before it is created, something else can have the same id.
* But why did the `is` operator evaluated to `False`? Let's see with this snippet.
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
  As you may observe, the order in which the objects are destroyed is what made all the difference here.

---

### ▶ Disorder within order *
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
    A dict that also implements __hash__ magic.
    """
    __hash__ = lambda self: 0

class OrderedDictWithHash(OrderedDict):
    """
    An OrderedDict that also implements __hash__ magic.
    """
    __hash__ = lambda self: 0
```

**Output**
```py
>>> dictionary == ordered_dict # If a == b
True
>>> dictionary == another_ordered_dict # and b == c
True
>>> ordered_dict == another_ordered_dict # then why isn't c == a ??
False

# We all know that a set consists of only unique elements,
# let's try making a set of these dictionaries and see what happens...

>>> len({dictionary, ordered_dict, another_ordered_dict})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

# Makes sense since dict don't have __hash__ implemented, let's use
# our wrapper classes.
>>> dictionary = DictWithHash()
>>> dictionary[1] = 'a'; dictionary[2] = 'b';
>>> ordered_dict = OrderedDictWithHash()
>>> ordered_dict[1] = 'a'; ordered_dict[2] = 'b';
>>> another_ordered_dict = OrderedDictWithHash()
>>> another_ordered_dict[2] = 'b'; another_ordered_dict[1] = 'a';
>>> len({dictionary, ordered_dict, another_ordered_dict})
1
>>> len({ordered_dict, another_ordered_dict, dictionary}) # changing the order
2
```

What is going on here?

#### 💡 Explanation:

- The reason why intransitive equality didn't hold among `dictionary`, `ordered_dict` and `another_ordered_dict` is because of the way `__eq__` method is implemented in `OrderedDict` class. From the [docs](https://docs.python.org/3/library/collections.html#ordereddict-objects)
  
    > Equality tests between OrderedDict objects are order-sensitive and are implemented as `list(od1.items())==list(od2.items())`. Equality tests between `OrderedDict` objects and other Mapping objects are order-insensitive like regular dictionaries.
- The reason for this equality in behavior is that it allows `OrderedDict` objects to be directly substituted anywhere a regular dictionary is used.
- Okay, so why did changing the order affect the length of the generated `set` object? The answer is the lack of intransitive equality only. Since sets are "unordered" collections of unique elements, the order in which elements are inserted shouldn't matter. But in this case, it does matter. Let's break it down a bit,
    ```py
    >>> some_set = set()
    >>> some_set.add(dictionary) # these are the mapping objects from the snippets above
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
    So the inconsistency is due to `another_ordered_dict in another_set` being `False` because `ordered_dict` was already present in `another_set` and as observed before, `ordered_dict == another_ordered_dict` is `False`.

---

### ▶ Keep trying... *
<!-- Example ID: b4349443-e89f-4d25-a109-82616be9d41a --->
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

#### 💡 Explanation:

- When a `return`, `break` or `continue` statement is executed in the `try` suite of a "try…finally" statement, the `finally` clause is also executed on the way out.
- The return value of a function is determined by the last `return` statement executed. Since the `finally` clause always executes, a `return` statement executed in the `finally` clause will always be the last one executed.
- The caveat here is, if the finally clause executes a `return` or `break` statement, the temporarily saved exception is discarded.

---


### ▶ For what?
<!-- Example ID: 64a9dccf-5083-4bc9-98aa-8aeecde4f210 --->
```py
some_string = "wtf"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    i = 10
```

**Output:**
```py
>>> some_dict # An indexed dict appears.
{0: 'w', 1: 't', 2: 'f'}
```

####  💡 Explanation:

* A `for` statement is defined in the [Python grammar](https://docs.python.org/3/reference/grammar.html) as:
  ```
  for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
  ```
  Where `exprlist` is the assignment target. This means that the equivalent of `{exprlist} = {next_value}` is **executed for each item** in the iterable.
  An interesting example that illustrates this:
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

  Did you expect the loop to run just once?

  **💡 Explanation:**

  - The assignment statement `i = 10` never affects the iterations of the loop because of the way for loops work in Python. Before the beginning of every iteration, the next item provided by the iterator (`range(4)` in this case) is unpacked and assigned the target list variables (`i` in this case).

* The `enumerate(some_string)` function yields a new value `i` (a counter going up) and a character from the `some_string` in each iteration. It then sets the (just assigned) `i` key of the dictionary `some_dict` to that character. The unrolling of the loop can be simplified as:
  ```py
  >>> i, some_dict[i] = (0, 'w')
  >>> i, some_dict[i] = (1, 't')
  >>> i, some_dict[i] = (2, 'f')
  >>> some_dict
  ```

---

### ▶ Evaluation time discrepancy
<!-- Example ID: 6aa11a4b-4cf1-467a-b43a-810731517e98 --->
1\.
```py
array = [1, 8, 15]
# A typical generator expression
gen = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
```

**Output:**

```py
>>> print(list(gen)) # Where did the other values go?
[8]
```

2\.

```py
array_1 = [1,2,3,4]
gen_1 = (x for x in array_1)
array_1 = [1,2,3,4,5]

array_2 = [1,2,3,4]
gen_2 = (x for x in array_2)
array_2[:] = [1,2,3,4,5]
```

**Output:**
```py
>>> print(list(gen_1))
[1, 2, 3, 4]

>>> print(list(gen_2))
[1, 2, 3, 4, 5]
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

#### 💡 Explanation

- In a [generator](https://wiki.python.org/moin/Generators) expression, the `in` clause is evaluated at declaration time, but the conditional clause is evaluated at runtime.
- So before runtime, `array` is re-assigned to the list `[2, 8, 22]`, and since out of `1`, `8` and `15`, only the count of `8` is greater than `0`, the generator only yields `8`.
- The differences in the output of `g1` and `g2` in the second part is due the way variables `array_1` and `array_2` are re-assigned values.
- In the first case, `array_1` is binded to the new object `[1,2,3,4,5]` and since the `in` clause is evaluated at the declaration time it still refers to the old object `[1,2,3,4]` (which is not destroyed).
- In the second case, the slice assignment to `array_2` updates the same old object `[1,2,3,4]` to `[1,2,3,4,5]`. Hence both the `g2` and `array_2` still have reference to the same object (which has now been updated to `[1,2,3,4,5]`).
- Okay, going by the logic discussed so far, shouldn't be the value of `list(gen)` in the third snippet be `[11, 21, 31, 12, 22, 32, 13, 23, 33]`? (because `array_3` and `array_4` are going to behave just like `array_1`). The reason why (only) `array_4` values got updated is explained in [PEP-289](https://www.python.org/dev/peps/pep-0289/#the-details)
  
    > Only the outermost for-expression is evaluated immediately, the other expressions are deferred until the generator is run.

---


### ▶ `is not ...` is not `is (not ...)`
<!-- Example ID: b26fb1ed-0c7d-4b9c-8c6d-94a58a055c0d --->
```py
>>> 'something' is not None
True
>>> 'something' is (not None)
False
```

#### 💡 Explanation

- `is not` is a single binary operator, and has behavior different than using `is` and `not` separated.
- `is not` evaluates to `False` if the variables on either side of the operator point to the same object and `True` otherwise. 
- In the example, `(not None)` evaluates to `True` since the value `None` is `False` in a boolean context, so the expression becomes `'something' is True`.

---

### ▶ A tic-tac-toe where X wins in the first attempt!
<!-- Example ID: 69329249-bdcb-424f-bd09-cca2e6705a7a --->

```py
# Let's initialize a row
row = [""] * 3 #row i['', '', '']
# Let's make a board
board = [row] * 3
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

We didn't assign three `"X"`s, did we?

#### 💡 Explanation:

When we initialize `row` variable, this visualization explains what happens in the memory

![image](/images/tic-tac-toe/after_row_initialized.png)

And when the `board` is initialized by multiplying the `row`, this is what happens inside the memory (each of the elements `board[0]`, `board[1]` and `board[2]` is a reference to the same list referred by `row`)

![image](/images/tic-tac-toe/after_board_initialized.png)

We can avoid this scenario here by not using `row` variable to generate `board`. (Asked in [this](https://github.com/satwikkansal/wtfpython/issues/68) issue).

```py
>>> board = [['']*3 for _ in range(3)]
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['', '', ''], ['', '', '']]
```

---

### ▶ Schrödinger's variable *
<!-- Example ID: 4dc42f77-94cb-4eb5-a120-8203d3ed7604 --->


```py
funcs = []
results = []
for x in range(7):
    def some_func():
        return x
    funcs.append(some_func)
    results.append(some_func())  # note the function call here

funcs_results = [func() for func in funcs]
```

**Output (Python version):**
```py
>>> results
[0, 1, 2, 3, 4, 5, 6]
>>> funcs_results
[6, 6, 6, 6, 6, 6, 6]
```

The values of `x` were different in every iteration prior to appending `some_func` to `funcs`, but all the functions return 6 when they're evaluated after the loop completes.

2.

```py
>>> powers_of_x = [lambda x: x**i for i in range(10)]
>>> [f(2) for f in powers_of_x]
[512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
```

#### 💡 Explanation:
* When defining a function inside a loop that uses the loop variable in its body, the loop function's closure is bound to the *variable*, not its *value*. The function looks up `x` in the surrounding context, rather than using the value of `x` at the time the function is created. So all of the functions use the latest value assigned to the variable for computation. We can see that it's using the `x` from the surrounding context (i.e. *not* a local variable) with:
```py
>>> import inspect
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={'x': 6}, builtins={}, unbound=set())
```
Since `x` is a global value, we can change the value that the `funcs` will lookup and return by updating `x`:

```py
>>> x = 42
>>> [func() for func in funcs]
[42, 42, 42, 42, 42, 42, 42]
```

* To get the desired behavior you can pass in the loop variable as a named variable to the function. **Why does this work?** Because this will define the variable *inside* the function's scope. It will no longer go to the surrounding (global) scope to look up the variables value but will create a local variable that stores the value of `x` at that point in time.

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

It is not longer using the `x` in the global scope:

```py
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={}, builtins={}, unbound=set())
```

---

### ▶ The chicken-egg problem *
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

So which is the "ultimate" base class? There's more to the confusion by the way,

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


#### 💡 Explanation

- `type` is a [metaclass](https://realpython.com/python-metaclasses/) in Python.
- **Everything** is an `object` in Python, which includes classes as well as their objects (instances).
- class `type` is the metaclass of class `object`, and every class (including `type`) has inherited directly or indirectly from `object`.
- There is no real base class among `object` and `type`. The confusion in the above snippets is arising because we're thinking about these relationships (`issubclass` and `isinstance`) in terms of Python classes. The relationship between `object` and `type` can't be reproduced in pure python. To be more precise the following relationships can't be reproduced in pure Python,
    + class A is an instance of class B, and class B is an instance of class A.
    + class A is an instance of itself.
- These relationships between `object` and `type` (both being instances of each other as well as themselves) exist in Python because of "cheating" at the implementation level.

---

### ▶ Subclass relationships
<!-- Example ID: 9f6d8cf0-e1b5-42d0-84a0-4cfab25a0bc0 --->
**Output:**
```py
>>> from collections import Hashable
>>> issubclass(list, object)
True
>>> issubclass(object, Hashable)
True
>>> issubclass(list, Hashable)
False
```

The Subclass relationships were expected to be transitive, right? (i.e., if `A` is a subclass of `B`, and `B` is a subclass of `C`, the `A` _should_ a subclass of `C`)

#### 💡 Explanation:

* Subclass relationships are not necessarily transitive in Python. Anyone is allowed to define their own, arbitrary `__subclasscheck__` in a metaclass.
* When `issubclass(cls, Hashable)` is called, it simply looks for non-Falsey "`__hash__`" method in `cls` or anything it inherits from.
* Since `object` is hashable, but `list` is non-hashable, it breaks the transitivity relation.
* More detailed explanation can be found [here](https://www.naftaliharris.com/blog/python-subclass-intransitivity/).

---

### ▶ Methods equality and identity
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

Accessing `classm` twice, we get an equal object, but not the *same* one? Let's see what happens
with instances of `SomeClass`:

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

Accessing` classm` or `method` twice, creates equal but not *same* objects for the same instance of `SomeClass`.

#### 💡 Explanation
* Functions are [descriptors](https://docs.python.org/3/howto/descriptor.html). Whenever a function is accessed as an
attribute, the descriptor is invoked, creating a method object which "binds" the function with the object owning the
attribute. If called, the method calls the function, implicitly passing the bound object as the first argument
(this is how we get `self` as the first argument, despite not passing it explicitly).
```py
>>> o1.method
<bound method SomeClass.method of <__main__.SomeClass object at ...>>
```
* Accessing the attribute multiple times creates a method object every time! Therefore `o1.method is o1.method` is
never truthy. Accessing functions as class attributes (as opposed to instance) does not create methods, however; so
`SomeClass.method is SomeClass.method` is truthy.
```py
>>> SomeClass.method
<function SomeClass.method at ...>
```
* `classmethod` transforms functions into class methods. Class methods are descriptors that, when accessed, create
a method object which binds the *class* (type) of the object, instead of the object itself.
```py
>>> o1.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* Unlike functions, `classmethod`s will create a method also when accessed as class attributes (in which case they
bind the class, not to the type of it). So `SomeClass.classm is SomeClass.classm` is falsy.
```py
>>> SomeClass.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* A method object compares equal when both the functions are equal, and the bound objects are the same. So
`o1.method == o1.method` is truthy, although not the same object in memory.
* `staticmethod` transforms functions into a "no-op" descriptor, which returns the function as-is. No method
objects are ever created, so comparison with `is` is truthy.
```py
>>> o1.staticm
<function SomeClass.staticm at ...>
>>> SomeClass.staticm
<function SomeClass.staticm at ...>
```
* Having to create new "method" objects every time Python calls instance methods and having to modify the arguments
every time in order to insert `self` affected performance badly.
CPython 3.7 [solved it](https://bugs.python.org/issue26110) by introducing new opcodes that deal with calling methods
without creating the temporary method objects. This is used only when the accessed function is actually called, so the
snippets here are not affected, and still generate methods :)

### ▶ All-true-ation *

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

Why's this True-False alteration?

#### 💡 Explanation:

- The implementation of `all` function is equivalent to

- ```py
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

- `all([])` returns `True` since the iterable is empty. 
- `all([[]])` returns `False` because the passed array has one element, `[]`, and in python, an empty list is falsy.
- `all([[[]]])` and higher recursive variants are always `True`. This is because the passed array's single element (`[[...]]`) is no longer empty, and lists with values are truthy.

---

### ▶ The surprising comma
<!-- Example ID: 31a819c8-ed73-4dcc-84eb-91bedbb51e58 --->
**Output (< 3.6):**

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

#### 💡 Explanation:

- Trailing comma is not always legal in formal parameters list of a Python function.
-  In Python, the argument list is defined partially with leading commas and partially with trailing commas. This conflict causes situations where a comma is trapped in the middle, and no rule accepts it.
-  **Note:** The trailing comma problem is [fixed in Python 3.6](https://bugs.python.org/issue9232). The remarks in [this](https://bugs.python.org/issue9232#msg248399) post discuss in brief different usages of trailing commas in Python.

---

### ▶ Strings and the backslashes
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

#### 💡 Explanation

- In a usual python string, the backslash is used to escape characters that may have a special meaning (like single-quote, double-quote, and the backslash itself).
    ```py
    >>> "wt\"f"
    'wt"f'
    ```
- In a raw string literal (as indicated by the prefix `r`),  the backslashes pass themselves as is along with the behavior of escaping the following character.
    ```py
    >>> r'wt\"f' == 'wt\\"f'
    True
    >>> print(repr(r'wt\"f')
    'wt\\"f'

    >>> print("\n")

    >>> print(r"\\n")
    '\\n'
    ```
- This means when a parser encounters a backslash in a raw string, it expects another character following it. And in our case (`print(r"\")`), the backslash escaped the trailing quote, leaving the parser without a terminating quote (hence the `SyntaxError`). That's why backslashes don't work at the end of a raw string.

---

### ▶ not knot!
<!-- Example ID: 7034deb1-7443-417d-94ee-29a800524de8 --->
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

#### 💡 Explanation:

* Operator precedence affects how an expression is evaluated, and `==` operator has higher precedence than `not` operator in Python.
* So `not x == y` is equivalent to `not (x == y)` which is equivalent to `not (True == False)` finally evaluating to `True`.
* But `x == not y` raises a `SyntaxError` because it can be thought of being equivalent to `(x == not) y` and not `x == (not y)` which you might have expected at first sight.
* The parser expected the `not` token to be a part of the `not in` operator (because both `==` and `not in` operators have the same precedence), but after not being able to find an `in` token following the `not` token, it raises a `SyntaxError`.

---

### ▶ Half triple-quoted strings
<!-- Example ID: c55da3e2-1034-43b9-abeb-a7a970a2ad9e --->
**Output:**
```py
>>> print('wtfpython''')
wtfpython
>>> print("wtfpython""")
wtfpython
>>> # The following statements raise `SyntaxError`
>>> # print('''wtfpython')
>>> # print("""wtfpython")
  File "<input>", line 3
    print("""wtfpython")
                        ^
SyntaxError: EOF while scanning triple-quoted string literal
```

#### 💡 Explanation:
+ Python supports implicit [string literal concatenation](https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation), Example,
  ```
  >>> print("wtf" "python")
  wtfpython
  >>> print("wtf" "") # or "wtf"""
  wtf
  ```
+ `'''` and `"""` are also string delimiters in Python which causes a SyntaxError because the Python interpreter was expecting a terminating triple quote as delimiter while scanning the currently encountered triple quoted string literal.

---

### ▶ What's wrong with booleans?
<!-- Example ID: 0bba5fa7-9e6d-4cd2-8b94-952d061af5dd --->
1\.

```py
# A simple example to count the number of booleans and
# integers in an iterable of mixed data types.
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



#### 💡 Explanation:

* `bool` is a subclass of `int` in Python
    
    ```py
    >>> issubclass(bool, int)
    True
    >>> issubclass(int, bool)
    False
    ```
    
* And thus, `True` and `False` are instances of `int`
  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

* The integer value of `True` is `1` and that of `False` is `0`.
  ```py
  >>> int(True)
  1
  >>> int(False)
  0
  ```

* See this StackOverflow [answer](https://stackoverflow.com/a/8169049/4354153) for the rationale behind it.

* Initially, Python used to have no `bool` type (people used 0 for false and non-zero value like 1 for true).  `True`, `False`, and a `bool` type was added in 2.x versions, but, for backward compatibility, `True` and `False` couldn't be made constants. They just were built-in variables, and it was possible to reassign them

* Python 3 was backward-incompatible, the issue was finally fixed, and thus the last snippet won't work with Python 3.x!

---

### ▶ Class attributes and instance attributes
<!-- Example ID: 6f332208-33bd-482d-8106-42863b739ed9 --->
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
>>> A.x, B.x, C.x # C.x changed, but B.x didn't
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

#### 💡 Explanation:

* Class variables and variables in class instances are internally handled as dictionaries of a class object. If a variable name is not found in the dictionary of the current class, the parent classes are searched for it.
* The `+=` operator modifies the mutable object in-place without creating a new object. So changing the attribute of one instance affects the other instances and the class attribute as well.

---

### ▶ yielding None
<!-- Example ID: 5a40c241-2c30-40d0-8ba9-cf7e097b3b53 --->
```py
some_iterable = ('a', 'b')

def some_func(val):
    return "something"
```

**Output (<= 3.7.x):**

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

#### 💡 Explanation:
- This is a bug in CPython's handling of `yield` in generators and comprehensions.
- Source and explanation can be found here: https://stackoverflow.com/questions/32139885/yield-in-list-comprehensions-and-generator-expressions
- Related bug report: https://bugs.python.org/issue10544
- Python 3.8+ no longer allows `yield` inside list comprehension and will throw a `SyntaxError`.

---


### ▶ Yielding from... return! *
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

Where did the `"wtf"` go? Is it due to some special effect of `yield from`? Let's validate that,

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

The same result, this didn't work either.

#### 💡 Explanation:

+ From Python 3.3 onwards, it became possible to use `return` statement with values inside generators (See [PEP380](https://www.python.org/dev/peps/pep-0380/)). The [official docs](https://www.python.org/dev/peps/pep-0380/#enhancements-to-stopiteration) say that,

> "... `return expr` in a generator causes `StopIteration(expr)` to be raised upon exit from the generator."

+ In the case of `some_func(3)`, `StopIteration` is raised at the beginning because of `return` statement. The `StopIteration` exception is automatically caught inside the `list(...)` wrapper and the `for` loop. Therefore, the above two snippets result in an empty list.

+ To get `["wtf"]` from the generator `some_func` we need to catch the `StopIteration` exception,

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

### ▶ Nan-reflexivity *

<!-- Example ID: 59bee91a-36e0-47a4-8c7d-aa89bf1d3976 --->

1\.

```py
a = float('inf')
b = float('nan')
c = float('-iNf')  # These strings are case-insensitive
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
>>> a == -c # inf==inf
True
>>> None == None # None == None
True
>>> b == d # but nan!=nan
False
>>> 50 / a
0.0
>>> a / a
nan
>>> 23 + b
nan
```

2\.

```py
>>> x = float('nan')
>>> y = x / x
>>> y is y # identity holds
True
>>> y == y # equality fails of y
False
>>> [y] == [y] # but the equality succeeds for the list containing y
True
```



#### 💡 Explanation:

- `'inf'` and `'nan'` are special strings (case-insensitive), which, when explicitly typecast-ed to `float` type, are used to represent mathematical "infinity" and "not a number" respectively.

- Since according to IEEE standards ` NaN != NaN`, obeying this rule breaks the reflexivity assumption of a collection element in Python i.e. if `x` is a part of a collection like `list`, the implementations like comparison are based on the assumption that `x == x`.  Because of this assumption, the identity is compared first (since it's faster) while comparing two elements, and the values are compared only when the identities mismatch. The following snippet will make things clearer,

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

  Since the identities of `x` and `y` are different, the values are considered, which are also different; hence the comparison returns `False` this time.

- Interesting read: [Reflexivity, and other pillars of civilization](https://bertrandmeyer.com/2010/02/06/reflexivity-and-other-pillars-of-civilization/)

---

### ▶ Mutating the immutable!

<!-- Example ID: 15a9e782-1695-43ea-817a-a9208f6bb33d --->

This might seem trivial if you know how references work in Python.

```py
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
```

**Output:**
```py
>>> some_tuple[2] = "change this"
TypeError: 'tuple' object does not support item assignment
>>> another_tuple[2].append(1000) #This throws no error
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000])
>>> another_tuple[2] += [99, 999]
TypeError: 'tuple' object does not support item assignment
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000, 99, 999])
```

But I thought tuples were immutable...

#### 💡 Explanation:

* Quoting from https://docs.python.org/3/reference/datamodel.html

    > Immutable sequences
        An object of an immutable sequence type cannot change once it is created. (If the object contains references to other objects, these other objects may be mutable and may be modified; however, the collection of objects directly referenced by an immutable object cannot change.)

* `+=` operator changes the list in-place. The item assignment doesn't work, but when the exception occurs, the item has already been changed in place.
* There's also an explanation in [official Python FAQ](https://docs.python.org/3/faq/programming.html#why-does-a-tuple-i-item-raise-an-exception-when-the-addition-works).

---

### ▶ The disappearing variable from outer scope
<!-- Example ID: 7f1e71b6-cb3e-44fb-aa47-87ef1b7decc8 --->

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

#### 💡 Explanation:

* Source: https://docs.python.org/3/reference/compound_stmts.html#except

  When an exception has been assigned using `as` target, it is cleared at the end of the `except` clause. This is as if

  ```py
  except E as N:
      foo
  ```

  was translated into

  ```py
  except E as N:
      try:
          foo
      finally:
          del N
  ```

  This means the exception must be assigned to a different name to be able to refer to it after the except clause. Exceptions are cleared because, with the traceback attached to them, they form a reference cycle with the stack frame, keeping all locals in that frame alive until the next garbage collection occurs.

* The clauses are not scoped in Python. Everything in the example is present in the same scope, and the variable `e` got removed due to the execution of the `except` clause. The same is not the case with functions that have their separate inner-scopes. The example below illustrates this:

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

* In Python 2.x, the variable name `e` gets assigned to `Exception()` instance, so when you try to print, it prints nothing.

    **Output (Python 2.x):**
    ```py
    >>> e
    Exception()
    >>> print e
    # Nothing is printed!
    ```

---


### ▶ The mysterious key type conversion
<!-- Example ID: 00f42dd0-b9ef-408d-9e39-1bc209ce3f36 --->
```py
class SomeClass(str):
    pass

some_dict = {'s': 42}
```

**Output:**
```py
>>> type(list(some_dict.keys())[0])
str
>>> s = SomeClass('s')
>>> some_dict[s] = 40
>>> some_dict # expected: Two different keys-value pairs
{'s': 40}
>>> type(list(some_dict.keys())[0])
str
```

#### 💡 Explanation:

* Both the object `s` and the string `"s"` hash to the same value because `SomeClass` inherits the `__hash__` method of `str` class.
* `SomeClass("s") == "s"` evaluates to `True` because `SomeClass` also inherits `__eq__` method from `str` class.
* Since both the objects hash to the same value and are equal, they are represented by the same key in the dictionary.
* For the desired behavior, we can redefine the `__eq__` method in `SomeClass`
  ```py
  class SomeClass(str):
    def __eq__(self, other):
        return (
            type(self) is SomeClass
            and type(other) is SomeClass
            and super().__eq__(other)
        )

    # When we define a custom __eq__, Python stops automatically inheriting the
    # __hash__ method, so we need to define it as well
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

### ▶ Let's see if you can guess this?
<!-- Example ID: 81aa9fbe-bd63-4283-b56d-6fdd14c9105e --->
```py
a, b = a[b] = {}, 5
```

**Output:**
```py
>>> a
{5: ({...}, 5)}
```

#### 💡 Explanation:

* According to [Python language reference](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements), assignment statements have the form
  ```
  (target_list "=")+ (expression_list | yield_expression)
  ```
  and
  
> An assignment statement evaluates the expression list (remember that this can be a single expression or a comma-separated list, the latter yielding a tuple) and assigns the single resulting object to each of the target lists, from left to right.

* The `+` in `(target_list "=")+` means there can be **one or more** target lists. In this case, target lists are `a, b` and `a[b]` (note the expression list is exactly one, which in our case is `{}, 5`).

* After the expression list is evaluated, its value is unpacked to the target lists from **left to right**. So, in our case, first the `{}, 5` tuple is unpacked to `a, b` and we now have `a = {}` and `b = 5`.

* `a` is now assigned to `{}`, which is a mutable object.

* The second target list is `a[b]` (you may expect this to throw an error because both `a` and `b` have not been defined in the statements before. But remember, we just assigned `a` to `{}` and `b` to `5`).

* Now, we are setting the key `5` in the dictionary to the tuple `({}, 5)` creating a circular reference (the `{...}` in the output refers to the same object that `a` is already referencing). Another simpler example of circular reference could be
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
  Similar is the case in our example (`a[b][0]` is the same object as `a`)

* So to sum it up, you can break the example down to
  ```py
  a, b = {}, 5
  a[b] = a, b
  ```
  And the circular reference can be justified by the fact that `a[b][0]` is the same object as `a`
  ```py
  >>> a[b][0] is a
  True
  ```

---
---

## Section: Slippery Slopes

### ▶ Modifying a dictionary while iterating over it
<!-- Example ID: b4e5cdfb-c3a8-4112-bd38-e2356d801c41 --->
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

Yes, it runs for exactly **eight** times and stops.

#### 💡 Explanation:

* Iteration over a dictionary that you edit at the same time is not supported.
* It runs eight times because that's the point at which the dictionary resizes to hold more keys (we have eight deletion entries, so a resize is needed). This is actually an implementation detail.
* How deleted keys are handled and when the resize occurs might be different for different Python implementations.
* So for Python versions other than Python 2.7 - Python 3.5, the count might be different from 8 (but whatever the count is, it's going to be the same every time you run it). You can find some discussion around this [here](https://github.com/satwikkansal/wtfpython/issues/53) or in [this](https://stackoverflow.com/questions/44763802/bug-in-python-dict) StackOverflow thread.
* Python 3.7.6 onwards, you'll see `RuntimeError: dictionary keys changed during iteration` exception if you try to do this.

---

### ▶ Stubborn `del` operation
<!-- Example ID: 777ed4fd-3a2d-466f-95e7-c4058e61d78e --->
<!-- read-only -->

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
>>> del x # this should print "Deleted!"
>>> del y
Deleted!
```

Phew, deleted at last. You might have guessed what saved `__del__` from being called in our first attempt to delete `x`. Let's add more twists to the example.

2\.
```py
>>> x = SomeClass()
>>> y = x
>>> del x
>>> y # check if y exists
<__main__.SomeClass instance at 0x7f98a1a67fc8>
>>> del y # Like previously, this should print "Deleted!"
>>> globals() # oh, it didn't. Let's check all our global variables and confirm
Deleted!
{'__builtins__': <module '__builtin__' (built-in)>, 'SomeClass': <class __main__.SomeClass at 0x7f98a1a5f668>, '__package__': None, '__name__': '__main__', '__doc__': None}
```

Okay, now it's deleted :confused:

#### 💡 Explanation:
+ `del x` doesn’t directly call `x.__del__()`.
+ When `del x` is encountered, Python deletes the name `x` from current scope and decrements by 1 the reference count of the object `x` referenced. `__del__()` is called only when the object's reference count reaches zero.
+ In the second output snippet, `__del__()` was not called because the previous statement (`>>> y`) in the interactive interpreter created another reference to the same object (specifically, the `_` magic variable which references the result value of the last non `None` expression on the REPL), thus preventing the reference count from reaching zero when `del y` was encountered.
+ Calling `globals` (or really, executing anything that will have a non `None` result) caused `_` to reference the new result, dropping the existing reference. Now the reference count reached 0 and we can see "Deleted!" being printed (finally!).

---

### ▶ The out of scope variable
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

#### 💡 Explanation:
* When you make an assignment to a variable in scope, it becomes local to that scope. So `a` becomes local to the scope of `another_func`, but it has not been initialized previously in the same scope, which throws an error.
* To modify the outer scope variable `a` in `another_func`, we have to use the `global` keyword.
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
* In `another_closure_func`, `a` becomes local to the scope of `another_inner_func`, but it has not been initialized previously in the same scope, which is why it throws an error. 
* To modify the outer scope variable `a` in `another_inner_func`, use the `nonlocal` keyword. The nonlocal statement is used to refer to variables defined in the nearest outer (excluding the global) scope.
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
* The keywords `global` and `nonlocal` tell the python interpreter to not declare new variables and look them up in the corresponding outer scopes.
* Read [this](https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html) short but an awesome guide to learn more about how namespaces and scope resolution works in Python.

---

### ▶ Deleting a list item while iterating
<!-- Example ID: 4cc52d4e-d42b-4e09-b25f-fbf5699b7d4e --->
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

Can you guess why the output is `[2, 4]`?

#### 💡 Explanation:

* It's never a good idea to change the object you're iterating over. The correct way to do so is to iterate over a copy of the object instead, and `list_3[:]` does just that.

     ```py
     >>> some_list = [1, 2, 3, 4]
     >>> id(some_list)
     139798789457608
     >>> id(some_list[:]) # Notice that python creates new object for sliced list.
     139798779601192
     ```

**Difference between `del`, `remove`, and `pop`:**
* `del var_name` just removes the binding of the `var_name` from the local or global namespace (That's why the `list_1` is unaffected).
* `remove` removes the first matching value, not a specific index, raises `ValueError` if the value is not found.
* `pop` removes the element at a specific index and returns it, raises `IndexError` if an invalid index is specified.

**Why the output is `[2, 4]`?**
- The list iteration is done index by index, and when we remove `1` from `list_2` or `list_4`, the contents of the lists are now `[2, 3, 4]`. The remaining elements are shifted down, i.e., `2` is at index 0, and `3` is at index 1. Since the next iteration is going to look at index 1 (which is the `3`), the `2` gets skipped entirely. A similar thing will happen with every alternate element in the list sequence.

* Refer to this StackOverflow [thread](https://stackoverflow.com/questions/45946228/what-happens-when-you-try-to-delete-a-list-element-while-iterating-over-it) explaining the example
* See also this nice StackOverflow [thread](https://stackoverflow.com/questions/45877614/how-to-change-all-the-dictionary-keys-in-a-for-loop-with-d-items) for a similar example related to dictionaries in Python.

---


### ▶ Lossy zip of iterators *
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
Where did element `3` go from the `numbers` list?

#### 💡 Explanation:

- From Python [docs](https://docs.python.org/3.3/library/functions.html#zip), here's an approximate implementation of zip function,
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
- So the function takes in arbitrary number of iterable objects, adds each of their items to the `result` list by calling the `next` function on them, and stops whenever any of the iterable is exhausted. 
- The caveat here is when any iterable is exhausted, the existing elements in the `result` list are discarded. That's what happened with `3` in the `numbers_iter`.
- The correct way to do the above using `zip` would be,
    ```py
    >>> numbers = list(range(7))
    >>> numbers_iter = iter(numbers)
    >>> list(zip(first_three, numbers_iter))
    [(0, 0), (1, 1), (2, 2)]
    >>> list(zip(remaining, numbers_iter))
    [(3, 3), (4, 4), (5, 5), (6, 6)]
    ```
    The first argument of zip should be the one with fewest elements.

---

### ▶ Loop variables leaking out!
<!-- Example ID: ccec7bf6-7679-4963-907a-1cd8587be9ea --->
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

But `x` was never defined outside the scope of for loop...

2\.
```py
# This time let's initialize x first
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

**Output (Python 2.x):**
```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
4
```

**Output (Python 3.x):**
```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
1
```

#### 💡 Explanation:

- In Python, for-loops use the scope they exist in and leave their defined loop-variable behind. This also applies if we explicitly defined the for-loop variable in the global namespace before. In this case, it will rebind the existing variable.

- The differences in the output of Python 2.x and Python 3.x interpreters for list comprehension example can be explained by following change documented in [What’s New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html) changelog:

    > "List comprehensions no longer support the syntactic form `[... for var in item1, item2, ...]`. Use `[... for var in (item1, item2, ...)]` instead. Also, note that list comprehensions have different semantics: they are closer to syntactic sugar for a generator expression inside a `list()` constructor, and in particular, the loop control variables are no longer leaked into the surrounding scope."

---

### ▶ Beware of default mutable arguments!
<!-- Example ID: 7d42dade-e20d-4a7b-9ed7-16fb58505fe9 --->

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

#### 💡 Explanation:

- The default mutable arguments of functions in Python aren't really initialized every time you call the function. Instead, the recently assigned value to them is used as the default value. When we explicitly passed `[]` to `some_func` as the argument, the default value of the `default_arg` variable was not used, so the function returned as expected.

    ```py
    def some_func(default_arg=[]):
        default_arg.append("some_string")
        return default_arg
    ```

    **Output:**
    ```py
    >>> some_func.__defaults__ #This will show the default argument values for the function
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

- A common practice to avoid bugs due to mutable arguments is to assign `None` as the default value and later check if any value is passed to the function corresponding to that argument. Example:

    ```py
    def some_func(default_arg=None):
        if default_arg is None:
            default_arg = []
        default_arg.append("some_string")
        return default_arg
    ```

---

### ▶ Catching the Exceptions
<!-- Example ID: b5ca5e6a-47b9-4f69-9375-cda0f8c6755d --->
```py
some_list = [1, 2, 3]
try:
    # This should raise an ``IndexError``
    print(some_list[4])
except IndexError, ValueError:
    print("Caught!")

try:
    # This should raise a ``ValueError``
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

#### 💡 Explanation

* To add multiple Exceptions to the except clause, you need to pass them as parenthesized tuple as the first argument. The second argument is an optional name, which when supplied will bind the Exception instance that has been raised. Example,
  ```py
  some_list = [1, 2, 3]
  try:
     # This should raise a ``ValueError``
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

* Separating the exception from the variable with a comma is deprecated and does not work in Python 3; the correct way is to use `as`. Example,
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

### ▶ Same operands, different story!
<!-- Example ID: ca052cdf-dd2d-4105-b936-65c28adc18a0 --->
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

#### 💡 Explanation:

*  `a += b` doesn't always behave the same way as `a = a + b`.  Classes *may* implement the *`op=`* operators differently, and lists do this.

* The expression `a = a + [5,6,7,8]` generates a new list and sets `a`'s reference to that new list, leaving `b` unchanged.

* The expression `a += [5,6,7,8]` is actually mapped to an "extend" function that operates on the list such that `a` and `b` still point to the same list that has been modified in-place.

---

### ▶ Name resolution ignoring class scope
<!-- Example ID: 03f73d96-151c-4929-b0a8-f74430788324 --->
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

#### 💡 Explanation
- Scopes nested inside class definition ignore names bound at the class level.
- A generator expression has its own scope.
- Starting from Python 3.X, list comprehensions also have their own scope.

---

### ▶ Rounding like a banker *

Let's implement a naive function to get the middle element of a list:
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
It seems as though Python rounded 2.5 to 2.

#### 💡 Explanation:

- This is not a float precision error, in fact, this behavior is intentional. Since Python 3.0, `round()` uses [banker's rounding](https://en.wikipedia.org/wiki/Rounding#Round_half_to_even) where .5 fractions are rounded to the nearest **even** number:

```py
>>> round(0.5)
0
>>> round(1.5)
2
>>> round(2.5)
2
>>> import numpy  # numpy does the same
>>> numpy.round(0.5)
0.0
>>> numpy.round(1.5)
2.0
>>> numpy.round(2.5)
2.0
```

- This is the recommended way to round .5 fractions as described in [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754#Rounding_rules). However, the other way (round away from zero) is taught in school most of the time, so banker's rounding is likely not that well known. Furthermore, some of the most popular programming languages (for example: JavaScript, Java, C/C++, Ruby, Rust) do not use banker's rounding either. Therefore, this is still quite special to Python and may result in confusion when rounding fractions. 
- See the [round() docs](https://docs.python.org/3/library/functions.html#round) or [this stackoverflow thread](https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior) for more information.
- Note that `get_middle([1])` only returned 1 because the index was `round(0.5) - 1 = 0 - 1 = -1`, returning the last element in the list.

---

### ▶ Needles in a Haystack *

<!-- Example ID: 52a199b1-989a-4b28-8910-dff562cebba9 --->

I haven't met even a single experience Pythonist till date who has not come across one or more of the following scenarios,

1\.

```py
x, y = (0, 1) if True else None, None
```

**Output:**

```py
>>> x, y  # expected (0, 1)
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

4\. Not asserting strongly enough

```py
a = "python"
b = "javascript"
```

**Output:**

```py
# An assert statement with an assertion failure message.
>>> assert(a == b, "Both languages are different")
# No AssertionError is raised
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

#### 💡 Explanation:

* For 1, the correct statement for expected behavior is `x, y = (0, 1) if True else (None, None)`.

* For 2, the correct statement for expected behavior is `t = ('one',)` or `t = 'one',` (missing comma) otherwise the interpreter considers `t` to be a `str` and iterates over it character by character.

* `()` is a special token and denotes empty `tuple`.

* In 3, as you might have already figured out, there's a missing comma after 5th element (`"that"`) in the list. So by implicit string literal concatenation,

  ```py
  >>> ten_words_list
  ['some', 'very', 'big', 'list', 'thatconsists', 'of', 'exactly', 'ten', 'words']
  ```

* No `AssertionError` was raised in 4th snippet because instead of asserting the individual expression `a == b`, we're asserting entire tuple. The following snippet will clear things up,

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

* As for the fifth snippet, most methods that modify the items of sequence/mapping objects like `list.append`, `dict.update`, `list.sort`, etc. modify the objects in-place and return `None`. The rationale behind this is to improve performance by avoiding making a copy of the object if the operation can be done in-place (Referred from [here](https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list)).

* Last one should be fairly obvious, mutable object (like `list`) can be altered in the function, and the reassignation of an immutable (`a -= 1`) is not an alteration of the value.

* Being aware of these nitpicks can save you hours of debugging effort in the long run. 

---


### ▶ Splitsies *
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

#### 💡 Explanation:

- It might appear at first that the default separator for split is a single space `' '`, but as per the [docs](https://docs.python.org/3/library/stdtypes.html#str.split)
    >  If sep is not specified or is `None`, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns `[]`.
    > If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, `'1,,2'.split(',')` returns `['1', '', '2']`). Splitting an empty string with a specified separator returns `['']`.
- Noticing how the leading and trailing whitespaces are handled in the following snippet will make things clear,
    ```py
    >>> ' a '.split(' ')
    ['', 'a', '']
    >>> ' a '.split()
    ['a']
    >>> ''.split(' ')
    ['']
    ```

---

### ▶ Wild imports *
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

#### 💡 Explanation:

- It is often advisable to not use wildcard imports. The first obvious reason for this is, in wildcard imports, the names with a leading underscore don't get imported. This may lead to errors during runtime.
- Had we used `from ... import a, b, c` syntax, the above `NameError` wouldn't have occurred.
    ```py
    >>> from module import some_weird_name_func_, _another_weird_name_func
    >>> _another_weird_name_func()
    works!
    ```
- If you really want to use wildcard imports, then you'd have to define the list `__all__` in your module that will contain a list of public objects that'll be available when we do wildcard imports.
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

### ▶ All sorted? *

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

#### 💡 Explanation:

- The `sorted` method always returns a list, and comparing lists and tuples always returns `False` in Python. 

- ```py
  >>> [] == tuple()
  False
  >>> x = 7, 8, 9
  >>> type(x), type(sorted(x))
  (tuple, list)
  ```

- Unlike `sorted`, the `reversed` method returns an iterator. Why? Because sorting requires the iterator to be either modified in-place or use an extra container (a list), whereas reversing can simply work by iterating from the last index to the first.

- So during comparison `sorted(y) == sorted(y)`, the first call to `sorted()` will consume the iterator `y`, and the next call will just return an empty list.

  ```py
  >>> x = 7, 8, 9
  >>> y = reversed(x)
  >>> sorted(y), sorted(y)
  ([7, 8, 9], [])
  ```

---

### ▶ Midnight time doesn't exist?
<!-- Example ID: 1bce8294-5619-4d70-8ce3-fe0bade690d1 --->
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

**Output (< 3.5):**

```py
('Time at noon is', datetime.time(12, 0))
```
The midnight time is not printed.

#### 💡 Explanation:

Before Python 3.5, the boolean value for `datetime.time` object was considered to be `False` if it represented midnight in UTC. It is error-prone when using the `if obj:` syntax to check if the `obj` is null or some equivalent of "empty."

---
---



## Section: The Hidden treasures!

This section contains a few lesser-known and interesting things about Python that most beginners like me are unaware of (well, not anymore).

### ▶ Okay Python, Can you make me fly?
<!-- Example ID: a92f3645-1899-4d50-9721-0031be4aec3f --->
Well, here you go

```py
import antigravity
```

**Output:**
Sshh... It's a super-secret.

#### 💡 Explanation:
+ `antigravity` module is one of the few easter eggs released by Python developers.
+ `import antigravity` opens up a web browser pointing to the [classic XKCD comic](https://xkcd.com/353/) about Python.
+ Well, there's more to it. There's **another easter egg inside the easter egg**. If you look at the [code](https://github.com/python/cpython/blob/master/Lib/antigravity.py#L7-L17), there's a function defined that purports to implement the [XKCD's geohashing algorithm](https://xkcd.com/426/).

---

### ▶ `goto`, but why?
<!-- Example ID: 2aff961e-7fa5-4986-a18a-9e5894bd89fe --->

```py
from goto import goto, label
for i in range(9):
    for j in range(9):
        for k in range(9):
            print("I am trapped, please rescue!")
            if k == 2:
                goto .breakout # breaking out from a deeply nested loop
label .breakout
print("Freedom!")
```

**Output (Python 2.3):**
```py
I am trapped, please rescue!
I am trapped, please rescue!
Freedom!
```

#### 💡 Explanation:
- A working version of `goto` in Python was [announced](https://mail.python.org/pipermail/python-announce-list/2004-April/002982.html) as an April Fool's joke on 1st April 2004.
- Current versions of Python do not have this module.
- Although it works, but please don't use it. Here's the [reason](https://docs.python.org/3/faq/design.html#why-is-there-no-goto) to why `goto` is not present in Python.

---

### ▶ Brace yourself!
<!-- Example ID: 5c0c75f2-ddd9-4da3-ba49-c4be7ec39acf --->
If you are one of the people who doesn't like using whitespace in Python to denote scopes, you can use the C-style {} by importing,

```py
from __future__ import braces
```

**Output:**
```py
  File "some_file.py", line 1
    from __future__ import braces
SyntaxError: not a chance
```

Braces? No way! If you think that's disappointing, use Java. Okay, another surprising thing, can you find where's the `SyntaxError` raised in `__future__` module [code](https://github.com/python/cpython/blob/master/Lib/__future__.py)?

#### 💡 Explanation:
+ The `__future__` module is normally used to provide features from future versions of Python. The "future" in this specific context is however, ironic.
+ This is an easter egg concerned with the community's feelings on this issue.
+ The code is actually present [here](https://github.com/python/cpython/blob/025eb98dc0c1dc27404df6c544fc2944e0fa9f3a/Python/future.c#L49) in `future.c` file.
+ When the CPython compiler encounters a [future statement](https://docs.python.org/3.3/reference/simple_stmts.html#future-statements), it first runs the appropriate code in `future.c` before treating it as a normal import statement.

---

### ▶ Let's meet Friendly Language Uncle For Life
<!-- Example ID: 6427fae6-e959-462d-85da-ce4c94ce41be --->
**Output (Python 3.x)**
```py
>>> from __future__ import barry_as_FLUFL
>>> "Ruby" != "Python" # there's no doubt about it
  File "some_file.py", line 1
    "Ruby" != "Python"
              ^
SyntaxError: invalid syntax

>>> "Ruby" <> "Python"
True
```

There we go.

#### 💡 Explanation:
- This is relevant to [PEP-401](https://www.python.org/dev/peps/pep-0401/) released on April 1, 2009 (now you know, what it means).
- Quoting from the PEP-401
  
  > Recognized that the != inequality operator in Python 3.0 was a horrible, finger-pain inducing mistake, the FLUFL reinstates the <> diamond operator as the sole spelling.
- There were more things that Uncle Barry had to share in the PEP; you can read them [here](https://www.python.org/dev/peps/pep-0401/).
- It works well in an interactive environment, but it will raise a `SyntaxError` when you run via python file (see this [issue](https://github.com/satwikkansal/wtfpython/issues/94)). However, you can wrap the statement inside an `eval` or `compile` to get it working,
    ```py
    from __future__ import barry_as_FLUFL
    print(eval('"Ruby" <> "Python"'))
    ```

---

### ▶ Even Python understands that love is complicated
<!-- Example ID: b93cad9e-d341-45d1-999c-fcdce65bed25 --->
```py
import this
```

Wait, what's **this**? `this` is love :heart:

**Output:**
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

It's the Zen of Python!

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
>>> love is not True or False; love is love  # Love is complicated
True
```

#### 💡 Explanation:

* `this` module in Python is an easter egg for The Zen Of Python ([PEP 20](https://www.python.org/dev/peps/pep-0020)).
* And if you think that's already interesting enough, check out the implementation of [this.py](https://hg.python.org/cpython/file/c3896275c0f6/Lib/this.py). Interestingly, **the code for the Zen violates itself** (and that's probably the only place where this happens).
* Regarding the statement `love is not True or False; love is love`, ironic but it's self-explanatory (if not, please see the examples related to `is` and `is not` operators).

---

### ▶ Yes, it exists!
<!-- Example ID: 4286db3d-1ea7-47c9-8fb6-a9a04cac6e49 --->
**The `else` clause for loops.** One typical example might be:

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

**The `else` clause in exception handling.** An example,

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

#### 💡 Explanation:
- The `else` clause after a loop is executed only when there's no explicit `break` after all the iterations. You can think of it as a "nobreak" clause.
- `else` clause after a try block is also called "completion clause" as reaching the `else` clause in a `try` statement means that the try block actually completed successfully.

---
### ▶ Ellipsis *
<!-- Example ID: 969b7100-ab3d-4a7d-ad7d-a6be16181b2b --->
```py
def some_func():
    Ellipsis
```

**Output**
```py
>>> some_func()
# No output, No Error

>>> SomeRandomString
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'SomeRandomString' is not defined

>>> Ellipsis
Ellipsis
```

#### 💡 Explanation
- In Python, `Ellipsis` is a globally available built-in object which is equivalent to `...`.
    ```py
    >>> ...
    Ellipsis
    ```
- Ellipsis can be used for several purposes,
    + As a placeholder for code that hasn't been written yet (just like `pass` statement)
    + In slicing syntax to represent the full slices in remaining direction
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
    So our `three_dimensional_array` is an array of array of arrays. Let's say we want to print the second element (index `1`) of all the innermost arrays, we can use Ellipsis to bypass all the preceding dimensions
    ```py
    >>> three_dimensional_array[:,:,1]
    array([[1, 3],
       [5, 7]])
    >>> three_dimensional_array[..., 1] # using Ellipsis.
    array([[1, 3],
       [5, 7]])
    ```
    Note: this will work for any number of dimensions. You can even select slice in first and last dimension and ignore the middle ones this way (`n_dimensional_array[firs_dim_slice, ..., last_dim_slice]`)
    + In [type hinting](https://docs.python.org/3/library/typing.html) to indicate only a part of the type (like `(Callable[..., int]` or `Tuple[str, ...]`))
    + You may also use Ellipsis as a default function argument (in the cases when you want to differentiate between the "no argument passed" and "None value passed" scenarios).

---

### ▶ Inpinity
<!-- Example ID: ff473ea8-a3b1-4876-a6f0-4378aff790c1 --->
The spelling is intended. Please, don't submit a patch for this.

**Output (Python 3.x):**
```py
>>> infinity = float('infinity')
>>> hash(infinity)
314159
>>> hash(float('-inf'))
-314159
```

#### 💡 Explanation:
- Hash of infinity is 10⁵ x π.
- Interestingly, the hash of `float('-inf')` is "-10⁵ x π" in Python 3, whereas "-10⁵ x e" in Python 2.

---

### ▶ Let's mangle
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
        # Let's try something symmetrical this time
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

Why did `Yo()._Yo__honey` work?

3\.

```py
_A__variable = "Some value"

class A(object):
    def some_func(self):
        return __variable # not initialized anywhere yet
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


#### 💡 Explanation:

* [Name Mangling](https://en.wikipedia.org/wiki/Name_mangling) is used to avoid naming collisions between different namespaces.
* In Python, the interpreter modifies (mangles) the class member names starting with `__` (double underscore a.k.a "dunder") and not ending with more than one trailing underscore by adding `_NameOfTheClass` in front.
* So, to access `__honey` attribute in the first snippet, we had to append `_Yo` to the front, which would prevent conflicts with the same name attribute defined in any other class.
* But then why didn't it work in the second snippet? Because name mangling excludes the names ending with double underscores.
* The third snippet was also a consequence of name mangling. The name `__variable` in the statement `return __variable` was mangled to `_A__variable`, which also happens to be the name of the variable we declared in the outer scope.
* Also, if the mangled name is longer than 255 characters, truncation will happen.

---
---

## Section: Appearances are deceptive!

### ▶ Skipping lines?
<!-- Example ID: d50bbde1-fb9d-4735-9633-3444b9d2f417 --->
**Output:**
```py
>>> value = 11
>>> valuе = 32
>>> value
11
```

Wut?

**Note:** The easiest way to reproduce this is to simply copy the statements from the above snippet and paste them into your file/shell.

#### 💡 Explanation

Some non-Western characters look identical to letters in the English alphabet but are considered distinct by the interpreter.

```py
>>> ord('е') # cyrillic 'e' (Ye)
1077
>>> ord('e') # latin 'e', as used in English and typed using standard keyboard
101
>>> 'е' == 'e'
False

>>> value = 42 # latin e
>>> valuе = 23 # cyrillic 'e', Python 2.x interpreter would raise a `SyntaxError` here
>>> value
42
```

The built-in `ord()` function returns a character's Unicode [code point](https://en.wikipedia.org/wiki/Code_point), and different code positions of Cyrillic 'e' and Latin 'e' justify the behavior of the above example.

---

### ▶ Teleportation

<!-- Example ID: edafe923-0c20-4315-b6e1-0c31abfc38f5 --->

```py
# `pip install numpy` first.
import numpy as np

def energy_send(x):
    # Initializing a numpy array
    np.array([float(x)])

def energy_receive():
    # Return an empty numpy array
    return np.empty((), dtype=np.float).tolist()
```

**Output:**
```py
>>> energy_send(123.456)
>>> energy_receive()
123.456
```

Where's the Nobel Prize?

#### 💡 Explanation:

* Notice that the numpy array created in the `energy_send` function is not returned, so that memory space is free to reallocate.
* `numpy.empty()` returns the next free memory slot without reinitializing it. This memory spot just happens to be the same one that was just freed (usually, but not always).

---

### ▶ Well, something is fishy...
<!-- Example ID: cb6a37c5-74f7-44ca-b58c-3b902419b362 --->
```py
def square(x):
    """
    A simple function to calculate the square of a number by addition.
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

Shouldn't that be 100?

**Note:** If you're not able to reproduce this, try running the file [mixed_tabs_and_spaces.py](/mixed_tabs_and_spaces.py) via the shell.

#### 💡 Explanation

* **Don't mix tabs and spaces!** The character just preceding return is a "tab",  and the code is indented by multiple of "4 spaces" elsewhere in the example.
* This is how Python handles tabs:
  
  > First, tabs are replaced (from left to right) by one to eight spaces such that the total number of characters up to and including the replacement is a multiple of eight <...>
* So the "tab" at the last line of `square` function is replaced with eight spaces, and it gets into the loop.
* Python 3 is kind enough to throw an error for such cases automatically.

    **Output (Python 3.x):**
    ```py
    TabError: inconsistent use of tabs and spaces in indentation
    ```

---
---

## Section: Miscellaneous


### ▶ `+=` is faster
<!-- Example ID: bfd19c60-a807-4a26-9598-4912b86ddb36 --->

```py
# using "+", three strings:
>>> timeit.timeit("s1 = s1 + s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.25748300552368164
# using "+=", three strings:
>>> timeit.timeit("s1 += s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.012188911437988281
```

#### 💡 Explanation:
+ `+=` is faster than `+` for concatenating more than two strings because the first string (example, `s1` for `s1 += s2 + s3`) is not destroyed while calculating the complete string.

---

### ▶ Let's make a giant string!
<!-- Example ID: c7a07424-63fe-4504-9842-8f3d334f28fc --->
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
# Executed in ipython shell using %timeit for better readability of results.
# You can also use the timeit module in normal python shell/scriptm=, example usage below
# timeit.timeit('add_string_with_plus(10000)', number=1000, globals=globals())

>>> NUM_ITERS = 1000
>>> %timeit -n1000 add_string_with_plus(NUM_ITERS)
124 µs ± 4.73 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
>>> %timeit -n1000 add_bytes_with_plus(NUM_ITERS)
211 µs ± 10.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_string_with_format(NUM_ITERS)
61 µs ± 2.18 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_string_with_join(NUM_ITERS)
117 µs ± 3.21 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> l = ["xyz"]*NUM_ITERS
>>> %timeit -n1000 convert_list_to_string(l, NUM_ITERS)
10.1 µs ± 1.06 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

Let's increase the number of iterations by a factor of 10.

```py
>>> NUM_ITERS = 10000
>>> %timeit -n1000 add_string_with_plus(NUM_ITERS) # Linear increase in execution time
1.26 ms ± 76.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_bytes_with_plus(NUM_ITERS) # Quadratic increase
6.82 ms ± 134 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_string_with_format(NUM_ITERS) # Linear increase
645 µs ± 24.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_string_with_join(NUM_ITERS) # Linear increase
1.17 ms ± 7.25 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> l = ["xyz"]*NUM_ITERS
>>> %timeit -n1000 convert_list_to_string(l, NUM_ITERS) # Linear increase
86.3 µs ± 2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

#### 💡 Explanation
- You can read more about [timeit](https://docs.python.org/3/library/timeit.html) or [%timeit](https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-timeit) on these links. They are used to measure the execution time of code pieces.
- Don't use `+` for generating long strings — In Python, `str` is immutable, so the left and right strings have to be copied into the new string for every pair of concatenations. If you concatenate four strings of length 10, you'll be copying (10+10) + ((10+10)+10) + (((10+10)+10)+10) = 90 characters instead of just 40 characters. Things get quadratically worse as the number and size of the string increases (justified with the execution times of `add_bytes_with_plus` function)
- Therefore, it's advised to use `.format.` or `%` syntax (however, they are slightly slower than `+` for very short strings).
- Or better, if already you've contents available in the form of an iterable object, then use `''.join(iterable_object)` which is much faster.
- Unlike `add_bytes_with_plus` because of the `+=` optimizations discussed in the previous example, `add_string_with_plus` didn't show a quadratic increase in execution time. Had the statement been `s = s + "x" + "y" + "z"` instead of `s += "xyz"`, the increase would have been quadratic.
  ```py
  def add_string_with_plus(iters):
      s = ""
      for i in range(iters):
          s = s + "x" + "y" + "z"
      assert len(s) == 3*iters

  >>> %timeit -n100 add_string_with_plus(1000)
  388 µs ± 22.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
  >>> %timeit -n100 add_string_with_plus(10000) # Quadratic increase in execution time
  9 ms ± 298 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
  ```
- So many ways to format and create a giant string are somewhat in contrast to the [Zen of Python](https://www.python.org/dev/peps/pep-0020/), according to which,
  
    > There should be one-- and preferably only one --obvious way to do it.

---

### ▶ Slowing down `dict` lookups *
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
Why are same lookups becoming slower?

#### 💡 Explanation:
+ CPython has a generic dictionary lookup function that handles all types of keys (`str`, `int`, any object ...), and a specialized one for the common case of dictionaries composed of `str`-only keys.
+ The specialized function (named `lookdict_unicode` in CPython's [source](https://github.com/python/cpython/blob/522691c46e2ae51faaad5bbbce7d959dd61770df/Objects/dictobject.c#L841)) knows all existing keys (including the looked-up key) are strings, and uses the faster & simpler string comparison to compare keys, instead of calling the `__eq__` method.
+ The first time a `dict` instance is accessed with a non-`str` key, it's modified so future lookups use the generic function.
+ This process is not reversible for the particular `dict` instance, and the key doesn't even have to exist in the dictionary. That's why attempting a failed lookup has the same effect.


### ▶ Bloating instance `dict`s *
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

**Output:** (Python 3.8, other Python 3 versions may vary a little)
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

Let's try again... In a new interpreter:

```py
>>> o1 = SomeClass()
>>> o2 = SomeClass()
>>> dict_size(o1)
104  # as expected
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

What makes those dictionaries become bloated? And why are newly created objects bloated as well?

#### 💡 Explanation:
+ CPython is able to reuse the same "keys" object in multiple dictionaries. This was added in [PEP 412](https://www.python.org/dev/peps/pep-0412/) with the motivation to reduce memory usage, specifically in dictionaries of instances - where keys (instance attributes) tend to be common to all instances.
+ This optimization is entirely seamless for instance dictionaries, but it is disabled if certain assumptions are broken.
+ Key-sharing dictionaries do not support deletion; if an instance attribute is deleted, the dictionary is "unshared", and key-sharing is disabled for all future instances of the same class.
+ Additionaly, if the dictionary keys have been resized (because new keys are inserted), they are kept shared *only* if they are used by a exactly single dictionary (this allows adding many attributes in the `__init__` of the very first created instance, without causing an "unshare"). If multiple instances exist when a resize happens, key-sharing is disabled for all future instances of the same class: CPython can't tell if your instances are using the same set of attributes anymore, and decides to bail out on attempting to share their keys.
+ A small tip, if you aim to lower your program's memory footprint: don't delete instance attributes, and make sure to initialize all attributes in your `__init__`!


### ▶ Minor Ones *
<!-- Example ID: f885cb82-f1e4-4daa-9ff3-972b14cb1324 --->
* `join()` is a string operation instead of list operation. (sort of counter-intuitive at first usage)

  **💡 Explanation:** If `join()` is a method on a string, then it can operate on any iterable (list, tuple, iterators). If it were a method on a list, it'd have to be implemented separately by every type. Also, it doesn't make much sense to put a string-specific method on a generic `list` object API.
  
* Few weird looking but semantically correct statements:
  + `[] = ()` is a semantically correct statement (unpacking an empty `tuple` into an empty `list`)
  + `'a'[0][0][0][0][0]` is also a semantically correct statement as strings are [sequences](https://docs.python.org/3/glossary.html#term-sequence)(iterables supporting element access using integer indices) in Python.
  + `3 --0-- 5 == 8` and `--5 == 5` are both semantically correct statements and evaluate to `True`.

* Given that `a` is a number, `++a` and `--a` are both valid Python statements but don't behave the same way as compared with similar statements in languages like C, C++, or Java.
  ```py
  >>> a = 5
  >>> a
  5
  >>> ++a
  5
  >>> --a
  5
  ```

  **💡 Explanation:**
  + There is no `++` operator in Python grammar. It is actually two `+` operators.
  + `++a` parses as `+(+a)` which translates to `a`. Similarly, the output of the statement `--a` can be justified.
  + This StackOverflow [thread](https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python) discusses the rationale behind the absence of increment and decrement operators in Python.

* You must be aware of the Walrus operator in Python. But have you ever heard about *the space-invader operator*?
  ```py
  >>> a = 42
  >>> a -=- 1
  >>> a
  43
  ```
  It is used as an alternative incrementation operator, together with another one
  ```py
  >>> a +=+ 1
  >>> a
  >>> 44
  ```
  **💡 Explanation:** This prank comes from [Raymond Hettinger's tweet](https://twitter.com/raymondh/status/1131103570856632321?lang=en). The space invader operator is actually just a malformatted `a -= (-1)`. Which is equivalent to `a = a - (- 1)`. Similar for the `a += (+ 1)` case.
  
* Python has an undocumented [converse implication](https://en.wikipedia.org/wiki/Converse_implication) operator. 
     
     ```py
     >>> False ** False == True
     True
     >>> False ** True == False
     True
     >>> True ** False == True
     True
     >>> True ** True == True
     True
     ```

     **💡 Explanation:** If you replace `False` and `True` by 0 and 1 and do the maths, the truth table is equivalent to a converse implication operator. ([Source](https://github.com/cosmologicon/pywat/blob/master/explanation.md#the-undocumented-converse-implication-operator))
     
* Since we are talking operators, there's also `@` operator for matrix multiplication (don't worry, this time it's for real).

     ```py
     >>> import numpy as np
     >>> np.array([2, 2, 2]) @ np.array([7, 8, 8])
     46
     ```

     **💡 Explanation:** The `@` operator was added in Python 3.5 keeping the scientific community in mind. Any object can overload `__matmul__` magic method to define behavior for this operator.

* From Python 3.8 onwards you can use a typical f-string syntax like `f'{some_var=}` for quick debugging. Example,
    ```py
    >>> some_string = "wtfpython"
    >>> f'{some_string=}'
    "some_string='wtfpython'"
    ``` 

* Python uses 2 bytes for local variable storage in functions. In theory, this means that only 65536 variables can be defined in a function. However, python has a handy solution built in that can be used to store more than 2^16 variable names. The following code demonstrates what happens in the stack when more than 65536 local variables are defined (Warning: This code prints around 2^18 lines of text, so be prepared!):
     
     ```py
     import dis
    exec("""
    def f():
        """ + """
        """.join(["X" + str(x) + "=" + str(x) for x in range(65539)]))

    f()

    print(dis.dis(f))
    ```
     
* Multiple Python threads won't run your *Python code* concurrently (yes, you heard it right!). It may seem intuitive to spawn several threads and let them execute your Python code concurrently, but, because of the [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) in Python, all you're doing is making your threads execute on the same core turn by turn. Python threads are good for IO-bound tasks, but to achieve actual parallelization in Python for CPU-bound tasks, you might want to use the Python [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) module.

* Sometimes, the `print` method might not print values immediately. For example,

     ```py
     # File some_file.py
     import time
     
     print("wtfpython", end="_")
     time.sleep(3)
     ```

     This will print the `wtfpython` after 3 seconds due to the `end` argument because the output buffer is flushed either after encountering `\n` or when the program finishes execution. We can force the buffer to flush by passing `flush=True` argument.

* List slicing with out of the bounds indices throws no errors
  ```py
  >>> some_list = [1, 2, 3, 4, 5]
  >>> some_list[111:]
  []
  ```

* Slicing an iterable not always creates a new object. For example,
    ```py
    >>> some_str = "wtfpython"
    >>> some_list = ['w', 't', 'f', 'p', 'y', 't', 'h', 'o', 'n']
    >>> some_list is some_list[:] # False expected because a new object is created.
    False
    >>> some_str is some_str[:] # True because strings are immutable, so making a new object is of not much use.
    True
    ```

* `int('١٢٣٤٥٦٧٨٩')` returns `123456789` in Python 3. In Python, Decimal characters include digit characters, and all characters that can be used to form decimal-radix numbers, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. Here's an [interesting story](https://chris.improbable.org/2014/8/25/adventures-in-unicode-digits/) related to this behavior of Python.

* You can separate numeric literals with underscores (for better readability) from Python 3 onwards.

     ```py
     >>> six_million = 6_000_000
     >>> six_million
     6000000
     >>> hex_address = 0xF00D_CAFE
     >>> hex_address
     4027435774
     ```

* `'abc'.count('') == 4`. Here's an approximate implementation of `count` method, which would make the things more clear
  ```py
  def count(s, sub):
      result = 0
      for i in range(len(s) + 1 - len(sub)):
          result += (s[i:i + len(sub)] == sub)
      return result
  ```
  The behavior is due to the matching of empty substring(`''`) with slices of length 0 in the original string.

---
---

# Contributing

A few ways in which you can contribute to wtfpython,

- Suggesting new examples
- Helping with translation (See [issues labeled translation](https://github.com/satwikkansal/wtfpython/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation))
- Minor corrections like pointing out outdated snippets, typos, formatting errors, etc.
- Identifying gaps (things like inadequate explanation, redundant examples, etc.)
- Any creative suggestions to make this project more fun and useful

Please see [CONTRIBUTING.md](/CONTRIBUTING.md) for more details. Feel free to create a new [issue](https://github.com/satwikkansal/wtfpython/issues/new) to discuss things.

PS: Please don't reach out with backlinking requests, no links will be added unless they're highly relevant to the project.

# Acknowledgements

The idea and design for this collection were initially inspired by Denys Dovhan's awesome project [wtfjs](https://github.com/denysdovhan/wtfjs). The overwhelming support by Pythonistas gave it the shape it is in right now.

#### Some nice Links!
* https://www.youtube.com/watch?v=sH4XF6pKKmk
* https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python
* https://sopython.com/wiki/Common_Gotchas_In_Python
* https://stackoverflow.com/questions/530530/python-2-x-gotchas-and-landmines
* https://stackoverflow.com/questions/1011431/common-pitfalls-in-python
* https://www.python.org/doc/humor/
* https://github.com/cosmologicon/pywat#the-undocumented-converse-implication-operator
* https://www.codementor.io/satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65
* https://github.com/wemake-services/wemake-python-styleguide/search?q=wtfpython&type=Issues
* WFTPython discussion threads on [Hacker News](https://news.ycombinator.com/item?id=21862073) and [Reddit](https://www.reddit.com/r/programming/comments/edsh3q/what_the_fck_python_30_exploring_and/).

# 🎓 License

[![WTFPL 2.0][license-image]][license-url]

&copy; [Satwik Kansal](https://satwikkansal.xyz)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square

## Surprise your friends as well!

If you like wtfpython, you can use these quick links to share it with your friends,

[Twitter](https://twitter.com/intent/tweet?url=https://github.com/satwikkansal/wtfpython&text=If%20you%20really%20think%20you%20know%20Python,%20think%20once%20more!%20Check%20out%20wtfpython&hashtags=python,wtfpython) | [Linkedin](https://www.linkedin.com/shareArticle?url=https://github.com/satwikkansal&title=What%20the%20f*ck%20Python!&summary=If%20you%20really%20thing%20you%20know%20Python,%20think%20once%20more!) | [Facebook](https://www.facebook.com/dialog/share?app_id=536779657179021&display=page&href=https%3A%2F%2Fgithub.com%2Fsatwikkansal%2Fwtfpython&quote=If%20you%20really%20think%20you%20know%20Python%2C%20think%20once%20more!)  

## Need a pdf version?

I've received a few requests for the pdf (and epub) version of wtfpython. You can add your details [here](https://satwikkansal.xyz/wtfpython-pdf/) to get them as soon as they are finished.


**That's all folks!** For upcoming content like this, you can add your email [here](https://www.satwikkansal.xyz/content-like-wtfpython/).
