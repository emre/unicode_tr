unicode_tr
==========

[![Build Status](https://drone.io/github.com/emre/unicode_tr/status.png)](https://drone.io/github.com/emre/unicode_tr/latest) &nbsp; <img src= "https://pypip.in/v/unicode_tr/badge.png"> &nbsp; <img src="https://pypip.in/d/unicode_tr/badge.png">


a python module to make unicode strings work as expected for turkish chars. solves the turkish "İ" problem.

lower(), upper(), capitalize() and title() methods are patched.

installation
==========

```
pip install unicode_tr
```
or if you like 90s:

```
easy_install unicode_tr
```

or add unicode_tr directory to the your path.

usage
============
Just import the module.
No need to refactor your unicode string by adding `unicode_tr` definition.

It simply monkey-patches builtin.unicode module.
Monkey-patched methods of unicode are:
- unicode.upper()
- unicode.lower()
- unicode.capitalize()
- unicode.title()

```python
# -*- coding: utf-8 -*-
import unicode_tr

text_true = u"istanbul"
text_wrong = u"istanbul"

# string.upper
print text_true.upper(), text_wrong.upper()
# output -> İSTANBUL ISTANBUL

# string.capitalize
print text_true.capitalize(), text_wrong.capitalize()
# output -> İstanbul Istanbul

# string.lower
text_true  = u"ÇINAR"
text_false = u"ÇINAR"

print text_true.lower(), text_false.lower()
# output -> çınar çinar

# string.title
text_true  = u"izmir istanbul"
text_false = u"izmir istanbul"

print text_true.title(), text_false.title()
# output -> İzmir İstanbul Izmir Istanbul


```

extras
============
*extras.slugify*

Turkish language supported slugify function.

> Converts to lowercase, removes non-word characters (alphanumerics and
> underscores) and converts spaces to hyphens. Also strips leading and
> trailing whitespace."

```
In [1]: from unicode_tr.extras import slugify

In [2]: slugify("türkçe")
Out[2]: u'turkce'

In [3]: slugify("diyarbakır")
Out[3]: u'diyarbakir'

```

Note: If you want to deasciify your text: <a href="https://github.com/emres/turkish-deasciifier">@emres/turkish-deasciifier</a>






[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/emre/unicode_tr/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

