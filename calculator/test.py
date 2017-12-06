# -*- coding: utf-8 -*-
import re
from handler import Calculator

exp = "({{a0}} * {{b1 }} + {{d1}}) * {{c1}} +7"

print re.split(r'[\{\}\s]+', exp)

a = r'\{{2}\s*([0-9a-zA-Z\_]+?)\s*\}{2}'
obj = tuple(re.findall(a, exp))
print obj

print tuple([i.split("}}")[0].strip() for i in exp.split('{{')[1:]])

#
exp_list = list()
for i in exp.split("}}"):
    exp_list.extend([v.strip() for v in i.split("{{")])
print "aaaa", exp_list

#
b = r'[\{{2}\}{2}\s*]'
exp_list= re.split(b, exp)
print exp_list
exp_list = filter(lambda x: x != "" and x != " ", exp_list)
print exp_list

print "CCCCCCCCCCCCCC"
c =  Calculator(exp)
print c._exp_list
print c._postfix_list