# -*- coding: utf8 -*-

import unicodedata
import re


def slugify(value):
    """
    django.utils.text.slugify
    patched for ı and İ chars.
    """
    if not isinstance(value, unicode):
        value = unicode(value, 'utf8')

    value = value.replace(u'\u0131', 'i')
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()

    return re.sub('[-\s]+', '-', value)

