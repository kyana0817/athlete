class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def check(p_node, q_node):
            if p_node is None and q_node is None:
                return True
            if p_node is None:
                return False
            if q_node is None:
                return False 
            if p_node.val == q_node.val:
                return check(p_node.left, q_node.left) and check(p_node.right, q_node.right)
            return False
        return check(p, q)


if __name__ == "__main__":
    solution = Solution()
    assert solution.sameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))) == True
    assert solution.sameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))) == False
    assert solution.sameTree(TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))) == False
    print('All tests passed!')
