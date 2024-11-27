---
hide:
  - toc
---

<p align="center"><img src="../images/logo.png#gh-light-mode-only" alt=""><img src="../images/logo-dark.png#gh-dark-mode-only" alt=""></p>
<h1 align="center">What the f*ck Python! 😱</h1>
<p align="center">Изучение и понимание Python с помощью нестандартного поведения и "магического" поведения.</p>

Другие переводы: [English Original](https://github.com/satwikkansal/wtfpython) | [Russian Русский](https://github.com/frontdevops/wtfpython) | [Chinese 中文](https://github.com/robertparley/wtfpython-cn) | [Vietnamese Tiếng Việt](https://github.com/vuduclyunitn/wtfptyhon-vi) | [Spanish Español](https://web.archive.org/web/20220511161045/https://github.com/JoseDeFreitas/wtfpython-es) | [Korean 한국어](https://github.com/buttercrab/wtfpython-ko) | [Add translation](https://github.com/satwikkansal/wtfpython/issues/new?title=Add%20translation%20for%20[LANGUAGE]&body=Expected%20time%20to%20finish:%20[X]%20weeks.%20I%27ll%20start%20working%20on%20it%20from%20[Y].)

Еще способы попробовать: [Interactive](https://colab.research.google.com/github/satwikkansal/wtfpython/blob/master/irrelevant/wtf.ipynb) | [CLI](https://pypi.python.org/pypi/wtfpython)

Python, будучи прекрасно разработанным языком программирования высокого уровня с интерпретатором, предоставляет нам множество возможностей для удобства программиста. Но иногда результаты работы фрагмента Python могут показаться неочевидными на первый взгляд.

Вот забавный проект, пытающийся объяснить, что именно происходит под капотом некоторых неинтуитивных сниппетов и менее известных возможностей Python.

Хотя некоторые из примеров, которые вы увидите ниже, возможно, не являются WTF в прямом смысле этого слова, но они раскроют некоторые интересные части Python, о которых вы могли не знать. Я считаю, что это хороший способ изучить внутреннее устройство языка программирования, и я верю, что вам это тоже покажется интересным!

Если вы опытный программист на Python, вы можете принять это как вызов, чтобы получить большинство из них правильно с первой попытки. Возможно, вы уже сталкивались с некоторыми из них раньше, и я смогу оживить ваши старые добрые воспоминания! :sweat_smile:

PS: Если вы постоянный читатель, вы можете узнать о новых изменениях [здесь](https://github.com/satwikkansal/wtfpython/releases/) (примеры, отмеченные звездочкой - это примеры, добавленные в последней основной редакции). 

Ну чтож, начнем...

# Table of Contents

<!-- Generated using "markdown-toc -i README.md --maxdepth 3"-->
<!-- toc -->
- [Структура примеров](#structure-of-the-examples)
    + [▶ Какое-то модное название](#-some-fancy-title)
- [Применение](#usage)
- [👀 Примеры](#-examples)
  * [Раздел: Напряги мозги!](#section-strain-your-brain)
    + [▶ Перво-наперво! *](#-first-things-first-)
    + [▶ Иногда строки могут быть хитрыми](#-strings-can-be-tricky-sometimes)
    + [▶ Осторожнее с цепочками операций](#-be-careful-with-chained-operations)
    + [▶ Как не надо использовать оператор `is`](#-how-not-to-use-is-operator)
    + [▶ Мистика хэширования](#-hash-brownies)
    + [▶ В глубине души мы все одинаковы](#-deep-down-were-all-the-same)
    + [▶ Беспорядок внутри порядка *](#-disorder-within-order-)
    + [▶ Продолжай пытаться... *](#-keep-trying-)
    + [▶ Для чего?](#-for-what)
    + [▶ Расхождение во времени оценки](#-evaluation-time-discrepancy)
    + [▶ `is not ...` не является `is(not ...)`](#-is-not--is-not-is-not-)
    + [▶ Крестики-нолики, где X побеждает в первой попытке!](#-a-tic-tac-toe-where-x-wins-in-the-first-attempt)
    + [▶ Переменная Шредингера](#-schrödingers-variable-)
    + [▶ The chicken-egg problem *](#-the-chicken-egg-problem-)
    + [▶ Отношения подклассов](#-subclass-relationships)
    + [▶ Методы равенства и тождества](#-methods-equality-and-identity)
    + [▶ All-true-ation *](#-all-true-ation-)
    + [▶ Удивительная запятая](#-the-surprising-comma)
    + [▶ Строки и обратные слеши](#-strings-and-the-backslashes)
    + [▶ not knot!](#-not-knot)
    + [▶ Строки с половиной тройных кавычек](#-half-triple-quoted-strings)
    + [▶ What's wrong with booleans?](#-whats-wrong-with-booleans)
    + [▶ Атрибуты класса и атрибуты экземпляра](#-class-attributes-and-instance-attributes)
    + [▶ yielding None](#-yielding-none)
    + [▶ Yielding из... возврата! *](#-yielding-from-return-)
    + [▶ NaN-рефлексивность *](#-nan-reflexivity-)
    + [▶ Мутация неизменного!](#-mutating-the-immutable)
    + [▶ Исчезающая переменная из внешней области видимости](#-the-disappearing-variable-from-outer-scope)
    + [▶ Загадочное преобразование типа ключа](#-the-mysterious-key-type-conversion)
    + [▶ Посмотрим, сможете ли вы угадать это?](#-lets-see-if-you-can-guess-this)
    + [▶ Exceeds the limit for integer string conversion](#-exceeds-the-limit-for-integer-string-conversion)
  * [Раздел: Скользкие склоны](#section-slippery-slopes)
    + [▶ Изменение словаря во время итерации по нему](#-modifying-a-dictionary-while-iterating-over-it)
    + [▶ Упрямая операция `del`](#-stubborn-del-operation)
    + [▶ Переменная вне области видимости](#-the-out-of-scope-variable)
    + [▶ Удаление элемента списка во время итерации](#-deleting-a-list-item-while-iterating)
    + [▶ zip итераторов с потерями *](#-lossy-zip-of-iterators-)
    + [▶ Loop variables leak out!](#-loop-variables-leaking-out)
    + [▶ Остерегайтесь мутабельных аргументов по умолчанию!](#-beware-of-default-mutable-arguments)
    + [▶ Catching the Exceptions](#-catching-the-exceptions)
    + [▶ Same operands, different story!](#-same-operands-different-story)
    + [▶ Разрешение имен, игнорирующее область действия класса](#-name-resolution-ignoring-class-scope)
    + [▶ Округление как у банкира *](#-rounding-like-a-banker-)
    + [▶ Needles in a Haystack *](#-needles-in-a-haystack-)
    + [▶ Splitsies *](#-splitsies-)
    + [▶ Дикий импорт *](#-wild-imports-)
    + [▶ Все отсортировано? *](#-all-sorted-)
    + [▶ Полуночное время не существует?](#-midnight-time-doesnt-exist)
  * [Раздел: Скрытые сокровища!](#section-the-hidden-treasures)
    + [▶ О'кей Питон, ты можешь заставить меня летать?](#-okay-python-can-you-make-me-fly)
    + [▶ `goto`, но почему?](#-goto-but-why)
    + [▶ Держитесь!](#-brace-yourself)
    + [▶ Давайте встретимся с дружелюбным языковым дядей на всю жизнь](#-lets-meet-friendly-language-uncle-for-life)
    + [▶ Даже Python понимает, что любовь - это сложно](#-even-python-understands-that-love-is-complicated)
    + [▶ Да, это существует!](#-yes-it-exists)
    + [▶ Многоточие *](#-ellipsis-)
    + [▶ Inpinity](#-inpinity)
    + [▶ Let's mangle](#-lets-mangle)
  * [Раздел: Внешность обманчива!](#section-appearances-are-deceptive)
    + [▶ Пропускаете строки?](#-skipping-lines)
    + [▶ Телепортация](#-teleportation)
    + [▶ Ну, что-то тут нечисто...](#-well-something-is-fishy)
  * [Раздел: Разное](#section-miscellaneous)
    + [▶ `+=` быстрее](#--is-faster)
    + [▶ Давайте создадим гигантскую строку!](#-lets-make-a-giant-string)
    + [▶ Замедление поиска `dict` *](#-slowing-down-dict-lookups-)
    + [▶ Раздувание экземпляров словарей *](#-bloating-instance-dicts-)
    + [▶ Minor Ones *](#-minor-ones-)
- [Contributing](#contributing)
- [Благодарности](#acknowledgements)
- [🎓 Лицензия](#-license)
  * [Удивите и своих друзей!](#surprise-your-friends-as-well)
  * [Больше подобных материалов?](#more-content-like-this)
<!-- tocstop -->

# Структура примеров

Все примеры имеют следующую структуру:

> ### ▶ Какой-то заголовок
>
> ```py
> # Код с приколдесами.
> # Подготовка к магии...
> ```
>
> **Вывод (Python версия(и)):**
>
> ```py
> >>> triggering_statement
> Неожиданные результаты
> ```
> (Опционально): Одна строка, описывающая неожиданный результат
>
>
> #### 💡 Объяснение:
>
> * Краткое объяснение того, что происходит и почему это происходит.
> ```py
> # Код
> # Дополнительные примеры для дальнейшего разъяснения (если необходимо)
> ```
> **Вывод (Python версия(и)):**
>
> ```py
> >>> trigger # какой-нибудь пример, позволяющий легко раскрыть магию
> # обоснованный вывод
> ```

**Важно:** Все примеры протестированы на интерактивном интерпретаторе Python 3.5.2, и они должны работать для всех версий Python, если это явно не указано перед выводом.

# Применение

Хороший способ получить максимальную пользу от этих примеров, на мой взгляд, - читать их в последовательном порядке, причем для каждого примера:
- Внимательно прочитайте исходный код для настройки примера. Если вы опытный программист на Python, то в большинстве случаев вы сможете предугадать, что произойдет дальше.
- Прочитайте фрагменты вывода и,
  + Проверьте, совпадают ли выходные данные с вашими ожиданиями.
  + Убедитесь, что вы знаете точную причину, по которой вывод получился именно таким.
    - Если ответ отрицательный (что совершенно нормально), сделайте глубокий вдох и прочитайте объяснение (а если вы все еще не понимаете, крикните! и создайте проблему [здесь](https://github.com/satwikkansal/wtfpython/issues/new)).
    - Если "да", похлопайте себя по спине и переходите к следующему примеру.

PS: Вы также можете читать WTFPython в командной строке, используя [pypi package](https://pypi.python.org/pypi/wtfpython),
```sh
$ pip install wtfpython -U
$ wtfpython
```
---

# 👀 Примеры

## Секция: Напряги мозги!

### ▶ Важное о главном!

<!-- Example ID: d3d73936-3cf1-4632-b5ab-817981338863 -->
<!-- read-only -->

По какой-то причине "моржовый оператор"(walrus) (`:=`) в Python 3.8 стал довольно популярным. Давайте проверим его,

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



#### 💡 Обьяснение

**Быстрый разбор что такое "моржовый оператор" (walrus)**

"Моржовый оператор" (`:=`) была введена в Python 3.8, она может быть полезна в ситуациях, когда вы хотите присвоить значения переменным в выражении.

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

**Вывод (> 3.8):**

```py
5
5
5
```

Это сэкономило одну строку кода и неявно предотвратило вызов `some_func` дважды.

- Непарентезированное "выражение присваивания" (использование моржового оператора), ограничено на верхнем уровне, отсюда `SyntaxError` в выражении `a := "wtf_walrus"` первого фрагмента. Расстановка парентез сработала, как и ожидалось, и присвоила `a`.  

- Как обычно, выделение скобками выражения, содержащего оператор `=`, не допускается. Отсюда синтаксическая ошибка в `(a, b = 6, 9)`. 

- Синтаксис моржового оператора имеет вид `NAME:= expr`, где `NAME` - допустимый идентификатор, а `expr` - допустимое выражение. Следовательно, упаковка и распаковка итерабельных выражений не поддерживается, что означает, 

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

### ▶ Строки иногда ведут себя непредсказуемо

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
>>> a is b # Все версии, кроме 3.7.x
True

>>> a = "wtf!"; b = "wtf!"
>>> a is b # Это выведет True или False в зависимости от того, где вы вызываете (python shell / ipython / as a script)
False
```

```py
# This time in file some_file.py
a = "wtf!"
b = "wtf!"
print(a is b)

# выводит True при вызове модуля!
```

4\.

**Результат (< Python3.7 )**

```py
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
```

Логично, правда?

#### 💡 Объяснение:
+ Поведение в первом и втором фрагментах связано с оптимизацией CPython (называемой интернированием строк), которая пытается использовать существующие неизменяемые объекты в некоторых случаях вместо того, чтобы каждый раз создавать новый объект.
+ После "интернирования" многие переменные могут ссылаться на один и тот же строковый объект в памяти (тем самым экономя память).
+ В приведенных выше фрагментах строки неявно интернированы. Решение о том, когда неявно интернировать строку, зависит от реализации. Существуют некоторые правила, по которым можно определить, будет ли строка интернирована или нет:
  * Все строки длины 0 и длины 1 интернируются.
  * Строки интернируются во время компиляции (`'wtf'' будет интернирована, но `''.join(['w'', 't'', 'f'])` не будет интернирована)
  * Строки, не состоящие из букв ASCII, цифр или знаков подчеркивания, не интернализируются. Это объясняет, почему `'wtf!'` не интернируется из-за `!`. Реализацию этого правила в CPython можно найти [здесь](https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19)
  ![image](../images/string-intern/string_intern.png)
+ Когда `a` и `b` имеют значение `"wtf!"` в одной строке, интерпретатор Python создает новый объект, а затем одновременно ссылается на вторую переменную. Если вы делаете это в отдельных строках, он не "знает", что уже существует `"wtf!"` как объект (потому что `"wtf!"` не является неявно интернированным в соответствии с фактами, упомянутыми выше). Это оптимизация времени компиляции. Эта оптимизация не применяется к версиям CPython 3.7.x (более подробное обсуждение смотрите здесь [issue](https://github.com/satwikkansal/wtfpython/issues/100)).
+ Единица компиляции в интерактивной среде, такой как IPython, состоит из одного оператора, тогда как в случае модулей она состоит из всего модуля. `a, b = "wtf!", "wtf!"` - это одно утверждение, тогда как `a = "wtf!"; b = "wtf!"` - это два утверждения в одной строке. Это объясняет, почему тождества различны в `a = "wtf!"; b = "wtf!"`, а также объясняет, почему они одинаковы при вызове в `some_file.py`.
+ Резкое изменение в выводе четвертого фрагмента связано с [peephole optimization](https://en.wikipedia.org/wiki/Peephole_optimization) техникой, известной как Constant folding. Это означает, что выражение `'a'*20` заменяется на `'aaaaaaaaaaaaaaaaaaaa'` во время компиляции, чтобы сэкономить несколько тактов во время выполнения. Складывание констант происходит только для строк длиной менее 21. (Почему? Представьте себе размер файла `.pyc`, созданного в результате выражения `'a'*10**10`). [Вот](https://github.com/python/cpython/blob/3.6/Python/peephole.c#L288) исходный текст реализации для этого.
+ Примечание: В Python 3.7 складывание констант было перенесено из оптимизатора peephole в новый оптимизатор AST с некоторыми изменениями в логике, поэтому четвертый фрагмент не работает в Python 3.7. Подробнее об изменении можно прочитать [здесь](https://bugs.python.org/issue11549). 

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

#### 💡 Объяснение:

As per https://docs.python.org/3/reference/expressions.html#comparisons

> Формально, если a, b, c, ..., y, z - выражения, а op1, op2, ..., opN - операторы сравнения, то a op1 b op2 c ... y opN z эквивалентно a op1 b и b op2 c и ... y opN z, за исключением того, что каждое выражение оценивается не более одного раза.

Хотя такое поведение может показаться вам глупым в приведенных выше примерах, оно просто фантастично для таких вещей, как `a == b == c` и `0 <= x <= 100`.

* `False is False is False` эквивалентно `(False is False) и (False is False)`.
* ``True is False == False`` эквивалентно ``(True is False) and (False == False)`` и так как первая часть высказывания (`True is False``) оценивается в `False``, то все выражение оценивается в `False``.
* `1 > 0 < 1` эквивалентно `(1 > 0) и (0 < 1)`, которое оценивается в `True`.
* Выражение `(1 > 0) < 1` эквивалентно `True < 1` и
  ```py
  >>> int(True)
  1
  >>> True + 1 # не имеет значения для данного примера, но просто для интереса
  2
  ```
  В итоге, `1 < 1` выполняется и дает результат `False`

---

### ▶ Как не надо использовать оператор `is`
<!-- Example ID: 230fa2ac-ab36-4ad1-b675-5f5a1c1a6217 --->
Ниже приведен очень известный пример, представленный во всем Интернете.

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
**Результат**

```py
>>> a, b = 257, 257
>>> a is b
True
```

**Вывод (Python 3.7.x specifically)**

```py
>>> a, b = 257, 257
>>> a is b
False
```

#### 💡 Объяснение:

**Разница между `is` и `==`**.

* Оператор `is` проверяет, ссылаются ли оба операнда на один и тот же объект (т.е. проверяет, совпадают ли идентификаторы операндов или нет).
* Оператор `==` сравнивает значения обоих операндов и проверяет, одинаковы ли они.
* Таким образом, оператор `is` предназначен для равенства ссылок, а `==` - для равенства значений. Пример, чтобы прояснить ситуацию,
  ```py
  >>> class A: pass
  >>> A() is A() # These are two empty objects at two different memory locations.
  False
  ```

**`256` - существующий объект, а `257` - нет**.

При запуске python будут выделены числа от `-5` до `256`. Эти числа используются часто, поэтому имеет смысл просто иметь их наготове.

Цитирую по https://docs.python.org/3/c-api/long.html
> Текущая реализация хранит массив целочисленных объектов для всех целых чисел от -5 до 256, когда вы создаете int в этом диапазоне, вы просто получаете обратно ссылку на существующий объект. Поэтому должно быть возможно изменить значение 1. Я подозреваю, что поведение Python в этом случае не определено. :-)

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

Здесь интерпретатору не хватает мозгов при выполнении `y = 257` понять, что мы уже создали целое число со значением `257,` и поэтому он продолжает создавать другой объект в памяти.

Подобная оптимизация применима и к другим **изменяемым** объектам, таким как пустые кортежи. Поскольку списки являются изменяемыми, поэтому `[] is []` вернет `False`, а `() is ()` вернет `True`. Это объясняет наш второй фрагмент. Перейдем к третьему, 

**И `a`, и `b` ссылаются на один и тот же объект при инициализации одним и тем же значением в одной и той же строке*.

**Вывод**

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

* Когда a и b устанавливаются в `257` в одной строке, интерпретатор Python создает новый объект, а затем одновременно ссылается на вторую переменную. Если вы делаете это в отдельных строках, он не "знает", что объект `257` уже существует.

* Это оптимизация компилятора и относится именно к интерактивной среде. Когда вы вводите две строки в живом интерпретаторе, они компилируются отдельно, поэтому оптимизируются отдельно. Если бы вы попробовали этот пример в файле `.py', вы бы не увидели такого же поведения, потому что файл компилируется весь сразу. Эта оптимизация не ограничивается целыми числами, она работает и для других неизменяемых типов данных, таких как строки (проверьте пример "Строки - это сложно") и плавающие числа,

  ```py
  >>> a, b = 257.0, 257.0
  >>> a is b
  True
  ```

* Почему это не сработало в Python 3.7? Абстрактная причина в том, что такие оптимизации компилятора зависят от реализации (т.е. могут меняться в зависимости от версии, ОС и т.д.). Я все еще выясняю, какое именно изменение реализации вызвало проблему, вы можете проверить этот [issue](https://github.com/satwikkansal/wtfpython/issues/100) для получения обновлений.

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

**Вывод:**

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

Так почему же Python повсюду?


#### 💡 Объяснение.

* Уникальность ключей в словаре Python определяется *эквивалентностью*, а не тождеством. Поэтому, даже если `5`, `5.0` и `5 + 0j` являются различными объектами разных типов, поскольку они равны, они не могут находиться в одном и том же `дикте` (или `наборе`). Как только вы вставите любой из них, попытка поиска по любому другому, но эквивалентному ключу будет успешной с исходным сопоставленным значением (а не завершится ошибкой `KeyError`):
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
* Это применимо и при установке элемента. Поэтому, когда вы делаете `some_dict[5] = "Python"`, Python находит существующий элемент с эквивалентным ключом `5.0 -> "Ruby"`, перезаписывает его значение на место, а исходный ключ оставляет в покое.
  ```py
  >>> some_dict
  {5.0: 'Ruby'}
  >>> some_dict[5] = "Python"
  >>> some_dict
  {5.0: 'Python'}
  ```
* Итак, как мы можем обновить ключ до `5` (вместо `5.0`)? На самом деле мы не можем сделать это обновление на месте, но что мы можем сделать, так это сначала удалить ключ (`del some_dict[5.0]`), а затем установить его (`some_dict[5]`), чтобы получить целое число `5` в качестве ключа вместо плавающего `5.0`, хотя это нужно в редких случаях.

* Как Python нашел `5` в словаре, содержащем `5.0`? Python делает это за постоянное время без необходимости сканирования каждого элемента, используя хэш-функции. Когда Python ищет ключ `foo` в словаре, он сначала вычисляет `hash(foo)` (что выполняется в постоянном времени). Поскольку в Python требуется, чтобы объекты, которые сравниваются одинаково, имели одинаковое хэш-значение ([docs](https://docs.python.org/3/reference/datamodel.html#object.__hash__) здесь), `5`, `5.0` и `5 + 0j` имеют одинаковое хэш-значение.
  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> hash(5) == hash(5.0) == hash(5 + 0j)
  True
  ```
  **Примечание:** Обратное не обязательно верно: Объекты с одинаковыми хэш-значениями сами могут быть неравными. (Это вызывает так называемую [хэш-коллизию](https://en.wikipedia.org/wiki/Collision_(computer_science)) и ухудшает производительность постоянного времени, которую обычно обеспечивает хэширование).

---

### ▶ В глубине души мы все одинаковы.
<!-- Example ID: 8f99a35f-1736-43e2-920d-3b78ec35da9b --->
```py
class WTF:
  pass
```

**Вывод:**
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
#### 💡 Объяснение:

* При вызове `id` Python создал объект класса `WTF` и передал его функции `id`. Функция `id` забирает свой `id` (местоположение в памяти) и выбрасывает объект. Объект уничтожается.
* Когда мы делаем это дважды подряд, Python выделяет ту же самую область памяти и для второго объекта. Поскольку (в CPython) `id` использует участок памяти в качестве идентификатора объекта, идентификатор двух объектов одинаков.
* Таким образом, id объекта уникален только в течение жизни объекта. После уничтожения объекта или до его создания, что-то другое может иметь такой же id.
* Но почему оператор `is` имеет значение `False`? Давайте посмотрим с помощью этого фрагмента.
  ```py
  class WTF(object):
    def __init__(self): print("I")
    def __del__(self): print("D")
  ```

  **Вывод:**
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
  Как вы можете заметить, порядок, в котором уничтожаются объекты, имеет значение.

---

### ▶ Нарушение в пределах порядка *
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

**Вывод**
```py
>>> dictionary == ordered_dict # If a == b
True
>>> dictionary == another_ordered_dict # and b == c
True
>>> ordered_dict == another_ordered_dict # then why isn't c == a ??
False

# Мы все знаем, что множество состоит только из уникальных элементов,
# давайте попробуем составить множество из этих словарей и посмотрим, что получится...

>>> len({dictionary, ordered_dict, another_ordered_dict})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

# Имеет смысл, поскольку в словаре не реализовано свойство __hash__, ну чтож давайте использовать
# наши классы-обертки.
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

Что здесь происходит?

#### 💡 Объяснение:

- Причина, по которой не выполняется транзитивное равенство между `dictionary`, `ordered_dict` и `another_ordered_dict`, заключается в том, как реализован метод `__eq__` в классе `OrderedDict`. Из [docs](https://docs.python.org/3/library/collections.html#ordereddict-objects)
  
    > Тесты равенства между объектами OrderedDict чувствительны к порядку и реализуются как `list(od1.items())==list(od2.items())`. Тесты на равенство между объектами `OrderedDict` и другими объектами Mapping нечувствительны к порядку, как обычные словари.
- Причина такого поведения равенства в том, что оно позволяет напрямую подставлять объекты `OrderedDict` везде, где используется обычный словарь.
- Итак, почему изменение порядка влияет на длину генерируемого объекта `set`? Ответ заключается только в отсутствии интранзитивного равенства. Поскольку множества являются "неупорядоченными" коллекциями уникальных элементов, порядок вставки элементов не должен иметь значения. Но в данном случае он имеет значение. Давайте немного разберемся в этом,
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
    Таким образом, несоответствие связано с тем, что `another_ordered_dict в another_set` является `False`, потому что `ordered_dict` уже присутствовал в `another_set` и, как было замечено ранее, `ordered_dict == another_ordered_dict` является `False`.

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

**Результат:**

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

#### 💡 Объяснение:

- Когда оператор `return`, `break` или `continue` выполняется в наборе `try` оператора "try...finally", на выходе также выполняется пункт `finally`.
- Возвращаемое значение функции определяется последним выполненным оператором `return`. Поскольку предложение `finally` выполняется всегда, оператор `return`, выполненный в предложении `finally`, всегда будет последним.
- Оговорка заключается в том, что если в предложении finally выполняется оператор `return` или `break`, то временно сохраненное исключение отбрасывается.

---


### ▶ Для чего?
<!-- Example ID: 64a9dccf-5083-4bc9-98aa-8aeecde4f210 --->
```py
some_string = "wtf"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    i = 10
```

**Вывод:**
```py
>>> some_dict # An indexed dict appears.
{0: 'w', 1: 't', 2: 'f'}
```

#### 💡 Объяснение:

* Оператор `for` определяется в [грамматике Python](https://docs.python.org/3/reference/grammar.html) как:
  ```
  for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
  ```
  Где `exprlist` - цель присваивания. Это означает, что эквивалент `{exprlist} = {next_value}` **выполняется для каждого элемента** в итерабле.
  Интересный пример, иллюстрирующий это:
  ```py
  for i in range(4):
      print(i)
      i = 10
  ```

  **Результат:**
  ```
  0
  1
  2
  3
  ```

  Ожидали ли вы, что цикл будет запущен только один раз?

  **💡 Объяснение:**.

  - Оператор присваивания `i = 10` никогда не влияет на итерации цикла из-за того, как циклы for работают в Python. Перед началом каждой итерации следующий элемент, предоставляемый итератором (в данном случае `range(4)`), распаковывается и присваивается переменной целевого списка (в данном случае `i`).

* Функция `enumerate(some_string)` на каждой итерации выдает новое значение `i` (счетчик, идущий вверх) и символ из `some_string`. Затем она устанавливает (только что присвоенный) ключ `i` словаря `some_dict` на этот символ. Развертывание цикла можно упростить следующим образом:
  ```py
  >>> i, some_dict[i] = (0, 'w')
  >>> i, some_dict[i] = (1, 't')
  >>> i, some_dict[i] = (2, 'f')
  >>> some_dict
  ```

---

### ▶ Несоответствие времени оценки
<!-- Example ID: 6aa11a4b-4cf1-467a-b43a-810731517e98 --->
1\.
```py
array = [1, 8, 15]
# A typical generator expression
gen = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
```

**Вывод:**

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

**Вывод:**
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

**Вывод:**
```py
>>> print(list(gen))
[401, 501, 601, 402, 502, 602, 403, 503, 603]
```

#### 💡 Пояснение

- В выражении [generator](https://wiki.python.org/moin/Generators) условие `in` оценивается во время объявления, но условное условие оценивается во время выполнения.
- Поэтому перед выполнением `array` переназначается на список `[2, 8, 22]`, а поскольку из `1`, `8` и `15` только счетчик `8` больше `0`, генератор выдает только `8`.
- Различия в выводе `g1` и `g2` во второй части связаны с тем, как переменным `array_1` и `array_2` присваиваются новые значения.
- В первом случае `array_1` привязывается к новому объекту `[1,2,3,4,5]`, а поскольку предложение `in` оценивается во время объявления, оно по-прежнему ссылается на старый объект `[1,2,3,4]` (который не уничтожается).
- Во втором случае присвоение среза `array_2` обновляет тот же старый объект `[1,2,3,4]` до `[1,2,3,4,5]`. Следовательно, и `g2`, и `array_2` по-прежнему имеют ссылку на один и тот же объект (который теперь обновлен до `[1,2,3,4,5]`).
- Хорошо, следуя логике, рассмотренной до сих пор, не должно ли значение `list(gen)` в третьем фрагменте быть `[11, 21, 31, 12, 22, 32, 13, 23, 33]`? (потому что `array_3` и `array_4` будут вести себя так же, как `array_1`). Причина, по которой (только) значения `array_4` обновляются, объясняется в [PEP-289](https://www.python.org/dev/peps/pep-0289/#the-details)
  
    > Только крайнее for-выражение оценивается немедленно, остальные выражения откладываются до запуска генератора.

---


### ▶ `is not ...` is not `is (not ...)`
<!-- Example ID: b26fb1ed-0c7d-4b9c-8c6d-94a58a055c0d --->
```py
>>> 'something' is not None
True
>>> 'something' is (not None)
False
```

#### 💡 Пояснение

- `is not` является единым бинарным оператором, и его поведение отличается от раздельного использования `is` и `not`.
- `is not` имеет значение `False`, если переменные по обе стороны оператора указывают на один и тот же объект, и `True` в противном случае. 
- В примере `(not None)` оценивается в `True`, поскольку значение `None` является `False` в булевом контексте, поэтому выражение становится `'something' is True`.

---

### ▶ Крестики-нолики, где X побеждает с первой попытки!
<!-- Example ID: 69329249-bdcb-424f-bd09-cca2e6705a7a --->

```py
# Let's initialize a row
row = [""] * 3 #row i['', '', '']
# Let's make a board
board = [row] * 3
```

**Результат:**

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

Мы же не назначили три ``Х``?

#### 💡 Объяснение:

Когда мы инициализируем переменную `row`, эта визуализация объясняет, что происходит в памяти

![image](../images/tic-tac-toe/after_row_initialized.png)

А когда `board` инициализируется путем умножения `row`, вот что происходит в памяти (каждый из элементов `board[0]`, `board[1]` и `board[2]` является ссылкой на тот же список, на который ссылается `row`)

![image](../images/tic-tac-toe/after_board_initialized.png)

Мы можем избежать этого сценария, не используя переменную `row` для генерации `board`. (Вопрос задан в [этом](https://github.com/satwikkansal/wtfpython/issues/68) выпуске).

```py
>>> board = [['']*3 for _ in range(3)]
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['', '', ''], ['', '', '']]
```

---

### ▶ Переменная Шредингера *
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

**Вывод (Python version):**
```py
>>> results
[0, 1, 2, 3, 4, 5, 6]
>>> funcs_results
[6, 6, 6, 6, 6, 6, 6]
```

Значения `x` были разными в каждой итерации до добавления `some_func` к `funcs`, но все функции возвращают 6, когда они оцениваются после завершения цикла.

2.

```py
>>> powers_of_x = [lambda x: x**i for i in range(10)]
>>> [f(2) for f in powers_of_x]
[512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
```

#### 💡 Объяснение:
* При определении функции внутри цикла, которая использует переменную цикла в своем теле, закрытие функции цикла привязывается к *переменной*, а не к ее *значению*. Функция ищет `x` в окружающем контексте, а не использует значение `x` на момент создания функции. Таким образом, все функции используют для вычислений последнее значение, присвоенное переменной. Мы можем видеть, что используется `x` из окружающего контекста (т.е. *не* локальная переменная):
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

* Чтобы получить желаемое поведение, вы можете передать переменную цикла как именованную переменную в функцию. **Почему это работает?** Потому что это определит переменную *внутри* области видимости функции. Она больше не будет обращаться к окружающей (глобальной) области видимости для поиска значения переменной, а создаст локальную переменную, которая будет хранить значение `x` в данный момент времени.

```py
funcs = []
for x in range(7):
    def some_func(x=x):
        return x
    funcs.append(some_func)
```

**Вывод:**

```py
>>> funcs_results = [func() for func in funcs]
>>> funcs_results
[0, 1, 2, 3, 4, 5, 6]
```

`x` больше не и спользуется в глобальной области видимости

```py
>>> inspect.getclosurevars(funcs[0])
ClosureVars(nonlocals={}, globals={}, builtins={}, unbound=set())
```

---

### ▶ Проблема курицы и яйца *
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

Так какой же базовый класс является "окончательным"? Кстати, это еще не все,

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


#### 💡 Объяснение

- `тип` - это [метакласс](https://realpython.com/python-metaclasses/) в Python.
- **Все** в Python является `объектом`, что включает в себя как классы, так и их объекты (экземпляры).
- Класс `type` является метаклассом класса `object`, и каждый класс (включая `type`) наследует прямо или косвенно от `object`.
- Между `object` и `type` нет реального базового класса. Путаница в приведенных выше фрагментах возникает потому, что мы думаем об этих отношениях (`issubclass` и `isinstance`) в терминах классов Python. Отношения между `object` и `type` не могут быть воспроизведены в чистом Python. Точнее говоря, следующие отношения не могут быть воспроизведены в чистом Python,
    + класс A является экземпляром класса B, а класс B является экземпляром класса A.
    + класс A является экземпляром самого себя.
- Эти отношения между `object` и `type` (оба являются экземплярами друг друга, а также самих себя) существуют в Python из-за "обмана" на уровне реализации.

---

### ▶ Отношения между подклассами
<!-- Example ID: 9f6d8cf0-e1b5-42d0-84a0-4cfab25a0bc0 --->
**Вывод:**
```py
>>> from collections import Hashable
>>> issubclass(list, object)
True
>>> issubclass(object, Hashable)
True
>>> issubclass(list, Hashable)
False
```

Предполагается, что отношения подклассов должны быть транзитивными, верно? (т.е. если `A` является подклассом `B`, а `B` является подклассом `C`, то `A` _должен_ быть подклассом `C`)

#### 💡 Пояснение:

* Отношения подклассов не обязательно являются транзитивными в Python. Любой может определить свой собственный, произвольный `__subclasscheck__` в метаклассе.
* Когда вызывается `issubclass(cls, Hashable)`, он просто ищет не-фальшивый метод "`__hash__`" в `cls` или во всем, от чего он наследуется.
* Поскольку `object` является хэшируемым, а `list` - нехэшируемым, это нарушает отношение транзитивности.
* Более подробное объяснение можно найти [здесь] (https://www.naftaliharris.com/blog/python-subclass-intransitivity/).
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

**Результат:**
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

Обращаясь к `classm` дважды, мы получаем одинаковый объект, но не *одинаковый*? Давайте посмотрим, что происходит
с экземплярами `SomeClass`:

2.
```py
o1 = SomeClass()
o2 = SomeClass()
```

**Вывод:**
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

Двойной доступ к `классу` или `методу` создает одинаковые, но не *одинаковые* объекты для одного и того же экземпляра `какого-либо класса`.

#### 💡 Пояснение.
* Функции являются [дескрипторами](https://docs.python.org/3/howto/descriptor.html). Всякий раз, когда к функции обращаются как к
атрибута, вызывается дескриптор, создавая объект метода, который "связывает" функцию с объектом, владеющим атрибутом.
атрибутом. При вызове метод вызывает функцию, неявно передавая связанный объект в качестве первого аргумента
(именно так мы получаем `self` в качестве первого аргумента, несмотря на то, что не передаем его явно).
```py
>>> o1.method
<bound method SomeClass.method of <__main__.SomeClass object at ...>>
```
* При многократном обращении к атрибуту каждый раз создается объект метода! Поэтому `o1.method is o1.method` является
никогда не является истиной. Доступ к функциям как к атрибутам класса (в отличие от экземпляра) не создает методов, однако; поэтому
`SomeClass.method is SomeClass.method` является истинным.
```py
>>> SomeClass.method
<function SomeClass.method at ...>
```
* `classmethod` преобразует функции в методы класса. Методы класса - это дескрипторы, которые при обращении к ним создают
объект метода, который связывает *класс* (тип) объекта, а не сам объект.
```py
>>> o1.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* В отличие от функций, `classmethod` будет создавать метод и при обращении к нему как к атрибуту класса (в этом случае они
привязываются к классу, а не к его типу). Поэтому `SomeClass.classm is SomeClass.classm` является ошибочным.
```py
>>> SomeClass.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* Объект метода сравнивается с равным, если обе функции равны, а связанные объекты одинаковы. Поэтому
`o1.method == o1.method` является истинным, хотя и не является одним и тем же объектом в памяти.
* `staticmethod` преобразует функции в дескриптор "no-op", который возвращает функцию как есть. Никакой метод
никогда не создается, поэтому сравнение с `is` является истинным.
```py
>>> o1.staticm
<function SomeClass.staticm at ...>
>>> SomeClass.staticm
<function SomeClass.staticm at ...>
```
* Необходимость создавать новые объекты "метод" каждый раз, когда Python вызывает методы экземпляра, и необходимость изменять аргументы
каждый раз, чтобы вставить `self`, сильно сказывается на производительности.
CPython 3.7 [решил эту проблему](https://bugs.python.org/issue26110), введя новые опкоды, которые работают с вызовом методов
без создания временных объектов методов. Это используется только при фактическом вызове функции доступа, так что
приведенные здесь фрагменты не затронуты и по-прежнему генерируют методы :)

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

Почему это изменение True-False?

#### 💡 Объяснение:

- Реализация функции `all` эквивалентна

- ```py
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

- `all([])` возвращает `True`, поскольку итерируемый массив пуст. 
- `all([[]])` возвращает `False`, поскольку переданный массив имеет один элемент, `[]`, а в python пустой список является ложным.
- `all([[[[]]])` и более высокие рекурсивные варианты всегда `True`. Это происходит потому, что единственный элемент переданного массива (`[[...]]`) уже не пуст, а списки со значениями являются истинными.

---

### ▶ Неожиданная запятая
<!-- Example ID: 31a819c8-ed73-4dcc-84eb-91bedbb51e58 --->
**Вывод (< 3.6):**

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

#### 💡 Объяснение:

- Запятая в конце списка формальных параметров функции Python не всегда законна.
- В Python список аргументов определяется частично с помощью ведущих запятых, а частично с помощью проходных запятых. Этот конфликт приводит к ситуациям, когда запятая оказывается в середине, и ни одно правило ее не принимает.
- **Примечание:** Проблема с запятыми в конце списка аргументов [исправлена в Python 3.6](https://bugs.python.org/issue9232). Замечания в [этом](https://bugs.python.org/issue9232#msg248399) сообщении кратко обсуждают различные варианты использования запятых в Python.

---

### ▶ Строки и обратные слэши
<!-- Example ID: 6ae622c3-6d99-4041-9b33-507bd1a4407b --->
**Вывод:**
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

#### 💡 Пояснение

- В обычной строке python обратная косая черта используется для экранирования символов, которые могут иметь специальное значение (например, одинарная кавычка, двойная кавычка и сама обратная косая черта).
    ```py
    >>> "wt\"f"
    'wt"f'
    ```
- В необработанном строковом литерале (на что указывает префикс `r`) обратные косые черты передаются как есть, вместе с поведением экранирования следующего символа.
    ```py
    >>> r'wt\"f' == 'wt\\"f'
    True
    >>> print(repr(r'wt\"f')
    'wt\\"f'

    >>> print("\n")

    >>> print(r"\\n")
    '\\n'
    ```
- Это означает, что когда синтаксический анализатор встречает обратную косую черту в необработанной строке, он ожидает, что за ней последует другой символ. А в нашем случае (`print(r"\")`) обратная косая черта вырвалась из концевой кавычки, оставив парсер без завершающей кавычки (отсюда `SyntaxError`). Вот почему обратный слеш не работает в конце необработанной строки.

---

### ▶ not knot!
<!-- Example ID: 7034deb1-7443-417d-94ee-29a800524de8 --->
```py
x = True
y = False
```

**Результат:**
```py
>>> not x == y
True
>>> x == not y
  File "<input>", line 1
    x == not y
           ^
SyntaxError: invalid syntax
```

#### 💡 Объяснение:

* Старшинство операторов влияет на то, как оценивается выражение, и оператор `==` имеет более высокий приоритет, чем оператор `not` в Python.
* Поэтому `not x == y` эквивалентно `not (x == y)`, что эквивалентно `not (True == False)`, в итоге оценивающемуся в `True`.
* Но `x == not y` вызывает `SyntaxError`, потому что его можно считать эквивалентным `(x == not) y`, а не `x == (not y)`, что можно было бы ожидать на первый взгляд.
* Парсер ожидал, что лексема `not` будет частью оператора `not in` (потому что оба оператора `==` и `not in` имеют одинаковый приоритет), но после того, как он не смог найти лексему `in`, следующую за лексемой `not`, он выдает `SyntaxError`.

---

### ▶ Половина строк в тройных кавычках
<!-- Example ID: c55da3e2-1034-43b9-abeb-a7a970a2ad9e --->
**Вывод:**
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

#### 💡 Объяснение:
+ Python поддерживает неявную [конкатенацию строковых литералов](https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation), Пример,
  ```
  >>> print("wtf" "python")
  wtfpython
  >>> print("wtf" "") # or "wtf"""
  wtf
  ```
+ `'''` and `"""` также являются разделителями строк в Python, что вызывает SyntaxError, поскольку интерпретатор Python ожидал завершающую тройную кавычку в качестве разделителя при сканировании текущего встреченного строкового литерала с тройной кавычкой.
---

### ▶ Что не так с логическими значениями?
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

**Результат:**
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

**Результат (< 3.x):**

```py
>>> tell_truth()
I have lost faith in truth!
```



#### 💡 Объяснение:

* `bool` это подкласс класса `int` в Python
    
    ```py
    >>> issubclass(bool, int)
    True
    >>> issubclass(int, bool)
    False
    ```
    
* И `True` и так же `False` это инстансы класса `int`
  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

* Целочисленное значение `True` равно `1`, а `False` равно `0`.
  ```py
  >>> int(True)
  1
  >>> int(False)
  0
  ```

* Смотри StackOverflow [answer](https://stackoverflow.com/a/8169049/4354153) там есть объяснение.

* Изначально в Python не было типа `bool` (использовали 0 для false и ненулевое значение 1 для true).  В версиях 2.x были добавлены `True`, `False` и тип `bool`, но для обратной совместимости `True` и `False` нельзя было сделать константами. Они просто были встроенными переменными, и их можно было переназначить.

* Python 3 был несовместим с предыдущими версиями, эту проблему наконец-то исправили, и поэтому последний фрагмент не будет работать с Python 3.x!

---

### ▶ Атрибуты класса и экземпляра
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

**Результат:**
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

**Результат:**

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

#### 💡 Объяснение:

* Переменные класса и переменные экземпляров класса внутренне обрабатываются как словари объекта класса. Если имя переменной не найдено в словаре текущего класса, оно ищется в родительских классах.
* Оператор += изменяет изменяемый объект на месте, не создавая новый объект. Таким образом, изменение атрибута одного экземпляра влияет на другие экземпляры и атрибут класса также.
---

### ▶ Возврат None из генератора (yielding None)
<!-- Example ID: 5a40c241-2c30-40d0-8ba9-cf7e097b3b53 --->
```py
some_iterable = ('a', 'b')

def some_func(val):
    return "something"
```

**Результат (<= 3.7.x):**

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

#### 💡 Объяснение:
- Это баг в обработке yield в генераторах и списочных выражениях CPython.
- Исходный код и объяснение можно найти здесь: https://stackoverflow.com/questions/32139885/yield-in-list-comprehensions-and-generator-expressions
- Связанный отчет об ошибке: https://bugs.python.org/issue10544
- В Python 3.8+ yield внутри списочных выражений больше не допускается и выдает SyntaxError.

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

**Результат (> 3.3):**

```py
>>> list(some_func(3))
[]
```

Куда исчезло "wtf"? Это связано с каким-то особым эффектом yield from? Давайте проверим это. То же самое, это тоже не сработало.

2\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        for i in range(x):
          yield i
```

**Результат:**

```py
>>> list(some_func(3))
[]
```

То же самое, это тоже не сработало. Что происходит?

#### 💡 Объяснение:

+ С Python 3.3 стало возможным использовать оператор return в генераторах с возвращением значения (см. PEP380). В официальной документации говорится, что

> "... return expr в генераторе вызывает исключение StopIteration(expr) при выходе из генератора."

+ В случае some_func(3) StopIteration возбуждается в начале из-за оператора return. Исключение StopIteration автоматически перехватывается внутри обертки list(...) и цикла for. Поэтому два вышеприведенных фрагмента приводят к пустому списку.

+ Чтобы получить ["wtf"] из генератора some_func, нам нужно перехватить исключение StopIteration.

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

**Результат:**

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



#### 💡 Объяснение:

- `'inf'` и `'nan'` - это специальные строки (без учета регистра), которые при явном приведении к типу float используются для представления математической "бесконечности" и "не число" соответственно.

- Поскольку согласно стандартам IEEE `NaN! = NaN`, соблюдение этого правила нарушает предположение о рефлексивности элемента коллекции в Python, то есть если x является частью коллекции, такой как `list`, реализации, такие как сравнение, основаны на предположении, что `x == x`. Из-за этого предположения сначала сравниваются идентификаторы (так как это быстрее),
  когда сравниваются два элемента, а значения сравниваются только при несовпадении идентификаторов. Следующий фрагмент сделает вещи более ясными:

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

  Поскольку идентификаторы `x` и `y` разные, рассматриваются значения, которые также различаются; следовательно, на этот раз сравнение возвращает `False`.

- Интересное чтение: [Рефлексивность и другие основы цивилизации](https://bertrandmeyer.com/2010/02/06/reflexivity-and-other-pillars-of-civilization/)

---

### ▶ Мутируем немутируемое!

<!-- Example ID: 15a9e782-1695-43ea-817a-a9208f6bb33d --->

Это может показаться тривиальным, если вы знаете, как работают ссылки в Python. Но если вы не знаете, то это может быть немного удивительно.

```py
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
```

**Результат:**
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

Но я думал, что кортежи неизменяемы... Что происходит?

#### 💡 Объяснение:

* Цитата из https://docs.python.org/3/reference/datamodel.html

    > Неизменяемые последовательности
      Объект неизменяемого типа последовательности не может измениться после создания. (Если объект содержит ссылки на другие объекты, эти другие объекты могут быть изменяемыми и могут быть изменены; однако набор объектов, на которые непосредственно ссылается неизменяемый объект, не может изменяться.)

* Оператор `+=` изменяет список на месте. Присваивание элемента не работает, но когда возникает исключение, элемент уже был изменен на месте.
* Также есть объяснение в официальном [Python FAQ](https://docs.python.org/3/faq/programming.html#why-does-a-tuple-i-item-raise-an-exception-when-the-addition-works).

---

### ▶ Исчезновение переменной из внешней области видимости
<!-- Example ID: 7f1e71b6-cb3e-44fb-aa47-87ef1b7decc8 --->

```py
e = 7
try:
    raise Exception()
except Exception as e:
    pass
```

**Результат (Python 2.x):**
```py
>>> print(e)
# prints nothing
```

**Результат (Python 3.x):**
```py
>>> print(e)
NameError: name 'e' is not defined
```

#### 💡 Объяснение:

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

     **Результат:**
     ```py
     >>> f(x)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>> f(y)
     UnboundLocalError: local variable 'x' referenced before assignment
     >>> x
     5
     >>> y
     [5, 4, 3]
     ```

* In Python 2.x, the variable name `e` gets assigned to `Exception()` instance, so when you try to print, it prints nothing.

    **Результат (Python 2.x):**
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

**Результат:**
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

#### 💡 Объяснение:

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

  **Результат:**
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

### ▶ Посмотрим, сможете ли вы угадать что здесь?
<!-- Example ID: 81aa9fbe-bd63-4283-b56d-6fdd14c9105e --->
```py
a, b = a[b] = {}, 5
```

**Результат:**
```py
>>> a
{5: ({...}, 5)}
```

#### 💡 Объяснение:

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

### ▶ Exceeds the limit for integer string conversion
```py
>>> # Python 3.10.6
>>> int("2" * 5432)
>>> # Python 3.10.8
>>> int("2" * 5432)
```
**Вывод:**
```py
>>> # Python 3.10.6
222222222222222222222222222222222222222222222222222222222222222...
>>> # Python 3.10.8 and Python 3.11
Traceback (most recent call last):
   ...
ValueError: Exceeds the limit (4300) for integer string conversion:
   value has 5432 digits; use sys.set_int_max_str_digits()
   to increase the limit.
```
#### 💡 Объяснение:
Этот вызов `int()` прекрасно работает в Python 3.10.6 и вызывает ошибку ValueError в Python 3.10.8, 3.11. Обратите внимание, что Python все еще может работать с большими целыми числами. Ошибка возникает только при преобразовании между целыми числами и строками.
К счастью, вы можете увеличить предел допустимого количества цифр, если ожидаете, что операция превысит его. Для этого можно воспользоваться одним из следующих способов:
- -X int_max_str_digits command-line flag
- set_int_max_str_digits() function from the sys module
- PYTHONINTMAXSTRDIGITS environment variable

[Смотри документацию](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits) для получения более подробной информации об изменении лимита по умолчанию, если вы ожидаете, что ваш код превысит это значение.

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

**Результат (Python 2.7- Python 3.5):**

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

#### 💡 Объяснение:

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

**Результат:**
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

#### 💡 Объяснение:
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

**Результат:**
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

#### 💡 Объяснение:
* When you make an assignment to a variable in scope, it becomes local to that scope. So `a` becomes local to the scope of `another_func`, but it has not been initialized previously in the same scope, which throws an error.
* To modify the outer scope variable `a` in `another_func`, we have to use the `global` keyword.
  ```py
  def another_func()
      global a
      a += 1
      return a
  ```

  **Результат:**
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

  **Результат:**
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

**Результат:**
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

#### 💡 Объяснение:

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

#### 💡 Объяснение:

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

**Результат:**
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

**Результат:**
```py
6 : for x inside loop
6 : x in global
```

3\.

**Результат (Python 2.x):**
```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
4
```

**Результат (Python 3.x):**
```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
1
```

#### 💡 Объяснение:

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

**Результат:**
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

#### 💡 Объяснение:

- The default mutable arguments of functions in Python aren't really initialized every time you call the function. Instead, the recently assigned value to them is used as the default value. When we explicitly passed `[]` to `some_func` as the argument, the default value of the `default_arg` variable was not used, so the function returned as expected.

    ```py
    def some_func(default_arg=[]):
        default_arg.append("some_string")
        return default_arg
    ```

    **Результат:**
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

**Результат (Python 2.x):**
```py
Caught!

ValueError: list.remove(x): x not in list
```

**Результат (Python 3.x):**
```py
  File "<input>", line 3
    except IndexError, ValueError:
                     ^
SyntaxError: invalid syntax
```

#### 💡 Объяснение

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
  **Результат (Python 2.x):**
  ```
  Caught again!
  list.remove(x): x not in list
  ```
  **Результат (Python 3.x):**
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
  **Результат:**
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

**Результат:**
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

**Результат:**
```py
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4, 5, 6, 7, 8]
```

#### 💡 Объяснение:

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

**Результат:**
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

**Результат (Python 2.x):**
```py
>>> SomeClass.y[0]
17
```

**Результат (Python 3.x):**
```py
>>> SomeClass.y[0]
5
```

#### 💡 Объяснение
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

#### 💡 Объяснение:

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

**Результат:**

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

**Результат:**

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

**Результат**

```py
>>> len(ten_words_list)
9
```

4\. Not asserting strongly enough

```py
a = "python"
b = "javascript"
```

**Результат:**

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

**Результат:**

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

**Результат:**

```py
>>> some_recursive_func([5, 0])
[0, 0]
>>> similar_recursive_func(5)
4
```

#### 💡 Объяснение:

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

* Last one should be fairly obvious, mutable object (like `list`) can be altered in the function, and the reassignment of an immutable (`a -= 1`) is not an alteration of the value.

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

#### 💡 Объяснение:

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

**Результат**

```py
>>> from module import *
>>> some_weird_name_func_()
"works!"
>>> _another_weird_name_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_another_weird_name_func' is not defined
```

#### 💡 Объяснение:

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
    **Результат**

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

#### 💡 Объяснение:

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

**Результат (< 3.5):**

```py
('Time at noon is', datetime.time(12, 0))
```
The midnight time is not printed.

#### 💡 Объяснение:

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

**Результат:**
Sshh... It's a super-secret.

#### 💡 Объяснение:
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

**Результат (Python 2.3):**
```py
I am trapped, please rescue!
I am trapped, please rescue!
Freedom!
```

#### 💡 Объяснение:
- A working version of `goto` in Python was [announced](https://mail.python.org/pipermail/python-announce-list/2004-April/002982.html) as an April Fool's joke on 1st April 2004.
- Current versions of Python do not have this module.
- Although it works, but please don't use it. Here's the [reason](https://docs.python.org/3/faq/design.html#why-is-there-no-goto) to why `goto` is not present in Python.

---

### ▶ Держитесь!
<!-- Example ID: 5c0c75f2-ddd9-4da3-ba49-c4be7ec39acf --->
Если вы относитесь к тем людям, которым не нравится использование пробелов в Python для обозначения диапазонов, вы можете использовать C-стиль {} импортировав это,

```py
from __future__ import braces
```

**Результат:**
```py
  File "some_file.py", line 1
    from __future__ import braces
SyntaxError: not a chance
```

Скобочки? Ни за что! Если это разочаровывало вас, используйте PHP :). Хорошо, еще одна удивительная вещь, можете ли вы найти ошибку
`SyntaxError` которая вызвана в модуле `__future__` [code](https://github.com/python/cpython/blob/master/Lib/__future__.py)?

#### 💡 Объяснение:
+ The `__future__` module is normally used to provide features from future versions of Python. The "future" in this specific context is however, ironic.
+ This is an easter egg concerned with the community's feelings on this issue.
+ The code is actually present [here](https://github.com/python/cpython/blob/025eb98dc0c1dc27404df6c544fc2944e0fa9f3a/Python/future.c#L49) in `future.c` file.
+ When the CPython compiler encounters a [future statement](https://docs.python.org/3.3/reference/simple_stmts.html#future-statements), it first runs the appropriate code in `future.c` before treating it as a normal import statement.

---

### ▶ Давайте познакомимся с дружелюбным Дядей Барри
<!-- Example ID: 6427fae6-e959-462d-85da-ce4c94ce41be --->

**Результат (Python 3.x)**
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

Вот так просто.

#### 💡 Объяснение:
- Это относится к [PEP-401](https://www.python.org/dev/peps/pep-0401/) released on April 1, 2009 (now you know, what it means).
- Цитируя из PEP-401
  
  > Recognized that the != inequality operator in Python 3.0 was a horrible, finger-pain inducing mistake, the FLUFL reinstates the <> diamond operator as the sole spelling.
  Некоторые считают, что оператор неравенства != в Python 3.0 отвратительный (хотя в других языках это вполне привычная и узнаваемая конструкция) и вызывал боль, FLUFL разрешает единственный вариант оператора неравенства в виде ромба <>.
- У Дяди Барри было еще много чего рассказать в PEP; вы можете прочитать их [здесь](https://www.python.org/dev/peps/pep-0401/).
- Это работает хорошо в интерактивной среде, но при запуске через файл python вызывает `SyntaxError` (смотри этот [ишью](https://github.com/satwikkansal/wtfpython/issues/94)). Однако вы можете обернуть оператор внутри `eval` или `compile`, чтобы заставить его работать (но зачем?)
    ```py
    from __future__ import barry_as_FLUFL
    print(eval('"Ruby" <> "Python"'))
    ```

---

### ▶ Даже Python понимает, что любовь - это сложно.
<!-- Example ID: b93cad9e-d341-45d1-999c-fcdce65bed25 --->
```py
import this
```

Подождите, что **это** (this) такое? Это любовь! :heart:

**Результат:**
```
Дзен Python, от Тима Петерса

Красивое лучше, чем уродливое.
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибки никогда не должны замалчиваться.
Если они не замалчиваются явно.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один и, желательно, только один очевидный способ сделать это.
Хотя он поначалу может быть и не очевиден, если вы не голландец [^1].
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить — идея плоха.
Если реализацию легко объяснить — идея, возможно, хороша.
Пространства имён — отличная штука! Будем делать их больше!
```

Это Дзен Python!

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

#### 💡 Объяснение:

* `this` module in Python is an easter egg for The Zen Of Python ([PEP 20](https://www.python.org/dev/peps/pep-0020)).
* And if you think that's already interesting enough, check out the implementation of [this.py](https://hg.python.org/cpython/file/c3896275c0f6/Lib/this.py). Interestingly, **the code for the Zen violates itself** (and that's probably the only place where this happens).
* Regarding the statement `love is not True or False; love is love`, ironic but it's self-explanatory (if not, please see the examples related to `is` and `is not` operators).

* Модуль `this` в Python - это пасхальное яйцо для The Zen Of Python ([PEP 20](https://www.python.org/dev/peps/pep-0020)).
* И если вы думаете, что это уже достаточно интересно, посмотрите реализацию [this.py](https://hg.python.org/cpython/file/c3896275c0f6/Lib/this.py). Интересно, что **код для дзена нарушает сам себя** (и это, вероятно, единственное место, где это происходит, но это не точно).
* Что касается утверждения `любовь не является истиной или ложью; любовь - это любовь`, иронично, но это самоочевидно (если нет, пожалуйста, посмотрите примеры, связанные с операторами `is` и `is not`).

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

**Результат:**
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

**Результат:**
```py
Try block executed successfully...
```

#### 💡 Объяснение:
- The `else` clause after a loop is executed only when there's no explicit `break` after all the iterations. You can think of it as a "nobreak" clause.
- `else` clause after a try block is also called "completion clause" as reaching the `else` clause in a `try` statement means that the try block actually completed successfully.

---
### ▶ Ellipsis *
<!-- Example ID: 969b7100-ab3d-4a7d-ad7d-a6be16181b2b --->
```py
def some_func():
    Ellipsis
```

**Результат**
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

#### 💡 Объяснение
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

**Результат (Python 3.x):**
```py
>>> infinity = float('infinity')
>>> hash(infinity)
314159
>>> hash(float('-inf'))
-314159
```

#### 💡 Объяснение:
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

**Результат:**
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

**Результат:**
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

**Результат:**
```py
>>> A().__variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__variable'

>>> A().some_func()
'Some value'
```


#### 💡 Объяснение:

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
**Результат:**
```py
>>> value = 11
>>> valuе = 32
>>> value
11
```

Wut?

**Note:** The easiest way to reproduce this is to simply copy the statements from the above snippet and paste them into your file/shell.

#### 💡 Объяснение

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

**Результат:**
```py
>>> energy_send(123.456)
>>> energy_receive()
123.456
```

Where's the Nobel Prize?

#### 💡 Объяснение:

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

**Результат (Python 2.x):**

```py
>>> square(10)
10
```

Shouldn't that be 100?

**Note:** If you're not able to reproduce this, try running the file [mixed_tabs_and_spaces.py](/mixed_tabs_and_spaces.py) via the shell.

#### 💡 Объяснение

* **Don't mix tabs and spaces!** The character just preceding return is a "tab",  and the code is indented by multiple of "4 spaces" elsewhere in the example.
* This is how Python handles tabs:
  
  > First, tabs are replaced (from left to right) by one to eight spaces such that the total number of characters up to and including the replacement is a multiple of eight <...>
* So the "tab" at the last line of `square` function is replaced with eight spaces, and it gets into the loop.
* Python 3 is kind enough to throw an error for such cases automatically.

    **Результат (Python 3.x):**
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

#### 💡 Объяснение:
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

**Результат:**

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

#### 💡 Объяснение
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

**Результат:**
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

#### 💡 Объяснение:
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

**Результат:** (Python 3.8, other Python 3 versions may vary a little)
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

#### 💡 Объяснение:
+ CPython is able to reuse the same "keys" object in multiple dictionaries. This was added in [PEP 412](https://www.python.org/dev/peps/pep-0412/) with the motivation to reduce memory usage, specifically in dictionaries of instances - where keys (instance attributes) tend to be common to all instances.
+ This optimization is entirely seamless for instance dictionaries, but it is disabled if certain assumptions are broken.
+ Key-sharing dictionaries do not support deletion; if an instance attribute is deleted, the dictionary is "unshared", and key-sharing is disabled for all future instances of the same class.
+ Additionaly, if the dictionary keys have been resized (because new keys are inserted), they are kept shared *only* if they are used by a exactly single dictionary (this allows adding many attributes in the `__init__` of the very first created instance, without causing an "unshare"). If multiple instances exist when a resize happens, key-sharing is disabled for all future instances of the same class: CPython can't tell if your instances are using the same set of attributes anymore, and decides to bail out on attempting to share their keys.
+ A small tip, if you aim to lower your program's memory footprint: don't delete instance attributes, and make sure to initialize all attributes in your `__init__`!


### ▶ Minor Ones *
<!-- Example ID: f885cb82-f1e4-4daa-9ff3-972b14cb1324 --->
* `join()` is a string operation instead of list operation. (sort of counter-intuitive at first usage)

  **💡 Объяснение:** If `join()` is a method on a string, then it can operate on any iterable (list, tuple, iterators). If it were a method on a list, it'd have to be implemented separately by every type. Also, it doesn't make much sense to put a string-specific method on a generic `list` object API.
  
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

  **💡 Объяснение:**
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
  **💡 Объяснение:** This prank comes from [Raymond Hettinger's tweet](https://twitter.com/raymondh/status/1131103570856632321?lang=en). The space invader operator is actually just a malformatted `a -= (-1)`. Which is equivalent to `a = a - (- 1)`. Similar for the `a += (+ 1)` case.
  
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

     **💡 Объяснение:** If you replace `False` and `True` by 0 and 1 and do the maths, the truth table is equivalent to a converse implication operator. ([Source](https://github.com/cosmologicon/pywat/blob/master/explanation.md#the-undocumented-converse-implication-operator))
     
* Since we are talking operators, there's also `@` operator for matrix multiplication (don't worry, this time it's for real).

     ```py
     >>> import numpy as np
     >>> np.array([2, 2, 2]) @ np.array([7, 8, 8])
     46
     ```

     **💡 Объяснение:** The `@` operator was added in Python 3.5 keeping the scientific community in mind. Any object can overload `__matmul__` magic method to define behavior for this operator.

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
