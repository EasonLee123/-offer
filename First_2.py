class Solution:
	def Find(self, array, target):
		# array 二维，很关键
		found = False
		for index in range(len(array)):
			if target in array[index]:
				found = True
		return found

x = Solution()
my_list = [[1,2,3], [8,10,11]]
target = 9
print(x.Find(target = target, array = my_list))

# two keypoints:
# 1. 2D array
# 2. in keyword
