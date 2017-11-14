# -*- coding:utf-8 -*-
# 线性空间复杂度
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if s == None:
            return None
        if len(s) == 0:
            return ''
        result = ''
        for item in s:
            if item.isspace():
                result = result+'%20'
            else:
                result = result+item
        return result


x = Solution()
print(x.replaceSpace(" Hello "))
