import re

def chinese_matching():
    txt = '张齐正'
    three_character = re.compile(r'...')
    m = three_character.match(txt)
    print(m.group())
# chinese_matching()

def empty_matching():
    txt1 = '   '
    txt2 = '  some words       '
    txt3 = '   \n   '

    empty_pattern = re.compile(r'^\s+$')
    result1 = empty_pattern.findall(txt1)
    result2 = empty_pattern.findall(txt2)
    result3 = empty_pattern.findall(txt3)

    print(result1)
    print(result2)
    print(result3)
    # print(txt3)
# empty_matching()

def Link_test():
    txt = '来自爱之光福音社的单曲《主你若纠察罪孽》:https://t3.kugou.com/wc/s/238cu2cxUV3 (@酷狗音乐)'
    Link = re.compile(r'https?')
    find = Link.findall(txt)
    match = Link.match(txt)
    search = Link.search(txt)
    if find:
        print('found', find)
    if match:
        print('matched', match)
    if search:
        print('search success', search)
Link_test()