# -*- coding: utf8 -*-

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


    def title(self):
        return " ".join(map(lambda x: unicode_tr(x).capitalize(), self.split()))
