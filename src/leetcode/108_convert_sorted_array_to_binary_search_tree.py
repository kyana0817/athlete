from queue import SimpleQueue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def convertSortedArrayToBinarySearchTree(self, nums: list[int]) -> list[int]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        def create_node(mn, mx):
            d = mx - mn
            idx = (mn + mx) // 2
            if d <= 0:
                return TreeNode(nums[idx])
            if d == 1:
                if idx == mn: 
                    return TreeNode(nums[idx], None, TreeNode(nums[mx]))
                else:
                    return TreeNode(nums[idx],TreeNode(nums[mn]))
                
            return TreeNode(nums[idx], create_node(mn, idx-1), create_node(idx+1, mx))
        
        return create_node(0, len(nums)-1)

if __name__ == "__main__":
    solution = Solution()
    assert solution.convertSortedArrayToBinarySearchTree([-10,-3,0,5,9]) == [0,-3,9,-10,None,5]
    assert solution.convertSortedArrayToBinarySearchTree([1,3]) == [3,1]
    print('All tests passed!')
