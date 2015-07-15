# -*- coding: utf-8 -*-

NEGATIVES = [
    u"не",
    u"не-а",
    u"нет",
    u"никак"
]


def is_negative(text):
    return any(text.lower().startswith(neg) for neg in NEGATIVES)
