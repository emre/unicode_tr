unicode_tr
==========

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

```python
# -*- coding: utf-8 -*-
from unicode_tr import unicode_tr

text_true = unicode_tr(u"istanbul")
text_wrong = unicode(u"istanbul")

# string.upper
print text_true.upper(), text_wrong.upper()
# output -> İSTANBUL ISTANBUL

# string.capitalize
print text_true.capitalize(), text_wrong.capitalize()
# output -> İstanbul Istanbul

# string.lower
text_true  = unicode_tr(u"ÇINAR")
text_false = unicode(u"ÇINAR")

print text_true.lower(), text_false.lower()
# output -> çınar çinar

# string.title
text_true  = unicode_tr(u"izmir istanbul")
text_false = unicode(u"izmir istanbul")

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




