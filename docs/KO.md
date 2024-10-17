---
hide:
  - toc
---

> > ## 번역
>
> 번역에 참여하고 싶으시면 [Github Discussion](https://github.com/buttercrab/wtfpython-ko/discussions)을 방문하세요!

<p align="center"><img src="../images/logo.png#gh-light-mode-only" alt=""><img src="../images/logo-dark.png#gh-dark-mode-only" alt=""></p>
<h1 align="center">What the f*ck Python! 😱</h1>
<p align="center">놀라운 예제들을 통해서 파이썬 탐험하고 이해하기</p>

<p align="center"><a href="https://github.com/satwikkansal/wtfpython">영어 English(원문)</a> | <a href="https://github.com/leisurelicht/wtfpython-cn">중국어 中文</a></p>

다른 읽는 방법: [인터랙티브](https://colab.research.google.com/github/satwikkansal/wtfpython/blob/master/irrelevant/wtf.ipynb) | [CLI](https://pypi.python.org/pypi/wtfpython)

설계가 잘된 고급 인터프리터 언어인 파이썬에는 프로그래머를 위한 편의 기능이 많습니다. 하지만 간혹 어떤 파이썬 코드들은 실행 결과가 이상해보일 때도 있습니다.

이 문서는 직관적이지 않거나 덜 알려진 기능을 사용하는 예제들에 대해 그 이면의 동작을 정확하게 설명합니다.

아래의 예제들이 WTF 까지는 아닐 수도 있지만, 파이썬의 잘 몰랐던 부분을 보여드릴 수는 있을 것입니다. 이런 식으로 공부하는 것이 프로그래밍 언어의 내부를 알게되는데 효과적이라고 생각합니다. 여러분도 동의하게 되실거라 믿습니다!

만약 파이썬의 고인물이라면 첫눈에 예제의 의미를 파악해보세요. 아마 이미 경험한 적이 있는 코드일 수도 있겠습니다. 그렇다면 옛 추억을 떠으로게 해드린 셈이 되겠네요! :sweat_smile:

추신: 예전에 읽었는데 다시 오신 분이라면 [여기서](https://github.com/satwikkansal/wtfpython/releases/) 바뀐 부분을 확인할 수 있습니다.

추신 2: [옮긴이의 말](https://github.com/buttercrab/wtfpython-ko/blob/3.0/translator.md)을 읽는 것을 추천합니다.

그럼, 시작합니다!

# 목차

<!-- Generated using "markdown-toc -i README.md --maxdepth 3"-->

<!-- toc -->

- [예제의 구성](#예제의-구성)
  - [▶ 빛나는 제목](#-빛나는-제목)
- [사용방법](#사용방법)
- [👀 예제](#-예제)
  - ["머리가 아플수도 있어요!" 단원](#머리가-아플수도-있어요-단원)
    - [▶ 먼저 처음 것들부터 \*](#-먼저-처음-것들부터-)
    - [▶ 문자열은 가끔 헷갈려요](#-문자열은-가끔-헷갈려요)
    - [▶ 연결된 연산들을 조심하세요](#-연결된-연산들을-조심하세요)
    - [▶ `is` 연산자를 안 쓰는 방법](#-is-연산자를-안-쓰는-방법)
    - [▶ 해시 브라우니](#-해시-브라우니)
    - [▶ 깊이 들어가면 우리는 다 똑같아.](#-깊이-들어가면-우리는-다-똑같아)
    - [▶ 질서 속의 무질서 \*](#-질서-속의-무질서-)
    - [▶ 계속 시도해 보세요... \*](#-계속-시도해-보세요-)
    - [▶ 무엇을 위해서(for)?](#-무엇을-위해서for)
    - [▶ 실행되는 시간의 차이](#-실행되는-시간의-차이)
    - [▶ `is not ...` 은 `is (not ...)`이 아니다](#-is-not--은-is-not-이-아니다)
    - [▶ X가 첫 번째 시도에서 승리하는 틱택토!](#-x가-첫-번째-시도에서-승리하는-틱택토)
    - [▶ 달라붙는 출력 함수](#-달라붙는-출력-함수)
    - [▶ 닭이 먼저일까, 달걀이 먼저일까 \*](#-닭이-먼저일까-달걀이-먼저일까-)
    - [▶ 서브 클래스의 관계](#-서브-클래스의-관계)
    - [▶ 메소드의 같음과 동일함](#-메소드의-같음과-동일함)
    - [▶ 참 거짓의 반복 \*](#-참-거짓의-반복-)
    - [▶ 놀라운 콤마](#-놀라운-콤마)
    - [▶ 문자열과 백슬래시](#-문자열과-백슬래시)
    - [▶ 매듭이 아니야!](#-매듭이-아니야)
    - [▶ 반쪽 3중 따옴표 문자열](#-반쪽-3중-따옴표-문자열)
    - [▶ 불린의 문제점이 뭐야?](#-불린의-문제점이-뭐야-)
    - [▶ 클래스 속성과 인스턴스 속성](#-클래스-속성과-인스턴스-속성)
    - [▶ yielding None](#-yielding-none)
    - [▶ Yielding from... return! \*](#-yielding-from-return-)
    - [▶ Nan-재귀성 \*](#-nan-재귀성-)
    - [▶ 불변을 변형하기!](#-불변을-변형하기)
    - [▶ 외부 범위에서 사라지는 변수](#-외부-범위에서-사라지는-변수)
    - [▶ 미스테리한 키 타입 형 변환](#-미스테리한-키-타입-형-변환)
    - [▶ 여러분이 맞출 수 있는지 한번 볼까요?](#-여러분이-맞출-수-있는지-한번-볼까요)
  - ["미끄러운 비탈길" 단원](#미끄러운-비탈길-단원)
    - [▶ 딕셔너리가 반복 중일 때 수정하기](#-딕셔너리가-반복-중일-때-수정하기)
    - [▶ 완강한 `del` 연산자](#-완강한-del-연산자)
    - [▶ 범위를 벗어난 변수](#-범위를-벗어난-변수)
    - [▶ 반복하는 동안 리스트의 아이템을 삭제하기](#-반복하는-동안-리스트의-아이템을-삭제하기)
    - [▶ 반복자의 손실되는 zip \*](#-반복자의-손실되는-zip-)
    - [▶ 루프 변수가 유출되고 있습니다!](#-루프-변수가-유출되고-있습니다)
    - [▶ 기본 가변인수를 조심하세요!](#-기본-가변인수를-조심하세요)
    - [▶ 여러 예외들을 잡기](#-여러-예외들을-잡기)
    - [▶ 같은 피연산자, 다른 이야기!](#-같은-피연산자-다른-이야기)
    - [▶ 이름 확인은 클래스 범위를 무시합니다](#-이름-확인은-클래스-범위를-무시합니다)
    - [▶ 모래밭에서 바늘찾기 \*](#-모래밭에서-바늘찾기-)
    - [▶ 나눠봅시다 \*](#-나눠봅시다-)
    - [▶ 제멋대로 가져오기 \*](#-제멋대로-가져오기-)
    - [▶ 다 정렬되었나요? \*](#-다-정렬되었나요-)
    - [▶ 자정은 존재하지 않나요?](#-자정은-존재하지-않나요)
  - ["숨겨진 보물들!" 단원](#숨겨진-보물들-단원)
    - [▶ 파이썬, 날 날게해줄 수 있니?](#-파이썬-날-날게해줄-수-있니)
    - [▶ `goto`, 하지만 왜?](#-goto-하지만-왜)
    - [▶ 마음 단단히 먹으세요!](#-마음-단단히-먹으세요)
    - [▶ 평생 친근한 아저씨 같은 언어를 만나봅시다](#-평생-친근한-아저씨-같은-언어를-만나봅시다)
    - [▶ 파이썬 조차 사랑이 복잡하다는 것을 이해합니다](#-파이썬-조차-사랑이-복잡하다는-것을-이해합니다)
    - [▶ 네, 존재합니다!](#-네-존재합니다)
    - [▶ Ellipsis \*](#-ellipsis-)
    - [▶ Inpinity](#-inpinity)
    - [▶ 망쳐봅시다](#-망쳐봅시다)
  - ["겉모습은 기만적입니다!" 단원](#겉모습은-기만적입니다-단원)
    - [▶ 줄 건너뛰기?](#-줄-건너뛰기)
    - [▶ 순간이동](#-순간이동)
    - [▶ 음, 뭔가 수상한데...](#-음-뭔가-수상한데)
  - ["기타 등등" 단원](#기타-등등-단원)
    - [▶ `+=` 가 더 빨라요](#--가-더-빨라요)
    - [▶ 거대한 문자열을 만들어봐요!](#-거대한-문자열을-만들어봐요)
    - [▶ dict 검색 속도 느려지게 하기 \*](#-dict-검색-속도-느려지게-하기-)
    - [▶ `dict` 인스턴스 부풀리기 \*](#-dict-인스턴스-부풀리기-)
    - [▶ 사소한 것들 \*](#-사소한-것들-)
- [기여하기](#기여하기)
- [감사의 말](#감사의-말)
- [🎓 License](#-license)
  - [친구들을 놀라게 해보세요!](#친구들을-놀라게-해보세요)
  - [Need a pdf version?](#Need-a-pdf-version-)

<!-- tocstop -->

# 예제의 구성

모든 예제는 아래와 같은 구조로 이루어져 있습니다.

> ### ▶ 빛나는 제목
>
> ```py
> # 예제 세팅
> # 마법 같은 일을 기대하세요...
> ```
>
> **출력 결과 (유효한 파이썬 버전들):**
>
> ```py
> >>> 입력
> 놀라운 결과
> ```
>
> 놀라운 결과에 대한 한 줄 설명이 있을 수도 있습니다.
>
> #### 💡 설명:
>
> - 무엇이 일어나고 있는지와 왜 일어나는지에 대한 간략한 설명
>
> ```py
> # 설명을 도울 예제
> ```
>
> **출력 결과 (유효한 파이썬 버전들):**
>
> ```py
> >>> 입력 # 놀라운 결과의 이해를 돕기 위한 예제
> # 이해 가능한 결과
> ```

**참고:** 여기에 있는 모든 예제는 파이썬 3.5.2 인터렉티브 인터프리터에서 테스트 되었고 추가적으로 명시되어 있지 않은 이상 모든 버전에서 작동할 것입니다.

# 사용방법

예제들을 순서대로 읽어내려가는 것을 권장하고 예제마다:

- 예제의 코드를 잘 읽어보세요. 만약 파이썬 고인물이라면 대부분 결과가 어떻게 될지 미리 알고 있을 것입니다.
- 결과를 읽고,
  - 예상한 결과와 실제 결과가 맞는지 확인해 보세요.
  - 결과와 그 작동원리에 대한 정확한 원리를 알고 있나요?
  * 만약 아니라면 (상관없어요), 큰 숨을 한 번 들이마시고, 설명을 읽어보세요 (그래도 이해하지 못했다면, [여기](https://github.com/satwikkansal/wtfpython/issues/new)에 이슈를 작성해주세요).
  * 알고 있다면, 자신을 한번 토닥여주고 다음 예제로 넘어가세요.

추신: [pypi 패키지](https://pypi.python.org/pypi/wtfpython)를 사용하면 command line에서도 이 문서를 읽을 수 있습니다.

```sh
$ pip install wtfpython -U
$ wtfpython
```

---

# 👀 예제

## "머리가 아플수도 있어요!" 단원

### ▶ 먼저 처음 것들부터 \*

<!-- Example ID: d3d73936-3cf1-4632-b5ab-817981338863 -->
<!-- read-only -->

어떤 이유에서인지, 파이썬 3.8의 Walrus 연산자 (`:=`) 가 꽤 알려지게 되었습니다. 확인해봅시다.

1\.

```py
# 파이썬 3.8+

>>> a = "wtf_walrus"
'wtf_walrus'
>>> a
'wtf_walrus'

>>> a := "wtf_walrus"
File "<stdin>", line 1
    a := "wtf_walrus"
      ^
SyntaxError: invalid syntax

>>> (a := "wtf_walrus") # 이건 잘 작동하네요
>>> a
'wtf_walrus'
```

2 \.

```py
# 파이썬 3.8+

>>> a = 6, 9
>>> a
(6, 9)

>>> (a := 6, 9)
>>> a
6

>>> a, b = 6, 9 # 전형적인 언패킹
>>> a, b
(6, 9)
>>> (a, b = 16, 19) # 이런
  File "<stdin>", line 1
    (a, b = 6, 9)
          ^
SyntaxError: invalid syntax

>>> (a, b := 16, 19) # 이것은 이상한 3-튜플을 출력합니다.
(6, 16, 19)

>>> a # a가 아직도 안 바뀌었네요?
6

>>> b
16
```

#### 💡 설명

**간단한 walrus 연산자 설명**

walrus 연산자 (`:=`) 는 파이썬 3.8에서 소개되었으며, 변수에 할당하면서 연산을 하고 싶을 때 유용하게 쓰일 수 있습니다.

```py
def some_func():
		# 많은 계산을 하는 함수라고 가정합시다.
        # time.sleep(1000)
        return 5

# 그래서
if some_func():
        print(some_func()) # 같은 계산이 두 번 이루어지므로 안 좋은 방법입니다.

# 또는
a = some_func()
if a:
    print(a)

# 대신에 이렇게 간단하게 쓸 수 있습니다.
if a := some_func():
        print(a)
```

**출력 결과 (> 3.8):**

```py
5
5
5
```

이 연산자는 한 줄의 코드를 아끼고 `some_func`를 두 번 호출하는 것을 방지할 수 있습니다.

- (walrus 연산자를 사용한) 괄호로 묶이지 않은 "할당문(assignment expression)"은 컴파일러의 상위 단계에서 제한되므로 첫 번째 줄 `a := "wtf_walrus"`에서 `SyntaxError`가 발생합니다. 괄호로 묶게 되면 예상했던 대로 작동하고 `a`에 값을 할당하게 됩니다.

- 정상적으로, `=` 연산자를 포함한 표현식에서는 괄호로 둘러싸는 것이 허용되지 않기 때문에, `(a, b = 6, 9)`에서 syntax error가 발생합니다.

- walrus 연산자는 `Name`이 유효한 식별자(identifier)이고 `expr`이 유효한 표현식 일 때, `Name := expr`로 사용됩니다. 따라서 패킹과 언패킹은 지원되지 않습니다. 그러므로,

  - `(a := 6, 9)`는 `((a := 6), 9)`와 같고 결국 `(a, 9)` (`a`의 값이 6 일때) 와 같게 됩니다.

    ```py
    >>> (a := 6, 9) == ((a := 6), 9)
    True
    >>> x = (a := 696, 9)
    >>> x
    (696, 9)
    >>> x[0] is a # 둘 다 메모리의 같은 위치를 가리키고 있습니다.
    True
    ```

  - 비슷하게, `(a, b := 16, 19)`는 `(a, (b := 16), 19)`와 같게 되고 이는 단순한 3-튜플과 같습니다.

---

### ▶ 문자열은 가끔 헷갈려요

<!-- Example ID: 30f1d3fc-e267-4b30-84ef-4d9e7091ac1a --->

1\.

```py
>>> a = "some_string"
>>> id(a)
140420665652016
>>> id("some" + "_" + "string") # 두 id가 같네요
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
>>> a is b # 3.7.x 버전을 제외하고 모든 버전에서 이렇게 작동합니다.
True

>>> a = "wtf!"; b = "wtf!"
>>> a is b # 어디서 실행시키는지에 따라 True 혹은 False가 출력될 것입니다. (파이썬 쉘 / ipython / 파이썬 스크립트)
False
```

```py
# 이번에는 some_file.py 파일에서 실행시켜봅시다.
a = "wtf!"
b = "wtf!"
print(a is b)

# 모듈을 실행시키면 True를 출력하네요.
```

4\.

**출력 결과 (< 3.7 )**

```py
>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
```

말이 되는 거 같죠?

#### 💡 설명:

- 첫 번째와 두 번째 코드에서의 결과는 새로운 객체를 항상 만드는 것보다 이미 존재하고 바뀌지 않는 객체를 사용하려고 하는 CPython 최적화 때문에 그렇습니다. (문자열 interning이라고 부릅니다)
- interning이 되고 난 다음, 많은 변수는 같은 메모리에 있는 문자열을 가리키고 있을 겁니다. (메모리를 줄이게 됩니다)
- 위의 코드들을 보면, 문자열은 알아서 interning이 됩니다. 구현 방식에 따라서 알아서 interning이 될 것인지 결정됩니다. 알아서 interning이 될 것인지 예측해볼 몇 가지 규칙이 있습니다:
  - 길이가 0과 1인 모든 문자열은 interning이 됩니다.
  - 문자열은 컴파일 시간에 interning이 됩니다. (`'wtf'`은 interning이 되지만 `''.join(['w', 't', 'f'])`은 interning이 되지 않습니다)
  - 아스키 문자, 숫자, 언더바 이외의 문자로 이루어져 있으면 interning이 되지 않습니다. 그래서 `'wtf!'`이 `!` 때문에 interning이 되지 않았습니다. CPython에서의 구현은 [여기](https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19)서 확인할 수 있습니다.
    ![image](../images/string-intern/string_intern.png)
- `a`와 `b`가 같은 줄에서 `"wtf!"`의 값으로 할당된다면, 파이썬 인터프리터가 새로운 객체를 만들고 두 번째 변수도 가리키게 만듭니다. 그런데 만약 이 작업을 다른 줄에서 한다면, 파이썬 인터프리터는 이미 `"wtf!"`가 객체로 존재한다는 사실을 모릅니다 (왜냐하면 `"wtf!"`는 interning이 되지 않았기 때문입니다). interning은 컴파일 시간에 작동하는 최적화입니다. 이 최적화는 CPython 3.7.x 버전들에는 적용되지 않았습니다. (더 많은 정보는 이 [이슈](https://github.com/satwikkansal/wtfpython/issues/100)를 확인하세요).
- IPython과 같은 인터랙티브 환경에서는 하나의 컴파일 유닛(unit)이 하나의 표현식이고 모듈일 때는 모듈 전체일 때도 있습니다. `a, b = "wtf!", "wtf!"`은 하나의 표현식이지만 `a = "wtf!"; b = "wtf!"`은 한 줄에 있는 두 개의 표현식입니다. 그러면 위 예제들의 결과를 설명할 수 있습니다.
- 네 번째 출력 결과의 갑작스러운 변화는 [핍홀 최적화](https://en.wikipedia.org/wiki/Peephole_optimization)에 의한 것입니다. 즉 `'a'*20`은 실행 시간에 클록수를 줄이기 위해 컴파일 시간에 `aaaaaaaaaaaaaaaaaaaa`로바뀝니다. 핍홀 최적화는 문자열의 길이가 20 이하일 때만 일어납니다 (`'a'*10**10`의 결과로 `.pyc`파일의 크기를 생각해보세요). [여기](https://github.com/python/cpython/blob/3.6/Python/peephole.c#L288)에 그에 대한 구현이 있습니다.
- 참고: 파이썬 3.7에서는 새로운 AST 최적화 새로운 로직으로 핍홀 최적화가 빠졌습니다. 그래서 세 번째 코드가 파이썬 3.7에서는 작동하지 않았습니다. [여기](https://bugs.python.org/issue11549)에서 더 자세히 알아보세요.

---

### ▶ 연결된 연산들을 조심하세요

<!-- Example ID: 07974979-9c86-4720-80bd-467aa19470d9 --->

```py
>>> (False == False) in [False] # 말이 되네요
False
>>> False == (False in [False]) # 이것도 말이 됩니다
False
>>> False == False in [False] # 이건 뭐죠?
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

#### 💡 설명:

https://docs.python.org/2/reference/expressions.html#not-in 에 따라서

> 형식적으로, a, b, c, ..., y, z가 표현식이고 op1, op2, ..., opN이 비교 연산자라면, 각 식이 한번에 평가된다는 점을 제외하고 a op1 b op2 c ... y opN z는 a op1 b and b op2 c and ... y opN z에 해당합니다.

위의 예시와 같은 결과들은 이상해 보일지도 모르지만, `a == b == c`나 `0 <= x <= 100`와 같은 표현들은 환상적입니다.

- `False is False is False`는 `(False is False) and (False is False)`와 같습니다.
- `True is False == False`는 `True is False and False == False`와 같으며 구문의 첫 부분 (`True is False`)가 `False`로 평가되기 때문에 전체 표현식의 결과는 `False`가 됩니다.
- `1 > 0 < 1`은 `1 > 0 and 0 < 1`과 같아 `True`가 계산됩니다.
- 표현식 `(1 > 0) < 1`은 `True < 1`과 같으며
  ```py
  >>> int(True)
  1
  >>> True + 1 #예제와는 관련이 없지만, 재미를 위해서입니다.
  2
  ```
  즉, `1 < 1`의 결과는 `False`입니다.

---

### ▶ `is` 연산자를 안 쓰는 방법

<!-- Example ID: 230fa2ac-ab36-4ad1-b675-5f5a1c1a6217 --->

아래 예제는 인터넷에서 매우 유명한 예제로 퍼져있습니다.

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
**출력 결과**

```py
>>> a, b = 257, 257
>>> a is b
True
```

**출력 결과 (파이썬 3.7.x)**

```py
>>> a, b = 257, 257
>> a is b
False
```

#### 💡 설명:

**`is`와 `==`의 차이점**

- `is` 연산자는 연산자 양쪽이 같은 객체를 참조하고 있는지를 확인합니다. (즉, 둘이 진짜로 같은지를 확인합니다).
- `==` 연산자는 양쪽의 값을 비교하여 이 둘이 같은지를 확인합니다.
- 그래서 `is`는 참조의 동등을, `==`는 값의 동등을 확인합니다. 다음 예제로 정리해보면,
  ```py
  >>> class A: pass
  >>> A() is A() # 이 둘은 메모리상에 다른 곳에 있는 두 빈 객체입니다.
  False
  ```

**`256`은 존재하는 객체이지만 `257`은 아닙니다**

파이썬을 시작하게 되면, `-5`부터 `256`까지의 수들은 할당됩니다. 이 수들은 많이 사용되기 때문에 미리 준비하는 것입니다.

https://docs.python.org/3/c-api/long.html 에서 인용한 글입니다.

> 현 구현은 -5부터 256까지의 정수들을 담는 배열을 만듭니다. 만약 이 범위 안에 있는 정수를 만들게 되면 이미 존재하는 객체의 참조를 반환합니다. 그래서 1의 값을 바꾸는 것이 가능할 것입니다. 아마도 이 경우는 파이썬의 행동은 정의되지 않을 것입니다. :-)

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

여기서 인터프리터는 `y = 257`을 실행할 때 위에서 벌써 `257`을 가지는 정수를 만들었다는 것을 알 정도로 똑똑하지 않아서 메모리에 새로운 객체를 만들게 됩니다.

빈 튜플과 같이 다른 **변하지 않는** 객체에 대해서도 비슷한 최적화가 적용됩니다. 배열은 변할 수 있어서, `[] is []`는 항상 `False`를 반환하고 `() is ()`는 항상 `True`를 반환합니다. 이는 두 번째 예제를 성명합니다. 이제 세 번쨰로 넘어가볼까요?

**같은 줄에서 같은 값으로 초기화할 때 `a`와 `b` 둘 다 같은 객체를 참조합니다.**

**출력 결과**

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

- a와 b가 같은 줄에서 `257`로 할당될 때, 파이썬 인터프리터는 새로운 객체를 만듦과 동시에 두 번째 변수가 참조하게 됩니다. 이것을 다른 줄에서 한다면, 인터프리터는 `257`이 이미 있는지 알지 못합니다.

- 이 현상은 컴파일러 최적화이고 특별히 인터랙티브 환경에서만 적용됩니다. 인터프리터에 두 줄을 입력하게 되면, 각각 컴파일되며, 각각 최적화됩니다. 만약 이를 `.py`파일에서 시도한다면, 한 번에 컴파일되기 때문에 이 현상을 보지 못합니다. 이 최적화는 정수에만 국한된 것이 아니라 문자열("문자열은 가끔 헷갈려요"를 확인해보세요.)과 실수와 같이 변하지 않는 자료 구조에도 적용됩니다.

  ```py
  >>> a, b = 257.0, 257.0
  >>> a is b
  True
  ```

- 왜 파이썬 3.7에서는 작동되지 않나요? 간단히 말하자면 컴파일러 최적화는 구현하기 나름이기 때문입니다. (즉, 버전이나 운영체제 등에 따라 바뀔 수 있어요) 아직 이 문제를 일으킨 정확한 이유를 찾지 못했지만, 이 [이슈](https://github.com/satwikkansal/wtfpython/issues/100)를 확인해보세요.

---

### ▶ 해시 브라우니

<!-- Example ID: eb17db53-49fd-4b61-85d6-345c5ca213ff --->

1\.

```py
some_dict = {}
some_dict[5.5] = "JavaScript"
some_dict[5.0] = "Ruby"
some_dict[5] = "Python"
```

**출력 결과:**

```py
>>> some_dict[5.5]
"JavaScript"
>>> some_dict[5.0] # "Python"이 "Ruby"를 사라지게 했네요.
"Python"
>>> some_dict[5]
"Python"

>>> complex_five = 5 + 0j
>>> type(complex_five)
complex
>>> some_dict[complex_five]
"Python"
```

그래서, 왜 파이썬이 여기저기서 발견되나요?

#### 💡 설명

- 파이썬 딕셔너리 키의 유일성은 키가 서로 동일한지가 아니라, 동등한 값으로 결정됩니다. 그래서 `5`, `5.0`, 그리고 `5 + 0j`가 서로 다른 타입이더라도 같은 값을 가지기 때문에 같은 딕셔너리나 집합안에 있을 수 없습니다. 그 중 하나를 삽입하게 되면 (`KeyError`을 발생시키는 것이 아닌) 동등한 원소를 발견하는 것을 성공하게 됩니다.
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
- 이는 한 원소의 값을 지정할 때도 적용됩니다. 그래서 `some_dict[5] = "Python"`을 하게 되면, 파이썬은 동등한 키인 `5.0 -> "Ruby"`를 찾게 되고, 그 값을 덮어쓰게 됩니다. 
  ```py
  >>> some_dict
  {5.0: 'Ruby'}
  >>> some_dict[5] = "Python"
  >>> some_dict
  {5.0: 'Python'}
  ```
- 그러면 우리는 어떻게 (`5.0` 대신) `5`인 키를 업데이트 할 수 있을까요? 이는 값을 업데이트 하는 것으로는 할 수 없지만, 먼저 키를 지우고 (`del some_dict[5.0]`), 다시 실수 `5.0` 대신 정수 `5`설정하는 (`some_dict[5]`) 것을 통해 할 수 있습니다. 이런 경우는 드물긴 하겠네요.

- 파이썬은 `5.0`을 포함하고 있는 딕셔너리에서 어떻게 `5`를 찾았을까요? 파이썬은 모든 원소를 보지 않고 해시 함수를 이용해 상수 시간에 해결합니다. 파이썬이 `foo`라는 키를 딕셔너리에서 찾을 때, 먼저 `hash(foo)`를 계산합니다. (이는 상수시간에 계산됩니다). 파이썬에서는 동등한 값은 같은 해시값을 가지므로 ([관련 문서](https://docs.python.org/ko/3/reference/datamodel.html#object.__hash__)), `5`, `5.0`, 그리고 `5 + 0j`는 같은 해시 값을 가지게 됩니다. 
  ```py
  >>> 5 == 5.0 == 5 + 0j
  True
  >>> hash(5) == hash(5.0) == hash(5 + 0j)
  True
  ```
  **관련 정보:** 반대는 참이 아닐 수가 있습니다: 해시 값이 같은 두 객체는 동등하지 않을 수 있습니다. (이는 [해시 충돌](https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%EC%B6%A9%EB%8F%8C)이라고 알려져 있고 해싱의 상수 시간의 성능을 저하시킬 수 있습니다. )

---

### ▶ 깊이 들어가면 우리는 다 똑같아.

<!-- Example ID: 8f99a35f-1736-43e2-920d-3b78ec35da9b --->

```py
class WTF:
  pass
```

**출력 결과:**

```py
>>> WTF() == WTF() # 두 인스턴스는 같을 수 없습니다
False
>>> WTF() is WTF() # 메모리 위에서도 다르네요
False
>>> hash(WTF()) == hash(WTF()) # 해시는 _당연히_ 같아야 합니다
True
>>> id(WTF()) == id(WTF())
True
```

#### 💡 설명:

- `id`가 호출되었을 때, 파이썬에서 `WTF` 객체를 만들고 `id` 함수로 넘겨줍니다. `id` 함수는 그 객체의 아이디(`id`, 메모리상의 위치)를 가져오고 객체를 버립니다. 객체는 파괴됩니다.
- 만약 이것을 두 번 한다면, 파이썬은 두 번째 객체도 같은 메모리에 할당하게 됩니다. (CPython에서는) `id`가 메모리의 위치를 객체의 아이디로 쓰기 때문에 두 아이디는 같게 됩니다.
- 그래서 객체의 아이디는 객체가 파괴되지 않는 한 고유합니다. 객체가 파괴된 후 또는 생성되기 이전에는 다른 것이 같은 아이디를 가질 수도 있습니다.
- 그러면 왜 `is` 연산자는 `False`라고 출력했을까요? 이 코드를 보세요.

  ```py
  class WTF(object):
    def __init__(self): print("I")
    def __del__(self): print("D")
  ```

  **출력 결과:**

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

  여러분도 보셨다시피 객체들이 만들어지고 파괴되는 순서가 다르게 됩니다.

---

### ▶ 질서 속의 무질서 \*

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
	__hash__ 마법을 구현하는 dict
    """
    __hash__ = lambda self: 0

class OrderedDictWithHash(OrderedDict):
    """
	__hash__ 마법을 구현하는 OrderedDict
    """
    __hash__ = lambda self: 0
```

**출력 결과**

```py
>>> dictionary == ordered_dict # 만약 a == b 이고,
True
>>> dictionary == another_ordered_dict # b == c 이면
True
>>> ordered_dict == another_ordered_dict # 왜 c == a 가 아닐까요?
False

# 집합(set)은 유일한 원소들만 가지고 있으므로,
# 위의 딕셔너리로 집합을 만들고 어떤 일이 일어나는지 알아봅시다.

>>> len({dictionary, ordered_dict, another_ordered_dict})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'

# 딕셔너리는 __hash__가 구현되어있지 않으므로 그런것 같네요.
# 그러면 위에서 만든 래퍼(wrapper) 클래스를 써봅시다.
>>> dictionary = DictWithHash()
>>> dictionary[1] = 'a'; dictionary[2] = 'b';
>>> ordered_dict = OrderedDictWithHash()
>>> ordered_dict[1] = 'a'; ordered_dict[2] = 'b';
>>> another_ordered_dict = OrderedDictWithHash()
>>> another_ordered_dict[2] = 'b'; another_ordered_dict[1] = 'a';
>>> len({dictionary, ordered_dict, another_ordered_dict})
1
>>> len({ordered_dict, another_ordered_dict, dictionary}) # 순서를 바꿔봅시다.
2
```

무슨 일이 벌어지고 있는거죠?

#### 💡 설명:

- `dictionary` 그리고 `ordered_dict`, `another_ordered_dict`가 자동적으로 같지 않은 이유는 `OrderedDict` 클래스에서 `__eq__` 메소드가 구현된 방식 때문입니다. [도큐먼트](https://docs.python.org/3/library/collections.html#ordereddict-objects)에서
  > OrderedDict 오브젝트이 같음을 확인하는 방법은 순서와 관련이 있고 `list(od1.items())==list(od2.items())`로 구현되어 있습니다. `OrderedDict` 오프젝트와 다른 매핑 오프젝트들의 같음을 확인하는 방법은 순서와 상관있습니다.
- 위와 같이 동작하는 이유는 `OrderedDict` 오브젝트가 바로 보통의 딕셔너리가 사용되는 곳에 사용될 수 있게 하기 위해서 입니다.
- 그러면 왜 `set` 오브젝트에서 순서를 바꾼것이 왜 길이에 영향을 미친 것일까요? 같음을 확인하는 함수가 잘 구현되어 있지 않기 때문입니다. 집합(set)은 유일한 원소들의 순서를 고려하지 않은 자료구조이므로, 각 원소를 삽입하는 순서는 상관이 없어야 합니다. 하지만 이 경우에는 상관이 있네요. 한번 깊이 들어가 봅시다.

  ```py
  >>> some_set = set()
  >>> some_set.add(dictionary) # 이것들은 위의 코드에서의 매핑 오브젝트들입니다
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

  그래서 `ordered_dict == another_ordered_dict`이 `False`이고 `ordered_dict`이 `another_set`안에 들어있었으므로 `another_ordered_dict in another_set`이 `False`인 모순으로 인해서 생긴일 입니다.

---

### ▶ 계속 시도해 보세요... \*

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

def one_more_func(): # 알았다!
    try:
        for i in range(3):
            try:
                1 / i
            except ZeroDivisionError:
				# 여기서 에러를 발생시키고 반복문 밖에서 다뤄보도록 하죠
                raise ZeroDivisionError("A trivial divide by zero error")
            finally:
                print("Iteration", i)
                break
    except ZeroDivisionError as e:
        print("Zero division error ocurred", e)
```

**출력 결과:**

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

#### 💡 설명:

- `return` 또는 `break`, `continue`가 "try-finally" 에서의 `try`문 안에서 실행된다면, `finally` 구문도 끝나기 전에 실행됩니다.
- 함수의 리턴값은 마지막 리턴문에 의해 결정됩니다. `finally` 구문이 항상 마지막에 실행되므로, `finally` 안에 있는 리턴문이 실행됩니다.
- 여기서 주의할 점은 만약 `finally` 구문 안에서 `return`이나 `break`이 있을 때 임시로 저장된 예외가 없어집니다.

---

### ▶ 무엇을 위해서(for)?

<!-- Example ID: 64a9dccf-5083-4bc9-98aa-8aeecde4f210 --->

```py
some_string = "wtf"
some_dict = {}
for i, some_dict[i] in enumerate(some_string):
    i = 10
```

**출력결과:**

```py
>>> some_dict # 딕셔너리가 나타나네요
{0: 'w', 1: 't', 2: 'f'}
```

#### 💡 설명:

- `for` 문은 [파이썬 문법](https://docs.python.org/3/reference/grammar.html)에서 정의되어 있습니다:

  ```
  for_stmt: 'for' exprlist 'in' testlist ':' suite ['else' ':' suite]
  ```

  `exprlist`는 할당되는 부분입니다. 이는 `{exprlist} = {next_value}`와 같다는 말이고 **각각의 원소에 대해 실행됩니다.**
  아래에 재미있는 예제가 있습니다.

  ```py
  for i in range(4):
      print(i)
      i = 10
  ```

  **출력 결과:**

  ```
  0
  1
  2
  3
  ```

  반복문이 한 번만 돌기를 기대했나요?

  **💡 설명:**

  - 반복문이 파이썬에서 특별하게 작동하기 때문에 할당문 `i = 10`은 절대로 반복문에 영향을 끼치지 않습니다. 매번 반복하기 전에 반복자(iterator)에 의해 제공된 값(위 경우는 `range(4)`)들이 변수(위 경우는 `i`)에 할당됩니다.

- `enumerate(some_string)` 함수는 반복마다 새로운 값 `i` (하나씩 올라가는 카운터)와 `some_string`에 있는 문자 하나씩을 yield 합니다. 그리고 딕셔너리 `some_dict`에 키가 `i`인 값을 그 문자로 지정합니다. 반복문을 풀어보면 아래처럼 나올 수 있습니다:
  ```py
  >>> i, some_dict[i] = (0, 'w')
  >>> i, some_dict[i] = (1, 't')
  >>> i, some_dict[i] = (2, 'f')
  >>> some_dict
  ```

---

### ▶ 실행되는 시간의 차이

<!-- Example ID: 6aa11a4b-4cf1-467a-b43a-810731517e98 --->

1\.

```py
array = [1, 8, 15]
# 전형적인 제너레이터(generator) 예제입니다
gen = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
```

**출력 결과:**

```py
>>> print(list(gen)) # 다른 값들은 어디 갔나요?
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

**출력 결과:**

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

**출력 결과:**

```py
>>> print(list(gen))
[401, 501, 601, 402, 502, 602, 403, 503, 603]
```

#### 💡 설명

- [제너레이터](https://wiki.python.org/moin/Generators)에서는 `in` 부분은 선언할 때 실행되지만 조건문은 런타임에 실행됩니다.
- 그래서 런타임 이전에, `array`가 `[2, 8, 22]`로 재할당 되고 `1`, `8`, `15`중에 `8`이 개수가 `0`보다 크므로 제너레이터는 오직 `8`만 yield 합니다.
- 두 번쨰 예제의 `gen_1`과 `gen_2`의 출력 결과가 다른 이유는 `array_1`과 `array_2`가 재할당되는 방법이 다르기 때문입니다.
- 첫 번째 경우에는, `array_1`이 새로운 객체인 `[1, 2, 3, 4, 5]`가 할당되고 `in` 부분은 선언할 때 계산되기 때문에 계속 이전 객체인 `[1, 2, 3, 4]`를 가지고 있습니다.
- 두 번째 경우에는, `array_2`에 슬라이스 객체가 할당될 때 이전의 객체인 `[1, 2, 3, 4]`를 `[1, 2, 3, 4, 5]`로 변화시킵니다. 따라서 `g2`와 `array_2` 모두 같은 (새롭게 `[1, 2, 3, 4, 5]`로 업데이트된) 객체를 가리키고 있습니다.
- 좋아요, 그런데 지금까지의 로직을 살펴보면, 세 번째 예제의 `list(g)`의 값이 `[11, 21, 31, 12, 22, 32, 13, 23, 33]` 가 되어야 하는 것이 아닌가요? (왜냐하면 `array_3`과 `array_4`가 `array_1`처럼 행동할 테니까요). (오직) `array_4`의 값만이 업데이트되는 이유는 [PEP-289](https://www.python.org/dev/peps/pep-0289/#the-details)에서 설명되어 있습니다

  > for 구문의 가장 바깥쪽 부분만 바로 계산되고, 다른 구문들은 제너레이터가 실행될때까지 참조되는 것이 없습니다.

---

### ▶ `is not ...` 은 `is (not ...)`이 아니다

<!-- Example ID: b26fb1ed-0c7d-4b9c-8c6d-94a58a055c0d --->

```py
>>> 'something' is not None
True
>>> 'something' is (not None)
False
```

#### 💡 설명

- `is not` 은 단일 이진 연산자이며, 이는 `is`와 `not`을 따로 사용하는 것과는 다른 기능을 합니다.
- `is not` 연산자는 양쪽의 변수가 동일한 객체를 가리키면 `False`를, 아니면 `True`로 나타납니다.
- In the example, `(not None)` evaluates to `True` since the value `None` is `False` in a boolean context, so the expression becomes `'something' is True`.

---

### ▶ X가 첫 번째 시도에서 승리하는 틱택토!

<!-- Example ID: 69329249-bdcb-424f-bd09-cca2e6705a7a --->

```py
# row를 초기화합니다
row = [""] * 3 #row i['', '', '']
# board를 만듭니다
board = [row] * 3
```

**출력 결과:**

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

우리는 세 개의 `"X"`를 할당하지 않았습니다. 그랬나요?

#### 💡 설명:

다음 시각화 자료는 `row` 변수를 초기화할 때 메모리에서 어떠한 일이 일어나는지 보여줍니다.

![image](../images/tic-tac-toe/after_row_initialized.png)

그리고 다음은 `row`를 곱하여 `board`를 초기화할 때, 메모리에서 일어나는 일입니다. (각각의 원소 `board[0]`, `board[1]` 그리고 `board[2]`는 `row`가 참조한 동일한 리스트의 참조자입니다.)

![image](../images/tic-tac-toe/after_board_initialized.png)

위와 같은 현상은 `row`를 사용하지 않고 `board`를 생성하여 해결할 수 있습니다. (이 [이슈](https://github.com/satwikkansal/wtfpython/issues/68)에서 질문되었습니다).

```py
>>> board = [['']*3 for _ in range(3)]
>>> board[0][0] = "X"
>>> board
[['X', '', ''], ['', '', ''], ['', '', '']]
```

---

### ▶ 달라붙는 출력 함수

<!-- Example ID: 4dc42f77-94cb-4eb5-a120-8203d3ed7604 --->

1\.

```py
funcs = []
results = []
for x in range(7):
    def some_func():
        return x
    funcs.append(some_func)
    results.append(some_func())  # 함수를 호출하고 있다는 것을 놓치지 마세요.

funcs_results = [func() for func in funcs]
```

**출력 결과:**

```py
>>> results
[0, 1, 2, 3, 4, 5, 6]
>>> funcs_results
[6, 6, 6, 6, 6, 6, 6]
```

`funcs`에 `some_func`를 추가하기 전의 `x`값은 항상 달랐는데도, 모든 함수가 6을 리턴합니다.

2\.

```py
>>> powers_of_x = [lambda x: x**i for i in range(10)]
>>> [f(2) for f in powers_of_x]
[512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
```

#### 💡 설명

- 반복문 내에서 반복문의 변수를 사용하는 함수를 정의하면, 함수의 클로저는 변수의 값이 아니라 변수 자체에 바인딩됩니다. 따라서 모든 함수가 그 변수에 마지막으로 할당된 값을 사용하게 되죠.

- 원하는 결과를 얻고 싶다면, 반복문의 변수를 함수의 인자로서 넘겨주면 됩니다. **이게 왜 되는 걸까요?** 이렇게 하면 변수가 함수의 스코프 내에서 다시 정의되기 때문입니다.

  ```py
  funcs = []
  for x in range(7):
      def some_func(x=x):
          return x
      funcs.append(some_func)
  ```

  **출력 결과:**

  ```py
  >>> funcs_results = [func() for func in funcs]
  >>> funcs_results
  [0, 1, 2, 3, 4, 5, 6]
  ```

---

### ▶ 닭이 먼저일까, 달걀이 먼저일까 \*

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

그래서, "궁극적인" 기본 클래스는 뭘까요? 혼란스러운 점은 이게 끝이 아닙니다.

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

#### 💡 설명

- `type`은 파이썬의 [메타클래스](https://realpython.com/python-metaclasses/)입니다.
- 파이썬에서 **모든 것은** `object`입니다. 이는 클래스와 인스턴스 모두에게 해당됩니다.
- `type` 클래스는 `object` 클래스의 메타클래스이고, (`type`을 포함하는) 모든 클래스는 직접적으로든 간접적으로든 `object`를 상속합니다.
- `object`와 `type` 중에서 진짜 기본 클래스는 존재하지 않습니다. 위의 코드들이 야기하는 혼란은 우리가 이런 관계들(`issubclass`와 `isinstance`)을 파이썬 클래스의 관점에서 생각하고 있기 때문에 발생합니다. `object`와 `type`의 관계는 순수 파이썬만으로는 재현할 수 없습니다. 정확히 말하자면, 아래의 관계는 순수 파이썬만으로 재현하는 것이 불가능합니다.
  - 클래스 A는 클래스 B의 인스턴스이고, 클래스 B는 클래스 A의 인스턴스입니다.
  - 클래스 A는 자기 자신의 인스턴스입니다.
- `object`와 `type`의 이러한 관계(서로가 서로와 자기 스스로의 인스턴스인 것)를 가질 수 있는 건 구현 수준에서의 "편법"이 사용되었기 때문입니다.

---

### ▶ 서브 클래스의 관계

<!-- Example ID: 9f6d8cf0-e1b5-42d0-84a0-4cfab25a0bc0 --->

**출력 결과:**

```py
>>> from collections import Hashable
>>> issubclass(list, object)
True
>>> issubclass(object, Hashable)
True
>>> issubclass(list, Hashable)
False
```

서브 클래스의 관계는 삼단논법을 따라야 하지 않나요? (즉 `A`가 `B`의 서브 클래스이고 `B`가 `C`의 서브 클래스이면 `A`는 `C`의 서브 클래스 _이여야만_ 합니다)

#### 💡 설명:

- 파이썬에서는 서브 클래스의 관계가 삼단논법을 따를 필요가 없습니다. 아무나 자유롭게 메타클래스에 자신만의 `__subclasscheck__`를 만들 수 있습니다.
- `issubclass(cls, Hashable)`이 호출되면, `cls`나 이의 조상 클래스에서 거짓이 아닌 "`__hash__`" 메소드를 찾습니다.
- `object`가 해싱할 수 있고 `list`는 해싱할 수 없기 때문에, 상속되었다고 보기 힘듭니다.
- 더 자세한 정보는 [여기](https://www.naftaliharris.com/blog/python-subclass-intransitivity/)에서 찾아볼 수 있습니다.

---

### ▶ 메소드의 같음과 동일함

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

**출력 결과:*

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

`classm`을 두 번 접근했을 때, 동등한 객체이지만 _같지는_ 않은 객체가 되네요?
`SomeClass`의 인스턴스는 어떻게 되는지 한 번 볼까요?:

> 여기서 동등하다는 것은 메모리 상 같은 위치에 있다는 것이고, 같다는 것은 단순하게 값이 같다는 의미입니다. 

2.

```py
o1 = SomeClass()
o2 = SomeClass()
```

**출력 결과:**

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

`SomeClass`의 같은 인스턴스는 `classm`와 `method`를 두 번 접근했을 때, 동등하지만 _같지는_ 않은 객체를 생성합니다.

#### 💡 설명

- 함수는 [디스크립터](https://docs.python.org/ko/3/howto/descriptor.html) 입니다. 
함수가 속성으로 접근되었을 때, 디스크립터가 호출되고, 객체를 가지고 속성으로 가지고 있는 함수를 "바인딩" 하는 메소드 객체를 생성합니다. 
만약 호출되면 메소드는 그 함수를 호출하고, 내부적으로 바인드된 객체를 첫 번째 인자로 넘겨줍니다. 
(이 원리로 인해 직접적으로 넘기지 않고 `self`를 첫 번째 인자로 받을 수 있는 것입니다.)

```py
>>> o1.method
<bound method SomeClass.method of <__main__.SomeClass object at ...>>
```

- 속성에 여러번 접근할 때마다 매번 메소드 객체를 만들게 됩니다! 
그래서 `o1.method is o2.method`는 참일 수가 없는 것이죠. 
(인스턴스와 반대되게) 함수를 클래스 속성으로 접근하게 되면 메소드를 생성하지 않게 됩니다. 
그래서 `SomeClass.method is SomeClass.method`는 항상 참입니다. 

```py
>>> SomeClass.method
<function SomeClass.method at ...>
```

- `classmethod`는 함수를 클래스 메소드로 변환시킵니다. 클래스 메소드는 접근할때 객체 대신에 객체의 _class_ (타입)을 바인드한 메소드 객체를 생성하는 디스크럽터 입니다.

```py
>>> o1.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```

- 함수와는 달리, `classmethods`는 클래스 속성으로 접근할 때 (타입이 아닌 클래스를 바인드 합니다) 새로운 메소드를 생성합니다. 
그래서 `SomeClass.classm is SomeClass.classm`는 거짓입니다.

```py
>>> SomeClass.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```

- 메소드 객체가 같다는 것은 두 함수가 같고 바인드 되어 있는 객체가 같음을 의미합니다.
그래서 메모리상 같은 객체가 아님에도 `o1.method == o1.method`는 같습니다.
- `staticmethod`는 함수를 그대로 리턴하는 "no-op" (아무 일도 하지 않는) 디스크립터를 통해 함수를 변형시킵니다.
어떠한 객체도 생성되지 않으며, `is`로 비교하는 것은 참이 됩니다.

```py
>>> o1.staticm
<function SomeClass.staticm at ...>
>>> SomeClass.staticm
<function SomeClass.staticm at ...>
```

- 파이썬에서 인스턴스 메소드를 호출할 때마다 인자들을 매번 변경하고 맨 앞에 `self`를 넣어주면서 새로운 "메소드" 객체를 만드는 것은 속도에 나쁘게 영향을 끼치게 됩니다.
CPython 3.7은 임시 메소드 객체를 만들지 않고 해결하는 새로운 명령코드를 만들어서 이 문제를 [해결했습니다.](https://bugs.python.org/issue26110).
이 방법은 함수가 실제로 호출 될 때 사용되므로, 여기 있는 코드들에 영향을 끼치지 않고 여전히 메소드를 생성합니다 :)

---

### ▶ 참 거짓의 반복 \*

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

왜 이런 참 거짓의 반복이 일어날까요?

#### 💡 설명:

- `all`함수의 구현은 다음과 같습니다

- ```py
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

- `all([])`은 비어있으므로 `True`를 반환합니다.
- `all([[]])`은 `not[]`는 True이며 이는 `not False`와 같고, `iterable` 안에 있는 리스트가 비어 있기 때문에 `False`를 반환합니다.
- `all([[[]]])`와 더 많이 겹친 경우는 `not [[]]`, `not [[[]]]`... 이 `not True`와 동일 하므로 모두 `True`를 반환합니다.

---

### ▶ 놀라운 콤마

<!-- Example ID: 31a819c8-ed73-4dcc-84eb-91bedbb51e58 --->

**출력 결과 (< 3.6):**

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

#### 💡 설명:

- 파이썬 함수의 정규 파라미터 리스트에 콤마를 남기는 것이 항상 허용되는 것은 아닙니다.
- 파이썬에서 전달인자 리스트는 선행 콤마(leading commas)들과 후행 콤마(trailing commas)들로 부분적으로 정의되어 있습니다. 이러한 충돌이 콤마가 가운데에 끼게되는 현상을 만들게 되고 결국 아무 규칙에도 맞지 않게 됩니다.
- **참고:** 후행 콤마 문제는 [파이썬 3.6에서 고쳐졌습니다](https://bugs.python.org/issue9232). 이 [포스트](https://bugs.python.org/issue9232#msg248399)에서는 파이썬에서의 후행 콤마들의 다양한 사용법들이 간결하게 논의하고 있습니다.

---

### ▶ 문자열과 백슬래시

<!-- Example ID: 6ae622c3-6d99-4041-9b33-507bd1a4407b --->

**출력 결과:**

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

#### 💡 설명

- 보통 파이썬 문자열에서 백슬래시는 특별한 의미의 문자(작은 따옴표나 큰 따옴표, 그리고 백슬래시 그 자체)를 이스케이프하는데 사용됩니다.
  ```py
  >>> "wt\"f"
  'wt"f'
  ```
- 원시 문자열 리터럴(raw string literal, 접두사 `r`로 나타난다)에서는 백슬래시들이 그대로 출력되지만 그 특성도 그대로 적용됩니다.

  ```py
  >>> r'wt\"f' == 'wt\\"f'
  True
  >>> print(repr(r'wt\"f')
  'wt\\"f'

  >>> print("\n")

  >>> print(r"\\n")
  '\\n'
  ```

- 즉, 이는 파서가 원시 문자열에서 백슬래시와 만나면 그 뒤에 문자가 나오기를 예상한다는 것입니다. 그리고 이러한 경우(`print(r"\")`)에서는 백슬래시가 뒤의 따옴표에서 이스케이프하여 파서는 끝나는 따옴표를 찾지 못합니다(따라서 `SyntaxError`이 발생합니다). 이 이유로 원시 문자열의 끝에서 백슬래시를 사용할 수 없습니다.

---

### ▶ 매듭이 아니야!

<!-- Example ID: 7034deb1-7443-417d-94ee-29a800524de8 --->

```py
x = True
y = False
```

**출력 결과:**

```py
>>> not x == y
True
>>> x == not y
  File "<input>", line 1
    x == not y
           ^
SyntaxError: invalid syntax
```

#### 💡 설명:

- 연산자 우선순위는 표현식이 실행되는 것에 영향을 주고 파이썬에서는 `==` 연산자는 `not` 연산자보다 우선순위가 높습니다.
- 그래서 `not x == y`는 `not (x == y)`와 같고 이는 `not (True == False)`와 같게 되므로 최종적으로 `True`가 됩니다.
- 하지만 `x == not y`는 `SyntaxError`를 발생시키게 됩니다. 왜냐하면 이는 보통 생각하는 `x == (not y)`가 아니라 `(x == not) y`로 해석되기 때문입니다.
- 파서는 `not` 토큰이 `not in` 연산자의 일부라고 예상하지만 (왜냐하면 `==`와 `not in` 연산자가 같은 연산자 우선순위를 가지고 있기 때문입니다) `not` 뒤에 `in` 토큰을 찾을 수 없기 때문에 `SyntaxError`를 발생시킵니다.

---

### ▶ 반쪽 3중 따옴표 문자열

<!-- Example ID: c55da3e2-1034-43b9-abeb-a7a970a2ad9e --->

**출력 결과:**

```py
>>> print('wtfpython''')
wtfpython
>>> print("wtfpython""")
wtfpython
>>> # 다음 표현식은 `SyntaxError`를 발생시킵니다.
>>> # print('''wtfpython')
>>> # print("""wtfpython")
  File "<input>", line 3
    print("""wtfpython")
                        ^
SyntaxError: EOF while scanning triple-quoted string literal
```

#### 💡 설명:

- 파이썬은 암묵적 [문자열 리터럴 병합 연산](https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation) 연산을 지원합니다, 예시로,
  ```
  >>> print("wtf" "python")
  wtfpython
  >>> print("wtf" "") # 또는 "wtf"""
  wtf
  ```
- `'''` 와 `"""` 는 파이썬에서 문자열 구분 기호로 파이썬은 후에 문자열 끝맺음 3중 따옴표를 찾지만 찾지 못해 SyntaxError를 발생시킵니다.

---

### ▶ 불린의 문제점이 뭐야?

<!-- Example ID: 0bba5fa7-9e6d-4cd2-8b94-952d061af5dd --->

1\.

```py
# 다양한 데이터 타입 속 불린의 개수와 정수의 개수를 세는 간단한 예제입니다.
mixed_list = [False, 1.0, "some_string", 3, True, [], False]
integers_found_so_far = 0
booleans_found_so_far = 0

for item in mixed_list:
    if isinstance(item, int):
        integers_found_so_far += 1
    elif isinstance(item, bool):
        booleans_found_so_far += 1
```

**출력 결과:**

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

**출력 (< 3.x):**

```py
>>> tell_truth()
I have lost faith in truth!
```

#### 💡 설명:

- 파이썬에서 `bool`은 `int`의 서브클래스입니다.
  ```py
  >>> issubclass(bool, int)
  True
  >>> issubclass(int, bool)
  False
  ```
- 추가로, `True`와 `False`는 `int`의 인스턴스입니다.

  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

- `True`의 정수 값은 `1`이고 `False`의 정수 값은 `0`입니다.

  ```py
  >>> int(True)
  1
  >>> int(False)
  0
  ```

- StackOverflow [답변](https://stackoverflow.com/a/8169049/4354153)을 통해 이러한 현상이 발생하는 이유에 대해서 알아보세요.

- 초기에, 파이썬은 `bool` 타입이 없었습니다. (사람들은 0을 거짓으로 쓰고 1과 같은 0이 아닌 수를 참으로 사용했습니다) `True` 그리고 `False`, `bool` 타입은 2.x 버전에서 추가되었지만 호환성을 위해 `True`와 `False`는 상수로 만들어질 수 없었습니다. 이들은 내장 변수이고 다시 할당하는 것이 가능했습니다.

- 파이썬 3은 호환이 안되기 때문에, 문제가 해결되었고 마지막 코드는 파이썬 3.x 에서는 작동하지 않습니다!

---

### ▶ 클래스 속성과 인스턴스 속성

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
>>> A.x, B.x, C.x # C.x 는 바뀌었지만, B.x 는 바뀌지 않았습니다.
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

#### 💡 설명:

- 클래스 변수들과 클래스 인스턴스 안에 있는 변수들은 내부에서 클래스 객체의 딕셔너리들로 처리됩니다. 현재 클래스의 딕셔너리에 변수 이름이 없는 경우, 부모 클래스에서 해당 이름을 검색합니다.
- '+=' 연산자는 새로운 객체를 생성하지 않고 그 자리에서 가변 객체를 수정합니다. 따라서, 한 인스턴스의 속성을 바꾸는 것은 다른 인스턴스들과 클래스 속성에도 영향을 미칩니다.

---

### ▶ yielding None

<!-- Example ID: 5a40c241-2c30-40d0-8ba9-cf7e097b3b53 --->

```py
some_iterable = ('a', 'b')

def some_func(val):
    return "something"
```

**출력 결과 (<= 3.7.x):**

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

#### 💡 설명:

- 이것은 CPython에서 제너레이터와 컴프리헨션에서 `yield`를 처리할 때 생기는 버그입니다.
- 소스와 설명은 여기서 찾아볼 수 있습니다: https://stackoverflow.com/questions/32139885/yield-in-list-comprehensions-and-generator-expressions
- 관련된 버그 리포트: https://bugs.python.org/issue10544
- 파이썬 3.8 이상의 버전에서는 리스트 컴프리헨션의 내부에 `yield`를 허용하지 않고 `SyntaxError`를 발생시킵니다.

---

### ▶ Yielding from... return! \*

<!-- Example ID: 5626d8ef-8802-49c2-adbc-7cda5c550816 --->

1\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        yield from range(x)
```

**출력 결과 (> 3.3):**

```py
>>> list(some_func(3))
[]
```

`"wtf"`이 어디로 갓나요? `yield from`의 특수한 효과 때문일까요? 확인해봅시다.

2\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        for i in range(x):
          yield i
```

**출력 결과:**

```py
>>> list(some_func(3))
[]
```

같은 결과입니다. 이것도 효과가 없습니다.

#### 💡 설명:

- 파이썬 3.3 이후의 버전부터, 내부의 제너레이터와 함께 `return`문을 사용할 수 있게 되었습니다 (이것을 참고하세요 [PEP380](https://www.python.org/dev/peps/pep-0380/)). [공식 문서](https://www.python.org/dev/peps/pep-0380/#enhancements-to-stopiteration)에서도 말하고 있습니다.

> "... 제너레이터 내부의 `return expr`는 제너레이터가 종료될 때 `StopIteration(expr)`을 발생시킵니다."

- `some_func(3)`의 경우, `return`문으로 인해 처음부터 `StopIteration`이 발생합니다. `StopIteration` 예외는 자동으로 `list(...)` 래퍼와 `for` 루프의 내부에 잡히게 됩니다. 따라서 위의 두 코드의 결과는 빈 리스트가 됩니다.

- 제너레이터의 `some_func`에서 `["wtf"]`을 얻으려면 `StopIteration` 예외를 잡아야 합니다.

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

### ▶ Nan-재귀성 \*

<!-- Example ID: 59bee91a-36e0-47a4-8c7d-aa89bf1d3976 --->

1\.

```py
a = float('inf')
b = float('nan')
c = float('-iNf')  # 이 문자열은 대소문자를 구분하지 않습니다
d = float('nan')
```

**출력 결과:**

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
>>> b == d # 하지만 nan!=nan 입니다
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
>>> y is y # 정체성은 유지됩니다
True
>>> y == y # y와 같은 값은 아닙니다
False
>>> [y] == [y] # 하지만 y를 리스트로 감싸면 같은 값이 됩니다
True
```

#### 💡 설명:

- `'inf'`와 `'nan'`은 대소문자를 구분하지 않는 특수한 문자열로, 명시적으로 `float` 타입으로 형 변환할 때 수학적 "무한대"와 "숫자가 아님"을 표현할 때 사용합니다.

- IEEE 표준 `NaN != NaN`을 따르면 파이썬에서 컬렉션 요소들의 재귀성 가정이 깨지게 됩니다. 만약 `x`가 `list`와 같은 컬렉션의 일부면 비교와 같은 구현들은 `x == x`라는 가정에 기반합니다. 이런 가정 때문에 두 요소를 비교할 때 정체성을 먼저 비교하고 (속도가 더 빠르기 때문입니다) 정체성이 일치하지 않을 때만 값을 비교합니다. 다음의 코드가 이것들을 더 확실하게 만들어 줄 겁니다,

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

  `x`와 `y`의 정체성이 다르기 때문에 값이 고려되고, 비교 결과 `False`가 반환됩니다.

- 흥미로운 읽을거리: [Reflexivity, and other pillars of civilization](https://bertrandmeyer.com/2010/02/06/reflexivity-and-other-pillars-of-civilization/)

---

### ▶ 불변을 변형하기!

<!-- Example ID: 15a9e782-1695-43ea-817a-a9208f6bb33d --->

여러분이 파이썬에서 참조가 어떻게 작동하는지 안다면 이건 당연해 보일 수 있습니다.

```py
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
```

**출력 결과:**

```py
>>> some_tuple[2] = "change this"
TypeError: 'tuple' object does not support item assignment
>>> another_tuple[2].append(1000) #이건 에러를 만들지 않습니다
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000])
>>> another_tuple[2] += [99, 999]
TypeError: 'tuple' object does not support item assignment
>>> another_tuple
([1, 2], [3, 4], [5, 6, 1000, 99, 999])
```

하지만 저는 튜플이 변경 불가능하다 생각했습니다...

#### 💡 설명:

- https://docs.python.org/ko/3/reference/datamodel.html 을 인용하면

  > 불변 시퀸스
  >
  > 불변 시퀀스 형의 객체는 일단 만들어진 후에는 변경될 수 없다. (만약 다른 객체로의 참조를 포함하면, 그 객체는 가변일 수 있고, 변경될 수 있다; 하지만, 불변 객체로부터 참조되는 객체의 집합 자체는 변경될 수 없다.)

- `+=` 연산자는 리스트를 그 자리에서 변경합니다. 그 항목 할당이 동작하지 않지만, 예외 발생 시 그 항목은 이미 그 자리에서 변경되었습니다.

---

### ▶ 외부 범위에서 사라지는 변수

<!-- Example ID: 7f1e71b6-cb3e-44fb-aa47-87ef1b7decc8 --->

```py
e = 7
try:
    raise Exception()
except Exception as e:
    pass
```

**출력 결과 (Python 2.x):**

```py
>>> print(e)
# 아무것도 출력하지 않습니다
```

**출력 결과 (Python 3.x):**

```py
>>> print(e)
NameError: name 'e' is not defined
```

#### 💡 설명:

- 출처: https://docs.python.org/ko/3/reference/compound_stmts.html#except

  예외가 `as target`을 사용해서 대입될 때, `except`절 끝에서 삭제됩니다. 이것은 마치

  ```py
  except E as N:
      foo
  ```

  가 이렇게 변환되는 것과 같습니다

  ```py
  except E as N:
      try:
          foo
      finally:
          del N
  ```

  이것은 except 절 후에 참조하려면 예외를 다른 이름에 대입해야 한다는 뜻입니다. 예외를 제거하는 이유는, 그것에 첨부된 트레이스백으로 인해, 스택 프레임과 참조 순환을 형성해서 다음 가비지 수거가 일어나기 전까지 그 프레임의 모든 지역 변수들을 잡아두기 때문입니다.

- 해당 절들은 파이썬에서 범위가 정해지지 않았습니다. 예시의 모든 것이 동일한 범위에 존재하며 `except` 절의 실행으로 `e` 변수가 삭제되었습니다. 별도의 내부 범위를 가지고 있는 함수들도 마찬가지인 데 다음의 예시가 보여줍니다:

  ```py
  def f(x):
      del(x)
      print(x)

  x = 5
  y = [5, 4, 3]
  ```

  **출력 결과:**

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

- 파이썬 2.x에서는 `e` 변수가 `Exception()` 인스턴스에 할당되므로 출력하려 할 때 아무것도 출력하지 않습니다.

  **출력 결과 (Python 2.x):**

  ```py
  >>> e
  Exception()
  >>> print e
  # 아무것도 출력되지 않았습니다!
  ```

---

### ▶ 미스테리한 키 타입 형 변환

<!-- Example ID: 00f42dd0-b9ef-408d-9e39-1bc209ce3f36 --->

```py
class SomeClass(str):
    pass

some_dict = {'s': 42}
```

**출력 결과:**

```py
>>> type(list(some_dict.keys())[0])
str
>>> s = SomeClass('s')
>>> some_dict[s] = 40
>>> some_dict # 예상: 두개의 다른 key-value 쌍
{'s': 40}
>>> type(list(some_dict.keys())[0])
str
```

#### 💡 설명:

- `SomeClass`는 `str` 클래스의 `__hash__` 메소드를 상속받기 때문에 객체 `s`와 문자열 `"s"`는 같은 값을 갖게 됩니다.
- `SomeClass`은 `str` 클래스의 `__eq__` 메소드도 상속받기 때문에 `SomeClass("s") == "s"`의 결과는 `True`가 됩니다.
- 두 객체는 같은 값으로 해싱되어 동일하기 때문에 딕셔너리에서 같은 키로 표현됩니다.
- 원하는 동작을 위해 `SomeClass`의 `__eq__` 메소드를 다시 정의할 수 있습니다.

  ```py
  class SomeClass(str):
    def __eq__(self, other):
        return (
            type(self) is SomeClass
            and type(other) is SomeClass
            and super().__eq__(other)
        )

    # 수정된 __eq__를 정의할 때 파이썬은 자동으로 __hash__ 메소드를
    # 상속받는 것을 중단합니다. 그래서 정의해줄 필요가 있습니다.
    __hash__ = str.__hash__

  some_dict = {'s':42}
  ```

  **출력 결과:**

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

### ▶ 여러분이 맞출 수 있는지 한번 볼까요?

<!-- Example ID: 81aa9fbe-bd63-4283-b56d-6fdd14c9105e --->

```py
a, b = a[b] = {}, 5
```

**출력 결과:**

```py
>>> a
{5: ({...}, 5)}
```

#### 💡 설명:

- [파이썬 언어 레퍼런스](https://docs.python/org/ko/2/reference/simple_stmts.html#assignment-statements)에 따르면, 대입문의 구조는 다음과 같은 형태를 보입니다.
  ```
  (target_list "=")+ (expression_list | yield_expression)
  ```
  그리고

> 대입문은 표현식 목록 (이것이 하나의 표현식일 수도, 쉼표로 분리된 목록일 수도 있는데, 후자의 경우는 튜플이 만들어진다는 것을 기억하라) 의 값을 구하고, 왼쪽에서 오른쪽으로, 하나의 결과 객체를 타깃 목록의 각각에 대입한다.

- `(target_list "=")+`의 `+`는 **하나 이상의** 타깃 목록이 있을 수 있음을 의미합니다. 예제의 경우 타깃 목록은 `a, b`, `a[b]` 입니다. (표현식 목록은 정확하게 하나이며 예제의 경우 `{}, 5` 입니다.)

- 표현식 목록을 평가한 후 해당 값은 **왼쪽에서 오른쪽으로** 타깃 목록에 풀어지게 됩니다. 예제의 경우 먼저 `{}, 5`의 튜플이 `a, b`로 풀리고 `a = {}`, `b = 5`가 됩니다.

- `a`는 이제 변경 가능한 객체인 `{}`에 할당됩니다.

- 두 번째 타깃 목록은 `a[b]`입니다. (여러분은 `a`와 `b`가 구문 이전에 정의되지 않아 에러가 발생할 거라 예상할 수 있습니다. 하지만 우리는 방금 `a`에 `{}`, `b`에 `5`를 대입한 사실을 기억하세요)

- 이제 딕셔너리에 있는 키 `5`를 튜플 `({}, 5)`로 설정하여 순환 참조를 생성합니다. (출력의 `{...}`는 `a`가 이미 참조하고 있는 객체를 가리킵니다.) 순화 참조의 다른 간단한 예는 다음과 같습니다.

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

  우리의 예제에서도 이것과 비슷합니다. (`a[b][0]`은 `a`와 같은 객체입니다.)

- 요약하자면, 예제를 다음과 같이 나눌 수 있습니다.
  ```py
  a, b = {}, 5
  a[b] = a, b
  ```
  그리고 순환 참조는 `a[b][0]`이 `a`와 동일한 객체라는 사실에 의해 정당화 될 수 있습니다.
  ```py
  >>> a[b][0] is a
  True
  ```

---

---

## "미끄러운 비탈길" 단원

### ▶ 딕셔너리가 반복 중일 때 수정하기

<!-- Example ID: b4e5cdfb-c3a8-4112-bd38-e2356d801c41 --->

```py
x = {0: None}

for i in x:
    del x[i]
    x[i+1] = None
    print(i)
```

**출력 결과 (Python 2.7- Python 3.5):**

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

정확히 **8**번 돌고 멈춥니다.

#### 💡 설명:

- 딕셔너리가 반복될 때 동시에 편집할 수 있는 것은 지원되지 않습니다.
- 8번 반복되는 이유는 더 많은 키를 소유하기 위해 딕셔너리가 크기를 조정하는 지점이기 때문입니다. (우리는 8개의 삭제 항목들이 있으므로, 크기의 조정이 필요합니다) 이는 실제 구현의 세부사항입니다.
- 삭제된 키를 처리하는 과정과 크기의 조정이 이루어지는 시점은 Python의 구현에 따라 다를 수 있습니다.
- 따라서, 파이썬 2.7 - 3.5 이외의 버전의 경우, 실행 횟수가 8과 다를 수 있습니다. (하지만 횟수가 어떻던 간에, 실행할 때 마다 동일한 결과입니다) [여기](https://github.com/satwikkansal/wtfpython/issues/53) 또는 StackOverflow의 [이 스레드](https://stackoverflow.com/questions/44763802/bug-in-python-dict)에서 이에 관한 토론을 찾을 수 있습니다.
- 파이썬 3.7.6 이상에서는 이것을 시도할 경우 `RuntimeError: dictionary keys changed during iteration` 예외를 보여줍니다.

---

### ▶ 완강한 `del` 연산자

<!-- Example ID: 777ed4fd-3a2d-466f-95e7-c4058e61d78e --->
<!-- read-only -->

```py
class SomeClass:
    def __del__(self):
        print("Deleted!")
```

**출력 결과:**
1\.

```py
>>> x = SomeClass()
>>> y = x
>>> del x # "Deleted!"를 출력해야 합니다
>>> del y
Deleted!
```

휴, 드디어 삭제되었습니다. 여러분은 처음의 `x` 삭제에서 `__del__`이 호출되지 않은 것을 생각하실 수도 있습니다. 이제 예제를 살짝 비틀어 봅시다.

2\.

```py
>>> x = SomeClass()
>>> y = x
>>> del x
>>> y # y가 존재하는지 확인합니다
<__main__.SomeClass instance at 0x7f98a1a67fc8>
>>> del y # 이전과 같이, "Deleted!"를 출력해야 합니다
>>> globals() # 오, 그렇지 않네요. 우리의 전역변수를 확인해봅시다
Deleted!
{'__builtins__': <module '__builtin__' (built-in)>, 'SomeClass': <class __main__.SomeClass at 0x7f98a1a5f668>, '__package__': None, '__name__': '__main__', '__doc__': None}
```

좋습니다. 이제 삭제되었습니다 :confused:

#### 💡 설명:

- `del x`는 직접적으로 `x.__del__()`을 부르지 않습니다.
- `del x`가 호출될 때, 파이썬은 `x`에 대한 참조 카운트를 하나씩 줄입니다. 그리고 `x.__del__()`은 x의 참조 카운트가 0에 도달할 때 실행됩니다.
- 두번째 코드의 출력에서, `y.__del__()` 는 호출되지 않습니다. 왜냐하면 이전의 구문에 (`>>> y`) 대화형 인터프리터가 같은 객체에 대해 또 다른 참조를 만들고, 따라서 `del y`가 호출될 때 참조 카운트가 0에 도달하지 않습니다.
- `globals`가 호출되면 존재하는 참조가 파괴돼, 이런 이유로 우리는 "Deleted!"가 출력되는 것을 볼 수 있습니다. (마침내!)

---

### ▶ 범위를 벗어난 변수

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

**출력 결과:**

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

#### 💡 설명:

- 범위 내의 변수에 할당하면, 해당 범위의 로컬 변수가 됩니다. 그래서 `a`는 `another_func`의 범위에 국한되지만 이전과 같은 범위에서 초기화 되지 않아 에러가 발생합니다.
- `another_func`에서 외부 범위의 `a`를 변경하려면, `global` 키워드를 사용하세요.

  ```py
  def another_func()
      global a
      a += 1
      return a
  ```

  **출력 결과:**

  ```py
  >>> another_func()
  2
  ```

- In `another_closure_func`, `a` becomes local to the scope of `another_inner_func`, but it has not been initialized previously in the same scope, which is why it throws an error.
- To modify the outer scope variable `a` in `another_inner_func`, use the `nonlocal` keyword. The nonlocal statement is used to refer to variables defined in the nearest outer (excluding the global) scope.

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

- The keywords `global` and `nonlocal` tell the python interpreter to not delcare new variables and look them up in the corresponding outer scopes.

- 짧지만 멋진 [이 가이드](http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html)를 읽고 네임스페이스와 범위 결정이 파이썬에서 작동하는 방법에 대해 알아보세요.

---

### ▶ 반복하는 동안 리스트의 아이템을 삭제하기

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

**출력 결과:**

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

왜 출력 결과가 `[2, 4]`가 나오는지 알 수 있나요?

#### 💡 설명:

- 반복하고 있는 객체를 바꾸는 것은 좋은 생각이 아닙니다. 올바른 방법은 `list_3[:]`과 같이 복사본을 반복하는 것입니다.

  ```py
  >>> some_list = [1, 2, 3, 4]
  >>> id(some_list)
  139798789457608
  >>> id(some_list[:]) # 파이썬은 슬라이스된 리스트를 위해 새로운 객체를 생성하는 것을 알 수 있습니다.
  139798779601192
  ```

**`del`, `remove`, `pop`의 차이점**

- `del var_name`은 로컬 또는 전역 네임스페이스에서 `var_name`의 바인딩을 삭제합니다. (그래서 `list_1`은 영향 받지 않습니다)
- `remove`는 특정 인덱스가 아닌 첫번째 일치하는 값을 삭제하는 경우 값을 찾을 수 없으면 `ValueError`를 일으킵니다.
- `pop`은 특정 인덱스에서 요소를 제거하고 반환하며, 인덱스가 유효하지 않으면 `IndexError`를 일으킵니다.

**왜 `[2, 4]`가 출력되나요?**

- 리스트의 반복은 인덱스별로 이루어지며, `list_2` 또는 `list_4`에서 `1`을 삭제하면, 리스트는 `[2, 3, 4]`가 됩니다. 나머지 요소들은 인덱스가 낮아지게 되어 `2`는 인덱스 0, `3`은 인덱스 1이 됩니다. 다음번 반복은 인덱스 1 (요소 `3`이 됩니다)을 보게 되고, `2`는 건너뛰게 됩니다. 리스트 순서의 모든 대안 요소들도 비슷한 상황이 일어납니다.

* 예제를 설명하는 StackOverflow [스레드](https://stackoverflow.com/questions/45946228/what-happens-when-you-try-to-delete-a-list-element-while-iterating-over-it) 를 참고하였습니다.
* 파이썬의 딕셔너리에 관련된 비슷한 예제로 이 StackOverflow [스레드](https://stackoverflow.com/questions/45877614/how-to-change-all-the-dictionary-keys-in-a-for-loop-with-d-items) 도 참고하세요.

---

### ▶ 반복자의 손실되는 zip \*

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
# 지금까지는 좋은데, 나머지도 압축해봅시다
>>> list(zip(numbers_iter, remaining))
[(4, 3), (5, 4), (6, 5)]
```

`numbers` 리스트에서 요소 `3`이 어디로 갔을까요?

#### 💡 설명:

- 파이썬의 [이 문서](https://docs.python.org/3.3/library/functions.html#zip)에서, zip 함수의 대략적인 구현을 살펴봅시다.
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
- 그래서 이 함수는 임의의 수의 반복 가능한 객체를 모아 `next` 함수를 호출하여 각각의 항목을 `result` 리스트에 추가하고, 반복 가능한 객체 중 하나가 고갈될 때에 중지합니다.
- 여기서 주의해야 할 점은 반복 가능한 객체들이 고갈될 때, `result` 리스트에 들어 있는 기존의 요소들이 폐기되는 것입니다. `numbers_iter` 내부의 `3`에 그러한 일이 일어났습니다.
- `zip`을 사용하여 위와 같은 일을 처리하는 올바른 방법은 다음과 같습니다,
  ```py
  >>> numbers = list(range(7))
  >>> numbers_iter = iter(numbers)
  >>> list(zip(first_three, numbers_iter))
  [(0, 0), (1, 1), (2, 2)]
  >>> list(zip(remaining, numbers_iter))
  [(3, 3), (4, 4), (5, 5), (6, 6)]
  ```
  zip의 첫번째 인자는 가장 적은 요소를 가지고 있어야 합니다.

---

### ▶ 루프 변수가 유출되고 있습니다!

<!-- Example ID: ccec7bf6-7679-4963-907a-1cd8587be9ea --->

1\.

```py
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')
```

**출력 결과:**

```py
6 : for x inside loop
6 : x in global
```

하지만 `x`는 루프의 밖에서 선언된 적이 없습니다...

2\.

```py
# 이번엔 먼저 x를 초기화해봅시다
x = -1
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')
```

**출력 결과:**

```py
6 : for x inside loop
6 : x in global
```

3\.

**출력 결과 (Python 2.x):**

```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
4
```

**출력 결과 (Python 3.x):**

```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
1
```

#### 💡 설명:

- 파이썬에서, for 루프는 루프의 스코프를 사용하고 정의된 루프 변수는 뒤로 남겨둡니다. 이전에 전역 네임스페이스에서 for 루프 변수를 명시적으로 정의한 경우에도 적용됩니다. 이 경우, 기존에 존재하는 변수를 다시 바인딩합니다.

- 파이썬 2.x와 파이썬 3.x의 인터프리터의 출력 결과의 차이는 다음의 [파이썬 3.0의 새로운 기능들](https://docs.python.org/3/whatsnew/3.0.html) 변경 로그에서 확인할 수 있습니다:

  > "리스트 컴프리헨션은 이제 `[... for var in item1, item2, ...]` 문법을 지원하지 않습니다. 대신 `[... for var in (item1, item2, ...)]`을 사용하세요. 또한 리스트 컴프리헨션은 다른 의미들을 가지고 있는점에 주목해야합니다: 그들은 `list()` 생성 표현식 생성자의 문법 설탕에 가깝고, 특히 루프 제어 변수들은 더 이상 범위 밖으로 유출되지 않습니다.

---

### ▶ 기본 가변인수를 조심하세요!

<!-- Example ID: 7d42dade-e20d-4a7b-9ed7-16fb58505fe9 --->

```py
def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg
```

**출력 결과:**

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

#### 💡 설명:

- 파이썬에서 함수의 기본 변경 가능한 인수는 함수가 호출될 때마다 실제로 초기화되지 않습니다. 대신, 최근에 할당된 값이 기본값으로 사용됩니다. `some_func`에 `[]`를 인수로 넘겨줄 때 `default_arg`의 기본값이 사용되지 않아 결과가 예상대로 나오게 됩니다.

  ```py
  def some_func(default_arg=[]):
      default_arg.append("some_string")
      return default_arg
  ```

  **출력 결과:**

  ```py
  >>> some_func.__defaults__ #이건 함수에 대한 기본 인수값을 보여줍니다
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

- 변경 가능한 인수로 인한 버그를 피하는 일반적인 방법으로는 기본값으로 `None`을 지정한 후에 해당 인수에 어떠한 값이 들어오는지 확인하는 것입니다. 예시:

  ```py
  def some_func(default_arg=None):
      if default_arg is None:
          default_arg = []
      default_arg.append("some_string")
      return default_arg
  ```

---

### ▶ 여러 예외들을 잡기

<!-- Example ID: b5ca5e6a-47b9-4f69-9375-cda0f8c6755d --->

```py
some_list = [1, 2, 3]
try:
    # ``IndexError``를 일으킵니다
    print(some_list[4])
except IndexError, ValueError:
    print("Caught!")

try:
    # ``ValueError``를 일으킵니다
    some_list.remove(4)
except IndexError, ValueError:
    print("Caught again!")
```

**출력 결과 (Python 2.x):**

```py
Caught!

ValueError: list.remove(x): x not in list
```

**출력 결과 (Python 3.x):**

```py
  File "<input>", line 3
    except IndexError, ValueError:
                     ^
SyntaxError: invalid syntax
```

#### 💡 설명

- 예외처리 구문에 여러 개의 예외를 처리하려면, 해당 예외들을 튜플로 묶어 첫 번째 인수로 넘겨줘야 합니다. 두 번째 인수는 선택적 이름으로, 주어진 경우 일어난 예외 인스턴스가 바인딩 됩니다. 예를 들어,

  ```py
  some_list = [1, 2, 3]
  try:
     # ``ValueError``를 일으킵니다
     some_list.remove(4)
  except (IndexError, ValueError), e:
     print("Caught again!")
     print(e)
  ```

  **출력 결과 (Python 2.x):**

  ```
  Caught again!
  list.remove(x): x not in list
  ```

  **출력 결과 (Python 3.x):**

  ```py
    File "<input>", line 4
      except (IndexError, ValueError), e:
                                       ^
  IndentationError: unindent does not match any outer indentation level
  ```

- 쉼표로 예외에서 변수를 분리하는 방법은 이제는 사용되지 않으며 파이썬 3에서는 작동하지 않습니다; 이 경우 `as`를 사용해야 합니다. 예를 들어,

  ```py
  some_list = [1, 2, 3]
  try:
      some_list.remove(4)

  except (IndexError, ValueError) as e:
      print("Caught again!")
      print(e)
  ```

  **출력 결과:**

  ```
  Caught again!
  list.remove(x): x not in list
  ```

---

### ▶ 같은 피연산자, 다른 이야기!

<!-- Example ID: ca052cdf-dd2d-4105-b936-65c28adc18a0 --->

1\.

```py
a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]
```

**출력 결과:**

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

**출력 결과:**

```py
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4, 5, 6, 7, 8]
```

#### 💡 설명:

- `a += b` 는 항상 `a = a + b`와 같게 동작하지 않습니다. 클래스는 _`op=`_ 연산자를 _다르게_ 구현할 수 있으며, 리스트는 다음과 같습니다.

- `a = a + [5,6,7,8]` 표현식은 새로운 리스트를 생성하여 새로운 리스트에 대한 `a`의 참조를 설정하므로, `b`는 바뀌지 않습니다.

- `a += [5,6,7,8]` 표현식은 실제로 `a`와 `b`가 여전히 내부에서 수정된 목록을 가리키도록 하는 "확장" 함수에 대치됩니다.

---

### ▶ 이름 확인은 클래스 범위를 무시합니다

<!-- Example ID: 03f73d96-151c-4929-b0a8-f74430788324 --->

1\.

```py
x = 5
class SomeClass:
    x = 17
    y = (x for i in range(10))
```

**출력 결과:**

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

**출력 결과 (Python 2.x):**

```py
>>> SomeClass.y[0]
17
```

**출력 결과 (Python 3.x):**

```py
>>> SomeClass.y[0]
5
```

#### 💡 설명

- 클래스 정의 내에서 중첩된 범위는 클래스 수준에서 바인딩 된 이름을 무시합니다.
- 생성 표현식은 자체적인 범위를 갖습니다.
- 파이썬 3.x부터는 리스트 컴프리헨션 또한 자체적인 범위를 갖습니다.

---

### ▶ 모래밭에서 바늘찾기 \*

<!-- Example ID: 52a199b1-989a-4b28-8910-dff562cebba9 --->

다음의 시나리오 중 하나 이상을 접해보지 못한 파이써니스트는 한 번도 만나본 적이 없습니다,

1\.

```py
x, y = (0, 1) if True else None, None
```

**출력 결과:**

```py
>>> x, y  # (0, 1)이 예상됩니다
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

**출력 결과:**

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

**출력 결과**

```py
>>> len(ten_words_list)
9
```

4\. 충분히 강하게 주장하지 않음

```py
a = "python"
b = "javascript"
```

**출력 결과:**

```py
# 실패 메세지가 있는 assert 구문.
>>> assert(a == b, "Both languages are different")
# AssertionError가 일어나지 않습니다
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

**출력 결과:**

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

**출력 결과:**

```py
>>> some_recursive_func([5, 0])
[0, 0]
>>> similar_recursive_func(5)
4
```

#### 💡 설명:

- 1번에서, 예상되는 동작에 대한 올바른 구문은 `x, y = (0, 1) if True else (None, None)`입니다.

- 2번에서, 예상되는 동작에 대한 올바른 구문은 `t = ('one',)` 또는 `t = 'one',` (콤마가 없음)입니다. 그렇지 않으면 인터프리터는 `t`를 `str`로 생각해 문자 별로 반복합니다.

- `()`은 특별한 토큰이며 빈 `tuple`을 의미합니다.

- 3번에서, 여러분들도 이미 알아 차렷겟지만, 리스트의 5번째 요소 (`"that"`)의 뒤에 콤마가 빠져있습니다. 그래서 암묵적인 문자열 리터럴의 연결에 의해,

  ```py
  >>> ten_words_list
  ['some', 'very', 'big', 'list', 'thatconsists', 'of', 'exactly', 'ten', 'words']
  ```

- 4번째 코드에서 `AssertionError`가 일어나지 않은 이유는 `a == b` 표현식이 아닌 전체 튜플을 비교하기 때문입니다. 다음의 코드에서 이를 해결할 수 있습니다.

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
  AssertionError: Values aren not equal
  ```

- 다섯 번째 코드에서, `list.append`, `dict.update`, `list.sort`또는 다른 것들과 같이 아이템의 순서/매핑 객체의 항목을 수정하는 대부분의 메소드입니다. 그 자리에서 객체를 수정한 후 `None`을 반환합니다. 이를 뒷받침하는 근거는 그 자리에서 연산을 시행할 수 있는 경우 객체의 사본을 만드는 것을 피해 성능을 향상하기 위함입니다. ([이것](http://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list)을 참조하였습니다)

- 마지막으로, `list`와 같은 가변 객체를 전달은 참조로 호출되는 반면, `int`와 같은 불변 객체는 값으로 호출됩니다.

- 이런 자잘한 것들까지 알고 있으면 장기적으로 디버깅 시간을 절약할 수 있습니다.

---

### ▶ 나눠봅시다 \*

<!-- Example ID: ec3168ba-a81a-4482-afb0-691f1cc8d65a --->

```py
>>> 'a'.split()
['a']

# 같은 결과입니다
>>> 'a'.split(' ')
['a']

# 하지만
>>> len(''.split())
0

# 이건 같지 않네요
>>> len(''.split(' '))
1
```

#### 💡 설명:

- 처음에는 split의 기본 구분자가 공백 한 칸 `' '`인 것처럼 보이지만, [문서](https://docs.python.org/2.7/library/stdtypes.html#str.split)에 따르면
  > sep 이 지정되지 않거나 None 이면, 다른 분할 알고리즘이 적용됩니다: 연속된 공백 문자는 단일한 구분자로 간주하고, 문자열이 선행이나 후행 공백을 포함해도 결과는 시작과 끝에 빈 문자열을 포함하지 않습니다. 결과적으로, 빈 문자열이나 공백만으로 구성된 문자열을 None 구분자로 나누면 [] 를 돌려줍니다.
  > sep 이 주어지면, 연속된 구분자는 묶이지 않고 빈 문자열을 구분하는 것으로 간주합니다 (예를 들어, '1,,2'.split(',') 는 ['1', '', '2'] 를 돌려줍니다). sep 인자는 여러 문자로 구성될 수 있습니다 (예를 들어, '1<>2<>3'.split('<>') 는 ['1', '2', '3'] 를 돌려줍니다). 지정된 구분자로 빈 문자열을 나누면 [''] 를 돌려줍니다.
- 다음 코드에서 앞뒤의 공백이 어떻게 처리되는지 알게 되면 명확해질 겁니다,
  ```py
  >>> ' a '.split(' ')
  ['', 'a', '']
  >>> ' a '.split()
  ['a']
  >>> ''.split(' ')
  ['']
  ```

---

### ▶ 제멋대로 가져오기 \*

<!-- Example ID: 83deb561-bd55-4461-bb5e-77dd7f411e1c --->
<!-- read-only -->

```py
# File: module.py

def some_weird_name_func_():
    print("works!")

def _another_weird_name_func():
    print("works!")

```

**출력 결과**

```py
>>> from module import *
>>> some_weird_name_func_()
"works!"
>>> _another_weird_name_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_another_weird_name_func' is not defined
```

#### 💡 설명:

- 와일드카드 import는 자주 사용하지 않는 것이 좋습니다. 와일드카드 import에 대해 명확한 첫 번째 이유는 언더스코어로 시작하는 이름이 import 되기 때문입니다. 이로 인해 런타임 중에 에러가 발생할 수 있습니다.
- 만약 `from ... import a, b, c` 문법을 사용한다면, `NameError`는 발생하지 않을 것입니다.
  ```py
  >>> from module import some_weird_name_func_, _another_weird_name_func
  >>> _another_weird_name_func()
  works!
  ```
- 만약 정말로 와일드카드 import가 사용하고 싶다면, 와일드카드 import를 할 때 사용할 수 있는 공용 객체가 들어 있는 리스트인 `__all__`을 모듈 내에 정의해야 합니다.

  ```py
  __all__ = ['_another_weird_name_func']

  def some_weird_name_func_():
      print("works!")

  def _another_weird_name_func():
      print("works!")
  ```

  **출력 결과**

  ```py
  >>> _another_weird_name_func()
  "works!"
  >>> some_weird_name_func_()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'some_weird_name_func_' is not defined
  ```

---

### ▶ 다 정렬되었나요? \*

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

#### 💡 설명:

- 파이썬에서 `sorted` 메소드는 항상 리스트를 반환하고, 리스트와 튜플의 비교는 항상 `False`를 반환합니다.

- ```py
  >>> [] == tuple()
  False
  >>> x = 7, 8, 9
  >>> type(x), type(sorted(x))
  (tuple, list)
  ```

- `sorted`와 달리 `reversed` 메소드는 반복자를 반환합니다. 왜 그럴까요? 왜냐하면 정렬은 반복자가 그 자리에서 변경되거나 추가적인 컨테이너(리스트)를 사용해야 하지만, 뒤집는 것은 단순히 끝 인덱스부터 처음까지 반복하면 되기 때문입니다.

- 따라서 `sorted(y) == sorted(y)`를 비교하는 동안에, 처음의 `sorted()`가 호출되면 `y`의 반복자를 소모하고, 다음의 호출에는 빈 리스트가 반환됩니다.

  ```py
  >>> x = 7, 8, 9
  >>> y = reversed(x)
  >>> sorted(y), sorted(y)
  ([7, 8, 9], [])
  ```

---

### ▶ 자정은 존재하지 않나요?

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

**출력 결과 (< 3.5):**

```py
('Time at noon is', datetime.time(12, 0))
```

자정은 출력되지 않습니다.

#### 💡 설명:

파이썬 3.5 이전에, `datetime.time` 객체의 불리언 값은 UTC 기준으로 자정을 나타내는 경우 `False`로 간주하였습니다. 이는 `if obj:` 구문을 사용하우 `obj`가 null 또는 "비어있음"인지 확인하는 경우 오류가 발생하기 쉽습니다.

---

---

## "숨겨진 보물들!" 단원

이 단원에는 저 같은 초보자들이 (더 이상은 아니지만) 대부분 모르고 있는 파이썬에 대한 덜 알려지고 흥미로운 것들이 몇 가지 포함되어있습니다.

### ▶ 파이썬, 날 날게해줄 수 있니?

<!-- Example ID: a92f3645-1899-4d50-9721-0031be4aec3f --->

자, 여기 있습니다

```py
import antigravity
```

**출력 결과:**
쉿... 이건 일급비밀이야.

#### 💡 설명:

- `antigravity` 모듈은 파이썬 개발자들이 추가한 몇 안 되는 이스터에그입니다.
- `import antigravity` 는 파이썬에 대한 [고전 XKCD 만화](https://xkcd.com/353)을 웹 브라우저에 띄워줍니다.
- 더 많은 것이 그 안에 있는데, **또 다른 이스터에그가 이스터에그 안에 있습니다**. [코드](https://github.com/python/cpython/blob/master/Lib/antigravity.py#L7-L17)를 보게 된다면, [XKCD의 geohashing 알고리즘](https://xkcd.com/426)을 구현하는 함수가 정의되어 있습니다.

---

### ▶ `goto`, 하지만 왜?

<!-- Example ID: 2aff961e-7fa5-4986-a18a-9e5894bd89fe --->

```py
from goto import goto, label
for i in range(9):
    for j in range(9):
        for k in range(9):
            print("I am trapped, please rescue!")
            if k == 2:
                goto .breakout # 깊게 중첩된 루프에서 탈출
label .breakout
print("Freedom!")
```

**출력 결과 (Python 2.3):**

```py
I am trapped, please rescue!
I am trapped, please rescue!
Freedom!
```

#### 💡 설명:

- 파이썬에 `goto`가 추가된 버전은 2004년 4월 1일에 만우절 장난으로 [발표](https://mail.python.org/pipermail/python-announce-list/2004-April/002982.html)되었습니다.
- 현재 버전의 파이썬은 이 모듈을 가지고 있지 않습니다.
- 비록 이것이 작동하지만, 사용하지 마십시오. 파이썬에는 `goto`가 존재하지 않는 [이유](https://docs.python.org/3/faq/design.html#why-is-there-no-goto)가 있습니다.

---

### ▶ 마음 단단히 먹으세요!

<!-- Example ID: 5c0c75f2-ddd9-4da3-ba49-c4be7ec39acf --->

만약 여러분이 파이썬에서 스코프를 나타내기 위해 공백을 사용하는 것을 좋아하지 않는 사람 중 한 명이라면, C-스타일의 {}을 가져와 사용할 수 있습니다.

```py
from __future__ import braces
```

**출력 결과:**

```py
  File "some_file.py", line 1
    from __future__ import braces
SyntaxError: not a chance
```

중괄호? 절대 안돼! 만약 이게 실망스럽다면 자바를 사용하세요. 또 하나 놀라운 것은 `__future__`모듈에서 발생한 `SyntaxError`가 [코드](https://github.com/python/cpython/blob/master/Lib/__future__.py)의 어디에 있는지 찾을 수 있나요?

#### 💡 설명:

- `__future__` 모듈은 일반적으로 미래의 파이썬 버전에서 추가될 기능을 제공합니다. 하지만 이 특정한 맥락에서 "미래"는 아이러니합니다.
- 이것은 이 문제에 대한 커뮤니티의 감정과 관련된 이스터에그입니다.
- 그 코드는 실제로 [여기](https://github.com/python/cpython/blob/025eb98dc0c1dc27404df6c544fc2944e0fa9f3a/Python/future.c#L49) `future.c` 파일 안에 존재합니다.
- CPython 컴파일러가 [future 구문](https://docs.python.org/3.3/reference/simple_stmts.html#future-statements)과 마주칠 때, 먼저 `future.c`에서 적절한 코드를 실행한 후 그걸 일반적인 구문으로 간주합니다.

---

### ▶ 평생 친근한 아저씨 같은 언어를 만나봅시다

<!-- Example ID: 6427fae6-e959-462d-85da-ce4c94ce41be --->

**출력 결과 (Python 3.x)**

```py
>>> from __future__ import barry_as_FLUFL
>>> "Ruby" != "Python" # 이건 의심할 여지가 없습니다
  File "some_file.py", line 1
    "Ruby" != "Python"
              ^
SyntaxError: invalid syntax

>>> "Ruby" <> "Python"
True
```

또 시작이군.

#### 💡 설명:

- 이것은 2009년 4월 1일에 출시된 [PEP-401](https://www.python.org/dev/peps/pep-0401/) 와 관련이 있습니다. (이제 여러분은 무엇을 의미하는지 알 것입니다)
- PEP-401의 일부를 인용하면

  > 파이선 3.0의 != 비항등 연산자는 손가락의 고통을 유발하는 끔직한 실수라는 것을 인지하고, FLUFL은 유일한 문법으로 <> 다이아몬드 연산자를 복구시켰습니다.

- 베리 아저씨가 PEP에서 공유한 것들은 더 많은데, [여기](https://www.python.org/dev/peps/pep-0401/) 서 읽을 수 있습니다.
- 이것은 대화형 환경에서는 잘 작동하지만, 파이썬 파일을 통해서는 `SyntaxError`를 일으킵니다. ([이 이슈](https://github.com/satwikkansal/wtfpython/issues/94)를 읽어보세요) 하지만, 여러분이 구분을 `eval`이나 `compile`으로 감싼다면 잘 작동할 것입니다.
  ```py
  from __future__ import barry_as_FLUFL
  print(eval('"Ruby" <> "Python"'))
  ```

---

### ▶ 파이썬 조차 사랑이 복잡하다는 것을 이해합니다

<!-- Example ID: b93cad9e-d341-45d1-999c-fcdce65bed25 --->

```py
import this
```

잠깐, **this**가 뭔가요? `this`는 사랑입니다 :heart:

**출력 결과:**

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

이것은 the Zen of Python 입니다!

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
>>> love is not True or False; love is love  # 사랑은 복잡합니다
True
```

#### 💡 설명:

- 파이썬의 `this` 모듈은 The Zen Of Python ([pep 20](https://www.python.org/dev/peps/pep-0020)) 을 위한 이스터에그입니다.
- 그리고 이게 아주 흥미롭다고 생각하면, [this.py](https://hg.python.org/cpython/file/c3896275c0f6/Lib/this.py)의 구현을 확인해보세요. 흥미롭게도, **the code for the Zen을 스스로 위반합니다** (그리고 아마도 유일하게 이런 일이 있는 곳입니다).
- `love is not True or False; love is love`라는 표현에 대해 아이러니하지만, 이것은 자기-설명적인 (그렇지 않다면, `is`와 `is not`에 관련된 예시를 봐주세요) 표현입니다.

---

### ▶ 네, 존재합니다!

<!-- Example ID: 4286db3d-1ea7-47c9-8fb6-a9a04cac6e49 --->

**반복문에 대한 `else` 조건**의 예로 다음과 같은게 있습니다:

```py
  def does_exists_num(l, to_find):
      for num in l:
          if num == to_find:
              print("Exists!")
              break
      else:
          print("Does not exist")
```

**출력 결과:**

```py
>>> some_list = [1, 2, 3, 4, 5]
>>> does_exists_num(some_list, 4)
Exists!
>>> does_exists_num(some_list, -1)
Does not exist
```

**예외 처리에 대한 `else` 조건**의 예는 다음과 같습니다,

```py
try:
    pass
except:
    print("Exception occurred!!!")
else:
    print("Try block executed successfully...")
```

**출력 결과:**

```py
Try block executed successfully...
```

#### 💡 설명:

- 모든 반복이 끝난 후 명시된 `break`가 없을 때, `else` 조건이 실행됩니다. "nobreak" 조건이라 생각할 수 있습니다.
- try 블록 뒤의 `else` 조건은 `try` 문에서 try 블록이 성공적으로 완료된 후 도달하므로 "완료 조건"이라고도 합니다.

---

### ▶ Ellipsis \*

<!-- Example ID: 969b7100-ab3d-4a7d-ad7d-a6be16181b2b --->

```py
def some_func():
    Ellipsis
```

**출력 결과**

```py
>>> some_func()
# 출력도 없고, 에러도 없다

>>> SomeRandomString
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'SomeRandomString' is not defined

>>> Ellipsis
Ellipsis
```

#### 💡 설명

- 파이썬에서, `Ellipsis`는 `...`에 해당하는 전역 내장 객체입니다.
  ```py
  >>> ...
  Ellipsis
  ```
- Ellipsis 는 여러가지 목적으로 사용될 수 있는데,

  - 아직 작성되지 않은 코드의 자리 표시자 (placeholder)로 사용될 수 있습니다 (`pass` 구문과 마찬가지로).
  - 슬라이스 문법에서 남은 방향의 전체 슬레이스를 나타낼 수 있습니다.

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

  우리의 `three_dimensional_array`는 배열의 배열의 배열입니다. 가장 안쪽 배열의 두번째 (1번 인덱스) 를 출력하고 싶다고 가정하면, 앞의 모든 차원을 생략하는데 Ellipsis를 사용할 수 있습니다.

  ```py
  >>> three_dimensional_array[:,:,1]
  array([[1, 3],
     [5, 7]])
  >>> three_dimensional_array[..., 1] # Ellipsis 사용.
  array([[1, 3],
     [5, 7]])
  ```

  참고: 이건 모든 차원에서 작동합니다. 여러분이 첫번째와 마지막 차원에서 슬라이스를 선택하고 중간의 값들을 무시하려면 이러한 방법이 있습니다. (`n_dimensional_array[firs_dim_slice, ..., last_dim_slice]`)

  - [타입 힌트](https://docs.python.org/3/library/typing.html) 에서는 파입의 일부만 나타내기 위해 사용합니다. (`(Callable[..., int]` 또는 `Tuple[str, ...]`))
  - Ellipsis를 기본 함수 인수로 ("인수가 전달되지 않음", "아무 값도 전달되지 않음"의 시나리오를 구분하기 위해) Ellipsis를 사용할 수 있습니다.

---

### ▶ Inpinity

<!-- Example ID: ff473ea8-a3b1-4876-a6f0-4378aff790c1 --->

철자는 의도된 것입니다. 이것에 대한 수정사항을 보내지 마세요.

**출력 결과 (Python 3.x):**

```py
>>> infinity = float('infinity')
>>> hash(infinity)
314159
>>> hash(float('-inf'))
-314159
```

#### 💡 설명:

- 무한대의 해시는 10⁵ x π 입니다.
- 흥미롭게도, 파이썬 3에서 `float('-inf')`의 해시는 "-10⁵ x π" 입니다. 반면에 파이썬 2에서는 "-10⁵ x e" 입니다.

---

### ▶ 망쳐봅시다

<!-- Example ID: 37146d2d-9e67-43a9-8729-3c17934b910c --->

1\.

```py
class Yo(object):
    def __init__(self):
        self.__honey = True
        self.bro = True
```

**출력 결과:**

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
        # 이번엔 대칭적으로 해봅시다
        self.__honey__ = True
        self.bro = True
```

**출력 결과:**

```py
>>> Yo().bro
True

>>> Yo()._Yo__honey__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Yo' object has no attribute '_Yo__honey__'
```

왜 `Yo()._Yo__honey`가 동작했을까요?

3\.

```py
_A__variable = "Some value"

class A(object):
    def some_func(self):
        return __variable # 아직 아무것도 초기화되지 않았습니다
```

**출력 결과:**

```py
>>> A().__variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__variable'

>>> A().some_func()
'Some value'
```

#### 💡 설명:

- [이름 망치기](https://en.wikipedia.org/wiki/Name_mangling) 는 서로 다른 네임스페이스 간의 이름이 충돌되는 것을 피하기 위해 사용됩니다.
- 파이썬에서, 인터프리터는 클래스 멤버의 이름 중 `__` (언더스코어 두개 또는 "dunder") 로 시작하고 앞에 `_NameOfTheClass`로 하나 이상의 언더스코어로 끝나지 않는 이름을 수정 (망치기) 합니다.
- 첫번째 코드에서 `__honey` 속성에 접근하기 위해 앞에 `_Yo`를 붙여야 했는데, 이는 다른 클래스에서 동일한 이름의 속성과 충돌되는 것을 막을 수 있습니다.
- 하지만 왜 두번쨰 코드는 작동하지 않을까요? 왜냐하면 이름 망치기가 이름 끝의 언더스코어 두개를 제거합니다.
- 세번째 코드또한 이름 망치기의 결과입니다. `return __variable` 구문의 `__variable`이 `_A_variable`로 바뀌었는데, 이는 우리가 스코프의 밖에서 선언한 변수의 이름이기도 합니다.
- 또한, 망친 이름이 255자보다 길어지면, 잘리게 될겁니다.

---

---

## "겉모습은 기만적입니다!" 단원

### ▶ 줄 건너뛰기?

<!-- Example ID: d50bbde1-fb9d-4735-9633-3444b9d2f417 --->

**출력 결과:**

```py
>>> value = 11
>>> valuе = 32
>>> value
11
```

뭐라고요?

**참고:** 이를 재현하는 가장 쉬운 방법은 위의 코드에서 구문을 복사해서 파일/셸에 붙여넣는 것입니다.

#### 💡 설명

일부 비-서양의 문자들은 영어의 알파벳과 똑같아 보이지만 인터프리터에 의해 별개의 것으로 여겨집니다.

```py
>>> ord('е') # 키릴 문자 'e' (Ye)
1077
>>> ord('e') # 라틴 문자 'e', 영어에 사용되고 표준 키보드를 사용하여 타이핑한 것
101
>>> 'е' == 'e'
False

>>> value = 42 # 라틴 문자 e
>>> valuе = 23 # 키릴 문자 'e', Python 2.x 인터프리터는 `SyntaxError`를 일으킵니다
>>> value
42
```

내장된 `ord()` 함수는 문자의 유니코드 [코드 포인트](https://en.wikipedia.org/wiki/Code_point) 를 반환하며, 키릴 문자 'e'와 라틴 문자 'e'의 다른 코드 위치는 예제의 동작이 옳음을 보여줍니다.

---

### ▶ 순간이동

<!-- Example ID: edafe923-0c20-4315-b6e1-0c31abfc38f5 --->

```py
# 먼저 `pip install numpy`를 하세요.
import numpy as np

def energy_send(x):
    # numpy 배열을 초기화합니다.
    np.array([float(x)])

def energy_receive():
    # 빈 numpy 배열을 반환합니다.
    return np.empty((), dtype=np.float).tolist()
```

**출력 결과:**

```py
>>> energy_send(123.456)
>>> energy_receive()
123.456
```

노벨상은 어디있나요?

#### 💡 설명:

- `energy_send` 함수에서 생성된 numpy 배열은 반환되지 않아 메모리 공간을 자유롭게 재할당할 수 있습니다.
- `numpy.empty()`는 다시 초기화하지 않고 다음에 사용 가능한 메모리 슬롯을 반환합니다. 이 메모리 위치는 막 풀려난 것과 같습니다. (보통 그러나, 항상 그렇지는 않습니다.)

---

### ▶ 음, 뭔가 수상한데...

<!-- Example ID: cb6a37c5-74f7-44ca-b58c-3b902419b362 --->

```py
def square(x):
    """
    숫자의 합으로 제곱을 구하는 간단한 함수.
    """
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
  return sum_so_far
```

**출력 결과 (Python 2.x):**

```py
>>> square(10)
10
```

100이 아니여야 하나요?

**참고:** 이걸 재현할 수 없는 경우 [mixed_tabs_and_spaces.py](/mixed_tabs_and_spaces.py)를 셸에서 실행해보세요.

#### 💡 설명

- **탭과 스페이스를 혼용하지 마세요!** 예제의 반환 직전에 있는 문자는 "탭"이며 다른 곳의 들여쓰기는 "4 스페이스"로 되어있습니다.
- 파이썬이 탭을 처리하는 방법입니다:

  > 탭은 왼쪽에서 오른쪽으로 1~8개의 공백으로 치환되며 치환된 항목을 포함하여 총 문자 수가 8의 배수가 되어야 합니다.

- 즉, `square` 함수의 마지막 줄에 있는 "탭"은 8개의 공백으로 바뀌어 루프 안으로 들어가게 됩니다.
- 파이썬 3는 그럴 때 자동으로 오류를 발생시킬 만큼 친절합니다.

  **출력 결과 (Python 3.x):**

  ```py
  TabError: inconsistent use of tabs and spaces in indentation
  ```

---

---

## "기타 등등" 단원

### ▶ `+=` 가 더 빨라요

<!-- Example ID: bfd19c60-a807-4a26-9598-4912b86ddb36 --->

```py
# 3개의 문자열을 "+"을 사용해서:
>>> timeit.timeit("s1 = s1 + s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.25748300552368164
# 3개의 문자열을 "+="을 사용해서:
>>> timeit.timeit("s1 += s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.012188911437988281
```

#### 💡 설명:

- `s1 += s2 + s3`에서 `s1`과 같은 첫 번째 문자열은 전체 문자열을 계산하는 동안에 파괴되지 않기 때문에 두 개 이상의 연결된 문자열에 대해서 `+=`가 `+` 보다 빠릅니다.

---

### ▶ 거대한 문자열을 만들어봐요!

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

**출력 결과:**

```py
# 더 좋은 가독성을 위해 %timeit을 사용하여 ipython shell에서 실행했습니다.
# 파이썬 shell/scriptm= 에서 timeit 모듈을 사용할 수 있습니다. 아래와 같은 방식입니다.
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

반복 횟수를 10배로 늘렸습니다.

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

#### 💡 설명

- [timeit](https://docs.python.org/3/library/timeit.html) 또는 [%timeit](https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-timeit)에 대해 더 읽을 수 있습니다. 그것들은 코드의 실행 시간을 측정하는 데 사용됩니다.
- 긴 문자열들을 생성하는데 `+` 을 사용하지 마세요. - 파이썬에서, `str` 은 변하지 않아서 좌우의 문자열들은 각각의 쌍들에 대해 새로운 문자열로 복사됩니다. 만약 길이 10의 문자열 4개를 연결한다면, 40개의 문자(character)만 복사하지 않고 (10+10) + ((10+10)+10) + (((10+10)+10)+10) = 90개의 문자(character)를 복사합니다. 문자열의 수와 길이가 증가함에 따라 상황은 이차적으로 악화합니다. (`add_bytes_with_plus` 함수로 실행 시간을 보였습니다.)
- 그러므로, `.format.` 또는 `%` 문법을 사용하는 것을 권고합니다. (하지만, 매우 짧은 문자열들의 경우 `+` 보다 약간 느립니다.)
- 더 좋은 방법으로, iterable 객체의 형태로 사용 가능한 콘텐츠가 있다면, 훨씬 더 빠른 `''.join(iterable_object)`을 사용할 수 있습니다.
- `add_bytes_with_plus`와 달리 앞의 예에서 보여준 `+=` 최적화로 인해 `add_string_with_plus`는 실행 시간이 이차적으로 증가하지 않습니다. `s += "xyz"` 대신 `s = s + "x" + "y" + "z"` 이였다면 실행 시간이 이차적으로 증가했을 겁니다.

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

- 거대한 문자열을 구성하고 만드는 많은 방법은 [Zen of Python](https://www.python.org/dev/peps/pep-0020/) 과 약간 대조적입니다. 이에 따르면,

  > 어떤 문제든지 해결할 하나의 - 가급적이면 유일한 - 명백한 방법이 존재해야 합니다.

---

### ▶ `dict` 검색 속도 느려지게 하기 *
<!-- Example ID: c9c26ce6-df0c-47f7-af0b-966b9386d4c3 --->
```py
some_dict = {str(i): 1 for i in range(1_000_000)}
another_dict = {str(i): 1 for i in range(1_000_000)}
```

**출력 결과:**
```py
>>> %timeit some_dict['5']
28.6 ns ± 0.115 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> some_dict[1] = 1
>>> %timeit some_dict['5']
37.2 ns ± 0.265 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

>>> %timeit another_dict['5']
28.5 ns ± 0.142 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> another_dict[1] # 존재하지 않는 키에 접근을 해볼까요
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> %timeit another_dict['5']
38.5 ns ± 0.0913 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```
왜 같은 검색의 속도가 느려질까요?

#### 💡 설명:
+ CPython은 모든 타입의 키 (`str`, `int`, 모든 오브젝트 ...)에 대해 일반적인 딕셔너리 검색 함수가 있고 흔한 경우인 `str` 키로만 이루어져 있는 딕셔너리에 대한 함수가 있습니다.
+ (CPython에서 이름이 `lookdict_unicode` [소스](https://github.com/python/cpython/blob/522691c46e2ae51faaad5bbbce7d959dd61770df/Objects/dictobject.c#L841)) 함수는 (검색하려는 키를 포함해서) 모든 키가 문자열 인것을 알고, `__eq__` 메소드를 호출하는 대신 빠르고 간단한 문자열 비교를 사용합니다.
+ `dict` 인스턴스가 처음으로 `str`이 아닌 키로 접근되었을 때, 추후 검색은 일반적인 함수를 사용하도록 수정됩니다.
+ 이 과정은 특정 `dict` 인스턴스에 대해서 되돌릴 수 없으며, 키가 딕셔너리 안에 없어도 작동합니다. 그래서 실패한 검색도 같은 효과를 가지게 된 것입니다.

### ▶ `dict` 인스턴스 부풀리기 \*

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

**출력 결과:** (파이썬 3.8, 다른 파이썬 3 버전은 조금 다를 수 있습니다.)

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

새로운 인터프리터에서 다시 시도해볼까요?:

```py
>>> o1 = SomeClass()
>>> o2 = SomeClass()
>>> dict_size(o1)
104  # 예상한 대로 나왔네요
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

무엇이 이 딕셔너리들을 부풀리게 했을까요? 그리고 왜 새롭게 생성된 객체도 부풀려질까요?

#### 💡 설명:

- CPython은 다양한 딕셔너리에서 같은 "키" 객체를 재사용할 수 있습니다.
이것은 특별히 키(인스턴스 속성)들이 주로 모든 인스턴스에서 비슷한 딕셔너리의 인스턴스의 메모리 사용량을 줄이기 위해서 [PEP 412](https://www.python.org/dev/peps/pep-0412/)에서 추가되었습니다.
- 이 최적화는 인스턴스 딕셔너리에는 원활히 적용되는데, 몇 몇 가정이 만족되지 않게 되면 작동하지 않습니다.
- 키를 공유하는 딕셔너리는 삭제를 지원하지 않습니다; 만약 어떤 인스턴스 속성이 삭제되었을 때, 그 딕셔너리는 "비공유"가 되고, 후의 그 클래스 인스턴스는 키를 공유하지 않게 됩니다.
- 추가로, (새로운 키가 삽입되어서) 딕셔너리의 키들의 크기가 조정되었다면, 그 키가 그 딕셔너리에서만 사용되었을 경우에만 계속 공유된 상태를 유지합니다 (이것은 `__init__`에서 인스턴스를 처음 만들 때 "비공유" 상태가 되지 않고 많은 속성을 추가할 수 있게 합니다).
만약 크기가 조정될 때 다양한 인스턴스가 존재하면, 키를 더 이상 공유하지 않게 되고 후의 그 클래스의 모든 인스턴스에 대해서 공유하지 않게 됩니다: CPython은 그 인스턴스가 같은 속성의 집합을 사용하는지 알 수 없게 되므로, 키를 공유하는 시도를 하지 않게 됩니다.
- 작은 팁으로, 만약 프로그램의 메모리 공간을 줄이고 싶다면: 인스턴스 속성을 지우지 말고, 꼭 모든 속성을 `__init__`에서 초기화 하세요!

---

### ▶ 사소한 것들 \*

<!-- Example ID: f885cb82-f1e4-4daa-9ff3-972b14cb1324 --->

- `join()` 은 리스트 연산이 아닌 문자열 연산입니다. (처음 보기에는 직관적이지 않습니다.)

  **💡 설명:** `join()`이 문자열의 메소드라면 모든 iterable 자료형 (리스트(list), 튜플(tuple), 반복자(iterators)) 에서 동작할 수 있습니다. 만약 리스트의 메소드라면 모든 타입에 대해 따로 정의해야 합니다. 또한, 일반적인 `list` 객체 API에 문자열 방식의 메소드를 붙이는 것은 별로 말이 되지 않습니다.

- 이상하게 보이지만 의미상 올바른 구문들:

  - `[] = ()` 은 의미상 올바른 구문입니다. (빈 `tuple`을 빈 `list` 안으로 풀어 넣습니다.(unpacking))
  - `'a'[0][0][0][0][0]` 은 파이썬에서 문자열들이 [sequences](https://docs.python.org/ko/3/glossary.html#term-sequence) (iterables 하고 인덱스로 요소에 접근이 가능합니다) 이므로 의미상 올바른 구문입니다.
  - `3 --0-- 5 == 8`과 `--5 == 5` 둘다 의미상 올바른 구문이며 결괏값은 `True`입니다.

- `a`을 숫자라고 고려할 때, `++a`와 `--a` 둘 다 파이썬에서 올바른 구문이지만 C, C++, 또는 Java 같은 언어에서 유사한 구문과는 같은 결과를 보이지 않습니다.

  ```py
  >>> a = 5
  >>> a
  5
  >>> ++a
  5
  >>> --a
  5
  ```

  **💡 설명:**

  - 파이썬 문법에는 `++` 연산자가 없습니다. 이것은 두 개의 `+` 연산자입니다.
  - `++a` 는 `+(+a)`로 분석되어 `a`가 됩니다. 마찬가지로 `--a` 도 올바른 구문입니다.
  - 이 StackOverflow [스레드](https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python)에서 파이썬에서 증가 및 감소 연산자가 없는 이유에 대한 토론을 확인할 수 있습니다.

- 파이썬의 Walrus 연산자에 대해 알고 있을 겁니다. 그런데 _space-invader 연산자_ 에 대해 들어보셨나요?
  ```py
  >>> a = 42
  >>> a -=- 1
  >>> a
  43
  ```
  다른 증가 연산자와 함께, 대체 증가 연산자로 사용됩니다.
  ```py
  >>> a +=+ 1
  >>> a
  >>> 44
  ```
  **💡 설명:** 이 장난은 [Raymond Hettinger's tweet](https://twitter.com/raymondh/status/1131103570856632321?lang=en) 에서 왔습니다. space-invader 연산자는 실제로 `a -= (-1)` 의 잘못된 형식입니다. `a = a - (- 1)`와 같습니다. `a += (+ 1)`도 비슷한 방식으로 적용됩니다.
- 파이썬은 문서화되지 않은 [converse implication](https://en.wikipedia.org/wiki/Converse_implication) 연산자를 가지고 있습니다.

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

  **💡 설명:** 만약 `False` 와 `True` 을 0과 1로 대체하고 계산을 해보면, 진리표는 converse implication 연산자와 같습니다. ([Source](https://github.com/cosmologicon/pywat/blob/master/explanation.md#the-undocumented-converse-implication-operator))

- 우리는 계속 연산자들을 말하고 있기 때문에, 행렬 곱셈을 위한 `@` 연산자도 있습니다. (걱정하지 마세요, 이번엔 진짜입니다).

  ```py
  >>> import numpy as np
  >>> np.array([2, 2, 2]) @ np.array([7, 8, 8])
  46
  ```

  **💡 설명:** 파이썬 3.5부터 `@` 연산자를 추가해 과학계를 염두에 두었습니다. 어떤 객체든 `__matmul__` 의 마법 메소드를 오버로드해 이 연산자의 행동을 정의할 수 있습니다.

- 파이썬 3.8 이상에서는 `f'{some_var=}` 와 같은 일반적인 f-string 구문을 사용하여 빠른 디버깅을 할 수 있습니다. 예를 들어,

  ```py
  >>> some_string = "wtfpython"
  >>> f'{some_string=}'
  "some_string='wtfpython'"
  ```

- 파이썬은 함수들의 지역 변수 저장소에 2바이트를 사용합니다. 이론적으로, 이것은 함수에서 65536개의 변수만 정의될 수 있는 것을 의미합니다. 하지만 파이썬에는 2^16개 이상의 변수 이름들을 저장하는 데 사용할 수 있는 유용한 해결책이 내장되어 있습니다. 다음 코드는 65536개 이상의 지역 변수가 정의되었을 때 스택에서 발생하는 상황을 보여줍니다. (주의: 이 코드는 약 2^18줄의 텍스트를 출력하므로, 준비하십시오!):

  ```py
  import dis
  exec("""
  def f():
     """ + """
     """.join(["X" + str(x) + "=" + str(x) for x in range(65539)]))

  f()

  print(dis.dis(f))
  ```

- 여러 파이썬 스레드들이 동시에 _파이썬 코드_ 를 실행하지 않습니다. (예, 제대로 들으셨습니다!) 여러 개의 스레드를 생성하여 파이썬 코드를 동시에 실행하도록 하는 것이 직관적으로 보일 수 있지만 파이썬의 [Global Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock) 때문에 당신이 만들고 실행시키는 스레드들은 같은 코어를 차례대로 동작하게 하는 것뿐입니다. 파이썬의 쓰레드는 IO-bound 작업에 적합하지만, CPU-bound 작업에서 병렬화를 달성하려면 [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) 모듈을 사용하는 것이 좋을 수 있습니다.

- 때때로, `print` 메소드는 값을 바로 출력하지 못할 수 있습니다. 예를 들어,

  ```py
  # File some_file.py
  import time

  print("wtfpython", end="_")
  time.sleep(3)
  ```

  출력 버퍼가 `\n` 에 도달한 후 또는 프로그램의 실행이 끝날 때 출력 버퍼가 플러시 되기 때문에 `end` 인자로 인하여 3초 뒤에 `wtfpython` 을 출력합니다. `flush=True` 인자를 전달하여 버퍼를 강제로 플러시 할 수도 있습니다.

- 범위를 벗어난 리스트 슬라이싱은 에러를 던지지 않습니다.

  ```py
  >>> some_list = [1, 2, 3, 4, 5]
  >>> some_list[111:]
  []
  ```

- iterable 을 슬라이싱 하면 항상 새로운 객체가 생성되는 것은 아닙니다. 예를 들어,

  ```py
  >>> some_str = "wtfpython"
  >>> some_list = ['w', 't', 'f', 'p', 'y', 't', 'h', 'o', 'n']
  >>> some_list is some_list[:] # False expected because a new object is created.
  False
  >>> some_str is some_str[:] # True because strings are immutable, so making a new object is of not much use.
  True
  ```

- 파이썬 3 에서 `int('١٢٣٤٥٦٧٨٩')` 는 `123456789` 을 반환합니다. 파이썬에서, 십진수 문자들에는 숫자 문자들과 십진법 숫자들을 형성하는데 사용될 수 있는 모든 문자가 포함됩니다, e.g. U+0660, ARABIC-INDIC DIGIT ZERO. 이 동작과 관련된 [interesting story](https://chris.improbable.org/2014/8/25/adventures-in-unicode-digits/) 입니다.

- 파이썬 3 이상에서는 더 나은 가독성을 위해 밑줄로 숫자 리터럴을 분리할 수 있습니다.

  ```py
  >>> six_million = 6_000_000
  >>> six_million
  6000000
  >>> hex_address = 0xF00D_CAFE
  >>> hex_address
  4027435774
  ```

- `'abc'.count('') == 4`. 다음은 더 명확하게 만들어 주는 `count` 메소드의 비슷한 구현입니다.
  ```py
  def count(s, sub):
      result = 0
      for i in range(len(s) + 1 - len(sub)):
          result += (s[i:i + len(sub)] == sub)
      return result
  ```
  이 동작은 원래 문자열에서 길이가 0인 슬라이스들에 빈 substring(`''`)이 일치하기 때문입니다.

---

---

# 기여하기

wtfpython에 기여할 수 있는 몇 가지 방법이 있어요,

- 새로운 예제들 추천
- 번역 돕기 ([issues labeled translation](https://github.com/satwikkansal/wtfpython/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation) 을 보세요.)
- 오래된 정보, 오타, 서식 오류 등의 작은 수정들
- 차이점들 식별 (불충분한 설명, 중복된 예제 등등.)
- 이 프로젝트를 더욱 재미있고 유용하게 만들기 위한 창의적인 제안들

더 많은 정보는 [CONTRIBUTING.md](/CONTRIBUTING.md)을는보세요. 자유롭게 새로운 [issue](https://github.com/satwikkansal/wtfpython/issues/new)를 만들어 토론해보세요.

추신: 역링크 요청으로 연락하지 마세요. 프로젝트와 관련이 높지 않으면 링크를 추가하지 않습니다.

# 감사의 말

이 항목들의 아이디어와 디자인은 Denys Dovhan's 의 멋진 프로젝트 [wtfjs](https://github.com/denysdovhan/wtfjs) 에서 영감을 받았습니다. Pythonista들의 압도적인 지지는 그것의 현재의 모습을 주었습니다.

#### 몇 개의 멋진 링크들!

- https://www.youtube.com/watch?v=sH4XF6pKKmk
- https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python
- https://sopython.com/wiki/Common_Gotchas_In_Python
- https://stackoverflow.com/questions/530530/python-2-x-gotchas-and-landmines
- https://stackoverflow.com/questions/1011431/common-pitfalls-in-python
- https://www.python.org/doc/humor/
- https://github.com/cosmologicon/pywat#the-undocumented-converse-implication-operator
- https://www.codementor.io/satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65
- https://github.com/wemake-services/wemake-python-styleguide/search?q=wtfpython&type=Issues
- WFTPython discussion threads on [Hacker News](https://news.ycombinator.com/item?id=21862073) and [Reddit](https://www.reddit.com/r/programming/comments/edsh3q/what_the_fck_python_30_exploring_and/).

# 🎓 License

[![WTFPL 2.0][license-image]][license-url]

&copy; [Satwik Kansal](https://satwikkansal.xyz)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square

## 친구들을 놀라게 해보세요!

만약 wtfpython이 마음에 드셨다면, 친구들에게 빠르게 공유하기 위한 퀵 링크들을 사용할 수 있어요.

[Twitter](https://twitter.com/intent/tweet?url=https://github.com/satwikkansal/wtfpython&text=If%20you%20really%20think%20you%20know%20Python,%20think%20once%20more!%20Check%20out%20wtfpython&hashtags=python,wtfpython) | [Linkedin](https://www.linkedin.com/shareArticle?url=https://github.com/satwikkansal&title=What%20the%20f*ck%20Python!&summary=If%20you%20really%20thing%20you%20know%20Python,%20think%20once%20more!) | [Facebook](https://www.facebook.com/dialog/share?app_id=536779657179021&display=page&href=https%3A%2F%2Fgithub.com%2Fsatwikkansal%2Fwtfpython&quote=If%20you%20really%20think%20you%20know%20Python%2C%20think%20once%20more!)

## Need a pdf version?

I've received a few requests for the pdf (and epub) version of wtfpython. You can add your details [here](https://satwikkansal.xyz/wtfpython-pdf/) to get them as soon as they are finished.

**That's all folks!** For upcoming content like this, you can add your email [here](https://www.satwikkansal.xyz/content-like-wtfpython/).
