#!/usr/bin/env python

import re, sys

def replace_dollar(content, s=r'$$\1$$'):
    dollar_pat = r"(?:^|(?<=\s))[$]([^\n]*?)(?<![\\])[$](?:$|(?=\s|[.,;\\]))"
    _dollar = re.compile(dollar_pat)
    _notdollar = re.compile(r"\\[$]")
    content = _dollar.sub(s, content)
    content = _notdollar.sub("$", content)
    return content

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    content = f.read()
    fout = open(sys.argv[1], 'w')
    fout.write(replace_dollar(content))


