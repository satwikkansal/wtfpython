# What the f*ck Python!

[![WTFPL 2.0][license-image]][license-url]

> A collection of tricky Python examples

Python being an awesomoe higher level language, provides us many functionalities for our comfort. But sometimes, the outcomes may not seem obvious to a normal Python user at the first sight. Here's an attempt to collect such examples and see what exactly is happening under the hood! I find it a nice way to learn internals of a language and I think you'll like them as well!

# Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Checklist](#checklist)
- [👀 Examples](#-examples)
  - [Example heading](#example-heading)
    - [💡 Explanation:](#-explanation)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [🎓 License](#-license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Checklist

[ ] https://www.youtube.com/watch?v=sH4XF6pKKmk
[ ] https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python/

# 👀 Examples

## Example heading

One line of what's happening:

```py
setting up
```

```py
>>> triggering_statement
weird output
```

### Explanation:

* Better to give outside links
* or just explain again in brief

## `datetime.time` object is considered to be false if it represented midnight in UTC

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

### Explanation

Before Python 3.5, a datetime.time object was considered to be false if it represented midnight in UTC. It is error-prone when using the `if obj:` syntax to check if the `obj` is null or some equivalent of "empty".


## `is` is not what it is!


```py
>>> a = 256
>>> b = 256
>>> a is b
True

>>> a = 257
>>> b = 257
>>> a is b
False

>>> a = 257; b = 257
>>> a is b
True
```


### 💡 Explanation:

**The difference between `is` and `==`**

* `is` operator checks if both the operands refer to the same object (i.e. it checks if the identity of the operands matches or not).
* `==` operator compares the values of both the operands and checks if they are the same.
* So if the `is` operator returns `True` then the equality is definitely `True`, but the opposite may or may not be True.


**`256` is an existing object but `257` isn't**

When you start up python the numbers from `-5` to `256` will be allocated. These numbers are used a lot, so it makes sense to just have them ready.

Quoting from https://docs.python.org/3/c-api/long.html
> The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object. So it should be possible to change the value of 1. I suspect the behaviour of Python in this case is undefined. :-)

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


**Both `a` and `b` refer to same object, when initialized with same value in same line**

* When a and b are set to `257` in the same line, the Python interpretor creates new object, then references the second variable at the same time. If you do it in separate lines, it doesn't "know" that there's already `257` as an object.
* It's a compiler optimization and specifically applies to interactive environment. When you do two lines in a live interpreter, they're compiled separately, therefore optimized separately. If you were to try this example in a `.py` file, you would not see the same behavior, because the file is compiled all at once.

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


# Contributing

All patches are Welcome! Filing an issue first before submitting a patch will be appreciated :)

# Acknowledgements

The idea and design for this list is inspired from Denys Dovhan's awesome project [wtfjs](https://github.com/denysdovhan/wtfjs).

* Reddit Link
* Youtube video link

# 🎓 License

[![CC 4.0][license-image]][license-url]

&copy; [Satwik Kansal](https://satwikkansal.xyz)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square

