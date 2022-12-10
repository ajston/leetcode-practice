# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:32:13 2021

@author: T14
"""

from collections import defaultdict

def find_palindrome(s):
    char_count = defaultdict(int)
    
    for c in s:
        char_count[c] += 1
    
    odd_char = ""
    palindrome = ""
    
    for c, cnt in char_count.items():
        if cnt %2 == 0:
            palindrome += c * (cnt//2)
        elif not odd_char:
            odd_char = c
            palindrome += c * (cnt//2)
        else:
            return None
    return palindrome + odd_char + palindrome[::-1]

print(find_palindrome('mommok'))
#momom

print(find_palindrome('qqaaao'))
#None