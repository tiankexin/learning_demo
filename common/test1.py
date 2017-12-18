class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        operator = '+'
        str_num = list(str(x))
        if not str_num[0].isdigit():
            operator = str_num[0]
            str_num = str_num[1:]
        str_num = sorted(str_num, reverse=True)
        final_list = [operator]+str_num
        result = int(''.join(final_list))
        if result > 2**32:
            return 0
        else:
            return result
s = Solution()
s.reverse(120)




class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        stx = list()
        str_num = str(x)
        if x < 0:
            return False
        middle = None
        lenth = len(str_num)
        if lenth == 1:
            return True
        if lenth>1 and lenth % 2:
            middle = (lenth - 1)/2
        judge = middle if middle else lenth/2 - 1
        for k, v in enumerate(str_num):
            if middle and k==middle:
                continue
            if k <= judge:
                stx.append(v)
            else:
                if stx[-1] == v:
                    stx.pop(-1)
        if len(stx) != 0:
            return False
        else:
            return True
        