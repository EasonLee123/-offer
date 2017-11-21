# print out pre-order of a tree in a list
def print_pre_order(self, TreeNode):
        if not TreeNode:
                return None
        
        # print(TreeNode.value) 
        # for printing out as a list format instead of a series of number
        # change the simple print sentence to a if-statement to create a list and then return
        if TreeNode.value != None:
                self.L.append(TreeNode.value)
                
        self.print_pre_order(TreeNode.left)      
        self.print_pre_order(TreeNode.right)

        return self.L


# print out in-order of a tree in a list
def print_in_order(self, TreeNode):
        if not TreeNode:
                return None

        self.print_in_order(TreeNode.left)
        
        if TreeNode.value != None:
                self.L.append(TreeNode.value)

        self.print_in_order(TreeNode.right)

        return self.L

# print out post-order of a tree in a list
def print_post_order(self, TreeNode):
        if not TreeNode:
                return None

        self.print_post_order(TreeNode.left)
        self.print_post_order(TreeNode.right)

        if TreeNode.value != None:
                self.L.append(TreeNode.value)

        return self.L

# print(test.print_pre_order(newTree))
# print(test.print_in_order(newTree))
# print(test.print_post_order(newTree))