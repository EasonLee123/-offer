class Listnode:
	def __init__(self, x = None):
		self.val = x 
		self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        L = []
        head = listNode
        while head:
            L.append(head.val)
            head = head.next
        L.reverse()
        return L

node1 = Listnode(6)
node2 = Listnode(7)
node3 = Listnode(8)
node4 = Listnode(9)
node1.next = node2
node2.next = node3
node3.next = node4


x=Solution()
print(x.printListFromTailToHead(node1))
