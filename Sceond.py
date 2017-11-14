class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if " " in s:
            my_list = s.split()
            ss = "%20".join(my_list)
            return ss
        else:
            print("there is no space in the s")


x = Solution()
print(x.replaceSpace("Something is wrong or right"))
