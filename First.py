    def Find(self, target, array):
        # write code here
        rownum = len(array)
        # print(rownum)                 testing purpose
        colnum = len(array[0])
        # print(colnum)                  testing purpose
        i = rownum -1
        j = 0
        while i>=0 and j<=colnum-1:
            if target>array[i][j]:
                j +=1
                # print("K")                testing purpose
            elif target<array[i][j]:
                i -=1
                # print("Q")                testing purpose
            else:
                return True
        return False


x = Solution()
array = [[1,2,3],[2,3,4]]
target = 1

print(x.Find(target, array))
