#!/usr/bin/env python
# -*- coding:utf-8 -*-

#   Author  :   lizhang
#   E-mail  :   lizhang@360.cn
#   Date    :   15/09/07 14:40:46
#   Desc    :   个人常用工具


import sys
import re
import json
from math import log
from operator import itemgetter
from collections import defaultdict as ddict


def cos_similarity(td, cd):
    '''计算两个(字典)集合的余弦相似度'''
    comm = set(cd.iterkeys()) & set(td.iterkeys())
    comm_sum = 0.0
    t_mod = 0.0
    for term in comm:
        comm_sum += td[term] * cd[term]

    t_mod = sum([i**2 for i in td.itervalues()]) **0.5 + 0.00001
    c_mod = sum([i**2 for i in cd.itervalues()]) **0.5 + 0.00001

    return comm_sum / (t_mod * c_mod)


def print_dict(d, top=20):
    for k, v in sorted(d.iteritems(), key=itemgetter(1), reverse=True)[:top]:
        print '%s:%s' % (k.encode('utf-8', 'ignore'), v),
    print ''


def stdin_reader(has_flag=False):
    '''
    pipeline行处理工具:
        has_flag(False):
            True:   输出读入行的每个域，并标识是否是当前key的最后一行
            False:  仅输出读入行的每个域
    '''
    last_items = False
    items = False
    for line in sys.stdin:
        items = map(lambda x:x.strip(), line.split('\t'))
        if len(items) == 1 and items[0] == '':  # 过滤空行
            continue
        if not has_flag:
            yield items
        else:
            if last_items:
                yield last_items, last_items[0] != items[0]
            last_items = items
    else:
        if has_flag and items:
            yield items, True


if __name__ == '__main__':
    for i in stdin_reader(True):
        print i


