class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def symmetricTree(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        def check(p_node, q_node):
            if p_node is None and q_node is None:
                return True
            if p_node is None:
                return False
            if q_node is None:
                return False 
            if p_node.val == q_node.val:
                return check(p_node.left, q_node.right) and check(p_node.right, q_node.left)
            return False
        return check(root.left, root.right)

if __name__ == "__main__":
    solution = Solution()
    assert solution.symmetricTree(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))) == True
    assert solution.symmetricTree(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))) == False
    assert solution.symmetricTree(TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(4)))) == False
    print('All tests passed!')
