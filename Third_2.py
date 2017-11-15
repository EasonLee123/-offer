# create listnode data structure
class Listnode:
	def __init__(self, x = None):
		self.val = x
		self.next = None

# insert(index, obj) built-in function
class Solution:
        def printFromTailToHead(self, listnode):
                if listnode.val == None:
                        return 
                L = [ ]
                head = listnode
                while head:
                        L.insert(0,head.val)
                        head = head.next
                return L

# create list by listnode
node1 = Listnode(1)
node2 = Listnode(2)
node3 = Listnode(3)
node4 = Listnode(4)
node1.next = node2
node2.next = node3
node3.next = node4        

# test
x = Solution()
print(x.printFromTailToHead(node1))



