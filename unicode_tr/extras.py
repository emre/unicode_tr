# -*- coding: utf8 -*-

import unicodedata
import re

from . import __instance__


def slugify(value):
    """
    django.utils.text.slugify
    patched for ı and İ chars.
    """
    if not isinstance(value, __instance__):
        value = __instance__(value, 'utf8')

    value = value.replace(u'\u0131', 'i')
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()

    return re.sub('[-\s]+', '-', value)
