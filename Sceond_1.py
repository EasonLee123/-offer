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

# this solution is not perfect one:
# cause it will not show the right answer with the string case begining or ending up with space, like" Hello"
# we expect "%20Hello" coming out after the compilation, but we will only get "Hello"
# all of this is because split() function by default will split a string **inbetween** according to space.

# but anyway, it is pretty good to show the convertion between string and list.
