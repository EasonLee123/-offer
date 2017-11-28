class Solution:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def queue_push(self,node):
		self.stack1.append(node)

	def queue_pop(self):
		if len(self.stack2) == 0 and len(self.stack1 == 0):
			print("Nothing to pop")

		elif len(self.stack2) == 0:
			while len(self.stack1):
				self.stack2.append(self.stack1.pop())  # pop() by default is pop(-1)

		return self.stack2.pop()

x = Solution()

x.queue_push(1)
x.queue_push(2)
x.queue_push(3)

print(x.queue_pop())

x.queue_push(4)

print(x.queue_pop())



		
