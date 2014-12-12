#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicode_tr
from unicode_tr.extras import slugify



UPPER_CASES = [
    {"word": u"ığdır", "upper": u"IĞDIR"},
    {"word": u"ırmak", "upper": u"IRMAK"},
    {"word": u"timu", "upper": u"TİMU",}
]

LOWER_CASES = [
    {"word": u"İstanbul", "lower": u"istanbul"},
    {"word": u"Irmak", "lower": u"ırmak"},
    {"word": u"ÇESİL", "lower": u"çesil"},
    {"word": u"AĞA", "lower": u"ağa"},
]

CAPITALIZE_CASES = [
    {"word": u"KADIKÖY", "capitalize": u"Kadıköy"},
    {"word": u"çınar", "capitalize": u"Çınar"},
    {"word": u"şansal", "capitalize": u"Şansal"},
    {"word": u"istanbul", "capitalize": u"İstanbul",}
]

TITLE_CASES = [
    {"phrase": u"ısparta", "title": u"Isparta"},
    {"phrase": u"ısparta istanbul", "title": u"Isparta İstanbul"},
    {"phrase": u"İstanbul", "title": u"İstanbul"},
    {"phrase": u"çarşı timu", "title": u"Çarşı Timu"},
    {"phrase": u"aĞa ÇEŞİL KADIKÖY", "title": u"Ağa Çeşil Kadıköy"},
    {"phrase": u"ŞamaTa ısparta istanbul", "title": u"Şamata Isparta İstanbul"},
]

SLUG_CASES = [
    {"phrase": "Türkçe", "slug": "turkce"},
    {"phrase": "Diyarbakır", "slug": "diyarbakir"},
    {"phrase": "Yeni başlayanlar için yalnızlık", "slug": "yeni-baslayanlar-icin-yalnizlik"},
]


def test_upper():
    for case in UPPER_CASES:
        word = case.get("word")
        assert(word.upper() == case.get("upper"))

def test_lower():
    for case in LOWER_CASES:
        word = case.get("word")
        assert(word.lower() == case.get("lower") )

def test_capitalize():
    for case in CAPITALIZE_CASES:
        word = case.get("word")
        assert(word.capitalize() ==  case.get("capitalize"))

def test_title():
    for case in TITLE_CASES:
        phrase = case.get("phrase")
        assert(phrase.title() == case.get("title"))

def test_slugify():
    for case in SLUG_CASES:
        assert(slugify(case.get("phrase")) == case.get("slug"))


if __name__ == '__main__':
    test_upper()
    test_lower()
    test_capitalize()
    test_title()
    test_slugify()
