# -*- coding: utf-8 -*-
import re
from decimal import Decimal, ROUND_DOWN
from stx import Stack


class Calculator(object):

    """
    科学计算器对象(注册的公式字符串必须如下:"{{a}} + {{b}}"
    参数必须为字母,数字或下划线组成的python标准字符串)
    """

    re_param = re.compile(r'\{{2}\s*([0-9a-zA-Z\_]+?)\s*\}{2}')

    split_param = re.compile(r'[\{{2}\}{2}\s*]')

    def __init__(self, expression):
        self.exp_params = tuple(self.re_param.findall(expression))
        self.exp = expression
        self._exp_list = list()
        self._validate()
        self._postfix_list = self._convert2postfix_exp()

    def _validate(self):
        exp_lst = list()
        # 如果第一个字符是运算符, 在最前面增加一个0
        if self.exp[0] in ["-", "+"]:
            exp_lst.append("0")
        exp_lst.extend(self.split_param.split(self.exp))
        exp_lst = filter(lambda x: x != "" and x != " ", exp_lst)
        for v in exp_lst:
            if v in self.exp_params or self._is_operators(v) or self._is_bracket(v):
                self._exp_list.append(v)
            else:
                num = ""
                v = list(v)
                while len(v) > 0:
                    i = v.pop(0)
                    j = v[0] if len(v) > 0 else ""
                    if self._is_num(i):
                        num += i
                        if not self._is_num(j):
                            self._exp_list.append(num)
                            num = ""
                    elif self._is_bracket(i) or self._is_operators(i):
                        self._exp_list.append(i)
                    else:
                        continue

    def _convert2postfix_exp(self):
        """
        Convert the infix expression to a postfix expression
        :return: the converted expression
        """
        postfix_list = list()
        stk = Stack()
        for x in self._exp_list:
            if x in self.exp_params or self._is_num(x):
                postfix_list.append(x)
            elif self._is_operators(x):
                tp = stk.top()
                if tp and tp != '(':
                    x_pri = self._get_priority(x)
                    tp_pri = self._get_priority(tp)
                    if x_pri > tp_pri:
                        stk.push(x)
                    else:
                        # 弹出操作符,直到出现优先级更低的为止
                        while stk.top() and stk.top() != '(':
                            if self._get_priority(stk.top()) >= x_pri:
                                postfix_list.append(stk.pop())
                            else:
                                break
                        stk.push(x)
                else:
                    stk.push(x)
            elif self._is_bracket(x):
                if x == '(':
                    stk.push(x)
                else:
                    while stk.top() and stk.top() != '(':
                        postfix_list.append(stk.pop())
                    stk.pop()
        while stk.top():
            postfix_list.append(stk.pop())
        return postfix_list

    def cal(self, params):
        """计算费用的值"""
        return self._calc_postfix_exp(params)

    def _calc_postfix_exp(self, param_vals=None, post_exp=None):
        """
        Get the result from a converted postfix expression
        e.g: a b c * +
        :param param_vals: 公式模板中参数的值
        :param post_exp: 自定义的后缀表达式(空格分开)
        """
        stk = Stack()
        postfix_list = self._postfix_list if post_exp is None else list(post_exp)
        for x in postfix_list:
            if self._is_operators(x):
                # pop two top numbers in the stack
                r = self._get_result(stk.pop(), stk.pop(), x, param_vals)
                if r is None:
                    return None
                else:
                    stk.push(r)
            elif x in self.exp_params or self._is_num(x):
                # push the converted number to the stack
                stk.push(x)
            else:
                raise ValueError("unexpected param!")
        result = stk.pop()
        return Decimal(str(param_vals.get(result, '0'))) if result in self.exp_params else result

    def _get_result(self, op_2, op_1, operator, params_dict=None):
        """
        params_dict:模板参数
        """
        op_2 = Decimal(str(params_dict.get(op_2, '0'))) if op_2 in self.exp_params else Decimal(str(op_2))
        op_1 = Decimal(str(params_dict.get(op_1, '0'))) if op_1 in self.exp_params else Decimal(str(op_1))
        result = None
        if operator == '+':
            result = op_1 + op_2
        elif operator == '-':
            result = op_1 - op_2
        elif operator == '*':
            result = op_1 * op_2
        elif operator == '/':
            if op_2 != 0:
                result = op_1 / op_2
            else:
                raise ValueError("Error:{}: divisor cannot be zero, params:{}".format(self.exp, params_dict))
        return result.quantize(Decimal('.01'), rounding=ROUND_DOWN) if isinstance(result, Decimal) else result


    @staticmethod
    def _is_operators(x):
        return x in ['+', '-', '*', '/']

    @staticmethod
    def _is_bracket(x):
        return x in ['(', ')']

    @staticmethod
    def _is_num(x):
        if len(x):
            for i in x:
                if i not in "0123456789.":
                    return False
            return True
        else:
            return False

    @staticmethod
    def _get_priority(op):
        if op in ['+', '-']:
            return 0
        elif op in ['*', '/']:
            return 1
        elif op in ['(', ')']:
            return 2
        else:
            raise ValueError("unexpected param")

