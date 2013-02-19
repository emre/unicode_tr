# -*- coding: utf8 -*-
import re

class unicode_tr(unicode):
    CHARMAP = {
        "to_upper": {
            u"ı": u"I",
            u"i": u"İ",
        },
        "to_lower": {
            u"I": u"ı",
            u"İ": u"i",
        }
    }

    def __charmap_handler(self, target):
        for key, value in target:
            text = self.text.replace(key, value)
        return text

    def lower(self):
        for key, value in self.CHARMAP.get("to_lower").items():
            self = self.replace(key, value)

        return self.lower()

    def upper(self):
        for key, value in self.CHARMAP.get("to_upper").items():
            self = self.replace(key, value)

        return self.upper()

    def capitalize(self):
        first, rest = self[0], self[1:]
        for key, value in self.CHARMAP.get("to_upper").items():
            first = first.replace(key, value)

        return (first + rest).capitalize()
