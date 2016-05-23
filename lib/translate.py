# -*- coding: utf-8 -*-

from letters import letters

def translate(text):
    result = ''
    for char in text:
        result += letters[char]
    return result
