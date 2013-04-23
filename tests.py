# -*- coding: utf-8 -*-

from unicode_tr import unicode_tr
from unicode_tr.extras import slugify

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

    TITLE_CASES = [
        {"phrase": u"ısparta", "title": u"Isparta"},
        {"phrase": u"ısparta istanbul", "title": u"Isparta İstanbul"},
        {"phrase": u"İstanbul", "title": u"İstanbul"},
        {"phrase": u"çarşı timu", "title": u"Çarşı Timu"},
        {"phrase": u"Ğaaa ÇEŞİL", "title": u"Ğaaa Çeşil"},
        {"phrase": u"ŞamaTa ısparta istanbul", "title": u"Şamata Isparta İstanbul"},
    ]

    SLUG_CASES = [
        {"phrase": "Türkçe", "slug": "turkce"},
        {"phrase": "Diyarbakır", "slug": "diyarbakir"},
        {"phrase": "Yeni başlayanlar için yalnızlık", "slug": "yeni-baslayanlar-icin-yalnizlik"},
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

    def test_title(self):
        for case in self.TITLE_CASES:
            phrase = unicode_tr(case.get("phrase"))
            self.assertEquals(phrase.title(), case.get("title"))

    def test_slugify(self):
        for case in self.SLUG_CASES:
            self.assertEquals(slugify(case.get("phrase")), case.get("slug"))


if __name__ == '__main__':
    unittest.main()
