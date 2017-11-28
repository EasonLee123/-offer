# 通过树结构深刻理解Recursive（递归）思想
# the order of Recursive call:类似深度搜索模式（栈结构），先进后出 

class TreeNode:
        # TreeNode data structure
        def __init__(self, x = None):
                self.value = x
                self.left = None
                self.right = None


class Solution:
        # for return pre,in,post order as a list, create a empty list attribute as initial function.
        def __init__(self):
                self.L = [ ]
        
        # pass the pre and in order to the function
        def rebuild_tree(self, pre, mid):
                # make sure pre and mid are not none
                if not pre and not mid:
                        return None

                # define root as TreeNode
                root = TreeNode(pre[0])     #   root.value = pre[0], wrong definition, need to create "TreeNode" DS first. 
                i = mid.index(pre[0])
                root.left = self.rebuild_tree(pre[1:i+1],mid[:i])        # root.left = rebuild_tree(pre[1:i+1],mid[:i])   wrong call for function
                root.right = self.rebuild_tree(pre[i+1:],mid[i+1:])  # root.right = rebuild_tree(pre[i+1:],mid[i+1:])  wrong call for function

                # return the root of built_tree
                return root

        # Then we need try to print the tree by level
        def PrintTreeAtLevel(self, RootNode, level):
                if not RootNode:
                        return None
                        

                if level == 1:
                        print(RootNode.value)

                self.PrintTreeAtLevel(RootNode.left, level - 1)
                self.PrintTreeAtLevel(RootNode.right, level - 1)


        # then we need to get the level of the tree
        def GetTreelevel(self, TreeNode):
                if not TreeNode:
                        return 0  # KEYPOINT.....can not return none, will get error:
                                        # not supported between instances of 'NoneType' and 'NoneType

                leftdepth = self.GetTreelevel(TreeNode.left)
                rightdepth = self.GetTreelevel(TreeNode.right)
                #print(rightdepth)       # test to understand the calling order of "Recursive"递归
                #print(leftdepth)
                return max(leftdepth, rightdepth) +1


        # now we can print the tree by just pass the root
        def PrintTree(self, TreeNode):
                if not TreeNode:
                        return None

                totallevel = self.GetTreelevel(TreeNode)     # self.PrintTreeByLevel(TreeNode, totoallevel)
                print("Tree Level is {}".format(totallevel))
                for tree_level in range(1, totallevel + 1):      # From 1 to(include) totallevel, do the print
                        self.PrintTreeAtLevel(TreeNode, tree_level)
                        print()




pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
test = Solution()
newTree = test.rebuild_tree(pre, tin)

print(test.PrintTree(newTree))
