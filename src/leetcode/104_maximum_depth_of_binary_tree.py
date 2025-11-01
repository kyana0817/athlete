class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maximumDepthOfBinaryTree(self, root: list[int]) -> list[int]:
        def depth(root, dep):
            if root is None: return dep
            ldep = depth(root.left, dep+1)
            rdep = depth(root.right, dep+1)
            if ldep > rdep: return ldep
            return rdep

        return depth(root, 0)
    
if __name__ == "__main__":
    solution = Solution()
    assert solution.maximumDepthOfBinaryTree([3,9,20,null,null,15,7]) == 3
    assert solution.maximumDepthOfBinaryTree([1,null,2]) == 2
    print('All tests passed!')
