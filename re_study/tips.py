# RE doc:
# https://docs.python.org/3/library/re.html

def raw_string_notation():
    """ 
    Regular expressions use the backslash character ('\') to indicate special forms or to allow 
    special characters to be used without invoking their special meaning. This collides with 
    Python’s usage of the same character for the same purpose in string literals; for example,
    to match a literal backslash, one might have to write '\\\\' as the pattern string, 
    because the regular expression must be \\, and each backslash must be expressed as \\ 
    inside a regular Python string literal. Also, please note that any invalid escape sequences 
    in Python’s usage of the backslash in string literals now generate a DeprecationWarning and 
    in the future this will become a SyntaxError. This behaviour will happen even if it is a 
    valid escape sequence for a regular expression.

    The solution is to use Python’s raw string notation for regular expression patterns; 
    backslashes are not handled in any special way in a string literal prefixed with 'r'. 
    So r"\n" is a two-character string containing '\' and 'n', while "\n" is a one-character 
    string containing a newline.
    """
    string2 = '\n'
    print(string2)
    print(len(string2))

    string = r'\n'
    print(string)
    print(len(string))
# raw_string_notation()

def special_characters_in_py():
    print(r"\n: ")
    print("1\n2")

    print(r"\t: ")
    print("1\t2")

    print(r"\r: ")
    print("1\r2")
    
    print(r"\f: ")
    print("1\f2")

    print(r"\v: ")
    print("1\n2")
# special_characters_in_py()


# Match objects always have a boolean value of True. 
# Since match() and search() return None when there is no match, 
# you can test whether there was a match with a simple if statement:
"""
match = re.search(pattern, string)
if match:
    process(match)
"""
# https://docs.python.org/3/library/re.html#match-objects