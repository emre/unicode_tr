# -*- coding: utf8 -*-

from unicode_tr import unicode_tr

import random
import unittest

class TestTurkishWords(unittest.TestCase):

    UPPER_CASES = [
        {"word": u"ığdır", "upper": u"IĞDIR"},
        {"word": u"ırmak", "upper": u"IRMAK"},
        {"word": u"timu", "upper": u"TİMU",}
    ]

    LOWER_CASES = [
        {"word": u"İstanbul", "lower": u"istanbul"},
        {"word": u"Irmak", "lower": u"ırmak"},
        {"word": u"ÇESİL", "lower": u"çesil"},
        {"word": u"Ğaaaa", "lower": u"ğaaaa"},
    ]

    CAPITALIZE_CASES = [
        {"word": u"çınar", "capitalize": u"Çınar"},
        {"word": u"şansal", "capitalize": u"Şansal"},
        {"word": u"istanbul", "capitalize": u"İstanbul",}
    ]

    def test_upper(self):
        for case in self.UPPER_CASES:
            word = unicode_tr(case.get("word"))
            self.assertEquals(word.upper(), case.get("upper"))

    def test_lower(self):
        for case in self.LOWER_CASES:
            word = unicode_tr(case.get("word"))
            self.assertEquals(word.lower(), case.get("lower"))

    def test_capitalize(self):
        for case in self.CAPITALIZE_CASES:
            word = unicode_tr(case.get("word"))
            self.assertEquals(word.capitalize(), case.get("capitalize"))

if __name__ == '__main__':
    unittest.main()

