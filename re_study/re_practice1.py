# https://www.cnblogs.com/think-and-do/p/6414135.html
# https://www.w3resource.com/python-exercises/re/
import re

def matching_a_link():
    link = "[使徒信经释义: http://mp.weixin.qq.com/s?__biz=MzIzNjc4NTUwMg==&amp;mid=2247486088&amp;idx=2&amp;sn=66befcbf130dfd685a974a6dcae6f441&amp;chksm=e8d3d0b9dfa459af56c1042b7693ee9f7eb311d963c0249f359008811f2b3c43d618de5a4725&amp;mpshare=1&amp;scene=1&amp;srcid=0309DMXtFxGaQGAz2GIoUXGz&amp;sharer_sharetime=1615267386010&amp;sharer_shareid=1a2bdb34aa311a7cce8bd838614762e8#rd]"
    Link = re.compile(r'\[(.*?): ?(https?.*)\]')
    match = Link.match(link)
    print(match)
    print(match.group(1), match.group(2))
matching_a_link()
