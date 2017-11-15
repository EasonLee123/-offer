class Solution:
    def printListFromTailToHead(self, listNode):
        i = -1          # subscript for list
        j = 0           # control loop
        while j<len(listNode):
            print(listNode[i])
            i -= 1
            j += 1


x = Solution()
my_list = [1, 2, 3, 4, 5]
x.printListFromTailToHead(my_list)

# Actually, this solution pass a list as the parameter instead of listnode
# so it is not eaxctly right.
# in Third_2 and Third_3, I will create a listnode data structure
# and pass the right listnode structure to the function.
