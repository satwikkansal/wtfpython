<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="/images/logo_dark_theme.svg">
      <source media="(prefers-color-scheme: light)" srcset="/images/logo.svg">
      <img alt="Shows a wtfpython logo." src="/images/logo.svg">
    </picture>
</p>
<h1 align="center">What the f*ck Python! 😱</h1>
<p align="center">کاوش و درک پایتون از طریق تکه‌های کد شگفت‌انگیز.</p>


ترجمه‌ها: [انگلیسی English](https://github.com/satwikkansal/wtfpython) | [چینی 中文](https://github.com/leisurelicht/wtfpython-cn) | [ویتنامی Tiếng Việt](https://github.com/vuduclyunitn/wtfptyhon-vi) | [اسپانیایی Español](https://web.archive.org/web/20220511161045/https://github.com/JoseDeFreitas/wtfpython-es) | [کره‌ای 한국어](https://github.com/buttercrab/wtfpython-ko) | [روسی Русский](https://github.com/satwikkansal/wtfpython/tree/master/translations/ru-russian) | [آلمانی Deutsch](https://github.com/BenSt099/wtfpython) | [اضافه کردن ترجمه](https://github.com/satwikkansal/wtfpython/issues/new?title=Add%20translation%20for%20[LANGUAGE]&body=Expected%20time%20to%20finish:%20[X]%20weeks.%20I%27ll%20start%20working%20on%20it%20from%20[Y].)

حالت‌های دیگر: [وبسایت تعاملی](https://wtfpython-interactive.vercel.app) | [دفترچه تعاملی](https://colab.research.google.com/github/satwikkansal/wtfpython/blob/master/irrelevant/wtf.ipynb)


پایتون، یه زبان زیبا طراحی شده، سطح بالا و مبتنی بر مفسره که قابلیت‌های بسیاری برای راحتی ما برنامه‌نویس‌ها فراهم می‌کنه.
ولی گاهی اوقات قطعه‌کدهایی رو می‌بینیم که تو نگاه اول خروجی‌هاشون واضح نیست.

این یه پروژه باحاله که سعی داریم توش توضیح بدیم که پشت پرده یه سری قطعه‌کدهای غیرشهودی و فابلیت‌های کمتر شناخته شده پایتون
چه خبره.

درحالی که بعضی از مثال‌هایی که قراره تو این سند ببینید واقعا عجیب و غریب نیستند ولی بخش‌های جالبی از پایتون رو ظاهر می‌کنند که
ممکنه شما از وجودشون بی‌خبر باشید. به نظرم این شیوه جالبیه برای یادگیری جزئیات داخلی یه زبان برنامه نویسی و باور دارم که
برای شما هم جالب خواهد بود.

اگه شما یه پایتون کار سابقه‌دار هستید، می‌تونید از این فرصت به عنوان یه چالش برای خودتون استفاده کنید تا بیشتر مثال‌ها رو
تو تلاش اول حدس بزنید. ممکنه شما بعضی از این مثال‌ها رو قبلا تجربه کرده باشید و من خاطراتشون رو در این سند براتون زنده
کرده باشم! :sweat_smile:

پ.ن: اگه شما قبلا این سند رو خوندید، می‌تونید تغییرات جدید رو در بخش انتشار (فعلا در [اینجا](https://github.com/satwikkansal/wtfpython/)) مطالعه کنید
(مثال‌هایی که کنارشون علامت ستاره دارند، در آخرین ویرایش اضافه شده‌اند).

پس، بزن بریم...

# فهرست مطالب

<!-- Generated using "markdown-toc -i README.md --maxdepth 3"-->

<!-- toc -->

- [فهرست مطالب](#فهرست-مطالب)
- [ساختار مثال‌ها](#ساختار-مثالها)
- [استفاده](#استفاده)
- [👀 مثال‌ها](#-مثالها)
  - [بخش: ذهن خود را به چالش بکشید!](#بخش-ذهن-خود-را-به-چالش-بکشید)
    - [▶ اول از همه! \*](#-اول-از-همه-)
      - [💡 توضیحات](#-توضیحات)
    - [▶ بعضی وقت‌ها رشته‌ها می‌توانند دردسرساز شوند](#-بعضی-وقتها-رشتهها-میتوانند-دردسرساز-شوند)
      - [💡 Explanation:](#-explanation)
    - [▶ Be careful with chained operations](#-be-careful-with-chained-operations)
      - [💡 Explanation:](#-explanation-1)
    - [▶ How not to use `is` operator](#-how-not-to-use-is-operator)
      - [💡 Explanation:](#-explanation-2)
    - [▶ Hash brownies](#-hash-brownies)
      - [💡 Explanation](#-explanation-3)
    - [▶ Deep down, we're all the same.](#-deep-down-were-all-the-same)
      - [💡 Explanation:](#-explanation-4)
    - [▶ Disorder within order \*](#-disorder-within-order-)
      - [💡 Explanation:](#-explanation-5)
    - [▶ Keep trying... \*](#-keep-trying-)
      - [💡 Explanation:](#-explanation-6)
    - [▶ For what?](#-for-what)
      - [💡 Explanation:](#-explanation-7)
    - [▶ Evaluation time discrepancy](#-evaluation-time-discrepancy)
      - [💡 Explanation](#-explanation-8)
    - [▶ `is not ...` is not `is (not ...)`](#-is-not--is-not-is-not-)
      - [💡 Explanation](#-explanation-9)
    - [▶ A tic-tac-toe where X wins in the first attempt!](#-a-tic-tac-toe-where-x-wins-in-the-first-attempt)
      - [💡 Explanation:](#-explanation-10)
    - [▶ Schrödinger's variable \*](#-schrödingers-variable-)
      - [💡 Explanation:](#-explanation-11)
    - [▶ The chicken-egg problem \*](#-the-chicken-egg-problem-)
      - [💡 Explanation](#-explanation-12)
    - [▶ Subclass relationships](#-subclass-relationships)
      - [💡 Explanation:](#-explanation-13)
    - [▶ ‫ برابری و هویت متدها](#--برابری-و-هویت-متدها)
      - [💡 ‫ توضیحات](#--توضیحات)
    - [▶ ‫ آل-ترو-یشن \*](#--آل-ترو-یشن-)
      - [💡 Explanation:](#-explanation-14)
      - [💡 ‫ توضیح:](#--توضیح)
    - [▶ ‫ رشته‌ها و بک‌اسلش‌ها](#--رشتهها-و-بکاسلشها)
      - [💡 ‫ توضیح:](#--توضیح-1)
    - [▶ ‫ گره نیست، نَه!](#--گره-نیست-نَه)
      - [💡 Explanation:](#-explanation-15)
    - [▶ رشته‌های نیمه سه‌نقل‌قولی](#-رشتههای-نیمه-سهنقلقولی)
      - [💡 ‫ توضیح:](#--توضیح-2)
    - [▶ ‫ مشکل بولین ها چیست؟](#--مشکل-بولین-ها-چیست)
      - [💡 ‫ توضیحات:](#--توضیحات-1)
    - [▶ ‫ ویژگی‌های کلاس و ویژگی‌های نمونه](#--ویژگیهای-کلاس-و-ویژگیهای-نمونه)
      - [💡 ‫ توضیح:](#--توضیح-3)
    - [▶ yielding None](#-yielding-none)
      - [💡 Explanation:](#-explanation-16)
    - [▶ Yielding from... return! \*](#-yielding-from-return-)
      - [💡 ‫ توضیح:](#--توضیح-4)
    - [▶ ‫ بازتاب‌ناپذیری \*](#--بازتابناپذیری-)
      - [💡 توضیحات:](#-توضیحات-1)
    - [▶ ‫ تغییر دادن اشیای تغییرناپذیر!](#--تغییر-دادن-اشیای-تغییرناپذیر)
      - [💡 ‫ توضیحات:](#--توضیحات-2)
    - [▶ ‫ متغیری که از اسکوپ بیرونی ناپدید می‌شود](#--متغیری-که-از-اسکوپ-بیرونی-ناپدید-میشود)
      - [💡 ‫ توضیحات:](#--توضیحات-3)
    - [▶ ‫ تبدیل اسرارآمیز نوع کلید](#--تبدیل-اسرارآمیز-نوع-کلید)
      - [💡 ‫ توضیحات:](#--توضیحات-4)
    - [▶ ‫ ببینیم می‌توانید این را حدس بزنید؟](#--ببینیم-میتوانید-این-را-حدس-بزنید)
      - [💡 ‫ توضیح:](#--توضیح-5)
    - [▶ ‫ از حد مجاز برای تبدیل رشته به عدد صحیح فراتر می‌رود](#--از-حد-مجاز-برای-تبدیل-رشته-به-عدد-صحیح-فراتر-میرود)
      - [💡 ‫ توضیح:](#--توضیح-6)
  - [‫ بخش: شیب‌های لغزنده](#-بخش-شیبهای-لغزنده)
    - [▶ ‫ تغییر یک دیکشنری هنگام پیمایش روی آن](#--تغییر-یک-دیکشنری-هنگام-پیمایش-روی-آن)
      - [‫ 💡 توضیح:](#--توضیح-7)
    - [▶ عملیات سرسختانه‌ی `del`](#-عملیات-سرسختانهی-del)
      - [‫ 💡 توضیح:](#--توضیح-8)
    - [▶ ‫ متغیری که از حوزه خارج است](#--متغیری-که-از-حوزه-خارج-است)
      - [‫ 💡 توضیح:](#--توضیح-9)
    - [▶ ‫ حذف المان‌های لیست در حین پیمایش](#--حذف-المانهای-لیست-در-حین-پیمایش)
      - [💡 Explanation:](#-explanation-17)
    - [▶ ‫ زیپِ دارای اتلاف برای پیمایشگرها \*](#--زیپِ-دارای-اتلاف-برای-پیمایشگرها-)
      - [‫ 💡 توضیحات:](#--توضیحات-5)
    - [▶ ‫ نشت کردن متغیرهای حلقه!](#--نشت-کردن-متغیرهای-حلقه)
      - [💡 ‫ توضیحات:](#--توضیحات-6)
    - [▶ ‫ مراقب آرگومان‌های تغییرپذیر پیش‌فرض باشید!](#--مراقب-آرگومانهای-تغییرپذیر-پیشفرض-باشید)
      - [💡 ‫ توضیحات:](#--توضیحات-7)
    - [▶ ‫ گرفتن استثناها (Exceptions)](#--گرفتن-استثناها-exceptions)
      - [💡 ‫ توضیحات](#--توضیحات-8)
    - [▶ ‫ عملوندهای یکسان، داستانی متفاوت!](#--عملوندهای-یکسان-داستانی-متفاوت)
      - [💡 ‫ توضیحات:](#--توضیحات-9)
    - [▶ ‫ تفکیک نام‌ها با نادیده گرفتن حوزه‌ی کلاس](#--تفکیک-نامها-با-نادیده-گرفتن-حوزهی-کلاس)
      - [💡 ‫ توضیحات](#--توضیحات-10)
    - [▶ ‫ گرد کردن به روش بانکدار \*](#--گرد-کردن-به-روش-بانکدار-)
      - [💡 ‫ توضیحات:](#--توضیحات-11)
    - [▶ ‫ سوزن‌هایی در انبار کاه \*](#--سوزنهایی-در-انبار-کاه-)
      - [💡 ‫ توضیحات:](#--توضیحات-12)
    - [▶ ‫ تقسیم‌ها \*](#--تقسیمها-)
      - [💡 ‫ توضیحات:](#--توضیحات-13)
    - [▶ واردسازی‌های عمومی \*](#-واردسازیهای-عمومی-)
      - [💡 ‫ توضیحات:](#--توضیحات-14)
    - [▶ ‫ همه چیز مرتب شده؟ \*](#--همه-چیز-مرتب-شده-)
      - [💡 ‫ توضیحات:](#--توضیحات-15)
    - [▶ ‫ زمان نیمه‌شب وجود ندارد؟](#--زمان-نیمهشب-وجود-ندارد)
      - [💡 ‫ توضیحات:](#--توضیحات-16)
  - [‫ بخش: گنجینه‌های پنهان!](#-بخش-گنجینههای-پنهان)
    - [▶ ‫ خب پایتون، می‌توانی کاری کنی پرواز کنم؟](#--خب-پایتون-میتوانی-کاری-کنی-پرواز-کنم)
      - [‫ 💡 توضیح:](#--توضیح-10)
    - [▶ ‫ `goto`، ولی چرا؟](#--goto-ولی-چرا)
      - [‫ 💡 توضیح:](#--توضیح-11)
    - [▶ ‫ خودتان را آماده کنید!](#--خودتان-را-آماده-کنید)
      - [‫ 💡 توضیح:](#--توضیح-12)
    - [▶ ‫ بیایید با «عمو زبان مهربان برای همیشه» آشنا شویم](#--بیایید-با-عمو-زبان-مهربان-برای-همیشه-آشنا-شویم)
      - [‫ 💡 توضیح:](#--توضیح-13)
    - [▶ ‫ حتی پایتون هم می‌داند که عشق پیچیده است](#--حتی-پایتون-هم-میداند-که-عشق-پیچیده-است)
      - [‫ 💡 توضیح:](#--توضیح-14)
    - [▶ ‫ بله، این واقعاً وجود دارد!](#--بله-این-واقعاً-وجود-دارد)
      - [‫ 💡 توضیح:](#--توضیح-15)
    - [▶ Ellipsis \*](#-ellipsis-)
      - [‫ 💡توضیح](#-توضیح)
    - [▶ ‫ بی‌نهایت (`Inpinity`)](#--بینهایت-inpinity)
      - [‫ 💡 توضیح:](#--توضیح-16)
    - [▶ ‫ بیایید خرابکاری کنیم](#--بیایید-خرابکاری-کنیم)
      - [‫ 💡 توضیح:](#--توضیح-17)
  - [‫ بخش: ظاهرها فریبنده‌اند!](#-بخش-ظاهرها-فریبندهاند)
    - [▶ ‫ خطوط را رد می‌کند؟](#--خطوط-را-رد-میکند)
      - [‫ 💡 توضیح](#--توضیح-18)
    - [▶ ‫ تله‌پورت کردن](#--تلهپورت-کردن)
      - [‫ 💡 توضیح:](#--توضیح-19)
    - [▶ ‫ خب، یک جای کار مشکوک است...](#--خب-یک-جای-کار-مشکوک-است)
      - [‫ 💡 توضیح](#--توضیح-20)
  - [بخش: متفرقه](#بخش-متفرقه)
    - [‫ ▶ `+=` سریع‌تر است](#---سریعتر-است)
      - [‫  💡 توضیح:](#---توضیح)
    - [‫ ▶ بیایید یک رشته‌ی بزرگ بسازیم!](#--بیایید-یک-رشتهی-بزرگ-بسازیم)
      - [💡 توضیحات](#-توضیحات-2)
    - [▶ ‫  کُند کردن جستجوها در `dict` \*](#---کُند-کردن-جستجوها-در-dict-)
      - [‫  💡 توضیح:](#---توضیح-1)
    - [‫ ▶ حجیم کردن دیکشنری نمونه‌ها (`instance dicts`) \*](#--حجیم-کردن-دیکشنری-نمونهها-instance-dicts-)
      - [💡 توضیح:](#-توضیح-1)
    - [‫  ▶ موارد جزئی \*](#---موارد-جزئی-)
- [‫ مشارکت](#-مشارکت)
- [‫ تقدیر و تشکر](#-تقدیر-و-تشکر)
      - [‫ چند لینک جالب!](#-چند-لینک-جالب)
- [‫ 🎓 مجوز](#--مجوز)
  - [‫ دوستانتان را هم شگفت‌زده کنید!](#-دوستانتان-را-هم-شگفتزده-کنید)
  - [‫ آیا به یک نسخه pdf نیاز دارید؟](#-آیا-به-یک-نسخه-pdf-نیاز-دارید)

<!-- tocstop -->

# ساختار مثال‌ها

همه مثال‌ها به صورت زیر ساخته می‌شوند:

> ### ▶ یه اسم خوشگل
>
> ```py
> # راه اندازی کد
> # آماده سازی برای جادو...
> ```
>
> **خروجی (نسخه(های) پایتون):**
>
> ```py
> >>> triggering_statement
> یه خروجی غیرمنتظره
> ```
> (دلخواه): توضیح یک‌خطی خروجی غیرمنتظره
>
>
> #### 💡 توضیح:
>
> * توضیح کوتاه درمورد این‌که چی داره اتفاق میافته و چرا.
> ```py
> # راه اندازی کد
> # مثال‌های بیشتر برای شفاف سازی (در صورت نیاز)
> ```
> **خروجی (نسخه(های) پایتون):**
>
> ```py
> >>> trigger # یک مثال که رونمایی از جادو رو راحت‌تر می‌کنه
> # یک خروجی توجیه شده و واضح
> ```

**توجه:** همه مثال‌ها در برنامه مفسر تعاملی پایتون نسخه
۳.۵.۲ آزمایش شده‌اند و باید در همه نسخه‌های پایتون کار
کنند مگراینکه به صورت جداگانه و به طور واضح نسخه مخصوص
پایتون قبل از خروجی ذکر شده باشد.


# استفاده

یه راه خوب برای بیشتر بهره بردن، به نظرم، اینه که مثال‌ها رو به ترتیب متوالی بخونید و برای هر مثال:
- کد ابتدایی برای راه اندازی مثال رو با دقت بخونید. اگه شما یه پایتون کار سابقه‌دار باشید، با موفقیت بیشتر اوقات اتفاق بعدی رو پیش‌بینی می‌کنید.
- قطعه خروجی رو بخونید و
  + بررسی کنید که آیا خروجی‌ها همونطور که انتظار دارید هستند.
  + مطمئین بشید که دقیقا دلیل اینکه خروجی اون طوری هست رو می‌دونید.
    - اگه نمی‌دونید (که کاملا عادیه و اصلا بد نیست)، یک نفس عمیق بکشید و توضیحات رو بخونید (و اگه نفهمیدید، داد بزنید! و [اینجا](https://github.com/emargi/wtfpython/issues/new) درموردش حرف بزنید).
    - اگه می‌دونید، به افتخار خودتون یه دست محکم بزنید و برید سراغ مثال بعدی.
---

# 👀 مثال‌ها

## بخش: ذهن خود را به چالش بکشید!

### ▶ اول از همه! *

<!-- Example ID: d3d73936-3cf1-4632-b5ab-817981338863 -->
<!-- read-only -->

به دلایلی، عملگر "Walrus" (`:=`) که در نسخه ۳.۸ پایتون معرفی شد، خیلی محبوب شده. بیاید بررسیش کنیم.

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

>>> (a := "wtf_walrus") # ولی این کار می‌کنه
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

>>> a, b = 6, 9 # باز کردن معمولی
>>> a, b
(6, 9)
>>> (a, b = 16, 19) # آخ آخ
  File "<stdin>", line 1
    (a, b = 16, 19)
          ^
SyntaxError: invalid syntax

>>> (a, b := 16, 19) # این یه تاپل ۳تایی چاپ می‌کنه رو صفحه
(6, 16, 19)

>>> a # هنوز تغییر نکرده؟
6

>>> b
16
```



#### 💡 توضیحات

**مرور سریع بر عملگر Walrus**

عملگر Walrus همونطور که اشاره شد، در نسخه ۳.۸ پایتون معرفی
شد. این عملگر می‌تونه تو مقعیت‌هایی کاربردی باشه که شما می‌خواید داخل یه عبارت، مقادیری رو به متغیرها اختصاص بدید

```py
def some_func():
        # فرض کنید اینجا یک سری محاسبه سنگین انجام میشه
        # time.sleep(1000)
        return 5

# پس به جای اینکه این کارو بکنید:
if some_func():
        print(some_func()) # که خیلی راه نادرستیه چون محاسبه دوبار انجام میشه

# یا حتی این کارو کنید (که کار بدی هم نیست)
a = some_func()
if a:
    print(a)

# می‌تونید از این به بعد به طور مختصر بنویسید:
if a := some_func():
        print(a)

```

**خروجی (+۳.۸):**

```py
5
5
5
```

این باعث میشه که یک خط کمتر کد بزنیم و از دوبار فراخوندن `some_func` جلوگیری کرد.

- "عبارت اختصاص‌دادن مقدار" بدون پرانتز (نحوه استفاده عملگر Walrus)، در سطح بالا محدود است، `SyntaxError` در عبارت `a := "wtf_walrus"` در قطعه‌کد اول به همین دلیل است. قرار دادن آن داخل پرانتز، همانطور که می‌خواستیم کار کرد و مقدار را به `a` اختصاص داد.

- به طور معمول، قرار دادن عبارتی که دارای `=` است داخل پرانتز مجاز نیست. به همین دلیل ‍عبارت `(a, b = 6, 9)` به ما خطای سینتکس داد.

- قائده استفاده از عملگر Walrus به صورت `NAME:= expr` است، به طوری که `NAME` یک شناسه صحیح و `expr` یک عبارت صحیح است. به همین دلیل باز و بسته کردن با تکرار (iterable) پشتیبانی نمی‌شوند. پس،

  - عبارت `(a := 6, 9)` معادل عبارت `((a := 6), 9)` و در نهایت `(a, 9)` است. (که مقدار `a` عدد 6 است)

    ```py
    >>> (a := 6, 9) == ((a := 6), 9)
    True
    >>> x = (a := 696, 9)
    >>> x
    (696, 9)
    >>> x[0] is a # هر دو به یک مکان در حافظه دستگاه اشاره می‌کنند
    True
    ```

  - به طور مشابه، عبارت `(a, b := 16, 19)` معادل عبارت `(a, (b := 16), 19)` است که چیزی جز یک تاپل ۳تایی نیست.

---

### ▶ بعضی وقت‌ها رشته‌ها می‌توانند دردسرساز شوند

<!-- Example ID: 30f1d3fc-e267-4b30-84ef-4d9e7091ac1a --->
1\.

```py
>>> a = "some_string"
>>> id(a)
140420665652016
>>> id("some" + "_" + "string") # دقت کنید که هردو ID یکی هستند.
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
>>> a is b # همه‌ی نسخه‌ها به جز 3.7.x
True

>>> a = "wtf!"; b = "wtf!"
>>> a is b # ممکن است True یا False باشد بسته به جایی که آن را اجرا می‌کنید (python shell / ipython / به‌صورت اسکریپت)
False
```

```py
# این بار در فایل some_file.py
a = "wtf!"
b = "wtf!"
print(a is b)

# موقع اجرای ماژول، True را چاپ می‌کند!
```

4\.

**خروجی (< Python3.7 )**

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
<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="/images/string-intern/string_interning_dark_theme.svg">
      <source media="(prefers-color-scheme: light)" srcset="/images/string-intern/string_interning.svg">
      <img alt="Shows a string interning process." src="/images/string-intern/string_interning.svg">
    </picture>
</p>

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

As per https://docs.python.org/3/reference/expressions.html#comparisons

> Formally, if a, b, c, ..., y, z are expressions and op1, op2, ..., opN are comparison operators, then a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z, except that each expression is evaluated at most once.

While such behavior might seem silly to you in the above examples, it's fantastic with stuff like `a == b == c` and `0 <= x <= 100`.

* `False is False is False` is equivalent to `(False is False) and (False is False)`
* `True is False == False` is equivalent to `(True is False) and (False == False)` and since the first part of the statement (`True is False`) evaluates to `False`, the overall expression evaluates to `False`.
* `1 > 0 < 1` is equivalent to `(1 > 0) and (0 < 1)` which evaluates to `True`.
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
>>> a is b
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
* But why did the `is` operator evaluate to `False`? Let's see with this snippet.
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
- In the first case, `array_1` is bound to the new object `[1,2,3,4,5]` and since the `in` clause is evaluated at the declaration time it still refers to the old object `[1,2,3,4]` (which is not destroyed).
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

<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="/images/tic-tac-toe/after_row_initialized_dark_theme.svg">
      <source media="(prefers-color-scheme: light)" srcset="/images/tic-tac-toe/after_row_initialized.svg">
      <img alt="Shows a memory segment after row is initialized." src="/images/tic-tac-toe/after_row_initialized.svg">
    </picture>
</p>

And when the `board` is initialized by multiplying the `row`, this is what happens inside the memory (each of the elements `board[0]`, `board[1]` and `board[2]` is a reference to the same list referred by `row`)

<p align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="/images/tic-tac-toe/after_board_initialized_dark_theme.svg">
      <source media="(prefers-color-scheme: light)" srcset="/images/tic-tac-toe/after_board_initialized.svg">
      <img alt="Shows a memory segment after board is initialized." src="/images/tic-tac-toe/after_board_initialized.svg">
    </picture>
</p>

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
>>> from collections.abc import Hashable
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

### ▶ &#x202b; برابری و هویت متدها
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

&#x202b; **خروجی:**
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

&#x202b; با دوبار دسترسی به `classm`، یک شیء برابر دریافت می‌کنیم، اما *همان* شیء نیست؟ بیایید ببینیم
&#x202b; چه اتفاقی برای نمونه‌های `SomeClass` می‌افتد:

2.
```py
o1 = SomeClass()
o2 = SomeClass()
```

&#x202b; **خروجی:**
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

&#x202b; دسترسی به `classm` یا `method` دو بار، اشیایی برابر اما نه *یکسان* را برای همان نمونه از `SomeClass` ایجاد می‌کند.

#### 💡 &#x202b; توضیحات
* &#x202b; تابع‌ها [وصاف](https://docs.python.org/3/howto/descriptor.html) هستند. هر زمان که تابعی به عنوان یک ویژگی فراخوانی شود، وصف فعال می‌شود و یک شیء متد ایجاد می‌کند که تابع را به شیء صاحب آن ویژگی "متصل" می‌کند. اگر این متد فراخوانی شود، تابع را با ارسال ضمنی شیء متصل‌شده به عنوان اولین آرگومان صدا می‌زند (به این ترتیب است که `self` را به عنوان اولین آرگومان دریافت می‌کنیم، با وجود اینکه آن را به‌طور صریح ارسال نکرده‌ایم).
```py
>>> o1.method
<bound method SomeClass.method of <__main__.SomeClass object at ...>>
```
* &#x202b; دسترسی به ویژگی چندین بار، هر بار یک شیء متد جدید ایجاد می‌کند! بنابراین عبارت `o1.method is o1.method` هرگز درست (truthy) نیست. با این حال، دسترسی به تابع‌ها به عنوان ویژگی‌های کلاس (و نه نمونه) متد ایجاد نمی‌کند؛ بنابراین عبارت `SomeClass.method is SomeClass.method` درست است.
```py
>>> SomeClass.method
<function SomeClass.method at ...>
```
* &#x202b; `classmethod` توابع را به متدهای کلاس تبدیل می‌کند. متدهای کلاس وصاف‌هایی هستند که هنگام دسترسی، یک شیء متد ایجاد می‌کنند که به *کلاس* (نوع) شیء متصل می‌شود، نه خود شیء.
```py
>>> o1.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* &#x202b; برخلاف توابع، `classmethod`‌ها هنگام دسترسی به عنوان ویژگی‌های کلاس نیز یک شیء متد ایجاد می‌کنند (که در این حالت به خود کلاس متصل می‌شوند، نه نوع آن). بنابراین عبارت `SomeClass.classm is SomeClass.classm` نادرست (falsy) است.
```py
>>> SomeClass.classm
<bound method SomeClass.classm of <class '__main__.SomeClass'>>
```
* &#x202b; یک شیء متد زمانی برابر در نظر گرفته می‌شود که هم تابع‌ها برابر باشند و هم شیءهای متصل‌شده یکسان باشند. بنابراین عبارت `o1.method == o1.method` درست (truthy) است، هرچند که آن‌ها در حافظه شیء یکسانی نیستند.
* &#x202b; `staticmethod` توابع را به یک وصف "بدون عملیات" (no-op) تبدیل می‌کند که تابع را به همان صورت بازمی‌گرداند. هیچ شیء متدی ایجاد نمی‌شود، بنابراین مقایسه با `is` نیز درست (truthy) است.
```py
>>> o1.staticm
<function SomeClass.staticm at ...>
>>> SomeClass.staticm
<function SomeClass.staticm at ...>
```
* &#x202b; ایجاد شیءهای "متد" جدید در هر بار فراخوانی متدهای نمونه و نیاز به اصلاح آرگومان‌ها برای درج `self`، عملکرد را به شدت تحت تأثیر قرار می‌داد.
CPython 3.7 [این مشکل را حل کرد](https://bugs.python.org/issue26110) با معرفی opcodeهای جدیدی که فراخوانی متدها را بدون ایجاد شیء متد موقتی مدیریت می‌کنند. این به شرطی است که تابع دسترسی‌یافته واقعاً فراخوانی شود، بنابراین قطعه‌کدهای اینجا تحت تأثیر قرار نمی‌گیرند و همچنان متد ایجاد می‌کنند :)

### ▶ &#x202b; آل-ترو-یشن *

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

&#x202b; چرا این تغییر درست-نادرسته؟

#### 💡 Explanation:

- &#x202b; پیاده‌سازی تابع `all` معادل است با

- ```py
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```

- &#x202b; `all([])` مقدار `True` را برمی‌گرداند چون iterable خالی است.  
- &#x202b; `all([[]])` مقدار `False` را برمی‌گرداند چون آرایه‌ی داده‌شده یک عنصر دارد، یعنی `[]`، و در پایتون، لیست خالی مقدار falsy دارد.  
- &#x202b; `all([[[]]])` و نسخه‌های بازگشتی بالاتر همیشه `True` هستند. دلیلش این است که عنصر واحد آرایه‌ی داده‌شده (`[[...]]`) دیگر خالی نیست، و لیست‌هایی که دارای مقدار باشند، truthy در نظر گرفته می‌شوند.

---

### ▶ &#x202b; کاما‌ی شگفت‌انگیز
<!-- Example ID: 31a819c8-ed73-4dcc-84eb-91bedbb51e58 --->
&#x202b; **خروجی (< 3.6):**

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

#### 💡 &#x202b; توضیح:

- &#x202b; کامای انتهایی همیشه در لیست پارامترهای رسمی یک تابع در پایتون قانونی نیست.
- &#x202b; در پایتون، لیست آرگومان‌ها تا حدی با کاماهای ابتدایی و تا حدی با کاماهای انتهایی تعریف می‌شود. این تضاد باعث ایجاد موقعیت‌هایی می‌شود که در آن یک کاما در وسط گیر می‌افتد و هیچ قانونی آن را نمی‌پذیرد.
- &#x202b; **نکته:** مشکل کامای انتهایی در [پایتون ۳.۶ رفع شده است](https://bugs.python.org/issue9232). توضیحات در [این پست](https://bugs.python.org/issue9232#msg248399) به‌طور خلاصه کاربردهای مختلف کاماهای انتهایی در پایتون را بررسی می‌کند.

---

### ▶ &#x202b; رشته‌ها و بک‌اسلش‌ها
<!-- Example ID: 6ae622c3-6d99-4041-9b33-507bd1a4407b --->
&#x202b; **خروجی:**
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

#### 💡 &#x202b; توضیح:

- &#x202b; در یک رشته‌ی معمولی در پایتون، بک‌اسلش برای فرار دادن (escape) نویسه‌هایی استفاده می‌شود که ممکن است معنای خاصی داشته باشند (مانند تک‌نقل‌قول، دوتا‌نقل‌قول، و خودِ بک‌اسلش).
    ```py
    >>> "wt\"f"
    'wt"f'
    ```
- &#x202b; در یک رشته‌ی خام (raw string literal) که با پیشوند `r` مشخص می‌شود، بک‌اسلش‌ها خودشان به همان شکل منتقل می‌شوند، به‌همراه رفتار فرار دادن نویسه‌ی بعدی.
    ```py
    >>> r'wt\"f' == 'wt\\"f'
    True
    >>> print(repr(r'wt\"f'))
    'wt\\"f'

    >>> print("\n")

    >>> print(r"\\n")
    '\\n'
    ```
- &#x202b; در یک رشته‌ی خام (raw string) که با پیشوند `r` مشخص می‌شود، بک‌اسلش‌ها خودشان به همان صورت منتقل می‌شوند، همراه با رفتاری که کاراکتر بعدی را فرار می‌دهد (escape می‌کند).

---

### ▶ &#x202b; گره نیست، نَه!
<!-- Example ID: 7034deb1-7443-417d-94ee-29a800524de8 --->
```py
x = True
y = False
```

&#x202b; **خروجی:**
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

* &#x202b; تقدم عملگرها بر نحوه‌ی ارزیابی یک عبارت تأثیر می‌گذارد، و در پایتون، عملگر `==` تقدم بالاتری نسبت به عملگر `not` دارد.
* &#x202b; بنابراین عبارت `not x == y` معادل `not (x == y)` است که خودش معادل `not (True == False)` بوده و در نهایت به `True` ارزیابی می‌شود.
* &#x202b; اما `x == not y` یک `SyntaxError` ایجاد می‌کند، چون می‌توان آن را به صورت `(x == not) y` تفسیر کرد، نه آن‌طور که در نگاه اول انتظار می‌رود یعنی `x == (not y)`.
* &#x202b; تجزیه‌گر (parser) انتظار دارد که توکن `not` بخشی از عملگر `not in` باشد (چون هر دو عملگر `==` و `not in` تقدم یکسانی دارند)، اما پس از اینکه توکن `in` بعد از `not` پیدا نمی‌شود، خطای `SyntaxError` صادر می‌شود.

---

### ▶ رشته‌های نیمه سه‌نقل‌قولی
<!-- Example ID: c55da3e2-1034-43b9-abeb-a7a970a2ad9e --->
&#x202b; **خروجی:**
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

#### 💡 &#x202b; توضیح:
+ &#x202b; پایتون از الحاق ضمنی [رشته‌های متنی](https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation) پشتیبانی می‌کند. برای مثال،
  ```
  >>> print("wtf" "python")
  wtfpython
  >>> print("wtf" "") # or "wtf"""
  wtf
  ```
+ &#x202b; `'''` و `"""` نیز جداکننده‌های رشته‌ای در پایتون هستند که باعث ایجاد SyntaxError می‌شوند، چون مفسر پایتون هنگام اسکن رشته‌ای که با سه‌نقل‌قول آغاز شده، انتظار یک سه‌نقل‌قول پایانی به‌عنوان جداکننده را دارد.

---

### ▶ &#x202b; مشکل بولین ها چیست؟
<!-- Example ID: 0bba5fa7-9e6d-4cd2-8b94-952d061af5dd --->
1\.

```py
# یک مثال ساده برای شمردن تعداد مقادیر بولی و
# اعداد صحیح در یک iterable با انواع داده‌ی مخلوط.
mixed_list = [False, 1.0, "some_string", 3, True, [], False]
integers_found_so_far = 0
booleans_found_so_far = 0

for item in mixed_list:
    if isinstance(item, int):
        integers_found_so_far += 1
    elif isinstance(item, bool):
        booleans_found_so_far += 1
```

&#x202b; **خروجی:**
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

&#x202b; **خروجی (< 3.x):**

```py
>>> tell_truth()
I have lost faith in truth!
```



#### 💡 &#x202b; توضیحات:

* &#x202b; در پایتون، `bool` زیرکلاسی از `int` است
    
    ```py
    >>> issubclass(bool, int)
    True
    >>> issubclass(int, bool)
    False
    ```
    
* &#x202b; و بنابراین، `True` و `False` نمونه‌هایی از `int` هستند
  ```py
  >>> isinstance(True, int)
  True
  >>> isinstance(False, int)
  True
  ```

* &#x202b; مقدار عددی `True` برابر با `1` و مقدار عددی `False` برابر با `0` است.
  ```py
  >>> int(True)
  1
  >>> int(False)
  0
  ```

* &#x202b; این پاسخ در StackOverflow را ببینید: [answer](https://stackoverflow.com/a/8169049/4354153) برای توضیح منطقی پشت این موضوع.

* &#x202b; در ابتدا، پایتون نوع `bool` نداشت (کاربران از 0 برای false و مقادیر غیر صفر مثل 1 برای true استفاده می‌کردند). `True`، `False` و نوع `bool` در نسخه‌های 2.x اضافه شدند، اما برای سازگاری با نسخه‌های قبلی، `True` و `False` نمی‌توانستند به عنوان ثابت تعریف شوند. آن‌ها فقط متغیرهای توکار (built-in) بودند و امکان تغییر مقدارشان وجود داشت.

* &#x202b; پایتون ۳ با نسخه‌های قبلی ناسازگار بود، این مشکل سرانجام رفع شد، و بنابراین قطعه‌کد آخر در نسخه‌های Python 3.x کار نخواهد کرد!

---

### ▶ &#x202b; ویژگی‌های کلاس و ویژگی‌های نمونه
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
>>> A.x, B.x, C.x # C.x تغییر کرد, اما B.x تغییر نکرد.
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

&#x202b; **خروجی:**

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

#### 💡 &#x202b; توضیح:

* &#x202b; متغیرهای کلاس و متغیرهای نمونه‌های کلاس درونی به‌صورت دیکشنری‌هایی از شیء کلاس مدیریت می‌شوند. اگر نام متغیری در دیکشنری کلاس جاری پیدا نشود، کلاس‌های والد برای آن جست‌وجو می‌شوند.
* &#x202b; عملگر `+=` شیء قابل‌تغییر (mutable) را به‌صورت درجا (in-place) تغییر می‌دهد بدون اینکه شیء جدیدی ایجاد کند. بنابراین، تغییر ویژگی یک نمونه بر نمونه‌های دیگر و همچنین ویژگی کلاس تأثیر می‌گذارد.


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

&#x202b; **خروجی (> 3.3):**

```py
>>> list(some_func(3))
[]
```

&#x202b; چی شد که `"wtf"` ناپدید شد؟ آیا به خاطر اثر خاصی از `yield from` است؟ بیایید این موضوع را بررسی کنیم،

2\.

```py
def some_func(x):
    if x == 3:
        return ["wtf"]
    else:
        for i in range(x):
          yield i
```

&#x202b; **خروجی:**

```py
>>> list(some_func(3))
[]
```

&#x202b; همان نتیجه، این یکی هم کار نکرد.

#### 💡 &#x202b; توضیح:

+ &#x202b; از پایتون نسخه ۳.۳ به بعد، امکان استفاده از عبارت `return` همراه با مقدار در داخل ژنراتورها فراهم شد (نگاه کنید به [PEP380](https://www.python.org/dev/peps/pep-0380/)). [مستندات رسمی](https://www.python.org/dev/peps/pep-0380/#enhancements-to-stopiteration) می‌گویند:

> &#x202b; "... `return expr` در یک ژنراتور باعث می‌شود که هنگام خروج از ژنراتور، `StopIteration(expr)` ایجاد شود."

+ &#x202b; در حالت `some_func(3)`، استثنای `StopIteration` در ابتدای اجرا به دلیل وجود دستور `return` رخ می‌دهد. این استثنا به‌طور خودکار درون پوشش `list(...)` و حلقه `for` گرفته می‌شود. بنابراین، دو قطعه‌کد بالا منجر به یک لیست خالی می‌شوند.

+ &#x202b; برای اینکه مقدار `["wtf"]` را از ژنراتور `some_func` بگیریم، باید استثنای `StopIteration` را خودمان مدیریت کنیم،

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

### ▶ &#x202b; بازتاب‌ناپذیری *

<!-- Example ID: 59bee91a-36e0-47a4-8c7d-aa89bf1d3976 --->

1\.

```py
a = float('inf')
b = float('nan')
c = float('-iNf')  # این رشته‌ها نسبت به حروف بزرگ و کوچک حساس نیستند
d = float('nan')
```

&#x202b; **خروجی:**

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
>>> b == d # اما nan!=nan
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
>>> y is y # برابری هویتی برقرار است
True
>>> y == y #برابری در مورد y برقرار نیست
False
>>> [y] == [y] # اما برابری برای لیستی که شامل y است برقرار می‌شود
True
```



#### 💡 توضیحات:

- &#x202b; `'inf'` و `'nan'` رشته‌هایی خاص هستند (نسبت به حروف بزرگ و کوچک حساس نیستند) که وقتی به‌طور صریح به نوع `float` تبدیل شوند، به ترتیب برای نمایش "بی‌نهایت" ریاضی و "عدد نیست" استفاده می‌شوند.

- &#x202b; از آنجا که طبق استاندارد IEEE، `NaN != NaN`، پایبندی به این قانون فرض بازتاب‌پذیری (reflexivity) یک عنصر در مجموعه‌ها را در پایتون نقض می‌کند؛ یعنی اگر `x` عضوی از مجموعه‌ای مثل `list` باشد، پیاده‌سازی‌هایی مانند مقایسه، بر اساس این فرض هستند که `x == x`. به دلیل همین فرض، ابتدا هویت (identity) دو عنصر مقایسه می‌شود (چون سریع‌تر است) و فقط زمانی مقادیر مقایسه می‌شوند که هویت‌ها متفاوت باشند. قطعه‌کد زیر موضوع را روشن‌تر می‌کند،

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

  &#x202b; از آنجا که هویت‌های `x` و `y` متفاوت هستند، مقادیر آن‌ها در نظر گرفته می‌شوند که آن‌ها نیز متفاوت‌اند؛ بنابراین مقایسه این بار `False` را برمی‌گرداند.

- &#x202b; خواندنی جالب: [بازتاب‌پذیری و دیگر ارکان تمدن](https://bertrandmeyer.com/2010/02/06/reflexivity-and-other-pillars-of-civilization/)

---

### ▶ &#x202b; تغییر دادن اشیای تغییرناپذیر!

<!-- Example ID: 15a9e782-1695-43ea-817a-a9208f6bb33d --->

&#x202b; این موضوع ممکن است بدیهی به نظر برسد اگر با نحوه‌ی کار ارجاع‌ها در پایتون آشنا باشید.

```py
some_tuple = ("A", "tuple", "with", "values")
another_tuple = ([1, 2], [3, 4], [5, 6])
```

&#x202b; **خروجی:**
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

اما من فکر می‌کردم تاپل‌ها تغییرناپذیر هستند...

#### 💡 &#x202b; توضیحات:

* &#x202b; نقل‌قول از https://docs.python.org/3/reference/datamodel.html

    > &#x202b; دنباله‌های تغییرناپذیر  
        &#x202b; شیئی از نوع دنباله‌ی تغییرناپذیر، پس از ایجاد دیگر قابل تغییر نیست. (اگر شیء شامل ارجاع‌هایی به اشیای دیگر باشد، این اشیای دیگر ممکن است قابل تغییر باشند و تغییر کنند؛ اما مجموعه‌ی اشیایی که مستقیماً توسط یک شیء تغییرناپذیر ارجاع داده می‌شوند، نمی‌تواند تغییر کند.)

* &#x202b; عملگر `+=` لیست را به‌صورت درجا (in-place) تغییر می‌دهد. تخصیص به یک عضو کار نمی‌کند، اما زمانی که استثنا ایجاد می‌شود، عضو موردنظر پیش از آن به‌صورت درجا تغییر کرده است.
* &#x202b; همچنین توضیحی در [پرسش‌های متداول رسمی پایتون](https://docs.python.org/3/faq/programming.html#why-does-a-tuple-i-item-raise-an-exception-when-the-addition-works) وجود دارد.


---

### ▶ &#x202b; متغیری که از اسکوپ بیرونی ناپدید می‌شود
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
# &#x202b; چیزی چاپ نمی شود.
```

**Output (Python 3.x):**
```py
>>> print(e)
NameError: name 'e' is not defined
```

#### 💡 &#x202b; توضیحات:
* &#x202b; منبع: [مستندات رسمی پایتون](https://docs.python.org/3/reference/compound_stmts.html#except)

&#x202b; هنگامی که یک استثنا (Exception) با استفاده از کلمه‌ی کلیدی `as` به متغیری تخصیص داده شود، این متغیر در انتهای بلاکِ `except` پاک می‌شود. این رفتار مشابه کد زیر است:

  ```py
  except E as N:
      foo
  ```

  &#x202b; به این شکل ترجمه شده باشد:

  ```py
  except E as N:
      try:
          foo
      finally:
          del N
  ```

&#x202b; این بدان معناست که استثنا باید به نام دیگری انتساب داده شود تا بتوان پس از پایان بند `except` به آن ارجاع داد. استثناها پاک می‌شوند چون با داشتن «ردیابی» (traceback) ضمیمه‌شده، یک چرخه‌ی مرجع (reference cycle) با قاب پشته (stack frame) تشکیل می‌دهند که باعث می‌شود تمام متغیرهای محلی (locals) در آن قاب تا زمان پاکسازی حافظه (garbage collection) باقی بمانند.

* &#x202b; در پایتون، بندها (`clauses`) حوزه‌ی مستقل ندارند. در مثال بالا، همه‌چیز در یک حوزه‌ی واحد قرار دارد، و متغیر `e` در اثر اجرای بند `except` حذف می‌شود. این موضوع در مورد توابع صادق نیست، زیرا توابع حوزه‌های داخلی جداگانه‌ای دارند. مثال زیر این نکته را نشان می‌دهد:


     ```py
     def f(x):
         del(x)
         print(x)

     x = 5
     y = [5, 4, 3]
     ```

     &#x202b; **خروجی:**
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

* &#x202b; در پایتون نسخه‌ی ۲.x، نام متغیر `e` به یک نمونه از `Exception()` انتساب داده می‌شود، بنابراین وقتی سعی کنید آن را چاپ کنید، چیزی نمایش داده نمی‌شود.

    &#x202b; **خروجی (Python 2.x):**
    ```py
    >>> e
    Exception()
    >>> print e
    # چیزی چاپ نمی شود.
    ```

---


### ▶ &#x202b; تبدیل اسرارآمیز نوع کلید
<!-- Example ID: 00f42dd0-b9ef-408d-9e39-1bc209ce3f36 --->
```py
class SomeClass(str):
    pass

some_dict = {'s': 42}
```

&#x202b; **خروجی:**
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

#### 💡 &#x202b; توضیحات:

* &#x202b; هر دو شیء `s` و رشته‌ی `"s"` به دلیل ارث‌بری `SomeClass` از متد `__hash__` کلاس `str`، هش یکسانی دارند.
* &#x202b; عبارت `SomeClass("s") == "s"` به دلیل ارث‌بری `SomeClass` از متد `__eq__` کلاس `str` برابر با `True` ارزیابی می‌شود.
* &#x202b; از آنجا که این دو شیء هش یکسان و برابری دارند، به عنوان یک کلید مشترک در دیکشنری در نظر گرفته می‌شوند.
* &#x202b; برای رسیدن به رفتار دلخواه، می‌توانیم متد `__eq__` را در کلاس `SomeClass` بازتعریف کنیم.
  ```py
  class SomeClass(str):
    def __eq__(self, other):
        return (
            type(self) is SomeClass
            and type(other) is SomeClass
            and super().__eq__(other)
        )

    # &#x202b; هنگامی که متد __eq__ را به‌طور دلخواه تعریف می‌کنیم، پایتون دیگر متد __hash__ را به صورت خودکار به ارث نمی‌برد،
    # &#x202b; بنابراین باید متد __hash__ را نیز مجدداً تعریف کنیم.
    __hash__ = str.__hash__

  some_dict = {'s':42}
  ```

  &#x202b; **خروجی:**
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

### ▶ &#x202b; ببینیم می‌توانید این را حدس بزنید؟
<!-- Example ID: 81aa9fbe-bd63-4283-b56d-6fdd14c9105e --->
```py
a, b = a[b] = {}, 5
```

&#x202b; **خروجی:**
```py
>>> a
{5: ({...}, 5)}
```

#### 💡 &#x202b; توضیح:

* &#x202b; طبق [مرجع زبان پایتون](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)، دستورات انتساب فرم زیر را دارند:
  ```
  (target_list "=")+ (expression_list | yield_expression)
  ```
  و
  
> &#x202b; یک دستور انتساب ابتدا فهرست عبارت‌ها (expression list) را ارزیابی می‌کند (توجه کنید این عبارت می‌تواند یک عبارت تکی یا فهرستی از عبارت‌ها جداشده با ویرگول باشد که دومی به یک تاپل منجر می‌شود)، سپس شیء حاصل را به هریک از اهداف انتساب از **چپ به راست** تخصیص می‌دهد.

* &#x202b; علامت `+` در `(target_list "=")+` به این معناست که می‌توان **یک یا چند** هدف انتساب داشت. در این حالت، اهداف انتساب ما `a, b` و `a[b]` هستند (توجه کنید که عبارت ارزیابی‌شده دقیقاً یکی است، که در اینجا `{}` و `5` است).

* &#x202b; پس از ارزیابی عبارت، نتیجه از **چپ به راست** به اهداف انتساب داده می‌شود. در این مثال ابتدا تاپل `({}, 5)` به `a, b` باز می‌شود، بنابراین `a = {}` و `b = 5` خواهیم داشت.

* &#x202b; حالا `a` یک شیء قابل تغییر (mutable) است (`{}`).

* &#x202b; هدف انتساب بعدی `a[b]` است (شاید انتظار داشته باشید که اینجا خطا بگیریم زیرا پیش از این هیچ مقداری برای `a` و `b` مشخص نشده است؛ اما به یاد داشته باشید که در گام قبل به `a` مقدار `{}` و به `b` مقدار `5` دادیم).

* &#x202b; اکنون، کلید `5` در دیکشنری به تاپل `({}, 5)` مقداردهی می‌شود و یک مرجع دوری (Circular Reference) ایجاد می‌کند (علامت `{...}` در خروجی به همان شیئی اشاره دارد که قبلاً توسط `a` به آن ارجاع داده شده است). یک مثال ساده‌تر از مرجع دوری می‌تواند به این صورت باشد:
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
  &#x202b; در مثال ما نیز شرایط مشابه است (`a[b][0]` همان شیئی است که `a` به آن اشاره دارد).


* &#x202b; بنابراین برای جمع‌بندی، می‌توانید مثال بالا را به این صورت ساده کنید:
  ```py
  a, b = {}, 5
  a[b] = a, b
  ```
  &#x202b; و مرجع دوری به این دلیل قابل توجیه است که `a[b][0]` همان شیئی است که `a` به آن اشاره دارد.
  ```py
  >>> a[b][0] is a
  True
  ```


---

### ▶ &#x202b; از حد مجاز برای تبدیل رشته به عدد صحیح فراتر می‌رود
```py
>>> # Python 3.10.6
>>> int("2" * 5432)

>>> # Python 3.10.8
>>> int("2" * 5432)
```

&#x202b; **خروجی:**
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

#### 💡 &#x202b; توضیح:
&#x202b; فراخوانی تابع `int()` در نسخه‌ی Python 3.10.6 به‌خوبی کار می‌کند اما در نسخه‌ی Python 3.10.8 منجر به خطای `ValueError` می‌شود. توجه کنید که پایتون همچنان قادر به کار با اعداد صحیح بزرگ است. این خطا تنها هنگام تبدیل اعداد صحیح به رشته یا برعکس رخ می‌دهد.

&#x202b; خوشبختانه می‌توانید در صورت انتظار عبور از این حد مجاز، مقدار آن را افزایش دهید. برای انجام این کار می‌توانید از یکی از روش‌های زیر استفاده کنید:

- &#x202b; استفاده از فلگ خط فرمان `-X int_max_str_digits`
- &#x202b; تابع `set_int_max_str_digits()` از ماژول `sys`
- &#x202b; متغیر محیطی `PYTHONINTMAXSTRDIGITS`

&#x202b; برای جزئیات بیشتر درباره‌ی تغییر مقدار پیش‌فرض این حد مجاز، [مستندات رسمی پایتون](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits) را مشاهده کنید.


---


## &#x202b; بخش: شیب‌های لغزنده

### ▶ &#x202b; تغییر یک دیکشنری هنگام پیمایش روی آن
<!-- Example ID: b4e5cdfb-c3a8-4112-bd38-e2356d801c41 --->
```py
x = {0: None}

for i in x:
    del x[i]
    x[i+1] = None
    print(i)
```

&#x202b; **خروجی (پایتون 2.7تا پایتون 3.5):**

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

&#x202b; بله، دقیقاً **هشت** مرتبه اجرا می‌شود و سپس متوقف می‌شود.

#### &#x202b; 💡 توضیح:

- &#x202b; پیمایش روی یک دیکشنری در حالی که همزمان آن را ویرایش می‌کنید پشتیبانی نمی‌شود.
- &#x202b; هشت بار اجرا می‌شود چون در آن لحظه دیکشنری برای نگهداری کلیدهای بیشتر تغییر اندازه می‌دهد (ما هشت ورودی حذف داریم، بنابراین تغییر اندازه لازم است). این در واقع یک جزئیات پیاده‌سازی است.
- &#x202b; اینکه کلیدهای حذف‌شده چگونه مدیریت می‌شوند و چه زمانی تغییر اندازه اتفاق می‌افتد ممکن است در پیاده‌سازی‌های مختلف پایتون متفاوت باشد.
- &#x202b; بنابراین در نسخه‌های دیگر پایتون (به جز Python 2.7 - Python 3.5)، تعداد ممکن است متفاوت از ۸ باشد (اما هر چه که باشد، در هر بار اجرا یکسان خواهد بود). می‌توانید برخی مباحث پیرامون این موضوع را [اینجا](https://github.com/satwikkansal/wtfpython/issues/53) یا در این [رشته‌ی StackOverflow](https://stackoverflow.com/questions/44763802/bug-in-python-dict) مشاهده کنید.
- &#x202b; از نسخه‌ی Python 3.7.6 به بعد، در صورت تلاش برای انجام این کار، خطای `RuntimeError: dictionary keys changed during iteration` را دریافت خواهید کرد.

---

### ▶ عملیات سرسختانه‌ی `del`
<!-- Example ID: 777ed4fd-3a2d-466f-95e7-c4058e61d78e --->
<!-- read-only -->

```py
class SomeClass:
    def __del__(self):
        print("Deleted!")
```

&#x202b; **خروجی:**
1\.
```py
>>> x = SomeClass()
>>> y = x
>>> del x # باید این عبارت را چاپ کند "Deleted!"
>>> del y
Deleted!
```

&#x202b; «خُب، بالاخره حذف شد.» احتمالاً حدس زده‌اید چه چیزی جلوی فراخوانی `__del__` را در اولین تلاشی که برای حذف `x` داشتیم، گرفته بود. بیایید مثال را پیچیده‌تر کنیم.

2\.
```py
>>> x = SomeClass()
>>> y = x
>>> del x
>>> y # بررسی وجود y
<__main__.SomeClass instance at 0x7f98a1a67fc8>
>>> del y # مثل قبل، باید این عبارت را چاپ کند "Deleted!"
>>> globals() # اوه، چاپ نکرد. بیایید مقادیر گلوبال را بررسی کنیم.
Deleted!
{'__builtins__': <module '__builtin__' (built-in)>, 'SomeClass': <class __main__.SomeClass at 0x7f98a1a5f668>, '__package__': None, '__name__': '__main__', '__doc__': None}
```

&#x202b; «باشه، حالا حذف شد» :confused:

#### &#x202b; 💡 توضیح:
- &#x202b; عبارت `del x` مستقیماً باعث فراخوانی `x.__del__()` نمی‌شود.
- &#x202b; وقتی به دستور `del x` می‌رسیم، پایتون نام `x` را از حوزه‌ی فعلی حذف کرده و شمارنده‌ی مراجع شیٔ‌ای که `x` به آن اشاره می‌کرد را یک واحد کاهش می‌دهد. فقط وقتی شمارنده‌ی مراجع شیٔ به صفر برسد، تابع `__del__()` فراخوانی می‌شود.
- &#x202b; در خروجی دوم، متد `__del__()` فراخوانی نشد چون دستور قبلی (`>>> y`) در مفسر تعاملی یک ارجاع دیگر به شیٔ ایجاد کرده بود (به صورت خاص، متغیر جادویی `_` به مقدار آخرین عبارت غیر `None` در REPL اشاره می‌کند). بنابراین مانع از رسیدن شمارنده‌ی مراجع به صفر در هنگام اجرای `del y` شد.
- &#x202b; فراخوانی `globals` (یا هر چیزی که نتیجه‌اش `None` نباشد) باعث می‌شود که `_` به نتیجه‌ی جدید اشاره کند و ارجاع قبلی از بین برود. حالا شمارنده‌ی مراجع به صفر می‌رسد و عبارت «Deleted!» (حذف شد!) نمایش داده می‌شود.

---

### ▶ &#x202b; متغیری که از حوزه خارج است
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

&#x202b; **خروجی:**
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

#### &#x202b; 💡 توضیح:
* &#x202b; وقتی در محدوده (Scope) یک تابع به متغیری مقداردهی می‌کنید، آن متغیر در همان حوزه محلی تعریف می‌شود. بنابراین `a` در تابع `another_func` تبدیل به متغیر محلی می‌شود، اما پیش‌تر در همان حوزه مقداردهی نشده است، و این باعث خطا می‌شود.
* &#x202b; برای تغییر متغیر سراسری `a` در تابع `another_func`، باید از کلیدواژه‌ی `global` استفاده کنیم.
  ```py
  def another_func()
      global a
      a += 1
      return a
  ```

  **خروجی:**
  ```py
  >>> another_func()
  2
  ```
* &#x202b; در تابع `another_closure_func`، متغیر `a` در حوزه‌ی `another_inner_func` محلی می‌شود ولی پیش‌تر در آن حوزه مقداردهی نشده است. به همین دلیل خطا می‌دهد.
* &#x202b; برای تغییر متغیر حوزه‌ی بیرونی `a` در `another_inner_func`، باید از کلیدواژه‌ی `nonlocal` استفاده کنیم. دستور `nonlocal` به مفسر می‌گوید که متغیر را در نزدیک‌ترین حوزه‌ی بیرونی (به‌جز حوزه‌ی global) جستجو کند.
  ```py
  def another_func():
      a = 1
      def another_inner_func():
          nonlocal a
          a += 1
          return a
      return another_inner_func()
  ```

  &#x202b; **خروجی:**
  ```py
  >>> another_func()
  2
  ```
* &#x202b; کلیدواژه‌های `global` و `nonlocal` به مفسر پایتون می‌گویند که متغیر جدیدی را تعریف نکند و به جای آن در حوزه‌های بیرونی (سراسری یا میانجی) آن را بیابد.
* &#x202b; برای مطالعه‌ی بیشتر در مورد نحوه‌ی کار فضای نام‌ها و مکانیزم تعیین حوزه‌ها در پایتون، می‌توانید این [مقاله کوتاه ولی عالی](https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html) را بخوانید.

---

### ▶ &#x202b; حذف المان‌های لیست در حین پیمایش
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

&#x202b;**خروجی:**
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

&#x202b; می‌توانید حدس بزنید چرا خروجی `[2, 4]` است؟

#### 💡 Explanation:

* &#x202b; هیچ‌وقت ایده‌ی خوبی نیست که شیئی را که روی آن پیمایش می‌کنید تغییر دهید. روش درست این است که روی یک کپی از آن شیء پیمایش کنید؛ در این‌جا `list_3[:]` دقیقاً همین کار را می‌کند.

     ```py
     >>> some_list = [1, 2, 3, 4]
     >>> id(some_list)
     139798789457608
     >>> id(some_list[:]) # دقت کنید که پایتون برای اسلایس کردن، یک شی جدید میسازد
     139798779601192
     ```

&#x202b; **تفاوت بین `del`، `remove` و `pop`:**
* &#x202b; `del var_name` فقط اتصال `var_name` را از فضای نام محلی یا سراسری حذف می‌کند (به همین دلیل است که `list_1` تحت تأثیر قرار نمی‌گیرد).
* &#x202b; متد `remove` اولین مقدار مطابق را حذف می‌کند، نه یک اندیس خاص را؛ اگر مقدار مورد نظر پیدا نشود، خطای `ValueError` ایجاد می‌شود.
* &#x202b; متد `pop` عنصری را در یک اندیس مشخص حذف کرده و آن را برمی‌گرداند؛ اگر اندیس نامعتبری مشخص شود، خطای `IndexError` ایجاد می‌شود.

&#x202b; **چرا خروجی `[2, 4]` است؟**
- &#x202b; پیمایش لیست به صورت اندیس به اندیس انجام می‌شود، و هنگامی که عدد `1` را از `list_2` یا `list_4` حذف می‌کنیم، محتوای لیست به `[2, 3, 4]` تغییر می‌کند. در این حالت عناصر باقی‌مانده به سمت چپ جابه‌جا شده و جایگاهشان تغییر می‌کند؛ یعنی عدد `2` در اندیس 0 و عدد `3` در اندیس 1 قرار می‌گیرد. از آنجا که در مرحله بعدی حلقه به سراغ اندیس 1 می‌رود (که اکنون مقدار آن `3` است)، عدد `2` به طور کامل نادیده گرفته می‌شود. این اتفاق مشابه برای هر عنصر یک‌درمیان در طول پیمایش لیست رخ خواهد داد.

* &#x202b; برای توضیح بیشتر این مثال، این [تاپیک StackOverflow](https://stackoverflow.com/questions/45946228/what-happens-when-you-try-to-delete-a-list-element-while-iterating-over-it) را ببینید.
* &#x202b; همچنین برای نمونه مشابهی مربوط به دیکشنری‌ها در پایتون، این [تاپیک مفید StackOverflow](https://stackoverflow.com/questions/45877614/how-to-change-all-the-dictionary-keys-in-a-for-loop-with-d-items) را ببینید.

---


### ▶ &#x202b; زیپِ دارای اتلاف برای پیمایشگرها *
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
&#x202b; عنصر `3` از لیست `numbers` چه شد؟

#### &#x202b; 💡 توضیحات:

- &#x202b; بر اساس [مستندات](https://docs.python.org/3.3/library/functions.html#zip) پایتون، پیاده‌سازی تقریبی تابع `zip` به شکل زیر است:
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
- &#x202b; بنابراین این تابع تعداد دلخواهی از اشیای قابل پیمایش (*iterable*) را دریافت می‌کند، و با فراخوانی تابع `next` روی آن‌ها، هر یک از عناصرشان را به لیست `result` اضافه می‌کند. این فرایند زمانی متوقف می‌شود که اولین پیمایشگر به انتها برسد.
- &#x202b; نکته مهم اینجاست که هر زمان یکی از پیمایشگرها به پایان برسد، عناصر موجود در لیست `result` نیز دور ریخته می‌شوند. این دقیقاً همان اتفاقی است که برای عدد `3` در `numbers_iter` رخ داد.
- &#x202b; روش صحیح برای انجام عملیات بالا با استفاده از تابع `zip` چنین است:
    ```py
    >>> numbers = list(range(7))
    >>> numbers_iter = iter(numbers)
    >>> list(zip(first_three, numbers_iter))
    [(0, 0), (1, 1), (2, 2)]
    >>> list(zip(remaining, numbers_iter))
    [(3, 3), (4, 4), (5, 5), (6, 6)]
    ```
    &#x202b; اولین آرگومانِ تابع `zip` باید پیمایشگری باشد که کمترین تعداد عنصر را دارد.

---

### ▶ &#x202b; نشت کردن متغیرهای حلقه!
<!-- Example ID: ccec7bf6-7679-4963-907a-1cd8587be9ea --->
1\.
```py
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')
```

&#x202b; **خروجی:**
```py
6 : for x inside loop
6 : x in global
```

&#x202b; اما متغیر `x` هرگز خارج از محدوده (scope) حلقه `for` تعریف نشده بود...

2\.
```py
# این دفعه، مقدار ایکس را در ابتدا مقداردهی اولیه میکنیم.
x = -1
for x in range(7):
    if x == 6:
        print(x, ': for x inside loop')
print(x, ': x in global')
```

&#x202b; **خروجی:**
```py
6 : for x inside loop
6 : x in global
```

3\.

&#x202b; **خروجی (Python 2.x):**
```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
4
```

&#x202b; **خروجی (Python 3.x):**
```py
>>> x = 1
>>> print([x for x in range(5)])
[0, 1, 2, 3, 4]
>>> print(x)
1
```

#### 💡 &#x202b; توضیحات:

- &#x202b; در پایتون، حلقه‌های `for` از حوزه (*scope*) فعلی که در آن قرار دارند استفاده می‌کنند و متغیرهای تعریف‌شده در حلقه حتی بعد از اتمام حلقه نیز باقی می‌مانند. این قاعده حتی در مواردی که متغیر حلقه پیش‌تر در فضای نام سراسری (*global namespace*) تعریف شده باشد نیز صدق می‌کند؛ در چنین حالتی، متغیر موجود مجدداً به مقدار جدید متصل می‌شود.

- &#x202b; تفاوت‌های موجود در خروجی مفسرهای Python 2.x و Python 3.x در مثال مربوط به «لیست‌های ادراکی» (*list comprehension*) به دلیل تغییراتی است که در مستند [«تغییرات جدید در Python 3.0»](https://docs.python.org/3/whatsnew/3.0.html) آمده است:

    > &#x202b; «لیست‌های ادراکی دیگر فرم نحوی `[... for var in item1, item2, ...]` را پشتیبانی نمی‌کنند و به جای آن باید از `[... for var in (item1, item2, ...)]` استفاده شود. همچنین توجه داشته باشید که لیست‌های ادراکی در Python 3.x معنای متفاوتی دارند: آن‌ها از لحاظ معنایی به بیان ساده‌تر، مشابه یک عبارت تولیدکننده (*generator expression*) درون تابع `list()` هستند و در نتیجه، متغیرهای کنترل حلقه دیگر به فضای نام بیرونی نشت نمی‌کنند.»

---

### ▶ &#x202b; مراقب آرگومان‌های تغییرپذیر پیش‌فرض باشید!
<!-- Example ID: 7d42dade-e20d-4a7b-9ed7-16fb58505fe9 --->

```py
def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg
```

&#x202b; **خروجی:**
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

#### 💡 &#x202b; توضیحات:

- &#x202b; آرگومان‌های تغییرپذیر پیش‌فرض در توابع پایتون، هر بار که تابع فراخوانی می‌شود مقداردهی نمی‌شوند؛ بلکه مقداردهی آنها تنها یک بار در زمان تعریف تابع انجام می‌شود و مقدار اختصاص‌یافته به آن‌ها به عنوان مقدار پیش‌فرض برای فراخوانی‌های بعدی استفاده خواهد شد. هنگامی که به صراحت مقدار `[]` را به عنوان آرگومان به `some_func` ارسال کردیم، مقدار پیش‌فرض برای متغیر `default_arg` مورد استفاده قرار نگرفت، بنابراین تابع همان‌طور که انتظار داشتیم عمل کرد.

    ```py
    def some_func(default_arg=[]):
        default_arg.append("some_string")
        return default_arg
    ```

    &#x202b; **خروجی:**
    ```py
    >>> some_func.__defaults__ # مقادیر پیشفرض این تابع را نمایش می دهد.
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

- &#x202b; یک روش رایج برای جلوگیری از باگ‌هایی که به دلیل آرگومان‌های تغییرپذیر رخ می‌دهند، این است که مقدار پیش‌فرض را `None` قرار داده و سپس درون تابع بررسی کنیم که آیا مقداری به آن آرگومان ارسال شده است یا خیر. مثال:

    ```py
    def some_func(default_arg=None):
        if default_arg is None:
            default_arg = []
        default_arg.append("some_string")
        return default_arg
    ```

---

### ▶ &#x202b; گرفتن استثناها (Exceptions)
<!-- Example ID: b5ca5e6a-47b9-4f69-9375-cda0f8c6755d --->
```py
some_list = [1, 2, 3]
try:
    # &#x202b; این باید یک `IndexError` ایجاد کند
    print(some_list[4])
except IndexError, ValueError:
    print("Caught!")

try:
    # &#x202b; این باید یک `ValueError` ایجاد کند
    some_list.remove(4)
except IndexError, ValueError:
    print("Caught again!")
```

&#x202b; **خروجی (Python 2.x):**
```py
Caught!

ValueError: list.remove(x): x not in list
```

&#x202b; **خروجی (Python 3.x):**
```py
  File "<input>", line 3
    except IndexError, ValueError:
                     ^
SyntaxError: invalid syntax
```

#### 💡 &#x202b; توضیحات

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
  &#x202b; **خروجی (Python 2.x):**
  ```
  Caught again!
  list.remove(x): x not in list
  ```
  &#x202b; **خروجی (Python 3.x):**
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
  &#x202b; **خروجی:**
  ```
  Caught again!
  list.remove(x): x not in list
  ```

---

### ▶ &#x202b; عملوندهای یکسان، داستانی متفاوت!
<!-- Example ID: ca052cdf-dd2d-4105-b936-65c28adc18a0 --->
1\.
```py
a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]
```

&#x202b; **خروجی:**
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

&#x202b; **خروجی:**
```py
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> b
[1, 2, 3, 4, 5, 6, 7, 8]
```

#### 💡 &#x202b; توضیحات:
* &#x202b; عملگر `a += b` همیشه همانند `a = a + b` رفتار نمی‌کند. کلاس‌ها *ممکن است* عملگرهای *`op=`* را به گونه‌ای متفاوت پیاده‌سازی کنند، و لیست‌ها نیز چنین می‌کنند.

* &#x202b; عبارت `a = a + [5,6,7,8]` یک لیست جدید ایجاد می‌کند و مرجع `a` را به این لیست جدید اختصاص می‌دهد، بدون آنکه `b` را تغییر دهد.

* &#x202b; عبارت `a += [5,6,7,8]` در واقع به تابعی معادل «extend» ترجمه می‌شود که روی لیست اصلی عمل می‌کند؛ بنابراین `a` و `b` همچنان به همان لیست اشاره می‌کنند که به‌صورت درجا (in-place) تغییر کرده است.

---

### ▶ &#x202b; تفکیک نام‌ها با نادیده گرفتن حوزه‌ی کلاس
<!-- Example ID: 03f73d96-151c-4929-b0a8-f74430788324 --->
1\.
```py
x = 5
class SomeClass:
    x = 17
    y = (x for i in range(10))
```

&#x202b; **خروجی:**
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

&#x202b; **خروجی (Python 2.x):**
```py
>>> SomeClass.y[0]
17
```

&#x202b; **خروجی (Python 3.x):**
```py
>>> SomeClass.y[0]
5
```

#### 💡 &#x202b; توضیحات
- &#x202b; حوزه‌هایی که درون تعریف کلاس تو در تو هستند، نام‌های تعریف‌شده در سطح کلاس را نادیده می‌گیرند.
- &#x202b; عبارت‌های جنراتور (generator expressions) حوزه‌ی مختص به خود دارند.
- &#x202b; از پایتون نسخه‌ی ۳ به بعد، لیست‌های فشرده (list comprehensions) نیز حوزه‌ی مختص به خود دارند.

---

### ▶ &#x202b; گرد کردن به روش بانکدار *

&#x202b; بیایید یک تابع ساده برای به‌دست‌آوردن عنصر میانی یک لیست پیاده‌سازی کنیم:
```py
def get_middle(some_list):
    mid_index = round(len(some_list) / 2)
    return some_list[mid_index - 1]
```

**Python 3.x:**
```py
>>> get_middle([1])  # خوب به نظر می رسد.
1
>>> get_middle([1,2,3])  # خوب به نظر می رسد.
2
>>> get_middle([1,2,3,4,5])  # چی?
2
>>> len([1,2,3,4,5]) / 2  # خوبه
2.5
>>> round(len([1,2,3,4,5]) / 2)  # چرا?
2
```
&#x202b; به نظر می‌رسد که پایتون عدد ۲٫۵ را به ۲ گرد کرده است.

#### 💡 &#x202b; توضیحات:

- &#x202b; این یک خطای مربوط به دقت اعداد اعشاری نیست؛ بلکه این رفتار عمدی است. از پایتون نسخه 3.0 به بعد، تابع `round()` از [گرد کردن بانکی](https://en.wikipedia.org/wiki/Rounding#Rounding_half_to_even) استفاده می‌کند که در آن کسرهای `.5` به نزدیک‌ترین عدد **زوج** گرد می‌شوند:

```py
>>> round(0.5)
0
>>> round(1.5)
2
>>> round(2.5)
2
>>> import numpy  # numpy هم همینکار را می کند.
>>> numpy.round(0.5)
0.0
>>> numpy.round(1.5)
2.0
>>> numpy.round(2.5)
2.0
```

- &#x202b; این روشِ پیشنهادی برای گرد کردن کسرهای `.5` مطابق با استاندارد [IEEE 754](https://en.wikipedia.org/wiki/IEEE_754#Rounding_rules) است. با این حال، روش دیگر (گرد کردن به سمت دور از صفر) اغلب در مدارس آموزش داده می‌شود؛ بنابراین، «گرد کردن بانکی» احتمالا چندان شناخته‌شده نیست. همچنین، برخی از رایج‌ترین زبان‌های برنامه‌نویسی (مانند جاوااسکریپت، جاوا، C/C++‎، روبی و راست) نیز از گرد کردن بانکی استفاده نمی‌کنند. به همین دلیل این موضوع همچنان مختص پایتون بوده و ممکن است باعث سردرگمی هنگام گرد کردن کسرها شود.
- &#x202b; برای اطلاعات بیشتر به [مستندات تابع `round()`](https://docs.python.org/3/library/functions.html#round) یا [این بحث در Stack Overflow](https://stackoverflow.com/questions/10825926/python-3-x-rounding-behavior) مراجعه کنید.
- &#x202b; توجه داشته باشید که `get_middle([1])` فقط به این دلیل مقدار 1 را بازگرداند که اندیس آن `round(0.5) - 1 = 0 - 1 = -1` بود و در نتیجه آخرین عنصر لیست را برمی‌گرداند.

---

### ▶ &#x202b; سوزن‌هایی در انبار کاه *

<!-- Example ID: 52a199b1-989a-4b28-8910-dff562cebba9 --->

&#x202b; من تا به امروز حتی یک برنامه‌نویس باتجربهٔ پایتون را ندیده‌ام که حداقل با یکی از سناریوهای زیر مواجه نشده باشد:

1\.

```py
x, y = (0, 1) if True else None, None
```

&#x202b; **خروجی:**

```py
>>> x, y  # چیزی که توقع داریم. (0, 1)
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

&#x202b; **خروجی:**

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

&#x202b; **خروجی**

```py
>>> len(ten_words_list)
9
```

4\. &#x202b; عدم تأکید کافی

```py
a = "python"
b = "javascript"
```

&#x202b; **خروجی:**

```py
# &#x202b; دستور assert همراه با پیام خطای assertion
>>> assert(a == b, "Both languages are different")
# &#x202b; هیچ AssertionError ای رخ نمی‌دهد
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

&#x202b; **خروجی:**

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

&#x202b; **خروجی:**

```py
>>> some_recursive_func([5, 0])
[0, 0]
>>> similar_recursive_func(5)
4
```

#### 💡 &#x202b; توضیحات:
* &#x202b; برای مورد ۱، عبارت صحیح برای رفتار مورد انتظار این است:  
`x, y = (0, 1) if True else (None, None)`

* &#x202b; برای مورد ۲، عبارت صحیح برای رفتار مورد انتظار این است:  
&#x202b;`t = ('one',)` یا `t = 'one',` (ویرگول از قلم افتاده است). در غیر این صورت مفسر `t` را به عنوان یک `str` در نظر گرفته و به صورت کاراکتر به کاراکتر روی آن پیمایش می‌کند.

* &#x202b; علامت `()` یک توکن خاص است و نشان‌دهنده‌ی یک `tuple` خالی است.

* &#x202b; در مورد ۳، همان‌طور که احتمالاً متوجه شدید، بعد از عنصر پنجم (`"that"`) یک ویرگول از قلم افتاده است. بنابراین با الحاق ضمنی رشته‌ها،
  ```py
  >>> ten_words_list
  ['some', 'very', 'big', 'list', 'thatconsists', 'of', 'exactly', 'ten', 'words']
  ```

* &#x202b; در قطعه‌ی چهارم هیچ `AssertionError`ای رخ نداد؛ زیرا به جای ارزیابی عبارت تکی `a == b`، کل یک تاپل ارزیابی شده است. قطعه‌ی کد زیر این موضوع را روشن‌تر می‌کند:

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

* &#x202b; در قطعه‌ی پنجم، بیشتر متدهایی که اشیای ترتیبی (Sequence) یا نگاشت‌ها (Mapping) را تغییر می‌دهند (مانند `list.append`، `dict.update`، `list.sort` و غیره)، شیء اصلی را به‌صورت درجا (in-place) تغییر داده و مقدار `None` برمی‌گردانند. منطق پشت این تصمیم، بهبود عملکرد با جلوگیری از کپی کردن شیء است (به این [منبع](https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list) مراجعه کنید).

* &#x202b; قطعه‌ی آخر نیز نسبتاً واضح است؛ شیء تغییرپذیر (mutable)، مثل `list`، می‌تواند در داخل تابع تغییر کند، درحالی‌که انتساب دوباره‌ی یک شیء تغییرناپذیر (مانند `a -= 1`) باعث تغییر مقدار اصلی آن نخواهد شد.

* &#x202b; آگاهی از این نکات ظریف در بلندمدت می‌تواند ساعت‌ها از زمان شما برای رفع اشکال را صرفه‌جویی کند.

---


### ▶ &#x202b; تقسیم‌ها *
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

#### 💡 &#x202b; توضیحات:

- &#x202b; در نگاه اول ممکن است به نظر برسد جداکننده‌ی پیش‌فرض متد `split` یک فاصله‌ی تکی (`' '`) است؛ اما مطابق با [مستندات رسمی](https://docs.python.org/3/library/stdtypes.html#str.split):
    > &#x202b; اگر `sep` مشخص نشده یا برابر با `None` باشد، یک الگوریتم متفاوت برای جدا کردن اعمال می‌شود: رشته‌هایی از فاصله‌های متوالی به عنوان یک جداکننده‌ی واحد در نظر گرفته شده و در نتیجه، هیچ رشته‌ی خالی‌ای در ابتدا یا انتهای لیست خروجی قرار نمی‌گیرد، حتی اگر رشته‌ی اولیه دارای فاصله‌های اضافی در ابتدا یا انتها باشد. به همین دلیل، تقسیم یک رشته‌ی خالی یا رشته‌ای که فقط شامل فضای خالی است با جداکننده‌ی `None` باعث بازگشت یک لیست خالی `[]` می‌شود.
    > &#x202b; اگر `sep` مشخص شود، جداکننده‌های متوالی در کنار هم قرار نمی‌گیرند و هر جداکننده، یک رشته‌ی خالی جدید ایجاد می‌کند. (مثلاً `'1,,2'.split(',')` مقدار `['1', '', '2']` را برمی‌گرداند.) تقسیم یک رشته‌ی خالی با یک جداکننده‌ی مشخص‌شده نیز باعث بازگشت `['']` می‌شود.
- &#x202b; توجه به اینکه چگونه فضای خالی در ابتدا و انتهای رشته در قطعه‌ی کد زیر مدیریت شده است، این مفهوم را روشن‌تر می‌کند:
    ```py
    >>> ' a '.split(' ')
    ['', 'a', '']
    >>> ' a '.split()
    ['a']
    >>> ''.split(' ')
    ['']
    ```

---

### ▶ واردسازی‌های عمومی *
<!-- Example ID: 83deb561-bd55-4461-bb5e-77dd7f411e1c --->
<!-- read-only -->

```py
# File: module.py

def some_weird_name_func_():
    print("works!")

def _another_weird_name_func():
    print("works!")

```

&#x202b; **خروجی**

```py
>>> from module import *
>>> some_weird_name_func_()
"works!"
>>> _another_weird_name_func()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_another_weird_name_func' is not defined
```

#### 💡 &#x202b; توضیحات:

- &#x202b; اغلب توصیه می‌شود از واردسازی عمومی (wildcard imports) استفاده نکنید. اولین دلیل واضح آن این است که در این نوع واردسازی‌ها، اسامی که با زیرخط (`_`) شروع شوند، وارد نمی‌شوند. این مسئله ممکن است در زمان اجرا به خطا منجر شود.
- &#x202b; اگر از ساختار `from ... import a, b, c` استفاده کنیم، خطای `NameError` فوق اتفاق نمی‌افتاد.
    ```py
    >>> from module import some_weird_name_func_, _another_weird_name_func
    >>> _another_weird_name_func()
    works!
    ```
- &#x202b; اگر واقعاً تمایل دارید از واردسازی عمومی استفاده کنید، لازم است فهرستی به نام `__all__` را در ماژول خود تعریف کنید که شامل نام اشیاء عمومی (public) قابل‌دسترس هنگام واردسازی عمومی است.
    ```py
    __all__ = ['_another_weird_name_func']

    def some_weird_name_func_():
        print("works!")

    def _another_weird_name_func():
        print("works!")
    ```
    &#x202b; **خروجی**

    ```py
    >>> _another_weird_name_func()
    "works!"
    >>> some_weird_name_func_()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'some_weird_name_func_' is not defined
    ```

---

### ▶ &#x202b; همه چیز مرتب شده؟ *

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

#### 💡 &#x202b; توضیحات:

- &#x202b; متد `sorted` همیشه یک لیست (`list`) برمی‌گرداند، و در پایتون مقایسه‌ی لیست‌ها و تاپل‌ها (`tuple`) همیشه مقدار `False` را برمی‌گرداند.

- ```py
  >>> [] == tuple()
  False
  >>> x = 7, 8, 9
  >>> type(x), type(sorted(x))
  (tuple, list)
  ```
- &#x202b; برخلاف متد `sorted`، متد `reversed` یک تکرارکننده (iterator) برمی‌گرداند. چرا؟ زیرا مرتب‌سازی نیاز به تغییر درجا (in-place) یا استفاده از ظرف جانبی (مانند یک لیست اضافی) دارد، در حالی که معکوس کردن می‌تواند به‌سادگی با پیمایش از اندیس آخر به اول انجام شود.

- &#x202b; بنابراین در مقایسه‌ی `sorted(y) == sorted(y)`، فراخوانی اولِ `sorted()` تمام عناصرِ تکرارکننده‌ی `y` را مصرف می‌کند، و فراخوانی بعدی یک لیست خالی برمی‌گرداند.

  ```py
  >>> x = 7, 8, 9
  >>> y = reversed(x)
  >>> sorted(y), sorted(y)
  ([7, 8, 9], [])
  ```

---

### ▶ &#x202b; زمان نیمه‌شب وجود ندارد؟
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

&#x202b; **خروجی (< 3.5):**

```py
('Time at noon is', datetime.time(12, 0))
```
The midnight time is not printed.

#### 💡 &#x202b; توضیحات:

Before Python 3.5, the boolean value for `datetime.time` object was considered to be `False` if it represented midnight in UTC. It is error-prone when using the `if obj:` syntax to check if the `obj` is null or some equivalent of "empty."

---
---



## &#x202b; بخش: گنجینه‌های پنهان!

&#x202b; این بخش شامل چند مورد جالب و کمتر شناخته‌شده درباره‌ی پایتون است که بیشتر مبتدی‌هایی مثل من از آن بی‌خبرند (البته دیگر اینطور نیست).

### ▶ &#x202b; خب پایتون، می‌توانی کاری کنی پرواز کنم؟
<!-- Example ID: a92f3645-1899-4d50-9721-0031be4aec3f --->
&#x202b; خب، بفرمایید

```py
import antigravity
```

&#x202b; **خروجی:**
Sshh... It's a super-secret.

#### &#x202b; 💡 توضیح:
+ &#x202b; ماژول `antigravity` یکی از معدود ایستر اِگ‌هایی است که توسط توسعه‌دهندگان پایتون ارائه شده است.
+ &#x202b; دستور `import antigravity` باعث می‌شود مرورگر وب به سمت [کمیک کلاسیک XKCD](https://xkcd.com/353/) در مورد پایتون باز شود.
+ &#x202b; البته موضوع عمیق‌تر است؛ در واقع یک **ایستر اگ دیگر داخل این ایستر اگ** وجود دارد. اگر به [کد منبع](https://github.com/python/cpython/blob/master/Lib/antigravity.py#L7-L17) نگاه کنید، یک تابع تعریف شده که ادعا می‌کند [الگوریتم جئوهشینگ XKCD](https://xkcd.com/426/) را پیاده‌سازی کرده است.

---

### ▶ &#x202b; `goto`، ولی چرا؟
<!-- Example ID: 2aff961e-7fa5-4986-a18a-9e5894bd89fe --->

```py
from goto import goto, label
for i in range(9):
    for j in range(9):
        for k in range(9):
            print("I am trapped, please rescue!")
            if k == 2:
                goto .breakout # خروج از یک حلقه‌ی تودرتوی عمیق
label .breakout
print("Freedom!")
```

&#x202b; **خروجی (پایتون ۲.۳):**
```py
I am trapped, please rescue!
I am trapped, please rescue!
Freedom!
```

#### &#x202b; 💡 توضیح:
- &#x202b; نسخه‌ی قابل استفاده‌ای از `goto` در پایتون به عنوان یک شوخی [در اول آوریل ۲۰۰۴ معرفی شد](https://mail.python.org/pipermail/python-announce-list/2004-April/002982.html).
- &#x202b; نسخه‌های فعلی پایتون فاقد این ماژول هستند.
- &#x202b; اگرچه این ماژول واقعاً کار می‌کند، ولی لطفاً از آن استفاده نکنید. در [این صفحه](https://docs.python.org/3/faq/design.html#why-is-there-no-goto) می‌توانید دلیل عدم حضور دستور `goto` در پایتون را مطالعه کنید.

---

### ▶ &#x202b; خودتان را آماده کنید!
<!-- Example ID: 5c0c75f2-ddd9-4da3-ba49-c4be7ec39acf --->
&#x202b; اگر جزو افرادی هستید که دوست ندارند در پایتون برای مشخص کردن محدوده‌ها از فضای خالی (whitespace) استفاده کنند، می‌توانید با ایمپورت کردن ماژول زیر از آکولاد `{}` به سبک زبان C استفاده کنید:

```py
from __future__ import braces
```

&#x202b; **خروجی:**
```py
  File "some_file.py", line 1
    from __future__ import braces
SyntaxError: not a chance
```

&#x202b; آکولاد؟ هرگز! اگر از این بابت ناامید شدید، بهتر است از جاوا استفاده کنید. خب، یک چیز شگفت‌آور دیگر؛ آیا می‌توانید تشخیص دهید که ارور `SyntaxError` در کجای کد ماژول `__future__` [اینجا](https://github.com/python/cpython/blob/master/Lib/__future__.py) ایجاد می‌شود؟

#### &#x202b; 💡 توضیح:
+ &#x202b; ماژول `__future__` معمولاً برای ارائه قابلیت‌هایی از نسخه‌های آینده پایتون به کار می‌رود. اما کلمه «future» (آینده) در این زمینه خاص، حالت طنز و کنایه دارد.
+ &#x202b; این مورد یک «ایستر اگ» (easter egg) است که به احساسات جامعه برنامه‌نویسان پایتون در این خصوص اشاره دارد.
+ &#x202b; کد مربوط به این موضوع در واقع [اینجا](https://github.com/python/cpython/blob/025eb98dc0c1dc27404df6c544fc2944e0fa9f3a/Python/future.c#L49) در فایل `future.c` قرار دارد.
+ &#x202b; زمانی که کامپایلر CPython با یک [عبارت future](https://docs.python.org/3.3/reference/simple_stmts.html#future-statements) مواجه می‌شود، ابتدا کد مرتبط در `future.c` را اجرا کرده و سپس آن را همانند یک دستور ایمپورت عادی در نظر می‌گیرد.

---

### ▶ &#x202b; بیایید با «عمو زبان مهربان برای همیشه» آشنا شویم
<!-- Example ID: 6427fae6-e959-462d-85da-ce4c94ce41be --->
&#x202b; **خروجی (Python 3.x)**
```py
>>> from __future__ import barry_as_FLUFL
>>> "Ruby" != "Python" # شکی در این نیست.
  File "some_file.py", line 1
    "Ruby" != "Python"
              ^
SyntaxError: invalid syntax

>>> "Ruby" <> "Python"
True
```

&#x202b; حالا می‌رسیم به اصل ماجرا.

#### &#x202b; 💡 توضیح:
- &#x202b; این مورد مربوط به [PEP-401](https://www.python.org/dev/peps/pep-0401/) است که در تاریخ ۱ آوریل ۲۰۰۹ منتشر شد (اکنون می‌دانید این یعنی چه!).
- &#x202b; نقل قولی از PEP-401:

  > &#x202b; با توجه به اینکه عملگر نابرابری `!=` در پایتون ۳.۰ یک اشتباه وحشتناک و انگشت‌سوز (!) بوده است، عمو زبان مهربان برای همیشه (FLUFL) عملگر الماسی‌شکل `<>` را مجدداً به‌عنوان تنها روش درست برای این منظور بازگردانده است.
  
- &#x202b; البته «عمو بَری» چیزهای بیشتری برای گفتن در این PEP داشت؛ می‌توانید آن‌ها را [اینجا](https://www.python.org/dev/peps/pep-0401/) مطالعه کنید.
- &#x202b; این قابلیت در محیط تعاملی به خوبی عمل می‌کند، اما در زمان اجرای کد از طریق فایل پایتون، با خطای `SyntaxError` روبرو خواهید شد (برای اطلاعات بیشتر به این [issue](https://github.com/satwikkansal/wtfpython/issues/94) مراجعه کنید). با این حال، می‌توانید کد خود را درون یک `eval` یا `compile` قرار دهید تا این قابلیت فعال شود.

    ```py
    from __future__ import barry_as_FLUFL
    print(eval('"Ruby" <> "Python"'))
    ```

---

### ▶ &#x202b; حتی پایتون هم می‌داند که عشق پیچیده است
<!-- Example ID: b93cad9e-d341-45d1-999c-fcdce65bed25 --->
```py
import this
```

Wait, what's **this**? `this` is love :heart:

&#x202b; **خروجی:**
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

&#x202b; این ذنِ پایتون است!

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
>>> love is not True or False; love is love  # عشق پیجیده است
True
```

#### &#x202b; 💡 توضیح:

* &#x202b; ماژول `this` در پایتون، یک ایستر اگ برای «ذنِ پایتون» ([PEP 20](https://www.python.org/dev/peps/pep-0020)) است.
* &#x202b; اگر این موضوع به‌اندازه کافی جالب است، حتماً پیاده‌سازی [this.py](https://hg.python.org/cpython/file/c3896275c0f6/Lib/this.py) را ببینید. نکته جالب این است که **کد مربوط به ذنِ پایتون، خودش اصول ذن را نقض کرده است** (و احتمالاً این تنها جایی است که چنین اتفاقی می‌افتد).
* &#x202b; درباره جمله `love is not True or False; love is love`، اگرچه طعنه‌آمیز است، اما خود گویاست. (اگر واضح نیست، لطفاً مثال‌های مربوط به عملگرهای `is` و `is not` را مشاهده کنید.)

---

### ▶ &#x202b; بله، این واقعاً وجود دارد!
<!-- Example ID: 4286db3d-1ea7-47c9-8fb6-a9a04cac6e49 --->
&#x202b; **عبارت `else` برای حلقه‌ها.** یک مثال معمول آن می‌تواند چنین باشد:

```py
  def does_exists_num(l, to_find):
      for num in l:
          if num == to_find:
              print("Exists!")
              break
      else:
          print("Does not exist")
```

**خروجی:**
```py
>>> some_list = [1, 2, 3, 4, 5]
>>> does_exists_num(some_list, 4)
Exists!
>>> does_exists_num(some_list, -1)
Does not exist
```

**عبارت `else` در مدیریت استثناها.** مثالی از آن:

```py
try:
    pass
except:
    print("Exception occurred!!!")
else:
    print("Try block executed successfully...")
```

**خروجی:**
```py
Try block executed successfully...
```

#### &#x202b; 💡 توضیح:
- عبارت `else` بعد از حلقه‌ها تنها زمانی اجرا می‌شود که در هیچ‌کدام از تکرارها (`iterations`) از دستور `break` استفاده نشده باشد. می‌توانید آن را به عنوان یک شرط «بدون شکست» (nobreak) در نظر بگیرید.
- عبارت `else` پس از بلاک `try` به عنوان «عبارت تکمیل» (`completion clause`) نیز شناخته می‌شود؛ چراکه رسیدن به عبارت `else` در ساختار `try` به این معنی است که بلاک `try` بدون رخ دادن استثنا با موفقیت تکمیل شده است.

---
### ▶ Ellipsis *
<!-- Example ID: 969b7100-ab3d-4a7d-ad7d-a6be16181b2b --->
```py
def some_func():
    Ellipsis
```

**خروجی**
```py
>>> some_func()
# بدون خروجی و بدون خطا

>>> SomeRandomString
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'SomeRandomString' is not defined

>>> Ellipsis
Ellipsis
```

#### &#x202b; 💡توضیح
- &#x202b; در پایتون، `Ellipsis` یک شیء درونی (`built-in`) است که به صورت سراسری (`global`) در دسترس است و معادل `...` است.
    ```py
    >>> ...
    Ellipsis
    ```
- &#x202b; `Ellipsis` می‌تواند برای چندین منظور استفاده شود:
    + &#x202b; به عنوان یک نگه‌دارنده برای کدی که هنوز نوشته نشده است (مانند دستور `pass`)
    + &#x202b; در سینتکس برش (`slicing`) برای نمایش برش کامل در ابعاد باقی‌مانده

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
    &#x202b; بنابراین، آرایه‌ی `three_dimensional_array` ما، آرایه‌ای از آرایه‌ها از آرایه‌ها است. فرض کنیم می‌خواهیم عنصر دوم (اندیس `1`) از تمامی آرایه‌های درونی را چاپ کنیم؛ در این حالت می‌توانیم از `Ellipsis` برای عبور از تمامی ابعاد قبلی استفاده کنیم:
    ```py
    >>> three_dimensional_array[:,:,1]
    array([[1, 3],
       [5, 7]])
    >>> three_dimensional_array[..., 1] # با استفاده از Ellipsis.
    array([[1, 3],
       [5, 7]])
    ```
    &#x202b; نکته: این روش برای آرایه‌هایی با هر تعداد بُعد کار می‌کند. حتی می‌توانید از برش (`slice`) در بُعد اول و آخر استفاده کرده و ابعاد میانی را نادیده بگیرید (به صورت `n_dimensional_array[first_dim_slice, ..., last_dim_slice]`).
    + &#x202b; در [نوع‌دهی (`type hinting`)](https://docs.python.org/3/library/typing.html) برای اشاره به بخشی از نوع (مانند `Callable[..., int]` یا `Tuple[str, ...]`) استفاده می‌شود.
    + &#x202b; همچنین می‌توانید از `Ellipsis` به عنوان آرگومان پیش‌فرض تابع استفاده کنید (برای مواردی که می‌خواهید میان «آرگومانی ارسال نشده است» و «مقدار `None` ارسال شده است» تمایز قائل شوید).


---

### ▶ &#x202b; بی‌نهایت (`Inpinity`)
<!-- Example ID: ff473ea8-a3b1-4876-a6f0-4378aff790c1 --->
&#x202b; این املای کلمه تعمداً به همین شکل نوشته شده است. لطفاً برای اصلاح آن درخواست (`patch`) ارسال نکنید.

&#x202b; **خروجی (پایتون 3.x):**
```py
>>> infinity = float('infinity')
>>> hash(infinity)
314159
>>> hash(float('-inf'))
-314159
```

#### &#x202b; 💡 توضیح:
- &#x202b; هش (`hash`) مقدار بی‌نهایت برابر با 10⁵ × π است.
- &#x202b; نکته جالب اینکه در پایتون ۳ هشِ مقدار `float('-inf')` برابر با «-10⁵ × π» است، در حالی که در پایتون ۲ برابر با «-10⁵ × e» است.

---

### ▶ &#x202b; بیایید خرابکاری کنیم
<!-- Example ID: 37146d2d-9e67-43a9-8729-3c17934b910c --->
1\.
```py
class Yo(object):
    def __init__(self):
        self.__honey = True
        self.bro = True
```

&#x202b; **خروجی:**
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
        # این بار بیایید چیزی متقارن را امتحان کنیم
        self.__honey__ = True
        self.bro = True
```

&#x202b; **خروجی:**
```py
>>> Yo().bro
True

>>> Yo()._Yo__honey__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Yo' object has no attribute '_Yo__honey__'
```

چرا کد `Yo()._Yo__honey` کار کرد؟

3\.

```py
_A__variable = "Some value"

class A(object):
    def some_func(self):
        return __variable # هنوز در هیچ جا مقداردهی اولیه نشده است
```

&#x202b; **خروجی:**
```py
>>> A().__variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__variable'

>>> A().some_func()
'Some value'
```


#### &#x202b; 💡 توضیح:

* &#x202b; [تغییر نام](https://en.wikipedia.org/wiki/Name_mangling) برای جلوگیری از برخورد نام‌ها بین فضاهای نام مختلف استفاده می‌شود.
* &#x202b; در پایتون، مفسر نام‌های اعضای کلاس که با `__` (دو آندرلاین که به عنوان "دندر" شناخته می‌شود) شروع می‌شوند و بیش از یک آندرلاین انتهایی ندارند را با اضافه کردن `_NameOfTheClass` در ابتدای آنها تغییر می‌دهد.
* &#x202b; بنابراین، برای دسترسی به ویژگی `__honey` در اولین قطعه کد، مجبور بودیم `_Yo` را به ابتدای آن اضافه کنیم، که از بروز تعارض با ویژگی با همان نام تعریف‌شده در هر کلاس دیگری جلوگیری می‌کند.
* &#x202b; اما چرا در دومین قطعه کد کار نکرد؟ زیرا تغییر نام، نام‌هایی که با دو آندرلاین خاتمه می‌یابند را شامل نمی‌شود.
* &#x202b; قطعه سوم نیز نتیجه تغییر نام بود. نام `__variable` در عبارت `return __variable` به `_A__variable` تغییر یافت، که همچنین همان نام متغیری است که در محدوده بیرونی تعریف کرده بودیم.
* &#x202b; همچنین، اگر نام تغییر یافته بیش از ۲۵۵ کاراکتر باشد، برش داده می‌شود.

---
---

## &#x202b; بخش: ظاهرها فریبنده‌اند!

### ▶ &#x202b; خطوط را رد می‌کند؟
<!-- Example ID: d50bbde1-fb9d-4735-9633-3444b9d2f417 --->
&#x202b; **خروجی:**
```py
>>> value = 11
>>> valuе = 32
>>> value
11
```

&#x202b; چی?

&#x202b; **نکته:** ساده‌ترین روش برای بازتولید این رفتار، کپی کردن دستورات از کد بالا و جایگذاری (paste) آن‌ها در فایل یا محیط تعاملی (shell) خودتان است.

#### &#x202b; 💡 توضیح

&#x202b; برخی از حروف غیرغربی کاملاً مشابه حروف الفبای انگلیسی به نظر می‌رسند، اما مفسر پایتون آن‌ها را متفاوت در نظر می‌گیرد.

```py
>>> ord('е') # حرف سیریلیک «е» (Ye)
1077
>>> ord('e') # حرف لاتین «e»، که در انگلیسی استفاده می‌شود و با صفحه‌کلید استاندارد تایپ می‌گردد
101
>>> 'е' == 'e'
False

>>> value = 42 # حرف لاتین e
>>> valuе = 23 # حرف سیریلیک «е»؛ مفسر پایتون نسخه ۲ در اینجا خطای `SyntaxError` ایجاد می‌کند
>>> value
42
```

&#x202b; تابع داخلی `ord()`، [کدپوینت](https://fa.wikipedia.org/wiki/کدپوینت) یونیکد مربوط به یک نویسه را برمی‌گرداند. موقعیت‌های کدی متفاوت برای حرف سیریلیک «е» و حرف لاتین «e»، علت رفتار مثال بالا را توجیه می‌کنند.

---

### ▶ &#x202b; تله‌پورت کردن

<!-- Example ID: edafe923-0c20-4315-b6e1-0c31abfc38f5 --->

```py
# `pip install numpy` first.
import numpy as np

def energy_send(x):
    # مقداردهی اولیه یک آرایه numpy
    np.array([float(x)])

def energy_receive():
    # بازگرداندن یک آرایه‌ی خالی numpy
    return np.empty((), dtype=np.float).tolist()
```

&#x202b; **خروجی:**
```py
>>> energy_send(123.456)
>>> energy_receive()
123.456
```

&#x202b; جایزه نوبل کجاست؟

#### &#x202b; 💡 توضیح:

* &#x202b; توجه کنید که آرایه‌ی numpy ایجادشده در تابع `energy_send` برگردانده نشده است، بنابراین فضای حافظه‌ی آن آزاد شده و مجدداً قابل استفاده است.
* &#x202b; تابع `numpy.empty()` نزدیک‌ترین فضای حافظه‌ی آزاد را بدون مقداردهی مجدد برمی‌گرداند. این فضای حافظه معمولاً همان فضایی است که به‌تازگی آزاد شده است (البته معمولاً این اتفاق می‌افتد و نه همیشه).

---

### ▶ &#x202b; خب، یک جای کار مشکوک است...
<!-- Example ID: cb6a37c5-74f7-44ca-b58c-3b902419b362 --->
```py
def square(x):
    """
    یک تابع ساده برای محاسبه‌ی مربع یک عدد با استفاده از جمع.
    """
    sum_so_far = 0
    for counter in range(x):
        sum_so_far = sum_so_far + x
  return sum_so_far
```

&#x202b; **خروجی (پایتون 2.X):**

```py
>>> square(10)
10
```

&#x202b; آیا این نباید ۱۰۰ باشد؟

&#x202b; **نکته:** اگر نمی‌توانید این مشکل را بازتولید کنید، سعی کنید فایل [mixed_tabs_and_spaces.py](/mixed_tabs_and_spaces.py) را از طریق شِل اجرا کنید.

#### &#x202b; 💡 توضیح

* &#x202b; **تب‌ها و فاصله‌ها (space) را با هم ترکیب نکنید!** کاراکتری که دقیقاً قبل از دستور return آمده یک «تب» است، در حالی که در بقیۀ مثال، کد با مضربی از «۴ فاصله» تورفتگی دارد.
* &#x202b; نحوۀ برخورد پایتون با تب‌ها به این صورت است:

  > &#x202b; ابتدا تب‌ها (از چپ به راست) با یک تا هشت فاصله جایگزین می‌شوند به‌طوری که تعداد کل کاراکترها تا انتهای آن جایگزینی، مضربی از هشت باشد <...>
* &#x202b; بنابراین «تب» در آخرین خط تابع `square` با هشت فاصله جایگزین شده و به همین دلیل داخل حلقه قرار می‌گیرد.
* &#x202b; پایتون ۳ آنقدر هوشمند هست که چنین مواردی را به‌صورت خودکار با خطا اعلام کند.

    &#x202b; **خروجی (Python 3.x):**

    ```py
    TabError: inconsistent use of tabs and spaces in indentation
    ```

---
---

## بخش: متفرقه


### &#x202b; ▶ `+=` سریع‌تر است
<!-- Example ID: bfd19c60-a807-4a26-9598-4912b86ddb36 --->

```py
# استفاده از "+"، سه رشته:
>>> timeit.timeit("s1 = s1 + s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.25748300552368164
# استفاده از "+="، سه رشته:
>>> timeit.timeit("s1 += s2 + s3", setup="s1 = ' ' * 100000; s2 = ' ' * 100000; s3 = ' ' * 100000", number=100)
0.012188911437988281
```

#### &#x202b;  💡 توضیح:
+ &#x202b;  استفاده از `+=` برای اتصال بیش از دو رشته سریع‌تر از `+` است، زیرا هنگام محاسبه رشته‌ی نهایی، رشته‌ی اول (به‌عنوان مثال `s1` در عبارت `s1 += s2 + s3`) از بین نمی‌رود.

---

### &#x202b; ▶ بیایید یک رشته‌ی بزرگ بسازیم!
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

&#x202b; **خروجی:**

&#x202b; اجرا شده در پوسته‌ی ipython با استفاده از `%timeit` برای خوانایی بهتر نتایج.
&#x202b; همچنین می‌توانید از ماژول `timeit` در پوسته یا اسکریپت عادی پایتون استفاده کنید؛ نمونه‌ی استفاده در زیر آمده است:
timeit.timeit('add_string_with_plus(10000)', number=1000, globals=globals())

```py

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

&#x202b; بیایید تعداد تکرارها را ۱۰ برابر افزایش دهیم.

```py
>>> NUM_ITERS = 10000
>>> %timeit -n1000 add_string_with_plus(NUM_ITERS) # افزایش خطی در زمان اجرا
1.26 ms ± 76.8 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_bytes_with_plus(NUM_ITERS) # افزایش درجه دو (افزایش مربعی)
6.82 ms ± 134 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_string_with_format(NUM_ITERS) # افزایش خطی
645 µs ± 24.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> %timeit -n1000 add_string_with_join(NUM_ITERS) # افزایش خطی
1.17 ms ± 7.25 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
>>> l = ["xyz"]*NUM_ITERS
>>> %timeit -n1000 convert_list_to_string(l, NUM_ITERS) # افزایش خطی
86.3 µs ± 2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

#### 💡 توضیحات
توضیحات
- &#x202b;  برای اطلاعات بیشتر درباره‌ی [timeit](https://docs.python.org/3/library/timeit.html) یا [%timeit](https://ipython.org/ipython-doc/dev/interactive/magics.html#magic-timeit)، می‌توانید به این لینک‌ها مراجعه کنید. این توابع برای اندازه‌گیری زمان اجرای قطعه‌کدها استفاده می‌شوند.
- &#x202b;  برای تولید رشته‌های طولانی از `+` استفاده نکنید — در پایتون، نوع داده‌ی `str` تغییرناپذیر (immutable) است؛ بنابراین برای هر الحاق (concatenation)، رشته‌ی چپ و راست باید در رشته‌ی جدید کپی شوند. اگر چهار رشته‌ی ۱۰ حرفی را متصل کنید، به‌جای کپی ۴۰ کاراکتر، باید `(10+10) + ((10+10)+10) + (((10+10)+10)+10) = 90` کاراکتر کپی کنید. این وضعیت با افزایش تعداد و طول رشته‌ها به‌صورت درجه دو (مربعی) بدتر می‌شود (که توسط زمان اجرای تابع `add_bytes_with_plus` تأیید شده است).
- &#x202b;  بنابراین توصیه می‌شود از `.format` یا سینتکس `%` استفاده کنید (البته این روش‌ها برای رشته‌های بسیار کوتاه کمی کندتر از `+` هستند).
- &#x202b;  اما بهتر از آن، اگر محتوای شما از قبل به‌شکل یک شیء قابل تکرار (iterable) موجود است، از دستور `''.join(iterable_object)` استفاده کنید که بسیار سریع‌تر است.
- &#x202b;  برخلاف تابع `add_bytes_with_plus` و به‌دلیل بهینه‌سازی‌های انجام‌شده برای عملگر `+=` (که در مثال قبلی توضیح داده شد)، تابع `add_string_with_plus` افزایشی درجه دو در زمان اجرا نشان نداد. اگر دستور به‌صورت `s = s + "x" + "y" + "z"` بود (به‌جای `s += "xyz"`)، افزایش زمان اجرا درجه دو می‌شد.
  ```py
  def add_string_with_plus(iters):
      s = ""
      for i in range(iters):
          s = s + "x" + "y" + "z"
      assert len(s) == 3*iters

  >>> %timeit -n100 add_string_with_plus(1000)
  388 µs ± 22.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
  >>> %timeit -n100 add_string_with_plus(10000) # افزایش درجه دو در زمان اجرا
  9 ms ± 298 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
  ```
- &#x202b; وجود راه‌های متعدد برای قالب‌بندی و ایجاد رشته‌های بزرگ تا حدودی در تضاد با [ذِن پایتون](https://www.python.org/dev/peps/pep-0020/) است که می‌گوید:

  
    > &#x202b;  «باید یک راه — و ترجیحاً فقط یک راه — واضح برای انجام آن وجود داشته باشد.»

---

### ▶ &#x202b;  کُند کردن جستجوها در `dict` *
<!-- Example ID: c9c26ce6-df0c-47f7-af0b-966b9386d4c3 --->
```py
some_dict = {str(i): 1 for i in range(1_000_000)}
another_dict = {str(i): 1 for i in range(1_000_000)}
```

&#x202b; **خروجی:**
```py
>>> %timeit some_dict['5']
28.6 ns ± 0.115 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> some_dict[1] = 1
>>> %timeit some_dict['5']
37.2 ns ± 0.265 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

>>> %timeit another_dict['5']
28.5 ns ± 0.142 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
>>> another_dict[1]  # تلاش برای دسترسی به کلیدی که وجود ندارد
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> %timeit another_dict['5']
38.5 ns ± 0.0913 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
```
چرا جستجوهای یکسان کندتر می‌شوند؟

#### &#x202b;  💡 توضیح:
+ &#x202b; در CPython یک تابع عمومی برای جستجوی کلید در دیکشنری‌ها وجود دارد که از تمام انواع کلیدها (`str`، `int` و هر شیء دیگر) پشتیبانی می‌کند؛ اما برای حالت متداولی که تمام کلیدها از نوع `str` هستند، یک تابع بهینه‌شده‌ی اختصاصی نیز وجود دارد.
+ &#x202b; تابع اختصاصی (که در کد منبع CPython با نام [`lookdict_unicode`](https://github.com/python/cpython/blob/522691c46e2ae51faaad5bbbce7d959dd61770df/Objects/dictobject.c#L841) شناخته می‌شود) فرض می‌کند که تمام کلیدهای موجود در دیکشنری (از جمله کلیدی که در حال جستجوی آن هستید) رشته (`str`) هستند و برای مقایسه‌ی کلیدها، به‌جای فراخوانی متد `__eq__`، از مقایسه‌ی سریع‌تر و ساده‌تر رشته‌ای استفاده می‌کند.
+ &#x202b; اولین باری که یک دیکشنری (`dict`) با کلیدی غیر از `str` فراخوانی شود، این حالت تغییر می‌کند و جستجوهای بعدی از تابع عمومی استفاده خواهند کرد.
+ &#x202b; این فرایند برای آن نمونه‌ی خاص از دیکشنری غیرقابل بازگشت است و حتی لازم نیست کلید موردنظر در دیکشنری موجود باشد. به همین دلیل است که حتی تلاش ناموفق برای دسترسی به کلیدی ناموجود نیز باعث ایجاد همین تأثیر (کند شدن جستجو) می‌شود.


### &#x202b; ▶ حجیم کردن دیکشنری نمونه‌ها (`instance dicts`) *
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

&#x202b; **خروجی:** (پایتون ۳.۸؛ سایر نسخه‌های پایتون ۳ ممکن است کمی متفاوت باشند)
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

&#x202b; بیایید دوباره امتحان کنیم... در یک مفسر (interpreter) جدید:

```py
>>> o1 = SomeClass()
>>> o2 = SomeClass()
>>> dict_size(o1)
104  # همان‌طور که انتظار می‌رفت
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

&#x202b; چه چیزی باعث حجیم‌شدن این دیکشنری‌ها می‌شود؟ و چرا اشیاء تازه ساخته‌شده نیز حجیم هستند؟

#### 💡 توضیح:
+ &#x202b; در CPython، امکان استفاده‌ی مجدد از یک شیء «کلیدها» (`keys`) در چندین دیکشنری وجود دارد. این ویژگی در [PEP 412](https://www.python.org/dev/peps/pep-0412/) معرفی شد تا مصرف حافظه کاهش یابد، به‌ویژه برای دیکشنری‌هایی که به نمونه‌ها (instances) تعلق دارند و معمولاً کلیدها (نام صفات نمونه‌ها) بین آن‌ها مشترک است.
+ &#x202b; این بهینه‌سازی برای دیکشنری‌های نمونه‌ها کاملاً شفاف و خودکار است؛ اما اگر بعضی فرضیات نقض شوند، غیرفعال می‌شود.
+ &#x202b; دیکشنری‌هایی که کلیدهایشان به اشتراک گذاشته شده باشد، از حذف کلید پشتیبانی نمی‌کنند؛ بنابراین اگر صفتی از یک نمونه حذف شود، دیکشنریِ آن نمونه «غیر مشترک» (`unshared`) شده و این قابلیت اشتراک‌گذاری کلیدها برای تمام نمونه‌هایی که در آینده از آن کلاس ساخته می‌شوند، غیرفعال می‌گردد.
+ &#x202b; همچنین اگر اندازه‌ی دیکشنری به‌علت اضافه‌شدن کلیدهای جدید تغییر کند (`resize` شود)، اشتراک‌گذاری کلیدها تنها زمانی ادامه می‌یابد که فقط یک دیکشنری در حال استفاده از آن‌ها باشد (این اجازه می‌دهد در متد `__init__` برای اولین نمونه‌ی ساخته‌شده، صفات متعددی تعریف کنید بدون آن‌که اشتراک‌گذاری کلیدها از بین برود). اما اگر چند نمونه همزمان وجود داشته باشند و تغییر اندازه‌ی دیکشنری رخ دهد، قابلیت اشتراک‌گذاری کلیدها برای نمونه‌های بعدی همان کلاس غیرفعال خواهد شد. زیرا CPython دیگر نمی‌تواند مطمئن باشد که آیا نمونه‌های بعدی دقیقاً از مجموعه‌ی یکسانی از صفات استفاده خواهند کرد یا خیر.
+ &#x202b; نکته‌ای کوچک برای کاهش مصرف حافظه‌ی برنامه: هرگز صفات نمونه‌ها را حذف نکنید و حتماً تمام صفات را در متد `__init__` تعریف و مقداردهی اولیه کنید!


### &#x202b;  ▶ موارد جزئی *
<!-- Example ID: f885cb82-f1e4-4daa-9ff3-972b14cb1324 --->
* &#x202b;  متد `join()` عملیاتی مربوط به رشته (`str`) است، نه لیست (`list`). (در نگاه اول کمی برخلاف انتظار است.)

  ** &#x202b;💡 توضیح:** اگر `join()` به‌عنوان متدی روی رشته پیاده‌سازی شود، می‌تواند روی هر شیء قابل پیمایش (`iterable`) از جمله لیست، تاپل و هر نوع تکرارشونده‌ی دیگر کار کند. اگر به‌جای آن روی لیست تعریف می‌شد، باید به‌طور جداگانه برای هر نوع دیگری نیز پیاده‌سازی می‌شد. همچنین منطقی نیست که یک متد مختص رشته روی یک شیء عمومی مانند `list` پیاده شود.

* &#x202b; تعدادی عبارت با ظاهری عجیب اما از نظر معنا صحیح:
  + &#x202b; عبارت `[] = ()` از نظر معنایی صحیح است (باز کردن یا `unpack` کردن یک تاپل خالی درون یک لیست خالی).
  + &#x202b; عبارت `'a'[0][0][0][0][0]` نیز از نظر معنایی صحیح است، زیرا پایتون برخلاف زبان‌هایی که از C منشعب شده‌اند، نوع داده‌ای جداگانه‌ای برای کاراکتر ندارد. بنابراین انتخاب یک کاراکتر از یک رشته، منجر به بازگشت یک رشته‌ی تک‌کاراکتری می‌شود.
  + &#x202b;  عبارات `3 --0-- 5 == 8` و `--5 == 5` هر دو از لحاظ معنایی درست بوده و مقدارشان برابر `True` است.

* &#x202b;  با فرض اینکه `a` یک عدد باشد، عبارات `++a` و `--a` هر دو در پایتون معتبر هستند؛ اما رفتاری مشابه با عبارات مشابه در زبان‌هایی مانند C، ++C یا جاوا ندارند.

  ```py
  >>> a = 5
  >>> a
  5
  >>> ++a
  5
  >>> --a
  5
  ```

  ** &#x202b; 💡 توضیح:**
  + &#x202b; در گرامر پایتون عملگری به‌نام `++` وجود ندارد. در واقع `++` دو عملگر `+` جداگانه است.
  + &#x202b; عبارت `++a` به‌شکل `+(+a)` تفسیر می‌شود که معادل `a` است. به‌همین ترتیب، خروجی عبارت `--a` نیز قابل توجیه است.
  + &#x202b;  این [تاپیک در StackOverflow](https://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python) دلایل نبودن عملگرهای افزایش (`++`) و کاهش (`--`) در پایتون را بررسی می‌کند.

* &#x202b; احتمالاً با عملگر Walrus (گراز دریایی) در پایتون آشنا هستید؛ اما تا به حال در مورد *عملگر Space-invader (مهاجم فضایی)* شنیده‌اید؟

  ```py
  >>> a = 42
  >>> a -=- 1
  >>> a
  43
  ```
&#x202b; از آن به‌عنوان جایگزینی برای عملگر افزایش (increment)، در ترکیب با یک عملگر دیگر استفاده می‌شود.
  ```py
  >>> a +=+ 1
  >>> a
  >>> 44
  ```
  **&#x202b; 💡 توضیح:** این شوخی از [توییت Raymond Hettinger](https://twitter.com/raymondh/status/1131103570856632321?lang=en) برگرفته شده است. عملگر «مهاجم فضایی» در واقع همان عبارت بدفرمت‌شده‌ی `a -= (-1)` است که معادل با `a = a - (- 1)` می‌باشد. حالت مشابهی برای عبارت `a += (+ 1)` نیز وجود دارد.

* &#x202b; پایتون یک عملگر مستندنشده برای [استلزام معکوس (converse implication)](https://en.wikipedia.org/wiki/Converse_implication) دارد.
     
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

     &#x202b; **💡 توضیح:** اگر مقادیر `False` و `True` را به‌ترتیب با اعداد ۰ و ۱ جایگزین کرده و محاسبات را انجام دهید، جدول درستی حاصل، معادل یک عملگر استلزام معکوس خواهد بود. ([منبع](https://github.com/cosmologicon/pywat/blob/master/explanation.md#the-undocumented-converse-implication-operator))

* &#x202b; حالا که صحبت از عملگرها شد، عملگر `@` نیز برای ضرب ماتریسی در پایتون وجود دارد (نگران نباشید، این بار واقعی است).

     ```py
     >>> import numpy as np
     >>> np.array([2, 2, 2]) @ np.array([7, 8, 8])
     46
     ```

     &#x202b; **💡 توضیح:** عملگر `@` در پایتون ۳٫۵ با در نظر گرفتن نیازهای جامعه علمی اضافه شد. هر شی‌ای می‌تواند متد جادویی `__matmul__` را بازنویسی کند تا رفتار این عملگر را مشخص نماید.

* &#x202b; از پایتون ۳٫۸ به بعد می‌توانید از نحو متداول f-string مانند `f'{some_var=}'` برای اشکال‌زدایی سریع استفاده کنید. مثال,
    ```py
    >>> some_string = "wtfpython"
    >>> f'{some_string=}'
    "some_string='wtfpython'"
    ``` 

* &#x202b; پایتون برای ذخیره‌سازی متغیرهای محلی در توابع از ۲ بایت استفاده می‌کند. از نظر تئوری، این به معنای امکان تعریف حداکثر ۶۵۵۳۶ متغیر در یک تابع است. با این حال، پایتون راهکار مفیدی ارائه می‌کند که می‌توان با استفاده از آن بیش از ۲^۱۶ نام متغیر را ذخیره کرد. کد زیر نشان می‌دهد وقتی بیش از ۶۵۵۳۶ متغیر محلی تعریف شود، در پشته (stack) چه اتفاقی رخ می‌دهد (هشدار: این کد تقریباً ۲^۱۸ خط متن چاپ می‌کند، بنابراین آماده باشید!):
     
     ```py
     import dis
    exec("""
    def f():
        """ + """
        """.join(["X" + str(x) + "=" + str(x) for x in range(65539)]))

    f()

    print(dis.dis(f))
    ```
     
* &#x202b; چندین رشته (Thread) در پایتون، کدِ *پایتونی* شما را به‌صورت همزمان اجرا نمی‌کنند (بله، درست شنیدید!). شاید به نظر برسد که ایجاد چندین رشته و اجرای همزمان آن‌ها منطقی است، اما به دلیل وجود [قفل مفسر سراسری (GIL)](https://wiki.python.org/moin/GlobalInterpreterLock) در پایتون، تمام کاری که انجام می‌دهید این است که رشته‌هایتان به‌نوبت روی یک هسته اجرا می‌شوند. رشته‌ها در پایتون برای وظایفی مناسب هستند که عملیات I/O دارند، اما برای رسیدن به موازی‌سازی واقعی در وظایف پردازشی سنگین (CPU-bound)، بهتر است از ماژول [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) در پایتون استفاده کنید.

* &#x202b; گاهی اوقات، متد `print` ممکن است مقادیر را فوراً چاپ نکند. برای مثال،

     ```py
     # File some_file.py
     import time
     
     print("wtfpython", end="_")
     time.sleep(3)
     ```

     &#x202b; این کد عبارت `wtfpython` را به دلیل آرگومان `end` پس از ۳ ثانیه چاپ می‌کند؛ چرا که بافر خروجی تنها پس از رسیدن به کاراکتر `\n` یا در زمان اتمام اجرای برنامه تخلیه می‌شود. برای تخلیه‌ی اجباری بافر می‌توانید از آرگومان `flush=True` استفاده کنید.

* &#x202b; برش لیست‌ها (List slicing) با اندیس‌های خارج از محدوده، خطایی ایجاد نمی‌کند.
  ```py
  >>> some_list = [1, 2, 3, 4, 5]
  >>> some_list[111:]
  []
  ```

* &#x202b; برش زدن (slicing) یک شئ قابل پیمایش (iterable) همیشه یک شئ جدید ایجاد نمی‌کند. به‌عنوان مثال،
    ```py
    >>> some_str = "wtfpython"
    >>> some_list = ['w', 't', 'f', 'p', 'y', 't', 'h', 'o', 'n']
    >>> some_list is some_list[:] # False expected because a new object is created.
    False
    >>> some_str is some_str[:] # True because strings are immutable, so making a new object is of not much use.
    True
    ```

* &#x202b; در پایتون ۳، فراخوانی `int('١٢٣٤٥٦٧٨٩')` مقدار `123456789` را برمی‌گرداند. در پایتون، نویسه‌های ده‌دهی (Decimal characters) شامل تمام ارقامی هستند که می‌توانند برای تشکیل اعداد در مبنای ده استفاده شوند؛ به‌عنوان مثال نویسه‌ی U+0660 که همان رقم صفر عربی-هندی است. [اینجا](https://chris.improbable.org/2014/8/25/adventures-in-unicode-digits/) داستان جالبی درباره این رفتار پایتون آمده است.

* &#x202b; از پایتون ۳ به بعد، می‌توانید برای افزایش خوانایی، اعداد را با استفاده از زیرخط (`_`) جدا کنید.

     ```py
     >>> six_million = 6_000_000
     >>> six_million
     6000000
     >>> hex_address = 0xF00D_CAFE
     >>> hex_address
     4027435774
     ```

* &#x202b; عبارت `'abc'.count('') == 4` مقدار `True` برمی‌گرداند. در اینجا یک پیاده‌سازی تقریبی از متد `count` آورده شده که این موضوع را شفاف‌تر می‌کند:
  ```py
  def count(s, sub):
      result = 0
      for i in range(len(s) + 1 - len(sub)):
          result += (s[i:i + len(sub)] == sub)
      return result
  ```
&#x202b;  این رفتار به این دلیل است که زیررشته‌ی خالی (`''`) با برش‌هایی (slices) به طول صفر در رشته‌ی اصلی مطابقت پیدا می‌کند.

---
---

# &#x202b; مشارکت

&#x202b;چند روشی که می‌توانید در wtfpython مشارکت داشته باشید:

- &#x202b; پیشنهاد مثال‌های جدید
- &#x202b; کمک به ترجمه (به [مشکلات برچسب ترجمه](https://github.com/satwikkansal/wtfpython/issues?q=is%3Aissue+is%3Aopen+label%3Atranslation) مراجعه کنید)
- &#x202b; اصلاحات جزئی مثل اشاره به تکه‌کدهای قدیمی، اشتباهات تایپی، خطاهای قالب‌بندی و غیره.
- &#x202b; شناسایی نواقص (مانند توضیحات ناکافی، مثال‌های تکراری و ...)
- &#x202b; هر پیشنهاد خلاقانه‌ای برای مفیدتر و جذاب‌تر شدن این پروژه

&#x202b; برای اطلاعات بیشتر [CONTRIBUTING.md](/CONTRIBUTING.md) را مشاهده کنید. برای بحث درباره موارد مختلف می‌توانید یک [مشکل جدید](https://github.com/satwikkansal/wtfpython/issues/new) ایجاد کنید.

&#x202b; نکته: لطفاً برای درخواست بک‌لینک (backlink) تماس نگیرید. هیچ لینکی اضافه نمی‌شود مگر اینکه ارتباط بسیار زیادی با پروژه داشته باشد.

# &#x202b; تقدیر و تشکر

&#x202b; ایده و طراحی این مجموعه ابتدا از پروژه عالی [wtfjs](https://github.com/denysdovhan/wtfjs) توسط Denys Dovhan الهام گرفته شد. حمایت فوق‌العاده‌ جامعه پایتون باعث شد پروژه به شکل امروزی خود درآید.


#### &#x202b; چند لینک جالب!
* https://www.youtube.com/watch?v=sH4XF6pKKmk
* https://www.reddit.com/r/Python/comments/3cu6ej/what_are_some_wtf_things_about_python
* https://sopython.com/wiki/Common_Gotchas_In_Python
* https://stackoverflow.com/questions/530530/python-2-x-gotchas-and-landmines
* https://stackoverflow.com/questions/1011431/common-pitfalls-in-python
* https://www.python.org/doc/humor/
* https://github.com/cosmologicon/pywat#the-undocumented-converse-implication-operator
* https://github.com/wemake-services/wemake-python-styleguide/search?q=wtfpython&type=Issues
* WFTPython discussion threads on [Hacker News](https://news.ycombinator.com/item?id=21862073) and [Reddit](https://www.reddit.com/r/programming/comments/edsh3q/what_the_fck_python_30_exploring_and/).

# &#x202b; 🎓 مجوز

[![WTFPL 2.0][license-image]][license-url]

&copy; [Satwik Kansal](https://satwikkansal.xyz)

[license-url]: http://www.wtfpl.net
[license-image]: https://img.shields.io/badge/License-WTFPL%202.0-lightgrey.svg?style=flat-square

## &#x202b; دوستانتان را هم شگفت‌زده کنید!

&#x202b; اگر از wtfpython خوشتان آمد، می‌توانید با این لینک‌های سریع آن را با دوستانتان به اشتراک بگذارید:

&#x202b; [توییتر](https://twitter.com/intent/tweet?url=https://github.com/satwikkansal/wtfpython&text=If%20you%20really%20think%20you%20know%20Python,%20think%20once%20more!%20Check%20out%20wtfpython&hashtags=python,wtfpython) | [لینکدین](https://www.linkedin.com/shareArticle?url=https://github.com/satwikkansal&title=What%20the%20f*ck%20Python!&summary=If%20you%20really%20thing%20you%20know%20Python,%20think%20once%20more!) | [فیسبوک](https://www.facebook.com/dialog/share?app_id=536779657179021&display=page&href=https%3A%2F%2Fgithub.com%2Fsatwikkansal%2Fwtfpython&quote=If%20you%20really%20think%20you%20know%20Python%2C%20think%20once%20more!)


## &#x202b; آیا به یک نسخه pdf نیاز دارید؟


&#x202b; من چند درخواست برای نسخه PDF (و epub) کتاب wtfpython دریافت کرده‌ام. برای دریافت این نسخه‌ها به محض آماده شدن، می‌توانید اطلاعات خود را [اینجا](https://form.jotform.com/221593245656057) وارد کنید.

&#x202b; **همین بود دوستان!**  برای دریافت مطالب آینده مشابه این، می‌توانید ایمیل خود را [اینجا](https://form.jotform.com/221593598380062) اضافه کنید.
