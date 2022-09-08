# Regular Expressions
# https://docs.python.org/3/library/re.html#regular-expression-syntax
# https://docs.python.org/3/howto/regex.html#regex-howto
# https://www.w3schools.com/python/python_regex.asp

import re

def character_class():
    abc = re.compile("[abc]")
    abc2 = re.compile("[a-c]")
    non_abc = re.compile("[^a-c]")
    string = "abcdefghijkABC ab scv"
    print(abc.findall(string))
    print(non_abc.findall(string))
# character_class()

def repeating_characters_1():
    string = 'ct'
    string2 = 'cat'
    string3 = 'caaaaaaat'
    p = re.compile("ca*t")
    print(p.match(string))
    print(p.match(string2))
    print(p.match(string3))
# repeating_characters_1()

def repeating_characters_2():
    string = 'ct'
    string2 = 'cat'
    string3 = 'caaaaaaat'
    p = re.compile("ca+t")
    print(p.match(string))
    print(p.match(string2))
    print(p.match(string3))
# repeating_characters_2()

def repeating_characters_3():
    string = 'homebrew'
    string2 = 'home-brew'
    p = re.compile("home-?brew")
    print(p.match(string))
    print(p.match(string2))
# repeating_characters_3()

def repeating_characters_4():
    string = 'ab'
    string2 = 'a/b'
    string3 = 'a//b'
    string4 = 'a///b'
    string5 = 'a////b'
    p = re.compile(r"a/{1,3}b")
    print(p.match(string))
    print(p.match(string2))
    print(p.match(string3))
    print(p.match(string4))
    print(p.match(string5))
# repeating_characters_4()

def digits():
    time = "19:21"
    digit = re.compile(r"\d\d:\d\d")
    print(digit.match(time))
# digits()

def module_methods_finditer():
    txt = "The rain in Spain"
    x = re.finditer(r"ain", txt)
    for item in x:
        print(item)
# module_methods_finditer()

def match_object():
    """
    .span() returns a tuple containing the start-, and end positions of the match.
    .string returns the string passed into the function
    .group() returns the part of the string where there was a match
    """
    txt = "The rain in Spain"
    pattern = re.compile(r"\bS\w+")
    x = pattern.search(txt)
    # x = re.search(r'\bS\w+')
    print(x)
    print(x.span())     # Return a tuple containing the (start, end) positions of the match
    print(x.start())    # Return the starting position of the match
    print(x.end())      # Return the ending position of the match
    print(x.string)     # Original string passed to the pattern
    print(x.group())    # Return the string matched by the RE
# match_object()

def pattern_methods():
    txt = "This module provides regular expression matching operations similar to those found in Perl."
    pattern = re.compile(r'\bm\w+')
    x1 = pattern.match(txt)
    x2 = pattern.search(txt)
    x3 = pattern.findall(txt)
    x4 = pattern.finditer(txt)

    print(x1)
    print(x2)
    print(x3)
    print(x4)
    for item in x4:
        print(item)
# pattern_methods()

def some_flags():
    # VERBOSE
    charref = re.compile(r"""
    &[#]                # Start of a numeric entity reference
    (
        0[0-7]+         # Octal form
    | [0-9]+            # Decimal form
    | x[0-9a-fA-F]+     # Hexadecimal form
    )
    ;                   # Trailing semicolon
    """, re.VERBOSE)
# some_flags()

def group():
    p = re.compile('(a(b)c)d')
    m = p.match('abcd')
    print(1, m.group(0))
    print(2, m.group(1))
    print(3, m.group(2))
    print(4, m.group(2,1,2,0))
    print(5, m.groups())
# group()

def group2():
    # You can figure out how the groups ordered through this function.
    p = re.compile('a(b(f)c)(d(e))')
    m = p.match('abfcde')
    print(m.group(0, 1, 2, 3, 4))
    print(p.groups)
    print(m.groups())
# group2()

def group3():
    """ 
    Backreferences in a pattern allow you to specify that the contents of an earlier capturing 
    group must also be found at the current location in the string. For example, \1 will succeed 
    if the exact contents of group 1 can be found at the current position, and fails otherwise. 
    Remember that Python’s string literals also use a backslash followed by numbers to allow 
    including arbitrary characters in a string, so be sure to use a raw string when incorporating 
    backreferences in a RE.

    For example, the following RE detects doubled words in a string.
    """
    p = re.compile(r'\b(\w+)\s+\1\b')
    print(p.search('Paris in the the spring').group())
# group3()

def non_capturing_group():
    # Reference link of Match.groups(): https://docs.python.org/3/library/re.html#re.Match.groups
    m = re.match("([abc])+", "abc")
    print(m.groups())
    print(m.group())
    print(m.group(1))
    # print(m.group(2))
    print("-----------------")

    m = re.match("(?:[abc])+", "abc")
    print(m.groups())
    print(m.group())
    # print(m.group(1))
# non_capturing_group()

def Lookahead_Assertions():
    # https://docs.python.org/3/howto/regex.html#lookahead-assertions
    # ???
    m = re.search(r'(?=exe)\d', 'exe5')
    print(m)

    m = re.search(r'.*[.](?!bat$|exe$)[^.]*$', 'oss.docx')
    print(m)
    m = re.search(r'.*[.](?!bat$|exe$)[^.]*$', 'oss.exe')
    print(m)
# Lookahead_Assertions()

# Sometimes, string methods is enough for you, and it's faster than re.
# https://docs.python.org/3/howto/regex.html#use-string-methods

