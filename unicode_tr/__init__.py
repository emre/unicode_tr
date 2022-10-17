# -*- coding: utf8 -*-

try:
    __instance__ = unicode
except:
    __instance__ = str


class unicode_tr(__instance__):
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

        return unicode_tr(getattr(__instance__, 'lower')(self))

    def upper(self):
        for key, value in self.CHARMAP.get("to_upper").items():
            self = self.replace(key, value)

        return unicode_tr(getattr(__instance__, 'upper')(self))

    def replace(self, *args, **kwargs):
        return unicode_tr(getattr(__instance__, 'replace')(self, args[0], args[1]))

    def capitalize(self):
        first, rest = self[0], self[1:]
        return unicode_tr(first).upper() + unicode_tr(rest).lower()

    def title(self):
        return " ".join(map(lambda x: unicode_tr(x).capitalize(), self.split())).title()
