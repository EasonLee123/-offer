class Solution:
	def replaceSpace(self, s):
		return s.replace(' ', '%20')


x = Solution()
print(x.replaceSpace("   World"))
